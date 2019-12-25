from ev3dev2.motor import LargeMotor, OUTPUT_A

motor_1 = LargeMotor(OUTPUT_A)


motor_1.on_for_degrees(speed=50, degrees=360, brake=True)