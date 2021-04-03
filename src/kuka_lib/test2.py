#!/usr/bin/env python2
#from greenrider_lib.robot_control import RobotControl
from kuka_lib.arm_control import ArmControl
import time

#robot = RobotControl("greenrider")
arm = ArmControl()
time.sleep(5)


while arm.is_ok():
    #arm.set_pose(0.000237648768374, -1.601132970488e-07, 1.30599996577, 6.39207527779e-08, 0.000185863806706, -0.000252382635842, 0.999999950879) # init pose
    #arm.set_pose(-0.387386932954, -0.387374500652, 0.573243573379, -0.224729723349, 0.224724081203, -1.01565976377e-05, 0.948153805386)
    #arm.set_pose(0.4, -0.4, 0.2, 0.0, 0.0, 0.0, 0.0)
    #arm.set_pose(0.000237648768374, -1.601132970488e-07, 1.30599996577, 6.39207527779e-08, 0.000185863806706, -0.000252382635842, 0.999999950879)
    arm.get_pose()




"""
while robot.is_ok():
    robot.new_object(True)
    robot.start_conveyor(True)
    robot.set_position(0,0,5)
    time.sleep(15)
    robot.start_conveyor(False)
    pick_place = False
    image = robot.image_data()
    color_pixel_counter = 0
    for i in range(image.width):
        for j in range(image.height):
            a = (i + j * image.width) * 3 # index to start RGB components
            r = image.data[a+0]   # red component
            g = image.data[a+1]   # green component
            b = image.data[a+2]   # blue component
            pixel_color = r + g + b
            if pixel_color > 0:
                color_pixel_counter += 1
    print(color_pixel_counter)

    if color_pixel_counter > 5000:
        print("This is a Box!")
        # Pick Islemi
        robot.grip(True)
        robot.set_position(0,0,0)
        time.sleep(4)

        # Place Islemi
        robot.set_position(0,0,5)
        time.sleep(4)
        robot.set_position(-1.31,1.97,0.49)
        time.sleep(4)
        robot.grip(False)

    elif color_pixel_counter > 1000:
        print("This is a Bottle!")
        # Pick Islemi
        robot.grip(True)
        robot.set_position(0,0,0)
        time.sleep(4)

        # Place Islemi
        robot.set_position(0,0,5)
        time.sleep(4)
        robot.set_position(-1.31,0.0,0.49)
        time.sleep(4)
        robot.grip(False)

    elif color_pixel_counter > 200:
        print("This is a Can!")
        # Pick Islemi
        robot.grip(True)
        robot.set_position(0,0,0)
        time.sleep(4)

        # Place Islemi
        robot.set_position(0,0,5)
        time.sleep(4)
        robot.set_position(-1.31,-1.97,0.49)
        time.sleep(4)
        robot.grip(False)
"""



