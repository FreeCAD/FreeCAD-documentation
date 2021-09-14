# Scripted Parts: Ball Bearing - Part 2/fr

 {{TutorialInfo/fr
|Topic= Part : écrire un script - Roulement à bille #2
|Level= Débutant
|Time= 30 min
|Author=r-frank
|FCVersion=0.16.6706
|Files=
}}

### Introduction

Ce tutoriel se veut une introduction pour les débutants à la création de pièces avec des scripts python dans FreeCAD.
Ce tutoriel explique comment construire un roulement à billes, avec un flux de travail, qui consiste à créer des esquisses et à les faire pivoter.
Le code produira un nouveau document FreeCAD avec 12 formes (anneau intérieur, anneau extérieur et 10 billes / sphères).
Cela ressemblera à ceci :
<img alt="" src=images/Tutorial_BallBearing01.jpg  style="width:400px;">

### Workflow ou flux de travail 

Le flux de travail est plus ou moins identique à la façon dont vous créeriez la pièce dans l\'atelier Part Design
Juste quelques petites differences.
\*Créer un nouveau document vide et en faire le document actif

-   Dessinez la forme de base de l\'anneau extérieur composé de quatre lignes droites et de quatre arcs

<img alt="" src=images/TutorialBallBearing_P2-Sketch.png  style="width:150px;">

