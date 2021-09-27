# <img alt="Icône de l\'atelier OpenSCAD" src=images/Workbench_OpenSCAD.svg  style="width:64px;"> OpenSCAD Workbench/fr

## Introduction

L\'<img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> _, qui est le noyau géométrique que FreeCAD utilise pour créer la géométrie à l\'écran. Les bibliothèques OpenCASCADE sont toujours nécessaires pour utiliser FreeCAD tandis que l\'exécutable OpenSCAD est entièrement facultatif.

Il contient un importateur [CSG](OpenSCAD_CSG/fr.md) pour ouvrir les fichiers CSG créés par OpenSCAD et un exportateur pour générer une arborescence basée sur CSG. Les géométries non basées sur des opérations CSG seront exportées sous forme de maillage.

Cet atelier contient des fonctions permettant de modifier l\'arborescence des éléments CSG et de réparer les modèles. Il contient également des outils d\'usage général qui ne nécessitent pas l\'installation d\'OpenSCAD et peuvent être utilisés conjointement avec d\'autres ateliers. Par exemple, l\'[Atelier Mesh](Mesh_Workbench/fr.md) utilise en interne les fonctions OpenSCAD pour effectuer des opérations avec de [maillage](mesh/fr.md) car elles sont assez robustes.


{{TOCright}}

![](images/OpenSCADexamaple1.png )

## Dépendances

Dans FreeCAD 0.19, le module Ply (Python-Lex-Yacc), qui est utilisé pour importer des fichiers CSG, a été supprimé du code source de FreeCAD, car il s\'agit d\'une bibliothèque tierce non développée par FreeCAD. Par conséquent, vous devez maintenant installer Ply avant d\'utiliser OpenSCAD Workbench. Lorsque vous utilisez une version pré-packagée et stable de FreeCAD, cette dépendance doit être installée automatiquement sur toutes les plates-formes. Dans d\'autres cas, par exemple, lorsque vous voulez [compiler](Compiling/fr.md) à partir de la source, vous devrez peut-être l\'installer à partir d\'un référentiel en ligne.


{{Userdocnavi/fr}}


```python
sudo zypper install python3-ply
```

Sur les systèmes basés sur Debian/Ubuntu, cela se fait de la manière suivante : 
```python
sudo apt install python3-ply
```

L\'installation générale sur toutes les plates-formes peut être effectuée à partir de l\'index du package Python. 
```python
pip3 install --user ply
```

## Langage OpenSCAD et format de fichier 

