# Migrating to FreeCAD from Revit/fr
Cette page est destinée à vous permettre de démarrer rapidement avec FreeCAD si vous venez d\'Autodesk Revit.

## Mise en place 

FreeCAD est une application de modélisation 3D polyvalente. Bien qu\'il ne s\'agisse pas uniquement d\'une application BIM, il dispose de deux ateliers BIM dédiés    * l\'[atelier Arch](Arch_Workbench/fr.md), qui est fourni avec chaque installation de FreeCAD, et contient un ensemble minimal d\'outils BIM, et l\'[atelier BIM](BIM_Workbench/fr.md), que vous devez installer via le [Gestionnaire d\'Addons](Std_AddonMgr/fr.md). Il est fortement recommandé de commencer par installer l\'atelier BIM, qui vous donnera un environnement plus proche de Revit.

### Concepts clés 

Bien que vous puissiez effectuer les mêmes tâches et obtenir un résultat similaire à celui auquel vous êtes habitué dans Revit, les deux logiciels sont différents et vous devez apprendre les différences.

-   Le format de fichier Revit (.RVT) est propriétaire, non documenté, et n\'est pas supporté par FreeCAD (le supporter serait une tâche gigantesque qui engloutirait toutes les ressources de FreeCAD pour un résultat très incomplet). A la place, vous devriez vous fier à des formats ouverts tels que [IFC](Arch_IFC/fr.md), qui est plutôt bien supporté par les deux applications. Les familles peuvent également être exportées vers ACIS/SAT qui est supporté par l\'extension InventorLoader, installable via le [gestionnaire des extensions](Std_AddonMgr/fr.md).

-   Les équipements BIM tels que les fenêtres, les équipements ou le mobilier sont généralement faciles à trouver sur des sites Web populaires tels que [bimobject.com](https   *//bimobject.com) au format IFC. Mais le format ne garantit pas toujours la qualité de la géométrie. La [grabcad library](https   *//grabcad.com/library?softwares=step-slash-iges) propose une bonne sélection de ressources téléchargeables au format STEP avec une géométrie de bonne qualité.

-   La notion de famille n\'existe pas dans FreeCAD. Mais il existe de nombreuses façons d\'obtenir le même résultat, c\'est-à-dire plusieurs objets qui partagent les mêmes propriétés et sont liés entre eux (si vous en modifiez un, vous les modifiez tous). La plus simple est [clonage](Draft_Clone/fr.md). Un clone est comme une copie d\'un objet, mais si vous modifiez l\'objet original, ses clones seront également mis à jour. Mais il existe d\'autres moyens, plus subtils, de faire en sorte que les objets partagent des propriétés. Par exemple, vous pouvez dessiner un profil 2D et construire plusieurs objets à partir de ce même profil 2D.

-   Bien qu\'ils puissent être pratiques, vous n\'avez pas besoin d\'utiliser les outils BIM pour produire des objets BIM. Tout objet FreeCAD, ou même des objets réalisés avec un autre logiciel, peuvent devenir des objets BIM. Il vous suffit d\'en sélectionner un et d\'utiliser l\'outil [Composant](Arch_Component/fr.md). Cela vous permet également d\'utiliser d\'autres outils, par exemple de l\'[atelier PartDesign](PartDesign_Workbench/fr.md), pour créer des objets complexes qui sont généralement difficiles à réaliser avec les outils BIM standard.

-   Les objets créés avec un outil BIM peuvent avoir tous les types BIM supportés. Il vous suffit de modifier leur propriété **IFC Type**. Ainsi, par exemple, vous pouvez créer une poutre à l\'aide de l\'outil mur, en changeant simplement son type IFC en \"Beam\" par la suite.

-   Les outils BIM suivent la philosophie de l\'[atelier Draft](Draft_Workbench/fr.md)    * Ils peuvent être créés n\'importe où et n\'importe comment dans l\'espace 3D. Il vous suffit de définir correctement votre [plan de travail](Draft_Snap_WorkingPlane/fr.md), et les prochains objets BIM seront créés sur ce plan.

-   Il n\'y a pas de structure de bâtiment obligatoire (étages dans Revit) dans FreeCAD. Vous pouvez regrouper vos objets en utilisant des [groupes](Std_Group/fr.md), ou des [parties de bâtiment](Arch_BuildingPart.md) (qui sont généralement utilisés pour faire des niveaux, mais peuvent en fait être utilisés pour n\'importe quel type de regroupement) pour travailler de la même manière que dans Revit, mais c\'est vous qui choisissez la manière la plus appropriée pour votre projet.

### Flux de travail suggéré à adopter 

-   N\'essayez pas de migrer en une seule fois. L\'apprentissage d\'un nouveau logiciel est une tâche complexe. FreeCAD est gratuit, commencez par l\'installer et l\'explorer, puis, lorsque vous le pouvez, utilisez-le pour modéliser une petite partie d\'un projet, puis, au fur et à mesure que vous gagnez en connaissances et en maîtrise, faites de plus en plus dans FreeCAD et moins dans Revit.

-   Assurez-vous de pouvoir toujours revenir à Revit si les choses tournent mal    * exportez tôt et souvent vers l\'IFC, ouvrez le fichier dans Revit, vérifiez que tout y est.

-   La création de vues et de feuilles fonctionne comme dans Revit, si vous utilisez des vues de [Draft](Draft_Workbench/fr.md) (la méthode recommandée). Créez des [vues 2D](Draft_Shape2DView/fr.md) de vos objets ou niveaux, déplacez-les hors de votre modèle, annotez-les, placez les tout dans un groupe ou une [partie de bâtiment](Arch_BuildingPart/fr.md), puis créez des pages [TechDraw](TechDraw_Workbench/fr.md) et ajoutez-y vos vues Draft.

## Lecture complémentaire 

-   L\'[atelier BIM](BIM_Workbench/fr.md)
-   [FreeCAD BIM migration guide](https   *//yorik.uncreated.net/blog/2020-010-freecad-bim-guide)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Migrating to FreeCAD from Revit/fr
