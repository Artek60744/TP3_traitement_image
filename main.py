import numpy as np
import cv2 as cv
boules=cv.imread("ressources/images/boules.png")
cv.imshow("boules",boules)
cv.waitKey(0)

#Question 10 : utilisation de shape et affichage du tableau numpy qui contient l'image
print("Question 10 : ")
print(f"Dimensions de l'image : {boules.shape}")
print(f"Tableau numpy de l'image \n: {boules}")

# Récupération des trois canaux RGB de l'image
r_boules, g_boules, b_boules = cv.split(boules)
# Affichage du rouge

cv.imshow("Boules (Rouge)", r_boules)
cv.waitKey(0)
#HSV
# Conversion BGR -> HSV
hsv_boules = cv.cvtColor(boules, cv.COLOR_BGR2HSV)
cv.imshow("Boules (HSV)", hsv_boules)
cv.waitKey(0)
# Extraction des canaux HSV
hue, saturation, value = cv.split(hsv_boules)
# Intervalle teinte rouge
I = 10
min_rouge1 = (0, 50, 50)
max_rouge1 = (I, 255, 255)
min_rouge2 = (180-I, 50, 50)
max_rouge2 = (180, 255, 255)
# Masques des deux intervalles
masque1 = cv.inRange(hsv_boules, min_rouge1, max_rouge1)
masque2 = cv.inRange(hsv_boules, min_rouge2, max_rouge2)
# Fusion des masques
masque_rouge = cv.bitwise_or(masque1, masque2)
cv.imshow("masque rouge", masque_rouge)
cv.waitKey(0)

#Avec imShow, afficher l’image correspondant à ce dernier tableau : les pixels blancs correspondent à ceux dont la valeur de teinte est proche de zéro.
