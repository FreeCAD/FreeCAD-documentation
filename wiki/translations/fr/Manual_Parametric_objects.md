# Manual:Parametric objects/fr
{{Manual:TOC}}

FreeCAD utilise une approche de modélisation paramétrique, où la géométrie des objets est régie par des règles et des paramètres sous-jacents plutôt que d\'être sculptée librement. Cela signifie que les dimensions et les caractéristiques de chaque composant sont définies par des paramètres, qui indiquent au programme comment générer la géométrie. Par exemple, pour créer un cylindre, des paramètres tels que le rayon et la hauteur sont spécifiés. Grâce à ces valeurs, FreeCAD génère la forme géométrique précise.

Dans FreeCAD, les objets paramétriques sont essentiellement de petits scripts programmables qui s\'exécutent lorsqu\'un paramètre est modifié. Ces paramètres peuvent varier considérablement, y compris les nombres entiers et les nombres à virgule flottante, les valeurs dimensionnelles réelles telles que les millimètres, les mètres ou les pieds, les coordonnées (exprimées en x, y, z), les chaînes de texte ou même les références à d\'autres objets. Cette polyvalence des paramètres permet de créer des modèles complexes par le biais d\'une série d\'opérations en chaîne où chaque nouvel objet tire ses caractéristiques d\'un objet précédent, tout en introduisant des attributs supplémentaires.

Prenons l\'exemple de la création d\'un objet cubique solide par modélisation paramétrique. Vous commencez par une forme rectangulaire de base en 2D, appelée « plaque », de longueur l et de largeur w. Cette esquisse définit la base de votre objet cubique. Ensuite, vous définissez une opération d\'« extrusion », ou « protrusion », en spécifiant la distance pour pousser ou tirer l\'esquisse dans un objet 3D. Il en résulte une forme cubique solide basée sur la forme de l\'esquisse et la distance d\'extrusion spécifiée.

<img alt="" src=images/FreeCAD_022_PArametricDesignPlate.png  style="width:600px;">

Sur la face supérieure de la plaque, vous dessinez un cercle d\'un diamètre donné d. Vous utilisez ensuite ce cercle pour créer une poche (enlever de la matière) à partir de la plaque d\'origine.

<img alt="" src=images/FreeCAD_022_ParametricDesignPocket.png  style="width:600px;">

Si vous décidez de modifier l\'une des dimensions de la plaque ou du cercle, l\'objet final sera également modifié. Grâce à l\'utilisation d\'une approche de conception paramétrique, il n\'est pas nécessaire de refaire l\'objet depuis le début.

1.  Le recalcul n\'est pas toujours automatique. Les opérations lourdes, qui pourraient modifier une grande partie de votre document, et donc prendre un certain temps, ne sont pas exécutées automatiquement. Au lieu de cela, l\'objet (et tous les objets qui en dépendent) seront marqués pour le recalcul (une petite icône bleue apparaît sur eux dans l\'arborescence). Vous devez alors appuyer sur le bouton de recalcul (ou **Édition → Rafraichir**) pour que tous les objets marqués soient recalculés.
2.  L\'arbre de dépendance doit toujours circuler dans la même direction. Les boucles sont interdites. (Voir [DAG](Glossary#Directed_Acyclic_Graph.md), et [vue DAG](DAG_view/fr.md)) Vous pouvez avoir l\'objet A qui dépend de l\'objet B qui dépend de l\'objet C. Mais vous ne pouvez pas avoir l\'objet A qui dépend de l\'objet B qui dépend de l\'objet A. Cela serait une dépendance circulaire. Cependant, vous pouvez avoir beaucoup d\'objets qui dépendent du même objet, par exemple, les objets B et C dépendent tous deux de A. Le menu **Outils → graphique de dépendance** vous montre un diagramme de dépendance comme sur l\'image ci-dessus. Ça peut être utile pour détecter les problèmes.

Dans le processus de modélisation paramétrique de FreeCAD, l\'examen de l\'arborescence de dépendance d\'un objet donne un aperçu clair de la construction séquentielle et des relations au sein d\'un modèle. Dans l\'exemple ci-dessus, la structure repose sur l\'« esquisse de plaque », qui sert de base à la forme initiale du modèle. L\'opération « Protrusion » est ensuite appliquée pour ajouter de la matière à cette esquisse fondatrice, créant ainsi une structure tridimensionnelle à partir de la base bidimensionnelle.

Ensuite, une « esquisse de cercle » est dessinée sur la surface formée. Ce cercle constitue la base de l\'opération « Cavité » suivante. Cette opération consiste à retirer stratégiquement de la matière de la structure, c\'est-à-dire à découper une partie sur la base de l\'esquisse du cercle. Ce processus d\'ajout puis de retrait de matière permet d\'intégrer des géométries et des caractéristiques complexes dans le modèle de base de manière transparente.

Grâce à cette séquence d\'opérations - en partant de l\'esquisse de base, en ajoutant du volume à l\'aide d\'une protrusion et en créant des fonctions détaillées à l\'aide d\'esquisses et de cavités supplémentaires - l\'objet final prend forme. Chaque étape de cette chaîne dépend de la précédente, illustrant la nature interconnectée de la conception paramétrique dans FreeCAD.

![](images/FreeCAD_022_ParametricDesignDependGraph.png )

Tous les objets ne sont pas paramétriques dans FreeCAD. Souvent, les géométries que vous importez d\'autres fichiers ne contiennent aucun paramètre et seront des objets simples et non paramétriques. Cependant, ceux-ci peuvent souvent être utilisés comme base ou point de départ pour les objets paramétriques nouvellement créés, en fonction, bien sûr, de ce que requiert l\'objet paramétrique, et de la qualité de la géométrie importée.

Tous les objets, cependant, paramétriques ou non, auront quelques paramètres de base, comme un Nom, qui est unique dans le document et ne peut pas être édité, un label, qui est un nom défini par l'utilisateur et qui peut être édité, et un emplacement ([placement](placement.md)) qui définit sa position dans l\'espace 3D.

Enfin, il convient de noter que les objets personnalisables paramétriques sont [faciles à programmer en Python](Scripted_objects/fr.md).

**Lire plus d\'informations**

-   [L\'éditeur de propriétés](Property_editor/fr.md)
-   [Comment programmer des objets paramétriques](Scripted_objects/fr.md)
-   [Positionnement des objets dans FreeCAD](Placement/fr.md)
-   [Graphe des dépendances](Std_DependencyGraph/fr.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/fr
