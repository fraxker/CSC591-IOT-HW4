import adafruit_bno08x
from board import SCL, SDA
from busio import I2C
from adafruit_bno08x.i2c import BNO08X_I2C
from pathlib import Path

PATH = Path("door")


if __name__ == "__main__":
    i2c = I2C(SCL, SDA, frequency=400000)
    bno = BNO08X_I2C(i2c)
    bno.enable_feature(adafruit_bno08x.BNO_REPORT_GAME_ROTATION_VECTOR)
    itr = int(input("Press enter the number of iteration you would like to train\n"))
    with PATH.open("a") as f:
        while itr > 0:
            input("Please close the door")
            game_quat_i, game_quat_j, game_quat_k, game_quat_real = bno.game_quaternion
            f_string = f"0 1:{game_quat_i} 2:{game_quat_j} 3:{game_quat_k} 4:{game_quat_real}\n"
            f.write(f_string)
            input("Please open the door")
            game_quat_i, game_quat_j, game_quat_k, game_quat_real = bno.game_quaternion
            f_string = f"q 1:{game_quat_i} 2:{game_quat_j} 3:{game_quat_k} 4:{game_quat_real}\n"
            f.write(f_string)
            itr -= 1