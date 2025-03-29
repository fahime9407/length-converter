from tkinter import *
from tkinter import ttk

length, current_unit, requested_unit = 0, '', ''

def convert():
    try :
        convert_dict = {"m": 1, "cm": 0.01, "mm": 0.001, "km": 1000, "inch": 0.0254, "ft": 0.3048, "yd": 0.9144, "mile": 1609.344}
        length, current_unit, requested_unit = float(e1.get()), combo_box1.get(), combo_box2.get() # receive informations
        # first we convert lenght to meter
        length = length * convert_dict[current_unit]
        # then we convert it to ither units
        result_length = length / convert_dict[requested_unit]
        # show in result lable
        lable_result.config(text= f"result : {result_length: .2f}")
    except ValueError : # if invalid input
        lable_result.config(text= "invalid input!")

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
combo_box1 = ttk.Combobox(root, values= ["m", "cm", "mm", "km", "inch", "ft", "yd", "mile"], width= 15)
combo_box1.place(x= 80, y= 35)
# requested unit
lable3 = Label(root, text= "requested unit : ").place(x= 0, y= 70)
combo_box2 = ttk.Combobox(root, values= ["m", "cm", "mm", "km", "inch", "ft", "yd", "mile"], width= 15)
combo_box2.place(x= 93, y= 70)
# convert button
button1 = Button(root, text= "convert", width= 30, command= convert, activebackground= "green", activeforeground= "red")
button1.place(x= 15, y= 100)
# show result
lable_result = Label(root, text= "result .....", bg= "lightgray")
lable_result.place(x= 0, y= 135)
# close button
button2 = Button(root, text= "Done", command= root.destroy, width= 30, activebackground= "black", activeforeground= "white").place(x= 15, y= 160)

root.mainloop()