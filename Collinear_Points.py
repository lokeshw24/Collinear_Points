#!/bin/python

import random

x_range=[-5,5]
y_range=[2,7]
pairs_of_coordinates_required=10

input_coordinates=[]

#Hard-coded input_coordinates for initial testing purpose
#input_coordinates=[[-4, 5], [0, 6], [2, 7], [2, 4], [3, 3], [-4, 3], [5, 2], [2, 3], [4, 3], [1, 6]]

#-----------------------------------------------------------------
def create_random_input_coordinates():
	global input_coordinates, x_range, y_range

	for i in range(0,pairs_of_coordinates_required):
		input_coordinates.append( [random.randint(x_range[0], x_range[1]) , random.randint(y_range[0], y_range[1])] )

	print "Input Coordinates are : " ,input_coordinates

#-----------------------------------------------------------------
def print_collinear_points( slopes, min_points_required, start_pos ):
	'''
	checks if there are (min_points_required-1) number of duplicate values in slopes list.
	if yes, they are all collinear and hence prints them.
	The logic is same as finding duplicate values in an array.
	'''
	global input_coordinates

	len_of_slopes=len(slopes)
	list_of_pos=[]
	print "Collinear points are : "
	for target_pos in range(0,len_of_slopes):
		target_element=slopes[target_pos]
		#length=len(slopes)
		count=0
		for pos in range(target_pos+1, len_of_slopes):
			if ( target_element==slopes[pos] ):
				list_of_pos.append(pos)

		#print "List of pos of duplicates : ", list_of_pos
		if ( len(list_of_pos) >= (min_points_required-2) ) :
			print "----------------"
			print input_coordinates[start_pos]
			list_of_pos.append(target_pos)
			for pos in list_of_pos : 
				print input_coordinates[start_pos+pos+1]

		#clear the list
		list_of_pos[:]=[]
#-----------------------------------------------------------------
def find_collinear_points(min_points_required):
	'''
	"min_points_required" denote the no. of points atleast required to be collinear
	'''
	global input_coordinates

	slopes=[]
	total_pairs=len(input_coordinates)
	#print "total_pairs : " , total_pairs

	for start_pos in range(0,total_pairs) :
		next_pos=start_pos+1
		total_count=total_pairs-next_pos
		if (total_count<(min_points_required-1) ):
			break
		while( next_pos < total_pairs ):
			#slope = (diff in y-coordinates)/(diff in x-coordinates)
			diff_x_coord=( input_coordinates[start_pos][0] - input_coordinates[next_pos][0] )
			if( diff_x_coord ) :
				slope=( input_coordinates[start_pos][1] - input_coordinates[next_pos][1] ) / (diff_x_coord * 1.0);
				#print "###" ,slope, input_coordinates[start_pos][0] , input_coordinates[next_pos][0],input_coordinates[start_pos][1] , input_coordinates[next_pos][1]
				if( slope==-0.0 ):
					slope=0.0
				slopes.append(slope)
			else :
				slopes.append(None)

			next_pos=next_pos+1

		#now find how many have same slopes
		print "Before checking for collinearity, the slopes are : ",slopes
		print_collinear_points(slopes, min_points_required, start_pos);

		#clear the list
		slopes[:]=[]

#-----------------------------------------------------------------
def main():

	create_random_input_coordinates()
	find_collinear_points(3)

main()

