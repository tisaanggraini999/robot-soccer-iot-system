import math

def calculate_angle(cx, frame_width):
    center = frame_width / 2
    return (cx - center) / center * 30.0  # deg

def calculate_distance(area):
    if area <= 0:
        return 999
    return 1200 / area
