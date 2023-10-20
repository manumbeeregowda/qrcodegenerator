import tkinter as tk
from PIL import Image, ImageTk
import pyqrcode

def generate_qr_code():
    data = text_entry.get()
    name = name_entry.get()

    if data and name:
        qr = pyqrcode.create(data)
        qr.png(f"{name}.png", scale=5)
        qr_code_image = Image.open(f"{name}.png")
        qr_code_photo = ImageTk.PhotoImage(qr_code_image)

        qr_code_canvas.create_image(125, 87, anchor=tk.CENTER, image=qr_code_photo)
        qr_code_canvas.image = qr_code_photo

    else:
        info_label.config(text="Please enter both data and name.")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and configure GUI elements
frame = tk.Frame(root, bg="white")  # Change background color to white
frame.pack(expand=True, fill="both")

info_label = tk.Label(frame, text="", font=("Arial", 12), bg="white", fg="black")  # Change font size and colors
info_label.pack()

text_label = tk.Label(frame, text="Enter the text/URL:", font=("Arial", 10), bg="white", fg="black")  # Change font size and colors
text_label.pack()
text_entry = tk.Entry(frame, font=("Arial", 10))  # Change font size
text_entry.pack()

name_label = tk.Label(frame, text="Enter the name of the QR Code:", font=("Arial", 10), bg="white", fg="black")  # Change font size and colors
name_label.pack()
name_entry = tk.Entry(frame, font=("Arial", 10))  # Change font size
name_entry.pack()

generate_button = tk.Button(frame, text="Generate Code", font=("Arial", 12), command=generate_qr_code)  # Change font size
generate_button.pack()

qr_code_canvas = tk.Canvas(frame, relief=tk.RIDGE, bd=2)
qr_code_canvas.pack()

root.geometry("600x600")
root.mainloop()
