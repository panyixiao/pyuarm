import pyuarm
import sys, os
from time import sleep
# from .log import DEBUG, INFO, ERROR, printf, init_logger, set_default_logger, close_logger

sleepTime = 3;

uArm = pyuarm.UArm()
uArm.connect()
# printf(uArm.firmware_version())
# printf(uArm.uArm.hardware_version())

uArm.set_servo_attach()
uArm.reset()
print("Start!")
while True:

	print("Move to Picking Point (Above)");
	uArm.set_position(100, 150, 150, speed = 100);
	sleep(sleepTime);

	print("Move to Picking Point");
	uArm.set_position(100, 150, 55, speed = 30);
	print("Pick !!!");
	uArm.set_pump(True);
	sleep(sleepTime);

	print("Move to Picking Point (Above)");
	uArm.set_position(100, 150, 150, speed = 1.0,wait = True);

	print("Move to Dropping Point (Above)");
	uArm.set_position(-100, 150, 150, speed = 50, wait = True);
	uArm.set_wrist(160)

	print("Move to Dropping Point");
	uArm.set_position(-100, 150, 55, speed = 30, wait = True);
	sleep(sleepTime);
	print("Drop!!!");
	uArm.set_pump(False);	

	print("Move to Dropping Point (Above)");
	uArm.set_position(-100, 150, 150, speed = 50);
	sleep(sleepTime);

	uArm.set_buzzer(1000, 0.1)
	print("Reset to Home Pose");
	uArm.reset()

