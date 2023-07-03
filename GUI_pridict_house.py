import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk
from PIL import Image, ImageTk

win = tk.Tk()
win.title('Predict New House')
win.geometry('1600x800')
win.configure(bg='cyan')

hd = tk.Label(win, text='House Price Prediction ', font='sans 18 bold', bg='cyan', fg='red')
hd.pack(fill='both')
hd = tk.Label(win, text='House Price Prediction using Machine Learning', font='sans 14 bold', bg='yellow', fg='blue')
hd.pack(fill='both')

user = tk.Label(win, text='House Size', font='sans 12 bold', bg='green', fg='white')
user.place(x=600, y=90)

tx1 = tk.Entry(win, font='sans 12 bold')
tx1.place(x=695, y=90)

result = tk.Label(win, text='Total Amount', font='sans 12 bold', bg='green', fg='white')
result.place(x=600, y=160)
result = tk.Entry(win, font='sans 12 bold')
result.place(x=710, y=160)

# Create a sample dataset
data = {
    'Size': [1000, 1500, 1800, 1350, 1200, 2400, 3200, 3600, 4000, 5000],
    'Price': [2500000, 3600000, 4000000, 3500000, 3200000, 4600000, 5600000, 6000000, 6500000, 7800000]
}

# Create a linear regression model and fit the data
model = LinearRegression()
model.fit([[1000], [1500], [1800], [1350], [1200], [2400], [3200], [3600], [4000], [5000]],
          [2500000, 3600000, 4000000, 3500000, 3200000, 4600000, 5600000, 6000000, 6500000, 7800000])


def predict_price():
    size = float(tx1.get())
    predicted_price = model.predict([[size]])
    result.delete(0, tk.END)
    result.insert(0, f"Rs. {predicted_price[0]:,.2f}")


def exitwin():
    win.destroy()


bt1 = tk.Button(win, text='Submit', font='sans 12 bold', bg='blue', fg='white', command=predict_price)
bt1.place(x=750, y=120)
bt2 = tk.Button(win, text='Exit', font='sans 12 bold', bg='red', fg='white', command=exitwin)
bt2.place(x=760, y=190)
hd = tk.Label(win, text='*Designed by Aneel Rathod (MIT INDIA)* ', font='sans 14 italic', bg='skyblue', fg='red')
hd.place(x=550, y=720)

image = Image.open('house2.png')
text = ImageTk.PhotoImage(image)
label1 = tk.Label(image=text)
label1.image = text
label1.place(x=0, y=250)



win.mainloop()
