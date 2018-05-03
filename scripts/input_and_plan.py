# code to take user input as mentioned in test - Moley  ( assuming robot is mounted on the mounting point )

# mounting point co-ordinates: (1,0.5,0) ( as per the figure given )

import random
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg 
import geometry_msgs.msg 


# required declarations
coord = []
coord.append([])
coord.append([])
coord.append([])


'''
# limits used for testing purpose considering the arm to be mounted on the top left corner of the robot

x_lowerlim = y_lowerlim = z_lowerlim = 0

x_upperlim = 2
y_upperlim = 1.5
z_upperlim = 0.7

'''

x_lowerlim = -1.0
y_lowerlim = -1.0
z_lowerlim = 0.0

x_upperlim = 1.0
y_upperlim = 1.0
z_upperlim = 0.7



j = k = 0

x_mount = 1.00   # assumed mounting point
y_mount = 0.50
z_mount = 0.00


# taking input
print "Enter number of poses"
pose = input(">")


for i in range(pose):
	# generating random x co-ordinates

	x = round(random.uniform(x_lowerlim,x_upperlim),2)
	y = round(random.uniform(y_lowerlim,y_upperlim),2)
	z = round(random.uniform(z_lowerlim,z_upperlim),2)

	coord[0].append(x)
	coord[1].append(y)
	coord[2].append(z)


print "Number of poses:"
print pose

print "Generated co-ordinates:"

# printing all random co-ordinates generated
for i in range(pose):
	
	print i+1
	print (coord[0][i],coord[1][i],coord[2][i])


# code for motion planning

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)

pose_target = geometry_msgs.msg.Pose()

pose_target.orientation.w = 1.0

for i in range(pose):
	pose_target.position.x = coord[0][i]
	pose_target.position.y = coord[1][i]
	pose_target.position.z = coord[2][i]
	group.set_pose_target(pose_target)

	plan1 = group.plan()

	print "planning attempted for iteration"
	print i+1

	rospy.sleep(5)

moveit_commander.roscpp_shutdown()

