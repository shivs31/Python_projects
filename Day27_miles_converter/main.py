import tkinter


def button_clicked():
    print('I got clicked')
    new_text = input.get() #enter the text in the box which is Entry
    my_label.config(text=new_text) # update the text in Label



window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=100,pady=200) #move the program window to desire location

#Label
my_label = tkinter.Label(text='I am a Label', font = ('Arial', 24, 'bold'))
#To update the text in Label
#my_label['text'] = "New Text"
# alternative way to update the text
my_label.config(text = 'New Text')

#my_label.pack() # to show on the screen and keeps adding the next widgets below
#To place the widget at desire location with coordinates
#my_label.place(x=100,y=0) #need to do calculation fro coordinates manually
#Grid works with rows and columns
my_label.grid(column=0, row=0)



#Button     
button = tkinter.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text='New Button')
new_button.grid(column=2, row=0)


#Entry
input = tkinter.Entry(width=10)
#input.pack()
input.get()
input.grid(column=3,row=2)






window.mainloop()