---
 GuiCommand:
   Name: BIM Views
   Name/fr: BIM Gérer les vues BIM
   MenuLocation: Gestion , Gérer les vues BIM
   Workbenches: BIM_Workbench/fr
---

# BIM Views/fr

## Description

La commande **BIM Gérer les vues BIM** ouvre une fenêtre ancrable sous l\'arborescence normale. Elle contient tous les [parties du bâtiment (niveaux)](Arch_BuildingPart/fr.md) et les [proxies des plans de travail](Draft_WorkingPlaneProxy/fr.md) de votre modèle.

Le but de cette fenêtre est de permettre d\'accéder rapidement à vos niveaux et configurations de plans de travail, sans avoir à naviguer dans l\'arborescence pour les retrouver.

<img alt="" src=images/BIM_views_screenshot.png  style="width:600px;"> 
*Le gestionnaire des vues BIM et des niveaux*



## Utilisation

Le gestionnaire des vues BIM affichera tous les niveaux (éléments de construction) et les proxies des plans de travail de votre document. Il peut être ancré n\'importe où dans l\'interface FreeCAD ou être laissé dans une fenêtre autonome. Les éléments de construction afficheront également leur niveau (la coordonnée Z de leur placement).

-   En appuyant sur Ctrl+9 ou en cliquant sur le bouton **Gérer les vues BIM** dans la barre d\'état, vous pouvez afficher ou masquer le gestionnaire des vues de BIM
-   Cliquez sur n\'importe quelle entrée sélectionne l\'objet correspondant
-   Double-cliquez sur la hauteur d\'un niveau permet de l\'éditer.
-   Double-cliquez sur le nom d\'un objet quelconque permet d\'y placer le plan de travail et, si la propriété **Restore View** de l\'objet est définie sur True et qu\'une configuration de vue a été stockée dans l\'objet, ce point de vue est également restauré.
-   Le gestionnaire des vues BIM dispose d\'un menu contextuel de clic droit avec les options suivantes :
    -   **Ajouter un niveau** crée un nouveau [niveau](Arch_BuildingPart/fr.md)
    -   **Ajouter un proxy** crée un nouveau [proxy de plan de travail](Draft_WorkingPlaneProxy/fr.md)
    -   **Supprimer** supprime l\'élément sélectionné
    -   **Activer/désactiver** active/désactive un niveau sélectionné (comme la barre d\'espace)
    -   **Isoler** désactive tous les niveaux à l\'exception du niveau sélectionné
    -   **Enregistrer la position de la vue** enregistre les paramètres de vue actuels dans l\'objet sélectionné, permettant de les restaurer si sa propriété **Restore View** est réglée sur True
    -   **Renommer** permet de renommer un objet sélectionné





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Views/fr
