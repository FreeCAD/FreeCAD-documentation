# Sketcher helper constraint/fr
## Présentation

<img alt="Exemple d\'une contrainte d\'aide (Contrainte5 : point sur le cercle) pour une contrainte de tangence (Contrainte6 : en mode tangent-via-point). Une seule contrainte d\'aide est utilisée dans ce cas, puisque le point de tangence est le point d\'extrémité du diamètre principal de l\'ellipse, qui se trouve par nature sur l\'ellipse." src=images/Sketcher_helper_constraint_example1.png  style="width:500px;">

Une Contrainte d\'aide est une contrainte d\'esquisse qui est nécessaire en tant que partie d\'une contrainte plus complexe, mais qui est exposée dans l\'interface utilisateur pour aider à gérer la redondance. Par exemple, pour la [Sketcher Contrainte de réfraction](Sketcher_ConstrainSnellsLaw/fr.md), les deux lignes qui représentent les rayons lumineux doivent être connectées ([Sketcher Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md)) et la jonction doit se trouver sur l\'interface ([Sketcher Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md)).

Les Contraintes d\'aide sont ajoutées automatiquement lorsqu\'elles sont nécessaires. La décision de savoir si elles sont nécessaires est actuellement prise en évaluant l\'erreur de contrainte de l\'assistant pour l\'état actuel de la géométrie (cela peut changer dans les futures versions). Si l\'erreur est suffisamment petite, la contrainte est considérée comme inutile et n\'est pas ajoutée. Dans certains cas, cette logique peut entraîner des erreurs (la contrainte peut être satisfaite par accident, ce qui peut facilement se produire lorsque l\'aimantation à la grille de Sketcher est activé).

Si cela se produit (une Contrainte d\'aide est manquante et les conditions requises ne sont pas satisfaites dans le cas contraire), la contrainte complexe sera rompue. Cela fera quelque chose, mais le comportement réel n\'est pas défini. Une telle contrainte défaillante peut être réparée en ajoutant manuellement la contrainte auxiliaire manquante.

Des Contraintes d\'aide sont actuellement requises pour:

-   [Sketcher Contrainte tangente ou colinéaire](Sketcher_ConstrainTangent/fr.md) (en mode tangent-via-point, deux contraintes point-sur-objet sont nécessaires)
-   [Sketcher Contrainte perpendiculaire](Sketcher_ConstrainPerpendicular/fr.md) (en mode perpendiculaire-via-point, deux contraintes point-sur-objet sont nécessaires)
-   [Sketcher Contrainte angulaire](Sketcher_ConstrainAngle/fr.md) (en mode angle-par-point, deux contraintes point-sur-objet sont nécessaires)
-   [Sketcher Contrainte de réfraction](Sketcher_ConstrainSnellsLaw/fr.md) (contrainte coïncidente et contrainte point-sur-objet sont nécessaires)



## Script

Lorsque des contraintes nécessitant des aides sont ajoutées à partir de Python, aucune contrainte d\'aide n\'est automatiquement ajoutée. On peut répliquer la prise de décision automatique des commandes de l\'interface utilisateur dans un script en testant les fonctions suivantes, spécifiquement ajoutées dans le but et utilisées dans les routines de l\'interface utilisateur:


```python
Sketch.isPointOnCurve(icurve,x,y)
```


{{Incode|isPointOnCurve}}

teste si un point virtuel, donné par les coordonnées de l\'esquisse {{Incode|x,y}} (valeurs flottantes), se trouve satisfaire une contrainte de point virtuel sur objet, c\'est-à-dire se trouve sur la courbe spécifiée par l\'indice de courbe {{Incode|icurve}}. Retourne True si le point se trouve sur la courbe, et False dans le cas contraire.


```python
Sketch.calculateConstraintError(iconstr)
```


{{Incode|calculateConstraintError}}

évalue une fonction d\'erreur d\'une contrainte spécifiée par son index {{Incode|iconstr}} dans l\'esquisse. S\'il n\'y a qu\'une seule fonction d\'erreur dans la contrainte, la valeur de retour est la valeur de retour signée de la fonction d\'erreur. S\'il y a plus d\'une fonction d\'erreur associée à la contrainte (c\'est-à-dire que la contrainte supprime plus d\'un degré de liberté), la valeur de retour est la valeur efficace de toutes les fonctions d\'erreur (toujours positive).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher helper constraint/fr
