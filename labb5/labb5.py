import cv2
import cvlib
import numpy
import close_openCV
import math


# Både del A och del B är redo för redovisning

def closeWindow(delay):
    """ Waits for key for delay sec and then closes all openCV windows """
    close_openCV.closeWindow(delay)

# =================== DEL A ===================

def start_5a():
    """
    Startar Uppgift 5a
    """
    img = cv2.imread("fin-bild.jpg", 1)
    return cvimg_to_list(img)


def cvimg_to_list(img):
    """
    Converts image to list
    """
    height = img.shape[0]
    width = img.shape[1]
    cvlist = []
    try:
        for y in range(height):
            for x in range(width):
                cvlist.append((img[y, x][0], img[y, x][1], img[y, x][2]))
    except TypeError:
        return None
    except IndexError:
        return None

    return cvlist


# ===== 5B ======

def Neg_Gaus_Blur(x, y):
    """ Returns a negative gaussian blur value for coordinates x and y """
    s = 4.5
    return (-1/(2*math.pi*s**2)) * math.e**(-(x**2 + y**2)/(2*s**2))


def unsharp_mask(n):
    """
    Creates negative gaussian blur mask of size n
    """
    [0, -1, 1, -2, 2]
    return [[1.5 if x - n + 2 == 0 and y - n + 2 == 0 else \
        Neg_Gaus_Blur(x - n + 2, y - n + 2) for x in range(n)] \
        for y in range(n)]


# =================== DEL B ===================

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """ Returns a function is_sky that takes a pixel as input and
    returns 1 if it is within the given constraints otherwise 0 """
    def is_sky(px):
        try:
            if px[0] < hhigh and px[0] > hlow and px[1] < shigh and \
                px[1] > slow and px[2] < vhigh and px[2] > vlow:
                return 1
        except TypeError:
            return None
        except IndexError:
            return None
        return 0
    return is_sky


def start_5c():
    """ Function to test 5C """

    plane = cvimg_to_list(\
        cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV))
    plane_img = cv2.imread("plane.jpg")

    is_sky = pixel_constraint(100, 150, 50, 200, 100 ,255)
    sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane)))
    cv2.imshow("Hej", cvlib.greyscale_list_to_cvimg(sky_pixels,\
        plane_img.shape[0], plane_img.shape[1]))
    closeWindow(0)


def generator_from_image(img_lst):
    """ Takes an image in list form returns a function that given an index
    returns the RGB value of the pixel at that index """
    def rgb_value(i):
        try:
            if len(img_lst[i]) == 3:
                return img_lst[i]
            else:
                print("img_lst not rgb pixel")
        except TypeError:
            return None
        except IndexError:
            return None
    return rgb_value


def start_5d(file_name):
    """ Function to test 5D """

    original_img = cv2.imread(file_name)
    original_list = cvimg_to_list(original_img)

    generator = generator_from_image(original_img)
    new_list = [generator(i) for i in range(len(original_list))]

    cv2.imshow('original', original_img)
    cv2.imshow('new', cvlib.rgblist_to_cvimg(new_list, \
        original_img.shape[0], original_img.shape[1]))
    closeWindow(0)


def create_transform(condition, generator1, generator2):
    """ Returns a function that takes a pixel and pixel index and combines
    generator1 and generator2 based on condition. """
    def combine_pixels(px, i):
        try:
            return cvlib.add_tuples(cvlib.multiply_tuple\
                                    (generator1(i), condition(px)), \
                                     cvlib.multiply_tuple\
                                    (generator2(i), 1-condition(px)))
        except TypeError:
            return None
        except IndexError:
            return None
    return combine_pixels


def combine_images(img_list, condition, generator1, generator2):
    """ Returns a combined image from generator1 and generator2
    based on condition applied to img_list """
    try:
        if not isinstance(img_list, (list, tuple)):
            return None
        combine_pixels = create_transform(condition, generator1, generator2)
        img_map = map(combine_pixels, img_list, range(len(img_list)))
    except TypeError:
        return None
    except IndexError:
        return None
    result = list(img_map)
    for elem in result:
        if None in result:
            return None
    return result

import random
def start_5e():
    """ Function used to starttest 5E """

    plane_img = cv2.imread("plane.jpg")
    condition = pixel_constraint(100, 150, 50, 200, 100, 255)

    hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
    plane_img_list = cvimg_to_list(plane_img)
    
    def generator1(index):
        try:
            val = random.random() * 255 if random.random() > 0.99 else 0
            return (val, val, val)
        except TypeError:
            return None
        except IndexError:
            return None

    generator2 = generator_from_image(plane_img_list)

    result = combine_images(hsv_list, condition, generator1, generator2)

    cv2.imshow("a", cvlib.rgblist_to_cvimg(result, plane_img.shape[0], \
            plane_img.shape[1]))
    closeWindow(0)


def gradient_condition(px):
    """ Assuming px is a gray pixel returns how grey on a scale from 0 to 1"""
    return px[0] / 255

def start_5f():
    """ Combines images plane.jpg and flowers.jpg based on gradient.jpg using
    combine_images, gradient_condition, and generator_from_image """
    plane_img = cv2.imread("plane.jpg")
    flowers_img = cv2.imread("flowers.jpg")
    gradient_img = cv2.imread("gradient.jpg")

    plane_img_list = cvimg_to_list(plane_img)
    flowers_img_list = cvimg_to_list(flowers_img)
    gradient_img_list = cvimg_to_list(gradient_img)

    generator2 = generator_from_image(plane_img_list)
    generator1 = generator_from_image(flowers_img_list)

    result = combine_images(gradient_img_list, gradient_condition, \
                            generator1, generator2)

    cv2.imshow("OMG THAT IS AWSOME", cvlib.rgblist_to_cvimg(result, \
                gradient_img.shape[0], gradient_img.shape[1]))
    closeWindow(0)
