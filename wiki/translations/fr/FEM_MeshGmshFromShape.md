---
- GuiCommand:/fr
   Name:FEM MeshGmshFromShape
   Name/fr:FEM Maillage MEF à partir d'une forme avec Gmsh
   MenuLocation:Mesh → Maillage MEF à partir d'une forme avec Gmsh
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM MeshGmshFromShape/fr

## Description

Pour une analyse par éléments finis, la géométrie doit être discrétisée en [FEM Mesh](FEM_Mesh/fr.md). Cette commande utilise le programme [Gmsh](https://fr.wikipedia.org/wiki/Gmsh) (qui doit être installé sur le système) pour calculer le maillage.

Gmsh est fourni avec les binaires d\'installation de FreeCAD. Sinon, vous pouvez l\'installer séparément de FreeCAD et ensuite utiliser le menu **Édition → Préférences → FEM → Gmsh** pour définir le chemin vers le *gmsh.exe*.

## utilisation

1.  Sélectionnez la forme que vous souhaitez analyser. Pour le volume FEM, il doit s\'agir d\'un solide ou d\'un solide. Un compsolid est nécessaire si votre pièce est composée de plusieurs matériaux. (Un compsolid peut être créé avec la commande [Part Fragments booléens](Part_BooleanFragments/fr.md).)
    -   Appuyez sur le bouton **<img src="images/FEM_MeshGmshFromShape.svg" width=16px> [Créer un maillage MEF à partir de la forme avec le mailleur Gmsh](FEM_MeshGmshFromShape/fr.md)**.
    -   Sélectionnez l\'option **Mesh → <img src="images/FEM_MeshGmshFromShape.svg" width=16px> Maillage MEF à partir d'une forme avec Gmsh** dans le menu.
2.  Vous pouvez éventuellement modifier la taille minimale et maximale de l\'élément. (La détection automatique fonctionne correctement, sauf si vous appliquez des conditions aux limites compliquées.)
3.  Cliquez sur le bouton **Apply** et attendez que le calcul du maillage soit terminé.
4.  Ferme la tâche. Vous devriez maintenant voir un nouvel objet FEMMeshGMSH dans votre conteneur d\'analyse active.

Une fois que le maillage a été créé, vous pouvez modifier ses propriétés à l\'aide de l\'[Éditeur de propriétés](Property_editor/fr.md). Après avoir modifié une propriété, vous devez rouvrir le dialogue Gmsh et cliquer sur le bouton **Appliquer**. (Vous pouvez laisser la boîte de dialogue ouverte pendant la modification des propriétés).

## Propriétés

-    {{PropertyData/fr|Algorithm2D}}: algorithme permettant de créer des maillages 2D. Les différents algorithmes sont [expliqué ici](https://gmsh.info/doc/texinfo/gmsh.html#Choosing-the-right-unstructured-algorithm). Pour Delaunay, voir [triangulation de Delaunay](https://fr.wikipedia.org/wiki/Triangulation_de_Delaunay).

-    {{PropertyData/fr|Algorithm3D}}: algorithme de création de maillages 3D. Les différents algorithmes sont [expliqué ici](https://gmsh.info/doc/texinfo/gmsh.html#Choosing-the-right-unstructured-algorithm).

-    {{PropertyData/fr|Characteristic Length Max}}: taille maximale des éléments du maillage. Si elle est définie sur *0.0*, la taille sera définie automatiquement. Cette propriété peut également être modifiée dans le dialogue Gmsh dans le champ **Max element size**.

-    {{PropertyData/fr|Characteristic Length Min}}: taille minimale des éléments du maillage. Si elle est définie à *0.0*, la taille sera définie automatiquement. Cette propriété peut également être modifiée dans le dialogue Gmsh dans le champ **Min element size**.

-    {{PropertyData/fr|Coherence Mesh}}:

    -   true (par défaut) ; les noeuds de maillage dupliqués seront supprimés.
    -   false

-    {{PropertyData/fr|Element Dimension}}: dimension des éléments du maillage. Cette propriété peut également être modifiée dans le dialogue Gmsh dans le champ **Mesh element dimension**.

    -   From Shape (par défaut) ; la dimension sera déterminée à partir de la dimension de l\'objet maillé.
    -   1D
    -   2D
    -   3D

-    {{PropertyData/fr|Element Order}}: [ordre des éléments de maillage](https://www.comsol.de/support/knowledgebase/1270). Cette propriété peut également être modifiée dans le dialogue Gmsh dans le champ **Mesh order**. {{Version/fr|0.20}}

    -   1st pour 1er
    -   2nd pour 2ème (par défaut)

-    {{PropertyData/fr|Geometrical Tolerance}}: tolérance géométrique pour que le maillage corresponde aux bords de l\'objet. La valeur par défaut *0.0* signifie que la valeur par défaut de 1e-8 de Gmsh est utilisée.

-    {{PropertyData/fr|Groups Of Nodes}}: tous les noeuds et pas seulement les éléments seront sauvegardés pour chaque groupe physique de maillage. Les groupes physiques sont des collections d\'entités de maillage (points, courbes, surfaces et volumes). Ils sont identifiés par leur dimension et par un tag. Par exemple, un maillage de la même région de l\'objet est étiqueté de la même façon en interne. Ainsi, toutes les surfaces de cette région formeront un seul groupe physique.

-    {{PropertyData/fr|High Order Optimize}}: si et comment les maillages de {{Version/fr|0.20}}. Gmsh supporte différents algorithmes d\'optimisation. **Elastic** est un algorithme dans lequel les éléments du maillage sont traités comme une collection de solides viscoélastiques déformables. Les maillages de 1er ordre ne peuvent pas être optimisés car les bords des éléments sont linéaires et ne peuvent pas être déformés.

-    {{PropertyData/fr|Mesh Size From Curvature}}{{Version/fr|0.20}} : nombre d\'éléments de maillage par $2\pi$ fois le rayon de la courbure. Pour obtenir un maillage plus fin au niveau des petits coins ou des trous, cette valeur peut être augmentée pour de meilleurs résultats

<img alt="" src=images/FEM_Gmsh-MeshSizeFromCurvature.png  style="width:450px;"> 
*Effet de ''Mesh Size From Curvature''; à gauche : réglé sur 12, à droite : désactivé*.

-    {{PropertyData/fr|Optimize Netgen}}: si le maillage sera optimisé à l\'aide du générateur de maillage 3D [Netgen](https://github.com/NGSolve/netgen) pour améliorer la qualité des éléments tétraédriques. Remarque : comme Netgen ne peut créer que des éléments tétraédriques, cette option est ignorée pour les maillages dont la {{PropertyData/fr|Element Dimension}} n\'est pas *3D*.

-    {{PropertyData/fr|Recombination Algorithm}}{{Version/fr|0.20}} : algorithme utilisé pour {{PropertyData/fr|Recombine 3D All}} et également pour {{PropertyData/fr|Recombine All}}. Pour plus d\'informations, voir la section [Recombinaison d\'éléments](#Recombinaison_d.27.C3.A9l.C3.A9ments.md) et pour les détails techniques, voir la [documentation Gmsh](https://www.gmsh.info/doc/texinfo/gmsh.html#t11).

-    {{PropertyData/fr|Recombine 3D All}}{{Version/fr|0.20}} : applique un algorithme de recombinaison 3D à tous les volumes. Les tétraèdres seront recombinés en prismes, hexaèdres ou pyramides si possible.

-    {{PropertyData/fr|Recombine All}}: applique un algorithme de recombinaison à toutes les surfaces. Les triangles seront recombinés en quadrangles si possible.

-    {{PropertyData/fr|Optimize Std}}: optimise le maillage pour améliorer la qualité des éléments tétraédriques.

-    **Second Order Linear**: option si les noeuds de second ordre (si {{PropertyData/fr|Element Order}} réglé sur *2nd*) et/ou les points de raffinement du maillage sont créés par interpolation linéaire.

    -   true; l\'interpolation linéaire est utilisée.
    -   false (par défaut); l\'interpolation curviligne est utilisée.

## Remarques

### Jacobiens non positifs 

Lorsque vous obtenez une erreur de maillage à cause de Jacobiens non positifs, vous pouvez essayer les stratégies suivantes :

-   Définissez {{PropertyData/fr|Second Order Linear}} à *true* mais gardez {{PropertyData/fr|Element Order}} à *2nd*.
-   Définissez {{PropertyData/fr|Element Order}} à *1st*.
-   Utilisez une taille d\'élément plus petite en réduisant {{PropertyData/fr|Characteristic Length Max}}.
-   Si le solveur ccxtools est utilisé et que le bouton d\'exécution est utilisé (pas le panneau des tâches), les nœuds des éléments jacobiens non positifs seront verts.

### Croissance du maillage 

Aux bords et aux petites entités géométriques, le maillage doit être plus petit que dans les zones sans bords. Ainsi, la taille des éléments du maillage augmente en s\'éloignant des bords. La stratégie de croissance de Gmsh consiste à croître entre des arêtes de tailles différentes. La croissance échoue donc lorsqu\'une zone a des arêtes de même taille, comme par exemple ce tube :

<img alt="" src=images/FEM_Gmsh-MeshGrowth-failing.png  style="width:400px;"> 
*Échec de la croissance du maillage car la zone cylindrique est entourée par les mêmes bords.*

Pour permettre une croissance raisonnable du maillage, vous devez dans ce cas ajouter un bord à la zone. Dans l\'exemple, il s\'agit d\'un cercle au milieu du cylindre. Le cercle est ajouté dans le cadre d\'un composé [Part Fragments booléens](Part_BooleanFragments/fr.md) (pour former un CompSolid), voir l\'exemple de [the project file](https://forum.freecadweb.org/download/file.php?id=146255).

<img alt="" src=images/FEM_Gmsh-MeshGrowth-success.png  style="width:400px;"> 
*Croissance notable du maillage grâce à l'arête supplémentaire au milieu de l'arête cylindrique.*

### Recombinaison d\'éléments 

Les éléments peuvent être recombinés de deux manières, à la surface des objets de sorte que les triangles seront recombinés en quadrangles si possible et dans le volume des objets de sorte que les tétraèdres seront recombinés en prismes, hexaèdres ou pyramides si possible. En réfléchissant à la géométrie, il devient clair que le résultat de la recombinaison dépend fortement de la géométrie du corps et que la recombinaison d\'un corps 3D uniquement à la surface conduira le plus souvent à des résultats étranges.

Pour illustrer cela, regardez l\'image ci-dessous. Un corps cuboïde est maillé en utilisant les paramètres standards (tétraèdres, maillage de 2ème ordre). C\'est la sous-image en haut à gauche. L\'image en haut à droite montre le résultat, quand en plus les éléments sont recombinés seulement à la surface du corps. Le résultat est mauvais car les éléments de surface modifiés ne correspondent pas aux éléments de volume inchangés. Ainsi, Si nous utilisons maintenant aussi {{PropertyData/fr|Recombine 3D All}}, le résultat est meilleur, voir la sous-image en bas à gauche. Cependant, le résultat ne montre pas une grande différence par rapport au maillage sans recombinaisons. Puisque notre corps est un cuboïde, il est donc judicieux d\'utiliser un algorithme de recombinaison qui essaie de créer des cuboïdes également. Et ce résultat est montré dans la sous-image en bas à droite.

L\'algorithme de recombinaison *Simple* laissera quelques triangles dans le maillage au cas où la recombinaison conduirait à des quads de mauvaise forme. Dans ce cas, utilisez un algorithme *full-quad* de recombinaison qui effectuera automatiquement un maillage plus grossier suivi de la recombinaison, du lissage et de la subdivision. Voir le [sujet sur le forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=20351#p520392)

<img alt="" src=images/FEM_Gmsh-Recombination.png  style="width:600px;"> 
*Effet de la recombinaison des éléments du maillage. En haut à gauche : maillage standard, En haut à droite : recombinaison uniquement en surface avec l'algorithme '''Simple'''. En bas à gauche : recombinaison en surface et dans le volume avec l'algorithme ''Simple''. En bas à droite : recombinaison en surface et dans le volume avec l'algorithme '''Simple full-quad'''.*





{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM MeshGmshFromShape/fr
