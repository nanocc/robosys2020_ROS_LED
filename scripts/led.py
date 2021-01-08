#!/usr/bin/env python3

import rospy, os
from std_msgs.msg import String

def cb(message):
    rospy.loginfo(message.data)
    if(message.data >= '0' and message.data <= '9'):
    	os.system("echo " + str(message.data) + " > /dev/myled0")
    else:
    	os.system("echo " + message.data + " > /dev/myled0")

if __name__ == '__main__':
    rospy.init_node('led')
    sub = rospy.Subscriber('key_type', String, cb)
    rospy.spin()
    os.system("echo 0 > /dev/myled0")
