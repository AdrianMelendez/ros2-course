import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_share = get_package_share_directory('robot_description')
    urdf_path = os.path.join(pkg_share, 'urdf', 'robot.urdf.xacro')
    world_path = os.path.join(pkg_share, 'worlds', 'obstacles.world')
    rviz_config = os.path.join(pkg_share, 'rviz', 'gazebo.rviz')

    robot_description = {
        'robot_description': ParameterValue(
            Command(['xacro ', urdf_path]), value_type=str
        )
    }

    rviz_args = ['-d', rviz_config] if os.path.exists(rviz_config) else []
    gui = LaunchConfiguration('gui')

    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'diffbot',
                   '-x', '0', '-y', '0', '-z', '0.05'],
        output='screen',
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        DeclareLaunchArgument('gui', default_value='false',
                              description='Abrir gzclient (ventana Gazebo)'),

        ExecuteProcess(
            cmd=['gzserver', '--verbose', '-s', 'libgazebo_ros_init.so',
                 '-s', 'libgazebo_ros_factory.so', world_path],
            output='screen',
        ),

        ExecuteProcess(
            cmd=['gzclient', '--verbose'],
            output='screen',
            condition=IfCondition(gui),
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[robot_description,
                        {'use_sim_time': LaunchConfiguration('use_sim_time')}],
        ),

        # Spawn retrasado 8s para dar tiempo a que el factory esté listo
        TimerAction(period=8.0, actions=[spawn_robot]),

        Node(
            package='rviz2',
            executable='rviz2',
            arguments=rviz_args,
            output='screen',
            parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}],
        ),
    ])