-   Reliez les lignes et les arcs et transformez les en un seul contour
-   Transformer le contour en face
-   Faites pivoter la face pour obtenir une forme volumique
-   Dessinez un cercle
-   Transformer le cercle en contour
-   Transformer le contour en face
-   Faire pivoter la face et appliquer une coupe booléenne pour obtenir une rainure dans la bague extérieure
-   Dessinez la forme de base de la bague intérieure composée de quatre lignes droites et de quatre arcs
-   Connectez les lignes et les arcs et transformez les en un seul contour
-   Transformer le contour en face
-   Faites pivoter la face pour obtenir une forme volumique
-   Dessinez un cercle
-   Transformer le cercle en contour
-   Transformer le contour en face
-   Faire pivoter la face et appliquer une coupe booléenne pour obtenir une rainure dans la bague intérieure
-   Insérer des billes avec le même flux de travail que dans la partie 1 (plus d\'efficacité)
-   Définir la vue sur axonométrique
-   Zoomez pour une vue d\'ensemble

### Concevoir la rainure 

Dessiner un arc nécessite trois points ou un angle de départ et un angle de fin.
Dans sketcher (l\'esquisseur), nous pourrions utiliser des contraintes pour définir le point de départ et le point final de l\'arc.
Comme nous ne pouvons pas faire cela dans les scripts, nous dessinons un rectangle arrondi et le faisons pivoter pour obtenir une \"forme d\'anneau\" de base.
Ensuite, nous dessinons un cercle et le faisons tourner pour obtenir la géométrie de la rainure.
Ensuite, nous appliquons une coupe booléenne aux deux figures de révolution et nous avons la forme complète de l\'anneau intérieur / extérieur.

### Insérez les billes 

Le flux de travail approprié basé sur sketcher (l\'esquisseur) pour insérer les billes serait :
\*Tracez un arc (demi-cercle) dont le centre est identique à l\'origine et tracez un segment fermant le côté \"ouvert\" de l\'arc

-   Convertissez les deux éléments en un contour, transformez le en face, tournez autour de l\'axe z pour obtenir une forme de boule
-   Utilisez la commande \"translate\" (traduire) pour déplacer la bille dans la bonne position
-   Répétez les étapes ci-dessus neuf fois, en utilisant la fonction mathématique pour créer et positionner les autres billes
-   Cette opération répétitive peut être programmée avec une boucle

Maintenant, ce n\'est pas efficace, insérer des primitives et les positionner est plus facile et plus rapide dans ce cas.
Nous utilisons donc la même méthode que dans \"[Objets scriptés \"Part\" : Roulement à billes - Partie 1](Scripted_Parts:_Ball_Bearing_-_Part_1/fr.md)\".

### Liens

[Objets créés par script](Scripted_objects/fr.md) : La page wiki expliquant les bases du langage de script
[Scripts pour création topologique](Topological_data_scripting/fr.md) : Un tutoriel qui couvre les bases de la création de scripts
[Objets scriptés \"Part\" : Roulement à billes - Partie 1](Scripted_Parts:_Ball_Bearing_-_Part_1/fr.md) : Le faire avec des esquisses
[Bearings from scripted sketches](http://linuxforanengineer.blogspot.de/2013/12/bearings-from-scripted-sketches.html) : Base utilisée pour ce tutoriel, grâce à JMG \...

### Code


```python
## Ball-bearing script
## 11.08.2016 by r-frank (BPLRFE/LearnFreeCAD on Youtube)
## based on ball bearing script by JMG
## (http://linuxforanengineer.blogspot.de/2013/12/bearings-from-scripted-sketches.html)
#
#needed for doing boolean operations
import Part
#needed for calculating the positions of the balls
import math
#needed for translation and rotation of objects
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
#
#Lines for basic shape of outer ring
L1o=Part.makeLine((R4,0,TH-RR),(R4,0,RR))
L2o=Part.makeLine((R4-RR,0,0),(R3+RR,0,0))
L3o=Part.makeLine((R3,0,RR),(R3,0,TH-RR))
L4o=Part.makeLine((R3+RR,0,TH),(R4-RR,0,TH))
#Corner rounding for basic shape of outer ring
A1o=Part.makeCircle(RR,Base.Vector(R4-RR,0,RR),Base.Vector(0,1,0),0,90)
A2o=Part.makeCircle(RR,Base.Vector(R3+RR,0,RR),Base.Vector(0,1,0),90,180)
A3o=Part.makeCircle(RR,Base.Vector(R3+RR,0,TH-RR),Base.Vector(0,1,0),180,270)
A4o=Part.makeCircle(RR,Base.Vector(R4-RR,0,TH-RR),Base.Vector(0,1,0),270,360)
#Connect Lines and arcs to make wire and upgrade to face, revolve and apply cut to obtain groove
OR=Part.Wire([L1o,A1o,L2o,A2o,L3o,A3o,L4o,A4o])
OR=Part.Face(OR)
OR=OR.revolve(Base.Vector(0,0,1),Base.Vector(0,0,360))
C1=Part.makeCircle(RBall,Base.Vector(R2+(R3-R2)/2,0,TH/2),Base.Vector(0,1,0),0,360)
GRo=Part.Wire([C1])
GRo=Part.Face(GRo)
GRo=GRo.revolve(Base.Vector(0,0,1),Base.Vector(0,0,360))
OR=OR.cut(GRo)
Part.show(OR)
#
#Lines for basic shape of inner ring
L1i=Part.makeLine((R2,0,TH-RR),(R2,0,RR))
L2i=Part.makeLine((R2-RR,0,0),(R1+RR,0,0))
L3i=Part.makeLine((R1,0,RR),(R1,0,TH-RR))
L4i=Part.makeLine((R1+RR,0,TH),(R2-RR,0,TH))
#Corner rounding for basic shape of inner ring
A1i=Part.makeCircle(RR,Base.Vector(R2-RR,0,RR),Base.Vector(0,1,0),0,90)
A2i=Part.makeCircle(RR,Base.Vector(R1+RR,0,RR),Base.Vector(0,1,0),90,180)
A3i=Part.makeCircle(RR,Base.Vector(R1+RR,0,TH-RR),Base.Vector(0,1,0),180,270)
A4i=Part.makeCircle(RR,Base.Vector(R2-RR,0,TH-RR),Base.Vector(0,1,0),270,360)
#Connect Lines and arcs to make wire and upgrade to face, revolve and apply cut to obtain groove
IR=Part.Wire([L1i,A1i,L2i,A2i,L3i,A3i,L4i,A4i])
IR=Part.Face(IR)
IR=IR.revolve(Base.Vector(0,0,1),Base.Vector(0,0,360))
C2=Part.makeCircle(RBall,Base.Vector(R2+(R3-R2)/2,0,TH/2),Base.Vector(0,1,0),0,360)
GRi=Part.Wire([C2])
GRi=Part.Face(GRi)
GRi=GRi.revolve(Base.Vector(0,0,1),Base.Vector(0,0,360))
IR=IR.cut(GRi)
Part.show(IR)
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
App.ActiveDocument.recompute()
Gui.ActiveDocument.ActiveView.viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
