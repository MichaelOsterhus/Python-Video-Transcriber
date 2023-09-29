import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Import your 'transcribe' function from app.py
from app import *

# Function to transcribe the video when the button is clicked
def transcribe_video():
    if selected_option.get() == "URL":
        url = url_textbox.get("1.0", "end-1c")
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
        else:
            # Call your 'transcribe' function with the URL
            result = transcribe_url(url)
            # Display the result (you can update this part based on your 'transcribe' function)
            messagebox.showinfo("Transcription Result", result)
    elif selected_option.get() == "File":
        file_path = filedialog.askopenfilename()
        if not file_path:
            messagebox.showerror("Error", "Please select a video file")
        else:
            # Call your 'transcribe' function with the selected file path
            result = transcribe_file(file_path)
            # Display the result (you can update this part based on your 'transcribe' function)
            messagebox.showinfo("Transcription Result", result)

# CREATE GUI
root = tk.Tk()
root.geometry("800x500")
root.title("Video Transcriber")

label = tk.Label(root, text="Choose Input Method", font=("Roboto", 18))
label.pack(padx=20, pady=20)

# Radio button to select input method
selected_option = tk.StringVar()
selected_option.set("URL")  # Default option is URL

radio_url = tk.Radiobutton(root, text="URL", font=("Roboto", 16), variable=selected_option, value="URL")
radio_url.pack(padx=10)

radio_file = tk.Radiobutton(root, text="File", font=("Roboto", 16), variable=selected_option, value="File")
radio_file.pack(padx=10)

# Textbox for URL input
url_label = tk.Label(root, text="Paste URL", font=("Roboto", 16))
url_label.pack(padx=20)

url_textbox = tk.Text(root, height=3, font=("Roboto", 16))
url_textbox.pack(padx=20)

# Button to transcribe video
button = tk.Button(root, text='Transcribe Video', font=('Roboto', 18), command=transcribe_video)
button.pack(padx=18, pady=18)

root.mainloop()
