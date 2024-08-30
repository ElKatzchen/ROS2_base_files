import rclpy
from rclpy.node import Node

from std_msgs.msg import UInt8MultiArray

class Alpha_PubSub(Node):

    def __init__(self):
        super().__init__('Alpha_PubSub')
        self.subscriber_ = self.create_subscription(UInt8MultiArray, 'Topic_1', self.listener_callback, 10)
        self.subscriber_

    def listener_callback(self, msg):
        print(f"1st Array: {list(msg.data)}")


def main(args=None):
    rclpy.init(args=args)

    alpha_pubsub = Alpha_PubSub()

    rclpy.spin(alpha_pubsub)

    alpha_pubsub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()