import cv2
import numpy as np
from vision.geometry import calculate_angle, calculate_distance

def detect_ball(frame, lower, upper, frame_width):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None

    c = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
    cx = x + w // 2

    angle = calculate_angle(cx, frame_width)
    distance = calculate_distance(area)

    return {
        "angle": angle,
        "distance": distance,
        "area": area
    }
