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

#question 13 :
# Segmentation multi-canaux
min_rouge1 = (0, 100, 50)
max_rouge1 = (I, 255, 255)
min_rouge2 = (180-I, 100, 50)
max_rouge2 = (180, 255, 255)
masque1 = cv.inRange(hsv_boules, min_rouge1, max_rouge1)
masque2 = cv.inRange(hsv_boules, min_rouge2, max_rouge2)
masque_rouge = cv.bitwise_or(masque1, masque2)
cv.imshow("masque rouge segmentation multicanaux", masque_rouge)
cv.waitKey(0)

#Question 14 :
kernel = np.ones((5, 5), np.uint8)
fermeture = cv.morphologyEx(masque_rouge, cv.MORPH_CLOSE, kernel)
ouverture = cv.morphologyEx(fermeture, cv.MORPH_OPEN, kernel)
cv.imshow("Masque rouge ameliore", ouverture)
cv.waitKey(0)

# Détecter la bille avec les contours
contours,_= cv.findContours(ouverture, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
if contours:
    (x, y), radius = cv.minEnclosingCircle(max(contours, key=cv.contourArea))
    center = (int(x), int(y))
    radius = int(radius)
    cv.circle(boules, center, radius, (255, 255, 255), 2) # cercle blanc épaisseur 2
    cv.imshow("Boules avec contours", boules)
    cv.waitKey(0)

cv.destroyAllWindows()

def drawCircleOnRedMarble(image: np.ndarray):
    # Conversion image en HSV
    image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    I = 10 # seuil
    # Segmentation multi-canaux
    image_seg = cv.inRange(image_hsv, (0-I, 100, 0), (0+I, 255, 255))

    kernel = np.ones((5, 5), np.uint8)
    fermeture = cv.morphologyEx(image_seg, cv.MORPH_CLOSE, kernel)
    ouverture = cv.morphologyEx(fermeture, cv.MORPH_OPEN, kernel)
    contours,_ = cv.findContours(ouverture, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    if contours:
        (x, y), radius = cv.minEnclosingCircle(max(contours, key=cv.contourArea))
        center = (int(x), int(y))
        radius = int(radius)
        cv.circle(image, center, radius, (255, 255, 255), 2) # cercle blanc épaisseur 2
        cv.imshow("TP3 video", image)
        cv.waitKey(100) # 100 ms

### Travail sur la vidéo
cap = cv.VideoCapture('./billes.mp4')
if not cap.isOpened():
    print("Erreur : impossible d'ouvrir la vidéo.")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    drawCircleOnRedMarble(frame)
cap.release()