import rclpy
from rclpy.node import Node
from random import randint as rdm

#----------DECLARATIONS----------
from example_interfaces.srv import AddTwoInts

class Alpha_Client(Node):
    #----------NODE DECLARATION----------
    def __init__(self):
        super().__init__('alpha_client')
        self.cli = self.create_client(AddTwoInts, 'Super_Topic')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            print('Service not available, waiting again...')
        self.req = AddTwoInts.Request()

    #----------CLIENT----------
    def send_request(self):
        self.req.a = rdm(1, 10)
        self.req.b = rdm(1, 10)
        self.future = self.cli.call_async(self.req)
        return self.future

def main(args=None):
    rclpy.init(args=args)
    client = Alpha_Client()
    future = client.send_request()

    #----------RESPONSE RECIEVE----------
    rclpy.spin_until_future_complete(client, future)
    if future.result() is not None:
        print(f'Result: {future.result().sum}')
    else:
        print('Exception while calling service: %r' % future.exception())

    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
