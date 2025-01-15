---
 GuiCommand:
   Name: Arch Axis
   Name/fr: Arch Axes
   MenuLocation: Annotation , Axes
   Workbenches: BIM_Workbench/fr
   Shortcut: **A** **X**
   SeeAlso: Arch_AxisSystem/fr, Arch_Grid/fr
---

# Arch Axis/fr

## Description

L\'outil **<img src="images/Arch_Axis.svg" width=16px> [Axes](Arch_Axis/fr.md)** vous permet de placer une série d\'axes dans le document en cours. La distance et l\'angle entre les axes sont personnalisables, ainsi que le style de numérotation. Les axes servent principalement de références pour accrocher des objets mais peuvent également être utilisés avec **<img src="images/Arch_AxisSystem.svg" width=16px> [Arch Système d'axes](Arch_AxisSystem/fr.md)**. Ils peuvent également être référencés par d\'autres objets Arch pour créer des réseaux paramétriques, par exemple des poutres ou des colonnes. **<img src="images/Arch_Grid.svg" width=16px> [Arch Grilles](Arch_Grid/fr.md)** peut également être utilisé à la place des axes.

<img alt="" src=images/Arch_Axis_example.jpg  style="width:600px;"> 
*Deux objets axes placés perpendiculairement l'un par rapport à l'autre pour créer une grille*



## Utilisation

1.  Appuyez sur le bouton **<img src="images/Arch_Axis.svg" width=16px> [Axe](Arch_Axis/fr.md)** ou appuyez sur les touches **A** puis **X**.
2.  [Draft Déplacer](Draft_Move/fr.md)/[Draft Pivoter](Draft_Rotate/fr.md) positionnent le système d\'axes dans la position souhaitée.
3.  Passez en mode édition en double-cliquant sur le système d\'axes dans l\'arborescence pour ajuster ses paramètres tels que le nombre d\'axes, les distances et les angles entre les axes.

## Options

-   Chaque axe de la série a sa propre distance et son propre angle par rapport à l\'axe précédent. Cela permet de faire des systèmes très complexes tels que des systèmes non orthogonaux, des systèmes polaires ou tout type de système non uniforme.
-   Double-cliquez sur l\'axe dans la vue en arborescence permet d\'éditer les distances, les angles et les étiquettes de chaque axe.
-   La longueur des axes, la taille des bulles et les styles de numérotation sont personnalisables directement via les propriétés du système d\'axes.
-   Chaque axe peut également afficher une étiquette, modifiable via la fenêtre de dialogue du panneau des tâches.



## Propriétés

-    **Length**: longueur des axes.

-    **Limit**: si supérieure à zéro, chaque axe sera représenté par deux lignes de la longueur donnée au lieu d\'une ligne continue. {{Version/fr|0.20}}

-    **Bubble Size**: taille des infobulles des axes.

-    **Numeration style**: style de numérotation : 1,2,3, A,B,C, etc\...

-    **Bubble Position**: position de l\'infobulle sur l\'axe : point de départ, point à la fin, les deux ou aucun.

-    **Font Name**: police du numéro de l\'infobulle et/ou des étiquettes

-    **Font Size**: taille du texte de l\'étiquette uniquement (le texte de l\'infobullee est contrôlé par la taille de l\'infobulle)

-    **Show Labels**: active/désactive l\'affichage du textes des étiquettes



## Utilisation comme marque de section 

En définissant la propriété **Bubble Position** à **Arrow left/right** ou **Bar left/right**, l\'axe affichera une flèche ou une barre remplie à la place de l\'infobulle, afin qu\'elle puisse être utilisée comme marque de section. {{Version/fr|0.20}}



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Axes peut être utilisé dans une [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Axes = makeAxis(num=5, size=1000, name="Axes")
```

-   Crée un objet `Axes` à partir du nombre donné (`num`) d\'axes et de `size`, l\'intervalle entre chaque axe.

Exemple :


```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > Arch Axis/fr
