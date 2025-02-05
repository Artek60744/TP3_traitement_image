from exos.exo1 import exercice1
from exos.exo2 import exercice2
from exos.exo3 import exercice3
from exos.traitement import traitement1, traitement2, traitement3
from exos.contour import contour

# import cv2 as cv

def main():
    print("Début du programme principal")
    
    # Appel des fonctions des exercices
    print("\nExercice 1 : ")
    exercice1()
    print("\nExercice 2 : ")
    exercice2()
    print("\nExercice 3 : ")
    exercice3()
    print("\nExercice 4 : ")
    image_binary = traitement1()
    tmp=traitement2()
    tmp2 = traitement3(tmp)
    contour(image_binary)


    print("Fin du programme principal")

if __name__ == "__main__":
    main()