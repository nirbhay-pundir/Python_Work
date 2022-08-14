import tkinter as tk
from tkinter import font as tkFont
import numpy as np
import keras
import tkinter.messagebox
from joblib import load


def checkInputs():
    info = []
    for feature in features:
        try:
            if feature.Text.get(1.0, "end-1c") == '':
                errorLabelFill.pack()
                return False, np.array(info)
            else:
                info.append(float(feature.Text.get(1.0, "end-1c")))
        except:
            errorLabelNumbers.pack()
            return False, np.array(info)
    return True, np.array(info)


def getPrice():
    errorLabelFill.pack_forget()
    errorLabelNumbers.pack_forget()
    isRight, info = checkInputs()
    if isRight:
        s_scaler = load('std_scaler.bin')
        model = keras.models.load_model('housing_price_prediction_model.h5')
        price = model.predict(s_scaler.transform(np.array(info).reshape(-1, 19)))
        tkinter.messagebox.showinfo("Prediction", "According to me house must be of Rs." + str(price[0][0]) + ".")


class labels:
    Text = ''

    def __init__(self, window, label, info):
        fontStyleLabel = tkFont.Font(family="Lucida Grande", size=12)
        fontStyleInfo = tkFont.Font(family="Lucida Grande", size=8)
        fontStyleText = tkFont.Font(family="Lucida Grande", size=10)
        f1 = tk.Frame(window)
        tk.Label(f1, text=label + ":", font=fontStyleLabel).pack(anchor='w', side='left')
        tk.Label(f1, text='(' + info + ')', font=fontStyleInfo).pack(anchor='nw', side='left')
        text = tk.Text(f1, height=1, font=fontStyleText)
        text.pack(fill='x', side="top", padx='20')
        f1.pack(padx=('10', '0'), pady=('15', '0'), side='top', anchor='w', fill='x')
        self.Text = text


features = []

window = tk.Tk()
window.title('Housing Price Predictor')
window.geometry("800x950")

tk.Label(window, text='Input your requirements: ',
         font=tkFont.Font(family="Lucida Grande", size=18, weight="bold")).pack(anchor='w', side='top',
                                                                                padx=('10', '0'), pady=('10', '0'))

features.append(labels(window, "Bedrooms", "Number of bedrooms"))
features.append(labels(window, "Bathrooms", "Number of bathrooms, .5 for a bathroom without shower"))
features.append(labels(window, "Living Area", "Square footage of the apartments interior living space"))
features.append(labels(window, "Total Area", "Square footage of the land space"))
features.append(labels(window, "Floors", "Number of floors"))
features.append(
    labels(window, "Waterfront", "Whether the apartment was overlooking the waterfront. If yes(1) or no(0)"))
features.append(labels(window, "View", "A value from 0 to 4 of how good the view of the property you want"))
features.append(labels(window, "Condition", "A value from 1 to 5 on the condition of the apartment"))
features.append(labels(window, "Grade", "A value from 1 to 13 for the quality of construction and design of building"))
features.append(labels(window, "Above Area", "The area of the interior house space that is above ground level"))
features.append(labels(window, "Below Area", "The area of the interior house space that is below ground level"))
features.append(labels(window, "Build Year", "The year the house was initially built"))
features.append(labels(window, "Renovation Year", "The year of the house’s last renovation"))
features.append(labels(window, "Latitude", "Location latitude where you want buy house"))
features.append(labels(window, "Longitude", "Location longitude where you want buy house"))
features.append(labels(window, "Neighbors Living Area", "Interior house living area for the nearest 15 neighbors"))
features.append(labels(window, "Neighbors Total Area", "Total house area for the nearest 15 neighbors"))
features.append(labels(window, "Buying Month", "Month, in number, in which you want to buy house"))
features.append(labels(window, "Buying Year", "Year, in number, in which you want to buy house"))

button = tk.Button(window, text="Get Price", bg='#A8F796',
                   font=tkFont.Font(family="Lucida Grande", size=14, weight="bold"), command=getPrice)
button.pack(pady=('15', '15'), side='top', anchor='n')

errorLabelFill = tk.Label(window, text='Please fill all the fields.', fg="red",
                          font=tkFont.Font(size=10, weight="bold"))
errorLabelNumbers = tk.Label(window, text='Please use only numbers.', fg="red",
                             font=tkFont.Font(size=10, weight="bold"))

window.resizable(False, False)
window.mainloop()
