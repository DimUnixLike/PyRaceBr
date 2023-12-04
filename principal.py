import tkinter as tk
import pathlib as pl
  
class pista: #WORKING ON THIS
    def __init__(self, pista_name, pista_localizacao):
        self.pista_name = pista_name
        self.pista_localizacao = pista_localizacao

class MoveCanvas(tk.Canvas):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.dx = 0
        self.dy = 0
        self.velocidade = 0
        self.deslocou = 0

        self.pistaPos = 400
        self.maximo = 768
        self.regresso = 1024

        self.pista0 = self.create_image(self.pistaPos, -128, image=img_pista)
        self.pista1 = self.create_image(self.pistaPos, 128, image=img_pista)
        self.pista2 = self.create_image(self.pistaPos, 384, image=img_pista)
        self.pista3 = self.create_image(self.pistaPos, 640, image=img_pista)

        self.carro = self.create_image(420, 520, image=img_car)
 
        self.dt = 25
        self.tick()
      
    def tick(self):

        if (self.dy == 1): self.velocidade += 0.01
        if (self.dy == -1 and self.velocidade > 0): self.velocidade -= 0.01 
        if (self.velocidade < 0): self.velocidade = 0
        self.deslocou += self.velocidade

        self.move(self.pista0, 0, self.velocidade)
        self.move(self.pista1, 0, self.velocidade)
        self.move(self.pista2, 0, self.velocidade)
        self.move(self.pista3, 0, self.velocidade)

        if ((self.coords(self.pista3)[1]) >= self.maximo): self.move(self.pista3,0, -self.regresso)
        if ((self.coords(self.pista2)[1]) >= self.maximo): self.move(self.pista2,0, -self.regresso)
        if ((self.coords(self.pista1)[1]) >= self.maximo): self.move(self.pista1,0, -self.regresso)
        if ((self.coords(self.pista0)[1]) >= self.maximo): self.move(self.pista0,0, -self.regresso)

        self.move(self.carro, self.dx, 0)

        self.after(self.dt, self.tick)
 
    def controles(self, dx, dy):
        self.dx = dx
        self.dy = dy


 
if __name__ == "__main__":
 
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Dim Game")

    img_path = str(pl.Path().absolute())
    img_car = tk.PhotoImage(file = img_path + "/car00.png")
    img_pista = tk.PhotoImage(file = img_path + "/pista.png")

    cvs = MoveCanvas(root, bg="green")
    cvs.pack(fill="both", expand=True)
 
    ds = 1

    ###CONTROLES
    root.bind("<KeyPress-Left>", lambda _: cvs.controles(-3, 0))
    root.bind("<KeyPress-Right>", lambda _: cvs.controles(3, 0))

    root.bind("<KeyPress-Up>", lambda _: cvs.controles(0, ds))
    root.bind("<KeyPress-Down>", lambda _: cvs.controles(0, -ds))

    root.bind("<KeyRelease-Left>", lambda _: cvs.controles(0, 0))
    root.bind("<KeyRelease-Right>", lambda _: cvs.controles(0, 0))
    root.bind("<KeyRelease-Up>", lambda _: cvs.controles(0, 0))
    root.bind("<KeyRelease-Down>", lambda _: cvs.controles(0, 0))
      
    root.mainloop()