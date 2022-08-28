import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
#IMAGEN 1
Imagen=input("Por favor ingrese el nombre de la imagen con su extension\nEjemplo 2.png\n=====================================================================\n===== LA IMAGEN DEBE ESTAR EN LA MISMA CARPETA QUE ESTE ARCHIVO =====\n=====================================================================\n")
I=plt.imread(Imagen)
rgb = [0.2989, 0.5870, 0.1140]
ig = np.dot(I[...,:3], rgb)
plt.imshow(ig,cmap='gray')
plt.title('Image at grayscale')
plt.show()

for x in range(len(ig)):
    for h in range(len(ig[x])):
            ig[x][h]=ig[x][h]+10
            if ig[x][h]>=256: 
                ig[x][h]=255
plt.imshow(ig,cmap='gray')
plt.title('Image with high brightness')
plt.show()
ig = np.dot(I[...,:3], rgb)
for x in range(len(ig)):
    for h in range(len(ig[x])):
            ig[x][h]=ig[x][h]*1.5
            if ig[x][h]>=256: 
                ig[x][h]=255
plt.imshow(ig,cmap='gray')
plt.title('Imagen with high contrast')
plt.show()