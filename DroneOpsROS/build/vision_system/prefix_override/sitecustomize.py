import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/manuel/TMR-2025/DroneOpsROS/install/vision_system'
