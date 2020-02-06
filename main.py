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
    image = cv2.imread(input_path + "source.jpg")
    print('source shape========', image.shape[0], " ", image.shape[1])


    homography = h.Homography()
    dist = d.Distance()

<<<<<<< HEAD
    img_out, h_matrix = homography.homography([141, 131], [480, 159], [493, 630], [64, 601], image)
    print(h_matrix)
=======
    image_copy = image.copy()
    dest_img = cv2.imread(input_path + "desti.jpg")

    #img_out, h_matrix = homography.homography([141, 131], [480, 159], [493, 630], [64, 601], image)
    img_out, h_matrix = homography.homography([1132, 1343], [1132 , 1555], [ 1564, 1556], [1565,1345], image)
    '''cv2.line(image_copy, (1132, 1343), (1132 , 1555),
             (0, 255, 0), 5)'''
>>>>>>> 0fdeec090750733dc08e2cc25bd2b0c969e2fcea

    # dist.fixjson("QIL/yoloJson.json", "QIL/yoloJson2.json")

    objects = dist.getObj(current + "/yoloJson3.json")
    distances = dist.calculateDistance(objects)
    img_dist = dist.drawlines(image, distances, objects)
    print('Original image distance', distances)

    output_image_name = output_path + "result" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(output_image_name, img_dist)

    h_objects = dist.transformdict(objects, h_matrix)
    h_distances = dist.calculateDistance(h_objects)
    h_img_dist = dist.drawlines(img_out, h_distances, h_objects)
    print('homographed image distance', h_distances)

    h_output_image_name = output_path + "homography_result" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(h_output_image_name, h_img_dist)

    '''    o_image_name = output_path + "test" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(o_image_name, image_copy)'''

    obj = dist.getObj(current + "/yoloJson4.json")
    distn = dist.calculateDistance(obj)
    img_dist = dist.drawlines(dest_img, distn, obj)
    print('Destination image distance', distn)

    input_image_name = output_path + "destination" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(input_image_name, img_dist)


if __name__ == "__main__":
    main()
