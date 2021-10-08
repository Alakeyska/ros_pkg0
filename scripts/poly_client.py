#!/usr/bin/env python3
from study_pkg.srv import Poly, PolyResponse, PolyRequest
from study_pkg.msg import Three_numbers
from std_msgs.msg import String
import rospy
import sys


def poly_clients (a, b, c=0):
	rospy.wait_for_service('poly')
	try:
		poly_srv = rospy.ServiceProxy('poly', Poly)
		req = PolyRequest(a, b,c)
		resp = poly_srv(req)
		
		print('Response: [%s^2 + %s = %s]' % (a, b,resp.poly))
	except (rospy.ServiceException):
	    rospy.logerr("Service call failed")
	    
if len(sys.argv) == 3:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
else:
	print('enter arguments')
	sys.exit(1)

poly_clients (a, b, c = 0)

