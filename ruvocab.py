import wx

import json
import ast


r1deu  = '^qwertzuiopü°QWERTZUIOPÜ'
r1rus  = 'ёйцукенгшщзхЁЙЦУКЕНГШЩЗХ'
r2deu  = 'asdfghjklöäASDFGHJKLÖÄ'
r2rus  = 'фывапролджэФЫВАПРОЛДЖЭ'
r3deu  = 'yxcvbnm,.-YXCVBNM;:_'
r3rus  = 'ячсмитьбю.ЯЧСМИТЬБЮ,'


newdata = {}

deurus = {}

for d, r in zip( r1deu, r1rus ):
	deurus[d] =r

for d, r in zip( r2deu, r2rus ):
	deurus[d] =r

for d, r in zip( r3deu, r3rus ):
	deurus[d] =r

deurusacc = {}
rusrusacc = {}

accdeu = 'e'
accrus = "\N{CYRILLIC SMALL LETTER U}\N{COMBINING ACUTE ACCENT}"
ohneaccrus = "\N{CYRILLIC SMALL LETTER U}"
deurusacc[ accdeu] = accrus
rusrusacc[ohneaccrus] = accrus

accdeu = 'E'
accrus = "\N{CYRILLIC CAPITAL LETTER U}\N{COMBINING ACUTE ACCENT}"
ohneaccrus = "\N{CYRILLIC CAPITAL LETTER U}"
deurusacc[ accdeu] = accrus
rusrusacc[ohneaccrus] = accrus

accdeu = 's'
accrus = "\N{CYRILLIC SMALL LETTER YERU}\N{COMBINING ACUTE ACCENT}"
ohneaccrus ="\N{CYRILLIC SMALL LETTER YERU}"
deurusacc[ accdeu] = accrus
rusrusacc[ohneaccrus] = accrus

accdeu = 'S'
accrus = "\N{CYRILLIC CAPITAL LETTER YERU}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus

accdeu = 'f'
accrus = "\N{CYRILLIC SMALL LETTER A}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus
ohneaccrus ="\N{CYRILLIC SMALL LETTER A}"
rusrusacc[ohneaccrus] = accrus


accdeu = 'F'
accrus = "\N{CYRILLIC CAPITAL LETTER A}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus

accdeu = 'b'
accrus = "\N{CYRILLIC SMALL LETTER I}\N{COMBINING ACUTE ACCENT}"
ohneaccrus ="\N{CYRILLIC SMALL LETTER I}"
deurusacc[ accdeu] = accrus
rusrusacc[ohneaccrus] = accrus


accdeu = 'B'
accrus = "\N{CYRILLIC CAPITAL LETTER I}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus

accdeu = 'y'
accrus = "\N{CYRILLIC SMALL LETTER YA}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus
ohneaccrus ="\N{CYRILLIC SMALL LETTER YA}"
rusrusacc[ohneaccrus] = accrus


accdeu = 'Y'
accrus = "\N{CYRILLIC CAPITAL LETTER YA}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus

accdeu = '.'
accrus = "\N{CYRILLIC SMALL LETTER YU}\N{COMBINING ACUTE ACCENT}"
ohneaccrus ="\N{CYRILLIC SMALL LETTER YU}"
deurusacc[ accdeu] = accrus
rusrusacc[ohneaccrus] = accrus

accdeu = ':'
accrus = "\N{CYRILLIC CAPITAL LETTER YU}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus


accdeu = 't'
accrus = "\N{CYRILLIC SMALL LETTER IE}\N{COMBINING ACUTE ACCENT}"
ohneaccrus ="\N{CYRILLIC SMALL LETTER IE}"
deurusacc[ accdeu] = accrus
rusrusacc[ohneaccrus] = accrus




accdeu = 'T'
accrus = "\N{CYRILLIC CAPITAL LETTER IE}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus

