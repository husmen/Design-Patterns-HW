#!/usr/bin/env python3
import logging
from random import seed, randint

import numpy as np
import cv2

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage

from singleton import singleton
from factory import factory
from abstract_factory import abstract_factory
from observer import observer
from decorator_ import decorator as dec

gnome = True
kde = not gnome

frame = None
obj = None

order_coffee = True

logging.basicConfig(level=logging.DEBUG)
logging.info('logging started')

# Start observer
ss = observer.SecuritySys()
ss.observe('image arrived',  ss.image_arrived)
ss.observe('image processed',  ss.image_processed)
ss.observe('object detected',  ss.object_detected)

def obj_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    tmp_str = data.data
    full_list = tmp_str.split(" ")

    #create separate instances for each detected object
    detected_obj = factory.DetectedObjectFactory()
    for _ in full_list:
        try:
            #print(_)
            tmp = detected_obj.create_object(_).get_type()
        except:
            print("unkown object")
        else:
            observer.Event('object detected', '0001' + " " + _)
            print(tmp)


def frame_callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    observer.Event('image arrived', '0001')
    np_arr = np.fromstring(data.data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
def subscriber():
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber("cam_objs", String, obj_callback)
    rospy.Subscriber("cam_frame", CompressedImage, frame_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    #create admin credentials
    seed(1)
    aid = randint(0,10)
    admin = singleton.OnlyOneAdmin()
    admin.id = aid
    print(admin)

    #order admins favorite coffee
    if order_coffee:
        adminCoffee = dec.Concrete_Coffee()
        adminCoffee = dec.Milk(adminCoffee)
        adminCoffee = dec.Sugar(adminCoffee)
        print('Ingredients: '+adminCoffee.get_ingredients()+'; Cost: '+str(adminCoffee.get_cost())+'; sales tax = '+str(adminCoffee.get_tax()))

    #create UI elements
    if gnome:
        ui = abstract_factory.GtkUIFactory()
    elif kde:
        ui = abstract_factory.QtUIFactory()
    toolbox = ui.getToolboxWindow()
    layers = ui.getLayersWindow()
    main = ui.getMainWindow()

    subscriber()