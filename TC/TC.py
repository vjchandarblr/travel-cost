
from tkinter import *

travel = Tk()
travel.title("Travel Cost")
travel.geometry("400x200")

def kmcal():
    pertrol = pinput.get()
    car_milage = vinput.get()
    Price_per_km = (int(pertrol)/int(car_milage))
    ltr.insert(END,round(float(Price_per_km)))
    distance = dist.get()
    dis = float(Price_per_km)*int(distance)
    total.insert(END,round(float(dis)))

Petrol = Label(travel,text="Fuel Price")
Petrol.grid(row=0,column=0,sticky=E)
pinput = Entry(travel)
pinput.grid(row=0,column=1)
vehicalM = Label(travel,text="Average Mileage of Vehicle")
vehicalM.grid(row=1,column=0,sticky=E)
vinput = Entry(travel)
vinput.grid(row=1,column=1)
pricepl = Label(travel,text="Price Per Kilometer")
ltr = Entry(travel)
pricepl.grid(row=2,column=0,sticky=E)
ltr.grid(row=2,column=1)
distance = Label(travel,text="Distance")
dist =Entry(travel)
distance.grid(row=3,column=0,sticky=E)
dist.grid(row=3,column=1)

calulate =Button(travel,text="Calculate" ,command=kmcal)
calulate.grid(row=4,column=0)
total = Label(travel,text="Total in Rupees").grid(row=4,column=3)
total = Entry(travel)
total.grid(row=4,column=1)

travel.mainloop()
