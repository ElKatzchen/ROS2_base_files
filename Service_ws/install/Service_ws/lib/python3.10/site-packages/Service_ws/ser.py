import rclpy
from rclpy.node import Node

#----------DECLARATIONS----------
from example_interfaces.srv import AddTwoInts

class Alpha_Server(Node):
    #----------NODE DECLARATION----------
    def __init__(self):
        super().__init__('alpha_server')
        self.srv = self.create_service(AddTwoInts, 'Super_Topic', self.server_callback)

    #----------SERVER----------
    def server_callback(self, request, response):
        response.sum = request.a + request.b
        print(f'Request: a={request.a}, b={request.b}, sum={response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)
    service = Alpha_Server()
    rclpy.spin(service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
