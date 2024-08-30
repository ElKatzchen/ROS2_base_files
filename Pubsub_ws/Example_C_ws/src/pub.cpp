#include <chrono>
#include <functional>
#include <memory>
#include <random>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/u_int8_multi_array.hpp"

using namespace std::chrono_literals;

class Alpha_Publisher : public rclcpp::Node
{
  //----------DECLARATIONS----------
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::UInt8MultiArray>::SharedPtr publisher_;

  public:
    //----------NODE DECLARATION----------
    Alpha_Publisher() : Node("Puublisher_N")
    {
      publisher_ = this->create_publisher<std_msgs::msg::UInt8MultiArray>("Topic_1", 10);
      timer_ = this->create_wall_timer(
      1000ms, std::bind(&Alpha_Publisher::timer_callback, this));
    }

  private:
    void timer_callback()
    {
      //----------PUBLISHER----------
      //----------MESSAGE TYPE----------
      auto message = std_msgs::msg::UInt8MultiArray();
      message.data = {0, 0, 0, 0, 0};

      //----------MESSAGE ARRAY----------
      std::cout << "1st Array: [";
      for (size_t i = 0; i < 5; ++i)
      {
        message.data[i] = rand() % 10;
        std::cout << static_cast<int>(message.data[i]);
        if (i != message.data.size() - 1)
        {
          std::cout << ", ";
        }
      }
      std::cout << "]" << std::endl;

      //----------SEND MESSAGE----------
      publisher_->publish(message);
    }
    
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Alpha_Publisher>());
  rclcpp::shutdown();
  return 0;
}