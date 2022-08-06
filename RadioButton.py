import tkinter

window = tkinter.Tk()


def reset():
    selected.set(None)


label = tkinter.Label(window, text='¿Qué comida prefieres?')
label.grid(column=0, row=1, pady=5, padx=5)
selected = tkinter.IntVar()
r1 = tkinter.Radiobutton(window, text='Hamburguesa', value=1, variable=selected)
r1.grid(column=0, row=2, pady=5, padx=5)
r2 = tkinter.Radiobutton(window, text='Pizza', value=2, variable=selected)
r2.grid(column=0, row=3, pady=5, padx=5)
r3 = tkinter.Radiobutton(window, text='Hot Dog', value=3, variable=selected)
r3.grid(column=0, row=4, pady=5, padx=5)
r4 = tkinter.Radiobutton(window, text='Sandwich', value=4, variable=selected)
r4.grid(column=0, row=5, pady=5, padx=5)

ButtonReset = tkinter.Button(window, command=reset, text='Reiniciar')
ButtonReset.grid(column=1, row=6, pady=5, padx=5)
window.mainloop()