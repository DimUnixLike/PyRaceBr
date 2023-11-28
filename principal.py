import tkinter as tk
  
class MoveCanvas(tk.Canvas):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dx = 0
        self.dy = 0
        self.velocidade = 3
        self.deslocou = 0
        #self.box = self.create_rectangle(0, 0, 20, 20, fill="black")

        self.pista0 = self.create_image(400, -128, image=img_pista)
        self.pista1 = self.create_image(400, 128, image=img_pista)
        self.pista2 = self.create_image(400, 384, image=img_pista)
        self.pista3 = self.create_image(400, 640, image=img_pista)

        self.box1 = self.create_image(420, 520, image=img_car)
 
        self.dt = 25
        self.tick()
      
    def tick(self):
        if (self.dy == 1): self.velocidade += 0.1

        self.deslocou += self.velocidade

        self.move(self.pista0, self.dx, self.velocidade)
        self.move(self.pista1, self.dx, self.velocidade)
        self.move(self.pista2, self.dx, self.velocidade)
        self.move(self.pista3, self.dx, self.velocidade)
            
        print(self.coords(self.pista3)[1])

        maximo = 896
        regresso = 128

        if ((self.coords(self.pista3)[1]) >= maximo): self.move(self.pista3,self.dx, -self.coords(self.pista3)[1] -regresso)
        if ((self.coords(self.pista2)[1]) >= maximo): self.move(self.pista2,self.dx, -self.coords(self.pista2)[1] -regresso)
        if ((self.coords(self.pista1)[1]) >= maximo): self.move(self.pista1,self.dx, -self.coords(self.pista1)[1] -regresso)
        if ((self.coords(self.pista0)[1]) >= maximo): self.move(self.pista0,self.dx, -self.coords(self.pista0)[1] -regresso)

        if (self.velocidade == 0): self.move(self.box1, self.dx, self.velocidade)

        self.after(self.dt, self.tick)
 
    def controles(self, dx, dy):
        self.dx = dx
        self.dy = dy


 
if __name__ == "__main__":
 
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Dim Game")

    img_path = "/home/um/Área de Trabalho/python/mygame/"
    #img_padrao = tk.PhotoImage(file = img_path + "")
    img_car = tk.PhotoImage(file = img_path + "car00.png")
    img_pista = tk.PhotoImage(file = img_path + "pista.png")


    cvs = MoveCanvas(root, bg="green")
    cvs.pack(fill="both", expand=True)
 
    
    ds = 1

    ###CONTROLES -- FALTA CONCERTAR AINDA
    root.bind("<KeyPress-Left>", lambda _: cvs.controles(-3, 0))
    root.bind("<KeyPress-Right>", lambda _: cvs.controles(3, 0))

    root.bind("<KeyPress-Up>", lambda _: cvs.controles(0, ds))
    root.bind("<KeyPress-Down>", lambda _: cvs.controles(0, -ds))

    root.bind("<KeyRelease-Left>", lambda _: cvs.controles(0, 0))
    root.bind("<KeyRelease-Right>", lambda _: cvs.controles(0, 0))
    root.bind("<KeyRelease-Up>", lambda _: cvs.controles(0, 0))
      
    root.mainloop()