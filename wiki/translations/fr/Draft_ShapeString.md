---
 GuiCommand:
   Name: Draft ShapeString
   Name/fr: Draft Forme à partir d'un texte
   MenuLocation: Draft , Forme à partir d'un texte
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   Shortcut: 
   Version/fr: 0.14
   SeeAlso: Draft_Text/fr, Draft_Label/fr, Part_Extrude/fr
---

# Draft ShapeString/fr

## Description

La commande <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> **Draft Forme à partir d\'un texte** crée une forme composée qui représente un texte. Cette forme peut être utilisée pour créer des lettres en 3D avec la commande [Part Extruder](Part_Extrude/fr.md).

La commande Draft Forme à partir d\'un texte n\'est pas destinée aux annotations de texte standard. La commande [Draft Texte](Draft_Text/fr.md) ou la commande [Draft Étiquette](Draft_Label/fr.md) doivent être utilisées à cette fin.

![](images/Draft_ShapeString_Example400.png ) 
*Un seul point requis pour positionner la Forme à partir d'un texte*



## Utilisation

Pour les utilisateurs de Windows : veuillez d\'abord lire le paragraphe [Sélection des fichiers de police sous Windows](#S.C3.A9lection_des_fichiers_de_police_sous_Windows.md).

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_ShapeString.svg" width=16px> [Forme à partir d'un texte](Draft_ShapeString/fr.md)**.
    -   Sélectionnez l\'option **Draft → <img src="images/Draft_ShapeString.svg" width=16px> Forme à partir d'un texte** du menu.
2.  Le panneau de tâches **Forme à partir d'un texte** s\'ouvre.
3.  Cliquez sur un point dans la [vue 3D](3D_view/fr.md) ou rentrez des coordonnées.
4.  Vous pouvez également appuyer sur le bouton **Réinitialiser le point** pour réinitialiser le point à l\'origine.
5.  Saisissez une **Chaîne**.
6.  Spécifiez la **Hauteur**.
7.  Pour sélectionner une police, effectuez l\'une des opérations suivantes :
    -   Saisissez un chemin de fichier dans la zone de saisie **Fichier de police**.
    -   Appuyez sur le bouton **...** et sélectionnez un fichier.
    -   Appuyez sur le bouton **OK** pour terminer la commande.
