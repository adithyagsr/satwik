#!/usr/bin/env python3 
import rclpy 
from rclpy.node import Node 
from turtlesim.msg import Pose 
from geometry_msgs.msg import Twist 
import math 
import time
# from turtle_control import TurtleControllerNode
class traingle(Node):
    def __init__(self):
        super().__init__("turtle_controller") 
        self.length_y = 2.0
        self.length_x=3.0
        self.theta = math.pi
        self.pose_ = None 
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10) 
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop) 
    
    def control_loop(self):
        msg = Twist() 
        msg.linear.x = 0.0
        msg.angular.z = (math.pi/2)
        if msg.angular.z == math.pi/2:
            self.cmd_vel_publisher_.publish(msg)
            time.sleep(2)
            msg.angular.z = 0.0
        msg.linear.x = self.length_x
        # msg.linear.y = self.length_y
        self.cmd_vel_publisher_.publish(msg)
        time.sleep(1)
        msg.angular.z = math.pi/2
        msg.linear.x = 0.0
        self.cmd_vel_publisher_.publish(msg)
        time.sleep(2)
        if msg.angular.z == math.pi/2:
            msg.angular.z = 0.0
        msg.linear.x = self.length_x
        self.cmd_vel_publisher_.publish(msg)
        time.sleep(1)
        msg.angular.z = math.pi/2
        msg.linear.x = 0.0
        self.cmd_vel_publisher_.publish(msg)
        time.sleep(2)
        if msg.angular.z == math.pi/2:
            msg.angular.z=0.0
        msg.linear.x = self.length_x
        self.cmd_vel_publisher_.publish(msg)
        time.sleep(2)
def main(args=None):
    rclpy.init(args=args)
    tri = traingle()
    rclpy.spin(tri)
    rclpy.shutdown()

if __name__=="__main__":
    main()