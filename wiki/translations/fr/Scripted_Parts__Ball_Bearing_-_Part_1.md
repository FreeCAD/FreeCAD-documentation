---
 TutorialInfo:r
   Topic: Part Tutoriel écrire un script - Roulement à bille #1
   Level: Débutant
   Time: 30 min
   Author: r-frank
   FCVersion: 0.16.6706
   Files: 
}}

### Introduction

Ce tutoriel est conçu comme une introduction pour les débutants à la création de pièces avec des scripts python dans FreeCAD.
Ce tutoriel expliquera comment construire un roulement à billes avec un workflow  CSG.
Le code produira un nouveau document FreeCAD avec 12 formes .
Cela ressemblera à ceci :
!{width="400"}

### Workflow ou flux de travail 

Le flux de travail est plus ou moins identique à la façon dont vous créeriez la pièce dans l\'atelier Part.
Juste quelques petites differences.
\*Créer un nouveau document vide et en faire le document actif

-   Insérez un cylindre
-   Insérez un cylindre
-   Faites une coupe booléenne pour obtenir la forme de base de la bague intérieure
-   Sélectionnez toutes les arêtes et appliquez un congé
-   Insérez un tore
-   Déplacez le tore en position et faites une coupe booléenne pour créer la rainure pour les billes
-   Répétez toutes les étapes pour obtenir la forme de la bague extérieure
-   Insérer la première bille
-   Insérez d\'autres billes en utilisant les mathématiques pour calculer la position des billes
-   Définir la vue sur axonométrique
-   Zoomez pour une vue d\'ensemble

### Filetage des arrêtes 

Dans l\'atelier Part  en utilisant l\'interface graphique, vous sélectionneriez des chanfreins dans la vue 3D ou dans le menu pour les congés, puis appliquez les congés.
Ici, nous sélectionnons toutes les arrêtes d\'une forme et appliquons des congés.
Par conséquent, nous devons sélectionner les arrêtes AVANT de créer la rainure.

### Notes

Ce tutoriel utilise des primitives Part et des opérations booléennes, ce qui peut nécessiter de la puissance de calcul.
Pour faire une pièce \"scriptée\" avec des esquisses de révolution, consultez le didacticiel Scripted Parts: Ball Bearing - Part 2.

### Liens

Objets créés par script : La page wiki expliquant les bases du langage de script
Scripts pour création topologique : Un tutoriel qui couvre les bases de la création de scripts
Objets scriptés \"Part\" : Roulement à billes - Partie 2 : Le faire avec des esquisses
Bearing Script 1 : Base utilisée pour ce tutoriel, grâce à JMG \...

### Code


{{Code   code: 
## Ball-bearing script
## 11.08.2016 by r-frank 
## based on ball bearing script by JMG
## 
#
#needed for inserting primitives
import Part
#needed for calculating the positions of the balls
import math
#needed for translation of torus
from FreeCAD import Base
#
#VALUES#
#
R1=15.0
#
R2=25.0
#
R3=30.0
#
R4=40.0
#
TH=15.0
#
NBall=10
#
RBall=5.0
#
RR=1
#first coordinate of center of ball
CBall=/2)+R2
#second coordinate of center of ball
PBall=TH/2
#
#Create new document
App.newDocument
App.setActiveDocument
App.ActiveDocument=App.getDocument
Gui.ActiveDocument=Gui.getDocument
#
#Inner Ring#
B1=Part.makeCylinder
B2=Part.makeCylinder
IR=B2.cut
#get edges and apply fillets
Bedges=IR.Edges
IRF=IR.makeFillet
#create groove and show shape
T1=Part.makeTorus
T1.translate)
InnerRing=IRF.cut
Part.show
#
#Outer Ring#
B3=Part.makeCylinder
B4=Part.makeCylinder
OR=B4.cut
#get edges and apply fillets
Bedges=OR.Edges
ORF=OR.makeFillet
#create groove and show shape
T2=Part.makeTorus
T2.translate)
OuterRing=ORF.cut
Part.show
#
#Balls#
for i in range:
  Ball=Part.makeSphere
  Alpha=/NBall
  BV=,CBall*math.sin,TH/2)
  Ball.translate
  Part.show
#
#Make it pretty#
App.activeDocument.recompute
Gui.activeDocument.activeView.viewAxometric
Gui.SendMsgToActiveView
---

# Scripted Parts: Ball Bearing - Part 1/fr

 

{{Powerdocnavi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripted Parts: Ball Bearing - Part 1/fr
