import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

# def simulate_loading(varBarra):
#     for i in range(101):
#         varBarra.set(i) 
#         root.update_idletasks()
#         time.sleep(0.1)

# def clear_screen():
#     canvas.delete("all")
#     pb.destroy()

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Instagram Bot")
        self.master.geometry("1000x800")
        self.master.resizable(False, False)

        self.container = tk.Frame(self.master)
        self.container.pack()
        
        self.repart_left = tk.Frame(self.container, bg="blue", height=800)
        self.repart_left["width"] = 500
        self.repart_left.pack(side="right")
    
        self.repart_right = tk.Frame(self.container, bg="green", width=500, height=800)
        self.repart_right.pack(side="left")
        self.repart_right_input = tk.Entry(self.repart_right, width=50)
        self.repart_right_input.pack()
        self.repart_right_input.place(x=0,y=0)

        # # Crie uma repartição preta dentro de repart_right
        # self.reparticao_preta = tk.Frame(self.repart_right, bg="black")
        # self.reparticao_preta.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.4)

        # # Crie uma repartição amarela dentro de repart_right
        # self.reparticao_amarela = tk.Frame(self.repart_right, bg="yellow")
        # self.reparticao_amarela.place(relx=0.5, rely=0.7, relwidth=0.9, relheight=0.2)

root = tk.Tk()
Application(root)
root.mainloop()


# root = tk.Tk()
# root.title("Instagram Bot")
# root.geometry("1000x800")
# root.resizable(False, False)

# imagem = Image.open("visual/images/robot.png")
# imagem = imagem.resize((100, 100))
# imagem_tk = ImageTk.PhotoImage(imagem)

# canvas = tk.Canvas(root, width=1000, height=800, background="white")
# canvas.pack()

# x = (1000 - imagem_tk.width()) // 2
# y = (700 - imagem_tk.height()) // 2
# canvas.create_image(x, y, anchor=tk.NW, image=imagem_tk)

# style = ttk.Style()
# style.configure("TProgressbar", troughcolor="black", background="green")
# varBarra = tk.DoubleVar()
# varBarra.set(0)
# pb = ttk.Progressbar(root, variable=varBarra, maximum=100, style="TProgressbar")
# pb.place(x=350, y=410, width=300, height=40)
# simulate_loading(varBarra)

# time.sleep(2)

# clear_screen()

# blue_frame = tk.Frame(root, bg="blue", width=500, height=800)
# green_frame = tk.Frame(root, bg="green", width=500, height=800)

# blue_frame.pack(side="left")
# green_frame.pack(side="left")

# time.sleep(4)

# blue_frame.destroy()
# green_frame.destroy()

# mensagem = tk.Label(root, text="Olá, Tkinter!", font=("Arial", 16))
# mensagem.pack(pady=20)

# botao_fechar = tk.Button(root, text="Fechar", command=clear_screen)
# botao_fechar.pack()