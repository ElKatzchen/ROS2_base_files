#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/u_int8_multi_array.hpp"

using std::placeholders::_1;

class Alpha_Subscriber : public rclcpp::Node
{
  //----------DECLARATIONS----------
  rclcpp::Subscription<std_msgs::msg::UInt8MultiArray>::SharedPtr subscription_;

  public:
    //----------NODE DECLARATION----------
    Alpha_Subscriber() : Node("Subscriber_N")
    {
      subscription_ = this->create_subscription<std_msgs::msg::UInt8MultiArray>(
      "Topic_2", 10, std::bind(&Alpha_Subscriber::topic_callback, this, _1));
    }

  private:
    void topic_callback(const std_msgs::msg::UInt8MultiArray & msg) const
    {
      //----------SUBSCRIBER----------
      //----------MESSAGE ARRAY----------
      std::cout << "2nd Array: [";
      for (size_t i = 0; i < 5; ++i)
      {
        std::cout << static_cast<int>(msg.data[i]);
        if (i != msg.data.size() - 1)
        {
          std::cout << ", ";
        }
      }
      std::cout << "]" << std::endl;

      //----------FINAL MESSAGE----------
      //----------MESSAGE TYPE----------
      auto message = std_msgs::msg::UInt8MultiArray();
      message.data = {0, 0, 0, 0, 0};

      //----------MESSAGE ARRAY----------
      std::cout << "3rd Array: [";
      for (size_t i = 0; i < 5; ++i)
      {
        message.data[i] = msg.data[i] - 5;
        if (message.data[i] >= 30)
        {
          message.data[i] = 0;
        }

        std::cout << static_cast<int>(message.data[i]);
        if (i != message.data.size() - 1)
        {
          std::cout << ", ";
        }
      }
      std::cout << "]" << std::endl;
    }
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Alpha_Subscriber>());
  rclcpp::shutdown();
  return 0;
}