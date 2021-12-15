# Macro FCInfo/fr
<div class="mw-translate-fuzzy">


{{Macro/fr
|Icon=FCInfo.png
|Name=Macro FCInfo
|Description=Donne des informations sur la forme sélectionnée et peut afficher une conversion de la longueur, de l'inclinaison (degrés, radians, grades, pourcentage), de la surface, du volume et du poids dans différentes unités (métriques et impériales). La macro fonctionne désormais aussi pour les éléments d'une esquisse en mode édition.
<br />[https://gist.githubusercontent.com/mario52a/6afc64081c4eb8be3b93/raw/4241a47fa69648e0bea0482fa1e6cfb2ac5f4858/FCInfo_fr_Ver_1-25-rmu_Docked.FCMacro Version française]
|Author=Mario52
|Version=1.25b
|Date=2021/12/11
|FCVersion=Toutes
|SeeAlso=<img src=images/Arch_Survey.svg style="width:Arch Survey|24px"> [Arch Prise de cotes](Arch_Survey/fr.md)<br />[Macro SimpleProperties](Macro_SimpleProperties/fr.md)
}}


</div>

## Description

Donne des informations sur la forme sélectionnée et peut afficher une conversion de la longueur, de l\'inclinaison (degrés, radians, grades, pourcentage), de la surface, du volume et du poids dans différentes unités (métriques et impériales). La macro fonctionne désormais aussi pour les éléments d\'une esquisse en mode édition.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/4ecf1b82162b7a9e600c9ee511410ddf06c6e534/FCInfo_en_Ver_1-25d-rmu_Docked.FCMacro}}

<img alt="FCInfo" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*

## Utilisation

Sélectionnez un objet ou lancez l\'application et sélectionnez un objet. Une série de renseignements s\'affichent. Les calculs sont basés sur l\'unité de FreeCAD, qui est le **mm** à chaque nouvelle sélection, l\'unité de longueur revient toujours sur **mm** et angle sur **degrés décimal**. <img alt="fenêtre supérieure" src=images/Macro_FCInfo_06.png  style="width:200px;"><img alt="fenêtre inférieure" src=images/Macro_FCInfo_07.png  style="width:200px;">




**Secteur 1: Document**

-   Nom du document courant
-   Label de l\'objet
-   Nom interne de l\'objet
-   Sub élément, nom du sous élément
-   Le type d\'objet

**Secteur 2: Coordinates click mouse**

-   Coordonnées X,Y et Z à l\'endroit du clic de souris
-   Le bouton crée sur le point, l'axe, le plan, copie la forme de l'axe vectoriel à partir de **FreeCAD.Vector (-24.0, 240.0, 7.0)**

**Secteur 3: Value**

-   Si l\'objet est un périmètre de face, la longueur de l\'objet est affichée. La taille de l\'unité peut être sélectionnée :
    km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.
-   Si l\'objet est un cercle, une deuxième ligne s\'affiche et donne le rayon du cercle.
-   Périmètre de la forme.

**Secteur 4: Vertexes and details**

-   Case à cocher pour la recherche ou non de tous les détails de l\'objet. Si elle n\'est pas cochée, seule la valeur principale est affichée.
-   Sommets et détails de la forme (compt\_Edge), (compt\_Faces), (compt\_Vector of the Face)
    max 200 lignes dans le tableau, s\'il y a plus de 200 lignes, il apparaîtra (!+ 200) et le nombre de lignes
    (les détails complets peuvent être sauvegardés par le bouton **Save** dans un fichier au format CSV et peuvent être visualisés dans le tableur avec le bouton **Read** ou par un tableur externe comme [LibreOffice](https://www.libreoffice.org/) [OpenOffice](http://openoffice.apache.org/downloads.html) ou autre).

**Secteur 5: Inclination**

-   *\' Inclinaison de l\'objet*\' est affiché dans les formats suivants :
    -   Degrés décimal, ex : 174.831872611°
    -   Degrés minutes secondes, ex: 174° 49\' 54.741401\'\'
    -   Radians, ex: 3.05139181449 rad
    -   Grades, ex: 194.257636235 gon
    -   Pourcent, ex: 30° = 57.74%
-   **Inclinaison des plans XY, YZ, ZX** et leurs coordonnées correspondantes
-   **Direction object**, donne la direction de l\'objet. Le calcul est : coord\_1 - coord\_2 = direction (ou l\'inverse)
    -   
        **Line**
        
        , ce bouton crée une ligne dans la direction de l\'objet.
-   **ValueAt** , renvoie le vecteur 3D correspondant à une valeur de paramètre.

**Secteur 6: Surface and Volume**

-   Surface de la forme affichée, la taille de l\'unité peut être sélectionnée
-   Surface de la face affichée, la taille de l\'unité peut être sélectionnée.
-   Volume de la forme affichée, la taille de l\'unité peut être sélectionnée.
-   Densité du matériau en **kg par dm3**
    (la \"spinBox\" est réglé sur **7,5** kg, densité moyenne de l\'acier. Si vous souhaitez une autre valeur par défaut, modifiez la valeur de la densité, ligne 204).
-   L\'unité de masse **gram** peut être choisie :
    ton,quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
    lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
-   Poids de la forme affichée, l\'unité de masse peut être sélectionnée.

**Secteur 7: BoundBox**

-   BoundBox donne les dimensions limites de la forme.

**Secteur 8: Center of:**

-   Centre du shape avec ses coordonnées XYZ
-   Center massique de la forme avec ses coordonnées XYZ
-   Le bouton crée sur le point, l\'axe, le plan, la copie de l\'axe du vecteur forme **FreeCAD.Vector(-24.0, 240.0, 7.0)**.

**Secteur 9: Inertia**

-   Moment d\'inertie et ces coordonnées longueur et poids
-   Le bouton crée sur point, axe, plan, copier vecteur axe forme **FreeCAD.Vector(-24.0, 240.0, 7.0)**.
    -   ligne d\'action 1 : x1, y1, z1
    -   Ligne d\'action 2 : x2, y2, z2
    -   action ligne 3 : x3, y3, z3
    -   action 4 diagonale : x1, y2, z3

même chose pour la longueur et le poids

-   Déterminant 1 : calcule le déterminant de la matrice, en [valeur scientifique](https://fr.wikipedia.org/wiki/Notation_scientifique)
-   Déterminant 2 : calcule le déterminant de la matrice, en valeur décimale

**Section 10: SpreadSheet**

-    **Read**: lire les données dans un tableur enregistré *.FCInfo* ou txt, asc, csv

-    **Save**: enregistrer les données sur disque sous la forme choisie ci-dessous *.FCInfo* ou txt, asc, csv

-    **Tabulation**: le séparateur est Tabulation

-    **Comma**: le séparateur est Virgule

-    **Semicolon**: le séparateur est le point-virgule.

-    **Space**: le séparateur est Espace

Option pour sauvegarder ou lire la feuille de calcul avec différents séparateurs, Tabulation, Virgule, Point-virgule, Espace
. La tabulation est le séparateur pour l\'\[Spreadsheet\_Workbench/fr\|atelier Spreadsheet\] de FreeCAD
Les numéros de ces quatre séparateurs sont calculés pour aider en cas d\'inconnu
Les VIRGULES sont les anciens séparateurs de la macro FCInfo (01.16 et avant)
Maintenant pour la compatibilité avec le tableur FreeCAD et depuis la version 01.17, la TABULATION est le séparateur par défaut
Si vous voulez convertir votre ancienne feuille de calcul FCInfo : ouvrez-la dans FCInfo et enregistrez-la avec l\'option Tabulation cochée.

**Section 11: Main**

-    **CheckBox Clip Board**: si la case est cochée les coordonnées sont copiées en mémoire dans la format : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    **CheckBox Point**: si la case est cochée un point est créé aux coordonnées affichées.

-    **CheckBox Axis **: si la case est cochée une série d\'axes dans les plans XYZ sont créés aux coordonnés affichées.

-    **CheckBox Plane**: si la case est cochée une série de plans dans les plans XYZ sont créés aux coordonnés affichées.

-    **Ref**: rafraîchi les données dans la macro.

-    **Exit**: quitte la macro (la macro reste en mémoire vous pouvez la redémarrer par votre bouton ou par le menu \"Affichage → Panneaux → FCInfo\"

-    **CheckBox****1** : si cette case est cochée les informations sont affichées dans la vue rapport.

-    **CheckBox****2** : Si cette case est cochée la fenêtre de la macro est placée à gauche de l\'écran sinon elle se placera à droite de l\'écran (option par défaut).

Une fois la macro lancée, la macro reste active et la fenêtre reste visible. Il faut quitter la macro par la touche **Quitter**. Si vous quittez par la petite croix, la fenêtre disparaît et la macro reste en mémoire, les données continuent de s\'afficher dans la *vue rapport* de FreeCAD.


<center>

Image:Macro\_FCInfo\_04.png\|Dockée à droite, Image:Macro FCInfo 05.png\|ou à gauche avec la Vue combinée et accessible par un onglet, ou non ancré, au choix.


</center>




## Options

### Les unités utilisées 

#### Unités de longueur : 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

#### Unités d\'angle : 

1.  **degré décimal**, ex: 174.831872611°
2.  degré minute seconde, ex: 174° 49\' 54.741401\'\'
3.  radian, ex: 3.05139181449 rad
4.  grade, ex: 194.257636235 gon ou gr
5.  pourcent, ex: 30° = 57.74%

Compréhension de l\'affichage des angles dans FCInfo.


<center>

Image:Macro FCInfo 02.png\|Compréhension de l\'affichage des angles dans FCInfo Image:Macro FCInfo 03.gif\|Compréhension de l\'affichage des angles en pourcentage dans FCInfo
Cliquez deux fois sur l\'image pour voir l\'animation (l\'image doit être en plein écran)


</center>




#### Unités de masse : 

ton, quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
La \"spinBox\" de densité est réglé sur 7,5 kg, densité moyenne de l\'acier. Si vous désirez mettre une autre valeur par défaut, modifiez la valeur de la densité ,ligne 208.


```python
 global densite       ; densite       = 7.5  # (steel = 7.5 kg par dm3)
```

Un fichier peut être créé par le bouton **Enregistrer**. Le fichier est écrit comme un fichier [csv](https://fr.wikipedia.org/wiki/Comma-separated_values) de cette manière, les données peuvent être étudiées dans un tableur dans FreeCAD ou [OpenOffice](http://www.openoffice.org/fr/), [LibreOffice](https://fr.libreoffice.org/)\...

## Script

Copiez le contenu de la macro dans un fichier nommé \"FCInfo.FCMacro\"

-   Windows: habituellement **\" drive:\\Users\\your\_user\_name\\AppData\\Roaming\\FreeCAD\\ \"**.
-   Ubuntu : habituellement **\" /home/your\_user\_name/.FreeCAD \"**.

Ou, directement dans l\'interface de FreeCAD.
Les icônes doivent se trouver dans le même répertoire que la macro.
Télécharger les images en vous positionnant sur les icônes <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> puis faites clic droit de la souris \"Enregistrer l\'image sous\"(ne pas modifier le nom)
**PS: le code est trop long pour être contenu dans la page du wiki (pour le moment les pages du wiki n\'acceptent que 64 KB). Le code de la macro a été placé dans le forum**


<div class="toccolours mw-collapsible mw-collapsed">

Il y a aussi une version seulement FCInfo\_Alternate\_Linux pour la version FreeCAD 0.13\... et PyQt4


<div class="mw-collapsible-content">

Il y a aussi une version [Macro\_FCInfo\_Alternate\_Linux](http://www.freecadweb.org/wiki/index.php?title=Macro_FCInfo_Alternate_Linux). Ici le code est modifié (à cause de l\'erreur d\'affichage des caractères : ² ³ ° µ\" ordinal not in range (128)\") qui posaient problèmes. Dans certaines configurations les fonctions sont les mêmes
Exemple : 
```python
global uniteSs       ; uniteSs       = u"mm²"
global uniteVs       ; uniteVs       = u"mm³"
global uniteAs       ; uniteAs       = u"°"
</syntaxhighlight>
remplacés par
<syntaxhighlight>
global uniteSs       ; uniteSs       = "mm"+iso8859(unichr(178))
global uniteVs       ; uniteVs       = "mm"+iso8859(unichr(179))
global uniteAs       ; uniteAs       = iso8859(unichr(176))
``` **Les fichiers sauvegardés avec cette version sont incompatibles avec l\'autre version (docké ou non)**.


</div>


</div>

Téléchargez le fichier des icônes de FCInfo [Macro\_FCInfo\_Icon](https://forum.freecadweb.org/download/file.php?id=50755) décompressez le fichier et copiez les images dans le même répertoire que la macro.

Téléchargez le fichier FCInfo **docké à droite**


{{CodeDownload|https://gist.github.com/mario52a/6afc64081c4eb8be3b93|Dernière version de Macro_FCInfo (les icônes sont à la fin de la page)}}

(Ou **[sur le forum.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)** )
**PS:** Cette macro utilise la fonction **getSelection()** et la liste des objets commence à 1 ex: pour un cube **Edge1 à Edge12** (arêtes) et le code qui liste les arêtes dans la console Python commence à 0 ex: pour un cube **Edge\[0\] à Edge\[11\]**
Cette différence est tout à fait normale, le compteur de la liste/tableau dans OpenCascade commence toujours à **1 et pas à 0**.

### Limitations

Toujours utiliser le bouton **Quitter**. Si vous quittez le programme sans passer par le bouton **Quitter**, le programme reste en mémoire et continue à s\'exécuter et l\'affichage continue dans le \"rapport de visualisation\". Vous devez quitter FreeCAD pour l'effacer de la mémoire.
Seuls les 200 premiers éléments de l'objet sont visibles dans le tableau. Si il y a plus de 200 éléments dans l'objet, un signal sera affiché par **(! +200)**. La liste complète des données est visible dans le fichier sauvegardé par le bouton **Enregistrer**.
Si la fenêtre de la macro n\'est pas visible au lancement, regardez en bas de la fenêtre :

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 

en projet :
~~lecture du fichier directement dans un tableau.~~ fait
~~correspondances des \"Edges\" et de leurs coordonnées~~ fait
~~association d\'une substance à sa masse volumique~~
~~inclinaison sur l\'élément plutôt que sur l\'objet global~~ fait
~~incrustation à droite dans l\'interface de FreeCAD~~ fait

## Version


<div class="mw-translate-fuzzy">

-   ver 1.25b 11/12/2021 correction d\'une erreur dans le changement/modification de nouveaux matériaux et réorganisation
-   ver 1.25 10/12/2021 PySide2 et ajout de la boîte combo pour matériaux
-   ver 1.24 02/12/2021 ajout [adjustedGlobalPlacement](https://forum.freecadweb.org/viewtopic.php?f=22&t=59852) modifié par edwilliams16 pour le placement avec un Corps, traçage de la boîte à outils
-   ver 1.23cb 25/11/2021 suppression de **\"import Sketcher \* \"** qui créait un conflit avec \"**open(OpenName, \"r\")**\" ??

Ajout


</div>


```python
FreeCAD.ActiveDocument.openTransaction(u"FCInfo")    # memorise les actions (avec annuler restore)
FreeCAD.ActiveDocument.commitTransaction()           # restore les actions  (avec annuler restore)
#FreeCAD.ActiveDocument.abortTransaction()            # abandonne les actions(avec annuler restore)
```


<div class="mw-translate-fuzzy">

-   ver 1.23b, 20/11/2021 petite correction, ajout de l\'info texte au début de la macro et ordonner le code texte.
-   ver 1.23 , 19/11/2021 inclut l\'icône dans la macro, le nombre de décimales affichées, la hauteur du texte, configure les options dans les Préférences de Freecad, corrige les infos pour les éléments de l\'esquisse en mode édition.
-   ver 1.22 , 12/11/2020 : maintenant la macro est totalement désinstallée en utilisant :


</div>


```python
try:
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)    # destroy
        self.window.deleteLater()                                     # destroy
        self.window.destroy()                                         # destroy
except Exception:
        None
```

[How do i exit from FreeCAD instead of Python?](https://forum.freecadweb.org/viewtopic.php?f=22&t=48013#p411508)

instead: 
```python
self.window.hide()
``` et j\'ai ajouté la possibilité d\'afficher ou non la fenêtre \"Message d\'erreur\" \"Faux\" par défaut, si vous voulez activer la fenêtre d\'avertissement allez à : 
```python
FreeCAD >Menu >Tools >Edit parameters... >BaseApp/Preferences/Macros/FCMmacros/FCInfo > switchWarning
```

-   ver 1.21-3.01 , 07/11/2019 \# 07/11/2019 ver \"01.21-3-rmu\" remplacé caractères micro = \"U\", square = \"2\", cube = \"3\", degrees = \" deg\" see \"<https://forum.freecadweb.org/viewtopic.php?f=3&t=6005&start=70#p345819>\"
-   ver 1.21-2.01 (1.21-rmu) 11/06/2019 rmu remplacé tous les caractères au dessus de 127 in ex: \"°\" en chr(176)) \#degree
-   ver 1.21.01 (1.21-rmu) 30/05/2019 rmu change fixed positions to qt layouts grid.addWidget() by rmu75 see the rmu75 fork \"<https://gist.github.com/rmu75/b165147bd1c2f2659c014103793ae1d8>\"
-   ver 1.21 , 16/04/2019 optimisation pour Py 3\... Qt 5\...
-   ver 1.20 , 29/01/2018 optimisation
-   ver 1.19 , 20/01/2018 mise en place d\'une case à cocher pour activer ou désactiver le module spreadSheet, le module ralenti la macro si l\'objet sélectionné est \"compliqué\". Optimisation.
-   ver 1.18 , 19/12/2017 \....
-   ver 1.17c , 14/12/2017 création de plans avec las mêmes coordonnées d\'un projet dans un autre projet et remplacement de \"FCInfo\" by \"\_\_title\_\_\"
-   ver 1.17b , 13/12/2017 petite correction remplascé FCTreeView to FCInfo
-   ver 1.17 , 12/12/2017 ajout et mise à jour de la section Moment of inertia mm et kg par pinq [FCMacro and moment of inertia of assembly](https://forum.freecadweb.org/viewtopic.php?t=23888), et création de plans, axes, point, et ajout de l\'option sépateur pour le spreadsheet
-   ver 1.16 , 21/06/2017 ajout du contrôle de la hauteur des caractères (here PointSize 8) et checkbox pour la position de la fenêtre à gauche ou à droite
-   ver 1.16 , 21/06/2017 ajout d\'un contrôle sur la hauteur des caractères affichés, ajout d\'une case à cocher pour positionner la macro à gauche ou droite et nouveau code de recherche de chemin de l\'emplacement des macros.
-   ver 1.15 , 19/12/2015 suppression de l\'option PyQt4 [voir la cause](http://forum.freecadweb.org/viewtopic.php?f=12&t=13541) , ajout d\'un checkBox pour éditer ou non les infos dans la vue rapport
-   ver 1.14 , 04/08/2014 PyQt4 et PySide, correction des tooltips qui ne s\'affichaient plus a cause de PySide, ajout de \"fg\" et d\'une décimale dans la densité
-   ver 1.13 , 27/07/2014 remplacement FCInfo\_fr\_Ver\_1-12\_Docked.FCMacro avec FCInfo\_fr\_Ver\_1-13\_Docked.FCMacro accepte PyQt4 et PySide
-   ver 1.12 , 10/03/2014 ajout de tooltips sur les boutons.
-   ver 1.11 , 04/03/2014 ajout de µm, nm, pm, fm, µg, ng, pg, pour-cent, correction de la grandeur carat ~~\"cd\"~~ en **\"ct\"**, affichage du label et du nom interne, correction du calcul des angles XY YZ ZX fonctionnait bien sur un objet simple mais donnait une valeur erronée sur une pièce composée (prenait d\'autres coordonnées ! découvert en comparant le tableau et les coordonnées affichées dans la section Inclinaisons), fenêtre volante ou dockable n\'importe où dans FreeCAD
-   ver 1.10.b, 19/11/2013 boutons à l\'extérieur du scrollbar et blocage des dimensions de la fenêtre
-   ver 1.10 , 18/11/2013 ajout d\'une \"scrollbar\" pour diminuer la dimension de la fenêtre
-   ver 1.08.b 10/11/2013 correction d\'erreur d\'affichage de la surface des faces listées dans le tableau et remplacement des \"**print**\" par \"**App.Console.PrintMessage**\"

~~ver 1.09 , 04/11/2013 fonctionne parfaitement sur Windows et Linux (cause de l\'erreur les caractères : ² ³ ° \" ordinal not in range(128)\")~~

Dans certaines distributions Linux et dans le cas d\'une erreur **\"ordinal not in range (128)\"** une autre version existe sur cette page [Macro\_FCInfo\_Alternate\_Linux](Macro_FCInfo_Alternate_Linux.md)

-   ver 1.08 , 24/10/2013 correction de l\'affichage dans le fichier des \"Faces\" et \"Edges\" haut dessus de 100 objets
-   ver 1.07 , 11/10/2013 correspondance des \"Faces\" et de leurs coordonnées.
-   ver 1.06 , 22/09/2013 correspondances des \"Edges\" et de leurs coordonnées, inclinaison sur l\'élément plutôt que sur l\'objet global
-   ver 1.05 , 17/09/2013 ajout d\'un icône pour le tableur, conversion en tonneau fr, affichage des dimensions hors tout à la place des coordonnées.
-   ver 1.04 , 11/09/2013: lecture du fichier et affichage directement dans un tableau
-   ver 1.03 , 09/09/2013: affichage plus clair dans Vue rapport et remplacement par \"typeObject = sel\[0\].Shape.ShapeType\"
-   ver 1.02 , 7/09/2013 : petites mises au point
-   ver 1.00 , 6/09/2013

## Liens

Voir aussi : <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width:36px;"> [Arch Prise de cotes](Arch_Survey/fr.md)

Vous pouvez faire part de vos commentaires sur le forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Ici un autre post traitant de [FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)

---
[documentation index](../README.md) > Macro FCInfo/fr
