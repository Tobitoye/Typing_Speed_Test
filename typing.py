from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random

root = Tk()
root.geometry("500x500")
root.configure(bg="black")

window = Tk()
window.geometry("550x500")
window.withdraw()



x = 0


def game():

    global x
    if x==0:
        root.withdraw()
        x=x+1
    window.deiconify()


    def check_result():
        end = timer()
        time_taken=end-start
        
        if entry.get("1.0", 'end-1c') == word:
            final=("passed You time was", time_taken)
            messagebox.showinfo("Passed", final)
        else:
            fail=("Invalid input, Upper and lower cases are significant")
            messagebox.showinfo("Invalid", fail)



                


    def finish():
        window.destroy()
        root.destroy()



    
    words = ("Goodness is a sharp guy", "This is a day in my life", "The constituition is not valid anymore", "You and I are made for ball")
    word = random.choice(words)

    x2 = Label(window, text=word, bg="black", fg="white", height=7, width=45, font="times 15")
    x2.place(x=40, y=100)

    x3 = Button(window, text="Submit!", font="times 20", bg="red", command=check_result)
    x3.place(x=170, y=240)

    entry = Text(window, bg="purple", fg="black", font="times 17")
    entry.place(x=16, y=280, height=75, width=400)

    b2 = Button(window, text="Done", font="times 13", bg='#ffc003', width=12, command=finish)
    b2.place(x=155, y=420)

    b3 = Button(window, bg="purple", fg="black", text="Retry?", font="times 13",  width=12, command=game)
    b3.place(x=265, y=420)
    start = timer()
    window.mainloop()




x1 = Label(root, text="Lets see how fast you can type!", bg="black", fg="white", font="times 30")
x1.place(x=60, y=50)

b1 = Button(root, text="Go!", width=15, bg='#03fcf8', font="times 25", command=game)
b1.place(x=140, y=250)




root.mainloop()
