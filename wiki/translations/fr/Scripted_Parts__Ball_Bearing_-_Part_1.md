# Scripted Parts: Ball Bearing - Part 1/fr
{{TutorialInfo/fr
|Topic= Part : écrire un script - Roulement à bille #1
|Level= Débutant
|Time= 30 min
|Author=r-frank
|FCVersion=0.16.6706
|Files=
}}

### Introduction

Ce tutoriel est conçu comme une introduction pour les débutants à la création de pièces avec des scripts python dans FreeCAD.
Ce tutoriel expliquera comment construire un roulement à billes avec un workflow (flux de travail) CSG.
Le code produira un nouveau document FreeCAD avec 12 formes (anneau intérieur, anneau extérieur et 10 billes / sphères).
Cela ressemblera à ceci :
<img alt="" src=images/Tutorial_BallBearing01.jpg  style="width:400px;">

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

Dans l\'atelier Part (pièce) en utilisant l\'interface graphique, vous sélectionneriez des chanfreins dans la vue 3D ou dans le menu pour les congés, puis appliquez les congés.
Ici, nous sélectionnons toutes les arrêtes d\'une forme et appliquons des congés.
Par conséquent, nous devons sélectionner les arrêtes AVANT de créer la rainure.

### Notes

Ce tutoriel utilise des primitives Part et des opérations booléennes, ce qui peut nécessiter de la puissance de calcul.
Pour faire une pièce \"scriptée\" avec des esquisses de révolution, consultez le didacticiel [Scripted Parts: Ball Bearing - Part 2](Scripted_Parts:_Ball_Bearing_-_Part_2.md).

### Liens

[Objets créés par script](Scripted_objects/fr.md) : La page wiki expliquant les bases du langage de script
[Scripts pour création topologique](Topological_data_scripting/fr.md) : Un tutoriel qui couvre les bases de la création de scripts
[Objets scriptés \"Part\" : Roulement à billes - Partie 2](Scripted_Parts:_Ball_Bearing_-_Part_2/fr.md) : Le faire avec des esquisses
[Bearing Script 1](http://linuxforanengineer.blogspot.de/2013/08/free-cad-bearing-script.html) : Base utilisée pour ce tutoriel, grâce à JMG \...

### Code


```python
## Ball-bearing script
## 11.08.2016 by r-frank (BPLRFE/LearnFreeCAD on Youtube)
## based on ball bearing script by JMG
## (http://linuxforanengineer.blogspot.de/2013/08/free-cad-bearing-script.html)
#
#needed for inserting primitives
import Part
#needed for calculating the positions of the balls
import math
#needed for translation of torus
from FreeCAD import Base
#
#VALUES#
#(radius of shaft/inner radius of inner ring)
R1=15.0
#(outer radius of inner ring)
R2=25.0
#(inner radius of outer ring)
R3=30.0
#(outer radius of outer ring)
R4=40.0
#(thickness of bearing)
TH=15.0
#(number of balls)
NBall=10
#(radius of ball)
RBall=5.0
#(rounding radius for fillets)
RR=1
#first coordinate of center of ball
CBall=((R3-R2)/2)+R2
#second coordinate of center of ball
PBall=TH/2
#
#Create new document
App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
#
#Inner Ring#
B1=Part.makeCylinder(R1,TH)
B2=Part.makeCylinder(R2,TH)
IR=B2.cut(B1)
#get edges and apply fillets
Bedges=IR.Edges
IRF=IR.makeFillet(RR,Bedges)
#create groove and show shape
T1=Part.makeTorus(CBall,RBall)
T1.translate(Base.Vector(0,0,TH/2))
InnerRing=IRF.cut(T1)
Part.show(InnerRing)
#
#Outer Ring#
B3=Part.makeCylinder(R3,TH)
B4=Part.makeCylinder(R4,TH)
OR=B4.cut(B3)
#get edges and apply fillets
Bedges=OR.Edges
ORF=OR.makeFillet(RR,Bedges)
#create groove and show shape
T2=Part.makeTorus(CBall,RBall)
T2.translate(Base.Vector(0,0,TH/2))
OuterRing=ORF.cut(T2)
Part.show(OuterRing)
#
#Balls#
for i in range(NBall):
  Ball=Part.makeSphere(RBall)
  Alpha=(i*2*math.pi)/NBall
  BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),TH/2)
  Ball.translate(BV)
  Part.show(Ball)
#
#Make it pretty#
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```


{{Powerdocnavi

}} 

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Scripted Parts: Ball Bearing - Part 1/fr
