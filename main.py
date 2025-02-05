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

# Récupération des trois canaux RGB de l'image
r_boules, g_boules, b_boules = cv.split(boules)
# Affichage du rouge
cv.imshow("Boules (Rouge)", r_boules)
cv.waitKey(0)
