import pyautogui as py
import time
x = 313
y = 426
drag=0
fixDrag = 85
fixDragCond = fixDrag*9
py.click(150,16)
for i in range(54):
    py.moveTo(650,104,0.2)
    py.click(650,104)
    if y>972:
        y = 973
        if drag<fixDragCond:
            py.moveTo(x,y,0.5)
            drag += fixDrag
            py.dragTo(x,y-drag,1)
            py.moveTo(x, y, 0.5)
            py.click(x,y)

        elif drag<fixDragCond*2:
            py.moveTo(x, y, 0.5)
            drag -= fixDragCond
            py.dragTo(x, y - 810, 1)
            py.moveTo(x, y, 0.5)
            drag += fixDrag
            py.dragTo(x, y - drag, 1)
            py.moveTo(x, y, 0.5)
            py.click(x, y)
            drag+=fixDragCond

        elif drag<fixDragCond*3:
            py.moveTo(x, y, 0.5)
            drag -= fixDragCond
            py.dragTo(x, y - 810, 1)
            py.moveTo(x, y, 0.5)
            drag -= fixDragCond
            py.dragTo(x, y - 810, 1)
            py.moveTo(x, y, 0.5)
            drag += fixDrag
            py.dragTo(x, y - drag, 1)
            py.moveTo(x, y, 0.5)
            py.click(x, y)
            drag += fixDragCond*2

        elif drag<fixDragCond*4:
            py.moveTo(x, y, 0.5)
            drag -= fixDragCond
            py.dragTo(x, y - 810, 1)
            py.moveTo(x, y, 0.5)
            drag -= fixDragCond
            py.dragTo(x, y - 810, 1)
            py.moveTo(x, y, 0.5)
            drag -= fixDragCond
            py.dragTo(x, y - 810, 1)
            py.moveTo(x, y, 0.5)
            drag += fixDrag
            py.dragTo(x, y - drag, 1)
            py.moveTo(x, y, 0.5)
            py.click(x, y)
            drag += fixDragCond*3
        else:
            py.moveTo(x, y, 0.5)
            drag -= fixDragCond
            py.dragTo(x, y - 810, 1)
            py.moveTo(x, y, 0.5)
            drag -= fixDragCond
            py.dragTo(x, y - 810, 1)
            py.moveTo(x, y, 0.5)
            drag -= fixDragCond
            py.dragTo(x, y - 810, 1)
            py.moveTo(x, y, 0.5)
            drag -= fixDragCond
            py.dragTo(x, y - 810, 1)
            py.moveTo(x, y, 0.5)
            drag += fixDrag
            py.dragTo(x, y - drag, 1)
            py.moveTo(x, y, 0.5)
            py.click(x, y)
            drag += fixDragCond*4
    else:
        py.moveTo(x,y,0.5)
        py.click(x,y)
        y+=78
    for t in reversed(range(0, 7)):
        print("Waiting for " + str(t) + " sec\r", end="")
        time.sleep(1)