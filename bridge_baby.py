from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.button import Button
import time


def spin(cross: MediumMotor, speed=10):
    cross.on(speed=speed, block=False)


def stop_cross(cross: MediumMotor):
    cross.stop()


def stop_swivel(swivel: LargeMotor):
    swivel.stop()


def scan_right(swivel: LargeMotor):
    swivel.on_for_degrees(speed=15, degrees=35, block=True)


def scan_left(swivel: LargeMotor):
    swivel.on_for_degrees(speed=15, degrees=-35, block=True)


def lock_scan(swivel: LargeMotor):
    swivel.stop()


def detect(eyes: UltrasonicSensor) -> int:
    speed = False
    distance = eyes.distance_centimeters
    if 0 < distance < 30:
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
    swivel = LargeMotor(OUTPUT_B)
    eyes = UltrasonicSensor(INPUT_1)
    while True:
        if button.any():
            stop_cross(bridge_cross)
            break
        speed = detect(eyes)
        if speed:
            spin(bridge_cross, speed)
        else:
            scan_left(swivel)
            scan_right(swivel)

        time.sleep(0.25)


bt_threat()
