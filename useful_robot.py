from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C

left_motor = LargeMotor(OUTPUT_A)
right_motor = LargeMotor(OUTPUT_B)
helicopter = MediumMotor(OUTPUT_C)

left_motor.on_for_degrees(speed=50, degrees=3200, brake=True, block=False)
right_motor.on_for_degrees(speed=50, degrees=3200, brake=True, block=False)

helicopter.on_for_seconds(speed=75, seconds=10, brake=False, block=False)



