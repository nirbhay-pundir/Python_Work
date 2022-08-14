import time
import turtle as t
import random

menu_options = {
    1: 'All Colors',
    2: 'Red Range',
    3: 'Green Range',
    4: 'Blue Range',
    5: 'Random Color for n time',
    6: 'Exit'
}


def allColors():
    for i in range(256):
        for j in range(256):
            for k in range(256):
                color0 = "%02x" % i
                color1 = "%02x" % j
                color2 = "%02x" % k
                color = color0 + color1 + color2
                t.bgcolor("#" + color)
                time.sleep(0.01)


def redColorRange():
    for i in range(256):
        color0 = "%02x" % i
        color = color0 + "0000"
        t.bgcolor("#" + color)
        time.sleep(0.01)


def blueColorRange():
    for i in range(256):
        color0 = "%02x" % i
        color = "0000" + color0
        t.bgcolor("#" + color)
        time.sleep(0.01)


def greenColorRange():
    for i in range(256):
        color0 = "%02x" % i
        color = "00" + color0 + "00"
        t.bgcolor("#" + color)
        time.sleep(0.01)


def randomColor(r):
    for i in range(r):
        color0 = "%02x" % random.randint(0, 255)
        color1 = "%02x" % random.randint(0, 255)
        color2 = "%02x" % random.randint(0, 255)
        color = color0 + color1 + color2
        t.bgcolor("#" + color)
        time.sleep(0.1)


def print_menu(menu):
    for key in menu.keys():
        print(key, '--', menu[key])


while (True):
    print_menu(menu_options)
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')

    if option == 1:
        allColors()
    elif option == 2:
        redColorRange()
    elif option == 3:
        greenColorRange()
    elif option == 4:
        blueColorRange()
    elif option == 5:
        n = int(input("Enter number for which color should change: "))
        randomColor(n)
    elif option == 6:
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 6.')
