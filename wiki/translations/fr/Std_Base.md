# <img alt="Icône de Std Base" src=images/Freecad.svg  style="width:64px;"> Std Base/fr




## Introduction

**Std Base** n\'est pas vraiment un atelier mais plutôt une catégorie de commandes et d\'outils \"standards\" qui peuvent être utilisés dans tous les ateliers.



## Outils

La plupart des outils **Std Base** sont accessibles depuis le [menu standard](Standard_Menu/fr.md). Ceux qui ne sont disponibles que par une barre d\'outils ou un menu contextuel sont répertoriés sous la [barre d\'outils Structure](#Barre_d'outils_Structure.md) et les [outils supplémentaires](#Outils_supplémentaires.md).



### Menu standard 

Le menu standard est composé de 7 sous-menus. Chaque sous-menu a une page dédiée. Cliquez simplement sur l\'un des noms ci-dessous.


{{StdMenu
|
[Fichier](Std_File_Menu/fr.md)
&nbsp;&nbsp;&nbsp;
[Édition](Std_Edit_Menu/fr.md)
&nbsp;&nbsp;&nbsp;
[Affichage](Std_View_Menu/fr.md)
&nbsp;&nbsp;&nbsp;
[Outils](Std_Tools_Menu/fr.md)
&nbsp;&nbsp;&nbsp;
[Macro](Std_Macro_Menu/fr.md)
&nbsp;&nbsp;&nbsp;
[Fenêtre](Std_Windows_Menu/fr.md)
&nbsp;&nbsp;&nbsp;
[Aide](Std_Help_Menu/fr.md)
}}



### Barre d\'outils Structure 

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Part](Std_Part/fr.md) : crée un nouveau part et le rend actif.

-   <img alt="" src=images/Part_CoordinateSystem.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer des références 

  - <img alt="" src=images/Part_CoordinateSystem.svg  style="width:32px;"> [Créer un système de coordonnées](Part_CoordinateSystem/fr.md) : crée un objet de système de coordonnées qui peut être attaché à d\'autres objets. {{Version/fr|1.1}}

  - <img alt="" src=images/Part_DatumPlane.svg  style="width:32px;"> [Crée un plan de référence](Part_DatumPlane/fr.md) : crée un objet plan de référence qui peut être attaché à d\'autres objets. {{Version/fr|1.1}}

  - <img alt="" src=images/Part_DatumLine.svg  style="width:32px;"> [Crée une ligne de référence](Part_DatumLine/fr.md) : crée un objet ligne de référence qui peut être attaché à d\'autres objets. {{Version/fr|1.1}}

  - <img alt="" src=images/Part_DatumPoint.svg  style="width:32px;"> [Crée un point de référence](Part_DatumPoint/fr.md) : crée un objet point de référence qui peut être attaché à d\'autres objets. {{Version/fr|1.1}}

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Groupe](Std_Group/fr.md) : crée un nouveau groupe.

-   <img alt="" src=images/Std_LinkMake.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Outils de liens :

  - <img alt="" src=images/Std_LinkMake.svg  style="width:32px;"> [Créer un lien](Std_LinkMake/fr.md) : crée un lien.

  - <img alt="" src=images/Std_LinkMakeRelative.svg  style="width:32px;"> [Créer un sous-lien](Std_LinkMakeRelative/fr.md) : crée un lien vers un sous-objet ou un sous-élément.

  - <img alt="" src=images/Std_LinkReplace.svg  style="width:32px;"> [Remplacer par un lien](Std_LinkReplace/fr.md) : remplace le(s) objet(s) par un(des) nouveau(x) lien(s).

  - <img alt="" src=images/Std_LinkUnlink.svg  style="width:32px;"> [Délier](Std_LinkUnlink/fr.md) : remplace le(s) lien(s) par leur(s) objet(s) lié(s).

  - <img alt="" src=images/Std_LinkImport.svg  style="width:32px;"> [Importer des liens](Std_LinkImport/fr.md) : importe un (des) lien(s) externe(s) sélectionné(s).

  - <img alt="" src=images/Std_LinkImportAll.svg  style="width:32px;"> [Importer tous les liens](Std_LinkImportAll/fr.md) : importe tous les liens externes.

