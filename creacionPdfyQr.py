from fpdf import FPDF
import pyqrcode
from qrcode import QRCode
from PIL import Image
import png

class PDF(FPDF):
    pass
    def logo(self, name, x, y, w, h):
        self.image(name, x, y, w, h)
    
    def texts(self,name):
        with open(name,'rb') as xy:
            txt=xy.read().decode('latin-1')
        self.set_xy(10.0,80.0)
        self.set_text_color(76.0,32.0,250.0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0,10,txt)

    def titles(self,title):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', 'B',16)
        self.set_text_color(220,50,50)
        self.multi_cell(w=210.0,h=40.0,align='c', txt=title, border=0)


#img = pyqrcode.create('sandra')
#img.png('sandra.png')



qr=QRCode(version=3, box_size=5, border=2)
qr.add_data("Hola1")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola1.png")

"""qr.add_data("Hola2")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola2.png")

qr.add_data("Hola3")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola3.png")

qr.add_data("Luki")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola4.png")

qr.add_data("Kio")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola5.png")

qr.add_data("Luki")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola6.png")

qr.add_data("Luki")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola7.png")

qr.add_data("Luki")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola8.png")

qr.add_data("Luki")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola9.png")"""

#print('-----------------TERMINA PRIMER BLOQUE----------------------')

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola10.png")

"""qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola11.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola12.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola13.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola14.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola15.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola16.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola17.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola18.png")"""

#print('-----------------TERMINA SEGUNDO BLOQUE----------------------')

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola19.png")

"""qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola20.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola21.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola22.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola23.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola24.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola25.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola26.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola27.png")"""

#print('-----------------TERMINA TERCER BLOQUE----------------------')

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola28.png")

"""qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola29.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola30.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola31.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola32.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes//hola33.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola34.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola35.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola36.png") """

#print('-----------------TERMINA CUARTO BLOQUE----------------------')

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola37.png")

"""qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola38.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola39.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola40.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola41.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola42.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola43.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola44.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola45.png")"""

#print('-----------------TERMINA QUINTO BLOQUE----------------------')

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola46.png")

""""qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola47.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola48.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola49.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola50.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola51.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola52.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola53.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola54.png")"""


#print('-----------------TERMINA SEXTO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola55.png")

"""qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola56.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola57.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola58.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola59.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola60.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola61.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola62.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola63.png")"""


#print('-----------------TERMINA SEPTIMO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola64.png")

"""qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola64.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola65.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola66.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola67.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola68.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola69.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola70.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola71.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola72.png")"""

#print('-----------------TERMINA OCTAVO BLOQUE----------------------')

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola73.png")

"""qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola74.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola75.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola76.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola77.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola78.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola79.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola80.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola81.png")"""

#print('-----------------TERMINA NOVENO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola82.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola83.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola84.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola85.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola86.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola87.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola88.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola89.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("imagenes/hola90.png")

"""#print('-----------------TERMINA DECIMO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola26.png")


#print('-----------------TERMINA ONCEAVO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola27.png")

#print('-----------------TERMINA DOCEAVO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola28.png")


#print('-----------------TERMINA TRECEAVO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola29.png")"""





#print('-----------------AQUI SE EMPIEZAN A GENERAR LOS QR----------------------')

