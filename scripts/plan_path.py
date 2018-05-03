import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg 
import geometry_msgs.msg 

print "Starting"
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)

pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1.0
pose_target.position.x = 0.16 # random positions
pose_target.position.y = -0.48
pose_target.position.z = 0.45
group.set_pose_target(pose_target)

plan1 = group.plan()

#print "After Execution"

print "============ Printing robot state"
print robot.get_current_state()
print "============"

rospy.sleep(5)

moveit_commander.roscpp_shutdown()