-   <img alt="" src=images/Std_VarSet.svg  style="width:32px;"> [Jeu de variables](Std_VarSet/fr.md) : crée un ensemble de propriétés qui peuvent être utilisées comme variables dans les [expressions](Expressions/fr.md). {{Version/fr|1.0}}



### Outils supplémentaires 

-   <img alt="" src=images/Std_LinkMakeGroup.svg  style="width:32px;"> [Créer un groupe de liens](Std_LinkMakeGroup/fr.md) : crée un groupe de liens.

-   [Actions sur les expressions](Std_Expressions/fr.md) :

  - [Copier la sélection](Std_Expressions/fr#Copier_la_sélection.md) : copie les données des expressions d\'objets sélectionnés dans le presse-papiers.

  - [Copier le document actif](Std_Expressions/fr#Copier_le_document_actif.md) : copie les données des expressions du document actif dans le presse-papiers.

  - [Copier tous les documents](Std_Expressions/fr#Copier_tous_les_documents.md) : copie les données des expressions de tous les documents dans le presse-papiers.

  - [Coller](Std_Expressions/fr#Coller.md) : colle les données des expressions à partir du presse-papiers.

-   <img alt="" src=images/Part_SelectFilter.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> [Filtre](Part_SelectFilter/fr.md) : {{Version/fr|1.0}}

  - <img alt="" src=images/Vertex-selection.svg  style="width:32px;"> [Sélection de sommets](Part_SelectFilter/fr#Sélection_de_sommets.md) : permet uniquement de sélectionner des sommets.

  - <img alt="" src=images/Edge-selection.svg  style="width:32px;"> [Sélection d\'arêtes](Part_SelectFilter/fr#Sélection_d'arêtes.md) : permet uniquement la sélection des arêtes.

  - <img alt="" src=images/Face-selection.svg  style="width:32px;"> [Sélection de faces](Part_SelectFilter/fr#Sélection_de_faces.md) : permet uniquement la sélection des faces.

  - <img alt="" src=images/Clear-selection.svg  style="width:32px;"> [Supprimer tous les filtres](Part_SelectFilter/fr#Supprimer_tous_les_filtres.md) : permet de sélectionner tous les sous-éléments.

-   <img alt="" src=images/Std_TreeSelectAllInstances.svg  style="width:32px;"> [Sélectionner toutes les instances](Std_TreeSelectAllInstances/fr.md) : sélectionne toutes les instances d\'un objet dans la [vue en arborescence](Tree_view/fr.md).

-   <img alt="" src=images/Std_ToggleFreeze.svg  style="width:32px;"> [Basculer le figeage](Std_ToggleFreeze/fr.md) : active/désactive le figeage des objets. Un objet figé n\'est pas recalculé lorsque ses parents changent. {{Version/fr|1.0}}



## Outils obsolètes 

-   <img alt="" src=images/View_Measure_Clear_All.svg  style="width:32px;"> [Supprimer les mesures](View_Measure_Clear_All/fr.md) : efface les mesures de [Part](Part_Workbench/fr.md). Non disponible dans {{VersionPlus/fr|1.0}}. Utilisez plutôt [Std Mesure](Std_Measure/fr.md).

-   <img alt="" src=images/View_Measure_Toggle_All.svg  style="width:32px;"> [Basculer les mesures](View_Measure_Toggle_All/fr.md) : permet de basculer l\'affichage des mesures de Part. Non disponible dans {{VersionPlus/fr|1.0}}. Utilisez plutôt [Std Mesure](Std_Measure/fr.md).

-   <img alt="" src=images/Std_MeasureDistance.svg  style="width:32px;"> [Mesurer une distance](Std_MeasureDistance/fr.md) : crée un objet pour mesurer et afficher une distance. Non disponible dans {{VersionPlus/fr|1.0}}. Utilisez plutôt [Std Mesure](Std_Measure/fr.md).





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Std Base/fr
