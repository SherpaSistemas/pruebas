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
img.save("hola1.png")

qr.add_data("Hola2")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola2.png")

qr.add_data("Hola3")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola3.png")

qr.add_data("Luki")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola4.png")

qr.add_data("Kio")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola5.png")

qr.add_data("Luki")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola6.png")

qr.add_data("Luki")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola7.png")

qr.add_data("Luki")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola8.png")

qr.add_data("Luki")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola9.png")

#print('-----------------TERMINA PRIMER BLOQUE----------------------')

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola10.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola11.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola12.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola13.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola14.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola15.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola16.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola17.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola18.png")

#print('-----------------TERMINA SEGUNDO BLOQUE----------------------')

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola19.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola20.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola21.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola22.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola23.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola24.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola25.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola26.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola27.png")

#print('-----------------TERMINA TERCER BLOQUE----------------------')

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola28.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola29.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola30.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola31.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola32.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola33.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola34.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola35.png")

qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola36.png")



























#print('-----------------TERMINA CUARTO BLOQUE----------------------')

"""qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola21.png")

#print('-----------------TERMINA QUINTO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola21.png")

#print('-----------------TERMINA SEXTO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola22.png")

#print('-----------------TERMINA SEPTIMO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola23.png")

#print('-----------------TERMINA OCTAVO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola24.png")

#print('-----------------TERMINA NOVENO BLOQUE----------------------')
qr.add_data("Milton")
qr.make(fit=True)
img=qr.make_image(fill_color=(0,0,0),back_color=(255,255,255))
img.save("hola25.png")

#print('-----------------TERMINA DECIMO BLOQUE----------------------')
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
pdf.image('hola1.png',20,20,20,20)
pdf.image('hola2.png',40,20,20,20)
pdf.image('hola3.png',60,20,20,20)
pdf.image('hola4.png',80,20,20,20)
pdf.image('hola5.png',100,20,20,20)
pdf.image('hola6.png',120,20,20,20)
pdf.image('hola7.png',140,20,20,20)
pdf.image('hola8.png',160,20,20,20)
pdf.image('hola9.png',180,20,20,20)
#print('-----------------TERMINA PRIMER BLOQUE----------------------')
pdf.image('hola10.png',20,40,20,20)
pdf.image('hola11.png',40,40,20,20)
pdf.image('hola12.png',60,40,20,20)
pdf.image('hola13.png',80,40,20,20)
pdf.image('hola14.png',100,40,20,20)
pdf.image('hola15.png',120,40,20,20)
pdf.image('hola16.png',140,40,20,20)
pdf.image('hola17.png',160,40,20,20)
pdf.image('hola18.png',180,40,20,20)
#print('-----------------TERMINA SEGUNDO BLOQUE----------------------')
pdf.image('hola19.png',20,60,20,20)
pdf.image('hola20.png',40,60,20,20)
pdf.image('hola21.png',60,60,20,20)
pdf.image('hola22.png',80,60,20,20)
pdf.image('hola23.png',100,60,20,20)
pdf.image('hola24.png',120,60,20,20)
pdf.image('hola25.png',140,60,20,20)
pdf.image('hola26.png',160,60,20,20)
pdf.image('hola27.png',180,60,20,20)
#print('-----------------TERMINA TERCER BLOQUE----------------------')
pdf.image('hola28.png',20,80,20,20)
pdf.image('hola29.png',40,80,20,20)
pdf.image('hola30.png',60,80,20,20)
pdf.image('hola31.png',80,80,20,20)
pdf.image('hola32.png',100,80,20,20)
pdf.image('hola33.png',120,80,20,20)
pdf.image('hola34.png',140,80,20,20)
pdf.image('hola35.png',160,80,20,20)
pdf.image('hola36.png',180,80,20,20)
#print('-----------------TERMINA CUARTO BLOQUE----------------------')
"""pdf.image('hola21.png',20,100,20,20)
#print('-----------------TERMINA QUINTO BLOQUE----------------------')
pdf.image('hola22.png',20,120,20,20)
#print('-----------------TERMINA SEXTO BLOQUE----------------------')
pdf.image('hola23.png',20,140,20,20)
#print('-----------------TERMINA SEPTIMO BLOQUE----------------------')
pdf.image('hola24.png',20,160,20,20)
#print('-----------------TERMINA OCTAVO BLOQUE----------------------')
pdf.image('hola25.png',20,180,20,20)
#print('-----------------TERMINA NOVENO BLOQUE----------------------')
pdf.image('hola26.png',20,200,20,20)
#print('-----------------TERMINA DECIMO BLOQUE----------------------')
pdf.image('hola27.png',20,220,20,20)
#print('-----------------TERMINA ONCEAVO BLOQUE----------------------')
pdf.image('hola28.png',20,240,20,20)
#print('-----------------TERMINA DOCEAVO BLOQUE----------------------')
pdf.image('hola29.png',20,260,20,20)
#print('-----------------TERMINA TRECEAVO BLOQUE----------------------')"""

pdf.output('QR.pdf', 'F')
