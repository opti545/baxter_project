#!/usr/bin/env python

import rospy
import copy
import sys
import moveit_commander as mc
import moveit_msgs.msg
import geometry_msgs.msg
import baxter_interface


def init_node():
    global robot
    global scene
    global group
    global gripper
    print "Starting node"
    mc.roscpp_initialize(sys.argv)
    rospy.init_node('move_arm_node')
    print "move_arm_node should be initialized"
    print "Initializing Robot Commander"
    robot = mc.RobotCommander()

    print "Initializing Planning Scene Interface"
    scene = mc.PlanningSceneInterface()
    print "Let's move left arm first"
    group = mc.MoveGroupCommander("left_arm")
    gripper = baxter_interface.Gripper('left')

def move_arm_node():
    print "Calling init_node()"
    init_node()
    print "move_arm_node should be initialized"
    rospy.sleep(1)
    robot_pose = geometry_msgs.msg.Pose()

    while not rospy.is_shutdown():
        robot_pose.orientation.x = 1

        robot_pose.position.x = 0.7
        robot_pose.position.y = 0.5
        robot_pose.position.z = 0.3

        group.set_pose_target(robot_pose)
        plan1 = group.plan()
        rospy.sleep(3)
        group.go(wait=True)

        robot_pose.orientation.x = 1

        robot_pose.position.x = 0.83
        robot_pose.position.y = 0.1
        robot_pose.position.z = 0.07

        group.set_pose_target(robot_pose)
        plan1 = group.plan()
        rospy.sleep(3)
        group.go(wait=True)

        
        

if __name__ == '__main__':
    move_arm_node()
