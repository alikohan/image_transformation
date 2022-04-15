from tkinter import *
from PIL import Image
import threading
from logging import exception
import transformation
import colorspace

#creating instance of TK
root = Tk()

root.configure(background="#444")
hadProblem = False

def applyFormula():
    global hadProblem
    try:
        image = Image.open(entry1.get()) # Can be many different formats.
        pixels = image.load()
        function = entry2.get()

        if not transformation.testTransformationPlot(pixels, image.width, image.height, function):
            raise exception()
        elif(hadProblem):
            mainLabel.config(text = "problem has been resolved :)")
        
        thread = threading.Thread(target=transformation.transformationPlot, args=(
            pixels, image.width, image.height, function, image))
        thread.start()

    except:
        hadProblem = True
        mainLabel.config(text = "error! please check arguments.")

def grayscaleButton():
    image = Image.open(entry1.get()) # Can be many different formats.
    pixels = image.load()
    thread = threading.Thread(target=colorspace.convert, args=(pixels, image.width, image.height, "grayscale", image, entry1.get()))
    thread.start()
    
def closeButton():
    root.destroy()

#setting title for the window
root.title("constract")

mainLabel = Label(root, text="welcome!", font=("arial Bold", 15), fg="white", bg="#222", height=2)
mainLabel.grid(row=0, rowspan=2, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

Label(root, text="input file name :", font=("arial Bold", 15), fg="#dfb", bg="#222",
      height=0).grid(row=2, rowspan=2, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

Label(root, text="input formula :", font=("arial Bold", 15), fg="#dfb", bg="#222",
      height=0).grid(row=10, rowspan=2, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

Button(root, text="apply formula", font=('arial Bold', 25), bg="#222", fg="#8d2",
       command=applyFormula).grid(row=14, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

Button(root, text="convert to grayscale", font=('arial Bold', 15), bg="#222", fg="#895",
       command=grayscaleButton).grid(row=16, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

Button(root, text="EXIT", font=('arial Bold', 25), bg="#222", fg="#f33",
       command=closeButton).grid(row=18, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

entry1 = Entry(root, text='fileName', font='arial 25', justify='left')
entry1.grid(row=4, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
entry1.insert(0, 'test.jpg') #default text

entry2 = Entry(root, text='formula', font='arial 20', justify='left')
entry2.grid(row=12, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
entry2.insert(0, 'a = a + 50') #default text

root.mainloop()