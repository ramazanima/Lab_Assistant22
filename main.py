# ------------------------------------------------------------------------------------------------------------------
# Author: Ali Ramazani
# Professor: Dr. Patrick Shepherd
# Class: Software Design & Implementation
# ID: B00794836
# Final Project | Electronics Laboratory Assistant | Equipment Finder
# December 13, 2022
# --------------------------------------------------------------------------------------------------------------------
from tkinter import *
import model
from PIL import Image, ImageTk
import os

# Define the main window
class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Electronics Lab Assistant")
        self.root.iconbitmap("finder_icon.ico")
        self.root.geometry("520x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#FFFAFA")

        # Define fonts and colors
        self.large_font = ('SimSun', 14)
        self.medium_font = ('SimSun', 12)
        self.small_font = ('SimSun', 10)

        # Create frame
        self.upper_frame = LabelFrame(self.root, width=500, height=40, text=" Berea College Electronics Laboratory Assistant", font=self.large_font, bg="#FFFAFA")
        self.upper_frame.grid(padx=10, pady=5)
        self.upper_frame.grid_propagate(False)

        # Define output frame
        self.output_frame = LabelFrame(self.root, width=500, height=200, bg="#FFFAFA")
        self.output_frame.grid(pady=5)
        self.output_frame.grid_propagate(False)

        self.picture_frame = LabelFrame(self.root, width=500, height=250, bg="#FFFAFA")
        self.picture_frame.grid(pady=5)
        self.picture_frame.grid_propagate(False)

        self.option_selected = StringVar()
        self.default_text = 'Select an equipment'
        self.option_selected.set(self.default_text)

        OptionMenu(self.root, self.option_selected, *model.get_equipment_names()).grid(padx=10, pady=10)

        self.label_location_var = StringVar()
        self.label_location_var.set('')
        self.label_location = Label(self.output_frame, textvariable=self.label_location_var,
                                    font=self.medium_font, bg="#FFFAFA", wraplength=500)
        self.label_description_var = StringVar()
        self.label_description_var.set('')
        self.label_description = Label(self.output_frame, textvariable=self.label_description_var,
                                       font=self.medium_font, bg="#FFFAFA", wraplength=500)

        self.label_picture = Label(self.picture_frame, image=None)
        self.label_picture.image = None

        self.label_location.grid()
        self.label_description.grid()
        self.label_picture.place(relx=0.5, rely=0.5, anchor=CENTER)

        Button(self.root, text='Find', font=self.medium_font, command=self.find).grid()

        self.root.mainloop()

    def find(self):
        if self.option_selected.get() != self.default_text:
            info = model.get_info(self.option_selected.get())
            self.label_location_var.set('Location : ' + info[0][2])
            self.label_description_var.set(info[0][3])

            path = os.path.join(os.getcwd() + info[0][4].replace('/', '\\'))
            im = Image.open(path).resize((200, 200))
            ph = ImageTk.PhotoImage(im)

            self.label_picture.configure(image=ph)
            self.label_picture.image = ph
            self.root.update()

def main():
    # Define root window
    GUI()

main()