pdf=PDF()
pdf.add_page()
pdf.logo('img.png',0,0,60,15)
#pdf.image('sandra.png',100,100,100,100)
pdf.image('imagenes/hola1.png',20,20,20,20)
"""pdf.image('imagenes/hola2.png',40,20,20,20)
pdf.image('imagenes/hola3.png',60,20,20,20)
pdf.image('imagenes/hola4.png',80,20,20,20)
pdf.image('imagenes/hola5.png',100,20,20,20)
pdf.image('imagenes/hola6.png',120,20,20,20)
pdf.image('imagenes/hola7.png',140,20,20,20)
pdf.image('imagenes/hola8.png',160,20,20,20)
pdf.image('imagenes/hola9.png',180,20,20,20)"""
#print('-----------------TERMINA PRIMER BLOQUE----------------------')
pdf.image('imagenes/hola10.png',20,40,20,20)
"""pdf.image('imagenes/hola11.png',40,40,20,20)
pdf.image('imagenes/hola12.png',60,40,20,20)
pdf.image('imagenes/hola13.png',80,40,20,20)
pdf.image('imagenes/hola14.png',100,40,20,20)
pdf.image('imagenes/hola15.png',120,40,20,20)
pdf.image('imagenes/hola16.png',140,40,20,20)
pdf.image('imagenes/hola17.png',160,40,20,20)
pdf.image('imagenes/hola18.png',180,40,20,20)"""
#print('-----------------TERMINA SEGUNDO BLOQUE----------------------')
pdf.image('imagenes/hola19.png',20,60,20,20)
"""pdf.image('imagenes/hola20.png',40,60,20,20)
pdf.image('imagenes/hola21.png',60,60,20,20)
pdf.image('imagenes/hola22.png',80,60,20,20)
pdf.image('imagenes/hola23.png',100,60,20,20)
pdf.image('imagenes/hola24.png',120,60,20,20)
pdf.image('imagenes/hola25.png',140,60,20,20)
pdf.image('imagenes/hola26.png',160,60,20,20)
pdf.image('imagenes/hola27.png',180,60,20,20)"""
#print('-----------------TERMINA TERCER BLOQUE----------------------')
pdf.image('imagenes/hola28.png',20,80,20,20)
"""pdf.image('imagenes/hola29.png',40,80,20,20)
pdf.image('imagenes/hola30.png',60,80,20,20)
pdf.image('imagenes/hola31.png',80,80,20,20)
pdf.image('imagenes/hola32.png',100,80,20,20)
pdf.image('imagenes/hola33.png',120,80,20,20)
pdf.image('imagenes/hola34.png',140,80,20,20)
pdf.image('imagenes/hola35.png',160,80,20,20)
pdf.image('imagenes/hola36.png',180,80,20,20)"""
#print('-----------------TERMINA CUARTO BLOQUE----------------------')
pdf.image('imagenes/hola37.png',20,100,20,20)
"""pdf.image('imagenes/hola38.png',40,100,20,20)
pdf.image('imagenes/hola39.png',60,100,20,20)
pdf.image('imagenes/hola40.png',80,100,20,20)
pdf.image('imagenes/hola41.png',100,100,20,20)
pdf.image('imagenes/hola42.png',120,100,20,20)
pdf.image('imagenes/hola43.png',140,100,20,20)
pdf.image('imagenes/hola44.png',160,100,20,20)
pdf.image('imagenes/hola45.png',180,100,20,20)"""
#print('-----------------TERMINA QUINTO BLOQUE----------------------')
pdf.image('imagenes/hola46.png',20,120,20,20)
""""pdf.image('imagenes/hola47.png',40,120,20,20)
pdf.image('imagenes/hola48.png',60,120,20,20)
pdf.image('imagenes/hola49.png',80,120,20,20)
pdf.image('imagenes/hola50.png',100,120,20,20)
pdf.image('imagenes/hola51.png',120,120,20,20)
pdf.image('imagenes/hola52.png',140,120,20,20)
pdf.image('imagenes/hola53.png',160,120,20,20)
pdf.image('imagenes/hola54.png',180,120,20,20)"""
#print('-----------------TERMINA SEXTO BLOQUE----------------------')
pdf.image('imagenes/hola55.png',20,140,20,20)
"""pdf.image('imagenes/hola56.png',40,140,20,20)
pdf.image('imagenes/hola57.png',60,140,20,20)
pdf.image('imagenes/hola58.png',80,140,20,20)
pdf.image('imagenes/hola59.png',100,140,20,20)
pdf.image('imagenes/hola60.png',120,140,20,20)
pdf.image('imagenes/hola61.png',140,140,20,20)
pdf.image('imagenes/hola62.png',160,140,20,20)
pdf.image('imagenes/hola63.png',180,140,20,20)"""
#print('-----------------TERMINA SEPTIMO BLOQUE----------------------')
pdf.image('imagenes/hola64.png',20,160,20,20)
"""pdf.image('imagenes/hola65.png',40,160,20,20)
pdf.image('imagenes/hola66.png',60,160,20,20)
pdf.image('imagenes/hola67.png',80,160,20,20)
pdf.image('imagenes/hola68.png',100,160,20,20)
pdf.image('imagenes/hola69.png',120,160,20,20)
pdf.image('imagenes/hola70.png',140,160,20,20)
pdf.image('imagenes/hola71.png',160,160,20,20)
pdf.image('imagenes/hola72.png',180,160,20,20)"""
#print('-----------------TERMINA OCTAVO BLOQUE----------------------')
pdf.image('imagenes/hola73.png',20,180,20,20)
"""pdf.image('imagenes/hola74.png',40,180,20,20)
pdf.image('imagenes/hola75.png',60,180,20,20)
pdf.image('imagenes/hola76.png',80,180,20,20)
pdf.image('imagenes/hola77.png',100,180,20,20)
pdf.image('imagenes/hola78.png',120,180,20,20)
pdf.image('imagenes/hola79.png',140,180,20,20)
pdf.image('imagenes/hola80.png',160,180,20,20)
pdf.image('imagenes/hola81.png',180,180,20,20)"""
#print('-----------------TERMINA NOVENO BLOQUE----------------------')
pdf.image('imagenes/hola82.png',20,200,20,20)
pdf.image('imagenes/hola83.png',40,200,20,20)
pdf.image('imagenes/hola84.png',60,200,20,20)
pdf.image('imagenes/hola85.png',80,200,20,20)
pdf.image('imagenes/hola86.png',100,200,20,20)
pdf.image('imagenes/hola87.png',120,200,20,20)
pdf.image('imagenes/hola88.png',140,200,20,20)
pdf.image('imagenes/hola89.png',160,200,20,20)
pdf.image('imagenes/hola90.png',180,200,20,20)
#print('-----------------TERMINA DECIMO BLOQUE----------------------')
"""pdf.image('hola27.png',20,220,20,20)
#print('-----------------TERMINA ONCEAVO BLOQUE----------------------')
pdf.image('hola28.png',20,240,20,20)
#print('-----------------TERMINA DOCEAVO BLOQUE----------------------')
pdf.image('hola29.png',20,260,20,20)
#print('-----------------TERMINA TRECEAVO BLOQUE----------------------')"""

pdf.output('QR.pdf', 'F')
