# ------------------------------------------------------------------------------------------------------------------
# Author: Ali Ramazani
# ID: B00794836
# Final Project | Electronics Laboratory Assistant | Equipment Finder
# December 13, 2022
# --------------------------------------------------------------------------------------------------------------------
from tkinter import *
import model
from PIL import ImageTk

# Define the main window
class GUI:
    def __init__(self, root):
        root.title("Electronics Lab Assistant")
        root.iconbitmap("finder_icon.ico")
        root.geometry("500x500")
        root.resizable(False, False)
        root.configure(bg="#FFFAFA")

        # Define fonts and colors
        sky_color = "#76c3ef"
        grass_color = "#aad207"
        output_color = "#dcf0fb"
        input_color = "#ecf2ae"
        large_font = ('SimSun', 14)
        medium_font = ('SimSun', 12)
        small_font = ('SimSun', 10)

        # Create frame
        upper_frame = LabelFrame(root, width=500, height=40, text="Berea College Electronics Laboratory Assistant", font=large_font, bg="#FFFAFA")
        upper_frame.pack(padx=10, pady=5)

        # Define output frame
        output_frame = LabelFrame(root, width=480, height=300, bg="#FFFAFA")
        output_frame.pack(pady=5)
        output_frame.propagate(False)

        option_selected = StringVar()
        default_text = 'Select an equipment'
        option_selected.set(default_text)

        OptionMenu(root, option_selected, *model.get_equipment_names()).pack(padx=10, pady=10)

        label_location = Label(root, text=' ', bg="#FFFAFA")
        label_description = Label(root, text=' ', bg="#FFFAFA")

        label_location.pack()
        label_description.pack()

        def find():
            if option_selected.get() != default_text:
                info = model.get_info(option_selected.get())
                Label(output_frame, text='Location : ' + info[0][2], font=medium_font, anchor=CENTER, wraplength=300, bg="#FFFAFA").pack()
                Label(output_frame, text=info[0][3], font=medium_font, justify=CENTER, wraplength=450, bg="#FFFAFA").pack()
                Label(output_frame, text=info[0][4], font=medium_font, justify=CENTER, wraplength=450, bg="#FFFAFA").pack()

        Button(root, text='Find', font=medium_font, command=find).pack()


def main():
    # Define root window
    root = Tk()
    # Make a root window object
    GUI(root)
    # Closes the mainloop
    root.mainloop()
main()