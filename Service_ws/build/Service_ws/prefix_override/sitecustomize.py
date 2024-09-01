import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/katzchen/Documents/Robotics/Service_ws/install/Service_ws'
