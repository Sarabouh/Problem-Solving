import cv2
import numpy as np
import os

class Homography:

    def make_dstimg(self, im_src):
        im_dst = im_src.copy()
        for i in range(im_src.shape[0]):
            for j in range( im_src.shape[1]):
                im_dst[i][j] = 0
        return im_dst

    def homography(self, a,b,c,d,im_src):
        current = "/".join(os.path.dirname(__file__).split("/"))
        input_path = current + "/input/"

        # Four corners of the item in source image
        pts_src = np.array([a,b,c,d])

        # Read destination image.
        #im_dst = self.make_dstimg(im_src)
        im_dst = cv2.imread(input_path + "destt.png")

        # Four corners of the item in destination image.
        pts_dst = np.array([[841, 2933],[839, 415], [698, 415],[1694, 2933]])
        #pts_dst = np.array([[0, 0],[im_dst.shape[0], 0], [im_dst.shape[0], im_dst.shape[1]] ,[0, im_dst.shape[1]] ])
        print('dest shape========', im_dst.shape[0]," " ,im_dst.shape[1])

        # Calculate Homography
        h, status = cv2.findHomography(pts_src, pts_dst)

        # Warp source image to destination based on homography
        im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))

        return im_out, h



    '''imgs = '/home/sara/PycharmProjects/Research/input/book2.jpg'
    homography([141, 131], [480, 159], [493, 630], [64, 601], imgs)
    '''