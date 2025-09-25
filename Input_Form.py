import ctypes               # Module for calling C language DLL (used for Windows DPI scaling)
import tkinter              # GUI module for desktop applications
from tkinter import ttk     # ttk = themed widgets for Tkinter
import csv                  # Module for handling CSV files
import tkinter.filedialog   # File dialog (open/save window)
import os                   # Module for file path operations
# -------------------------------
# Function: Add user data to a CSV file
# -------------------------------
def add_user():
   if w_name.get() == "":
       mes = "Please enter a name"
       w_res.set(mes)
       return
   # File save dialog (only CSV files)
   fTyp = [("CSV file", "*.csv")]
   iDir = os.path.abspath(os.path.dirname(__file__))  # Current directory
   file = tkinter.filedialog.asksaveasfilename(filetypes=fTyp, initialdir=iDir)
   if not file:
       w_res.set("No file selected")
       return
   # If the file doesn’t have a .csv extension, add it
   if not file.lower().endswith(".csv"):
       file += '.csv'
   # If file doesn’t exist, create a new one with headers
   if not os.path.exists(file):
       with open(file, 'w', newline='', encoding='utf-8') as f:
           writer = csv.writer(f)
           writer.writerow(["Name", "Age", "Gender", "Address", "Phone Number"])
   # Write user input to the CSV file
   with open(file, 'a', newline="", encoding="utf-8") as f:
       writer = csv.writer(f)
       csv_txt = [
           w_name.get(),
           w_age.get(),
           w_sex.get(),
           w_address.get(),
           w_tel.get()
       ]
       writer.writerow(csv_txt)
       print("Data written: ", csv_txt)
       w_res.set("Data saved successfully")

# -------------------------------
# Function: Show CSV data in a new window
# -------------------------------
def show_csv_data(file_path):
   # Create a new window
   top = tkinter.Toplevel(root)
   top.title("CSV Viewer")
   top.geometry("1000x400")
   # Table widget (Treeview)
   tree = ttk.Treeview(top)
   tree.pack(fill="both", expand=True)
   # Read CSV file
   with open(file_path, "r", encoding="utf-8") as f:
       reader = csv.reader(f)
       headers = next(reader)  # First row (headers)
       # Set headers for Treeview
       tree["columns"] = headers
       tree["show"] = "headings"
       for h in headers:
           tree.heading(h, text=h)
       # Add each row to the Treeview
       for row in reader:
           tree.insert("", "end", values=row)
   # Exit button
   end_button = tkinter.Button(top, text="Close", command=top.destroy)
   end_button.pack(pady=10)

# -------------------------------
# Function: Open CSV file and load first row into input form
# -------------------------------
def open_file():
   file_path = tkinter.filedialog.askopenfilename(
       filetypes=[("CSV file", "*.csv*")],
       initialdir=os.path.abspath(os.path.dirname(__file__))
   )
   if file_path:
       try:
           with open(file_path, 'r', encoding='utf-8') as f:
               reader = csv.reader(f)
               headers = next(reader)   # Skip headers
               first_row = next(reader) # Get the first data row
               # Load into input form
               w_name.set(first_row[0])
               w_age.set(first_row[1])
               w_sex.set(first_row[2])
               w_address.set(first_row[3])
               w_tel.set(first_row[4])
               w_res.set("CSV file loaded")
               # Show the full CSV in a new window
               show_csv_data(file_path)
       except Exception as e:
           w_res.set(f"Read error: {e}")
   else:
       w_res.set("No file selected")

# -------------------------------
# Function: Create input form window
# -------------------------------
def create_window():
   global sub_window
   # Sub-window
   sub_window = tkinter.Toplevel(root)
   sub_window.title("Input Form")
   sub_window.geometry("800x600")
   # Title
   tkinter.Label(
       sub_window,
       text="Input Form",
       bg="lightblue",
       font=("MS Gothic", 20, "bold")
   ).place(x=200, y=10)
   # Name field
   tkinter.Label(sub_window, text="Name", font=("MS Gothic", 16, "bold")).place(x=230, y=75)
   tkinter.Entry(sub_window, textvariable=w_name, width=15, font=("MS Gothic", 16), bg="white").place(x=400, y=75)
   # Age field
   tkinter.Label(sub_window, text="Age", font=("MS Gothic", 16, "bold")).place(x=230, y=115)
   tkinter.Label(sub_window, text="years", font=("MS Gothic", 16, "bold")).place(x=430, y=115)
   tkinter.Entry(sub_window, textvariable=w_age, width=2, font=("MS Gothic", 16), bg="white").place(x=400, y=115)
   # Gender field
   tkinter.Label(sub_window, text="Gender", font=("MS Gothic", 16, "bold")).place(x=230, y=155)
   options = ["Male", "Female"]
   ttk.Combobox(sub_window, width=10, textvariable=w_sex, values=options, state="readonly", font=("MS Gothic", 12, "bold")).place(x=400, y=155)
   # Address field
   tkinter.Label(sub_window, text="Address", font=("MS Gothic", 16, "bold")).place(x=230, y=195)
   tkinter.Entry(sub_window, textvariable=w_address, width=15, font=("MS Gothic", 16), bg="white").place(x=400, y=195)
   # Phone field
   tkinter.Label(sub_window, text="Phone Number", font=("MS Gothic", 16, "bold")).place(x=230, y=245)
   tkinter.Entry(sub_window, textvariable=w_tel, width=15, font=("MS Gothic", 16), bg="white").place(x=400, y=245)
   # Register button
   tkinter.Button(sub_window, text="Register", width=10, font=("MS Gothic", 20, "bold"), bg="lightgreen", command=add_user).place(x=200, y=305)
   # Finish button
   tkinter.Button(sub_window, text="Close", width=20, font=("MS Gothic", 20, "bold"), bg="red", command=sub_window.destroy).place(x=200, y=445)
   # Open file button
   tkinter.Button(sub_window, text="Open File", width=15, font=("MS Gothic", 20, "bold"), bg="lightblue", command=open_file).place(x=420, y=305)
   # Result display
   tkinter.Entry(sub_window, textvariable=w_res, width=15, font=("MS Gothic", 32), bg="white", justify="center").place(x=200, y=375)
   # Make sub-window modal (block parent window until closed)
   sub_window.grab_set()

# -------------------------------
# Main application
# -------------------------------
if __name__ == "__main__":
   global w_name, w_age, w_sex, w_address, w_tel, w_res
   # DPI scaling fix (for high-resolution displays on Windows)
   ctypes.windll.shcore.SetProcessDpiAwareness(1)
   # Create main window
   root = tkinter.Tk()
   root.title("App Menu")
   root.geometry("800x600")
   # Main title
   tkinter.Label(root, text="App Menu", font=("MS Gothic", 20, "bold")).place(x=10, y=10)
   # Button: open input form
   tkinter.Button(root, text="Input Form", width=30, height=2, font=("MS Gothic", 20, "bold"), bg="lightgreen", command=create_window).place(x=100, y=100)
   # Button: exit
   tkinter.Button(root, text="Exit", width=30, height=2, font=("MS Gothic", 20, "bold"), bg="red", command=root.destroy).place(x=100, y=250)
   # Initialize variables
   w_name = tkinter.StringVar()
   w_age = tkinter.StringVar()
   w_sex = tkinter.StringVar()
   w_address = tkinter.StringVar()
   w_tel = tkinter.StringVar()
   w_res = tkinter.StringVar()
   sub_win = None
   # Run the application
   root.mainloop()