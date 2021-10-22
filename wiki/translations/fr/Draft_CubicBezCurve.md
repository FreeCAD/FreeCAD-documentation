---
- GuiCommand:/fr
   Name:Draft CubicBezCurve
   Name/fr:Draft Courbe de Bézier cubique
   MenuLocation:Drafting → Outils Bézier → Courbe de Bézier cubique
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Draft Courbe de Bézier](Draft_BezCurve/fr.md), [Draft B-spline](Draft_BSpline/fr.md)
---

# Draft CubicBezCurve/fr

## Description

La commande <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> **Courbe de Bézier cubique** crée une [Courbe de Bézier](https://fr.wikipedia.org/wiki/Courbe_de_B%C3%A9zier) du troisième degré (quatre points requis).

La courbe de Bézier est l\'une des courbes les plus utilisées en infographie. Cette commande vous permet de créer une courbe continue composée de plusieurs segments de Bézier du 3e degré, d\'une manière similaire à l\'outil Bézier de _.

Les commandes [Draft Courbe de Bézier](Draft_BezCurve/fr.md) et Draft Courbe de Bézier cubique utilisent **des points de contrôle** pour définir la position et la courbure de la spline. La commande [Draft B-spline](Draft_BSpline/fr.md), quant à elle, spécifie les **points exacts** par lesquels la courbe passera.

<img alt="" src=images/Draft_CubicBezCurve_example.png  style="width:500px;"> 
*Spline constituée de trois segments cubiques de Bézier. Le premier segment est défini par quatre points. Les segments suivants réutilisent deux points du segment précédent et ne nécessitent donc que deux points supplémentaires.*

## Utilisation

Voir aussi: [Draft La barre](Draft_Tray/fr.md), [Draft Accrochage](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_CubicBezCurve.svg" width=16px> [Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md)**.
    -   Sélectionnez la **Drafting → Outils Bézier → <img src="images/Draft_CubicBezCurve.svg" width=16px> Courbe de Bézier cubique** dans le menu.
2.  Le panneau de tâches **Courbe cubique de Bézier** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Il n\'est pas possible de saisir des points via le panneau de tâches.
4.  Pour les [modes de navigation par la souris](Mouse_navigation/fr.md) suivants, une touche du clavier doit être maintenue enfoncée :
    -   Si vous utilisez le [Mode OpenInventor](Mouse_navigation/fr#Mode_OpenInventor.md), la touche **Ctrl** doit être maintenue enfoncée pendant toute la durée de la commande.
    -   Si vous utilisez le [Mode Gestuel](Mouse_navigation/fr#Mode_Gestuel.md), la touche **Alt** doit être maintenue enfoncée pour chaque séquence de clic et de relâchement, mais il est également possible de maintenir cette touche enfoncée pendant toute la durée de la commande.
5.  Choisissez le premier point dans la [Vue 3D](3D_view/fr.md) et maintenez le bouton de la souris (1), il s\'agit du premier point.
6.  Faites glisser le pointeur vers un autre point de la [Vue 3D](3D_view/fr.md) et relâchez le bouton de la souris (2), il s\'agit du premier point de contrôle.
7.  Déplacez le pointeur vers un autre point dans la [Vue 3D](3D_view/fr.md), choisissez ce point et maintenez le bouton de la souris (3), il s\'agit du deuxième point d\'extrémité.
8.  Déplacez le pointeur vers un autre point dans la [Vue 3D](3D_view/fr.md) pour ajuster la courbure finale du segment et relâchez le bouton de la souris (4), il s\'agit du deuxième point de contrôle.
9.  Vous avez maintenant une courbe de Bézier du 3ème degré.
10. Vous pouvez répéter le processus de cliquer et de maintenir (5), puis de faire glisser et de relâcher (6) pour ajouter d\'autres segments.
11. Chaque segment suivant utilisera le deuxième point d\'extrémité et le deuxième point de contrôle du segment précédent comme premier point d\'extrémité et premier point de contrôle respectivement.
12. Appuyez sur **Echap** ou sur le bouton **Fermer** pour terminer la commande.

## Options

Voir [Draft Courbe de Bézier](Draft_BezCurve/fr#Options.md).

## Notes

-   Une Draft Courbe de Bézier cubique peut être éditée avec la commande [Draft Editer](Draft_Edit/fr.md).

## Préférences

Voir [Draft Courbe de Bézier](Draft_BezCurve/fr#Pr.C3.A9f.C3.A9rences.md).

## Propriétés

Voir [Draft Courbe de Bézier](Draft_BezCurve/fr#Propri.C3.A9t.C3.A9s.md).

## Script

Voir aussi: _.

Voir [Draft Courbe de Bézier](Draft_BezCurve/fr.md) pour des informations générales. Une courbe de Bézier cubique est créée en passant l\'option degré=3 à `makeBezCurve()`.

Pour chaque segment de Bézier cubique, il faut utiliser quatre points dont les deux points extrêmes indiquent le passage de la spline et où les deux points intermédiaires sont des points de contrôle.

-   Si seulement 3 points sont donnés, cela crée une courbe de Bézier quadratique, avec un seul point de contrôle.
-   Si seulement 2 points sont donnés, cela crée une courbe de Bézier linéaire, c\'est-à-dire une ligne droite.
-   Si 5 points sont donnés, les 4 premiers créent un segment de Bézier cubique; les 4ème et 5ème points sont utilisés pour créer une ligne droite.
-   Si 6 points sont donnés, les 4 premiers créent un segment de Bézier cubique; le 4ème et les deux autres points sont utilisés pour créer un segment de Bézier quadratique.
-   Si 7 points sont donnés, les 4 premiers créent un segment de Bézier cubique; le 4ème et les trois autres points sont utilisés pour créer un deuxième segment de Bézier cubique.
-   En général, le dernier point d\'un groupe de quatre est partagé avec les trois points suivants au maximum pour créer un autre segment de Bézier.
-   Pour avoir des courbes lisses, sans segment droit, le nombre de points doit être `3n + 1` ou `3n` où `n` est le nombre de segments, pour n >= 1.

<img alt="" src=images/Draft_CubicBezCurve_API_example.png  style="width:600px;">



*Exemples de courbes de Bézier produites en utilisant 2, 3, 4, 5, 6, 7 et 8 points. Les lignes continues indiquent les segments de Bézier cubiques. Les autres lignes sont quadratiques ou linéaires.*

Exemple:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(-3500, 0, 0)
p2 = App.Vector(-3000, 2000, 0)
p3 = App.Vector(-1100, 2000, 0)
p4 = App.Vector(0, 0, 0)

p5 = App.Vector(1500, -2000, 0)
p6 = App.Vector(3000, -1500, 0)
p7 = App.Vector(5000, 0, 0)
p8 = App.Vector(6000, 1500, 0)
rot = App.Rotation()

c1 = Draft.make_circle(100, placement=App.Placement(p1, rot), face=False)
c1.Label = "B1_E1"
c2 = Draft.make_circle(50, placement=App.Placement(p2, rot), face=True)
c2.Label = "B1_c1"
c3 = Draft.make_circle(50, placement=App.Placement(p3, rot), face=True)
c3.Label = "B1_c2"
c4 = Draft.make_circle(100, placement=App.Placement(p4, rot), face=False)
c4.Label = "B1_E2"
c5 = Draft.make_circle(50, placement=App.Placement(p5, rot), face=True)
c5.Label = "B2_c3"
c6 = Draft.make_circle(50, placement=App.Placement(p6, rot), face=True)
c6.Label = "B2_c4"
c7 = Draft.make_circle(100, placement=App.Placement(p7, rot), face=False)
c7.Label = "B2_E3"
c8 = Draft.make_circle(50, placement=App.Placement(p8, rot), face=True)
c8.Label = "B3_c5"

doc.recompute()

B1 = Draft.make_bezcurve([p1, p2], degree=3)
B1.Label = "B_lin"
B1.ViewObject.DrawStyle = "Dashed"

B2 = Draft.make_bezcurve([p1, p2, p3], degree=3)
B2.Label = "B_quad"
B2.ViewObject.DrawStyle = "Dotted"

B3 = Draft.make_bezcurve([p1, p2, p3, p4], degree=3)
B3.Label = "B_cub"
B3.ViewObject.LineWidth = 4

B4 = Draft.make_bezcurve([p1, p2, p3, p4, p5], degree=3)
B4.Label = "B_cub+lin"
B4.ViewObject.DrawStyle = "Dashed"

B5 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6], degree=3)
B5.Label = "B_cub+quad"
B5.ViewObject.DrawStyle = "Dotted"

B6 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6, p7], degree=3)
B6.Label = "B_cub+cub"
B6.ViewObject.LineWidth = 2

B7 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6, p7, p8], degree=3)
B7.Label = "B_cub+cub+lin"
B7.ViewObject.DrawStyle = "Dashed"

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft CubicBezCurve/fr
