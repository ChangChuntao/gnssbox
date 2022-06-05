# 计算方位角
def xy2azi(x1, y1, x2, y2):
    import math
    angle = 0.0
    dy = y2 - y1
    dx = x2 - x1
    if dx == 0.0 and dy > 0.0:
        angle = 0.0
    if dx == 0.0 and dy < 0.0:
        angle = 180.0
    if dy == 0.0 and dx > 0.0:
        angle = 90.0
    if dy == 0.0 and dx < 0.0:
        angle = 270.0
    if dx > 0.0 and dy > 0.0:
        angle = math.atan(dx / dy) * 180.0 / math.pi
    elif dx < 0.0 and dy > 0.0:
        angle = 360.0 + math.atan(dx / dy) * 180.0 / math.pi
    elif dx < 0.0 and dy < 0:
        angle = 180.0 + math.atan(dx / dy) * 180.0 / math.pi
    elif dx > 0.0 and dy < 0:
        angle = 180.0 + math.atan(dx / dy) * 180.0 / math.pi
    angle = math.radians(angle)
    return angle