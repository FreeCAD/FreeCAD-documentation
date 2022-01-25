---
- TutorialInfo:/fr
   Topic:Sketcher
   Level:Débutant
   Author:[Maker](User_Maker.md)
   FCVersion:
---

# Sketcher requirement for a sketch/fr





## Exigences minimales pour une esquisse 

La création d\'un corps dans l\'espace de travail PartDesign est déjà possible et **seulement** à l\'aide d\'une courbe fermée (profil). La détermination complète de toutes leurs dimensions et propriétés (*totalement contrainte*) n\'est pas encore requise.

Qu\'une courbe fermée soit présente, ne va pas de soi et n\'est pas reconnaissable. Lorsque vous connectez un arc de cercle à une ligne droite, par ex. les deux points d\'extrémité sont créés uniquement l\'un au-dessus de l\'autre. Vous devez utiliser l\'outil Contrainte <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [Coincidente](Sketcher_ConstrainCoincident/fr.md) pour créer un seul point qui relie réellement la ligne et l\'arc.

![](images/Skizze2a.png )



*Un simple croquis. 
A gauche: courbe uniquement à quatre endroits (rouge, contraintes automatiques lors du dessin avec [<img src=images/Sketcher_CreatePolyline.svg style="width:32px"> [Polyligne](Sketcher_CreatePolyline/fr.md)) fermée.
Au milieu: avertissement - ... face brisée (courbe brisée).
A droite: courbe fermée aux quatre places restantes (vert)*

Cependant, un travail paramétrique cohérent signifie que l\'esquisse est complètement déterminée.

## Définir complètement un croquis 

Même une esquisse relativement simple peut contenir des dizaines d\'indéterminations (indiquées dans la vue combinée par un nombre en \"degrés de liberté\"). Les éliminer ensemble à la fin est une tâche relativement confuse.

![](images/Skizze4a.png )



*Un simple croquis; complètement déterminé par 25 contraintes, dont seulement 5 sont des contraintes de dimension.*

Ce travail est plus clair et plus simple si l'on élimine immédiatement les \"libertés\" de chaque élément géométrique ajouté, i. ces *dimensions* (c\'est-à-dire les valeurs pour les dimensions et les emplacements). L\'intégralité provisoire est atteinte si toutes les lignes sont affichées en vert.

Si vous attendez la fin du dessin pour déterminer, vous trouvez les \"libertés\" restantes en touchant les points et les lignes avec le pointeur de la souris et en déterminant où ils ne sont pas encore fixés. Une fois terminé, tout le dessin est affiché en vert.

Si vous créez accidentellement une \"surmodulation\", un avertissement apparaît dans la vue combinée vous demandant d\'annuler les actions correspondantes (contraintes).


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher requirement for a sketch/fr
