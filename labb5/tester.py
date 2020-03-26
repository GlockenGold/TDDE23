from labb5 import *

def run_tests():
    test_combine_images()
    test_pixel_constraint()
    test_generator_from_image()
    print("All tests passed")

def test_pixel_constraint():
    """ Tests the functionaly pixel_constraint to make sure we get expected
    outputs and returns True if all tests are passed.
    """

    #test_cases is structured (case1, case2) where every case has
    #((constraint1, constraint2...), input pixel, excpected output)
    test_cases = (((100, 60, 128, 60, 200, 100), (80, 80, 120), 0)\
                  , ((60, 100, 60, 128, 100, 200), (80, 80, 120), 1)\
                  , ((0, 300, 50, 52, 0, 200), (280, 51, 50), 1)\
                  , ((0, 255, 0 ,255, 0 ,255), "inte tuple", None)\
                  , ("inte en pixel", (80, 80, 120), None))

    for elem in test_cases:
        a = pixel_constraint(elem[0][0], elem[0][1], elem[0][2], \
                             elem[0][3], elem[0][4], elem[0][5])
        assert a(elem[1]) == elem[2]


def test_generator_from_image():
    """Tests the functionaly generator_from_image to make sure we get expected
    outputs and returns True if all tests are passed.
    """

    test_cases = ((((100, 100, 100), (20, 150, 255), (300, 255, 300)), 2, \
                   (300, 255, 300)), (((260, 260, 300), (00, 000, 255), \
                                       (150, 150, 150)), 0, (260, 260, 300)),\
                  (((100, 100, 100), (20, 150, 255), (300, 255, 300)), 96, \
                   None))

    for elem in test_cases:
        a = generator_from_image(elem[0])
        assert a(elem[1]) == elem[2]



def test_combine_images():
    """Tests the functionaly combine_images to make sure we get expected
    outputs and returns True if all tests are passed.
    First two tests assert that basic functionality is correct, third test tests
    two images of different sizes, and the fourth test tests invalid input type.
    """

    # input image list for every test case
    img_lsts = (((1, 1, 1), (85, 85, 85), (200, 200, 200)), \
                ((75, 101, 101), (256, 256, 256), (75, 101, 101)), \
                ((75, 101, 101), (256, 256, 256), (75, 101, 101)), \
                "not a pixel")

    # 2 generators for every test case
    generators = (generator_from_image(((255, 0, 0), (255, 0, 0), (255,0, 0))),\
                  generator_from_image(((0, 255, 0), (0, 255, 0), (0,255 ,0))),\
                  generator_from_image(((255, 0, 0), (255, 0, 0), (255,0,0))),\
                  generator_from_image(((0, 255, 0), (0,255,0), (0,255,0))),\
                  generator_from_image(((0, 255, 0), (0, 0, 10))), \
                  generator_from_image(((0, 0, 255), (0, 20, 0), (0, 10, 0))), \
                  generator_from_image(((0, 255, 0), (0, 0, 0), (0, 0 ,0))), \
                  generator_from_image(((0, 0, 0), (0, 0, 0), (0, 0, 0))))

    # expected output for every testcase
    test_results = ([(255, 0, 0), (255, 0, 0), (0, 255, 0)], \
                    [(255, 0, 0),(0, 255, 0), (255, 0, 0)], \
                    None, None)

    # condition function for every test case
    conditions = (pixel_constraint(0, 100, 0, 100, 0, 100), \
                  pixel_constraint(50, 300, 100, 255, 0, 102), \
                  pixel_constraint(0, 255, 0, 15, 0, 20), \
                  pixel_constraint(0, 255, 0, 255, 0, 255))

    # every loop asserts that a test case gets the expected result
    for i in range(len(img_lsts)):
        assert combine_images(img_lsts[i], conditions[i], generators[i*2], generators[i*2+1]) == test_results[i]





