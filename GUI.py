import tkinter as tk
root = tk.Tk()

greeting = tk.Label(text="Python Rocks!")
greeting.pack()

label = tk.Label(
    text = "Hello, Tkinter",
    foreground = "white",   # Set the text color to white, alternatively can name it "fg".
    background = "black"    # Set the background color to black, alternatively can name it "bg".
)
label.pack()

label2 = tk.Label(
    text = "Hello Tkinter Upsized.",
    fg = "blue",
    bg = "white",
    height = 10
)
label2.pack()

# Create a clickable button with the Button() class.
button = tk.Button(
    text="Click Me!",
    width = 25,
    height = 5,
    bg = "blue",
    fg = "red"
)
button.pack()

# Create a text entry field using the Entry() class.
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

# Retrieve text input with the .get() method.
name = entry.get()
print(name)

# Need to call the mainloop method on the Tk window object at the end of all 
# the code or else it won't display a window.
root.mainloop()