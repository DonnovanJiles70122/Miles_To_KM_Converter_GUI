from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    kilo_result_label.config(text=f"{km}")

# Create window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry
# Create entry
miles_input = Entry(width=7)

# Place entry label
miles_input.grid(column=1, row=0)

# Label 
# Create labels
miles_label = Label(text="Miles")
is_equal_to_label = Label(text="Is equal to")
kilo_result_label = Label(text="0")
kilo_label = Label(text="Km")

# Place Labels
miles_label.grid(column=2, row=0)
is_equal_to_label.grid(column=0, row=1)
kilo_result_label.grid(column=1, row=1)
kilo_label.grid(column=2, row=1)

# Button
# Create button
calculate_button = Button(text="Calculate", command=miles_to_km)

# Place Button
calculate_button.grid(column=1, row=2)






# Keeps window open
window.mainloop()