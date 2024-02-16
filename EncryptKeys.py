import tkinter as tk
import random
import string

messages = []
public_key = ''
private_key = ''

def create_keys():
    global public_key, private_key  # Specify that we want to modify the global variable
    public_key = ''.join(random.choices(string.ascii_letters, k=32))
    private_key = public_key + user_input

def get_input():
    global user_input, public_key, private_key

    user_input = entry.get()
    messages.append(user_input)
    create_keys()

    print(private_key)

    # Append the input text to the list
    messages_list.insert(tk.END, "User input: " + user_input)
    messages_list.insert(tk.END, "Public key: " + public_key)
    # Clear the entry widget for the next input
    entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Input Field Example")

# Create an entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button to get the input
button = tk.Button(root, text="Get Input", command=get_input)
button.pack()

# Create a listbox to display messages
messages_list = tk.Listbox(root, width=50, height=90)
messages_list.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
