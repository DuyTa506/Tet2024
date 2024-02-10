import os
import random
import time
import cv2
from pathlib import Path

rand_seed = 42

with open('tet.txt', 'r', encoding='utf-8') as file:
    questions = file.readlines()

data_list = []

for question in questions:
    question = question.strip()
    data_list.append(question)

def open_random_image(folder_path, display_duration=1):
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if image_files:
        selected_image = random.choice(image_files)
        image_path = Path(folder_path) / selected_image

        image = cv2.imread(str(image_path))

        if image is not None:
            height, width, _ = image.shape

            cv2.namedWindow('Random Image', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Random Image', int(width/1.5), int(height/1.5))

            cv2.imshow('Random Image', image)
            cv2.waitKey(0)

            time.sleep(display_duration)

            cv2.destroyAllWindows()
        else:
            print("Error reading the image.")
    else:
        print("Hết ảnh fence ơi.")


ROOT = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(ROOT, "images")

for i in range(rand_seed):
    seed_child = random.choice(data_list)
    print(seed_child)
    open_random_image(image_folder_path)
    #time.sleep(random.randint(0, 1))
