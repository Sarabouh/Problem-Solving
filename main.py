import Distance as d
import Homography as h
import cv2
import os
from datetime import datetime

def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

def main():
    current = "/".join(os.path.dirname(__file__).split("/"))
    output_path = current + "/output/"
    input_path = current + "/input/"
    image = cv2.imread(input_path + "cap.png")

    homography = h.Homography()
    dist = d.Distance()

    img_out, h_matrix = homography.homography([141, 131], [480, 159], [493, 630], [64, 601], image)
    print(h)

    # dist.fixjson("Research/yoloJson.json", "Research/yoloJson2.json")

    objects = dist.getObj(current + "/yoloJson2.json")
    distances = dist.calculateDistance(objects)
    img_dist = dist.drawlines(image, distances, objects)

    output_image_name = output_path + "result" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(output_image_name, img_dist)

    h_objects = dist.transformdict(objects, h_matrix)
    h_distances = dist.calculateDistance(h_objects)
    h_img_dist = dist.drawlines(img_out, h_distances, h_objects)

    h_output_image_name = output_path + "homography_result" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(h_output_image_name, h_img_dist)


if __name__ == "__main__":
    main()
