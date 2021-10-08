#!/usr/bin/env python3

from study_pkg.srv import Poly, PolyResponse, PolyRequest
from std_msgs.msg import String
from study_pkg.msg import Three_numbers
import rospy

def callback(answer):
	rospy.loginfo("i came from summator %s", answer.data)
	resp.poly = int(answer.data)
	
	
def start_poly(number):
	while not rospy.is_shutdown():
		#poly_str = number.a ** number.b
		poly_str = number.a ** 2
		number.c = poly_str
		rospy.loginfo('%s ^ %s = %s' % (number.a, number.b, poly_str))
		pub.publish(number)
		rate.sleep()
		rospy.Subscriber('from_summator', String, callback, queue_size=10)
		rospy.loginfo('response must be %s' % resp.poly)
		rospy.loginfo (type(resp))
		return resp
	
		
		
def poly_server():
	s = rospy.Service('poly', Poly, start_poly)
	rospy.loginfo('Ready to calc.')
	rospy.spin()
		

rospy.init_node('poly_server')
pub = rospy.Publisher('to_summator', Three_numbers, queue_size=10) #инициализируем публикацию
rate = rospy.Rate(1)

resp = PolyResponse()
poly_server()

