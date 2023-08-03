---
 TutorialInfo:r
   Topic:  Part : écrire un script - Roulement à bille #2
   Level:  Débutant
   Time:  30 min
   Author: r-frank
   FCVersion: 0.16.6706
   Files: 
}}

### Introduction

Ce tutoriel se veut une introduction pour les débutants à la création de pièces avec des scripts python dans FreeCAD.
Ce tutoriel explique comment construire un roulement à billes, avec un flux de travail, qui consiste à créer des esquisses et à les faire pivoter.
Le code produira un nouveau document FreeCAD avec 12 formes .
Cela ressemblera à ceci :
!{width="400"}

### Workflow ou flux de travail 

Le flux de travail est plus ou moins identique à la façon dont vous créeriez la pièce dans l\'atelier Part Design
Juste quelques petites differences.
\*Créer un nouveau document vide et en faire le document actif

-   Dessinez la forme de base de l\'anneau extérieur composé de quatre lignes droites et de quatre arcs

!{width="150"}

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
-   Insérer des billes avec le même flux de travail que dans la partie 1 
-   Définir la vue sur axonométrique
-   Zoomez pour une vue d\'ensemble

### Concevoir la rainure 

Dessiner un arc nécessite trois points ou un angle de départ et un angle de fin.
Dans sketcher , nous pourrions utiliser des contraintes pour définir le point de départ et le point final de l\'arc.
Comme nous ne pouvons pas faire cela dans les scripts, nous dessinons un rectangle arrondi et le faisons pivoter pour obtenir une \"forme d\'anneau\" de base.
Ensuite, nous dessinons un cercle et le faisons tourner pour obtenir la géométrie de la rainure.
Ensuite, nous appliquons une coupe booléenne aux deux figures de révolution et nous avons la forme complète de l\'anneau intérieur / extérieur.

### Insérez les billes 

Le flux de travail approprié basé sur sketcher  pour insérer les billes serait :
\*Tracez un arc  dont le centre est identique à l\'origine et tracez un segment fermant le côté \"ouvert\" de l\'arc

-   Convertissez les deux éléments en un contour, transformez le en face, tournez autour de l\'axe z pour obtenir une forme de boule
-   Utilisez la commande \"translate\"  pour déplacer la bille dans la bonne position
-   Répétez les étapes ci-dessus neuf fois, en utilisant la fonction mathématique pour créer et positionner les autres billes
-   Cette opération répétitive peut être programmée avec une boucle

Maintenant, ce n\'est pas efficace, insérer des primitives et les positionner est plus facile et plus rapide dans ce cas.
Nous utilisons donc la même méthode que dans \"Objets scriptés \"Part\" : Roulement à billes - Partie 1\".

### Liens

Objets créés par script : La page wiki expliquant les bases du langage de script
Scripts pour création topologique : Un tutoriel qui couvre les bases de la création de scripts
Objets scriptés \"Part\" : Roulement à billes - Partie 1 : Le faire avec des esquisses
Bearings from scripted sketches : Base utilisée pour ce tutoriel, grâce à JMG \...

### Code


{{Code   code: 
## Ball-bearing script
## 11.08.2016 by r-frank 
## based on ball bearing script by JMG
## 
#
#needed for doing boolean operations
import Part
#needed for calculating the positions of the balls
import math
#needed for translation and rotation of objects
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
#
#Lines for basic shape of outer ring
L1o=Part.makeLine,)
L2o=Part.makeLine,)
L3o=Part.makeLine,)
L4o=Part.makeLine,)
#Corner rounding for basic shape of outer ring
A1o=Part.makeCircle,Base.Vector,0,90)
A2o=Part.makeCircle,Base.Vector,90,180)
A3o=Part.makeCircle,Base.Vector,180,270)
A4o=Part.makeCircle,Base.Vector,270,360)
#Connect Lines and arcs to make wire and upgrade to face, revolve and apply cut to obtain groove
OR=Part.Wire
OR=Part.Face
OR=OR.revolve,Base.Vector)
C1=Part.makeCircle/2,0,TH/2),Base.Vector,0,360)
GRo=Part.Wire
GRo=Part.Face
GRo=GRo.revolve,Base.Vector)
OR=OR.cut
Part.show
#
#Lines for basic shape of inner ring
L1i=Part.makeLine,)
L2i=Part.makeLine,)
L3i=Part.makeLine,)
L4i=Part.makeLine,)
#Corner rounding for basic shape of inner ring
A1i=Part.makeCircle,Base.Vector,0,90)
A2i=Part.makeCircle,Base.Vector,90,180)
A3i=Part.makeCircle,Base.Vector,180,270)
A4i=Part.makeCircle,Base.Vector,270,360)
#Connect Lines and arcs to make wire and upgrade to face, revolve and apply cut to obtain groove
IR=Part.Wire
IR=Part.Face
IR=IR.revolve,Base.Vector)
C2=Part.makeCircle/2,0,TH/2),Base.Vector,0,360)
GRi=Part.Wire
GRi=Part.Face
GRi=GRi.revolve,Base.Vector)
IR=IR.cut
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
App.ActiveDocument.recompute
Gui.ActiveDocument.ActiveView.viewAxometric
Gui.SendMsgToActiveView
---

# Scripted Parts: Ball Bearing - Part 2/fr

 

{{Powerdocnavi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted Parts: Ball Bearing - Part 2/fr
