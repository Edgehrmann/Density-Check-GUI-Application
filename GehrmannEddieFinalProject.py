# Import the Tkinter module for creating GUI
from tkinter import *
# Import the datetime module for getting the current date and time
import datetime
# Import pathlib module which provides an object-oriented interface to the file system
from pathlib import Path
# Import PIL module
from PIL import ImageTk, Image
# Import message box
from tkinter import messagebox


# Define a class for the main window of the program


class MainWindow:

    # Initialize the main window with three buttons
    def __init__(self, win):
        # Create a label to welcome the user
        lbl1 = Label(win, text='Welcome to the density check program!', relief=SUNKEN,
                     bg='#F5F5F5', font='Times 16 bold')
        # Create a button to open the density check window
        b1 = Button(win, text='Check Density', relief=RAISED, font='Times 13 bold',
                    command=self.density_check_window)
        # Create a button to display the prior density checks from a file
        b2 = Button(win, text='Review Prior Checks', relief=RAISED, font='Times 13 bold',
                    command=self.display_file_contents)
        # Create a button to quit the program
        b3 = Button(win, text='Quit', relief=RAISED, font='Times 13 bold', command=self.close_program)
        # import image into python and MainWindow
        self.img = Image.open('TFCO Image.jpg')
        self.img = self.img.resize((300, 100))
        self.img = ImageTk.PhotoImage(self.img)
        tfco_img = Label(image=self.img, relief=SUNKEN)
        # Place the widgets and image on the main window
        lbl1.place(x=25, y=65)
        b1.place(x=150, y=130)
        b2.place(x=125, y=170)
        b3.place(x=185, y=210)
        tfco_img.place(x=55, y=250)

    # Define a method to create a new window for the density check
    def density_check_window(self):
        # Create a new window with a title and a size
        new_win = Toplevel(window)
        new_win.title('Density Check')
        new_win.geometry('500x600')
        new_win.configure(background='#C7C6C6')
        # import image into python and window, resize and place
        self.img2 = Image.open('caliper.jpeg')
        self.img2 = self.img2.resize((150, 100))
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.caliper_img = Label(new_win, image=self.img2, relief=SUNKEN)
        self.caliper_img.place(x=175, y=450)
        # import image into python and window, resize and place
        self.img3 = Image.open('measurement.jpeg')
        self.img3 = self.img3.resize((300, 80))
        self.img3 = ImageTk.PhotoImage(self.img3)
        self.measurment_img = Label(new_win, image=self.img3, relief=SUNKEN)
        self.measurment_img.place(x=100, y=10)

        # Create labels to prompt the user to enter the information for the density check
        lbl1 = Label(new_win, text='Enter the Lot Number :', relief=SUNKEN, font='Times 12 bold')
        lbl2 = Label(new_win, text='Click date button :', relief=SUNKEN, font='Times 12 bold')
        lbl3 = Label(new_win, text='Enter the product type :', relief=SUNKEN, font='Times 12 bold')
        lbl4 = Label(new_win, text='Enter intended density :', relief=SUNKEN, font='Times 12 bold')
        lbl5 = Label(new_win, text='Enter the width in inches :', relief=SUNKEN, font='Times 12 bold')
        lbl6 = Label(new_win, text='Enter the length in inches :', relief=SUNKEN, font='Times 12 bold')
        lbl7 = Label(new_win, text='Enter the thickness in inches :', relief=SUNKEN, font='Times 12 bold')
        lbl8 = Label(new_win, text='Enter the weight in lbs :', relief=SUNKEN, font='Times 12 bold')
        lbl9 = Label(new_win, text='Calculated density :', relief=SUNKEN, font='Times 12 bold')
        # Create entry widgets to get the user input for the density check
        self.t1 = Entry(new_win, font='Times 11 bold')
        self.t2 = Entry(new_win, font='Times 11 bold')
        self.t3 = Entry(new_win, font='Times 11 bold')
        self.t4 = Entry(new_win, font='Times 11 bold')
        self.t5 = Entry(new_win, font='Times 11 bold')
        self.t6 = Entry(new_win, font='Times 11 bold')
        self.t7 = Entry(new_win, font='Times 11 bold')
        self.t8 = Entry(new_win, font='Times 11 bold')
        self.t9 = Entry(new_win, font='Times 11 bold')

        # Create buttons to perform the actions for the density check
        b1 = Button(new_win, text='Calculate Density', font='Times 11 bold', command=self.density_calculation)
        b2 = Button(new_win, text='Date', font='Times 11 bold', command=self.get_date)
        b3 = Button(new_win, text='Clear', font='Times 11 bold', command=self.clear_entries)
        b4 = Button(new_win, text='Save', font='Times 11 bold', command=self.write_to_file)
        # Place the buttons on the new window
        b1.place(x=135, y=400)
        b2.place(x=450, y=138)
        b3.place(x=320, y=400)
        b4.place(x=270, y=400)
        # Place the labels and entries on the new window
        lbl1.place(x=60, y=110)
        lbl2.place(x=60, y=140)
        lbl3.place(x=60, y=170)
        lbl4.place(x=60, y=200)
        lbl5.place(x=60, y=230)
        lbl6.place(x=60, y=260)
        lbl7.place(x=60, y=290)
        lbl8.place(x=60, y=320)
        lbl9.place(x=60, y=350)
        self.t1.place(x=280, y=110)
        self.t2.place(x=280, y=140)
        self.t3.place(x=280, y=170)
        self.t4.place(x=280, y=200)
        self.t5.place(x=280, y=230)
        self.t6.place(x=280, y=260)
        self.t7.place(x=280, y=290)
        self.t8.place(x=280, y=320)
        self.t9.place(x=280, y=350)

    # Define a method to calculate the density of the product
    def density_calculation(self):

        # declare density variable

        density = 0

        # Get the values of the variables from the entry widgets

        lot_number = self.t1.get()
        check_date = self.t2.get()
        product_type = self.t3.get()
        intended_density = self.t4.get()
        width = self.t5.get()
        length = self.t6.get()
        thickness = self.t7.get()
        weight = self.t8.get()

        # Try to convert the input to float
        try:
            width = float(width)
            length = float(length)
            thickness = float(thickness)
            weight = float(weight)
            # check if the inputs are empty
            if lot_number == '' or check_date == '' or product_type == '' or intended_density == '':
                # pop up message box with error if any entry is left blank
                messagebox.showerror('Entry Error', 'Please fill in all Entries')
            # Check if the input is positive
            elif width > 0 and length > 0 and thickness > 0 and weight > 0:

                # Calculate the density
                density = (weight * 454) / ((width * thickness * length) * 2.54 ** 3)

                # Insert the calculated density into the ninth entry widget
                self.t9.insert(END, str(density))

            else:
                # Pop up message box with an error message if the input is not positive
                messagebox.showerror('Entry Error', 'Input must be positive')

        # Catch any ValueError exceptions that might occur when converting the input to float
        except ValueError:
            # Insert an error message if the input is invalid
            messagebox.showerror('Entry Error', 'Enter a valid input!')

        # Return the values of the variables
        return lot_number, check_date, product_type, intended_density, width, length, thickness, weight, density

    # Define a method to clear all the entries in the density check window
    def clear_entries(self):
        # Create a list of entry widgets
        entries = [self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7, self.t8, self.t9]

        # Loop through the list and delete the contents of each entry widget
        for entry in entries:
            entry.delete(0, END)

    # Define a method to get the current date and time
    def get_date(self):
        # Get the current date and time using the datetime module and format it as YYYY-MM-DD HH:MM:SS
        check_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        # Insert the current date and time into the second entry widget
        self.t2.insert(END, check_date)

    # Define a method to write the information from the density check window to a file
    def write_to_file(self):
        # Specify the file path
        file_path = 'density_checks.txt'

        # Call the density_calculation method to get the values of the variables
        lot_number, check_date, product_type, intended_density, width, length, \
            thickness, weight, density = self.density_calculation()

        # Open the file in append mode using the with statement
        with open(file_path, 'a') as file:
            # Write the information from the density check window to the file using the write method
            file.write(f'Lot Number: {lot_number}\n')
            file.write(f'Date: {check_date}\n')
            file.write(f'Product Type: {product_type}\n')
            file.write(f'Intended Density: {intended_density}\n')
            file.write(f'Width: {width}\n')
            file.write(f'Length: {length}\n')
            file.write(f'Thickness: {thickness}\n')
            file.write(f'Weight: {weight}\n')
            file.write(f'Density: {density}\n')

    # Define a method to display the contents of the file that stores the prior density checks
    @staticmethod
    def display_file_contents():
        # Specify the file path
        file_path = 'density_checks.txt'

        # create the file and any missing parent directories
        Path(file_path).touch()

        # Open the file that stores the prior density checks in read mode and read its contents
        with open(file_path, 'r') as file:
            content = file.read()

        # Create a new window with the main window as its parent
        new_win_two = Toplevel(window)
        # Set the title and the size of the new window
        new_win_two.title('Prior Density Checks')
        new_win_two.geometry('600x500')

        # Create a text widget to display the file contents
        text_widget = Text(new_win_two, wrap='word')
        # Insert the file contents into the text widget
        text_widget.insert('1.0', content)
        # Create a scrollbar to scroll through the text widget
        scrollbar = Scrollbar(new_win_two, command=text_widget.yview)
        # Configure the text widget to use the scrollbar
        text_widget.config(yscrollcommand=scrollbar.set)

        # Pack the scrollbar and the text widget on the new window
        scrollbar.pack(side="right", fill="y")
        text_widget.pack(side="left", fill="both", expand=True)

    # Define a method to quit the program
    @staticmethod
    def close_program():
        quit()


# Create the main window with a title configure background and size
window = Tk()
window.geometry('400x400')
window.title('Density Check Program')
window.configure(background='#C7C6C6')

# Create an instance of the Main_Window class
mywin = MainWindow(window)

# Start the main loop of the program
window.mainloop()