accdeu = 'ä'
accrus = "\N{CYRILLIC SMALL LETTER E}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus
ohneaccrus ="\N{CYRILLIC SMALL LETTER E}"
rusrusacc[ohneaccrus] = accrus

accdeu = 'Ä'
accrus = "\N{CYRILLIC CAPITAL LETTER E}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus


accdeu = 'j'
accrus = "\N{CYRILLIC SMALL LETTER O}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus
ohneaccrus ="\N{CYRILLIC SMALL LETTER O}"
rusrusacc[ohneaccrus] = accrus

accdeu = 'J'
accrus = "\N{CYRILLIC CAPITAL LETTER O}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus

accdeu = '^'
accrus = "\N{CYRILLIC SMALL LETTER IO}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus

accdeu = '°'
accrus = "\N{CYRILLIC CAPITAL LETTER IO}\N{COMBINING ACUTE ACCENT}"
deurusacc[ accdeu] = accrus



print("rracc",rusrusacc ) 
#print(accdeu, accrus )




#deurusacc[ accdeu] = accrus

#for d, r in zip( accdeu, accrus ):
#	deurusacc[d] =r

#print( deurusacc)



class MyFrame(wx.Frame):
	def __init__(self):
		super().__init__(parent=None, title="Russisch - Deutsch", size=(800, 600))

		self.panel = wx.Panel(self)

		# Create a vertical BoxSizer to arrange widgets vertically
		#sizer = wx.BoxSizer(wx.VERTICAL)
		#sizer = wx.BoxSizer(wx.HORIZONTAL)
		

		# 1. Label
		self.label = wx.StaticText(self.panel, label="Enter your name:")
		#sizer.Add(self.label, flag=wx.ALL, border=10)

		# 2. Textbox
		self.Truss = wx.TextCtrl(self.panel,pos = (50, 50), size = (200, 100), style = wx.TE_MULTILINE)
		self.Truss.AppendText("у́лица ")
		self.Truss.Bind( wx.EVT_KEY_UP, self.keypressed )
		
		#self.Truss.Bind( wx.EVT_CHAR_HOOK, self.keypressed )

		self.EnterTruss = wx.TextCtrl(self.panel,pos = (50, 250), size = (200, 100), style = wx.TE_MULTILINE)
		self.EnterTruss.AppendText("у́лица ")
		self.EnterTruss.Bind( wx.EVT_KEY_UP, self.keypressed2 )



		self.accent = False

		#sizer.Add(self.Truss, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
		#sizer.Add(self.Truss, flag=wx.LEFT|wx.RIGHT, border=10)
		
		#sizer = wx.BoxSizer(wx.HORIZONTAL)
		
		self.Tdeut = wx.TextCtrl(self.panel,pos = (300, 50), size = (200, 100), style = wx.TE_MULTILINE)
		self.Tdeut.AppendText("Strasse ")
		#sizer.Add(self.Tdeut, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
		#sizer.Add(self.Truss, flag=wx.LEFT|wx.RIGHT, border=10)

		self.Tline = wx.TextCtrl(self.panel,pos = (300, 250) )
		self.Tline.AppendText("1")

		# 3. Button

		button = wx.Button(self.panel, label="vor Vocab",pos = (300, 300))
		button.Bind(wx.EVT_BUTTON, self.nxVocab)

		button = wx.Button(self.panel, label="zur Vocab",pos = (300, 350))
		button.Bind(wx.EVT_BUTTON, self.prevVocab)
		
		button = wx.Button(self.panel, label="Save Vocab",pos = (550, 50))
		button.Bind(wx.EVT_BUTTON, self.saveVocab)
		#sizer.Add(button, flag=wx.ALL|wx.ALIGN_CENTER, border=10)

		button = wx.Button(self.panel, label="get Vocab",pos = (550, 250))
		button.Bind(wx.EVT_BUTTON, self.getVocab)

		button = wx.Button(self.panel, label="show Vocab",pos = (550, 300))
		button.Bind(wx.EVT_BUTTON, self.showVocab)

		



		#self.panel.SetSizer(sizer)

		self.Centre()
		self.Show()

	def keypressed( self, event):
		keycode = event.GetUnicodeKey()
		print( keycode )
		if keycode == 0:
			s = self.Truss.GetStringSelection()
			if s :
				print("selected text", s )
				
				if s in rusrusacc:
					print("found")
					ip = self.Truss.GetInsertionPoint()
					#self.Truss.Remove(ip , ip+1)
					self.Truss.Replace( ip, ip+1, rusrusacc[s] )
					#self.Truss.Remove(self.Truss.GetLastPosition()-1, self.Truss.GetLastPosition())
					#
					#self.Truss.AppendText("  "+)
		
			
		
				
		if keycode != 0 :
			if keycode == 35 and self.accent == False : # "'" character
				
				
				
				self.accent = True
				#self.Truss.Remove(self.Truss.GetLastPosition()-1, self.Truss.GetLastPosition())
				
				self.label.SetLabel("Accent")
				ip = self.Truss.GetInsertionPoint()
				self.Truss.Remove(ip-1 , ip)
				
				
			else:	
				if self.accent == False:
					ip = self.Truss.GetInsertionPoint()
					if ip >0:
						c = self.Truss.GetValue()[ip-1]	
						print(" c=", c)
						if c in deurus:
							self.Truss.Replace( ip-1, ip, deurus[c] )
					
					#if c in deurus:
					#
					#	print("kk",c )
					#	lp = self.Truss.GetLastPosition()
					#	self.Truss.Replace( lp, lp+1, deurus[c] )
					#	#self.Truss.Remove(self.Truss.GetLastPosition()-1, self.Truss.GetLastPosition())
					#	#self.Truss.AppendText(deurus[c])
					#self.Truss.Replace( lp, lp+1, deurus[c] )	
						
					self.accent = False
					self.label.SetLabel("NO Accent")
				else:
					ip = self.Truss.GetInsertionPoint()
					c = self.Truss.GetValue()[ip-1]	
					print(" c=", c)
					
					if c in deurus:
						self.Truss.Replace( ip-1, ip, deurusacc[c] )
					
					
					self.accent = False	
					
					
					#c = self.Truss.GetValue()[-1]	
					#print("kk in accent",c )
					self.label.SetLabel("NO Accent")
					
					#if c in deurusacc:
					#
					#	
					#	self.Truss.Remove(self.Truss.GetLastPosition()-1, self.Truss.GetLastPosition())
					#	self.Truss.AppendText(deurusacc[c])
						
						
						
				#self.Truss.SetValue(self.Truss.GetValue()[:-1]) 
				#self.Truss.SetValue(self.Truss.GetValue()+ "у́")
		
		print("k", keycode )
		#event.Skip()

	def keypressed2( self, event):
		keycode = event.GetUnicodeKey()
		print( keycode )
		if keycode == 0:
			s = self.EnterTruss.GetStringSelection()
			if s :
				print("selected text", s )
				
				if s in rusrusacc:
					print("found")
					ip = self.EnterTruss.GetInsertionPoint()
					#self.EnterTruss.Remove(ip , ip+1)
					self.EnterTruss.Replace( ip, ip+1, rusrusacc[s] )
					#self.EnterTruss.Remove(self.EnterTruss.GetLastPosition()-1, self.EnterTruss.GetLastPosition())
					#
					#self.EnterTruss.AppendText("  "+)
		
			
		
				
		if keycode != 0 :
			if keycode == 35 and self.accent == False : # "'" character
				
				
				
				self.accent = True
				#self.EnterTruss.Remove(self.EnterTruss.GetLastPosition()-1, self.EnterTruss.GetLastPosition())
				
				self.label.SetLabel("Accent")
				ip = self.EnterTruss.GetInsertionPoint()
				self.EnterTruss.Remove(ip-1 , ip)
				
				
			else:	
				if self.accent == False:
					ip = self.EnterTruss.GetInsertionPoint()
					if ip >0:
						c = self.EnterTruss.GetValue()[ip-1]	
						print(" c=", c)
						if c in deurus:
							self.EnterTruss.Replace( ip-1, ip, deurus[c] )
					
					#if c in deurus:
					#
					#	print("kk",c )
					#	lp = self.EnterTruss.GetLastPosition()
					#	self.EnterTruss.Replace( lp, lp+1, deurus[c] )
					#	#self.EnterTruss.Remove(self.EnterTruss.GetLastPosition()-1, self.EnterTruss.GetLastPosition())
					#	#self.EnterTruss.AppendText(deurus[c])
					#self.EnterTruss.Replace( lp, lp+1, deurus[c] )	
						
					self.accent = False
					self.label.SetLabel("NO Accent")
				else:
					ip = self.EnterTruss.GetInsertionPoint()
					c = self.EnterTruss.GetValue()[ip-1]	
					print(" c=", c)
					
					if c in deurus:
						self.EnterTruss.Replace( ip-1, ip, deurusacc[c] )
					
					
					self.accent = False	
					
					
					#c = self.EnterTruss.GetValue()[-1]	
					#print("kk in accent",c )
					self.label.SetLabel("NO Accent")
					
					#if c in deurusacc:
					#
					#	
					#	self.EnterTruss.Remove(self.EnterTruss.GetLastPosition()-1, self.EnterTruss.GetLastPosition())
					#	self.EnterTruss.AppendText(deurusacc[c])
						
						
						
				#self.EnterTruss.SetValue(self.EnterTruss.GetValue()[:-1]) 
				#self.EnterTruss.SetValue(self.EnterTruss.GetValue()+ "у́")
		
		print("k", keycode )
		#event.Skip()


	def nxVocab(self, event):
		key = self.Tline.GetValue()
		ikey = int( key)
		ikey += 1
		self.Tline.SetValue(str( ikey))
		self.getVocab( event)

	def prevVocab(self, event):
		key = self.Tline.GetValue()
		ikey = int( key)
		ikey -= 1
		self.Tline.SetValue(str( ikey))
		self.getVocab( event)




	def getVocab(self, event):
		
		with open("sample.json", "r") as f:    
			newdata = json.load(f)
			f.close()
		key = self.Tline.GetValue()
		rd = newdata[ key]
		mylist = ast.literal_eval(rd)
		print( rd , "_", mylist )
		self.Tdeut.Clear()
		self.Tdeut.AppendText(mylist[1])
		self.Truss.Clear()
		self.EnterTruss.Clear()
		
	def showVocab(self, event):
		with open("sample.json", "r") as f:    
			newdata = json.load(f)
			f.close()
		key = self.Tline.GetValue()
		rd = newdata[ key]
		mylist = ast.literal_eval(rd)
		print( rd , "show_", mylist )
		self.Truss.Clear()
		self.Truss.AppendText(mylist[0])	
		
		    
	def saveVocab(self, event):
		global newdata 
		with open("sample.json", "r") as f:    
			newdata = json.load(f)
			f.close()


		maxi = 0
		i = 1
		for k in newdata:
		
			print("i",i, k[0], k )
			i += 1
			if( int( k ) > maxi ):
				maxi = int( k )
				print("max",maxi, i ) 
			
		print("highest number", maxi, str(maxi+1))	


		russ = self.Truss.GetValue()
		deu =  self.Tdeut.GetValue()
		 
		print("before nd,",newdata)
		
		newdata.update( {str(maxi+1) :str([russ, deu]) } )
		 
		print("after nd,",newdata)
		 
		json_str = json.dumps(newdata, indent=4,ensure_ascii=False)
		with open("sample.json", "w",encoding='utf8') as f:
			f.write(json_str)
			f.flush()
			f.close()		    
		    
		    
		    

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
