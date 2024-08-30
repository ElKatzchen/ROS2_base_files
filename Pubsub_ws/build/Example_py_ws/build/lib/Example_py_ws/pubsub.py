import rclpy
from rclpy.node import Node

#----------DECLARATIONS----------
from std_msgs.msg import UInt8MultiArray

class Alpha_PubSub(Node):
    #----------NODE DECLARATION----------
    def __init__(self):
        super().__init__('Alpha_PubSub')
        self.subscriber_ = self.create_subscription(UInt8MultiArray, 'Topic_1', self.listener_callback, 10)
        self.subscriber_

        self.publisher_ = self.create_publisher(UInt8MultiArray, 'Topic_2', 10)

    #----------SUBSCRIBER----------
    def listener_callback(self, msg):
        #----------MESSAGE ARRAY----------
        print(f"1st Array: {list(msg.data)}")

        #----------PUBLISHER----------
        #----------MESSAGE TYPE----------
        message = UInt8MultiArray()
        message.data = [0, 0, 0, 0, 0]

        #----------MESSAGE ARRAY----------
        for i in range(5):
            message.data[i] = msg.data[i] * 2
        print(f"2st Array: {list(message.data)}")

        #----------SEND MESSAGE----------
        self.publisher_.publish(message)
        

def main(args=None):
    rclpy.init(args=args)

    alpha_pubsub = Alpha_PubSub()

    rclpy.spin(alpha_pubsub)

    alpha_pubsub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
