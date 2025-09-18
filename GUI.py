from tkinter import *
from PIL import Image, ImageTk
import action
import speech_to_text

# Create the main application window
root = Tk()
root.title("AI AGENT")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#D3D3D3")

# Function to handle speech input
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)

    text_box.insert(END, "You --> " + user_val + "\n")
    if bot_val is not None:
        text_box.insert(END, "BOT --> " + str(bot_val) + "\n")

    if bot_val == "ok sir":
        root.destroy()

# Function to handle text input from entry box
def send():
    user_input = entry_box.get()
    if not user_input.strip():
        return  # Prevent sending empty messages

    bot_response = action.Action(user_input)

    text_box.insert(END, "You --> " + user_input + "\n")
    if bot_response is not None:
        text_box.insert(END, "BOT --> " + str(bot_response) + "\n")

    if bot_response == "ok sir":
        root.destroy()

    entry_box.delete(0, END)

# Function to clear the text box
def del_text():
    text_box.delete("1.0", END)

# === GUI Layout ===

# Frame for heading and image
frame_box = LabelFrame(root, padx=100, pady=7, borderwidth=2.7, relief="raised", bg="#151617")
frame_box.grid(row=0, column=1, padx=55, pady=10)

# Title Label
text_label = Label(
    frame_box,
    text="Your AI Agent",
    font=("Times New Roman", 14, "bold"),
    bg="#151617",
    fg="white",
    highlightbackground="#1F2122",
    highlightthickness=2,
    relief="solid"
)
text_label.grid(row=0, column=0, pady=10)

# Image
image = ImageTk.PhotoImage(Image.open("images/AI_AGENT.png"))
image_label = Label(frame_box, image=image)
image_label.grid(row=1, column=0, pady=20)

# Chat display box
text_box = Text(
    root,
    font=("Times New Roman", 12, "bold"),
    bg="#835669",
    fg="white",
    height=6,
    width=50,
    wrap=WORD
)
text_box.grid(row=1, column=1, pady=20)

# Entry field for user input
entry_box = Entry(root, width=35, font=("Arial", 12), justify=CENTER)
entry_box.grid(row=2, column=1, padx=35, pady=10, ipady=3)

# Buttons
Button(root, text="ASK", bg="#356696", fg="white", padx=20, pady=10, border=3, relief=SOLID, command=ask).place(x=70, y=600)
Button(root, text="Send", bg="#356696", fg="white", padx=20, pady=10, border=3, relief=SOLID, command=send).place(x=238, y=600)
Button(root, text="Delete", bg="#356696", fg="white", padx=20, pady=10, border=3, relief=SOLID, command=del_text).place(x=410, y=600)

# Start the Tkinter event loop
root.mainloop()
