---
 GuiCommand:
   Name: Sketcher ConstrainRadiam
   Name/fr: Sketcher Contrainte automatique rayon/diamètre
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte automatique du rayon/diamètre
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **K** **S**
   Version: 0.20
   SeeAlso: Sketcher_ConstrainDistance/fr, Sketcher_ConstrainDistanceX/fr, Sketcher_ConstrainDistanceY/fr
---

# Sketcher ConstrainRadiam/fr

## Description

Cette contrainte contraint automatiquement la valeur du rayon/diamètre d\'un cercle ou d\'un arc à avoir une valeur spécifique. Les règles suivantes sont appliquées :

-   Si l\'objet est un pôle B-spline, une contrainte de poids est ajoutée.
-   Si l\'objet est un cercle complet, une contrainte de diamètre est ajoutée.
-   Dans les autres cas (typiquement un arc), une contrainte de rayon est ajoutée.

Si plus d\'un cercle ou d\'un arc est sélectionné avant de lancer la commande.. :

-   Si la contrainte est appliquée en mode \"Référence\", une nouvelle contrainte de référence est ajoutée à chaque objet séparément selon les règles ci-dessus.
-   Si la contrainte est appliquée en mode \"Normal\" (conduite), les règles suivantes sont appliquées
    -   Une contrainte de référence est appliquée séparément sur chaque objet qui est une géométrie externe.
    -   Des **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Contraintes égalités](Sketcher_ConstrainEqual/fr.md)** sont appliquées successivement entre tous les objets de géométrie réelle/construction et une contrainte dimensionnelle est appliquée au premier objet sélectionné selon les règles ci-dessus.

NB : les pôles des B-splines ne peuvent pas être mélangés avec d\'autres types d\'objets dans la sélection.



## Utilisation

1.  Choisissez un ou plusieurs cercles ou arcs.
2.  Appuyez sur le bouton **[<img src=images/Sketcher_ConstrainRadiam.svg style="width:16px"> [Contrainte automatique du rayon/diamètre](Sketcher_ConstrainRadiam/fr.md)**.
3.  Une boîte de dialogue s\'ouvre pour modifier ou confirmer la valeur. Appuyez sur **OK** pour valider.
4.  Il est possible de déplacer et de faire pivoter l\'étiquette et la ligne de dimension dans la vue 3D en cliquant sur la valeur et en la faisant glisser tout en maintenant le bouton gauche de la souris enfoncé.

**Remarque :** l\'outil de contrainte peut également être démarré sans sélection préalable. Par défaut, la commande sera en mode Continu pour créer de nouvelles contraintes. Appuyez une fois sur le bouton droit de la souris ou sur **Echap** pour quitter la commande.



## Script

Aucun script spécifique ne s\'applique. Voir la page [Sketcher Scripts](Sketcher_scripting/fr.md) qui explique les valeurs qui peuvent être utilisées pour `ArcOrCircle` et `Circle` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadiam/fr
