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
    global both_group
    global left_group
    global right_group
    global plan_left, plan_right
    global pose_left, pose_right, pose_both

    mc.roscpp_initialize(sys.argv)
    rospy.init_node('move_arm_node')
    robot = mc.RobotCommander()

    scene = mc.PlanningSceneInterface()
    both_group = mc.MoveGroupCommander("both_arms")
    left_group = mc.MoveGroupCommander("left_arm")
    right_group = mc.MoveGroupCommander("right_arm")

    pose_left = geometry_msgs.msg.Pose()
    pose_right = geometry_msgs.msg.Pose()
    pose_both = geometry_msgs.msg.Pose()


    #Get the arms to the position needed
    rospy.loginfo('For left')
    pose_left.orientation.x = 1
    pose_left.position.x = 0.7
    pose_left.position.y = 0.4
    pose_left.position.z = 0.3
    left_group.set_pose_target(pose_left)

    plan_left = left_group.plan()
    rospy.sleep(2)

    rospy.loginfo('For right_group')
    pose_right.orientation.x = 1
    pose_right.position.x = 0.7
    pose_right.position.y = -0.4
    pose_right.position.z = 0.3
    right_group.set_pose_target(pose_right)

    plan_right = right_group.plan()
    rospy.sleep(2)

    both_group.set_pose_target(pose_right,'right_gripper')
    both_group.set_pose_target(pose_left, 'left_gripper')

    plan_both = both_group.plan()
    rospy.sleep(2)
    both_group.go(wait = True)


def move_arm_node():
    rospy.loginfo('Calling init_node()')
    init_node()
    rospy.loginfo('move_arm_node should be initialized')
    rospy.sleep(1)

    while not rospy.is_shutdown():
        rospy.loginfo('For left')
        pose_left.orientation.x = 1
        pose_left.position.x = 0.7
        pose_left.position.y = 0.4
        pose_left.position.z = 0.3
        left_group.set_pose_target(pose_left)

        plan_left = left_group.plan()
        rospy.sleep(2)
        
        left_group.go(wait = True)
        
        
        rospy.loginfo('For left')
        pose_left.orientation.x = 1
        pose_left.position.x = 0.83
        pose_left.position.y = 0.1
        pose_left.position.z = 0.07
        left_group.set_pose_target(pose_left)

        plan_left = left_group.plan()
        rospy.sleep(2)
        
        left_group.go(wait = True)
        rospy.sleep(2)

if __name__ == '__main__':
    move_arm_node()
