#!/usr/bin/env python3
from study_pkg.srv import PolyArray, PolyArrayResponse
import rospy

def hande_poly_srv(req):
	result = 0
	returning_string = ''
	for i in range(len(req.coeff)):
		result = result + (req.coeff[i] ** (len(req.coeff) - i))
		if i != (len(req.coeff) - 1) :
			returning_string += str(req.coeff[i]) + '^' + str((len(req.coeff) - i)) + '+'
		else:
			returning_string += str(req.coeff[i])
			
	rospy.loginfo("Rerutning %s = %s" % (returning_string, result))
	resp = PolyArrayResponse()
	resp.poly = result
	
	return resp
	
def poly_server():
	rospy.init_node('poly_server')
	s = rospy.Service('poly', PolyArray, hande_poly_srv)
	rospy.loginfo('Ready to calc')
	rospy.spin()

poly_server()
