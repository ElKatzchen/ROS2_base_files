import rclpy
from rclpy.node import Node
from random import randint as rdm

from std_msgs.msg import UInt8MultiArray

class Alpha_Publisher(Node):

    def __init__(self):
        super().__init__('Alpha_Publisher')
        self.publisher_ = self.create_publisher(UInt8MultiArray, 'Topic_1', 10)
        timer_period = 1  # 1 segundo
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        message = UInt8MultiArray()
        message.data = [0, 0, 0, 0, 0]
        for i in range(5):
            message.data[i] = rdm(1, 10)  # Usar 'i' como índice, no 'i-1'
        print(f"1st Array: {list(message.data)}")
        self.publisher_.publish(message)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Alpha_Publisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
