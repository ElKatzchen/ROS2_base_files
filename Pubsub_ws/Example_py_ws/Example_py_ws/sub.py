import rclpy
from rclpy.node import Node

#----------DECLARATIONS----------
from std_msgs.msg import UInt8MultiArray

class Alpha_Subscriber(Node):
    #----------NODE DECLARATION----------
    def __init__(self):
        super().__init__('Alpha_Subscriber')
        self.subscriber_ = self.create_subscription(UInt8MultiArray, 'Topic_2', self.listener_callback, 10)
        self.subscriber_

    #----------SUBSCRIBER----------
    def listener_callback(self, msg):
        #----------MESSAGE ARRAY----------
        print(f"2st Array: {list(msg.data)}")

        #----------MESSAGE TYPE----------
        message = UInt8MultiArray()
        message.data = [0, 0, 0, 0, 0]

        #----------MESSAGE ARRAY----------
        for i in range(5):
            if (msg.data[i] <= 5):
                message.data[i] = 0
            else:
                message.data[i] = msg.data[i] - 5
        print(f"Final Array: {list(message.data)}")
        

def main(args=None):
    rclpy.init(args=args)

    alpha_sub = Alpha_Subscriber()

    rclpy.spin(alpha_sub)

    alpha_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()