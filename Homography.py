import cv2
import numpy as np

class Homography:

    def make_dstimg(self, im_src):
        im_dst = im_src.copy()
        for i in range(im_src.shape[0]):
            for j in range( im_src.shape[1]):
                im_dst[i][j] = 0
        return im_dst

    def homography(self, a,b,c,d,im_src):

        # Four corners of the item in source image
        pts_src = np.array([a,b,c,d])

        # Read destination image.
        im_dst = self.make_dstimg(im_src)

        # Four corners of the item in destination image.
        #pts_dst = np.array([[318, 256],[534, 372],[316, 670],[73, 473]])
        pts_dst = np.array([[0, 0],[im_dst.shape[0], 0], [im_dst.shape[0], im_dst.shape[1]] ,[0, im_dst.shape[1]] ])

        # Calculate Homography
        h, status = cv2.findHomography(pts_src, pts_dst)

        # Warp source image to destination based on homography
        im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))
        return im_out, h



    '''imgs = '/home/sara/PycharmProjects/Research/input/book2.jpg'
    homography([141, 131], [480, 159], [493, 630], [64, 601], imgs)
    '''