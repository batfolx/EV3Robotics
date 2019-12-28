from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.button import Button
import time


def spin(cross: MediumMotor, speed=10):
    cross.on(speed=speed, block=False)


def stop_cross(cross: MediumMotor):
    cross.stop()


def detect(eyes: UltrasonicSensor) -> int:
    speed = 5
    distance = eyes.distance_centimeters
    if 10 <= distance < 30:
        speed = 85
    elif 30 <= distance < 40:
        speed = 60
    elif 40 <= distance < 50:
        speed = 40
    elif 50 <= distance < 60:
        speed = 30
    elif 60 <= distance < 70:
        speed = 20
    elif 70 <= distance < 80:
        speed = 10
    return speed


def bt_threat():
    button = Button()
    bridge_cross = MediumMotor(OUTPUT_A)
    eyes = UltrasonicSensor(INPUT_1)
    while True:
        speed = detect(eyes)
        if button.any():
            stop_cross(bridge_cross)
            break

        spin(bridge_cross, speed)
        time.sleep(1)


bt_threat()
