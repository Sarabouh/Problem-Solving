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
    image = cv2.imread(input_path + "src2.png")
    print('source shape========', image.shape[0], " ", image.shape[1])


    homography = h.Homography()
    dist = d.Distance()

    image_copy = image.copy()
    dest_img = cv2.imread(input_path + "dst0.jpg")

    img_out, h_matrix = homography.homography([0, 209], [209, 179], [449, 470], [43, 518], image)
    #dst/src1
    #img_out, h_matrix = homography.homography([353, 418],[497, 410],[499 , 467], [353,467] , image)
    #dst/src 0
    #img_out, h_matrix = homography.homography([271, 61], [644, 44], [685, 287], [229, 280], image)
    '''cv2.line(image_copy, (1132, 1343), (1132 , 1555),
             (0, 255, 0), 5)'''

    # dist.fixjson("QIL/yoloJson.json", "QIL/yoloJson2.json")

    objects = dist.getObj(current + "/JSON/yoloJson2.json")
    distances = dist.calculateDistance(objects)
    img_dist = dist.drawlines(image, distances, objects)
    print('Original image distance ', distances['o1']['o2'])

    output_image_name = output_path + "result" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(output_image_name, img_dist)

    h_objects = dist.transformdict(objects, h_matrix)
    print(h_objects)
    h_distances = dist.calculateDistance(h_objects)
    h_img_dist = dist.drawlines(img_out, h_distances, h_objects)
    print('homographed image distance ', h_distances['o1']['o2'])

    h_output_image_name = output_path + "homography_result" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(h_output_image_name, h_img_dist)

    '''obj = dist.getObj(current + "/JSON/obj_dst0.json")
    distn = dist.calculateDistance(obj)
    img_dist = dist.drawlines(dest_img, distn, obj)
    print('Destination image distance ', distn['o1']['o2'])

    input_image_name = output_path + "destination" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(input_image_name, img_dist)'''


if __name__ == "__main__":
    main()
