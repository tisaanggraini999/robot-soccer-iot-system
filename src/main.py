from vision.camera import init_camera
from vision.vision_processor import detect_ball
from vision.config import *
from communication.redis_client import publish_vision
from control.motion_controller import process_vision
from serial_comm.serial_sender import send_motion

cap = init_camera()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    vision = detect_ball(frame, BALL_LOWER, BALL_UPPER, FRAME_WIDTH)
    if vision:
        publish_vision(vision)
        vx, vy, w = process_vision(vision)
        send_motion(vx, vy, w)
