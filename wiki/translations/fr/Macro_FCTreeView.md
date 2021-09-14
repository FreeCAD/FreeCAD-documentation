# Macro FCTreeView/fr

 {{Macro/fr
|Name=Macro FCTreeView
|Icon=Macro_FCTreeView.png
|Description=Cette macro affiche tous les objets du projet dans une liste avec des options de tri avancées.<br/> <br/>Pour la version précédente voir [https://gist.githubusercontent.com/mario52a/67517ef758ff20005d0a6adcfd8c9190/raw/0a92d7f591a0a179f84b2fc417046723b4d7b0e6/Macro_FCTreeView.FCMacro Macro_FCTreeView.FCMacro] et installez la manuellement.
|Author=Mario52
|Version=00.09
|Date=2020-09-24
|FCVersion=0.18 et plus
|Download=[https://forum.freecadweb.org/download/file.php?id=70498 Macro FCTreeView Icon package] dézipez le fichier .zip et copiez les icônes dans votre répertoire de macros.
}}

## Description

Cette macro affiche tous les objets du projet dans une liste avec des options de tri avancées, rcherche par nom, label, type, majuscule \... une option permet de sauver dans un tableur les valeurs ou données au choix relatives à l\'objet avec l\'unité de grandeur sélectionnée, ou sous forme d\'une liste des objets avec différenciation du volume (pour les objets ayants le même label et volumes différents) {{Codeextralink|https://gist.githubusercontent.com/mario52a/67517ef758ff20005d0a6adcfd8c9190/raw/59bc2028978c82744c83c6b138ab3ef30e0bf6f3/Macro_FCTreeView.FCMacro}}

## Comment l\'utiliser 

![Macro FCTreeView](images/FCTreeView.gif ) 

### Section **Window** 

Le titre affiche les options, nombre et type d\'objet(s) affiché

-   **O** = Objects
-   **N** = Name
-   **L** = Label
-   **T** = Total
-   **G** = Group
-   **S** = Single
-   **V** = Visible
-   **H** = Hidden

Si un objet est sélectionné: le placement de base, la rotation et le centre massique est affiché (si disponible!)
![Icône utilisé pour le Nom de l\'objet](images/Macro_FCTreeView_00.png ) Icône utilisé pour le Nom de l\'objet (la barre de défilement est colorée en bleu)

![Icône utilisé pour le Label de l\'objet](images/Macro_FCTreeView_05.png ) Icône utilisé pour le Label de l\'objet (la barre de défilement est colorée en bleu clair)

![Icône utilisé pour visualiser si le statut de l\'objet est Visible (cliquez avec la souris pour caché l\'objet)](images/Macro_FCTreeView_01.png ) (la barre de défilement est colorée en vert)

![Icon used for visualise if the object is status Hidden (mouse click for Visible)](images/Macro_FCTreeView_02.png ) Icône utilisé pour visualiser si le statut de l\'objet est Caché (cliquez avec la souris pour le rendre Visible) (la barre de défilement est colorée en rouge)

![Icon used for the Name contains objects (or folder Group)](images/Macro_FCTreeView_17.png ) Icône utilisé si l\'objet contient des objets (ou est un groupe)

![Icon used for inform the object in a group the number objects is displayed in top group](images/Macro_FCTreeView_03.png ) Icône utilisé pour informer si l\'objet est un groupe, (le nombre d\'objet dans le groupe est affiché entre parenthèses) (la barre de défilement est colorée en rouge clair)

![Icon used for displayed the single object (not group)](images/Macro_FCTreeView_04.png ) Icône utilisé pour un simple objet (pas un groupe)

### Section **Sort by :** 


**<img src=images/Macro_FCTreeView_10.png style="width:18px"> Name**

Icône utilisé pour trier les objet par nom (flip/flop normal/reverse)


**<img src=images/Macro_FCTreeView_11.png style="width:18px"> Label**

Icône utilisé pour lister les objets par label (flip/flop normal/reverse)


**<img src=images/Macro_FCTreeView_12.png style="width:18px"> Visible**

Icône utilisé pour lister les données par Visible/caché (flip/flop normal/reverse)


**<img src=images/Macro_FCTreeView_13.png style="width:18px"> Group**

Icône utilisé pour lister les objets par Groupe/Simple objet (flip/flop normal/reverse)


**<img src=images/Macro_FCTreeView_19.png style="width:18px"> Length**

Si cette case à cocher est activée le tri se fera sur la longueur du nom affiché de la fonction active (Name, Label \...)

### Section **Global** 


**<img src=images/Macro_FCTreeView_21.png style="width:18px"> Split**

flip/flop Sépare le Nom de la liste


**<img src=images/Macro_FCTreeView_22.png style="width:18px"> Split**

flip/flop Sépare le Nom et le Label de la liste


**<img src=images/Macro_FCTreeView_14.png style="width:18px"> Expend**

flip/flop liste les données Fold/Expend


**<img src=images/Macro_FCTreeView_15.png style="width:18px"> Expend**

flip/flop liste les données Expend/Fold


**<img src=images/Macro_FCTreeView_06.png style="width:18px"> Visibility**

flip/flop normal/Visible


**<img src=images/Macro_FCTreeView_07.png style="width:18px"> Group**

flip/flop normal/Groupe


**<img src=images/Macro_FCTreeView_16.png style="width:18px"> Reload**

recharge les objets du projet


**<img src=images/Macro_FCTreeView_18.png style="width:18px"> Original**

retourne à l\'organisation originale après une opération visibility/Hidden


**<img src=images/Macro_FCTreeView_01.png style="width:18px"> All Visible**

visualise si l\'objet est de status Visible


**<img src=images/Macro_FCTreeView_02.png style="width:18px"> All Hidden**

visualise si l\'objet est de statut Hidden

### Section **Search** 


**<img src=images/Macro_FCTreeView_20.png style="width:18px"> Clear**

Efface la ligne de recherche

#### Les radioButton de recherche **Search**: 

-   **(\"NLwc\")** : Recherche par Name et Label **W**ithout sans respecter la **C**ase sensitive

-   **(\"Nsc\")** : Recherche par Name en respectant la **S**ensitive **C**ase

-   **(\"Lwc\")** : Recherche par Label **W**ithout sans respecter la **C**ase sensitive

-   **(\"NLsc\")** : Recherche par Name et Label en respectant la **S**ensitive **C**ase

-   **(\"NLwsc\")** : Recherche par Name et Label dans le mot en respectant la **S**ensitive **C**ase (comme dans le panneau sélection de FreeCAD)

-   **(Nu)** : Search by numeric value (radius, length, angle \.....) voir la version section


**<img src=images/Macro_FCTreeView_23.png style="width:18px"> Select**

flip/flop pour sélectionner tous les objets affichés dans la fenêtre


**<img src=images/Macro_FCTreeView_24.png style="width:18px"> Unselected**

flip/flop désélectionner tous les objets


**<img src=images/Macro_FCTreeView_25.png style="width:18px"> S Sheet**

accès aux options du tableur (Spreadsheet)

### The SpreadSheet options: 

![Macro FCTreeView](images/TreeView_SpeadSheet.gif ) 

![](images/Macro_FCTreeView_001.png )

![](images/Macro_FCTreeView_002.png )

-   Série de cases à cocher pour sélectionner la donnée à introduire dans le tableur


**<img src=images/Macro_FCTreeView_28.png style="width:18px"> Select**

: Active toutes les cases à cocher


**<img src=images/Macro_FCTreeView_29.png style="width:18px"> Select**

: désactive toutes les cases à cocher

![](images/Macro_FCTreeView_003.png )

-   **Value** : seul la valeur est sauvée dans la cellule
    -   Ex : 10.00 ![](images/Macro_FCTreeView_30.png )
-   **Val Gr** : la valeur et son unité sont sauvés dans une unique cellule
    -   Ex : 10.00 mm ![](images/Macro_FCTreeView_31.png )
-   **Val Gr Ph** : la valeur, l\'unité et la donnée physique sont sauvées dans une seule cellule
    -   Ex : 10.00 mm Length ![](images/Macro_FCTreeView_32.png )
-   **Split** : si cette case à cocher est activée, les données valeur, unité et donnée physique sont enregistrées dans des cellules séparées
    -   Ex : 10.00 \| mm \| length ![](images/Macro_FCTreeView_33.png )

![](images/Macro_FCTreeView_004.png )

-   Combobox **mm** : sélectionnez l\'unité désirée. La valeur est convertie dans l\'unité sélectionnée. Les unités disponibles sont:
    -   km, hm, dam, m, dm, cm, **mm**, um, nm, pm, fm, in, lk, ft, yd, rd, ch, fur, mi, lea, nmi
-   Combobox **gram** : sélectionnez l\'unité de poids désirée. La valeur est convertie dans l\'unité sélectionnée. Les unités disponibles sont:
    -   t, q, kg, hg, dag, **g**, dg, cg, mg, µg, ng, pg, fg, gr, dr, oz, oz t, lb, t lb, st, qtr, cwt, tonneau fr, ct
-   Spinbox **Densite** : donnez la densité par dm3 du matériel utilisé (Défaut : 1.0000)
-   Spinbox **Round** : donnez la valeur d\'arrondi désirée (Default : 3)

![](images/Macro_FCTreeView_005.png )

-   Combobox **Name spreadSheet** : Liste les tableurs (spreadsheet) dans la document
-   Line edit **Name spreadSheet** : Affiche le tableur courant (spreadsheet) ou donnez un nom pour un nouveau tableur (spreadsheet)

![](images/Macro_FCTreeView_006.png )


**<img src=images/Macro_FCTreeView_28.png style="width:18px"> Select**

sélectionne tous les checkBox


**<img src=images/Macro_FCTreeView_29.png style="width:18px"> Unselect**

déselectionne tous les checkbox


**<img src=images/Macro_FCTreeView_27.png style="width:18px"> Save**

sauves les données dans le Spreadsheet affiché. S\'il n\'y a aucun spreadsheet actif un spreadsheet nommé **FCSpreadSheet** est créé


**<img src=images/Macro_FCTreeView_26.png style="width:18px"> Quit**

quitte la fenêtre options Spreadsheet

### Icons

Les icônes doivent être copiés dans le même répertoire que la macro [Macro\_FCTreeView\_Icon](https://forum.freecadweb.org/download/file.php?id=70498)

![Icon used for the Name of object](images/Macro_FCTreeView_00.png ) ![Icon used for visualise if the object is status Visible (mouse click for Hidden)](images/Macro_FCTreeView_01.png ) ![Icon used for visualise if the object is status Hidden (mouse click for Visible)](images/Macro_FCTreeView_02.png ) ![Icon used for inform the object in a group the number objects is displayed in top group](images/Macro_FCTreeView_03.png ) ![Icon used for displayed the single object (not group)](images/Macro_FCTreeView_04.png ) ![Icon used for the Label of object](images/Macro_FCTreeView_05.png ) ![Icon used for flip/flop normal/Visibility](images/Macro_FCTreeView_06.png ) ![Icon used for flip/flop normal/Group](images/Macro_FCTreeView_07.png ) ![Icon used for Reverse the data listing (momentarily not used)](images/Macro_FCTreeView_08.png ) ![Icon used for quit Macro FCTreeView (momentarily not used)](images/Macro_FCTreeView_09.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Name](images/Macro_FCTreeView_10.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Label](images/Macro_FCTreeView_11.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Visibility/Hidden](images/Macro_FCTreeView_12.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Grout/Single object](images/Macro_FCTreeView_13.png ) ![Icon used for flip/flop the data listing Fold/Expend](images/Macro_FCTreeView_14.png ) ![Icon used for flip/flop the data listing Expend/Fold](images/Macro_FCTreeView_15.png ) ![Icon used for reload the data in the project](images/Macro_FCTreeView_16.png ) ![Icon used for the Name contains objects (or folder Group)](images/Macro_FCTreeView_17.png ) ![Icon used for return in original organisation after operation visibility/Hidden](images/Macro_FCTreeView_18.png ) ![If this check Box is checked the sort is created by length with the button clicked (Name, Label \...)](images/Macro_FCTreeView_19.png ) ![Icon used for Clear the search line edit](images/Macro_FCTreeView_20.png ) ![Icon used for flip/flop Split the Name list](images/Macro_FCTreeView_21.png ) ![Icon used for flip/flop Split the Name and Label list](images/Macro_FCTreeView_22.png ) ![Icon used for Selected all object(s) displayed in the window](images/Macro_FCTreeView_23.png ) ![Icon used for Unselected all object(s)](images/Macro_FCTreeView_24.png ) ![Icon used for access in Spreadsheet options](images/Macro_FCTreeView_25.png ) ![Icon used for quit the Spreadsheet options](images/Macro_FCTreeView_26.png ) ![Icon used for save the data in Spreadsheet](images/Macro_FCTreeView_27.png ) ![Icon used for select all checkbox options](images/Macro_FCTreeView_28.png ) ![Icon used for unselected all checkbox options](images/Macro_FCTreeView_29.png ) ![Icon used for save the value data in Spreadsheet](images/Macro_FCTreeView_30.png ) ![Icon used for save the value and Unit data in Spreadsheet](images/Macro_FCTreeView_31.png ) ![Icon used for save the value, Unit and type data in Spreadsheet](images/Macro_FCTreeView_32.png ) ![Icon used for split the value, Unit and type in cell separate in Spreadsheet](images/Macro_FCTreeView_33.png )

## Script

Pour éviter de nombreuses instances, le clic sur le bouton ToolBar a un effet flip/flop (masquer/visible)

La macro s\'accroche du côté droit de la fenêtre, pour avoir la macro dockée à gauche de l\'écran, modifiez la valeur de la ligne 133 **testing = 0** (ou changez la en maintenant la touche de la souris enfoncée sur le bord supérieur de la fenêtre et déplacez la)

The icon ToolBar ![Macro FCTreeView](images/Macro_FCTreeView.png )

**Macro\_FCTreeView.FCMacro**


{{CodeDownload|https://gist.github.com/mario52a/67517ef758ff20005d0a6adcfd8c9190|Macro_FCTreeView.FCMacro}}

## A faire 

~~Docked the macro~~

## Version

ver 00.09 (2020-09-24) : correction de la cause du \"**gel**\" de la macro après avoir appellé **assembly4 workbench** j\'ai activé \"**Class SelObserver**\" et ça a fonctionné ???


```python
class SelObserver:
    def addSelection(self, document, object, element, position):  # Selection
        global sourisPass
        global listeSorted
        global ui

        None
```

ver 00.08 (2020-02-25) : upgrade avec des Layout

ver 00.07 (06/05/2018) : modification de la procédure pour rechercher l\'emplacement de la dernière cellule utilisée

ver 00.06 (13/12/2017) : correction d\'un petit bug ligne del line num 1881 \"del listeSortedBis\[doublon\]\[4:\] \# supprime le fond inutile\" thanks renatorivo

ver 00.05 (27/11/2017) : ajout création d\'un spreadsheet avec inclusion de beaucoup d\'options

ver 00.04 (29-09-2017) : ajout recherche par valeur numerique (longueur, rayon\....)

recherche par valeur :


```python
global impost                 ; impost = ["Angle","Angle0","Angle1","Angle2","Angle3","ChamferSize","Circumradius","Columns","Degree",
                                          "FilletRadius","FirstAngle","Growth","Height","LastAngle","Length","Length2","MajorRadius",
                                          "MinorRadius","Pitch","Polygon","Radius","Radius1","Radius2","Radius3","Rows","Size","Width",
                                          "X","X1","X2","Xmax","Xmin","X2max","X2min",
                                          "Y","Y1","Y2","Ymax","Ymin","Y2max","Y2min",
                                          "Z","Z1","Z2","Zmax","Zmin","Z2max","Z2min"]
```

ver 00.03 (23/09/2017) : ajout recherche par type d\'objet

ver 00.02 (11/09/2017) : modifié pour docker et limiter les multiples instances avec bouton flip/flop (macro caché/visible)

ver 00.01 (08/09/2017) :
