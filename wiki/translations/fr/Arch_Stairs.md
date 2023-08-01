---
- GuiCommand:
   Name: Arch Stairs
   Name/fr: Arch Escalier
   MenuLocation: Arch - Escalier
   Workbenches: [Arch](Arch_Workbench/fr.md)
   Shortcut: **S** **R**
   Version: 0.14
   SeeAlso: [Arch Structure](Arch_Structure/fr.md), [Arch Equipement](Arch_Equipment/fr.md)
---

# Arch Stairs/fr

## Description

L\'outil [Arch Escalier](Arch_Stairs/fr.md) vous permet de construire automatiquement plusieurs types d\'escaliers. Les escaliers droits (avec ou sans palier central) peuvent être créés de toutes pièces. Les escaliers plus complexes nécessitent des objets de base.

Voir la [terminologie des escaliers](https://fr.wikipedia.org/wiki/Escalier#Terminologie) pour une définition des différents termes utilisés pour décrire les parties d\'un escaliers.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:600px;"> 
*Deux escaliers ont été créés : l'un avec une structure massive et un palier, l'autre avec un seul limon.*

## Options

-   L\'outil Escalier partage les propriétés communes et les comportements de tous les [Arch Composants](Arch_Component/fr.md)



## Utilisation

1.  Sélectionnez un ou plusieurs objets de base, par exemple des [Draft Lignes](Draft_Line.md) et des [Draft Polylignes](Draft_Wire.md) :
    -   Les Draft Polylignes avec deux segments ou plus seront utilisés pour créer des paliers. Ils doivent être sur un plan parallèle au plan global XY. Par exemple, sélectionnez une polyligne en U pour un palier en demi-tour et une polyligne en L pour un palier en coin.
    -   Les Draft Lignes seront utilisées pour créer des étages.
    -   Si les sommets de toutes les lignes et polylignes ont des coordonnées Z correctes, les escaliers créés utiliseront ces informations.
    -   Les objets de base doivent être sélectionnés dans l\'ordre correctement en commençant par l\'objet du bas.
2.  Appuyez sur le bouton **<img src="images/Arch_Stairs.svg" width=16px> [Escalier](Arch_Stairs/fr.md)** ou appuyez sur les touches **S**, **R**.
3.  Ajustez les propriétés souhaitées. Certaines parties de l\'escalier, comme la structure, peuvent ne pas apparaître immédiatement, si l\'une des propriétés le rend impossible, par exemple une épaisseur de structure de 0.

<img alt="" src=images/Arch_Stairs_Complex_Example.png  style="width:600px;"> 
*Escalier complexe basé sur une sélection de lignes et relié comme indiqué sur la gauche.<br>
En rouge les polylignes utilisées pour les paliers à Z&equals;1500mm, Z&equals;3000mm et Z&equals;4500mm.<br>
En noir, les lignes les reliant utilisées pour les étages.
*



## Propriétés



### Données


{{TitleProperty|Segment and Parts}}

-    **Abs Top|Vector**: (en lecture seule) niveau supérieur absolu auquel mène l\'escalier.

-    **Last Segment|Link**: dernier segment (volée des marches ou palier) d\'un escalier en arc se connectant à ce segment. Le niveau de départ de l\'escalier sera le niveau final de ce dernier segment.

-    **Outline Left|VectorList**: contour gauche de l\'escalier.

-    **Outline Left All|VectorList**: contour gauche de tous les segments de l\'escalier.

-    **Outline Right|VectorList**: contour droit de l\'escalier.

-    **Outline Right All|VectorList**: contour droit de tous les segments de l\'escalier.

-    **Railing Height Left|Length**: hauteur de la rampe gauche de l\'escalier ou du palier.

-    **Railing Height Right|Length**: hauteur de la rampe droite de l\'escalier ou du palier.

-    **Railing Left|LinkHidden**: balustrade gauche. {{Version/fr|0.20}} : Le type de propriété est passé de {{Incode|String}} à {{Incode|LinkHidden}}.

-    **Railing Offset Left|Length**: décalage de la rampe gauche par rapport au bord de l\'escalier ou du palier.

-    **Railing Offset Right|Length**: décalage de la rampe droite par rapport au bord de l\'escalier ou du palier.

-    **Railing Right|LinkHidden**: balustrade droite. {{Version/fr|0.20}} : Le type de propriété est passé de {{Incode|String}} à {{Incode|LinkHidden}}.


{{TitleProperty|Stairs}}

-    **Align|Enumeration**: alignement des escaliers sur la ligne de base. Utilisé uniquement si une ligne de base est définie. Peut être {{value|Left}}, {{value|Right}} ou {{value|Center}}.

-    **Height|Length**: hauteur totale de l\'escalier. Utilisé uniquement si aucune ligne de base n\'est définie, ou si la ligne de base est horizontale. Ignoré si **Riser Height Enforce** est non nul.

-    **Length|Length**: longueur totale de l\'escalier si aucune ligne de base n\'est définie. Ignoré si **Tread Depth Enforce** est non nul.

-    **Width|Length**: largeur de l\'escalier.

-    **Width of Landing|FloatList**: si la valeur de **Number Of Steps** est 1, l\'objet escalier agit comme un palier. Lorsque c\'est le cas et que la ligne de base est multi-segments, la largeur du premier segment du palier suit la **Width**, les largeurs des segments suivants suivent la liste définie ici.


{{TitleProperty|Steps}}

-    **Blondel Ratio|Float**: (en lecture seule) le rapport Blondel calculé. Ce rapport indique un escalier confortable et devrait se situer entre 62 et 64 cm ou 24,5 et 25,5 pouces.

-    **Landing Depth|Length**: profondeur du palier de la volée des marches, si elle est activée dans **Landings**. Par défaut, elle correspond à **Width** si elle est égale à 0.

-    **Nosing|Length**: taille du nez des marches.

-    **Number Of Steps|Integer**: nombre de marches (contremarches). Doit être d\'au moins 2 pour une volée simple et d\'au moins 4 pour un escalier avec un palier central.

-    **Riser Height|Length**: (lecture seule) hauteur des contremarches. Si **Riser Height Enforce** est 0, elle est calculée (**Height** / **Number of Steps**). Sinon, il est identique à **Riser Height Enforce**.

-    **Riser Height Enforce|Length**: hauteur imposée des contremarches.

-    **Riser Thickness|Length**: épaisseur des contremarches.

-    **Tread Depth|Length**: (Lecture seule) profondeur des marches. Si **Tread Depth Enforce** est 0, elle est calculée (**Length** / **Number of Steps**). Sinon, il est identique à **Tread Depth Enforce**.

-    **Tread Depth Enforce|Length**: profondeur imposée des marches.

-    **Tread Thickness|Length**: épaisseur des marches.


{{TitleProperty|Structure}}

-    **Connexion Down Start Stairs|Enumeration**: type de liaison entre la plate-forme du plancher inférieur et le début de l\'escalier. Peut être {{value|HorizontalCut}}, {{value|VerticalCut}} ou {{value|HorizontalVerticalCut}}.

-    **Connection End Stairs Up|Enumeration**: type de connexion entre l\'extrémité de l\'escalier et la plate-forme du plancher supérieur. Peut être {{value|toFlightThickness}} ou {{value|toSlabThickness}}.

-    **Down Slab Thickness|Length**: épaisseur de la plate-forme de l\'étage inférieur.

-    **Flight|Enumeration**: direction de volée des marches après le palier. Peut être {{value|Straight}}, {{value|HalfTurnLeft}} ou {{value|HalfTurnRight}}.

-    **Landings|Enumeration**: type de palier. Peut être {{value|None}} ou {{value|At center}}. ({{value|At each corner}} pas encore implémenté).

-    **Stringer Overlap|Length**: chevauchement des limons au-dessus du bas des marches.

-    **Stringer Width|Length**: largeur des longerons.

-    **Structure|Enumeration**: type de structure de l\'escalier. Peut être {{value|None}}, {{value|Massive}}, {{value|One stringer}} ou {{value|Two stringer}}.

-    **Structure Offset|Length**: décalage entre la bordure de l\'escalier et la structure.

-    **Structure Thickness|Length**: épaisseur de la structure.

-    **Up Slab Thickness|Length**: épaisseur de la dalle de l\'étage supérieur.

-    **Winders|Enumeration**: type de revêtements. Non implémenté.

## Limitations

-   Seuls les escaliers droits sont disponible pour le moment
-   Voir la [fil du forum](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) pour les escaliers circulaires
-   Voir la [annonce sur le forum](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564).



## Script


**Voir aussi :**

[API](Arch_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Escalier peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante : 
```python
Stairs = makeStairs(baseobj=None, length=None, width=None, height=None, steps=None, name="Stairs")
```

-   Crée un objet avec les attributs donnés
-   Retourne le nouvel objet escalier

-   Crée un objet `Stairs` à partir de `baseobj` donné.
-   Si `baseobj` n\'est pas indiqué, il utilisera `length`, `width`, `height` et `steps` pour construire un objet solide.

Exemple : 
```python
import Arch

Stairs = Arch.makeStairs(length=5000, width=1200, height=3000, steps=14)
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Stairs/fr
