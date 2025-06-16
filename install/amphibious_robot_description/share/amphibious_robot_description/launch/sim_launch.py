from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_share = FindPackageShare('amphibious_robot_description').find('amphibious_robot_description')

    urdf_file = Command([
        'xacro ',
        PathJoinSubstitution([pkg_share, 'description', 'amphibot.urdf.xacro'])
    ])

    return LaunchDescription([
        # Launch Gazebo Fortress with your world
        ExecuteProcess(
            cmd=[
                'ign', 'gazebo',
                PathJoinSubstitution([pkg_share, 'worlds', 'world.sdf']),
                '--verbose'
            ],
            output='screen'
        ),

        # Robot state publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': urdf_file}]
        ),

        # Spawn robot into Gazebo Fortress
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-name', 'amphibot', '-topic', 'robot_description', '-z', '0.1'],
            output='screen'
        )
    ])
