import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
ws = tk.Tk()
ws.title('Main Window')
ws.configure(bg='lightblue')
def resize_image(image_path, width, height):
    # Open the image file
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo
image_path = "C:/Users/mohse/Downloads/banque-misr.png"
resized_photo = resize_image(image_path, 150, 100)  # Change dimensions as needed
label = tk.Label(ws, image=resized_photo)
label.pack()
def New_Window():
    Window = tk.Toplevel()
    canvas = tk.Canvas(Window, height=HEIGHT, width=WIDTH)
    canvas.pack()
HEIGHT = 500
WIDTH = 600
def loan():
    loan_value = loan_input.get()
    if loan_value.strip():  # Check if the input is not empty
        try:
            # Try to convert the input to an integer
            entry_value = int(loan_value)
            # Perform the comparison
            if entry_value > 3000000:
                messagebox.showinfo("Result", "The entered value is greater than 3000000.")
            elif entry_value < 25000:
                messagebox.showinfo("Result", "The entered value is less than 25000.")
            else:
                print('Input is within the valid range.')
        except ValueError:
            # Handle the case where conversion to integer fails
            messagebox.showerror("Error", "Please enter a valid integer.")
    else:
        # Handle the case where input is empty
        messagebox.showerror("Error", "The input cannot be empty.")
def month():
    user_input = month_input.get()
    if user_input.strip():  # Check if the input is not empty
        try:
            # Try to convert the input to an integer
            entry_value = int(user_input)
            if entry_value > 84:
                messagebox.showinfo("Result", "The entered value is greater than 84.")
            elif entry_value < 6:
                messagebox.showinfo("Result", "The entered value is less than 6.")
            else:
                print('Input is within the valid range.')
        except ValueError:
            # Handle the case where conversion to integer fails
            messagebox.showerror("Error", "Please enter a valid integer.")
    else:
        # Handle the case where input is empty
        print('The input cannot be empty.')
def calculate_payment():
    try:
        print("month_value, loan_value")
        if int(month_input.get()) > 0 and int(loan_input.get()) > 0:
            loan = int(loan_input.get())  # Assuming entry is where the loan amount is entered
            month = int(month_input.get())  # Assuming entry is where the month or term is entered
            monthly_payment = 0
            print("calculate_payment 1")

            if loan <= 0 or month <= 0:
                raise ValueError("Loan amount and terms must be positive numbers.")

            if month == 1:
                interest_rate = 13.76 / 100  # Interest rate for 12 months
                total_interest = loan * interest_rate  # Total interest for one year
                total_loan = total_interest + loan  # Total loan amount including interest
                monthly_payment = total_loan / 12  # Monthly payment over 12 months
            elif month == 3:
                interest_rate = 14.06 / 100  # Interest rate for 36 months
                total_interest = loan * interest_rate * 3  # Total interest for three years
                total_loan = total_interest + loan  # Total loan amount including interest
                monthly_payment = total_loan / 36  # Monthly payment over 36 months
            elif month == 5:
                interest_rate = 14.87 / 100  # Interest rate for 36 months
                total_interest = loan * interest_rate * 5 # Total interest for three years
                total_loan = total_interest + loan  # Total loan amount including interest
                monthly_payment = total_loan / 60  # Monthly payment over 36 months
            elif month == 7:
                interest_rate = 15.71 / 100  # Interest rate for 36 months
                total_interest = loan * interest_rate * 7 # Total interest for three years
                total_loan = total_interest + loan  # Total loan amount including interest
                monthly_payment = total_loan / 84 # Monthly payment over 36 months

            else:
                print('f')  # Exit the function if an invalid term is entered
                return  # Properly exit the function if an invalid term is entered

            print("calculate_payment 2")
            result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
            rate_label.config(text=f"interest rate: ${interest_rate:.2f}")
            total_label.config(text=f"total interest: ${total_interest:.2f}")
    except ValueError as e:
        print("error", str(e))


label = tk.Label(ws, text='personal loan', font=('Arial',10))
label.pack(pady=20)
def drop_down(event):
    print("Selected:", event.widget.get())
ws.geometry("800x500")
chosen_value = tk.StringVar()
dropdown = ttk.Combobox(ws, textvariable=chosen_value)
dropdown['values'] = ('income proof professionals', 'doctors')
dropdown.current(0)  # default selection
dropdown.bind('<<ComboboxSelected>>', drop_down)
dropdown.pack(pady=15)

tk.Label(ws, text="Min 6-Max 84").pack()
month_input = tk.Entry(ws)
month_input.pack()

check_button = tk.Button(ws, text="Done", command=month)
check_button.pack(pady=5)

tk.Label(ws, text="Min 25000- Max 3000000").pack()
loan_input = tk.Entry(ws)
loan_input.pack()

check_button = tk.Button(ws, text="Done", command=loan)
check_button.pack(pady=5)

result_label = tk.Label(ws, text="")
result_label.pack()
rate_label = tk.Label(ws, text='')
rate_label.pack()
total_label = tk.Label(ws,text="")
total_label.pack()

button = tk.Button(ws, text="view details", bg='blue',
                   fg='white', command=calculate_payment)
button.pack(pady=20)

def clear_entries():
    month_input.delete(0, tk.END)
    loan_input.delete(0, tk.END)
    result_label.config(text="")

def exit_application():
    ws.destroy()


ws.mainloop()


canvas = tk.Canvas(ws, height=HEIGHT, width=WIDTH)
canvas.pack()
