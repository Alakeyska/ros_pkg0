#!/usr/bin/env python3

from study_pkg.srv import Poly, PolyResponse, PolyRequest
from std_msgs.msg import String
from study_pkg.msg import Two_numbers
import rospy

def callback(answer):
	rospy.loginfo("i came from summator %s", answer.data)
	number.a += 1

	
def start_poly():
	while not rospy.is_shutdown():
		poly_str = number.a ** number.b
		rospy.loginfo('%s ^ %s = %s' % (number.a, number.b, poly_str))
		pub.publish(number)
		rate.sleep()
		rospy.Subscriber('from_summator', String, callback, queue_size=10)
		
		
		
number = Two_numbers()
number.a = 2
number.b = 2	
rospy.init_node('poly_node')
rate = rospy.Rate(1)
pub = rospy.Publisher('to_summator', Two_numbers, queue_size=10) #инициализируем публикацию

#rospy.Subscriber('from_summator', String, callback, queue_size=10) инициализируем подписку


try:
    start_poly()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
