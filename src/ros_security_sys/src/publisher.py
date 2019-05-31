#!/usr/bin/env python3

import numpy as np
import cv2

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage

from object_pool import object_pool
from prototype import prototype
from iterator import iterator
from builder import builder

def publisher():
    pub_frame = rospy.Publisher('cam_frame', CompressedImage, queue_size=1)
    pub_obj = rospy.Publisher('cam_objs', String, queue_size=1)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(1) # 1Hz

    cameras = object_pool.CamerasPool(1) #only one camera
    cam1 = cameras.acquire()
    print(cam1.get_id())
    cam2 = cameras.acquire() #will raise error
    
    prototype.DetectorFactory.initialize()
    detector1 = prototype.DetectorFactory.getYOLO3()
    print("%s: %s" % (detector1.getType(), detector1.getValue()))
    detector2 = prototype.DetectorFactory.getSSD()
    print("%s: %s" % (detector2.getType(), detector2.getValue()))

    while not rospy.is_shutdown():
        frame = cam1.get_frame()
        obj = detector1.getDetections(frame)
        obj_str = str(obj)
        rospy.loginfo(obj_str)

        msg_f = CompressedImage()
        msg_f.header.stamp = rospy.Time.now()
        msg_f.format = "jpeg"
        msg_f.data = np.array(frame).tostring()

        msg_o = ""

        #create a custom iterator for detected objects
        aggregate = iterator.Aggregate()  
        aggregate.set(obj)
        for value in aggregate:
            msg_o = msg_o + str(value) + " "
            print("Item: " + str(value)) 

        pub_frame.publish(msg_f)
        pub_obj.publish(msg_o)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
