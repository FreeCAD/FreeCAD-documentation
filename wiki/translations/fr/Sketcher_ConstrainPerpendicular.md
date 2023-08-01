---
- GuiCommand:
   Name:Sketcher ConstrainPerpendicular
   Name/fr:Sketcher Contrainte perpendiculaire
   MenuLocation:Esquisse → Contraintes d'esquisse → Contrainte perpendiculaire
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**N**
   SeeAlso:[Sketcher Contrainte angulaire](Sketcher_ConstrainAngle/fr.md)
---

# Sketcher ConstrainPerpendicular/fr

## Description

La Contrainte perpendiculaire fait que deux lignes soient perpendiculaires (càd orthognales) l\'une à l\'autre, ou deux courbes soit perpendiculaires à leur intersection. Les lignes sont traitées infinie, et des arcs sont traités comme des cercles pleins/ellipses. La contrainte est également capable de connecter deux courbes, les forçant perpendiculaire à la jointure, de manière similaire à la **[<img src=images/Sketcher_ConstrainTangent.svg style="width:16px"> [Contrainte tangente](Sketcher_ConstrainTangent/fr.md)**.



## Utilisation

Il y a quatre façons différentes d\'appliquer la contrainte :

1.  entre deux courbes (non disponible pour toutes les courbes)
2.  entre deux extrémités d\'une courbe
3.  entre une courbe et un point de terminaison d\'un autre courbe
4.  entre deux courbes au point défini par l\'utilisateur

Pour appliquer la contrainte perpendiculaire, suivre les étapes suivantes :

-   sélectionnez deux ou trois entités dans l\'esquisse.
-   lancez la contrainte en cliquant sur son icône sur la barre d\'outils, ou en sélectionnant l\'option de menu, ou en utilisant le raccourci clavier.



### Entre deux courbes (directement perpendiculaire) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode1.png  style="width:600px;">

Deux courbes doivent être perpendiculaires au point d\'intersection (réel ou des extensions de courbes), et le point d\'intersection sera implicite. Ce mode est appliqué si deux courbes ont été sélectionnées.

**Sélection Acceptée :**

-   la ligne + ligne, cercle, arc
-   cercle, arc + cercle, arc.

Si la perpendicularité direct entre les courbes sélectionnées n\'est pas prise en charge (par exemple, entre une ligne et une ellipse), un point d\'aide sera ajoutés pour esquisser automatiquement, et la perpendiculaire-via-point sera appliquée.

Contrairement aux tangences, il est parfaitement bien de reconstruire le point de perpendicularité en créant un point et le contraindre d\'être sur les deux courbes (Contraignant ainsi le point à l\'intersection).



### Entre deux points terminaux (perpendicularité point-à-point) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode2.png  style="width:600px;">

Dans ce mode, les extrémités sont confondues et le joint est fait pour être à angle droit. Ce mode s\'applique lorsque deux extrémités de deux courbes ont été sélectionnées.

**Sélection acceptée :**

-   point extrémité de ligne/arc/arc d\'ellipse + extrémité de ligne/arc/arc d\'ellipse (soit, deux points de deux courbes)



### Entre courbe et extrémité (Perpendicularité de point-à-courbe) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode3.png  style="width:600px;">

Dans ce mode, une extrémité d\'une courbe est contraint de se trouver sur l\'autre courbe, et les courbes sont obligatoirement perpendiculaires en ce point. Ce mode est appliqué lorsqu\'une courbe et un point de terminaison d\'une autre courbe ont été sélectionnés.

**Sélection acceptée :**

-   ligne, cercle, arc, ellipse, arc-d\'ellipse + extrémité de ligne/arc/arc-d\'ellipse (soit., courbe + extrémité de courbe)



### Entre deux courbes en un point (perpendiculaire-par-point) (v0.15) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode4.png  style="width:600px;">

Dans ce mode, deux courbes sont rendues perpendiculaires, et le point de perpendicularité est identifié. Ce mode est appliqué lorsque deux courbes et un point ont été sélectionnés.

**Sélection acceptée :**

-   ligne/courbe + ligne/courbe

\"Tout point\" peut être un point isolé, ou un point d\'un élément, par exemple, le centre d\'un cercle, un point d\'extrémité d\'un arc, ou l\'origine.

Pour que la contrainte fonctionne correctement, le point doit être sur les deux courbes. Donc, comme la contrainte est invoquée, le point sera automatiquement contraint sur les deux courbes, une ([contrainte auxiliaire](Sketcher_helper_constraint/fr.md) sera ajoutée, si nécessaire) et les courbes seront forcées perpendiculaires en ce point. Ces [contraintes auxiliaires](Sketcher_helper_constraint/fr.md) sont des contraintes ordinaires simples. Elles peuvent être ajoutées manuellement ou supprimées.

Comparé à la perpendiculaire directe cette contrainte est plus lente, car il y a des modes de degrés de liberté impliquées, mais elle prend en charge les ellipses

Le placement du point avant la contrainte qui est appliquée est une indication pour le calculateur dans le cas où il devrait y avoir une perpendicularité .



## Scripts

La Contrainte perpendiculaire peut être créée à partir de [macros](Macros/fr.md) et de la console Python en utilisant ce qui suit : 
```python
# direct perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,icurve2))

# point-to-point perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2))

# perpendicular-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('PerpendicularViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` où :

  - `Sketch` est un objet d\'esquisse

  - `icurve1`, `icurve2` sont deux entiers identifiant les courbes à rendre perpendiculaires. Les entiers sont des indices dans l\'esquisse (la valeur, renvoyée par `Sketch.addGeometry`).

  - `pointpos1`, `pointpos2` doivent être `1` pour le point de départ et `2` pour le point d\'arrivée.

  - `point géoïde` et `pointpos` dans PerpendicularViaPoint sont les indices spécifiant le point de perpendicularité.

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `icurve1`, `icurve2`, `pointpos1`, `pointpos2` et `geoidpoint` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPerpendicular/fr
