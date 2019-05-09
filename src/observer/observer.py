import logging

class Observer():
    _observers = []
    def __init__(self):
        self._observers.append(self)
        self._observables = {}
    def observe(self, event_name, callback):
        self._observables[event_name] = callback

class Event():
    def __init__(self, name, data, autofire = True):
        self.name = name
        self.data = data
        if autofire:
            self.fire()
    def fire(self):
        for observer in Observer._observers:
            if self.name in observer._observables:
                observer._observables[self.name](*self.data.split(" "))
				
class SecuritySys(Observer):
    def __init__(self):
        logging.info("Security System started.")
        Observer.__init__(self) # Observer's init needs to be called
    def image_arrived(self, img_id):
        logging.info("image {} has arrived!".format(img_id))
    def image_processed(self, img_id):
        logging.info("image {} has been processed!".format(img_id))
    def object_detected(self, img_id, what):
        logging.info("image {} includes {}!".format(img_id, what))
	
if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	logging.info('logging started')
	
	# Start observer
	ss = SecuritySys()
	ss.observe('image arrived',  ss.image_arrived)
	ss.observe('image processed',  ss.image_processed)
	ss.observe('object detected',  ss.object_detected)
	
	# Example events
	Event('image arrived', '0001')
	Event('image arrived', '0002')
	Event('image processed', '0001')
	Event('image arrived', '0003')
	Event('image processed', '0002')
	Event('object detected', '0001' + " person")
	Event('object detected', '0001' + " dog")
	