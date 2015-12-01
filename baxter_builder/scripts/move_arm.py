#!/usr/bin/env python

import rospy
import copy
import sys
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

def move_arm():
    print "Starting tutorial setup"
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_arm_node')
    print "move_arm_node should be initialized"
    print "Initializing Robot Commander"
    robot = moveit_commander.RobotCommander()
    print "Initializing Planning Scene Interface"
    scene = moveit_commander.PlanningSceneInterface()
    print "Let's move left arm first"
    group = moveit_commander.MoveGroupCommander("left_arm")
    
    print "Create publisher to display_planned_path"
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory)
    
    robot_pose = geometry_msgs.msg.Pose()
    robot_pose.orientation.x = 1

    robot_pose.position.x = 0.7
    robot_pose.position.y = 0.4
    robot_pose.position.z = 0.3
    
    group.set_pose_target(robot_pose)
    plan1 = group.plan()
    rospy.sleep(5)
    group.go(wait=True)
    
    moveit_commander.roscpp_shutdown()

    print "Finishing"

if __name__ == '__main__':
    try:
        move_arm()
    except rospy.ROSInterruptException:
        pass

