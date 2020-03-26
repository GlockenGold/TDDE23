import cv2
import numpy

# ------------------------------------------
#  Helper functions
# ------------------------------------------
def multiply_tuple(tpl, mult):
    """
    Multiplies eac element of a tuple with a scalar (single number)

    (a,b,c) * k = (a*k, b*k, c*k)
    """
    return tuple(map(lambda x: x*mult, tpl))

def add_tuples(tpl1, tpl2):
    """
    Adds each element of two tuples

    (a,b,c) + (d,e,f) = (a+d, b+e, c+f)
    """
    return tuple(map(lambda t1, t2: t1+t2, tpl1, tpl2))


# -------------------------------------------
#  Converting between python list and images
# -------------------------------------------

def rgblist_to_cvimg(lst, height, width):
    """
    Creates a opencv image from a list of rgb tuples, a width and a height
    """
    # A 3d array that will contain the image data
    img = numpy.zeros((height, width, 3), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y,x,0] = pixel[0]
            img[y,x,1] = pixel[1]
            img[y,x,2] = pixel[2]

    return img

def greyscale_list_to_cvimg(lst, height, width):
    """
    Creates a grayscale opencv image from a list list of grayscale pixel values
    """
    img = numpy.zeros((height, width), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            img[y,x] = lst[y * width + x]

    return img
