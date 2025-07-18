import tkinter


def miles_to_km():
    miles = float(miles_input.get()) #enter the text in the box which is Entry
    km = miles * 1.609
    kilometer_result_label.config(text=f'{km}') # update the text in Label

window = tkinter.Tk()
window.title('Miles to Km converter')
window.config(padx=20, pady=20)

#Label
miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=2,row=0)
#Entry
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1,row=0)


is_equal_label = tkinter.Label(text='is equal to')
is_equal_label.grid(column=0,row=1)

kilometer_result_label = tkinter.Label(text='0')
kilometer_result_label.grid(column=1,row=1)

kilometer_label = tkinter.Label(text='Km')
kilometer_label.grid(column=2,row=1)

calculate_button = tkinter.Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1,row=2)


window.mainloop()