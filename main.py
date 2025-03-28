from tkinter import *
from tkinter import ttk
# create a window
root =Tk()
root.title("converter")
root.geometry("250x200")
# receive length
lable1 = Label(root, text= "length : ").place(x= 0, y= 5)
e1 = Entry(root)
e1.place(x= 50, y= 7)
# receive current unit
lable2 = Label(root, text= "current unit : ").place(x= 0, y= 35)
combo_box1 = ttk.Combobox(root, values= ["m", "cm", "mm", "km", "in", "ft", "yd", "ml"], width= 15)
combo_box1.place(x= 80, y= 35)
# requested unit
lable3 = Label(root, text= "requested unit : ").place(x= 0, y= 70)
combo_box2 = ttk.Combobox(root, values= ["m", "cm", "mm", "km", "in", "ft", "yd", "ml"], width= 15)
combo_box2.place(x= 93, y= 70)
# convert button
button1 = Button(root, text= "convert", width= 30)
button1.place(x= 15, y= 100)
# show result
lable_result = Label(root, text= "result .....")
lable_result.place(x= 0, y= 140)
# close button
button2 = Button(root, text= "Done", command= root.destroy, width= 30).place(x= 15, y= 160)

root.mainloop()