import copy

class Prototype:

   _type = None
   _value = None

   def clone(self):
      pass

   def getType(self):
      return self._type

   def getValue(self):
      return self._value

   def getDetections(self, img):
      # Place holder for detection functionality, returns a list of detected objects
      return ['person', 'bag', 'dog', 'cat', 'car']

class YOLO(Prototype):

   def __init__(self, number):
      self._type = "YOLO"
      self._value = number

   def clone(self):
      return copy.copy(self)

class SSD(Prototype):

   """ Concrete prototype. """

   def __init__(self, number):
      self._type = "SSD"
      self._value = number

   def clone(self):
      return copy.copy(self)

class RCNN(Prototype):

   """ Concrete prototype. """

   def __init__(self, number):
      self._type = "RCNN"
      self._value = number

   def clone(self):
      return copy.copy(self)

class DetectorFactory:

   """ Manages prototypes.
   Static factory, that encapsulates prototype
   initialization and then allows instatiation
   of the classes from these prototypes.
   """

   __yolo2 = None
   __yolo3 = None
   __ssd = None
   __rcnn = None

   @staticmethod
   def initialize():
      DetectorFactory.__yolo2 = YOLO(2)
      DetectorFactory.__yolo3 = YOLO(3)
      DetectorFactory.__ssd = SSD(1)
      DetectorFactory.__rcnn = RCNN(1)

   @staticmethod
   def getYOLO2():
      return DetectorFactory.__yolo2.clone()

   @staticmethod
   def getYOLO3():
      return DetectorFactory.__yolo3.clone()

   @staticmethod
   def getSSD():
      return DetectorFactory.__ssd.clone()

   @staticmethod
   def getRCNN():
      return DetectorFactory.__rcnn.clone()

if __name__ == "__main__":
   DetectorFactory.initialize()
   
   detector = DetectorFactory.getYOLO2()
   print("%s: %s" % (detector.getType(), detector.getValue()))
   
   detector = DetectorFactory.getYOLO3()
   print("%s: %s" % (detector.getType(), detector.getValue()))
   
   detector = DetectorFactory.getSSD()
   print("%s: %s" % (detector.getType(), detector.getValue()))
   
   detector = DetectorFactory.getRCNN()
   print("%s: %s" % (detector.getType(), detector.getValue()))