import rclpy
from rclpy.node import Node
from random import randint as rdm

#----------DECLARATIONS----------
from std_msgs.msg import UInt8MultiArray

class Alpha_Publisher(Node):
    #----------NODE DECLARATION----------
    def __init__(self):
        super().__init__('Alpha_Publisher')
        self.publisher_ = self.create_publisher(UInt8MultiArray, 'Topic_1', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    #----------PUBLISHER----------
    def timer_callback(self):
        #----------MESSAGE TYPE----------
        message = UInt8MultiArray()
        message.data = [0, 0, 0, 0, 0]

        #----------MESSAGE ARRAY----------
        for i in range(5):
            message.data[i] = rdm(1, 10)
        print(f"1st Array: {list(message.data)}")

        #----------SEND MESSAGE----------
        self.publisher_.publish(message)

def main(args=None):
    rclpy.init(args=args)

    alpha_pub = Alpha_Publisher()

    rclpy.spin(alpha_pub)

    alpha_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
