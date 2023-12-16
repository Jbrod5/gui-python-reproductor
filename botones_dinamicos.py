import tkinter as tk

class imprimir:
    
    def imprimir_pantalla(self):
        print("soy la clase imprimir")

class FrameArtistas(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs, bg="black")

        # Crear el label en la parte superior
        label_artistas = tk.Label(self, text="Artistas", font=("Arial", 35, "bold"), bg="black", fg="white")
        label_artistas.grid(row=0, column=0, sticky="w", pady = 20, padx=15)

        # Crear un canvas escroleable
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.grid(row=1, column=0, sticky="nsew")

        # Crear un frame para contener los botones
        self.contenedor_botones = tk.Frame(self.canvas, bg="black")
        self.canvas.create_window((0, 0), window=self.contenedor_botones, anchor="nw")

        # Configurar el peso de la fila y la columna para que el frame se expanda
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Agregar un scrollbar al canvas
        scrollbar = tk.Scrollbar(self, command=self.canvas.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Configurar el canvas para que sea escroleable
        self.contenedor_botones.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Permitir desplazamiento con la rueda del mouse
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        # Crear el botón "Agregar Nuevo" en el contenedor de botones
        btn_agregar_nuevo = tk.Button(self.contenedor_botones, text="Agregar Nuevo", command=self.agregar_nuevo, font=("Arial", 12))
        btn_agregar_nuevo.grid(row=0, column=0, sticky="ew")

        self.contador_columnas = 1
        self.contador_filas = 0

   def agregar_nuevo(self):
        # Añadir una instancia de un botón al contenedor de botones
        impri = imprimir()
        imagen = tk.PhotoImage(file="gui-python-reproductor/assets/Artista_icon.png")
        #imagen = imagen.subsample(3, 3)  # Redimensionar la imagen (ajusta los valores según sea necesario)

        nuevo_boton = tk.Button(self.contenedor_botones, image=imagen, compound="top", bg="#181818", fg="white", font=("Arial", 15, "bold"), highlightthickness=0, relief="flat", text="Nuevo Artista", command=impri.imprimir_pantalla)
        
        # Mantener una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        nuevo_boton.image = imagen

        if(self.contador_columnas == 6):
            self.contador_columnas = 0
            self.contador_filas += 1
        
        nuevo_boton.grid(row=self.contador_filas, column=self.contador_columnas, sticky="ew", pady = 20, padx= 20)
        self.contador_columnas += 1

# Ejemplo de uso
#root = tk.Tk()
#frame_artistas = FrameArtistas(root)
#frame_artistas.pack(fill = "both", expand=True )
#root.mainloop()
