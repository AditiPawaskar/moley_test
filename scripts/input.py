# code to take user input as mentioned in test - Moley  ( assuming robot is mounted on the mounting point )

# mounting point co-ordinates: ()

import random

# required declarations
coord = []
coord.append([])
coord.append([])
coord.append([])


x_lowerlim = y_lowerlim = z_lowerlim = 0

x_upperlim = 2
y_upperlim = 1.5
z_upperlim = 0.7

'''
# during actual simulation when robot is mounted at mounting point , COMMENT OTHER LIMITS

x_lowerlim = -1.0
y_lowerlim = -1.0
z_lowerlim = 0.0

x_upperlim = 1.0
y_upperlim = 1.0
z_upperlim = 0.7

'''

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
	
	'''
	# during actual simulation when robot is mounted at mounting point , COMMENT OTHER LIMITS

	x = round(random.uniform(x_lowerlim,x_upperlim),2)
	y = round(random.uniform(y_lowerlim,y_upperlim),2)
	
	'''

	z = round(random.uniform(z_lowerlim,z_upperlim),2)

	coord[0].append(x)
	coord[1].append(y)
	coord[2].append(z)


# printing all random co-ordinates
for i in range(pose):
	
	print i
	print (coord[0][i],coord[1][i],coord[2][i])