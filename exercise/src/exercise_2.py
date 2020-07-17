#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def shutdown_hook():
    print("[ square Publisher ] , I'm shutting down ... ")

def circle(node_name="node_square",topic_name= "/turtle1/cmd_vel" ,rate_node=1):
    square_side = input("Enter length of square side : ")
    i=8
    count=0
    angle = 90
    rospy.init_node(node_name)
    rate = rospy.Rate(rate_node)
    rospy.on_shutdown(shutdown_hook)
    relative_angle = angle * 2 * PI / 360
    circle_data1 = Twist()
    circle_data1.linear.x += square_side
    circle_data1.angular.z = 0
    circle_data2 = Twist()
    circle_data2.linear.x += 0
    circle_data2.angular.z = relative_angle



   # pub = rospy.Publisher(topic_name, msg_class, queue_size=1)
    pub = rospy.Publisher(topic_name, Twist, queue_size=1)

    while count < i:
        if count % 2 == 1:
            pub.publish(circle_data1)
            count += 1


        elif count % 2 == 0:
            pub.publish(circle_data2)
            count += 1






        rate.sleep()




def main():
    circle()

if __name__=="__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass