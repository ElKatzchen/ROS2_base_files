import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/katzchen/Documents/Robotics/Examples_ws/install/Example_py_ws'
