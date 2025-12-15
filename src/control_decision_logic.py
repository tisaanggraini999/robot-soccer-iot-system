def compute_velocity(angle, distance):
    vx = 0.6 if distance > 40 else 0
    vy = 0
    w  = angle * 0.05
    return vx, vy, w
