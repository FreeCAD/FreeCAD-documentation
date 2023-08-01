# Manual:Parametric objects/fr
{{Manual:TOC/fr}}

FreeCAD est conçu pour la modélisation paramétrique. Cela signifie que la géométrie que vous créez, au lieu d\'être librement constructible, est produite par des règles et des paramètres. Par exemple, un cylindre pourrait être produit à partir d\'un rayon et d\'une hauteur. Avec ces deux paramètres, le programme contient suffisamment d\'informations pour construire le cylindre.

Les objets paramétriques, dans FreeCAD, sont en réalité de petits morceaux d\'un programme qui fonctionnent chaque fois que l\'un des paramètres a changé. Les objets peuvent avoir beaucoup de types de paramètres différents  : des nombres (nombres entiers comme 1, 2, 3 ou à virgule flottante comme 3.1416), des tailles réelles (1m m, 2.4m, 4.5ft), des coordonnées (x, y, z), des chaînes de texte (\"hello!\") ou même d'autres objets.

Ce dernier type permet de créer rapidement des chaînes d\'opérations complexes, chaque nouvel objet étant basé sur un précédent, et en ajoutant de nouvelles fonctionnalités.

Dans l\'exemple ci-dessous, un objet parallélipipédique solide (Pad) est basé sur une forme 2D rectangulaire (Sketch ou esquisse) et a une longueur d\'extrusion. Avec ces deux propriétés, il produit une forme solide en extrudant la forme de base par la distance donnée. Vous pouvez alors utiliser cet objet comme base pour d\'autres opérations, comme le dessin d\'une nouvelle forme 2D sur l\'une de ses faces (Sketch001) et puis faire une soustraction (Pocket), jusqu\'à ce que vous arriviez à votre objet final.

Toutes les opérations intermédiaires (formes 2D, pad, poche, etc.) sont toujours là, et vous pouvez toujours modifier n\'importe lequel de leurs paramètres à tout moment. Toute la chaîne sera reconstruite (recalculée) chaque fois que cela s\'avère nécessaire.

![](images/Parametric_objects.jpg )

Il est nécessaire de savoir deux choses importantes :

1.  Le recalcul n\'est pas toujours automatique. Les opérations lourdes, qui pourraient modifier une grande partie de votre document, et donc prendre un certain temps, ne sont pas exécutées automatiquement. Au lieu de cela, l\'objet (et tous les objets qui en dépendent) seront marqués pour le recalcul (une petite icône bleue apparaît sur eux dans l\'arborescence). Vous devez alors appuyer sur le bouton de recalcul (ou **Édition -> Rafraichir**) pour que tous les objets marqués soient recalculés.
2.  L\'arbre de dépendance doit toujours circuler dans la même direction. Les boucles sont interdites. (Voir [DAG](Glossary#Directed_Acyclic_Graph.md), et [DAG view](DAG_view/fr.md)) Vous pouvez avoir l\'objet A qui dépend de l\'objet B qui dépend de l\'objet C. Mais vous ne pouvez pas avoir l\'objet A qui dépend de l\'objet B qui dépend de l\'objet A. Cela serait une dépendance circulaire. Cependant, vous pouvez avoir beaucoup d\'objets qui dépendent du même objet, par exemple, les objets B et C dépendent tous deux de A. Le menu **outils → graphique de dépendance** vous montre un diagramme de dépendance comme sur l\'image ci-dessus. Ça peut être utile pour détecter les problèmes.

Tous les objets ne sont pas paramétriques dans FreeCAD. Souvent, les géométries que vous importez d\'autres fichiers ne contiennent aucun paramètre et seront des objets simples et non paramétriques. Cependant, ceux-ci peuvent souvent être utilisés comme base ou point de départ pour les objets paramétriques nouvellement créés, en fonction, bien sûr, de ce que requiert l\'objet paramétrique, et de la qualité de la géométrie importée.

Tous les objets, cependant, paramétriques ou non, auront quelques paramètres de base, comme un Nom, qui est unique dans le document et ne peut pas être édité, un label, qui est un nom défini par l'utilisateur et qui peut être édité, et un emplacement ([placement](placement.md)) qui définit sa position dans l\'espace 3D.

Enfin, il convient de noter que les objets paramétriques personnalisés sont faciles à programmer en python ([easy to program in python](Scripted_objects.md)).

**Lire plus d\'informations**

-   [L\'éditeur de propriétés](Property_editor/fr.md)
-   [Comment programmer des objets paramétriques](Scripted_objects/fr.md)
-   [Positionnement des objets dans FreeCAD](Placement/fr.md)
-   [Activation du graphe de dépendance](Std_DependencyGraph/fr.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/fr
