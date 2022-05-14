import gopigo
import time
from easygopigo3 import EasyGoPiGo3

gpg = EasyGoPiGo3()
d = gpg.forward()                     # Démarrage du gopigo forward, vitesse réglée de base à 300°/seconde de roue
c = gpg.read_encoders()               # Première récupération du positionnement angulaire des roues

while True : 
    
    b = gpg.read_encoders()           # Seconde récupération du positionnement angulaire des roues
    dg = b[0] - c[0]                  # Calcul de la distance angulaire de la roue gauche
    dd = b[1] - c[1]                  # Calcul de la distance angulaire de la roue droite
    diff =  abs(dg - dd)              # Calcul de la différence absolu de distance angulaire parcouru par les deux roues
    print("difference =",diff)
    c = b                             # Changement de référentiel angulaire
    
    if dd - dg > 0 :                  # Retard de la roue gauche ou roue droite en avance
        vitesse = diff/0.5            # Calcul de la vitesse angulaire de différence
        v = (vitesse/gpg.get_speed)*100 # Calcul de cette vitesse angulaire de différence en pourcentage par rapport à la vitesse initiale
       
        t_end = time.time() + 0.5     # Timer de 0.5 seconde pour la boucle while
        
        while time.time() < t_end:    # Boucle while tournant pendant 0.5 seconde
            gpg.steer(100,100-v)      # Ralentissement de la roue droite du pourcnetage calculé précédement
        
    elif dd - dg < 0 :                # Retard de la roue droite ou roue gauche en avance
        vitesse = diff/0.5            
        v = (vitesse/gpg.get_speed)*100
        
        t_end = time.time() + 0.5
        
        while time.time() < t_end:
            gpg.steer(100-v,100)      #Ralentissement de la roue gauche
        
