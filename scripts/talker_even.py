#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker_even')
pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
rate = rospy.Rate(10)

def start_talker():
    msg = String()
    counter = 0
    while not rospy.is_shutdown():
        if (counter % 2 == 0):
                outputstr = str(counter)
                rospy.loginfo(outputstr)
                    
                msg.data = outputstr
                pub.publish(msg)

        rate.sleep()
        counter += 1

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
