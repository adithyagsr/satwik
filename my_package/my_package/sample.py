#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Sample(Node):
    def __init__(self):
       super().__init__('sample')
       self.get_logger().info("Node Started")
       self.timer_ = self.create_timer(1.0,self.timer_callback)
       
    def timer_callback(self):
      self.get_logger().info("ROS2")



def main(args=None):
   rclpy.init(args=args)
   node = Sample()
   rclpy.spin(node)
   rclpy.shutdown()
   

if __name__ =="__main__":
    main()