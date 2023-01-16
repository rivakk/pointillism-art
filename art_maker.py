"""
Name: Riva Kansakar
CSC 201
Programming Project 2

This program (complete a description): This program first checks to see if the file selected has .gif or
not. If it does, it will exit, otherwise it will create a .art file where it will store a random x, random
y, a random radius (ranging from 2-9) and it finds the pixel of the random x, y chosen. This is executed
5000 times.

Assistance Documentation: I used the book assigned to us by Zelle and also used the help of the website
GeeksforGeeks for some syntaxes.


"""
from graphics import *
import random
import tkinter as tk
import sys
from tkinter import filedialog

NUM_CIRCLES = 5000


def convert(imageFileName):
  
    ext = imageFileName.rfind('.')
    afterExt = imageFileName[ext: ]
    
    if afterExt == '.gif':
        
        image = Image(Point(0,0), imageFileName)
        file_name = imageFileName[:ext] + '.art'
        
        fout = open(file_name, 'w')
        width = image.getWidth()
        height = image.getHeight()
        
        fout.write (f'{width} \n')
        
        for i in range (NUM_CIRCLES):
            
            x = random.randrange(0, width)
            y = random.randrange(0, height)
            radius = random.randrange(2, 9)
            red = 0
            green = 0
            blue = 0
            red, green, blue = image.getPixel(x, y)
            
            fout.write(f'{x} {y} {radius} {red} {green} {blue}\n')
            
        fout.close()
        
    else:
        print("Invalid file format. Must choose a 'gif' file. Ending execution.")
        sys.exit(-1)


def main():
    # opens file dialog to choose a file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    convert(file_path)

main()
