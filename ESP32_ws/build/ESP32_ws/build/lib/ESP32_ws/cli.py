import rclpy
from rclpy.node import Node
import requests

class ESP_Client(Node):
    #----------NODE DECLARATION----------
    def __init__(self):
        super().__init__('ESP_client')
        self.timer = self.create_timer(2.0, self.send_command)

    #----------CLIENT----------
    def send_command(self):
        led_status = input("WRITE 1 OR 0 TO TURN ON OR OFF THE USERLED ")
        if led_status not in ['0', '1']:
            print("----------NOT VALID----------")
            return

        #----------ESP32 IP----------
        #---Change to the ESP IP---
        esp32_ip = '192.168.145.169'
        url = f'http://{esp32_ip}/{led_status}'

        #----------RESPONCE RECIEVE----------
        try:
            response = requests.get(url)
            print(f'Server Responce: {response.text}')
        except Exception as e:
            print(f'----------ERROR---------- {e}')

def main(args=None):
    rclpy.init(args=args)
    ESP_client = ESP_Client()
    rclpy.spin(ESP_client)
    ESP_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
