
from tkinter import ttk
import tkinter as tk
from unicodedata import lookup


r1deu  = '^qwertzuiopü°QWERTZUIOPÜ'
r1rus  = 'ёйцукенгшщзхЁЙЦУКЕНГШЩЗХ'
r2deu  = 'asdfghjklöäASDFGHJKLÖÄ'
r2rus  = 'фывапролджэФЫВАПРОЛДЖЭ'
r3deu  = 'yxcvbnm,.-YXCVBNM;:_'
r3rus  = 'ячсмитьбю.ЯЧСМИТЬБЮ,'

deurus = {}

accdeu = "e"
accrus = "у́"


deurusacc = {}
for d, r in zip( accdeu, accrus ):
	deurusacc[d] =r




linkeHand  = "adsfgadsafgadsfgadsafg"
rechteHand = "kjlhjlökljlähkljlhäökj"
train = []
train.append("adsfgadsafgadsfgadsafg")
train.append("kjlhjlökljlähkljlhäökj")
train.append("kjadsafgadsjlähkljlasj")
train.append("qrerweqwewrtqewtrewqwq")
train.append("uipozuiouizpopiüzuoüpu")
train.append("vxybvxbcybxvbvyxvbxycv")
train.append("mn,.-.,m,n-.,-.m.,n.,-")


combobox= ["mittlere Zeile links", "mittlere Zeile rechts",
"mittlere Zeile li/re", "obere Zeile links","obere Zeile rechts","untere Zeile links","untere Zeile rechts"]



for d, r in zip( r1deu, r1rus ):
	deurus[d] =r

for d, r in zip( r2deu, r2rus ):
	deurus[d] =r

for d, r in zip( r3deu, r3rus ):
	deurus[d] =r


class Browser:
	def __init__(self):
		self.window = tk.Tk()
		self.window.geometry("600x600")

		#self.window.config(width=500, height=500)
		self.canvas = tk.Canvas(
		    self.window,
		    width=500,
		    height=500,
		    bg="white",
		)
		self.canvas.pack()
		
		self.window.bind("<Down>", self.keydown)
		self.window.bind("<Up>", self.keyup)
		self.window.bind("<Key>", self.key)
		#self.window.bind("<Button-1>", self.aktionSF)
		self.limit = 20
		self.score = 0

		self.ScoreL = tk.Label(self.window, text = self.score)
		self.ScoreL.pack()


		self.schaltf1 = tk.Button(self.canvas, text="Aktion durchführen", command=self.aktionSF)
		self.schaltf1.pack()
		self.zeichen_deu='a'
		self.training = rechteHand
		self.combo = ttk.Combobox( state="readonly", values=combobox)
		self.combo.set("mittlere Zeile links")
		self.combo.place(x=0, y=0)

		# Create text widget and specify size.
		self.Truss = tk.Text(self.canvas, height = 20, width = 52)
		y_acc = '\N{CYRILLIC SMALL LETTER U}\N{COMBINING ACUTE ACCENT}'
		message = "тьб"+ y_acc
		print( message)
		#c = lookup("cyrillic %s letter %c with %s" % (cap, c, accent))
		#c = lookup(y_acc)
		self.Truss.insert(tk.END, y_acc)
		print(y_acc)
		self.Truss.pack(padx=5, pady=15, side=tk.LEFT)
		self.akzent = False 

		self.Tdeut = tk.Text(self.canvas, height = 20, width = 52)
		self.Tdeut.pack(padx=5, pady=15, side=tk.LEFT)

# tk inter is not able to place accents on cyrillic letters, whereas the   
#bash is able to do so this program needs a deeper change
		
		
	def key(self, e):
	
		if self.akzent == True:
		
			#self.Truss.insert(tk.END, deurusacc[e.char])	
			self.Truss.insert(tk.END,u"у́" )	
			self.akzent = False	
		else:
			if e.char == "´":
				self.akzent = True
				self.Truss.configure(bg="green") 	
				print(" AKzent")
						
			else:
				self.Truss.configure(bg="white")
				print( 'up', e.char, deurus[e.char] )
				#self.zeichen_deu = self.training[self.score]
				
				self.Truss.delete("end-2c",tk.END)
				self.Truss.insert(tk.END, deurus[e.char])
				
				if self.zeichen_deu == e.char :
					print("richtig")
					self.window.configure(bg="green")
				else:
					print("falsch")	
					self.window.configure(bg="red")
				
	def keyup(self, e):
		print( 'up', e.char)
	def keydown(self, e):
		print( 'down', e.char )
		
		
	
	def aktionSF(self):
		global train
	
		#label3 = tk.Label(self.canvas, text="Aktion durchgeführt", bg="yellow")
		#label3.pack()
		self.timer = self.window.after(1000, self.update)
		index = self.combo.current()
		print("index" , index, train[ index])
		self.training = train[index]
		
		self.score = 0
		

	def update(self):
		self.score +=1
		#self.zeichen_deu = self.training[self.score]
		#self.Truss.delete(tk.END)
		#self.Truss.insert(tk.END, "тьб")
		
		
		if self.score < self.limit:
			self.zeichen_deu = self.training[self.score]
			self.ScoreL.configure(font=('Arial', 30) )
			self.ScoreL.configure(text=deurus[self.zeichen_deu])
			
			self.timer = self.window.after(2000, self.update)
		else:
			self.window.after_cancel(self.timer)
			self.ScoreL.configure(text='Game over')


b = Browser()
tk.mainloop()




