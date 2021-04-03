#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float64
from iiwa_msgs.msg import JointPosition
from iiwa_msgs.msg import JointQuantity
class ArmControl:
    def __init__(self):
        rospy.init_node("set_poser",anonymous=True)
        self.pub = rospy.Publisher('/iiwa/command/CartesianPose', PoseStamped, queue_size=10)       
        self.grabber_left_pub = rospy.Publisher('/iiwa/grabber_left_joint/set_speed', Float64, queue_size=10)
        self.grabber_right_pub = rospy.Publisher('/iiwa/grabber_right_joint/set_speed', Float64, queue_size=10)
        self.joint_pub = rospy.Publisher('iiwa/command/JointPosition', JointPosition, queue_size=10)
        self.pos = PoseStamped()    
        self.left_gripper_msg = Float64()
        self.right_gripper_msg = Float64()
        self.joint_values = JointPosition()
        self.joint_quantity = JointQuantity()
        
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
        rospy.sleep(2)
        

    def is_ok(self):
        if not rospy.is_shutdown():
            return True
        else:
            return False

    def get_pose(self):
        self.sub = rospy.Subscriber('/iiwa/state/CartesianPose', PoseStamped, self.subsFonk)
        rospy.spin()        

    def subsFonk(self,data):
        print(data)     
            
    def gripper(self, state):
        if state == True:
            self.left_gripper_msg.data = 0.05
            self.right_gripper_msg.data = -0.05
        else:
            self.left_gripper_msg.data = -0.05
            self.right_gripper_msg.data = 0.05

        self.grabber_left_pub.publish(self.left_gripper_msg)
        self.grabber_right_pub.publish(self.right_gripper_msg)
        
    
    def joint_control(self,joint1=0.0,joint2=0.0,joint3=0.0,joint4=0.0,joint5=0.0,joint6=0.0,joint7=0.0):
        self.joint_quantity.a1 = joint1
        self.joint_quantity.a2 = joint2
        self.joint_quantity.a3 = joint3
        self.joint_quantity.a4 = joint4
        self.joint_quantity.a5 = joint5
        self.joint_quantity.a6 = joint6
        self.joint_quantity.a7 = joint7

        self.joint_values.position = self.joint_quantity

        self.joint_pub.publish(self.joint_values)

        rospy.sleep(0.2)
    