#!/usr/bin/env python
#from greenrider_lib.robot_control import RobotControl
import rospy
from kuka_lib.arm_control import ArmControl
import time
from std_msgs.msg import String

class Doit():

    def __init__(self):
        arm = ArmControl()
        key_down_sub = rospy.Subscriber("/keyboard_down", String, self.key_down)
        key_up_sub = rospy.Subscriber("/keyboard_up", String, self.key_up)
        self.joint1_angle = 0.0
        self.joint2_angle = 0.0
        self.joint3_angle = 0.0
        self.joint4_angle = 0.0
        self.joint5_angle = 0.0
        self.joint6_angle = 0.0
        self.joint7_angle = 0.0
        print("__init__")
        ros_rate = rospy.Rate(10)

        rospy.sleep(2.0)

        while arm.is_ok():
            print("__while__")
            arm.joint_control(self.joint1_angle, self.joint2_angle, self.joint3_angle, self.joint4_angle, self.joint5_angle, self.joint6_angle, self.joint7_angle)
            

    def key_down(self, msg):
        print("__key_down__")
        messages = msg.data.split(',')
        for elm in messages:
            if elm == "q":
                self.joint1_angle += 0.05
            elif elm == "e":
                self.joint1_angle -= 0.05
            if elm == "a":
                self.joint2_angle += 0.05
            elif elm == "d":
                self.joint2_angle -= 0.05
            if elm == "z":
                self.joint3_angle += 0.05
            elif elm == "c":
                self.joint3_angle -= 0.05
            if elm == "t":
                self.joint4_angle += 0.05
            elif elm == "u":
                self.joint4_angle -= 0.05
            if elm == "g":
                self.joint5_angle += 0.05
            elif elm == "j":
                self.joint5_angle -= 0.05
            if elm == "b":
                self.joint6_angle += 0.05
            elif elm == "m":
                self.joint6_angle -= 0.05
            if elm == "s":
                self.joint7_angle += 0.05
            elif elm == "f":
                self.joint7_angle -= 0.05
        return
    def key_up(self, msg):
        print("__key_up__")
        messages = msg.data.split(',')
        for elm in messages:
            if elm == "q":
                self.joint1_angle += 0.0
            elif elm == "e":
                self.joint1_angle -= 0.0
            if elm == "a":
                self.joint2_angle += 0.0
            elif elm == "a":
                self.joint2_angle -= 0.0
            if elm == "z":
                self.joint3_angle += 0.0
            elif elm == "c":
                self.joint3_angle -= 0.0
            if elm == "t":
                self.joint4_angle += 0.0
            elif elm == "u":
                self.joint4_angle -= 0.0
            if elm == "g":
                self.joint5_angle += 0.0
            elif elm == "j":
                self.joint5_angle -= 0.0
            if elm == "b":
                self.joint6_angle += 0.0
            elif elm == "m":
                self.joint6_angle -= 0.0
            if elm == "s":
                self.joint7_angle += 0.0
            elif elm == "f":
                self.joint7_angle -= 0.0
        return    

Doit()

