"""
Name: Riva Kansakar
CSC 201
Programming Project 2

This program (complete a description)

Assistance Documentation: This program uses the .art file and
creates circles of random pixels created by the art_maker. This
program reads every line of the file created by the art_maker
and identifies x, y coordinates, color and radius 5000 times
(because there are 5000 lines). Also, program this adjusts
to the width size if the size of the image is smaller. This
program also exits if the file selected doesn't have .art


"""
from graphics import *
import tkinter as tk
import sys
from tkinter import filedialog

WINDOW_SIZE = 600

def display(artFileName):
    fin = open(artFileName, 'r')
    ext = artFileName.rfind('.')
    afterExt = artFileName[ext: ]
    
    if afterExt == '.art':
        
        window = GraphWin("Art Viewer", WINDOW_SIZE, WINDOW_SIZE)
        window.setBackground('black')
        

        
        width = int(fin.readline())
        
        for line_f in fin:
            

                
            strip = line_f.strip()
            line = strip.split()

            x = int(line[0])
            y = int(line[1])
            radius = int(line[2])
            r = int(line[3])
            g = int(line[4])
            b = int(line[5])
            
            color = color_rgb(r, g, b)
            
            circle = Circle(Point(x*(WINDOW_SIZE/width),y*(WINDOW_SIZE/width)), radius)
            circle.setFill(color)
            circle.setOutline(color)
            circle.draw(window)

        fin.close()
        
    else:
        print("Invalid file format. Must choose a 'art' file. Ending execution.")
        sys.exit(-1)

def main():
    # opens a file dialog to choose a file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    print(file_path)
    display(file_path)

main()



