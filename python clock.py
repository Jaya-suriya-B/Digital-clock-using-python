from tkinter import*
a=Tk()
a.title("MY CLOCK")


from time import strftime

def time():
    string=strftime("%H:%M:%S:%p")
    a.config(text=string)
    a.after(1000,time)


a = Label(a, font=("Times New Roman",80),fg="white",bg="purple")
a.grid(row=1,column=3)

time()
a.mainloop()
    


