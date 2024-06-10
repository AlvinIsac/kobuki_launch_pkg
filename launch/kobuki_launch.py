from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='kobuki_node',
            executable='kobuki_ros_node',
            name='kobuki_node',
            output='screen',
            parameters=[
                {'device_port': '/dev/ttyUSB0'},
                {'base_frame': 'base'},
            ],
            remappings=[
                ('commands/velocity', 'cmd_vel'),
                ('commands/led1', 'cmd/led1'),
                ('commands/led2', 'cmd/led2'),
                ('commands/digital_output', 'cmd/digital_output'),
                ('commands/external_power', 'cmd/external_power'),
                ('commands/sound', 'cmd/sound'),
                ('commands/reset_odometry', 'cmd/reset_odometry'),
                ('commands/motor_power', 'cmd/motor_power'),
                ('commands/controller_info', 'cmd/controller_info'),
            ]
        )
    ])

