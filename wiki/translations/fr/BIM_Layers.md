---
 GuiCommand:
   Name: BIM Layers
   Name/fr: BIM Calques
   MenuLocation: Gestion , Gérer les calques...
   Workbenches: BIM_Workbench/fr
---

# BIM Layers/fr

## Description

Le **Gestionnaire de calques** vous permet de gérer les [Draft Calques](Draft_Layer/fr.md). Les calques sont un type spécial de groupe qui contrôle les propriétés visuelles des objets placés à l\'intérieur. En modifiant les propriétés du calque, telles que la largeur de ligne, la couleur de ligne, la couleur de forme et la transparence, les modifications sont propagées à ses objets enfants. Les calques n\'interfèrent avec aucune autre structure FreeCAD telle que des [groupes](Std_Group/fr.md) ou des [parties de bâtiment](Arch_BuildingPart/fr.md) donc tout objet peut être à la fois partie d\'un calque et partie d\'un groupe.

<img alt="" src=images/BIM_layers_screenshot.png  style="width:600px;"> 
*Gestionnaire de calques*

Les calques sont importés et exportés de/vers [Arch IFC](Arch_IFC/fr.md) et [Draft DXF/DWG](Draft_DXF/fr.md).

Le gestionnaire de calques vous permet de gérer vos calques, d\'ajouter ou de supprimer des calques ou de modifier leurs propriétés visuelles. Pour ajouter des objets à un calque, faites-les simplement glisser dans le calque de l\'[arborescence](Tree_view/fr.md). Pour les supprimer, faites-les glisser du calque et déposez-les dans la racine du document.

## NativeIFC

Cet outil est exactement le même que l\'outil [Gestionnaire de calques](Draft_LayerManager/fr.md) et crée le même objet de calque. Il n\'y a qu\'une seule différence : il prend en charge les objets [NativeIFC](NativeIFC/fr.md) :

-   Une icône IFC indique si un calque fait partie d\'un projet IFC ou non.
-   Un bouton **Assigner à un IFC** permet de déplacer un calque vers un projet IFC et de la transformer ainsi en calque IFC.



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Layers/fr
