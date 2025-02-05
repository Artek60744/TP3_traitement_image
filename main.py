import numpy as np
import cv2 as cv
boules=cv.imread("ressources/images/boules.png")
cv.imshow("boules",boules)
cv.waitKey(0)
cv.destroyAllWindows()

#Question 10 : utilisation de shape et affichage du tableau numpy qui contient l'image
print("Question 10 : ")
print(f"Dimensions de l'image : {boules.shape}")
print(f"Tableau numpy de l'image \n: {boules}")
