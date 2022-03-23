# Macro FCSpring Helix Variable/fr
{{Macro/fr
|Name=Macro FCSpring Helix Variable
|Icon=FCSpring Helix Variable.png
|Description=Cette macro crée un ressort avec personnalisable, tout tour peut changer la configuration du ressort peut être enregistré dans un fichier avec l'extension '''.FCSpring'''.<br/>Sont détectés: Surface (direction de la face), Cylindre (rayon), Ellipse (rayon mineur), Sphère (rayon), Tore (rayon1), Plan (direction), Ligne (suit la direction), point (Position XYZ du vertex) <br / > Si aucun objet n'est détecté (pas de sélection), le ressort est créé au point XYZ 0., 0., 0. <br/>Voir des [https://www.freecadweb.org/wiki/Macro_FCSpring_Helix_Variable/fr#Exemples exemples]
|Author=Mario52
|Version=01.18
|Date=2022/03/16
|Download= du fichier .zip [https://forum.freecadweb.org/download/file.php?id=80844 des icônes]
|FCVersion=0.19
}}

## Description

Cette macro crée un ressort hautement personnalisable. Toute modification modifiant la configuration du ressort peut être enregistrée dans un fichier avec l\'extension .FCSpring ou coordonnées .FCSpringCoor
Sont détectées: Surface (Direction de la face), Cylindre (Rayon), Ellipse (MinorRadius), Sphère (Rayon), Toroid (Rayon1), Plan (direction), ligne (suivre la direction), point (position du sommet XYZ)
Si aucun objet n\'est détecté (pas de sélection) le ressort est créé au point XYZ 0., 0., 0.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/68c81c32a0727a693d3a/raw/8b0b60336a62f22c0730e6fb88687ffd1b1dd502/Macro_FCSpring_Helix_Variable.FCMacro}}

<img alt="" src=images/TruncateSpring00.png  style="width:400px;"> 
*FCSpring Helix Variable*

## Utilisation

Cette section est utilisée pour configurer le ressort.

Détail schématique de la définition du ressort

![](images/Macro_TruncateSpring_01.png ) 

#### Interface graphique 

![](images/Macro_FCSpring_Helix_Variable_01.png ) 

#### Configuration

-    {{SpinBox|10 coils}}**Number of coil** : Nombre total de spires du ressort. Par défaut = 10

-    {{SpinBox|20,000 mm}}**Radius of spring** : Rayon du ressort. Par défaut = 20.0

-    {{SpinBox|15,000 mm}}**Pitch of spring** : Pas du ressort. Par défaut = 15.0

-    {{SpinBox|5 ( 72 points )}}**Precision of turn** : Précision par tour. Cela correspond au nombre de points par tour. Le nombre de points est calculé comme suit : precision (nombre de points) = (pitch / (360/precision)). Par défaut = 5 (72 points)

-    {{SpinBox|20,000 mm}}: Rayon du grand cercle du cône ({{CheckBox|TRUE|Spring conical}} doit être coché)

-    {{CheckBox|Spring conical}}: Grand diamètre du cône. Cette dimension sera toujours supérieure au rayon

-    {{CheckBox|Angles}}: Case à cocher pour activer la fonction Begin et End des angles des spires.
    Si la fonction est activée, le réglage {{SpinBox|1 ( 360 points )}} se règle automatiquement à 1 (360 points par tour, 1 point = 1 degré)

-    {{SpinBox|0 deg}}**Begin** : Angle de départ ou commence la première spire.

-    {{SpinBox|360 deg}}**End** : Angle de fin ou se termine la dernière spire.

![](images/Macro_FCSpring_Helix_Variable_02.png ) 

#### Type de ligne 

-    {{RadioButton|TRUE|<img src="images/Draft_BSpline.svg" width=24px> Bspline}}**BSpline** : le type de ligne est une BSpline.

-    {{RadioButton|<img src="images/Draft_Wire.svg" width=24px> Wire}}**Wire** : le type ligne est filaire.

-    {{CheckBox|<img src="images/Draft_Point.svg" width=24px> Points}}**Points** : Si la case est cochée, un point est créé sur chaque point.

-    {{CheckBox|Reverse}}**Reverse** : Mode inverse. Si la case est cochée, le ressort change de direction (sens horaire).

![](images/Macro_FCSpring_Helix_Variable_03.png ) 

#### Option

Cette section s\'affiche dès qu\'un objet est sélectionné. le type d\'objet est renseigné dans l\'éditeur de texte

L\'objet peut être une ligne, 2 points, cercle, arête\... Un axe de la longueur du ressort est automatiquement créé.

Détection : Cylindre (radius), Sphère (rayon), Tore (rayon) , Cône (petit rayon), Cercle (rayon), Arc (rayon), Ellipse (petit rayon)

-    **Normal**: Si un cercle est sélectionné **Normal**, ne modifie pas le rayon du cercle (Par défaut)

    -   
        **Adapt Rad.**
        
        : Si le bouton **Normal** est pressé, le texte **Adapt Rad.** est affiché, le rayon du ressort est adapté au rayon du cercle ou de l\'objet sélectionné (Si un rayon est détecté)

-    **Point Mouse**: Si le clic de souris se fait sur une face, le point de la souris sera le point de départ de l\'axe (Par défaut)

    -   
        **Center Face**
        
        : Si le bouton **Point Mouse** est pressé, le texte du bouton change et le ressort sera créé au centre de la face sélectionnée

-    {{CheckBox|Position}}: Si deux objets sont sélectionnés (le premier l\'axe et le second le ressort (ou tout autre objet)), cette case est activé et vous pouvez de modifier l\'emplacement du ressort (le deuxième objet) le long de l\'axe (premier objet). {{CheckBox|TRUE|Position}} doit être sélectionnée sur \"Position\" pour être active.

-    **Circle**: Si trois points sont sélectionnés, le bouton **Circle** est activé et un cercle pourra être créé, il pourra servir de base pour un ressort.

![](images/Macro_FCSpring_Helix_Variable_02_1.png ) 

#### Position (0)(xx) 

(0)(xx) : Nombre de sélection(s), longueur de l\'axe en mm x 10, est égal au nombres de points de déplacements disponibles sur la longueur de l\'axe (pas de 0.1 mm)

-    **Begin/End**: Positionnement du ressort au début, au milieu ou à la fin de l\'axe

-    **Reverse Spr.**: Inverse le ressort sur son axe

-    {{SpinBox|0,1 mm}}: Déplace le ressort de manière précise le long du ressort par pas de 0.1 mm le long de son axe

-    **Reverse Count.**: Inverse le compteur, par exemple: Begin 0 to 10.. ou End 0 to 10..

-   **Slider** : Positionne le ressort sur son axe

![](images/Macro_FCSpring_Helix_Variable_02_2.png ) 

#### Dimensions particulières du ressort 

-    {{SpinBox|Num: 2}}**Numbering of coil** : Numéro de la spire a modifier. (Defaut : 0)

-    {{CheckBox|Smoothing}}**Smoothing** Cette case à cocher découvre un spinBox pour déterminer le degré de lissage entre deux spires ou l\'écartement est important, le degré maximum du lissage est la valeur de précision -1 (cette option est à l\'état de prototype et le résultat peur être satisfaisant, invisible ou mauvais)

-    {{SpinBox|0,000 mm}}**Pitch of coil** : Dimension du pas de la spire a modifier. (Defaut : 0)

-    **15.0 mm**: Si le bouton est cliqué, la valeur de \"Pitch of string\" est affectée à \"Pitch of coil\" (Cette valeur est automatiquement alignée à la valeur de Pitch of string)

-    {{SpinBox|0,000 mm}}**Radius of coil** : Rayon de la spire a modifier. (Defaut : 0)

-    **20.0 mm**: Si le bouton est cliqué, la valeur de \"Radius of string\" est affectée à \"Radius of coil\" (Cette valeur est automatiquement alignée à la valeur de Radius of string)

-    **<img src="images/FCSpring_Helix_Variable_Icon_01.png" width=16px> Accept the value modified**: Bouton d\'acceptation pour valider les modifications de la spire a modifier.

-   **Text edit** : Cette fenêtre affiche les spires modifiées et validées.

-    **Clear**: Nettoie l\'éditeur de texte

-    **Zoom**: Bouton \"Zoom\", agrandit la fenêtre text-edit

![](images/Macro_FCSpring_Helix_Variable_04.png ) 

#### Commandes

-    **<img src="images/FCSpring_Helix_Variable_Icon_02.png" width=16px> Load**: Le bouton Lead ouvre une boîte de dialogue pour lire un fichier sauvegardé, le fichier porte l\'extension **.FCSpring**.

-    **<img src="images/FCSpring_Helix_Variable_Icon_03.png" width=16px> Save**: Le bouton Save ouvre une boîte de dialogue pour sauver un fichier avec la configuration du ressort modifiée ou non, le fichier porte l\'extension **.FCSpring**.

-    **<img src="images/FCSpring_Helix_Variable_Icon_02b.png" width=16px> Load Coordinates**: Ouvre une boîte de dialogue pour charger un fichier **.FCSpringCoor** (toutes les coordonnées des points constituants le ressort).

-    **<img src="images/FCSpring_Helix_Variable_Icon_03b.png" width=16px> Save Coordinates**: Ouvre une boîte de dialogue pour sauver un fichier **.FCSpringCoor** (toutes les coordonnées des points constituants le ressort).

-    **<img src="images/FCSpring_Helix_Variable_Icon_04.png" width=16px> Quit**: Quitte la macro.

-    **<img src="images/FCSpring_Helix_Variable_Icon_05.png" width=16px> Reset**: Reset la macro à la configuration par défaut.

-    **<img src="images/FCSpring_Helix_Variable_Icon_06.png" width=16px> Launch**: Lance la macro et crée le ressort dans sa configuration.

-    **Help**: Ce bouton affiche la page wiki dans la fenêtre web de FreeCAD

![](images/Macro_FCSpring_Helix_Variable_05.png ) 

## Vue rapport 

La fenêtre Vue rapport affiche les détails de la configuration du ressort.

![](images/Macro_FCSpring_Helix_Variable_06.png ) 

## Exemple de ressort 

Exemple de ressort modifié:

![](images/Macro_FCSpring_Helix_Variable_07.png ) 

## Exemple de vue rapport 

Dès que la macro est lancée, la liste de la configuration du ressort est affichée sous forme de tableau.

Ici les données du ressort affichées dans la vue rapport. ![](images/Macro_FCSpring_Helix_Variable_08.png ) 

## Icônes

Téléchargez les icônes et copier les dans votre répertoire de macro.

Cliquez sur l\'image, dans la nouvelle fenêtre positionnez votre souris sur l\'icône, clique droit et faites \"Save target as \...\"

Bouton pour votre barre d\'outils ![Bouton](images/FCSpring_Helix_Variable.png )  Icônes de la Macro

![](images/FCSpring_Helix_Variable_Icon_01.png ) ![](images/FCSpring_Helix_Variable_Icon_02.png ) ![](images/FCSpring_Helix_Variable_Icon_02b.png ) ![](images/FCSpring_Helix_Variable_Icon_03.png ) ![](images/FCSpring_Helix_Variable_Icon_03b.png ) ![](images/FCSpring_Helix_Variable_Icon_04.png ) ![](images/FCSpring_Helix_Variable_Icon_05.png ) ![](images/FCSpring_Helix_Variable_Icon_06.png ) 

## Script

**Macro\_FCSpring\_Helix\_Variable.FCMacro**

Téléchargez la macro sur Gist [Macro\_FCSpring\_Helix\_Variable](https://gist.github.com/mario52a/68c81c32a0727a693d3a)

## Installation

Le fichier ci-dessus est une macro sous la forme de code GitHub. Téléchargez le fichier Zip depuis GitHub, puis suivez les instructions d\'installation des macros pour débutants indiquées à l\'adresse [installing FreeCAD macros in Ubuntu](https://wiki.opensourceecology.org/wiki/Installing_Macros_in_FreeCAD)

## Exemples


<center>

<File:Valves> Assembly IN EX.png\| Valves Assembly IN EX avec la permission de et créée par r.tec voir [Inlet & Exhaust Valves Assembly](http://forum.freecadweb.org/viewtopic.php?f=24&t=14183) et [Spiralfeder](http://forum.freecadweb.org/viewtopic.php?f=13&t=14143) merci r.tec


</center>



<center>

<File:Macro> FCSpring Helix Variable 12.png\| <File:Macro> FCSpring Helix Variable 13.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 14.png\| <File:Macro> FCSpring Helix Variable 15.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 16.png\| <File:Macro> FCSpring Helix Variable 17.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 18.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 19.png\|Différence entre le ressort lissé (ici 71 avec précision 5 (72 points)) et le ressort sans lissage


</center>



<center>

<File:Macro> FCSpring Helix Variable.gif\|Exemple


</center>



<center>

<File:Macro> FCSpringHelixVariable Example 02.gif\|Exemple pour créeer un ressort conique


</center>



<center>

<File:Macro_FCSpringHelixVariable_Spring_On_Circle.gif%7CExemple> pour créer un ressort sur un cercle [File:Macro\_FCSpringHelixVarable\_Spring\_Along\_Axis.gif\|Déplacement](File:Macro_FCSpringHelixVarable_Spring_Along_Axis.gif%7CDéplacement) le long de l\'axe


</center>


## Liens

Discussion sur le forum [Try to do a Spring](http://forum.freecadweb.org/viewtopic.php?f=3&t=8313&p=68161#p68161)

## Projet

Ressort tronqué

Lissage des spires aux changements des spires : fait

Modification du diamètre à chaque spire au choix : fait

## Versions

2022/03/16 Version 0.18 : ajout scrollBar, possibilité docking Gauche or Droite, restauration du chrono *(time.time())*, mémorise le dernier FilePath


```python
####chrono################
import time
global depart ; depart  = 0.0
global arrivee; arrivee = 0.0
def chrono(switch):    # 0=depart autre=stop
#time.strftime('%X %x %Z')#'15:44:07 12/14/19 Paris, Madrid'
    global depart
    global arrivee
    try:
        if switch == 0:
            depart = time.time()#time.clock()
            App.Console.PrintMessage("Chrono begin   : "+str(time.strftime('%X'))+"\n")
        else:
            arrivee = time.time()#time.clock()
            App.Console.PrintMessage("Chrono end     : "+str(time.strftime('%X'))+"\n")
            parcouru = ((arrivee - depart)/60.0)
            App.Console.PrintError("Time execution : "+str("%.3f" % parcouru)+" min"+"\n\n")
        return parcouru
        FreeCADGui.updateGui()    
    except Exception: None
####chrono################
```

2020/11/12 Version=01.17 : suppression du timer chrono !!

2020/10/18 Ver 00.16b : suppression du test FC 18 line 56, et suppression de timer chrono j\'attends\...

2020/05/01 Ver 00.16: fichier d\'erreur de correction (sauvegarde et chargement) cause la suppression de \"label\_11\_Name\" \...

2020/04/11 Ver 01.15: layout et présentation

2019/05/03 Ver 01.14: compatible FreeCAD 0.19.16523 (Git)

2019/04/08 Ver 01.13: compatible FreeCAD 0.18.16093 (Git) /Python version: 3.6.6 /Qt version: 5.6.2

03/04/2017: ver 01.12: correction bug ligne 2314 add \"global ui\"

11/12/2016: ver 01.11: Ajout de position du ressort sur un objet sélectionné

10/09/2016: ver 01.10: Ajout du Bouton \"Zoom\" pour agrandit la fenêtre textedit

04/09/2016: ver 01.09: ajout de la fonction lissage et sauvegarde/chargement des coordonnées du ressort

16/03/2016: ver 01.08 : correction et ajout \"int()\" à debutAngle et finAngle (dans la section lecture du fichier)

02/03/2016: ver 01.07 : ajout d\'une option reverse spring (sens horaire)

08/02/2016: ver 01.06 : correction du bug angle cause \"modifyAngle = int(file.readline().rstrip(\'\\n\\r\')) \# 9\" modifyAngle est int() pas char

07/01/2015: ver 01.05 : ajout de \"Try \...Except\" (données cône) pour assurer la compatibilité avec les versions précédentes.

07/01/2015: ver 01.04 : ajout de fabrication de ressort conique et modification du chemin (path) sur \"UserAppData\".

07/12/2014 : ver 01.03 : nouvelle version avec rayon de chaque spire modifiable.

17/11/2014: ver 1.02 : nouvelle version avec interface graphique, modification de chaque pas et rayon, sauvegarde et chargement des données sur disque.

10/11/2014 : (23h20) correction de la modification. 
```python
ligne.Placement = App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(App.Vector(0,0,1),angleTr), App.Vector(0,0,0))
``` 10/11/2014 : modification de la ligne 44 : 
```python
        a = FreeCAD.ActiveDocument.Line.Placement=App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(App.Vector(0,0,1),angleTr), App.Vector(0,0,0))
``` en 
```python
        ligne = FreeCAD.ActiveDocument.Line.Placement=App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(App.Vector(0,0,1),angleTr), App.Vector(0,0,0))
``` 6/11/2014 : ajout de \"makeBSpline\" et configuration.

## Limitations

Durant les tests de balayage, certaines erreurs ont été obtenues !


<center>

<File:Macro> FCSpring Helix Variable 20.png\|Pour l\'instant, la macro n\'est pas adaptée au carré, au rectangle\...
Seul le cercle fonctionne bien


</center>



<center>

<File:Macro> FCSpring Helix Variable 09.png\|VIOLATION D\'ACCÈS <File:Macro> FCSpring Helix Variable 10.png\|TCollection\_IndexedDataMap


</center>



<center>

<File:Macro> FCSpring Helix Variable 11.png\|Utilisation incorrecte des sections ponctuelles


</center>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCSpring Helix Variable/fr
