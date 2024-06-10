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
                
            ],
            remappings=[
                ('commands/velocity', 'cmd/vel'),
                ('commands/led1', 'cmd/led1'),
                ('commands/led2', 'cmd/led2'),
                ('commands/digital_output', 'cmd/digital_output'),
                ('commands/external_power', 'cmd/external_power'),
                ('commands/sound', 'cmd/sound'),
                ('commands/reset_odometry', 'cmd/reset_odometry'),
                ('commands/motor_power', 'cmd/motor_power'),
                ('commands/controller_info', 'cmd/controller_info'),
                ('sensors/core', 'sensors/core'),
                ('sensors/dock_ir', 'sensors/dock_ir'),
                ('sensors/battery_state', 'sensors/battery_state'),
                ('sensors/imu_data', 'sensors/imu_data'),
                ('sensors/imu_data_raw', 'sensors/imu_data_raw'),
                ('debug/raw_data_command', 'debug/raw_data_command'),
                ('debug/raw_data_stream', 'debug/raw_data_stream'),
                ('debug/raw_control_command', 'debug/raw_control_command'),
                ('odom', 'odom'),
                ('joint_states', 'joint_states'),
                ('events/button', 'events/button'),
                ('events/bumper', 'events/bumper'),
                ('events/cliff', 'events/cliff'),
                ('events/wheel_drop', 'events/wheel_drop'),
                ('events/power_system', 'events/power_system'),
                ('events/digital_input', 'events/digital_input'),
                ('events/robot_state', 'events/robot_state'),
            ]
        )
    ])

