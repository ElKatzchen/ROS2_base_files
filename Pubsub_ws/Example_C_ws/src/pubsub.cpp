#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/u_int8_multi_array.hpp"

using std::placeholders::_1;

class Alpha_PubSub : public rclcpp::Node
{
  //----------DECLARATIONS----------
  rclcpp::Subscription<std_msgs::msg::UInt8MultiArray>::SharedPtr subscription_;
  rclcpp::Publisher<std_msgs::msg::UInt8MultiArray>::SharedPtr publisher_;

  public:
    //----------NODE DECLARATION----------
    Alpha_PubSub() : Node("PubSub_N")
    {
      publisher_ = this->create_publisher<std_msgs::msg::UInt8MultiArray>("Topic_2", 10);
      subscription_ = this->create_subscription<std_msgs::msg::UInt8MultiArray>(
      "Topic_1", 10, std::bind(&Alpha_PubSub::topic_callback, this, _1));
    }

  private:
    void topic_callback(const std_msgs::msg::UInt8MultiArray & msg) const
    {
      //----------SUBSCRIBER----------
      //----------MESSAGE ARRAY----------
      std::cout << "1st Array: [";
      for (size_t i = 0; i < 5; ++i)
      {
        std::cout << static_cast<int>(msg.data[i]);
        if (i != msg.data.size() - 1)
        {
          std::cout << ", ";
        }
      }
      std::cout << "]" << std::endl;

      //----------PUBLISHER----------
      //----------MESSAGE TYPE----------
      auto message = std_msgs::msg::UInt8MultiArray();
      message.data = {0, 0, 0, 0, 0};

      //----------MESSAGE ARRAY----------
      std::cout << "2nd Array: [";
      for (size_t i = 0; i < 5; ++i)
      {
        message.data[i] = msg.data[i] * 2;
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
  rclcpp::spin(std::make_shared<Alpha_PubSub>());
  rclcpp::shutdown();
  return 0;
}