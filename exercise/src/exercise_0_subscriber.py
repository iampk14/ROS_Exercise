#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def shutdown_hook():
    print("[ circle Publisher ] , I'm shutting down ... ")

def circle(node_name="node_circle",topic_name= "/turtle1/cmd_vel" ,rate_node=1):
    rospy.init_node(node_name)
    rate = rospy.Rate(rate_node)
    rospy.on_shutdown(shutdown_hook)
    circle_data = Twist()
    circle_data.linear.x = 0.5
    circle_data.angular.z = 0.5

   # pub = rospy.Publisher(topic_name, msg_class, queue_size=1)
    pub = rospy.Publisher(topic_name, Twist, queue_size=1)

    while not rospy.is_shutdown():
        pub.publish(circle_data)
        rate.sleep()




def main():
    circle()

if __name__=="__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass