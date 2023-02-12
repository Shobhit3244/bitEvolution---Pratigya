# import tkinter
import tkinter
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("400*580")
app.title("Customtkinter Interface2")


def button_callback(combobox_1=None):
    print("Click here", combobox_1.get())


def slider_callback(value, progressbar_1=None):
    progressbar_1.set(value)

frame_2 = customtkinter.CTkFrame(master=app)
frame_2.grid(row=0, column=0, pady=20, padx=40,ipadx=20,ipady=40)

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(row=0, column=1, pady=20, padx=60)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT)
label_1.grid(pady=12, padx=10)

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.grid(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
button_1.grid(pady=12, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.grid(pady=12, padx=10)
slider_1.set(0.5)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
entry_1.grid(pady=12, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(master=frame_1,
                                           values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.grid(pady=12, padx=10)
optionmenu_1.set("CTkOptionMenu")

combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.grid(pady=12, padx=10)
optionmenu_1.set("CtkComboBox")

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
checkbox_1.grid(pady=12, padx=10)

radiobutton_var = tkinter.IntVar(value=1)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.grid(pady=12, padx=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.grid(pady=12, padx=10)

switch_1 = customtkinter.CTkSwitch(master=frame_1)
switch_1.grid(pady=12, padx=10)

app.mainloop()