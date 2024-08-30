import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='Example_pw_ws',
            executable='pub',
            name='pub'),
        launch_ros.actions.Node(
            package='Example_pw_ws',
            executable='pubsub',
            name='pubsub'),
        launch_ros.actions.Node(
            package='Example_pw_ws',
            executable='sub',
            name='sub'),
  ])

