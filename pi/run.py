import adafruit_bno08x
from board import SCL, SDA
from busio import I2C
from adafruit_bno08x.i2c import BNO08X_I2C
import paho.mqtt.client as paho
from libsvm.svmutil import svm_load_model, svm_predict
import time

decisions = {0: "Close", 1: "Open"}

if __name__ == "__main__":
    m = svm_load_model('door.model')
    i2c = I2C(SCL, SDA, frequency=400000)
    bno = BNO08X_I2C(i2c)
    bno.enable_feature(adafruit_bno08x.BNO_REPORT_GAME_ROTATION_VECTOR)
    bno.enable_feature(adafruit_bno08x.BNO_REPORT_STABILITY_CLASSIFIER)
    client = paho.Client("Pi")
    client.username_pw_set(username="use-token-auth", password="TfJjx?zJKHc?5e)yW9")
    client.connect("rhasq4.messaging.internetofthings.ibmcloud.com")
    client.loop_start()
    last_decision = "Close"
    try:
        while True:
            stable = bno.stability_classification
            if stable == "In motion":
                continue
            game_quat_i, game_quat_j, game_quat_k, game_quat_real = bno.game_quaternion
            p_label, _, _ = svm_predict([], [{1:game_quat_i, 2: game_quat_j, 3: game_quat_k, 4: game_quat_real}], m)
            decision = decisions[int(p_label[0])]
            if decision != last_decision:
                client.publish("iot-2/evt/decision/fmt/str", decision, qos=2)
                last_decision = decision
            time.sleep(1)
    except KeyboardInterrupt:
        client.loop_stop()
        pass