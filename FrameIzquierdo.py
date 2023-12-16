import tkinter as tk
from PIL import Image, ImageTk

class FrameIzquierdo(tk.Frame):
    """
    Clase perteneciente al panel (frame) izquierdo de la aplizacion
    En ella se contiene la vista del reproductor y el menu para navegar entre canciones
    
    Attributes:

    Methods:
    
    """
    
    def __init__(self, master):
        """
        Constructor de la clase 
        
        Args:
            master: widget padre al que estará asociado
        Rerurns: 
            None
        Ejemolo: 
        """
        
        
        
        super().__init__(master, bg = "black")
        self.master = master # widget padre
        self.pack(fill = "y")
        
        # FRAME INTERCAMBIO VISTAS
        # Crear el frame
        self.frame_menu = tk.Frame(self, bg = "black")
        
        # Crear botones de navegacion
        
        #Espaciadores
        self.btn_espaciador1 = tk.Button(self.frame_menu, bg = "black", text = " ", relief= "flat")
        self.btn_espaciador1.grid(row = 2, column= 0, sticky="ns")
        self.btn_espaciador2 = tk.Button(self.frame_menu, bg = "black", text = " ", relief= "flat")
        self.btn_espaciador2.grid(row = 6, column= 0, sticky="ns")
        
        self.btn_top_10 = tk.Button(self.frame_menu, bg = '#1877f2', fg = "white", text = "Top 10", font = ("Arial" , 15), relief="flat", command = self.abrir_top_10)
        self.btn_top_10.grid(row = 1, column=0, padx= 15, pady=10, sticky="ew") 
        
        self.btn_artistas = tk.Button(self.frame_menu, bg="black", fg = "white", text = "Artistas", font = ("Arial" , 15), relief="flat", command = self.navegar_a_artistas)
        self.btn_artistas.grid(row = 3, column=0, padx= 15, pady=10)
        
        self.btn_albumes = tk.Button(self.frame_menu, bg="black", fg = "white", text = "Albumes", font = ("Arial" , 15), relief="flat", command = self.navegar_a_albumes)
        self.btn_albumes.grid(row = 4, column=0, padx= 15, pady=10)
        
        self.btn_listas_reproduccion = tk.Button(self.frame_menu, bg="black", fg = "white", text = "Listas de reproduccion", font = ("Arial" , 15), relief="flat", command = self.navegar_a_listas_de_reproduccion)
        self.btn_listas_reproduccion.grid(row = 5, column=0, padx= 15, pady=10)
        
        
        
        self.frame_menu.pack()
        
        
        # FRAME REPRODUCTOR DE MUSICA 
        # Agregar los botones
        self.frame_reproductor = tk.Frame(self, bg="black")
        
        self.btn_retroceder = tk.Button(self.frame_reproductor, text="⏮️", command=self.retroceder, bg='white', fg='black', font=('Arial', 8), width=3, height=1, relief="flat")
        self.btn_retroceder.grid(row=0, column=0, padx=5, pady=5)

        self.btn_reproducir = tk.Button(self.frame_reproductor, text="▶️", command=self.reproducir, bg='white', fg='black', font=('Arial', 8), width=3, height=1, relief="flat")
        self.btn_reproducir.grid(row=0, column=1, padx=5, pady=5)

        self.btn_pausar = tk.Button(self.frame_reproductor, text="⏸️", command=self.pausar, bg='white', fg='black', font=('Arial', 8), width=3, height=1, relief="flat")
        self.btn_pausar.grid(row=0, column=2, padx=5, pady=5)

        self.btn_avanzar = tk.Button(self.frame_reproductor, text="⏭️", command=self.avanzar, bg='white', fg='black', font=('Arial', 8), width=3, height=1, relief="flat")
        self.btn_avanzar.grid(row=0, column=3, padx=5, pady=5)

        self.btn_aleatorio = tk.Button(self.frame_reproductor, text="🔀", command=self.aleatorio, bg='white', fg='black', font=('Arial', 8), width=3, height=1, relief="flat")
        self.btn_aleatorio.grid(row=0, column=4, padx=5, pady=5)

        image_path = "C:/Users/Jorge/OneDrive/Escritorio/dios.jpg"
        self.imagen = Image.open(image_path)
        self.imagen = self.imagen.resize((150, 150))  # Ajustar el tamaño de la imagen
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.frame_reproductor, image=self.imagen)
        self.label_imagen.grid(row=1, column=0, columnspan=5, padx=10, pady=5)

        self.label_cancion = tk.Label(self.frame_reproductor, text="Run", font=('Arial', 14), bg='black', fg='white')
        self.label_cancion.grid(row=2, column=0, columnspan=5, padx=10, pady=2)

        self.label_artista = tk.Label(self.frame_reproductor, text="Joji", font=('Arial', 12), bg='black', fg='white')
        self.label_artista.grid(row=3, column=0, columnspan=5, padx=10, pady=2)

        self.label_album = tk.Label(self.frame_reproductor, text="Nectar", font=('Arial', 10), bg='black', fg='white')
        self.label_album.grid(row=4, column=0, columnspan=5, padx=10, pady=2)

        self.frame_reproductor.pack(side = "bottom")
    
    
    
    # METODOS    
    # 1. Navegacion   
    def abrir_top_10(self):
        print("Abro el navegador para ver el top 10 de canciones mas reproducidas")
    
    def navegar_a_artistas(self):
        print("Estoy navegando a artistas!")
        
    def navegar_a_albumes(self):  
        print("Estoy navegando a albumes!")
    
    def navegar_a_listas_de_reproduccion(self):
        print("Estoy navegando a listas de reproduccion!")
        
        
        
    # 2. Reproductor
    def retroceder(self):
        print("Soy retroceder y estoy retrocediendo!")

    def reproducir(self):
        print("Soy reproducir y estoy reproduciendo!")

    def pausar(self):
        print("Soy pausar y estoy pausando!")

    def avanzar(self):
        print("Soy avanzar y estoy avanzando!")

    def aleatorio(self):
        print("Soy aleatorio y estoy reproduciendo aleatoriamente!")

    # 2. Intercambio de vista lateral derecha
    
    
    
    
    
root = tk.Tk()
root.title("Frame de prueba")
frameIzquierdo = FrameIzquierdo(root)
frameIzquierdo.pack(side =  "left", fill="y", expand = True)
#frameIzquierdo.grid(row = 0, column = 0,  sticky = "ns")


#Prueba con frame derecho expandible
framederecho = tk.Frame(root)
#framederecho.pack(side = "right", fill = "both", expand = True)
#framederecho.grid(row = 0, column = 1, sticky = "nsew")

root.mainloop() 