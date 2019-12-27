from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.button import Button


def check_distance(eyes: UltrasonicSensor):
    return eyes.distance_centimeters < 7.5


def forward(left_motor: LargeMotor, right_motor: LargeMotor, seconds=0.5, speed=50):
    left_motor.on_for_seconds(speed=speed, seconds=seconds, brake=True, block=False)
    right_motor.on_for_seconds(speed=speed, seconds=seconds, brake=True, block=False)


def stop(left_motor: LargeMotor, right_motor: LargeMotor):
    left_motor.off()
    right_motor.off()


def backward(left_motor: LargeMotor, right_motor: LargeMotor, seconds=0.5, speed=50):
    left_motor.on_for_seconds(speed=-speed, seconds=seconds, brake=True, block=False)
    right_motor.on_for_seconds(speed=-speed, seconds=seconds, brake=True, block=True)


def knock_o_matic(bulldozer: MediumMotor, seconds=3, speed=75):
    bulldozer.on_for_seconds(speed=speed, seconds=seconds, brake=False, block=False)


def left_and_right(left_motor: LargeMotor, right_motor: LargeMotor, seconds=0.5, speed=50):
    left_motor.on_for_seconds(speed=speed, seconds=seconds, block=False)
    right_motor.on_for_seconds(speed=speed / 2, seconds=seconds, block=True)
    left_motor.on_for_seconds(speed=speed / 2, seconds=seconds, block=False)
    right_motor.on_for_seconds(speed=speed, seconds=seconds, block=True)


def turn_left(left_motor: LargeMotor):
    left_motor.on_for_degrees(speed=100, degrees=180, block=True)


def main():
    left_motor = LargeMotor(OUTPUT_A)
    right_motor = LargeMotor(OUTPUT_B)
    bulldozer = MediumMotor(OUTPUT_C)
    eyes = UltrasonicSensor(INPUT_1)
    button = Button()

    forward(left_motor, right_motor, seconds=60)
    print("Blocking not caught we can still check for distance and stop as needed")
    while True:
        if check_distance(eyes):
            print("Detected an object in front of me.")
            stop(left_motor, right_motor)
            knock_o_matic(bulldozer)
            left_and_right(left_motor, right_motor)
            backward(left_motor, right_motor, seconds=2, speed=75)
            turn_left(left_motor)
            stop(left_motor, right_motor)
            forward(left_motor, right_motor, seconds=60)
        if button.any():
            stop(left_motor, right_motor)
            break


main()
