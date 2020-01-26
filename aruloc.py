import cv2


class Aruloc:
    def __init__(
        self,
        aruco_locations,
        img_width,
        at=1.0,
        unit="m",
        cam_angle=90,
        aruco_dict="DICT_4X4_50",
        aruco_params=None,
    ):
        pass

    def locate(self, img):
        pass

    def set_cam_angle(self, angle):
        pass

    def draw_location(self, location, pixels_per_unit=100):
        pass


class Location:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

    def __str__(self):
        pass
