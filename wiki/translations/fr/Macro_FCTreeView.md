# Macro FCTreeView/fr
{{Macro/fr
|Name=Macro FCTreeView
|Icon=Macro_FCTreeView.png
|Description={{ColoredText|#ff0000|#ffffff|Nouvelle version de l'interface graphique modifiée pour la HD dpi (QGridLayout) fonctionnant uniquement avec FC version 0.18 et plus (PySide2 Qt5)}}<br/> <br/>Macro pour lister tous les objets d'un projet dans une liste sans hiérarchie, options de tri par nom, étiquette, visibilité, groupe, par longueur, option de recherche par nom, étiquette... avec ou sans distinction de la casse et sélection de tous les objets affichés dans la fenêtre de la macro.<br/> <br/>Pour la version précédente, voir [https://gist.githubusercontent.com/mario52a/67517ef758ff20005d0a6adcfd8c9190/raw/0a92d7f591a0a179f84b2fc417046723b4d7b0e6/Macro_FCTreeView.FCMacro Macro_FCTreeView.FCMacro] installez la manuellement.
|Author=Mario52
|Version=00.09
|Date=2020-09-24
|FCVersion=0.18 et avant
|Download=[https://forum.freecadweb.org/download/file.php?id=70498 Macro FCTreeView Pack d'icônes] dézipez le fichier .zip et copiez les icônes dans votre répertoire de macros.
}}

## Description

Macro permettant de lister tous les objets du projet dans une seule liste sans hiérarchie, options de tri par nom, étiquette, visibilité, groupe, par longueur, option de recherche par nom, étiquette\... avec ou sans distinction de la casse et de sélectionnez tous les objets affichés dans la fenêtre de la macro. {{Codeextralink|https://gist.githubusercontent.com/mario52a/67517ef758ff20005d0a6adcfd8c9190/raw/59bc2028978c82744c83c6b138ab3ef30e0bf6f3/Macro_FCTreeView.FCMacro}}

## Utilisation

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

Si un objet est sélectionné : le placement de base, la rotation et le centre de masse sont affichés (si disponibles !).
![Icône utilisé pour le nom de l\'objet](images/Macro_FCTreeView_00.png ) Icône utilisé pour le nom de l\'objet (la barre de défilement est colorée en bleu)

![Icône utilisé pour le label de l\'objet](images/Macro_FCTreeView_05.png ) Icône utilisé pour le label de l\'objet (la barre de défilement est colorée en bleu clair)

![Icône utilisé pour visualiser si le statut de l\'objet est Visible (cliquez avec la souris pour caché l\'objet)](images/Macro_FCTreeView_01.png ) (la barre de défilement est colorée en vert)

![Icon used for visualise if the object is status Hidden (cliquez avec la souris pour le rendre visible)](images/Macro_FCTreeView_02.png ) Icône utilisé pour visualiser si le statut de l\'objet est caché (cliquez avec la souris pour le rendre visible) (la barre de défilement est colorée en rouge)

![Icône utilisée pour le nom contient des objets (ou le dossier Groupe)](images/Macro_FCTreeView_17.png ) Icône utilisée pour le nom contenant des objets (ou le dossier Group)

![Icône utilisée pour informer l\'objet dans un groupe, le nombre d\'objets est affiché dans le groupe supérieur.](images/Macro_FCTreeView_03.png ) Icône utilisée pour informer l\'objet dans un groupe que le nombre d\'objets est affiché dans le groupe supérieur (la barre de défilement est colorée en rouge clair).

![Icône utilisée pour afficher l\'objet unique (pas le groupe)](images/Macro_FCTreeView_04.png ) Icône utilisée pour afficher l\'objet unique (pas le groupe)

### Section **Sort by :** 


**[<img src=images/Macro_FCTreeView_10.png style="width:18px"> Name**

Icône utilisée pour le basculement normal/inversé de la liste des données triées par nom


**[<img src=images/Macro_FCTreeView_11.png style="width:18px"> Label**

Icône utilisée pour le basculement normal/inversé de la liste des données triées par étiquette


**[<img src=images/Macro_FCTreeView_12.png style="width:18px"> Visible**

Icône utilisée pour le basculement normal/inversé de la liste des données triées par visible/caché


**[<img src=images/Macro_FCTreeView_13.png style="width:18px"> Group**

Icône utilisée pour le basculement normal/inversé de la liste des données triées par groupe/objet unique


**[<img src=images/Macro_FCTreeView_19.png style="width:18px"> Length**

Si cette case est cochée, le tri est créé par longueur avec le bouton cliqué (Name, Label\...)

### Section **Global** 


**[<img src=images/Macro_FCTreeView_21.png style="width:18px"> Split**

Bascule de séparation de la liste des noms


**[<img src=images/Macro_FCTreeView_22.png style="width:18px"> Split**

Bascule de séparation de la liste des noms et des étiquettes


**[<img src=images/Macro_FCTreeView_14.png style="width:18px"> Expend**

Bascule de séparation de la liste les données plier/déployer


**[<img src=images/Macro_FCTreeView_15.png style="width:18px"> Expend**

Bascule de séparation de la liste les données déployer/plier


**[<img src=images/Macro_FCTreeView_06.png style="width:18px"> Visibility**

Bascule de normal/visible


**[<img src=images/Macro_FCTreeView_07.png style="width:18px"> Group**

Bascule de normal/groupe


**[<img src=images/Macro_FCTreeView_16.png style="width:18px"> Reload**

Recharge les données dans le projet


**[<img src=images/Macro_FCTreeView_18.png style="width:18px"> Original**

Retour dans l\'organisation originale après l\'opération visibilité/caché


**[<img src=images/Macro_FCTreeView_01.png style="width:18px"> All Visible**

Visualise si l\'objet est de status Visible


**[<img src=images/Macro_FCTreeView_02.png style="width:18px"> All Hidden**

Visualise si l\'objet a le statut caché

### Section **Search** 


**[<img src=images/Macro_FCTreeView_20.png style="width:18px"> Clear**

Efface l\'édition de la ligne de recherche

#### Options du bouton radio **Search**: 

-   **(\"NLwc\")** : recherche par Name et Label **W**ithout sans respecter la **C**ase sensitive

-   **(\"Nsc\")** : recherche par Name en respectant la **S**ensitive **C**ase

-   **(\"Lwc\")** : recherche par Label **W**ithout sans respecter la **C**ase sensitive

-   **(\"NLsc\")** : recherche par Name et Label en respectant la **S**ensitive **C**ase

-   **(\"NLwsc\")** : recherche par Name et Label dans le mot en respectant la **S**ensitive **C**ase (comme dans le panneau sélection de FreeCAD)

-   **(Nu)** : recherche par valeur numérique (rayon, longueur, angle\...) voir section version


**[<img src=images/Macro_FCTreeView_23.png style="width:18px"> Select**

bascule pour sélectionner tous les objets affichés dans la fenêtre


**[<img src=images/Macro_FCTreeView_24.png style="width:18px"> Unselected**

bascule pour désélectionner tous les objets


**[<img src=images/Macro_FCTreeView_25.png style="width:18px"> S Sheet**

accès aux options du tableur (Spreadsheet)

### Les options de SpreadSheet 

![Macro FCTreeView](images/TreeView_SpeadSheet.gif ) 

![](images/Macro_FCTreeView_001.png )

![](images/Macro_FCTreeView_002.png )

-   Options de case à cocher pour sélectionner les données à sauvegarder dans la feuille de calcul


**[<img src=images/Macro_FCTreeView_28.png style="width:18px"> Select**

: sélectionne toutes les cases à cocher à garder


**[<img src=images/Macro_FCTreeView_29.png style="width:18px"> Select**

: désélectionne toutes les cases à cocher à garder

![](images/Macro_FCTreeView_003.png )

-   **Value** : seule la valeur est sauvegardées dans la cellule
    -   Ex : 10.00 ![](images/Macro_FCTreeView_30.png )
-   **Val Gr** : la valeur et l\'unité sont sauvegardées dans une unique cellule
    -   Ex : 10.00 mm ![](images/Macro_FCTreeView_31.png )
-   **Val Gr Ph** : la valeur, l\'unité et la donnée physique sont sauvegardées dans une seule cellule
    -   Ex : 10.00 mm Length ![](images/Macro_FCTreeView_32.png )
-   **Split** : si cette case est cochée, les données sont coupées et sauvegardées dans une cellule séparée
    -   Ex : 10.00 \| mm \| length ![](images/Macro_FCTreeView_33.png )

![](images/Macro_FCTreeView_004.png )

-   Combobox **mm** : sélectionnez l\'unité désirée. La valeur est convertie dans l\'unité sélectionnée. Les unités disponibles sont :
    -   km, hm, dam, m, dm, cm, **mm**, um, nm, pm, fm, in, lk, ft, yd, rd, ch, fur, mi, lea, nmi
-   Combobox **gram** : sélectionnez l\'unité de poids désirée. La valeur est convertie dans l\'unité sélectionnée. Les unités disponibles sont :
    -   t, q, kg, hg, dag, **g**, dg, cg, mg, µg, ng, pg, fg, gr, dr, oz, oz t, lb, t lb, st, qtr, cwt, tonneau fr, ct
-   Spinbox **Densite** : donnez la densité par dm3 du matériau utilisé (Par défaut : 1.0000)
-   Spinbox **Round** : donnez la valeur d\'arrondi désirée (Par défaut : 3)

![](images/Macro_FCTreeView_005.png )

-   Combobox **Name spreadSheet** : liste la feuille de calcul dans le document
-   Modification de la ligne **Name spreadSheet** : affiche la feuille de calcul actuelle ou donnez le nom de la nouvelle feuille de calcul.

![](images/Macro_FCTreeView_006.png )


**[<img src=images/Macro_FCTreeView_28.png style="width:18px"> Select**

sélectionne toutes les options des cases à cocher


**[<img src=images/Macro_FCTreeView_29.png style="width:18px"> Unselect**

déselectionne toutes les options des cases à cocher


**[<img src=images/Macro_FCTreeView_27.png style="width:18px"> Save**

sauvegarde les données dans la feuille de calcul affichée. Si aucune feuille de calcul n\'est active, la feuille de calcul nommée **FCSpreadSheet** est créée


**[<img src=images/Macro_FCTreeView_26.png style="width:18px"> Quit**

quitte les options de la feuille de calcul

### Icônes

Les icônes doivent être copiés dans le même répertoire que la macro. [Macro_FCTreeView_Icon](https://forum.freecadweb.org/download/file.php?id=70498)

![Icon used for the Name of object](images/Macro_FCTreeView_00.png ) ![Icon used for visualise if the object is status Visible (mouse click for Hidden)](images/Macro_FCTreeView_01.png ) ![Icon used for visualise if the object is status Hidden (mouse click for Visible)](images/Macro_FCTreeView_02.png ) ![Icon used for inform the object in a group the number objects is displayed in top group](images/Macro_FCTreeView_03.png ) ![Icon used for displayed the single object (not group)](images/Macro_FCTreeView_04.png ) ![Icon used for the Label of object](images/Macro_FCTreeView_05.png ) ![Icon used for flip/flop normal/Visibility](images/Macro_FCTreeView_06.png ) ![Icon used for flip/flop normal/Group](images/Macro_FCTreeView_07.png ) ![Icon used for Reverse the data listing (momentarily not used)](images/Macro_FCTreeView_08.png ) ![Icon used for quit Macro FCTreeView (momentarily not used)](images/Macro_FCTreeView_09.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Name](images/Macro_FCTreeView_10.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Label](images/Macro_FCTreeView_11.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Visibility/Hidden](images/Macro_FCTreeView_12.png ) ![Icon used for flip/flop normal/reverse the data listing sort by Grout/Single object](images/Macro_FCTreeView_13.png ) ![Icon used for flip/flop the data listing Fold/Expend](images/Macro_FCTreeView_14.png ) ![Icon used for flip/flop the data listing Expend/Fold](images/Macro_FCTreeView_15.png ) ![Icon used for reload the data in the project](images/Macro_FCTreeView_16.png ) ![Icon used for the Name contains objects (or folder Group)](images/Macro_FCTreeView_17.png ) ![Icon used for return in original organisation after operation visibility/Hidden](images/Macro_FCTreeView_18.png ) ![If this check Box is checked the sort is created by length with the button clicked (Name, Label \...)](images/Macro_FCTreeView_19.png ) ![Icon used for Clear the search line edit](images/Macro_FCTreeView_20.png ) ![Icon used for flip/flop Split the Name list](images/Macro_FCTreeView_21.png ) ![Icon used for flip/flop Split the Name and Label list](images/Macro_FCTreeView_22.png ) ![Icon used for Selected all object(s) displayed in the window](images/Macro_FCTreeView_23.png ) ![Icon used for Unselected all object(s)](images/Macro_FCTreeView_24.png ) ![Icon used for access in Spreadsheet options](images/Macro_FCTreeView_25.png ) ![Icon used for quit the Spreadsheet options](images/Macro_FCTreeView_26.png ) ![Icon used for save the data in Spreadsheet](images/Macro_FCTreeView_27.png ) ![Icon used for select all checkbox options](images/Macro_FCTreeView_28.png ) ![Icon used for unselected all checkbox options](images/Macro_FCTreeView_29.png ) ![Icon used for save the value data in Spreadsheet](images/Macro_FCTreeView_30.png ) ![Icon used for save the value and Unit data in Spreadsheet](images/Macro_FCTreeView_31.png ) ![Icon used for save the value, Unit and type data in Spreadsheet](images/Macro_FCTreeView_32.png ) ![Icon used for split the value, Unit and type in cell separate in Spreadsheet](images/Macro_FCTreeView_33.png )

## Script

Pour éviter de nombreuses instances, les clics sur les boutons de la barre d\'outils ont pour effet d\'inverser les rôles (caché/visible).

La macro est située du côté droit de la fenêtre, pour la modifier modifier la valeur ligne numéro 133 **testing = 0** (ou la modifier avec la souris comme un widget normal)

The icon ToolBar ![Macro FCTreeView](images/Macro_FCTreeView.png )

**Macro_FCTreeView.FCMacro**


{{CodeDownload|https://gist.github.com/mario52a/67517ef758ff20005d0a6adcfd8c9190|Macro_FCTreeView.FCMacro}}

## A faire 

~~Ancrer la macro~~

## Version

ver 00.09 (2020-09-24) : correction de la cause **freeze** de la macro après avoir appellé **assembly4 workbench**. J\'ai essayé d\'activer la \"*\'Classe SelObserver*\" et cela a fonctionné???


```python
class SelObserver:
    def addSelection(self, document, object, element, position):  # Selection
        global sourisPass
        global listeSorted
        global ui

        None
```

ver 00.08 (2020-02-25) : mise à niveau avec la mise en page

ver 00.07 (06/05/2018) : modification de la procédure de recherche de la dernière cellule utilisée

ver 00.06 (13/12/2017) : correction d\'un petit bug ligne del line num 1881 \"del listeSortedBis\[doublon\]\[4:\] \# supprime le fond inutile\" merci renatorivo

ver 00.05 (27/11/2017) : ajout d\'un tableur de création et de nombreuses options

ver 00.04 (29-09-2017) : ajout de la recherche par valeur numérique (longueur, rayon\...)

valeurs recherchées :


```python
global impost                 ; impost = ["Angle","Angle0","Angle1","Angle2","Angle3","ChamferSize","Circumradius","Columns","Degree",
                                          "FilletRadius","FirstAngle","Growth","Height","LastAngle","Length","Length2","MajorRadius",
                                          "MinorRadius","Pitch","Polygon","Radius","Radius1","Radius2","Radius3","Rows","Size","Width",
                                          "X","X1","X2","Xmax","Xmin","X2max","X2min",
                                          "Y","Y1","Y2","Ymax","Ymin","Y2max","Y2min",
                                          "Z","Z1","Z2","Zmax","Zmin","Z2max","Z2min"]
```

ver 00.03 (23/09/2017) : ajout recherche par type d\'objet

ver 00.02 (11/09/2017) : modification de la fonction docked et prévention de nombreux cas où le clic sur le bouton est un effet bascule (macro caché/visible)

ver 00.01 (08/09/2017) :



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCTreeView/fr
