import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--order', type=str, default='original_order')
parser.add_argument('-m', '--method', type=str, default='random')
parser.add_argument('-d', '--dataset', type=str, default='chair')
# parser.add_argument('-i', '--iteration', type=int, default=10000)
args = parser.parse_args()

iterations = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 10000]
image_files = []

for iteration in iterations:
    root_dir = '/home/daeunlee/workspace/DNGaussian/output/' + str(args.order) + '/' + str(args.method) + '/' + str(args.dataset) + '/test/ours_' + str(iteration)
    # Path to the directory containing the images
    image_dir = root_dir + '/renders/00003.png'
    
    

    # Append the list of image file name('00007.png') to the list
    image_files.append(image_dir)

# Output video file name
output_file = '/home/daeunlee/workspace/DNGaussian/output/' + str(args.order) + '/' + str(args.method) + '/' + str(args.dataset) + '/' + str(args.dataset) + 'video3.mp4'

if not image_files:
    print("No image files found in the directory.")
else:
    # Get the dimensions of the first image
    image = cv2.imread(image_files[0])
    if image is None:
        print(f"Failed to read the image: {image_files[0]}")
    else:
        height, width, _ = image.shape
        # Create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video = cv2.VideoWriter(output_file, fourcc, 30, (width, height))
        # Iterate through the image files and write them to the video
        for image_file in image_files:
            image = cv2.imread(image_file)
            if image is None:
                print(f"Failed to read the image: {image_file}")
                continue
            for i in range(30):
                video.write(image)
            # video.write(image)
        # Release the VideoWriter object
        video.release()
        print(f"Video saved as {output_file}")