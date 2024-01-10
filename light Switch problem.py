# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 09:51:46 2023

@author: byc
"""

import Tkinter as tk
import numpy
import xlrd
import xlwt


N=8
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle
radius = 20



def save(path='condition.xls'):#保存进度
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('Worksheet')
    for i in range(N):
        for j in range(N):
            if (i-j)%N == 1 or (j-i)%N == 1:
                worksheet.write(i,j,1)
            else:
                worksheet.write(i,j,0)
    workbook.save(path)
    for i in range(N,2*N):
        for j in range(N,2*N):
            if (i-j)%N == 1 or (j-i)%N == 1:
                worksheet.write(i,j,1)
            else:
                worksheet.write(i,j,0)
    workbook.save(path)
    for i in range(N):
        for j in range(N,2*N):
            if (i-j)%N == 0:
                worksheet.write(i,j,1)
            else:
                worksheet.write(i,j,0)
    workbook.save(path)
    for i in range(N,2*N):
        for j in range(N):
            if (i-j)%N == 0:
                worksheet.write(i,j,1)
            else:
                worksheet.write(i,j,0)
    workbook.save(path)

def dist(c1,c2):
    d =((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)**0.5
    return (d)
    

def get_adjcent_matrix():#读取进度
    Mat = numpy.zeros((2*N,2*N),dtype=int)
    workbook = xlrd.open_workbook('condition.xls')
    for sheet in workbook.sheets():
        if sheet.name == 'Worksheet':
            for i in range(2*N):
                line= []
                for j in range(2*N):
                    line.append(sheet.cell_value(i,j))
                Mat[i:]=line[0:2*N]
    return Mat




# Click
def on_click(e):
    print("hi")


def change_circle(event):
    c1 = [event.x,event.y]
    k = 0
    for j in range(2*N):
        c2 = center[j]
        if dist(c1,c2)<= radius + 10:
            k=j
            for i in range(2*N):
                if Mat[k,i]:
                    color_list[i] = color_list[i] ^ True
                    my_canvas.itemconfigure(button[i], fill=Color[color_list[i]])
# Create the frame with a label inside



root = tk.Tk()
root.title('temp')
root.geometry("1200x1200")
Color = ["black","white"]
color_list = []
for i in range(2*N):
    color_list.append(False)
save()
Mat = get_adjcent_matrix()
my_canvas = tk.Canvas(root,width=800,height=800,bg='white')
button = []
center = []
for i in range(N):
    x = 400 + numpy.cos(2 * i * numpy.pi / N)*150
    y = 400 + numpy.sin(2 * i * numpy.pi / N)*150
    b = my_canvas.create_circle(x, y, radius, fill=Color[color_list[i]], outline="#DDD", width=4)
    center.append([x,y])
    button.append(b)
    my_canvas.create_line(x, y, 400 + numpy.cos(2 * (i-1) * numpy.pi / N)*150, 400 + numpy.sin(2 * (i-1) * numpy.pi / N)*150)
    my_canvas.create_line(x, y, 400 + numpy.cos(2 * (i+1) * numpy.pi / N)*150, 400 + numpy.sin(2 * (i+1) * numpy.pi / N)*150)
for i in range(N,2*N):
    x = 400 + numpy.cos(2 * i * numpy.pi / N)*300
    y = 400 + numpy.sin(2 * i * numpy.pi / N)*300
    b = my_canvas.create_circle(x, y, radius, fill=Color[color_list[i]], outline="#DDD", width=4)
    center.append([x,y])
    button.append(b)
    my_canvas.create_line(x, y, 400 + numpy.cos(2 * (i-1) * numpy.pi / N)*300, 400 + numpy.sin(2 * (i-1) * numpy.pi / N)*300)
    my_canvas.create_line(x, y, 400 + numpy.cos(2 * (i+1) * numpy.pi / N)*300, 400 + numpy.sin(2 * (i+1) * numpy.pi / N)*300)
    my_canvas.create_line(x, y, 400 + numpy.cos(2 * i * numpy.pi / N)*150, 400 + numpy.sin(2 * i * numpy.pi / N)*150)
# Packing
#button.pack()
#button.pack()
my_canvas.bind('<Button-1>', change_circle)
my_canvas.pack(side='left', expand='no', anchor='center', fill='y', padx=5, pady=5)
# Loop
root.mainloop()


