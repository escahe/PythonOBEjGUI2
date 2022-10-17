from tkinter import Tk,Label,Listbox
marcas = ['Fiat', 'Ford', 'Mazda', 'Audi', 'Toyota','Kia','Renault','BMW']
window = Tk()
window.geometry('200x200')
label = Label(text="Marcas de autos")
label.pack()
list = Listbox(window,activestyle='none',justify='center')
for marca in marcas:
 list.insert(0,marca)
list.pack()
window.mainloop()