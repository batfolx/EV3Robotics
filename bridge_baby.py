from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.button import Button
import time


def detect(cross: MediumMotor, speed=10):
    cross.on(speed=speed, block=False)


def stop_cross(cross: MediumMotor):
    cross.stop()


def bt_threat():
    button = Button()
    bridge_cross = MediumMotor(OUTPUT_A)
    speed = 5
    while True:

        if button.any():
            break

        detect(bridge_cross, speed)
        if speed < 100:
            speed += 5

        time.sleep(1)


bt_threat()
