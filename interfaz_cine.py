from tkinter import *
from tkinter import ttk
import cine_database

window = Tk()
frame_app = Frame(window, width=700, height=1000, bg="red")
frame_app.pack()

pelicula = StringVar()
hora= StringVar()
fecha = StringVar()
idioma = StringVar()
precio= StringVar()

def crear_sala():
    pelicula= entry_sala.get()
    hora= entry_butakas.get()
    fecha = entry_boletos.get()
    idioma= entry_precio.get()
    precio= entry_precio.get()
    cine_db = cine_database.MyDatabase()
    cine_db.insert_db(pelicula,hora,fecha,idioma,precio)


# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=150)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender OPTIONS
frame_food = Frame(frame_options, width=350, height=450, bg="#E74C3C")
frame_food.place(x=25, y=30)
label_pelicula = Label(frame_food, 
              text="PELICULA",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#E74C3C")
label_pelicula.place(x=20, y=60)
entry_pelicula = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_pelicula.place(x=20, y=100)
label_hora= Label(frame_food, 
              text="HORA",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#E74C3C")
label_hora.place(x=20, y=130)
entry_hora = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"), show="*")
entry_hora.place(x=20, y=170)
label_fecha= Label(frame_food, 
              text="FECHA",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#E74C3C")
label_fecha.place(x=20, y=200)
entry_fecha = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_fecha.place(x=20, y=240)

label_idioma = Label(frame_food, 
              text="IDIOMA",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#E74C3C")
label_idioma.place(x=20, y=280)
entry_idioma = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_idioma.place(x=20, y=320)

label_precio = Label(frame_food, 
              text="PRECIO",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#E74C3C")
label_precio.place(x=20, y=360)
entry_precio = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_precio.place(x=20, y=400)

button_agregar = Button(frame_form, text="crear sala", 
                        font=("Calibri", "14", "bold"),
                        command= crear_sala)
button_register.place(x=20, y=440)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="Ticket",
              font=("Calibri", "14"))
title.place(x=320, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="¡Bienvenidos(as) a nuestro cine!", 
              font=("Valentime", "24", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="El cine no es un trozo de vida, sino un pedazo de pastel.", 
              font=("Modern Love Caps", "10"),
              justify=LEFT)
title2.place(x=25, y=50)

window.mainloop()