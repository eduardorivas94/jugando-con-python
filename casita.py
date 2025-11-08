import tkinter as tk

ventana = tk.Tk()
ventana.title("mi casita")

lienzo = tk.Canvas (ventana, width=400, height=400, bg="skyblue")
lienzo.pack()

lienzo.create_rectangle(100, 200 , 300, 350, fill= "saddlebrown", outline="black")

lienzo.create_polygon(100, 200, 300, 200, 200, 100, fill= "firebrick", outline="black")

lienzo.create_rectangle(175, 275, 225 ,350, fill="darkgoldenrod", outline="black")

lienzo.create_rectangle(120, 230 ,160, 270, fill="lightblue", outline="black")
lienzo.create_rectangle(240, 230, 280, 270, fill= "lightblue", outline="black")

ventana.mainloop()