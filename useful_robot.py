from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1


def check_distance(eyes: UltrasonicSensor):
    return eyes.distance_centimeters < 5


def forward(left_motor: LargeMotor, right_motor: LargeMotor, seconds=0.5, speed=50):
    left_motor.on_for_seconds(speed=speed, seconds=seconds, brake=True, block=False)
    right_motor.on_for_seconds(speed=speed, seconds=seconds, brake=True, block=False)


def stop(left_motor: LargeMotor, right_motor: LargeMotor):
    left_motor.off()
    right_motor.off()


def backward(left_motor: LargeMotor, right_motor: LargeMotor, seconds=0.5, speed=50):
    left_motor.on_for_seconds(speed=-speed, seconds=seconds, brake=True, block=False)
    right_motor.on_for_seconds(speed=-speed, seconds=seconds, brake=True, block=False)


def main():
    left_motor = LargeMotor(OUTPUT_A)
    right_motor = LargeMotor(OUTPUT_B)
    bulldozer = MediumMotor(OUTPUT_C)
    eyes = UltrasonicSensor(INPUT_1)

    forward(left_motor, right_motor, seconds=15)
    print("Blocking not caught we can still check for distance and stop as needed")
    while True:
        if check_distance(eyes):
            print("Detected an object in front of me.")
            stop(left_motor, right_motor)
            return


main()
