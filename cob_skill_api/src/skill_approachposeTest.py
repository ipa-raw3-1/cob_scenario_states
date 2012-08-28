#!/usr/bin/python

# Example using the current version of the cob_skill_api

import roslib
roslib.load_manifest('cob_skill_api')
import rospy
import smach
import smach_ros
from actionlib import *
from actionlib.msg import *

import sys

import skill_approachpose

if __name__ == "__main__":

	rospy.init_node('skill_template')

	fName = sys.argv[1] 
	sm = skill_approachpose.SkillImplementation(fName)

	sis = smach_ros.IntrospectionServer('SM', sm, 'SM')
	sis.start()
	outcome = sm.execute()
	rospy.spin()
	sis.stop()
