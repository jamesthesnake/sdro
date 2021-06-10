import argparse
from math import radians, sin, cos
import copy
import numpy as np
from matplotlib import pyplot as plt

reverse_turn={'port':'starboard','starboard':'port'}
def run_waves(start_coordinate,degrees,hor_length,vert_length,number_of_legs,turn_dir):
	wave_points=[]
	wave_points.append(start_coordinate)
	start_coordinates=copy.copy(start_coordinate)
	varchange=90
	if turn_dir=='starboard':
		hor_length*=-1
		varchange*=-1

	degrees-=varchange
	rad_degrees=radians(degrees)
	for i in range(number_of_legs*2):
		if i%2==0:
			start_coordinates[0]=start_coordinates[0]+vert_length*round(cos(rad_degrees),2)
			start_coordinates[1]=start_coordinates[1]+vert_length*round(sin(rad_degrees),2)
			varchange*=-1
		else:
			start_coordinates[0]=start_coordinates[0]+hor_length*round(cos(rad_degrees),2)
			start_coordinates[1]=start_coordinates[1]+hor_length*round(sin(rad_degrees),2)
		degrees+=varchange
		rad_degrees=radians(degrees)
		stand=copy.copy(start_coordinates)
		wave_points.append(stand)
	return wave_points
def test_case(start_coordinate,degrees,hor_length,vert_length,number_of_legs,turn_dir):
	assert run_waves(start_coordinate,degrees,hor_length,vert_length,number_of_legs,turn_dir)==run_waves(start_coordinate,degrees+180,hor_length,vert_length,number_of_legs,reverse_turn[turn_dir])
	assert run_waves(start_coordinate,degrees,hor_length,vert_length,number_of_legs,turn_dir)==run_waves(start_coordinate,degrees+360,hor_length,vert_length,number_of_legs,turn_dir)
def main():
	my_parser = argparse.ArgumentParser(description='List the content of a folder')

	# Add the arguments
	my_parser.add_argument('--lat',
		               metavar='lat', default=0.0,
		               type=float,
		               help='lattitude')
	my_parser.add_argument('--long',
		               metavar='long', default=0.0,
		               type=float,
		               help='longitude')
	my_parser.add_argument('--vertical_length','-vert_leg',nargs="?",
		               metavar='vert',default=3,
		               type=int,
		               help='length of vertical segments')
	my_parser.add_argument('--horizontal_length','-hor_leg',nargs="?",
		               metavar='hor',default=3,
		               type=int,
		               help='the length of horizontial segments')
	my_parser.add_argument("--number_of_legs",'-numb',nargs="?",
		               metavar='numb',default=5,
		               type=int,
		               help='number of iterations the horozontial and vetical switch')
	my_parser.add_argument('--degrees','-deg',nargs="?",
		               metavar='deg',default=0.0,
		               type=float,
		               help='degrees that you want to turn, 0 is the example given')
	my_parser.add_argument("--turn_dir",'-turn_dir',nargs="?",
		               metavar='turn_dir',choices=['port','starboard'],default='port',
		               type=str,
		               help='turn direction, port or starboard')
	# Execute the parse_args() method
	args = my_parser.parse_args()
	start_coordinate=[args.lat,args.long]
	degrees=args.degrees
	hor_length=args.horizontal_length
	number_of_legs=args.number_of_legs
	vert_length=args.vertical_length
	turn_dir=args.turn_dir
	array_point=run_waves(start_coordinate,degrees,hor_length,vert_length,number_of_legs,turn_dir)
	data = np.array(array_point)
	x, y = data.T
	plt.plot(x,y,'xb-')
	plt.quiver(x[:-1], y[:-1], x[1:]-x[:-1], y[1:]-y[:-1], scale_units='xy', angles='xy', scale=1)
	plt.show()


if  __name__ == "__main__":
	main()

