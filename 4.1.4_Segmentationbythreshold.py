from email.mime import image
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
def graficar(datos):
    plt.figure(1)
    x=range(len(datos))
    plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
    plt.bar(x, datos, align='center')
    plt.title('Histograma')
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    plt.show()
   # plt.savefig(nombre_del_archivo, bbox_inches='tight')

    return None
#IMAGEN 1
Imagen=input("Por favor ingrese el nombre de la imagen con su extension\nEjemplo 2.png\n=====================================================================\n===== LA IMAGEN DEBE ESTAR EN LA MISMA CARPETA QUE ESTE ARCHIVO =====\n=====================================================================\n")
I=plt.imread(Imagen)
rgb = [0.2989, 0.5870, 0.1140]
ig = np.dot(I[...,:3], rgb)
plt.imshow(ig,cmap='gray')
plt.title('Image at grayscale')
plt.show()

h1=[]
h2=[] 
for x in range(len(ig)):
    for h in range(len(ig[x])):
            h1.append(ig[x][h])
            if ig[x][h]<80: 
                ig[x][h]=0
            else:
                ig[x][h]=1
            h2.append(ig[x][h])
plt.imshow(ig,cmap='gray')
plt.title("Segmentacion por umbral")
plt.savefig('temp', bbox_inches='tight')
plt.show()
foto=Image.open('temp.png')
if foto.mode != 'L':
    foto=foto.convert('L')
histograma=foto.histogram()
graficar(histograma)
foto=Image.open(Imagen)
if foto.mode != 'L':
    foto=foto.convert('L')
histograma=foto.histogram()
graficar(histograma)