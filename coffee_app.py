import tkinter as tk
from tkinter import messagebox

# Menu items and their prices
menu = {
    "Espresso": 2.50,
    "Latte": 3.50,
    "Cappuccino": 3.00,
    "Americano": 2.00,
    "Mocha": 3.75
}

# Function to calculate the total bill
def calculate_total():
    total = 0
    order_summary = "Your Order:\n"
    for item, var in item_vars.items():
        quantity = var.get()
        if quantity > 0:
            total += menu[item] * quantity
            order_summary += f"{item} x {quantity} = ${menu[item] * quantity:.2f}\n"
    order_summary += f"Total Bill: ${total:.2f}"
    
    # Display the order summary
    messagebox.showinfo("Order Summary", order_summary)

# Create the main application window
app = tk.Tk()
app.title("Coffee Shop Order App")

# Create a frame for the menu
menu_frame = tk.Frame(app)
menu_frame.pack(pady=10)

# Display the menu items with quantity input
tk.Label(menu_frame, text="Menu", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
item_vars = {}
row = 1
for item, price in menu.items():
    tk.Label(menu_frame, text=f"{item} (${price:.2f})", font=("Arial", 12)).grid(row=row, column=0, padx=10, pady=5, sticky="w")
    var = tk.IntVar(value=0)  # Variable to store quantity
    item_vars[item] = var
    tk.Spinbox(menu_frame, from_=0, to=10, textvariable=var, width=5).grid(row=row, column=1, padx=10, pady=5)
    row += 1

# Add a button to calculate the total bill
tk.Button(app, text="Calculate Total", font=("Arial", 12), command=calculate_total, bg="green", fg="white").pack(pady=10)

# Run the application
app.mainloop()