8.  Vous pouvez également modifier la **Justification** de la Forme à partir de texte. Voir [Propriétés](#Propriétés.md).

## Options

-   Appuyez sur **Échap** ou sur le bouton **Annuler** pour annuler la commande.



## Remarques

-   Une Draft Forme à partir d\'un texte peut être éditée en double-cliquant dessus dans la [vue en arborescence](Tree_view/fr.md). {{Version/fr|0.20}}
-   Les polices prises en charge sont TrueType (**.ttf**), OpenType (**.otf**) et Type 1 (**.pfb**).
-   La commande est limitée au texte de gauche à droite. Les textes de droite à gauche et de haut en bas ne sont pas pris en charge.
-   De très petites hauteurs de texte peuvent entraîner des formes de caractères déformées en raison de la perte de détails lors de la mise à l\'échelle.
-   Les polices peuvent générer une géométrie problématique. En effet, les contours des polices peuvent se chevaucher et présenter de petites discontinuités. Ces conditions sont considérées comme des erreurs dans les bords utilisés pour définir les faces.
-   Une Forme à partir d\'un texte peut également être créée avec la [Macro Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP/fr.md).
-   Pour créer des Draft Formes à partir d\'un texte disposées de manière circulaire, utilisez la [Macro FCCircularText](Macro_FCCircularText/fr.md).



## Sélection des fichiers de police sous Windows 

Sous Windows, l\'accès au dossier des polices par défaut est restreint. Cela affecte la sélection du fichier de police pour les Formes à partir d\'un texte. Il y a trois cas dans FreeCAD où un fichier de police pour les Formes à partir d\'un texte peut être spécifié : dans le panneau des tâches de Forme à partir d\'un texte, lors de la modification de la propriété **Font File** d\'un ShapeString et lors de la spécification du fichier de police par défaut dans les [Draft Préférences](Draft_Preferences/fr#Textes_et_cotes.md).

Il n\'est pas possible d\'appuyer sur le bouton **...** puis de sélectionner un fichier dans le dossier de polices par défaut de Windows lorsque l\'on utilise la boîte de dialogue des fichiers natifs. Il existe un certain nombre de solutions de contournement :

-   Assurez-vous que la valeur **DontUseNativeFontDialog** est définie sur {{True}}, qui est la valeur par défaut de cette préférence. Cela n\'appellera un dialogue de fichier différent, non natif, que si vous appuyez sur le bouton **...** dans le panneau de tâches de Forme à partir de texte. Cette boîte de dialogue de fichier permet d\'accéder au dossier de polices par défaut de Windows.
-   Changez **DontUseNativeDialog** en {{True}}. Ceci indique à FreeCAD de toujours utiliser le dialogue de fichier non-natif.
-   Spécifiez le fichier de police dans le champ de saisie. Vous pouvez bien sûr taper le chemin complet ou copier-coller le chemin depuis l\'explorateur de fichiers de Windows. Mais il existe aussi une autre façon de saisir le chemin. Si vous saisissez {{Value|C:\}}, une liste déroulante s\'affiche. Sélectionnez {{Value|Windows}} dans cette liste et ajoutez {{Value|\F}}. Sélectionnez {{Value|Fonts}} dans la nouvelle liste déroulante. Enfin, ajoutez {{Value|\}} et la ou les premières lettres du fichier de police, puis sélectionnez-le dans la liste déroulante.

Voir le paragraphe [Préférences](#Pr.C3.A9f.C3.A9rences.md) ci-dessous pour l\'emplacement des préférences mentionnées.



## Tutoriels

-   [Draft Tutoriel Forme à partir d\'un texte](Draft_ShapeString_tutorial/fr.md) : extruder une chaîne de caractère, la positionner dans un espace 3D et créer une gravure dans un autre corps.
-   [How to use ShapeStrings in PartDesign sur le forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md), [Draft Préférences](Draft_Preferences/fr.md) et [Std Éditeur des paramètres](Std_DlgParameter/fr.md).

-   Le fichier de police par défaut peut être modifié dans les préférences : **Édition → Préférences... → Draft → Textes et cotes → Fichier de la police par défaut de Forme à partir d'un texte**.
-   Pour les utilisateurs de Windows :
    -   Définissez **Outils → Editer les paramètres... → BaseApp → Preferences → Dialog → DontUseNativeFontDialog** à {{True}} pour utiliser le dialogue de fichier non natif lors de la sélection d\'un fichier de police dans le panneau des tâches de Forme à partir d\'un texte.
    -   Autre possibilité, définissez **Outils → Modifier les paramètres... → BaseApp → Preferences → Dialog → DontUseNativeDialog** à {{True}} pour toujours utiliser le dialogue de fichier non natif.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Forme à partir d\'un texte est dérivé d\'un [Part Part2DObject](Part_Part2DObject/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Draft}}

-    **Font File|File**: nom du fichier de la police.

-    **Fuse|Bool**: fusionne les faces si les faces se chevauchent, ce qui n\'est généralement pas nécessaire (peut être très lent). Ignoré si **Make Face** est `False`. {{Version/fr|0.22}}

-    **Justification|Enumeration**: alignement horizontal et vertical. Options : {{value|Top-Left}}, {{value|Top-Center}}, {{value|Top-Right}}, {{value|Middle-Left}}, {{value|Middle-Center}}, {{value|Middle-Right}}, {{value|Bottom-Left}}, {{value|Bottom-Center}}, {{value|Bottom-Right}}. {{Version/fr|0.22}}

-    **Justification Reference|Enumeration**: référence de hauteur utilisée pour la justification. Options : {{value|Cap Height}}, {{value|Shape Height}}. La hauteur de la forme dépend des caractères figurant dans **String**. {{Version/fr|0.22}}

-    **Keep Left Margin|Bool**: conserve la marge gauche et l\'espace blanc en tête lorsque la justification est à gauche. {{Version/fr|0.22}}

-    **Make Face|Bool**: remplit les lettres avec des faces.

-    **Oblique Angle|Angle**: angle oblique. Doit être compris entre -80° et +80°. {{Version/fr|0.22}}

-    **Scale To Size|Bool**: met à l\'échelle pour s\'assurer que la hauteur de la majuscule est égale à la taille. Si la valeur est `False`, en fonction de la police, la hauteur de la majuscule ne correspondra pas exactement à **Size**. {{Version/fr|0.22}}

-    **Size|Length**: hauteur du texte.

-    **String|String**: chaîne de texte. Une Forme à partir de texte ne peut afficher qu\'une seule ligne de texte.

-    **Tracking|Distance**: espace entre les caractères. Le type de propriété a été mis à jour ({{Version/fr|0.22}}).

<img alt="" src=images/Draft_ShapeString_Justification.png  style="width:200px;"> 
*La hauteur du rectangle rouge (ligne continue) est égale à la hauteur de la majuscule.<br>
La hauteur du rectangle vert (ligne pointillée) est égale à la hauteur de la forme.<br>
Les coins, les points médians des bords et le centre des rectangles correspondent aux<br>
9 options de justification : haut à gauche à bas à droite.*



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour créer une Draft Forme à partir d\'un texte, utilisez la méthode `make_shapestring` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeShapeString`.


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```

-   Crée une forme composée `shapestring` à l\'aide de `String` spécifié et du chemin d\'accès complet d\'un `FontFile` pris en charge.

-    `Size`est la hauteur du texte obtenu en millimètres.

-    `Tracking`est l\'espace entre les caractères en millimètres.

L\'emplacement de la Forme à partir d\'un texte peut être modifié en écrasant ses attributs `Placement` ou en écrasant individuellement ses attributs `Placement.Base` et `Placement.Rotation`.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ShapeString/fr
