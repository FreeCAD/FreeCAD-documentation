---
- GuiCommand:
   Name:Path Vcarve
   Name/fr:Path Gravure en V
   MenuLocation:Path - Graver en V
   Workbenches:[Path](Path_Workbench/fr.md)
   Version:0.19
---

# Path Vcarve/fr

## Description

L\'outil <img alt="" src=images/Path_Vcarve.svg  style="width:24px;"> [Gravure en V](Path_Vcarve/fr.md) est principalement destiné à la gravure de la ligne centrale d\'une <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> [Draft Forme à partir texte](Draft_ShapeString/fr.md) sur une pièce. Cependant, cela peut être utile pour d\'autres types de 2D.

Contrairement à la gravure qui suit les lignes d\'une Forme à partir texte, la gravure en V utilise un couteau en forme de V et tente de dégager la zone en déplaçant le couteau au centre de la région et en variant la profondeur de coupe. Étant donné qu\'un rayon de coupe en V varie avec la profondeur, la largeur de coupe varie également. Le résultat est une coupe plus naturelle, en particulier pour les polices serif.

![](images/Engravepath.png ) ![Example Vcarving Path](images/Vcarvepath.png ) ![](images/Vcarved.png ) ![](images/Scrolltest.png )

L\'algorithme V-carve calcule une trajectoire le long de la ligne centrale d\'une région à l\'aide d\'un diagramme de Voronoï. Cette ligne centrale est le parcours que l\'outil suivra dans le plan XY. Il calcule ensuite un \"cercle inscrit maximal\" le long du parcours. Il s\'agit du plus grand cercle qui peut être tracé à ce point et qui reste entièrement à l\'intérieur de la zone de dégagement. La profondeur de coupe est calculée à l\'aide du rayon du cercle et de l\'angle de la pointe de l\'outil.



## Utilisation



### Préparation des formes à graver 

-   Les **[<img src=images/Draft_ShapeString.svg style="width:24px"> [Draft Formes à partir texte](Draft_ShapeString/fr.md)** sont utilisables dès la sortie de la boîte
-   Les fichiers SVG nécessitent un certain traitement, à la fois dans l\'éditeur et dans l\'<img alt="" src=images/_Workbench_Draft.svg  style="width:24px;"> [Atelier Draft](Draft_Workbench/fr.md) :
    -   Dans l\'éditeur (par exemple [Inkscape](https://www.inkscape.org)) : assurez-vous que le fichier ne contient que des parcours et que les parcours sont dissociés. Assurez-vous qu\'il n\'y a pas de parcours auto-sécants, (dans Inkscape) utilisez Path → Simplify and union to join paths that overlap.
    -   Basculez vers l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md) depuis la [liste déroulante des ateliers](Std_Workbench/fr.md)
    -   Importez le SVG en utilisant **Fichier → Importer → sélectionnez "SVG as geometry"**
    -   Le résultat devrait ressembler à ceci :

        :   ![](images/Svgimport.png )
        :   
            
*Ci-dessus: Résultats de l'importation de "SVG as geometry"*
            

:   

    :   Les trajectoires avec des trous (lettres, la vigne dans l\'image ci-dessus) sont importés comme 2 parcours séparés (nommés le long des lignes de `Path905` et `Path905001` dans la [vue en arborescence](Tree_view/fr.md)), l\'un d\'eux est le trou et l\'autre est le contour. Nous traiterons de cela dans la prochaine étape

-   -   Pour obtenir les faces 2D, [Path Gravure en V](Path_Vcarve/fr.md) a besoin de :
        -   Pour les parcours sans trous :
            1.  Sélectionnez le parcours
            2.  Choisissez **Modification → ![](images/)_[Agréger](Draft_Upgrade/fr.md)**
            3.  Suivi de **Modification → ![](images/)_[Désagréger](Draft_Downgrade/fr.md)**
        -   Pour les parcours avec trous :
            1.  Sélectionnez le parcours extérieur puis le parcours intérieur
            2.  Choisissez **Modification → ![](images/)_[Désagréger](Draft_Downgrade/fr.md)** **deux fois**

        :   Certains parcours se comportent différemment, vous devrez donc peut-être jouer avec **<img src="images/Draft_Upgrade.svg" width=16px> Agréger** et **<img src="images/Draft_Downgrade.svg" width=16px> Désagréger** jusqu\'à ce que vous obteniez quelque chose nommé : `Face<number>`
        :   Le résultat final devrait ressembler à ceci :
        :   ![](images/Svgfaces.png )



### Création de l\'opération Gravure en V 

-   Passer à l\'**[<img src=images/Workbench_Path.svg style="width:16px"> [atelier Path](Path_Workbench/fr.md)** depuis le [menu déroulant des ateliers](Std_Workbench/fr.md)
-   Ajouter une tâche, utilisez les objets nommés `Face<number>` (ou le ShapeString) comme base, ajouter contrôleur d\'objets coupants en V, définir les avances, les vitesses, etc.
-   L\'opération ne prend en charge qu\'un seul objet (soit un seul objet Face, soit un ShapeString), donc pour chaque objet :
    -   Sélectionner **Path → <img src="images/Path_Vcarve.svg" width=24px> Gravure en V** dans le menu supérieur. Cela ouvre le panneau de configuration.
    -   Ouvrir l\'onglet **Géométrie de base** et ajouter toutes les faces du ShapeString, ou la face d\'un seul objet Face obtenu ci-dessus.
    -   Cliquer sur **Appliquer** et inspecter le parcours généré; si nécessaire, ajuster les paramètres d\'opération (le seuil peut être réglé plus haut dans la plupart des situations).
    -   Appuyez sur **OK** pour terminer.

## Options

Vide



## Propriétés



### Données


{{TitleProperty|Base}}

-    **Placement**: -

-    **Label**: -


{{TitleProperty|Depth}}

-    **ClearanceHeight**: -

-    **FinalDepth**: -

-    **SafeHeight**: -

-    **StartDepth**: -

-    **StepDown**: -


{{TitleProperty|Op Values}}

-    **OpFinalDepth**: -

-    **OpStartDepth**: -

-    **OpStockZMax**: -

-    **OpStockZMin**: -

-    **OpToolDiameter**: -


{{TitleProperty|Path}}

-    **Active**: -

-    **Comment**: -

-    **CoolantMode**: -

-    **StartVertex**: -

-    **ToolController**: -

-    **UserLabel**: -

#### Hidden

-    **Base**: -

-    **BaseObject**: -

-    **BaseShapes**: -

-    **ExpressionEngine**: -

-    **Label2**: -

-    **Path**: -

-    **Proxy**: -

-    **Visibility**: -



### Vue

Vide



## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple :


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Vcarve/fr
