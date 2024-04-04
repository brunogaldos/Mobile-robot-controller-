#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
#from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R
import math
import time

class MoveRobotNode(Node):
    def on_shutdown(self):
        # create and publish Twist message to stop the robot
        stop_msg = Twist()
        stop_msg.linear.x = 0.0
        stop_msg.angular.z =0.0
        # publish the stop message continuously for a short period of time
        start_time = time.time()

        while time.time() - start_time < 1.0:
            self.publisher_.publish(stop_msg)
            time.sleep(0.1)
            print("robot stop")
        super().on_shutdown()

    def __init__(self):
        super().__init__('move_robot_node')
        self.publisher_ = self.create_publisher(Twist, '/diff_cont/cmd_vel_unstamped', 10)  #for differential robot

        self.subscription = self.create_subscription(Odometry, '/diff_cont/odom', self.odom_callback, 10)    #differential

        self.current_pose = self.get_start_pose()

    #enter the asked values x,y,theta in the terminal 
        
    def get_start_pose(self):
  
        start_x = float(input("Enter start x: "))
        start_y = float(input("Enter start y: "))
        start_theta = float( input("Enter start theta in radians:"))
        return [start_x, start_y, start_theta]

    #function to update the current pose based on the odometry from gazebo 
    def odom_callback(self, msg):

        self.current_pose[0] = msg.pose.pose.position.x
        self.current_pose[1] = msg.pose.pose.position.y
        orientation_q = msg.pose.pose.orientation
        r = R.from_quat([orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w])
        _, _, yaw = r.as_euler('xyz')

        self.current_pose[2] = yaw

    #function for moving the robot 
    def move_robot(self, goal_pose, velocity):
        # calculate error in x,y and theta 
        error_x = goal_pose[0] - self.current_pose[0]
        error_y = goal_pose[1] - self.current_pose[1]
        error_theta = math.atan2(error_y, error_x) - self.current_pose[2]
        



    # Stage 1: Rotate the robot to face the goal
        while abs(error_theta) > 0.001:  # adjust the threshold as needed
            error_theta = math.atan2(error_y, error_x) - self.current_pose[2]
            angular_velocity = velocity * error_theta*1.5 #increase by a factor of 2 arbitrarily to speed up 
            if abs(error_theta) < 0.001:  # if the robot is close enough to the target orientation
                angular_velocity = 0.0  # stop rotating

            print("error of orientation is",error_theta)
            msg = Twist()
            msg.angular.z = angular_velocity
            self.publisher_.publish(msg)

            rclpy.spin_once(self)


        # Stage 2: Move the robot forward towards the goal
        distance = (error_x**2 + error_y**2)**0.5

        while distance >= 0.05:
            error_x = goal_pose[0] - self.current_pose[0]
            error_y = goal_pose[1] - self.current_pose[1]
            distance = (error_x**2 + error_y**2)**0.5
            
            print("Current pose x,y: ", self.current_pose[0], self.current_pose[1])
            print("distance left", distance)    
            linear_velocity = velocity * distance
  

            # create and publish Twist message so the mobile robot moves
            msg = Twist()
            msg.linear.x = linear_velocity
            
            #msg.angular.z = angular_velocity
            self.publisher_.publish(msg)

            rclpy.spin_once(self)

        # Stage 3: Rotate the robot to the goal orientation
        error_theta_final = goal_pose[2] - self.current_pose[2]
        error_theta_final = (error_theta_final + math.pi) % (2 * math.pi) - math.pi  # normalize to [-pi, pi]
        while abs(error_theta_final) > 0.02:  # adjust threshold

            angular_velocity = velocity * error_theta_final*1.5 
            print("error_theta_is",error_theta_final)
            error_theta_final = goal_pose[2] - self.current_pose[2]
            error_theta_final = (error_theta_final + math.pi) % (2 * math.pi) - math.pi
            if abs(error_theta_final) < 0.02:  # if the robot is close enough to the target orientation
                goal_reached= True 
                print("goal orientation reached END") # stop rotating
                        # create and publish Twist message to stop the robot
                stop_msg = Twist()
                stop_msg.linear.x = 0.0
                stop_msg.angular.z =0.0
                self.publisher_.publish(stop_msg)
                            
                
                break
            
            msg = Twist()
            msg.angular.z = angular_velocity
            self.publisher_.publish(msg)

            rclpy.spin_once(self)    
 
     
def main(args=None):
    rclpy.init(args=args)
    
    move_robot_node = MoveRobotNode()
    #enter the asked values for goal_pose x,y,theta, velocity in the terminal 
    goal_pose = [float(input("Enter goal x: ")), float(input("Enter goal y: ")), float(input("Enter goal theta: "))]
    velocity = float(input("Enter velocity: "))
    move_robot_node.move_robot(goal_pose, velocity)
    #while rclpy.ok():
        
    rclpy.spin(move_robot_node)

    move_robot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()