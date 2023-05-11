#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TriangleTurtle(Node):

    def __init__(self):
        super().__init__('triangle_turtle')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.subscription_ = self.create_subscription(Pose, 'turtle1/pose', self.listener_callback, 10)
        self.subscription_  # prevent unused variable warning
        self.twist_msg = Twist()
        self.rate = self.create_rate(10)

        self.x, self.y, self.theta = 5, 5, 60
        self.side_length = 5 # adjust the side length of the triangle here
        self.vertices = [(self.side_length, 0), (-self.side_length/2, self.side_length*math.sqrt(3)/2), (-self.side_length/2, -self.side_length*math.sqrt(3)/2)] # vertices of the triangle

        self.target_x, self.target_y = self.vertices[0]

    def listener_callback(self, pose):
        self.x, self.y, self.theta = pose.x, pose.y, pose.theta
        self.move_turtle()

    def move_turtle(self):
        dist_x = self.target_x - self.x
        dist_y = self.target_y - self.y
        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)

        if distance < 0.05:
            vertex_index = self.vertices.index((self.target_x, self.target_y))
            next_index = (vertex_index + 1) % len(self.vertices)
            self.target_x, self.target_y = self.vertices[next_index]

        angle_to_goal = math.atan2(dist_y, dist_x)
        angle_diff = angle_to_goal - self.theta

        if angle_diff > math.pi:
            angle_diff -= 2*math.pi
        elif angle_diff < -math.pi:
            angle_diff += 2*math.pi

        # set linear and angular velocity based on distance to target and angle difference
        self.twist_msg.linear.x = 0.2 if distance > 0.1 else 0.0
        self.twist_msg.angular.z = 0.5 if angle_diff > 0.1 else (-0.5 if angle_diff < -0.1 else 0.0)

        # publish velocity command
        self.publisher_.publish(self.twist_msg)
        self.rate.sleep()


def main(args=None):
    rclpy.init(args=args)
    triangle_turtle = TriangleTurtle()
    rclpy.spin(triangle_turtle)

    # clean up node on shutdown
    triangle_turtle.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
