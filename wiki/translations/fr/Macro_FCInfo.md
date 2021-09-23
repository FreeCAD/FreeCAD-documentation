# Macro FCInfo/fr
{{Macro/fr
|Icon=FCInfo.png
|Name=Macro FCInfo
|Description=Donne une série d'informations sur la forme.<br />Version française[https://gist.githubusercontent.com/mario52a/6afc64081c4eb8be3b93/raw/c1dd823886fe2e75dc5c6dd490157c259051b651/FCInfo_fr_Ver_1-22-rmu_Docked.FCMacro]
|Author=Mario52
|Version=1.22
|Date=2020/11/12
|FCVersion=Toutes
|Download=Téléchargez le paquet [https://forum.freecadweb.org/download/file.php?id=50755 Macro_FCInfo_Icon.zip] dézipez le et copiez la totalité des fichiers dans votre répertoire des macros
|SeeAlso=<img src=images/Arch_Survey.svg style="width:Arch Survey|24px"> [Arch Prise de cotes](Arch_Survey/fr.md)<br />[Macro SimpleProperties](Macro_SimpleProperties/fr.md)
}}

## Description

Donne une série de renseignements sur la forme sélectionnée et peut afficher une conversion de la longueur, de l\'inclinaison de la forme (degrés, radian, grade, pourcent), de la surface, du volume et du poids de la forme dans la densité sélectionnée dans différentes unités de grandeurs internationales et anglo-saxonnes.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/4ff055ff5eb117f75beea5843efca4791990cf62/FCInfo_en_Ver_1-22-rmu_Docked.FCMacro}}

<img alt="FCInfo" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*

## Utilisation

Sélectionnez un objet ou lancez l\'application et sélectionnez un objet, et une série de renseignements s\'affichent. Les calculs son basés sur l\'unité de FreeCAD, qui est le **mm** à chaque nouvelle sélection, l\'unité de longueur revient toujours sur **mm** et angle sur **degrés décimal**.

<img alt="upper window" src=images/Macro_FCInfo_06.png  style="width:200px;"><img alt="lower window" src=images/Macro_FCInfo_07.png  style="width:200px;">




**Secteur 1: Document**

-   Nom du document courant
-   Label de l\'objet
-   Nom interne de l\'objet
-   Sub élément, nom du sous élément
-   Le type d\'objet

**Secteur 2: Coordinates click mouse**

-   Coordonnées X,Y et Z à l\'endroit du clic de souris
-   Le bouton crée sur le point, l'axe, le plan, copie la forme de l'axe vectoriel **FreeCAD.Vector (-24.0, 240.0, 7.0)**

**Secteur 3: Value**

-   Longueur de l\'objet, si l\'objet est une face le périmètre de la face est affiché

-    **mm**boite déroulante permet de choisir l\'unité de longueur voulue, sont disponibles : km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique. Si un cercle est détecté une deuxième boîte de dialogue s\'ouvre et affiche le rayon du cercle. Si l\'objet est un cercle une seconde lineEdit est ouverte et affiche le rayon du cercle.

-   Périmètre du shape

**Secteur 4: Vertexes et détails**

-   CheckBox case à cocher qui permet d\'activer la recherche complète de tous les éléments de l\'objet sélectionné. Cette option a été introduite pour diminuer le temps de recherche des éléments surtout pour les objets très compliqués. Si décochée (par défaut) seul les éléments principaux de l\'objet seront recherchés et affichés.
-   Vertexes et détails du shape (compt\_Edge), (compt\_Faces), (compt\_Vector of the Face)
    max 200 éléments seront affichés dans la table, s\'il y a plus de 200 éléments, (!+ 200) s\'affiche et le nombre total d\'éléments de la forme
    (le détail de tous les éléments est sauvé dans un fichier au format CSV en cliquant sur le bouton **Enregistrer**.
    Le fichier peut être lu en cliquant sur le bouton **Lecture** ou avec un tableur externe comme [LibreOffice](https://www.libreoffice.org/) [OpenOffice](http://openoffice.apache.org/downloads.html) ou celui de votre choix)

**Secteur 5: Inclinaison**

-   Inclinaison de l\'objet est affiché dans les formats suivants :
-   **Degrés décimal**, ex : 174.831872611°
-   **Degrés minutes secondes**, ex: 174° 49\' 54.741401\'\'
-   **Radians**, ex: 3.05139181449 rad
-   **Grades**, ex: 194.257636235 gon
-   **Pourcent** ex: 30° = 57.74%
-   Inclinaison des plans XY, YZ, ZX et leurs coordonnées correspondantes
-   \'\'\'Direction Objet\" , donne la direction de l\'objet. La direction est calculée : direction = (ou inverse , coord\_2 - coord\_1 )
    -   
        **Line**
        
        , crée une ligne dans la direction de l\'objet (ex: 0,0,0 direction obtenue)
-   **ValueAt** , donne la direction valueAt du vecteur correspondant

**Secteur 6: Surface et volume**

-   Surface de la forme sélectionnée dans l\'unité choisie
-   Surface de la face sélectionnée dans l\'unité choisie
-   Volume de la forme sélectionnée dans l\'unité choisie
-   Densité du matériau utilisé en **kg par dm3**
    (Le \"spinBox\" est réglé sur **1,0** kg).
-   La boîte déroulante **Gramme** permet de choisir l\'unité de masse disponible:
    tonne, quintal, kg, hg, dag, **gramme**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
    lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
-   Le poids de la forme est affiché dans l\'unité de masse sélectionné

**Secteur 7: BoundBox** Le BoundBox est le volume occupé de l\'objet dans l\'espace, ce volume délimité par les coordonnées extérieures maximales dans les axes XYZ

**Secteur 8: Centre du:**

-   Centre du shape avec ses coordonnées XYZ
-   Center massique de la forme avec ses coordonnées XYZ
-   Le **bouton** crée un point, axes, plans, copie du repère vectoriel sous la forme **FreeCAD.Vector(-24.0, 240.0, 7.0)**

**Secteur 9: Inertie**

-   Moment d\'inertie et ses coordonnées (longueur et masse)
-   Le **bouton** crée un point, axes, plans, copie du vecteur sous la forme **FreeCAD.Vector(-24.0, 240.0, 7.0)**
    -   action line 1 : x1, y1, z1
    -   action line 2 : x2, y2, z2
    -   action line 3 : x3, y3, z3
    -   action 4 diagonal : x1, y2, z3

(même commande pour inertie massique)

-   Déterminant 1 : calcule le déterminant de la matrice en notation scientifique
-   Déterminant 2 : même valeur en notation décimale

**Section 10: SpreadSheet**

-    **Lire**: Ouvre un fichier **.FCInfo**, csv, asc, txt

-    **Sauve**: Sauve les données dans un fichier **.FCInfo** , csv, asc, txt

-    **Tabulation**: Le séparateur est une tabulation.

-    **Virgule**: Le séparateur est une virgule

-    **Point V.**: Le séparateur est un point virgule

-    **Espace**: Le séparateur est un espace

Cette option permet de sauver le tableur avec différents séparateurs, Tabulation, Virgule, Point virgule, Espace
La tabulation est le séparateur par défaut du module spreadSheet de FreeCAD.
Le nombre de séparateurs est affiché à l\'ouverture du fichier et permet \"éventuellement\" de déterminer le séparateur utilisé dans le fichier.
La virgule était le séparateur utilisé dans les anciennes versions de FCInfo (1.16 et avant)
Maintenant depuis la version 1.17 le séparateur utilisé par défaut est la tabulation
Si vous voulez convertir vos anciens fichiers .FCinfo : cochez l\'option virgule ouvrez le fichier dans FCInfo et sauvez le avec l\'option Tabulation cochée.

**Section 11: Main**

-    **CheckBox Copie**: si la case est cochée les coordonnées sont copiées en mémoire dans la format : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    **CheckBox Point**: si la case est cochée un point est créé aux coordonnées affichées.

-    **CheckBox Axes **: si la case est cochée une série d\'axes dans les plans XYZ sont créés aux coordonnés affichées.

-    **CheckBox Plan**: si la case est cochée une série de plans dans les plans XYZ sont créés aux coordonnés affichées.

-    **Ref**: Rafraîchi les données dans la macro.

-    **Exit**: Quitte la macro (la macro reste en mémoire vous pouvez la redémarrer par votre bouton ou par le menu \"Affichage → Panneaux → FCInfo\"

-    **CheckBox****1** : Si cette case est cochée les informations sont affichées dans la vue rapport.

-    **CheckBox****2** : Si cette case est cochée la fenêtre de la macro est placée à gauche de l\'écran sinon elle se placera à droite de l\'écran (option par défaut).

Une fois la macro lancée, la macro reste active et la fenêtre reste visible. Il faut quitter la macro par la touche **Quitter**. Si vous quittez par la petite croix, la fenêtre disparaît et la macro reste en mémoire, les données continuent de s\'afficher dans la *vue rapport* de FreeCAD.


<center>

Image:Macro\_FCInfo\_04.png\|Dockée à droite, Image:Macro FCInfo 05.png\|ou à gauche avec la Vue combinée et peut être appelé avec un onglet ou peut être volante au choix.


</center>



## Options

### Les unités utilisées 

#### Longueur :

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

#### Degrés d\'angle : 

1.  **degré décimal**, ex: 174.831872611°
2.  degré minute seconde, ex: 174° 49\' 54.741401\'\'
3.  radian, ex: 3.05139181449 rad
4.  grade, ex: 194.257636235 gon
5.  pourcent, ex: 30° = 57.74%

Compréhension de l\'affichage des angles dans FCInfo.


<center>

Image:Macro FCInfo 02.png\|Compréhension de l\'affichage des angles dans FCInfo Image:Macro FCInfo 03.gif\|Compréhension de l\'affichage des angles en pourcentage dans FCInfo
Cliquez deux fois sur l\'image pour voir l\'animation (l\'image doit être en plein écran)


</center>




#### Unités de masse : 

ton, quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
Le \"spinBox\" de densité est réglé sur 7,5 kg, densité moyenne de l\'acier. Si vous désirez mettre une autre valeur par défaut, modifiez la valeur de la densité ,ligne 208


```python
 global densite       ; densite       = 7.5  # (steel = 7.5 kg par dm3)
```

Un fichier peut être créé par le bouton **Enregistrer**. Le fichier est écrit comme un fichier [csv](https://fr.wikipedia.org/wiki/Comma-separated_values) de cette manière, les données peuvent être étudiées dans un tableur dans FreeCAD ou [OpenOffice](http://www.openoffice.org/fr/), [LibreOffice](https://fr.libreoffice.org/) \...

## Script

Copiez le contenu de la macro dans un fichier nommé \"FCInfo.FCMacro\"

-   Windows: habituellement **\" drive:\\Users\\your\_user\_name\\AppData\\Roaming\\FreeCAD\\ \"**.
-   Ubuntu : habituellement **\" /home/your\_user\_name/.FreeCAD \"**.

Ou, directement dans l\'interface de FreeCAD.
Les icônes doivent se trouver dans le même répertoire que la macro.
Télécharger les images en vous positionnant sur les icônes <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> puis faites clic droit de la souris \"Enregistrer l\'image sous\"(ne pas modifier le nom)
\'\'\'PS: trop long pour être contenu dans la page du wiki (pour le moment les pages du wiki n\'acceptent que 64 ko) le code de la macro a été placé dans le forum \'\'\'


<div class="toccolours mw-collapsible mw-collapsed">

Il y a aussi une version seulement FCInfo\_Alternate\_Linux pour la version FreeCAD 0.13\... et PyQt4


<div class="mw-collapsible-content">

Il y a aussi une version [Macro\_FCInfo\_Alternate\_Linux](http://www.freecadweb.org/wiki/index.php?title=Macro_FCInfo_Alternate_Linux) ici le code est modifié (à cause de l\'erreur d\'affichage des caractères : ² ³ ° µ\" ordinal not in range (128)\") qui posaient problèmes dans certaines configurations les fonctions sont les mêmes
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
``` Les fichiers sauvé avec cette version sont incompatibles avec les autres version (à cause de l\'encodage différent)


</div>


</div>

Téléchargez le fichier des icônes de FCInfo [Macro\_FCInfo\_Icon](https://forum.freecadweb.org/download/file.php?id=50755) décompressez le fichier et copiez les images dans la même répertoire que la macro.

Téléchargez le fichier FCInfo **docké à droite**


{{CodeDownload|https://gist.github.com/mario52a/6afc64081c4eb8be3b93|Dernière version de Macro_FCInfo (les icônes sont à la fin de la page)}}

(Ou **[sur le forum.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)** )
**PS:** Cette macro utilise la fonction **getSelection()** et la liste des objets commence à 1 ex: pour un cube **Edge1 jusque Edge12** (arêtes) et le code qui liste les arêtes dans la console Python commence à 0 ex: pour un cube **Edge\[0\] jusque Edge\[11\]**
Cette différence est tout à fait normale le compteur de la liste/tableau dans OpenCascade commence toujours à **1 et pas à 0**

### Limitations

Toujours utiliser le bouton **Quitter**. Si vous quittez le programme sans passer par le bouton **Quitter**, le programme reste en mémoire et continue à s\'exécuter et l\'affichage continue dans le \"rapport de visualisation\". Vous devez quitter FreeCAD pour l'effacer de la mémoire.
Seuls les 200 premiers éléments de l'objet sont visibles dans le tableau, s'il y a plus de 200 éléments dans l'objet un signal sera affiché par \"\'(! +200)\'\". La liste complète des données est visible dans le fichier sauvegardé par le bouton **Enregistrer**.
Si la fenêtre de la macro n\'est pas visible au lancement, regardez en bas de la fenêtre :

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 

en projet :

~~lecture du fichier directement dans un tableau.~~ fait

~~correspondances des \"Edges\" et de leurs coordonnées~~ fait

association d\'une substance à sa masse volumique

~~inclinaison sur l\'élément plutôt que sur l\'objet global~~ fait

~~incrustation à droite dans l\'interface de FreeCAD~~ fait

## Version

-   ver 1.22 , 12/11/2020 : maintenant la macro est totalement désinstallée en utilisant :


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
``` et j\'ajoute la possibilité d\'afficher ou non la fenêtre \"Error Message\" \"Faux\" par défaut, si vous voulez activer la fenêtre d\'avertissement aller à: 
```python
FreeCAD >Menu >Tools >Edit parameters... >BaseApp/Preferences/Macros/FCMmacros/FCInfo > switchWarning
``` actuellement :

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

Voir aussi [Arch Prise de cotes](Arch_Survey/fr.md) <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width:36px;">

Vous pouvez faire part de vos commentaires sur le forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Ici un autre post traitant de [FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)

---
[documentation index](../README.md) > Macro FCInfo/fr
