import tkinter as tk
import os

def is_display_available():
    # Check if the DISPLAY environment variable is set
    return os.environ.get('DISPLAY') is not None

if is_display_available():
    class NamePickerApp:
        def __init__(self, master):
            self.master = master
            self.master.title("Name Picker App")

            self.name_pool = []

            # Create widgets for adding a name
            self.add_name_label = tk.Label(master, text="Enter Your Name:")
            self.name_entry = tk.Entry(master)
            self.add_name_button = tk.Button(master, text="Add Name", command=self.add_name_to_pool)

            # Create widgets for picking a name
            self.pick_name_label = tk.Label(master, text="Click 'Pick a Name' to Select a Random Name:")
            self.pick_name_button = tk.Button(master, text="Pick a Name", command=self.select_random_name)
            self.selected_name_label = tk.Label(master, text="Selected Name:")

            # Layout
            self.add_name_label.pack()
            self.name_entry.pack()
            self.add_name_button.pack()
            self.pick_name_label.pack()
            self.pick_name_button.pack()
            self.selected_name_label.pack()

        def add_name_to_pool(self):
            name = self.name_entry.get()
            if name:
                self.name_pool.append(name)
                self.name_entry.delete(0, 'end')
                print(f"Name '{name}' added to the pool. Pool: {self.name_pool}")

        def select_random_name(self):
            if self.name_pool:
                selected_name = random.choice([name for name in self.name_pool if name != self.name_entry.get()])
                self.selected_name_label.config(text=f"Selected Name: {selected_name}")
            else:
                self.selected_name_label.config(text="Name pool is empty")

    if __name__ == "__main__":
        root = tk.Tk()
        app = NamePickerApp(root)
        root.mainloop()
else:
    print("No display available. This program requires a graphical environment.")
