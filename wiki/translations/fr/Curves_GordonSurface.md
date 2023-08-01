---
- GuiCommand:
   Name:Curves GordonSurface
   Name/fr:Curves Surface de Gordon
   MenuLocation:Surfaces - Gordon surface
   Workbenches:[Curves](Curves_Workbench/fr.md)
---

# Curves GordonSurface/fr

## Description

<img alt="" src=images/Curves_GordonSurface.svg  style="width:24px;"> [Surface de Gordon](Curves_GordonSurface/fr.md) crée une surface qui enveloppe un réseau de courbes. Cet outil fait partie des [ateliers externes](External_workbenches/fr.md) appelé [Curves](Curves_Workbench/fr.md).

<img alt="" src=images/GordonSurf-1.png  style="width:800px;">



## Utilisation

1.  Une surface Gordon nécessite un réseau de lignes ou de courbes qui créent un réseau de support pour la surface.
    -   La surface sera \"tendue\" entre et au-dessus de ces lignes.
2.  Dans l\'exemple ci-dessus, les lignes bleues (ou nervures) représentent la forme de la surface en différents points le long de la surface.
    -   Ceux-ci peuvent être considérés comme des coupes transversales le long de la surface. Ou, comme des supports sur lesquels la surface «tente».
3.  Les lignes jaunes représentent l\'étendue et la forme de la surface entre les sections transversales (\"nervures\") définies par les lignes bleues.
4.  Ces lignes (bleues et jaunes) peuvent être créées dans des croquis.
    -   Les esquisses contenant les nervures bleues ont généralement un décalage de placement.
        -   Chaque \"nervure\" est dans un croquis séparé.
    -   Les esquisses contenant les lignes d\'étendue/forme (jaunes) référenceront généralement la géométrie externe à partir des esquisses de \"nervure\" pour un positionnement précis.
5.  Celles-ci doivent être créées avant l\'étape suivante.
6.  Basculez vers <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench/fr.md) (installez à partir du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) est nécessaire s\'il n\'est pas déjà installé)
7.  Sélectionnez maintenant toutes les lignes qui définiront la surface.
8.  L\'ordre de sélection définit l\'ordre de couture ou de tente.
9.  Utilisez la sélection multiple pour sélectionner toutes les lignes définissant la surface. (Faites un clic gauche tout en maintenant la touche Ctrl enfoncée.)
10. Sélectionnez d\'abord les côtes, dans l\'ordre. (Dans l\'exemple ci-dessus, sélectionnez les lignes bleues de gauche à droite ou de droite à gauche.)
11. Continuez à maintenir la touche Ctrl enfoncée et sélectionnez les lignes d\'étendue. (Lignes jaunes dans l\'exemple ci-dessus.)
12. Pour appeler la commande, effectuez l\'une des opérations suivantes:
    -   Appuyez sur le bouton <img alt="" src=images/Curves_GordonSurface.svg  style="width:24px;">
    -   Utilisez **Surfaces → Gordon surface**



## Propriétés

-    {{PropertyData/fr|Placement}}: peut être utilisé pour ajuster le placement de la surface Gordon résultante. Voir: [Placement](Placement/fr.md)

    -   Remarque: Les propriétés Placement n\'ajuste pas le placement des courbes/lignes utilisées pour créer la surface, uniquement la surface.

-    {{PropertyData/fr|Label}}: étiquette (nom) spécifiée par l\'utilisateur pour la surface. (Par défaut: Gordon)

-    {{PropertyData/fr|Output}}: définit le type de sortie. (par défaut: Surface, Options: Surface, Wireframe)

-    {{PropertyData/fr|Gordon>Max Ctrl Pts}}: (Par défaut: 80)

-    {{PropertyData/fr|Gordon>Sources}}: lignes sélectionnées par l\'utilisateur qui sont utilisées pour créer la surface de Gordon.

-    {{PropertyData/fr|Gordon>Tol3D}}: tolérance 3D (par défaut: 0,01)

-    {{PropertyData/fr|Wireframe>Samples U}}: Nombre d\'échantillons dans la direction U. (par défaut: 16)

    -   Cette valeur est utilisée pour déterminer la densité du maillage lorsque la propriété Output est définie sur Wireframe.

-    {{PropertyData/fr|Wireframe>Samples V}}: Nombre d\'échantillons dans la direction V. (par défaut: 16)

    -   Cette valeur est utilisée pour déterminer la densité du maillage lorsque la propriété Output est définie sur Wireframe.
    -   Surface Gordon en mode fil de fer, U=16, V=16

<img alt="" src=images/GordonSurf-wireframe.png  style="width:600px;">



## Remarques

-   Les courbes de chaque groupe (nervures et rails) doivent toucher toutes les courbes de l\'autre groupe.
-   En d\'autres termes, elles doivent former une grille ou un motif de réseau comme indiqué ici:

<img alt="" src=images/grid.png  style="width:200px;">

-   En général, la normale à la surface de la surface Gordon résultante sera déterminée par la direction des nervures.

Dans cet exemple, la surface à gauche, les rails ont été dessinés de +Y à -Y et la normale de surface résultante est +Z
Sur la droite, les nervures sont dessinées de -Y à +Y, ce qui donne la surface normale orientée -Z.

<img alt="" src=images/Normals_shown.png  style="width:600px;">

-   [Part Extrusion](Part_Extrude/fr.md) peut être utilisé pour créer un solide à partir de la surface.

-   [PartDesign Protrusion](PartDesign_Pad/fr.md) peut également créer un solide à partir de la surface. Faire glisser la surface dans un corps crée une [Fonction de base](PartDesign_Body/fr#Fonction_de_base.md) qui peut ensuite être protusée.

## Limitations

A faire



## Script





{{Curves Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves GordonSurface/fr
