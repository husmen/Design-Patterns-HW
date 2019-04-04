# singleton.py

from random import seed, randint

class OnlyOneAdmin(object):
	""" Implementation of Singleton pattern to allow for only one admin at a time """

	instance = None

	class __OnlyOneAdmin:
		def __init__(self): # object initializer 
			self.id = None
			self.name = None
			self.pw = None
		def __str__(self): # provides string representation of object
			return repr(self) + " " + str(self.id)

	def __new__(cls): # __new__ always a classmethod
		# only create new instance of does not exist, otherwise, return old instance
		if not OnlyOneAdmin.instance:
			OnlyOneAdmin.instance = OnlyOneAdmin.__OnlyOneAdmin()
		return OnlyOneAdmin.instance

	def __getattr__(self, name):
		return getattr(self.instance, name)

	def __setattr__(self, name):
		return setattr(self.instance, name)


if __name__ == "__main__":
	seed(1)
	id = randint(0,10)
	x = OnlyOneAdmin()
	x.id = id
	print(x)

	id = randint(0,10)
	y = OnlyOneAdmin()
	y.id = id
	print(y)

	id = randint(0,10)
	z = OnlyOneAdmin()
	z.id = id
	print(z)

	print(x)
	print(y)

	output = '''
	<__main__.__OnlyOneAdmin instance at 0x00798900> 2
	<__main__.__OnlyOneAdmin instance at 0x00798900> 9
	<__main__.__OnlyOneAdmin instance at 0x00798900> 1
	<__main__.__OnlyOneAdmin instance at 0x00798900> 1
	<__main__.__OnlyOneAdmin instance at 0x00798900> 1
	'''