import sys
sys.path.append("../../")

def press(b):
    if b == "U":
        t.fd(100)

from appJar import gui
app=gui()
t = app.addTurtle("t1")
canvas = app.addCanvas("c1")
canvas.create_oval(10, 10, 100, 100, fill="red", outline="blue", width=3)
canvas.create_line(0, 0, 255, 255, width=5)
canvas.create_line(0, 255, 255, 0, dash=123)
app.addButtons(["L", "R", "U", "D"], press)
app.go()
