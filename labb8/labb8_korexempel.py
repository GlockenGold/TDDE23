from calendar import *

def test_8C():
    create("asd")
    book("asd", 20, "sep", "08:00", "10:00", "Rob train")
    book("asd", 20, "sep", "13:15", "17:00", "Escape with loot")
    show("asd", 20, "sep")
    remove("asd", 20, "sep", "08:00")
    show("asd", 20, "sep")


    create("Jane")
    book("Jane", 20, "sep", "08:15", "10:00", "TDDE24")
    book("Jane", 20, "sep", "10:15", "12:00", "TDDE24")
    book("Jane", 20, "sep", "15:15", "17:00", "TDDD70")
    show("Jane", 20, "sep")
    remove("Jane", 20, "sep", "15:15")
    show("Jane", 20, "sep")


def test_8D():
    create("Karl")
    book("Karl", 20, "sep", "08:00", "10:00", "Rob train")
    book("Karl", 20, "sep", "13:15", "13:00", "Escape with loot")
    show("Karl", 20, "sep")
    show_free("Karl", 20, "sep", "08:00", "17:00")

    create("Lars")
    book("Lars", 20, "sep", "08:15", "10:00", "TDDE24")
    book("Lars", 20, "sep", "10:15", "12:00", "TDDE24")
    book("Lars", 20, "sep", "15:15", "17:00", "TDDD70")
    show("Lars", 20, "sep")
    show_free("Lars", 20, "sep", "00:00","23:00")

#
