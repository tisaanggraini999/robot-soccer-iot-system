import serial
from communication.protocol import encode_command

ser = serial.Serial("COM3", 115200, timeout=1)

def send_motion(vx, vy, w):
    cmd = encode_command(vx, vy, w)
    ser.write(cmd.encode())
