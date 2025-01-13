# Release notes 1.1/fr
**FreeCAD 1.1 est en cours de développement, il n'y a pas encore de date de sortie prévue.**


{{Message|Des fonctions sont manquantes? Faites en part dans le fil du forum [https://forum.freecad.org/viewtopic.php?f&#61;10&t&#61;92080 Release notes for v1.1].

Voir [Contribuer à FreeCAD](Help_FreeCAD/fr.md) pour savoir comment contribuer à FreeCAD.
}}


{{Message|Toutes les images de cette page doivent utiliser le suffixe **_relnotes_1.1**}}




**FreeCAD 1.1** a été publié le **JJ MM AA**, téléchargez la depuis la page [Téléchargement](Download/fr.md). Cette page liste toutes les nouvelles fonctions et les changements.

Les notes de versions plus anciennes de FreeCAD sont disponibles dans la [liste des notes de versions](Feature_list/fr#Notes_de_versions.md).

L\'endroit pour une image évocatrice sélectionnée par les administrateurs sur le [forum des modèles des utilisateurs](https://forum.freecad.org/viewforum.php?f=24).



## Général



## Interface utilisateur 



### Autres améliorations de l\'interface utilisateur 

-   Un raccourci par défaut pour [Std Préférences](Std_DlgPreferences/fr.md) a été ajouté. [Pull request #15536](https://github.com/FreeCAD/FreeCAD/pull/15536)
-   La page des préférences de la zone de notification a été améliorée. [Pull request #15207](https://github.com/FreeCAD/FreeCAD/pull/15207)
-   Les fonctions de sauvegarde automatique et de sélection additive ont été ajoutées à l\'outil [Mesurer](Std_Measure/fr.md). [Pull request #17717](https://github.com/FreeCAD/FreeCAD/pull/17717)



## Noyau et API 



### Noyau

+++
| <img alt="" src=images/Core_datums_relnotes_1.1.png  style="width:384px;"> | Les outils Core Datum ont été implémentés pour créer des systèmes de coordonnées, des plans de référence, des lignes de référence et des points de référence qui peuvent être attachés et utilisés dans Assembly. [Pull request #18332](https://github.com/FreeCAD/FreeCAD/pull/18332) |
+++

   
  <img alt="" src=images/Core_Transform_relnotes_1.1.gif  style="width:384px;">Cliquez sur l\'image si l\'animation ne démarre pas.   L\'outil [Transformer](Std_TransformManip/fr.md) a été remanié et permet désormais d\'effectuer des saisies précises en plus du déplacement dans la vue 3D. Il est possible d\'aligner le curseur interactif sur n\'importe quel élément du document et de transformer l\'objet dans le système de coordonnées local (U, V, W) du curseur ou dans le système de coordonnées global du document. Le curseur peut être aligné sur l\'origine de l\'objet comme auparavant, ainsi que sur le centre de masse de l\'objet. Une nouvelle fonctionnalité permet de déplacer l\'objet (à l\'emplacement du dragueur) vers un emplacement cible dans le document et d\'en inverser l\'orientation. [Pull request #17564](https://github.com/FreeCAD/FreeCAD/pull/17564)
   

### API



#### Suppression d\'API Python 



#### API en Python modifiées 



#### Nouvelles API en Python 

## Start



## Gestionnaire des extensions 



## Atelier Assembly 

-   L\'outil [Nouvelle pièce](Assembly_InsertNewPart/fr.md) a été ajouté, ce qui permet d\'ajouter facilement de nouvelles pièces à l\'assemblage. [Pull request #17922](https://github.com/FreeCAD/FreeCAD/pull/17922)
-   L\'outil [Simulation](Assembly_CreateSimulation/fr.md) a été ajouté, ce qui permet d\'ajouter des mouvements aux liaisons et de créer des animations. [Pull request #16414](https://github.com/FreeCAD/FreeCAD/pull/16414)



### Autres améliorations d\'Assembly 

-   Les nouvelles données de base peuvent être utilisées pour attacher des liaisons afin d\'assembler des pièces multiples. [Pull request #18332](https://github.com/FreeCAD/FreeCAD/pull/18332)



## Atelier BIM 



### Autres améliorations de BIM 

-   Le panneau de [BIM Gérer les vues BIM](BIM_Views/fr.md) a été remanié et comporte désormais une section pour toutes les vues 2D. [Pull request #15836](https://github.com/FreeCAD/FreeCAD/pull/15836)
-   La prise en charge de NativeIFC pour les objets 2D a été ajouté à BIM, permettant d\'incorporer des objets 2D (lignes, textes, dimensions) dans des fichiers IFC, ainsi que d\'ouvrir de tels fichiers à partir d\'autres applications BIM. [Pull request #16629](https://github.com/FreeCAD/FreeCAD/pull/16629)



## Atelier CAM 



### Autres améliorations de CAM 

-   Les opérations de taraudage G84/G74 ont été ajoutées. [Pull request #8069](https://github.com/FreeCAD/FreeCAD/pull/8069)
-   La prise en charge multi-passe a été ajoutée pour les opérations de profilage. [Pull request #17326](https://github.com/FreeCAD/FreeCAD/pull/17326)



## Atelier Draft 



### Autres améliorations de Draft 

-   La prise en charge des chemins relatifs des polices a été ajoutée à [Forme à partir d\'un texte](Draft_ShapeString/fr.md). [Pull request #17819](https://github.com/FreeCAD/FreeCAD/pull/17819)
-   La commande [Draft Congé](Draft_Fillet/fr.md) fonctionne désormais sur les arêtes sélectionnées, au lieu de la première arête des objets sélectionnés. [Pull request #17945](https://github.com/FreeCAD/FreeCAD/pull/17945) et [Pull request #18150](https://github.com/FreeCAD/FreeCAD/pull/18150)
-   Le menu des calques de la commande [Draft Groupement automatique](Draft_AutoGroup/fr.md) est trié par ordre alphabétique. [Pull request #18172](https://github.com/FreeCAD/FreeCAD/pull/18172)
-   La gestion des liens dans [TechDraw Vue d\'un objet Draft](TechDraw_DraftView/fr.md) a été corrigée. [Pull request #18175](https://github.com/FreeCAD/FreeCAD/pull/18175)
-   La position du champ *Multiplicateur d\'échelle* dans l\'interface utilisateur a été améliorée ([Draft SetStyle](Draft_SetStyle/fr.md), [Draft Éditer le style des annotations](Draft_AnnotationStyleEditor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md)). [Pull request #18299](https://github.com/FreeCAD/FreeCAD/pull/18299)



## Atelier FEM 



### Autres améliorations de FEM 

-   La verbosité des logs peut maintenant être définie pour Gmsh dans les [préférences](FEM_Preferences/fr#Gmsh.md). [Pull request #17699](https://github.com/FreeCAD/FreeCAD/pull/17699)
-   La propriété **Second Order Linear** et la prise en charge du [maillage plus fin localement](FEM_MeshRegion/fr.md), jusque là disponibles uniquement pour Gmsh, sont maintenant également disponibles pour la nouvelle implémentation de [Netgen](FEM_MeshNetgenFromShape/fr.md). [Pull request #17170](https://github.com/FreeCAD/FreeCAD/pull/17170)
-   Les types de sections de poutres-caissons et elliptiques ont été ajoutés à [FEM Coupe transversale d\'un élément 1D](FEM_ElementGeometry1D/fr.md). [Pull request #15843](https://github.com/FreeCAD/FreeCAD/pull/15843)
-   L\'outil [Purger les résultats](FEM_ResultsPurge/fr.md) supprime désormais tous les objets résultat et pas seulement ceux natifs de CalculiX. [Pull request #18328](https://github.com/FreeCAD/FreeCAD/pull/18328)
-   La [contrainte de liaison](FEM_ConstraintTie/fr.md) peut maintenant être appliquée également aux faces de coques. [Pull request #18325](https://github.com/FreeCAD/FreeCAD/pull/18325)
-   Le format de sortie (binaire ou ASCII) et la sauvegarde des ID de géométrie peuvent maintenant être définis pour Elmer, de même dans les [préférences](FEM_Preferences/fr#Elmer.md). [Pull request #17972](https://github.com/FreeCAD/FreeCAD/pull/17972)
-   Une option de lissage a été ajoutée au [filtre par contours](FEM_PostFilterContours/fr.md). [Pull request #18088](https://github.com/FreeCAD/FreeCAD/pull/18088)
-   Le paramètre *BucklingAccuracy* a été ajouté au [solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md). Il peut être nécessaire de capturer la première valeur propre dans certaines analyses de flambage linéaire. [Pull request #18790](https://github.com/FreeCAD/FreeCAD/pull/18790)
-   Maintenant tous les objets FEM pour lesquels la suppression a un sens peuvent être supprimés. Auparavant, seules les contraintes pouvaient être supprimées. [Pull request #18636](https://github.com/FreeCAD/FreeCAD/pull/18636)



## Atelier Material 



### Autres améliorations de Material 



## Atelier Mesh 



### Autres améliorations de Mesh 



## Atelier OpenSCAD 



### Autres améliorations de OpenSCAD 



## Atelier Part 



### Autres améliorations de Part 

-   L\'outil [Vérifier la géométrie](Part_CheckGeometry/fr.md) a maintenant des entrées de résultats pour les formes valides, montre les objets ignorés et génère des rapports dans la [vue rapport](Report_view/fr.md).



## Atelier PartDesign 



### Autres améliorations de PartDesign 

-   La fonction d\'origine dans un corps de PartDesign utilise les nouveaux points de référence centraux. L\'apparence a été modifiée et les plans s\'agrandissent lors de la création d\'une nouvelle esquisse. L\'orientation étant erronée dans les anciennes versions de FreeCAD, les fichiers créés avec ces versions doivent être convertis à l\'ouverture. Cela peut casser les fichiers qui font référence aux datums, et les fichiers convertis ou créés avec {{VersionPlus/fr|1.1}} seront cassés dans {{VersionMinus/fr|1.0}}. [Pull request #18126](https://github.com/FreeCAD/FreeCAD/pull/18126)
-   La commande [Basculer le figeage](Std_ToggleFreeze/fr.md) est désormais disponible dans PartDesign. [Pull request #18373](https://github.com/FreeCAD/FreeCAD/pull/18373)
-   La fonction [Perçage](PartDesign_Hole/fr.md) peut maintenant produire différents [filetages Whitworth](https://fr.wikipedia.org/wiki/British_Standard_Whitworth) suivant les normes BSW, BSF, BSP et NPT. [Pull request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)
-   Les performances des filetages modélisés à partir de la fonction [Perçage](PartDesign_Hole/fr.md) ont été améliorées. [Pull request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)
-   L\'angle initial pour les filets coniques de la fonction [Perçage](PartDesign_Hole/fr.md) est désormais automatiquement défini sur la valeur des normes ISO 7-1 et ASME B1.20.1. [Pull request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)



## Atelier Points 



### Autres améliorations de Points 



## Atelier Sketcher 

   
  <img alt="" src=images/Sketcher_defining_external_relnotes_1.1.gif  style="width:384px;">Cliquez sur l\'image si l\'animation ne démarre pas.   L\'outil [Projection](Sketcher_Projection/fr.md) a été ajouté, ce qui permet de créer une géométrie [géométrie externe](Sketcher_External/fr.md) de définition et de basculer entre les modes de définition et de construction pour la géométrie externe. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
   

+++
| <img alt="" src=images/Sketcher_intersection_relnotes_1.1.png  style="width:384px;"> | L\'outil [Intersection](Sketcher_Intersection/fr.md) a été ajouté, ce qui permet de créer une [géométrie externe](Sketcher_External/fr.md) basée sur la géométrie de référence sélectionnée et l\'intersection du plan de l\'esquisse. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736) |
+++

   
  <img alt="" src=images/Sketcher_external_faces_relnotes_1.1.gif  style="width:384px;">Cliquez sur l\'image si l\'animation ne démarre pas.   Les [géométries externes](Sketcher_External.md) (projection et intersection) peuvent désormais être créées en sélectionnant une face. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
   



### Autres améliorations de Sketcher 

-   Il est maintenant possible d\'utiliser directement une géométrie externe comme entrée pour des outils comme le décalage ou la transformation (réseau), pour les deux géométries externes construction et définition [Pull request #17615](https://github.com/FreeCAD/FreeCAD/pull/17615).
-   La géométrie externe (projetée ou intersectée) est maintenant par défaut une géométrie réelle (définissant) (qui n\'a pas besoin d\'être tracée comme dans la version 1.0 et les versions antérieures). Elle peut être transformée en géométrie de construction comme n\'importe quelle autre géométrie [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736).
-   Les axes de Sketcher sont désormais affichés avec une longueur infinie. [Pull request #17312](https://github.com/FreeCAD/FreeCAD/pull/17312)
-   Les esquisses sont désormais classées par ordre alphabétique dans la boîte de dialogue de [Ancrer une esquisse](Sketcher_MapSketch/fr.md). [Pull request #16518](https://github.com/FreeCAD/FreeCAD/pull/16518)
-   Le déplacement de groupe a été ajouté, ce qui permet de déplacer toutes les entités géométriques sélectionnées. [Pull request #18273](https://github.com/FreeCAD/FreeCAD/pull/18273)
-   Il y a une nouvelle préférence qui, si elle est cochée, rend la création de géométrie externe indépendante du mode de construction actuel. Elle est toujours créée en tant que géométrie de référence dans ce cas. [Pull request #18697](https://github.com/FreeCAD/FreeCAD/pull/18697)



## Atelier Spreadsheet 



### Autres améliorations de Spreadsheet 

-   Des raccourcis par défaut pour [Texte en gras](Spreadsheet_StyleBold/fr.md), [Texte en italique](Spreadsheet_StyleItalic/fr.md) et [Texte en souligné](Spreadsheet_StyleUnderline/fr.md) ont été ajoutés. [Pull request #15556](https://github.com/FreeCAD/FreeCAD/pull/15556)
-   Double-cliquer sur le séparateur dans l\'en-tête redimensionne maintenant la colonne en fonction du contenu. [Pull request #16296](https://github.com/FreeCAD/FreeCAD/pull/16296)
-   Le zoom a été ajouté à la feuille de calcul. [Pull request #16130](https://github.com/FreeCAD/FreeCAD/pull/16130)



## Atelier Surface 



### Autres améliorations de Surface 



## Atelier TechDraw 



### Autres améliorations de TechDraw 

-   L\'outil [Cote de surface](TechDraw_AreaDimension/fr.md) prend désormais correctement en compte les trous dans les faces. [Pull request #17740](https://github.com/FreeCAD/FreeCAD/pull/17740)
-   La validation des formes est maintenant disponible et peut être activée dans les [préférences](TechDraw_Preferences/fr#Avancé.md). [Pull request #18282](https://github.com/FreeCAD/FreeCAD/pull/18282)

## Compilation



## Limitations connues 



## Autres ressources



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.1/fr
