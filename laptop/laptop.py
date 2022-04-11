import paho.mqtt.client as paho
from datetime import datetime
import time

def on_message(client, userdata, message):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(message.topic, ": ", str(message.payload.decode("utf-8")), current_time, flush=True)

if __name__ == "__main__":
    client = paho.Client("laptop")
    client.username_pw_set(username="use-token-auth", password="(15*dkt(isrOBk8CUW")
    client.connect("rhasq4.messaging.internetofthings.ibmcloud.com")
    client.on_message=on_message
    client.subscribe("iot-2/evt/decision/fmt/str", qos=2)

    client.loop_start()
    while True:
        time.sleep(1)