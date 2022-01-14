---
- GuiCommand:/fr
   Name:Path Vcarve
   Name/fr:Path Gravure en V
   MenuLocation:Path → Vcarve
   Workbenches:[Path](Path_Workbench.md)
   Version:0.19
---

# Path Vcarve/fr

## Description

L\'outil <img alt="" src=images/Path_Vcarve.svg  style="width:24px;"> [Path Gravure en V](Path_Vcarve/fr.md) est principalement destiné à la gravure de la ligne centrale d\'une <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> [Draft Formes à partir texte](Draft_ShapeString/fr.md) sur une pièce. Cependant, cela peut être utile pour d\'autres types de 2D.

Contrairement à la gravure qui suit les lignes d\'une Forme à partir texte, la gravure en V utilise un couteau en forme de V et tente de dégager la zone en déplaçant le couteau au centre de la région et en variant la profondeur de coupe. Étant donné qu\'un rayon de coupe en V varie avec la profondeur, la largeur de coupe varie également. Le résultat est une coupe plus naturelle, en particulier pour les polices serif.

![](images/Engravepath.png ) ![Example Vcarving Path](images/Vcarvepath.png ) ![](images/Vcarved.png ) ![](images/Scrolltest.png )

L\'algorithme V-carve calcule une trajectoire le long de la ligne médiane d\'une région à l\'aide d\'un diagramme de voronoï. Cette ligne centrale est le chemin que l\'outil suivra dans le plan XY. Il calcule ensuite un \'cercle inscrit maximum\' le long de la trajectoire. C\'est le plus grand cercle qui peut être dessiné à ce point et rester entièrement à l\'intérieur de la zone de compensation. En utilisant le rayon du cercle et l\'angle de pointe de la fraise, la profondeur de coupe est calculée.

## Utilisation

### Préparation des formes à graver 

-   Les **[<img src=images/Draft_ShapeString.svg style="width:24px"> [Draft Formes à partir texte](Draft_ShapeString/fr.md)** sont utilisables dès la sortie de la boîte
-   Les fichiers SVG nécessitent un certain massage, à la fois dans l\'éditeur et dans le <img alt="" src=images/_Workbench_Draft.svg  style="width:24px;"> [Atelier Draft](Draft_Workbench/fr.md):
    -   Dans l\'éditeur (par exemple [inkscape](https://www.inkscape.org)): assurez-vous que le fichier ne contient que des chemins et que les chemins sont dissociés; assurez-vous qu\'il n\'y a pas de chemins auto-sécants, (dans inkscape) utilisez Chemin → Simplifier et union pour joindre les chemins qui se chevauchent.
    -   Basculez vers le <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Atelier Draft](Draft_Workbench/fr.md) dans la [liste déroulante d\'Ateliers](Std_Workbench/fr.md)
    -   Importez le SVG en utilisant **Fichier → Importer → sélectionnez "SVG comme géométrie"**
    -   Le résultat devrait ressembler à ceci:

        :   ![](images/Svgimport.png )
        :   
            
*Ci-dessus: Résultats de l'importation de "SVG en tant que géométrie"*
            

:   

    :   Les trajectoires avec des trous (lettres, la vigne dans l\'image ci-dessus) sont importés comme 2 chemins séparés (nommés le long des lignes de `Path905` et `Path905001` dans l\'arbre), l\'un d\'eux est le trou et l\'autre est le contour; nous traiterons de cela dans la prochaine étape

-   -   Pour obtenir les faces 2D, [Path Vcarve](Path_Vcarve/fr.md) a besoin de:
        -   Pour les trajectoires sans trous:
            1.  Sélectionnez le chemin
            2.  Choisissez **Modification → ![](images/)_[Mettre_à_niveau](Draft_Upgrade/fr.md)**
            3.  Suivi de **Modification → ![](images/)_[Rétrograder](Draft_Downgrade/fr.md)**
        -   Pour les trajectoires sans trous:
            1.  Sélectionnez la trajectoire extérieure puis la trajectoire intérieur
            2.  Choisissez **Modification → ![](images/)_[Rétrograder](Draft_Downgrade/fr.md)** **deux fois**

        :   Certaines trajectoires se comportent différemment, vous devrez donc peut-être jouer avec **<img src="images/Draft_Upgrade.svg" width=16px> Mettre à niveau** et **<img src="images/Draft_Downgrade.svg" width=16px> Rétrograder** jusqu\'à ce que vous obteniez quelque chose nommé: `Face<number>`
        :   Le résultat final devrait ressembler à ceci:
        :   ![](images/Svgfaces.png )

### Création de l\'opération Vcarve 

-   Passez à l\'**[<img src=images/Workbench_Path.svg style="width:16px"> [atelier Path](Path_Workbench/fr.md)** dans le [menu déroulant des ateliers](Std_Workbench/fr.md)
-   Ajoutez un travail, utilisez les objets nommés `Face<number>` (ou le ShapeString) comme base, ajoutez un contrôleur d\'outil v-bit, définissez les flux, les vitesses, etc.
-   L\'opération ne prend en charge qu\'un seul objet (soit un seul objet Face, soit un ShapeString) donc pour chaque objet:
    -   Sélectionnez **Path → <img src="images/Path_Vcarve.svg" width=24px> Vcarve** dans le menu supérieur. Cela ouvre le panneau de configuration.
    -   Ouvrez l\'onglet **Base Geometry** et ajoutez toutes les faces du ShapeString, ou la face d\'un seul objet Face obtenu ci-dessus
    -   Appuyez sur **Apply** et inspectez le chemin généré; si nécessaire, ajustez les paramètres de fonctionnement (le seuil peut être réglé plus haut dans la plupart des situations)
    -   Appuyez sur **OK** pour terminer

## Options

Vide

## Propriétés

### Données

#### Base

-    {{PropertyData/fr|Placement}}: -

-    {{PropertyData/fr|Label}}: -

#### Profondeur

-    {{PropertyData/fr|ClearanceHeight}}: -

-    {{PropertyData/fr|FinalDepth}}: -

-    {{PropertyData/fr|SafeHeight}}: -

-    {{PropertyData/fr|StartDepth}}: -

-    {{PropertyData/fr|StepDown}}: -

#### Valeurs Op 

-    {{PropertyData/fr|OpFinalDepth}}: -

-    {{PropertyData/fr|OpStartDepth}}: -

-    {{PropertyData/fr|OpStockZMax}}: -

-    {{PropertyData/fr|OpStockZMin}}: -

-    {{PropertyData/fr|OpToolDiameter}}: -

#### Trajectoire

-    {{PropertyData/fr|Active}}: -

-    {{PropertyData/fr|Comment}}: -

-    {{PropertyData/fr|CoolantMode}}: -

-    {{PropertyData/fr|StartVertex}}: -

-    {{PropertyData/fr|ToolController}}: -

-    {{PropertyData/fr|UserLabel}}: -

### Cachés

-    {{PropertyData/fr|Base}}: -

-    {{PropertyData/fr|BaseObject}}: -

-    {{PropertyData/fr|BaseShapes}}: -

-    {{PropertyData/fr|ExpressionEngine}}: -

-    {{PropertyData/fr|Label2}}: -

-    {{PropertyData/fr|Path}}: -

-    {{PropertyData/fr|Proxy}}: -

-    {{PropertyData/fr|Visibility}}: -

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
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path Vcarve/fr
