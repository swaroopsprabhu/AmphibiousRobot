from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
   pkg_share = FindPackageShare('amphibious_robot_description').find('amphibious_robot_description')


   return LaunchDescription([
       Node(
           package='joint_state_publisher',
           executable='joint_state_publisher',
           name='joint_state_publisher',
           output='screen'
       ),
       Node(
           package='robot_state_publisher',
           executable='robot_state_publisher',
           name='robot_state_publisher',
           output='screen',
           parameters=[{
               'robot_description': Command(['xacro ', PathJoinSubstitution([pkg_share, 'description', 'amphibot.urdf.xacro'])])
           }]
       ),
       Node(
           package='rviz2',
           executable='rviz2',
           name='rviz2',
           output='screen',
       ),
   ])