---
- GuiCommand:/fr
   Name:Part Circle
   Name/fr:Part Cercle
   MenuLocation:Pièce → [Créer des primitives](Part_Primitives/fr.md) → Cercle
   Workbenches:[Part](Part_Workbench/fr.md)
---

# Part Circle/fr

## Description

Cette commande va créer une ligne courbe circulaire. Avec les valeurs par défaut, la ligne circulaire sera fermée et sera donc un cercle. Si les propriétés Angle 0 ou Angle 1 sont modifiés par rapport aux valeurs par défaut (0 et 360), le bord sera une courbe ouverte ou arc.

Alternativement, un Cercle peut être défini à partir de trois points. Une fois créé le cercle ne contiendra que les propriétés Cercle standard et ne contient plus les références du point de sa création.

## Utilisation

Une primitive géométrique Cercle est disponible dans la boîte de dialogue Créer des primitives dans l\'atelier Part.

1.  Basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md)
2.  Il existe plusieurs façons d\'accéder à la boîte de dialogue Créer des primitives:
    -   Appuyez sur le bouton <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Création de primitives géométriques](Part_Primitives.md) situé dans la barre d\'outils Part
    -   Utilisez la **Pièce → [Créer des primitives](Part_Primitives/fr.md) → Cercle**

## Propriétés

-    {{Parameter|Radius}}: Le rayon de la courbe ou du cercle (arc ou cercle)

-    {{Parameter|Angle 0}}: Début de la courbe, (en degrés anti-horaire), la valeur par défaut est de 0°.

-    {{Parameter|Angle 1}}: Fin de la courbe, (en degrés anti-horaire), la valeur par défaut est de 360°.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Circle/fr
