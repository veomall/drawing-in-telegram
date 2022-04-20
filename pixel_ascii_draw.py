from tkinter import *


def paint(event):
    x, y = event.x // 20, event.y // 20
    c.create_rectangle(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill='black')
    field[x][y] = 1


def clear(event):
    x, y = event.x // 20, event.y // 20
    c.create_rectangle(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill='white')
    field[x][y] = 0


field = [[0 for j in range(32)] for i in range(32)]
field[0][0] = '.  '

root = Tk()
root.geometry('640x640+200+100')

c = Canvas(root, width=640, height=640, bg='white')
c.pack()

for i in range(32):
    for j in range(32):
        c.create_rectangle(i * 20, j * 0, i * 20 + 20, j * 20 + 20)

root.bind('<Button-1>', paint)
root.bind('<B1-Motion>', paint)
root.bind('<Button-3>', clear)
root.bind('<B3-Motion>', clear)
root.mainloop()
f = open('pad.txt', 'w')
for i in range(32):
    k = 0
    for j in range(32):
        if field[j][i] == 0:
            if k % 2 == 0:
                f.write('   ')
            else:
                f.write('    ')
            k += 1
        elif field[j][i] == 1:
            f.write('@')
        else:
            f.write('.  ')
    f.write('\n')
