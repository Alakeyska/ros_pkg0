#!/usr/bin/env python3
import rospy
from study_pkg.msg import Control

rospy.init_node('wheel_status')
pub = rospy.Publisher('wheel_topic', Control, queue_size=10)
rate = rospy.Rate(10)

msg = Control()
msg.steer = 40
msg.speed = 10


def topic_cb(msg):
	while not rospy.is_shutdown():
		rospy.loginfo('Speed: %d / Steer: %d' % (msg.speed, msg.steer))
		pub.publish(msg)
		rate.sleep()
	
try:
	topic_cb(msg)
except (rospy.ROSInterruptException, KeyboardInterrupt):
	rospy.logerr('Exception catched')

