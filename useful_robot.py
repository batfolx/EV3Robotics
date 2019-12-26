from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B

left_motor = LargeMotor(OUTPUT_A)
right_motor = LargeMotor(OUTPUT_B)


left_motor.on_for_degrees(speed=50, degrees=3200, brake=True, block=False)
right_motor.on_for_degrees(speed=50, degrees=3200, brake=True, block=True)

