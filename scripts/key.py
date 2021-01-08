#!/usr/bin/env python3

import rospy, sys, tty, termios
from std_msgs.msg import String

if __name__ == '__main__':

    rospy.init_node('key')
    pub = rospy.Publisher('key_type', String, queue_size=1)
    rate = rospy.Rate(10)

    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    tty.setcbreak(sys.stdin.fileno())

    while not rospy.is_shutdown():
        ch = sys.stdin.read(1)
        pub.publish(ch)
        rate.sleep()

    termios.tcsetattr(fd, termios.TCSANOW, old)
