import logging
import cv2

class CamerasPool:
    """
    Manage Reusable objects for use by Client objects.
    """

    def __init__(self, size):
        self._reusables = [Camera(_) for _ in range(size)]

    def acquire(self):
        try:
            return self._reusables.pop()
        except:
            logging.error("All Cameras Are Busy!")
            return -1

    def release(self, reusable):
        self._reusables.append(reusable)


class Camera:
    """
    Unique Camera with unique ID
    """

    def __init__(self, id):
        self._id = id
        self._params = None
        self._frame = None
        self.cap = cv2.VideoCapture(self._id)
        
    def get_id(self):
        return self._id
    
    def start(self):
        pass
    
    def stop(self):
        pass

    def get_frame(self):
        # Capture frame-by-frame
        ret, self._frame = self.cap.read()
        return self._frame

if __name__ == "__main__":
    cameras = CamerasPool(2)
    cam1 = cameras.acquire()
    cam2 = cameras.acquire()
    print(cam1.get_id())
    print(cam2.get_id())
    cameras.release(cam1)
    del cam1
    cam3 = cameras.acquire()
    print(cam2.get_id())
    print(cam3.get_id())
    cam4 = cameras.acquire()