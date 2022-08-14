import turtle as te

screen = te.Screen()
screen.setup(width=1.0, height=1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

te.bgcolor('black')
te.speed(0)
te.hideturtle()
for i in range(535):
    te.color('red')
    te.circle(i)
    te.color('orange')
    te.circle(i * 0.8)
    te.right(3)
    te.forward(5)
te.done()
