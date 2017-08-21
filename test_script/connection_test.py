import pyuarm
import sys, os
from time import sleep
# from .log import DEBUG, INFO, ERROR, printf, init_logger, set_default_logger, close_logger

vel = 3;

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
	sleep(vel);

	print("Move to Picking Point");
	uArm.set_position(100, 150, 55, speed = 30);
	print("Pick !!!");
	uArm.set_pump(True);
	sleep(vel);

	print("Move to Picking Point (Above)");
	uArm.set_position(100, 150, 150, speed = 5,wait = True);
	sleep(vel);

	print("Move to Dropping Point (Above)");
	uArm.set_position(-100, 150, 150, speed = 50, wait = True);
	uArm.set_wrist(160)
	sleep(vel);

	print("Move to Dropping Point");
	uArm.set_position(-100, 150, 55, speed = 30, wait = True);
	sleep(vel);
	print("Drop!!!");
	uArm.set_pump(False);	

	print("Move to Dropping Point (Above)");
	uArm.set_position(-100, 150, 150, speed = 50);
	sleep(vel);

	print("Reset to Home Pose");
	uArm.reset()
