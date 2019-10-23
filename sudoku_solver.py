import cv2 
import numpy as np 
import matplotlib.pyplot as plt
from solver import *
import keras 
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from image_utils import *

image = cv2.imread('1.jpg')

dilated_image = preprocessing_image(image)

approx = find_sudoku_border(dilated_image)

aligned_image = align_sudoku(dilated_image, approx)

square_images_list = obtain_squares_list(aligned_image)

for i in range(81):
    plt.subplot(9,9,i+1), plt.imshow(square_images_list[i])
plt.show()

numbered_squares_list = detect_numbers(square_images_list)
print(numbered_squares_list)
model = create_model()

digits_dict = predict_digits(square_images_list, numbered_squares_list, model)

sudoku_string = create_string(digits_dict)

answer_dict = solve('003020600900305001001806400008102900700000008006708200002609500800203009005010300')

answers_list = list(answer_dict.items())

answered_image = write_answers_on_image(sudoku_string, aligned_image, answers_list)

aligned_answered_image = inverse_perspective(answered_image, approx, image)

final_answered_image = cv2.addWeighted(image, 0.5, aligned_answered_image, 0.5, 0.5)

#plt.imshow(answered_image,cmap='gray')
plt.show()




