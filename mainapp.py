from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter

#setting up my app with the appropriate dependencies, including file types. For a trial I will only add png. I plan to add jpg and pdf later on.

#I set my terminal to a specific folder directory with the cd line. Researching libraries for the QR 
root = Tk()
root.title("Furniture QR Code Generator")
root.eval("tk::PlaceWindow . center")
#root.iconbitmap('c:/Users/Valerie/Documents/QR_code_gen_app.ico') fix and add if you want to add icon on window
root.geometry('500x600')
root.title("Furniture QR Code")
root.configure(background='azure')

def generate_code():
    #creating a file path + file dialog
    input_path = filedialog.asksaveasfilename(title="Save Image",
         filetyp=(("PNG File", ".png"), ("All Files", "*.*")))
    if input_path:
        if  input_path.endswith(".png"):
            #creates qr code from the entry box
             get_code = pyqrcode.create(my_entry.get())
            # saves the file as png
             get_code.png(input_path, scale=5)
        else:
            #adds png to the end of file name
            input_path = f'{input_path}.png'
            get_code = pyqrcode.create(my_entry.get()) 
            # saves file as png
            get_code.png(input_path, scale=5)
        #displays the QR code on the screen
        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))
        #this adds the image to label below
        my_label.config(image=get_image)

        my_entry.delete(0, END)
        #flash a finished message
        my_entry.insert(0, "Done!")
            
def clear_all():
    my_entry.delete(0, END)
    my_label.config(image='')

#creating the GUI
my_entry=Entry(root,font=("Cambria",20))
my_entry.pack(pady=20)
my_entry.place(relx=0.5, rely=0.3, anchor=CENTER)

my_button= customtkinter.CTkButton(root,width=120,
                         height=32, border_width=0, corner_radius=8,
                         text="Generate QR Code", command=generate_code)
my_button.place(relx=0.5, rely=0.4, anchor=CENTER)

my_button2= customtkinter.CTkButton(root,width=120,
                         height=32, border_width=0, corner_radius=8,
                         text="Clear", command=clear_all)
my_button2.place(relx=0.5, rely=0.5, anchor=CENTER)

my_label = Label(root, text='')
my_label.pack(pady=20)
my_label.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
