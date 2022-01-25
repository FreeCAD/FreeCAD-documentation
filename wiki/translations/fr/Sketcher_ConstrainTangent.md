---
- GuiCommand:/fr
   Name:Sketcher ConstrainTangent
   Name/fr:Sketcher Contrainte tangente
   MenuLocation:Sketch → Contraintes d'esquisse → Contrainte tangente
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**T**
   SeeAlso:[Sketcher Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md)
---

# Sketcher ConstrainTangent/fr

## Description

La Contrainte tangente fait se toucher deux courbes (devant être tangente). Les lignes sont traitées comme infinie, et les arcs sont traités comme des cercles pleins/ellipses. La contrainte est également capable de connecter deux courbes, les forçant à tangenter au niveau du joint, ce qui rend le joint lisse et continu.

La contrainte de tangente peut également être utilisée avec deux lignes pour les rendre colinéaires.

## Utilisation

Il y a cinq façons différentes d\'appliquer la contrainte :

1.  entre deux courbes (non disponible pour toutes les courbes)
2.  entre deux extrémités d\'une courbe
3.  entre une courbe et un point de terminaison d\'un autre courbe
4.  entre deux courbes au point défini par l\'utilisateur
5.  entre deux lignes pour créer une condition colinéaire

Pour appliquer la contrainte tangente, suivre les étapes suivantes :

-   Sélectionnez deux ou trois entités dans l\'esquisse.
-   Appelez la contrainte en cliquant sur son icône sur la barre d\'outils, ou en sélectionnant l\'option de menu, ou en utilisant le raccourci clavier.

### Entre deux courbes (tangence directe) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:600px;">

Deux courbes doivent être rendues tangentes, et un point de tangence doit être implicite. Ce mode est appliqué si deux courbes sont sélectionnées

**Sélection Acceptée :**

-   ligne + ligne, cercle, arc, ellipse, arc d\'ellipse
-   cercle, arc + cercle, arc.

Si la tangence direct entre les courbes sélectionnées n\'est pas prise en charge (par exemple, entre une ligne et une ellipse), un point d\'aide sera ajoutés pour esquisser automatiquement, et la tangence-via-point sera appliquée.

Il n\'est pas recommandé de reconstruire le point de tangence en créant un point et le contraindre à se positionner sur les deux courbes. Il fonctionnera, mais la convergence sera sérieusement plus lente et il faudra environ deux fois plus d\'itérations pour converger par rapport à la normale. Utiliser d\'autres méthodes pour cette contrainte si le point de tangence est nécessaire.

### Entre deux points de terminaison (tangence point à point) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:600px;">

Dans ce mode, les extrémités sont rendues coïncidentes et le joint est rendu tangent (C1-smooth, ou \"sharp\", selon le placement des courbes avant l\'application de la contrainte). Ce mode est appliqué lorsque deux points d\'extrémité de deux courbes ont été sélectionnés. Si vous voulez ce type de tangence, vous ne devez pas utiliser la concidence plus la tangence entre les courbes/lignes. Le solveur ne peut pas créer de solutions stables pour cette combinaison et remplace les contraintes de manière appropriée.

**Sélection acceptée :**

-   point extrémité de ligne/arc/arc d\'ellipse + extrémité de ligne/arc/arc d\'ellipse (soit deux points de terminaison de deux courbes quelconques)

### Entre une courbe et un point de terminaison (tangence point à courbe) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:600px;">

Dans ce mode, une extrémité d\'une courbe est contraint de se trouver sur l\'autre courbe, et les courbes sont obligatoirement tangentes en ce point. Ce mode est appliqué lorsqu\'une courbe et un point de terminaison d\'une autre courbe ont été sélectionnés.

**Sélection acceptée :**

-   ligne, cercle, arc, ellipse, arc d\'ellipse + extrémité de ligne/arc/arc d\'ellipse (soit une courbe + une extrémité de courbe)

### Entre deux courbes au point (tangent-via-point) (v0.15) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:600px;">

Dans ce mode, deux courbes sont rendues tangentes et le point de tangence est identifié. Ce mode est appliqué lorsque deux courbes et un point ont été sélectionnés.

**Sélection acceptée :**

-   ligne/courbe + ligne/courbe

\"Tout point\" peut être un point isolé ou un point d\'un élément, par exemple, le centre d\'un cercle, un point d\'extrémité d\'un arc ou l\'origine.

Pour que la contrainte fonctionne correctement, le point doit être sur les deux courbes. Donc, comme la contrainte est invoquée, le point sera automatiquement contraint sur les deux courbes (une [Sketcher contrainte auxiliaire](Sketcher_helper_constraint/fr.md) sera ajoutée si nécessaire) et les courbes seront forcées à tangenter en ce point. Ces [Sketcher contraintes auxiliaires](Sketcher_helper_constraint/fr.md) sont des contraintes ordinaires simples. Elles peuvent être ajoutées manuellement ou supprimées.

Comparée à la tangence directe, cette contrainte est plus lente, car il ya des modes de degrés de liberté invoquée, mais si le point de tangence est nécessaire, c\'est la méthode recommandée car elle offre une meilleure tanggence par rapport à tangence directe + point sur les deux courbes.

Le placement du point avant que la contrainte soit appliquée est une indication pour le calculateur pour savoir où doit se trouver la tangence. Avec cette contrainte, on peut forcer deux ellipses à se toucher en deux endroits.

### Entre deux lignes (colinéaire) 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width:600px;">

**Sélection acceptée:**

-   toute ligne/sommet + toute ligne/sommet

## Programmation

La Contrainte Tangente peut être créée à partir de [macros](Macros/fr.md) et de la console de [Python](Python/fr.md) en utilisant les éléments suivants : 
```python
# direct tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,icurve2))

# point-to-point tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2))

# tangent-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('TangentViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` où :

:\* `Sketch` est un objet d\'esquisse.

:\* `icurve1`, `icurve2` sont deux entiers identifiant les courbes à faire tangenter. Les entiers sont des index de l\'esquisse (la valeur est retournée par `Sketch.addGeometry`).

:\* `pointpos1`, `pointpos2` devrait être 1 pour point de départ et 2 pour le point de fin.

:\* `geoidpoint` et `pointpos` dans `TangentViaPoint` sont les index précisant le point de tangence.

La page [Sketcher : Écrire des scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `incurve1`, `incurve2`, `pointpos1`, `pointpos2`, `geoidpoint` et `pointpos` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainTangent/fr
