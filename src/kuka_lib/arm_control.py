#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import PoseStamped

class ArmControl:
    def __init__(self):
        rospy.init_node("set_poser",anonymous=True)
        self.pub = rospy.Publisher('/iiwa/command/CartesianPose', PoseStamped, queue_size=10)
        self.pos = PoseStamped()               
        print("init fonk ici")
    def set_pose(self,posX,posY,posZ,oriX,oriY,oriZ,oriW):        
        self.pos.header.seq = 1
        self.pos.header.stamp = rospy.Time.now()
        self.pos.header.frame_id = "iiwa_link_0"

        self.pos.pose.position.x = posX
        self.pos.pose.position.y = posY
        self.pos.pose.position.z = posZ

        self.pos.pose.orientation.x = oriX
        self.pos.pose.orientation.y = oriY
        self.pos.pose.orientation.z = oriZ
        self.pos.pose.orientation.w = oriW      
        self.pub.publish(self.pos)        
            

    def is_ok(self):
        if not rospy.is_shutdown():
            return True
        else:
            return False
        
    