import cv2
from dataclasses import dataclass
from typing import List
import numpy as np

@dataclass
class sData:
    ball_x:float = None
    ball_y: float = None
    hsv_img:np.ndarray = None
    h:float = None
    b_mask:np.ndarray= None
    d_mask:np.ndarray = None
    e_mask:np.ndarray = None
    mask:np.ndarray = None
    min_hsv:float = None
    max_hsv:float = None
    bbox_frame:np.ndarray = None
    connected: tuple[int, np.ndarray, np.ndarray, np.ndarray] = None
    stats:np.ndarray = None
    bbox_center:List[int] = None

class color_segment:
    def __init__(self):
        self.data = sData()

    def color_segment(self,img,min,max):
        self.data.hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        self.data.min_hsv = min
        self.data.max_hsv = max
        self.data.h = self.data.hsv_img[:, :, 0]
        self.data.bbox_frame = img

        self.data.mask = cv2.inRange(self.data.hsv_img, self.data.min_hsv, self.data.max_hsv)
        self.data.b_mask = cv2.blur(self.data.mask, (6,6))
        self.data.d_mask = cv2.dilate(self.data.b_mask,np.ones((10,10),np.int8))
        self.data.e_mask = cv2.erode(self.data.d_mask,np.ones((10,10),np.int8))

        if self.data.e_mask is not None:
            self.data.connected = cv2.connectedComponentsWithStats(self.data.e_mask)
            self.data.stats = self.data.connected[2]
            for stat in self.data.stats[1:]:
                x, y, w, h, area = stat
                if area > 250:  # skip small blobs
                    cv2.rectangle(self.data.bbox_frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
                    self.data.bbox_center = (int(x + w / 2), int(y + h / 2))
                    cv2.circle(self.data.bbox_frame, self.data.bbox_center, 2, (255, 255, 255), 1)

        return [self.data.e_mask, self.data.bbox_center,self.data.bbox_frame]
