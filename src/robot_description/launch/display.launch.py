import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    pkg_share_str = get_package_share_directory('robot_description')
    rviz_config = os.path.join(pkg_share_str, 'rviz', 'display.rviz')

    pkg_share = FindPackageShare('robot_description')
    urdf_path = PathJoinSubstitution([pkg_share, 'urdf', 'robot.urdf.xacro'])

    robot_description = {
        'robot_description': ParameterValue(
            Command(['xacro ', urdf_path]), value_type=str
        )
    }

    rviz_args = ['-d', rviz_config] if os.path.exists(rviz_config) else []

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[robot_description,
                        {'use_sim_time': LaunchConfiguration('use_sim_time')}],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen',
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=rviz_args,
            output='screen',
        ),
    ])
