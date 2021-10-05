#!/usr/bin/env python3
from study_pkg.srv import Poly, PolyResponse, PolyRequest
from study_pkg.msg import Three_numbers
from std_msgs.msg import String
import rospy
import sys


def poly_clients ():
	rospy.wait_for_service('poly')
	try:
		poly_srv = rospy.ServiceProxy('poly', Poly)
		req = PolyRequest(a = 3, b = 2)
		resp = poly_srv(req)
		
		rospy.loginfo('Response %s' % resp.poly)
	except (rospy.ServiceException, e):
	    rospy.logerr("Service call failed: %s" % e)
	    
#number = Two_numbers()
#if len(sys.argv) == 3:
#	number.a = int(sys.argv[1])
#	number.b = int(sys.argv[2])
#else:
#	print('enter arguments')
#	sys.exit(1)

poly_clients ()

