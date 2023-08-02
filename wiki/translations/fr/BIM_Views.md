---
- GuiCommand:Addon/fr
   Name: BIM Views
   Name/fr: BIM Vues
   Workbenches: Image:IFC.svg BIM Workbench/fr
   Addon: BIM
   MenuLocation: Manage -> Views
---

# BIM Views/fr

## Description

Le gestionnaire de vues et de niveaux BIM est une fenêtre ancrable qui s\'ouvre sous l\'arborescence normale. Il contient tous les [Parties de bâtiment (niveaux)](Arch_BuildingPart/fr.md) et [Proxy de plan de travail](Draft_WorkingPlaneProxy/fr.md) de votre modèle.

Le but de cette fenêtre est de permettre d\'accéder rapidement à vos niveaux et configurations de plans de travail, sans avoir à naviguer dans l\'arborescence pour les retrouver.

<img alt="" src=images/BIM_views_screenshot.png  style="width:800px;">

## Utilisation

Le gestionnaire de vues BIM affichera tous les niveaux (éléments de construction) et les proxys du plan de travail de votre document. Il peut être ancré n\'importe où dans l\'interface FreeCAD ou être laissé dans une fenêtre autonome. Les éléments de construction afficheront également leur niveau (la coordonnée Z de leur placement).

-   Appuyez sur Ctrl+9 ou cliquez sur le bouton **BIM Views** dans le coin inférieur droit de l\'écran affiche ou masque le gestionnaire de vues BIM
-   Cliquez sur n\'importe quelle entrée sélectionne l\'objet correspondant
-   Double-cliquez sur la hauteur d\'un niveau vous permet de le modifier
-   Double-cliquez sur le nom d\'un objet pour définir le plan de travail et si l\'option **Restore View** de l\'objet est activée et qu\'une configuration de vue y a été stockée, ce point de vue est également restauré
-   Cliquez sur le bouton **Add a new level** crée un nouveau [étage](Arch_BuildingPart/fr.md)
-   Cliquez sur le bouton **Add a new working plane proxy** crée un nouveau [proxy de plan de travail](Draft_WorkingPlaneProxy/fr.md)
-   Cliquez sur le bouton **Delete** supprime l\'élément sélectionné
-   Cliquez sur le bouton **Toggle on/off** active/désactive un niveau sélectionné (identique à la barre d\'espace)
-   Cliquez sur le bouton **Isolate** désactive tous les niveaux sauf celui sélectionné
-   Cliquez sur le bouton **Save camera position** stocke les paramètres d\'affichage actuels dans l\'objet sélectionné, ce qui permet de le restaurer si sa propriété **Restore View** est définie sur True
-   Cliquez sur le bouton **Rename** vous permet de renommer un objet sélectionné



---
⏵ [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > BIM Views/fr
