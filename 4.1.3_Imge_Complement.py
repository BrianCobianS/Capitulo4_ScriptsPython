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
#2 procesamiento            
IC=255-ig
plt.imshow(IC,cmap='gray')
plt.title('Imagen complemento')
plt.show()