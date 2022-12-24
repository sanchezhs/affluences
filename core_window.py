import tkinter as tk
from core import book
from pyrsistent import s

def validate_number(n):
    return n.isnumeric()

window = tk.Tk()
window.title('Reserva Affluences')
window.geometry('350x250+200+200')

frame = tk.Frame(master=window, width=100, height=100)
frm_buttons = tk.Frame(master=window)

dia = tk.IntVar()
lbl_dia = tk.Label(master=frame, text="Día")
entr_dia = tk.Entry(master=frame, fg="black", bg="#2eeeee", 
                    width=50, justify=tk.CENTER, textvariable=dia,
                    validate="key",
                    validatecommand=(window.register(validate_number), "%S")
                    )

hora_inic = tk.StringVar()
lbl_inic = tk.Label(master=frame, text="Hora de inicio")
entr_inic = tk.Entry(master=frame, fg="black", bg="#2eeeee", width=50, justify=tk.CENTER, textvariable=hora_inic)

hora_fin = tk.StringVar()
lbl_fin = tk.Label(master=frame, text="Hora de fin")
entr_fin = tk.Entry(master=frame, fg="black", bg="#2eeeee", width=50, justify=tk.CENTER, textvariable=hora_fin)

correo = tk.StringVar()
lbl_corr = tk.Label(master=frame, text="Correo")
entr_corr = tk.Entry(master=frame, fg="black", bg="#2eeeee", width=50, justify=tk.CENTER, textvariable=correo)

puesto = tk.IntVar()
lbl_puesto = tk.Label(master=frame, text="Puesto")
entr_puesto = tk.Entry(master=frame, fg="black", bg="#2eeeee", width=50, justify=tk.CENTER, textvariable=puesto)


btn_enviar = tk.Button(master=frm_buttons, text="Reservar", 
                       command= lambda: book(dia.get(), hora_inic.get(), 
                       hora_fin.get(), correo.get(), puesto.get())
                       )
btn_quit = tk.Button(master=frm_buttons, text="Cerrar", command=window.quit)

lbl_dia.pack()
entr_dia.pack()
lbl_inic.pack()
entr_inic.pack()
lbl_fin.pack()
entr_fin.pack()
lbl_corr.pack()
entr_corr.pack()
lbl_puesto.pack()
entr_puesto.pack()
btn_enviar.pack()
btn_quit.pack()


frame.pack()
frm_buttons.pack()
entr_dia.focus()

window.mainloop()