Le langage [OpenSCAD](http://www.openscad.org/) permet l\'utilisation de variables et de boucles. Il permet de spécifier les sous-modules pour réutiliser le code et les formes géométriques. Cette grande flexibilité, rend l\'analyse très complexe. Actuellement le module **OpenSCAD de FreeCAD** ne permet pas de gérer le langage OpenSCAD nativement. Au contraire, si **OpenSCAD** est installé, il est utilisé pour compiler l\'entrée dans un format de sortie nommé **CSG**. C\'est un sous-ensemble du langage d\'OpenSCAD et peut être utilisé comme entrée de **OpenSCAD** pour un traitement ultérieur. Cependant dans cette étape de la compilation, tous les comportements paramétriques sont perdus. Tous les noms de variables seront écartés, les boucles sont élargies et les expressions mathématiques sont évaluées.

## Outils

-   <img alt="" src=images/OpenSCAD_ColorCodeShape.svg  style="width:32px;"> [ColorCodeShape](OpenSCAD_ColorCodeShape/fr.md) : Change la couleur de la sélection, ou toutes les formes en fonction de leurs validités.
-   <img alt="" src=images/OpenSCAD_ReplaceObject.svg  style="width:32px;"> [Remplacement d\'un objet](OpenSCAD_ReplaceObject/fr.md) : Remplace un objet dans l\'arborescence des éléments.
-   <img alt="" src=images/OpenSCAD_RemoveSubtree.svg  style="width:32px;"> [Suppression de l\'arborescence](OpenSCAD_RemoveSubtree/fr.md) : Supprime les objets sélectionnés, et toute leur descendance non référencée depuis d\'autres objets.
-   <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:32px;"> [Affinage de la forme](OpenSCAD_RefineShapeFeature/fr.md) : Crée et affine les caractéristiques de la forme.
-   <img alt="" src=images/OpenSCAD_MirrorMeshFeature.svg  style="width:32px;"> [Maillage miroir](OpenSCAD_MirrorMeshFeature/fr.md): Crée un maillage en miroir.
-   <img alt="" src=images/OpenSCAD_ScaleMeshFeature.svg  style="width:32px;"> [Mettre à l\'echelle](OpenSCAD_ScaleMeshFeature/fr.md): Changer d\'echelle un maillage.
-   <img alt="" src=images/OpenSCAD_ResizeMeshFeature.svg  style="width:32px;"> [Redimensionner le maillage](OpenSCAD_ResizeMeshFeature/fr.md): Redimensionne le maillage.
-   <img alt="" src=images/OpenSCAD_IncreaseToleranceFeature.svg  style="width:32px;"> [Augmenter la tolérance](OpenSCAD_IncreaseToleranceFeature/fr.md) : Augmente la tolérance des arêtes/faces/sommets des objets sélectionnés.
-   <img alt="" src=images/OpenSCAD_Edgestofaces.svg  style="width:32px;"> [Convertir des arêtes en faces](OpenSCAD_Edgestofaces/fr.md) : Converti les Bords en Faces. Utile pour préparer les formes géométriques **DXF** importées, pour les extruder.
-   <img alt="" src=images/OpenSCAD_ExpandPlacements.svg  style="width:32px;"> [Développer les placements](OpenSCAD_ExpandPlacements/fr.md) : Développe toutes les éléments vers le bas de l\'arborescence.
-   <img alt="" src=images/OpenSCAD_ExplodeGroup.svg  style="width:32px;"> [Dégrouper](OpenSCAD_ExplodeGroup/fr.md): Dégroupe les primitives des pièces fusionnées.
-   <img alt="" src=images/OpenSCAD_AddOpenSCADElement.png  style="width:32px;"> [Ajout d\'un élément OpenSCAD](OpenSCAD_AddOpenSCADElement/fr.md) : Ajoute un élément OpenSCAD en entrant le code OpenSCAD dans le panneau de tâches et exécute le binaire OpenSCAD (OpenSCAD doit être installé sur votre ordinateur) Remarque: Cet icône ne s\'affiche pas (même si OpenSCAD est installé sur votre ordinateur), vous devez également configurer FreeCAD. [Voir ici pour plus de détails](https://sourceforge.net/apps/mediawiki/free-cad/index.php?title=OpenSCAD_AddOpenSCADElement#Initial_set_up_from_within_FreeCAD)
-   <img alt="" src=images/OpenSCAD_MeshBoolean.svg  style="width:32px;"> [Maillage à partir d\'opération booléenne](OpenSCAD_MeshBoolean/fr.md) : Crée un nouvel objet maille avec une opération booléenne à partir de plusieurs formes.
-   <img alt="" src=images/OpenSCAD_Hull.svg  style="width:32px;"> [Enveloppe convexe](OpenSCAD_Hull/fr.md) : Applique une coque aux formes sélectionnées.
-   <img alt="" src=images/OpenSCAD_Minkowski.svg  style="width:32px;"> [Somme de Minkowski](OpenSCAD_Minkowski/fr.md) : Applique une somme de Minkowski aux formes sélectionnées.

## Préférences

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Préférences\...](OpenSCAD_Preferences/fr.md): préférences disponibles dans OpenSCAD Tools.

## Limites

OpenSCAD permet la construction de formes géométriques solides, comme l\'importation de fichiers de maillage et d\'extrusion géométriques 2d à partir de fichiers _ ne l\'est généralement pas.

OpenSCAD fonctionne en interne avec les maillages (mesh). Certaines opérations qui sont utiles sur les maillages ne sont pas significatives sur un modèle BREP et peuvent ne pas être entièrement supporté. Parmi celle-ci figurent le recouvrement convexe, la somme de Minkowski, glide et subdiv. Pour l'instant OpenSCAD est exécuté pour réaliser le recouvrement convexe et la somme de Minkowski et importer le résultat. Cela signifie que la géométrie impliquée sera triangulée. Avec OpenSCAD la mise à l'échelle non uniforme est souvent utilisée, ce qui ne pose pas de problèmes avec les maillages. Avec notre noyau géométrique, les formes primitives (lignes, sections circulaires, etc) sont converties en BSpline avant d'être déformées. Ces BSplines sont connues pour poser problèmes avec des opérations booléennes futures. Une solution automatique n'est pas disponible pour le moment. S'il vous plaît n'hésitez pas à poster sur le [forum](http://forum.freecadweb.org/) si vous rencontrez ce genre de problème. Souvent ce genre de problèmes peut être résolu en modélisant des parties plus petites. Une déformation d'un cylindre peut être remplacée par l'extrusion d'une ellipse.

## Conseils

Lors de l\'importation du fichier [DXF](DXF/fr.md), il faut définir la précision du projet à une valeur raisonnable, car cela aura une incidence sur la détection des arêtes connectées.

Si FreeCAD se bloque lors de l\'importation de CSG, il est fortement recommandé d\'activer la case à cocher *Vérifier les modèles automatiquement après une opération booléenne* dans le menu **Édition → Préférences → Conception de pièces → Général → Paramètres de modèle**

## Tutoriels

-   [Importer code OpenSCAD](Import_OpenSCAD_code/fr.md)

## Liens

-   Dépôt du code source d\'OpenSCAD [GitHub](https://github.com/openscad/openscad)
-   [Open tickets tagged \"Openscad\" sur le FreeCAD bugtracker](https://freecadweb.org/tracker/search.php?tag_string=OpenSCAD)
-   [Plus de renseignements au sujet d\'Openscad sur Thingiverse](http://www.thingiverse.com/tag:openscad)





{{OpenSCAD Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > OpenSCAD Workbench/fr
