import os
import random 
from shlex import join
import shutil

source_folder = r'D:\Downloads\archive\real_vs_fake\real-vs-fake\train\fake'
destination_folder = r'D:\Downloads\Dataset\Fake'

num_images_to_select = 5000

all_images = os.listdir(source_folder)

selected_images = random.sample(all_images, num_images_to_select)

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for image in selected_images:
    source_path = os.path.join(source_folder, image)
    destination_path = os.path.join(destination_folder, image)
    shutil.copyfile(source_path, destination_path)

print("Images copied successfully!!")