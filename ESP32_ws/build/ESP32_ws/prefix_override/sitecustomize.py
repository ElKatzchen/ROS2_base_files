import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/katzchen/Documents/Robotics/ESP32_ws/install/ESP32_ws'
