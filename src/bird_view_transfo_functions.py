import numpy as np
import cv2


def compute_perspective_transform(corner_points,width,height,image):
	corner_points_array = np.float32(corner_points)
	img_params = np.float32([[0,0],[width,0],[0,height],[width,height]])
	matrix = cv2.getPerspectiveTransform(corner_points_array,img_params) 
	img_transformed = cv2.warpPerspective(image,matrix,(width,height))
	return matrix,img_transformed


def compute_point_perspective_transformation(matrix,list_downoids):

	list_points_to_detect = np.float32(list_downoids).reshape(-1, 1, 2)
	transformed_points = cv2.perspectiveTransform(list_points_to_detect, matrix)
	transformed_points_list = list()
	for i in range(0,transformed_points.shape[0]):
		transformed_points_list.append([transformed_points[i][0][0],transformed_points[i][0][1]])
	return transformed_points_list
