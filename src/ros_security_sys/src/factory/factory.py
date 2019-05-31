# factory.py

class DetectedObject(object):
	type = ""
	color = ""
	danger = False
	def get_type(self):
		return repr(self) + self.type

class Person(DetectedObject):
	type = "person"

class Bag(DetectedObject):
	type = "bag"

class Animal(DetectedObject):
	type = "animal"

class DetectedObjectFactory():
	""" Implementation of Factory pattern to create an object for each detected object on the stream """
	
	def create_object(self, typ):
		targetclass = typ.capitalize()
		return globals()[targetclass]()


if __name__ == "__main__":
	detected_obj = DetectedObjectFactory()
	types = ['person', 'bag', 'animal']
	for t in types:
		print(detected_obj.create_object(t).get_type())

	output = '''
		<__main__.Person object at 0x0000028BE3ABC518>person
		<__main__.Bag object at 0x0000028BE3ABC518>bag
		<__main__.Animal object at 0x0000028BE3ABC518>animal
	'''