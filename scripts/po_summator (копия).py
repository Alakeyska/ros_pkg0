#!/usr/bin/env python3
from study_pkg.srv import Poly, PolyResponse
import rospy
from std_msgs.msg import String
from study_pkg.msg import Two_numbers
from study_pkg.msg import Three_numbers



#тело программы
def start_summator(req):
	msg = String()
	result_str = req.c + req.b
	rospy.loginfo('summator is summing: %s' % result_str)
	#rospy.loginfo(type(result_str))
		
	msg.data = str(result_str)
	pub.publish(msg)
		
		
rospy.init_node('summator')
rate = rospy.Rate(1)	
pub = rospy.Publisher('from_summator', String, queue_size=10)
rospy.Subscriber('to_summator', Three_numbers, start_summator, queue_size=10)
rospy.spin()
