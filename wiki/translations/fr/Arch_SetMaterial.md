---
 GuiCommand:
   Name: Arch SetMaterial
   Name/fr: Arch Matériaux
   MenuLocation: Arch , Outils pour les matériaux , Matériau
   Workbenches: Arch_Workbench/fr, BIM_Workbench/fr
   Shortcut: **M** **T**
   SeeAlso: Arch_MultiMaterial/fr
---

# Arch SetMaterial/fr

## Description

Cet outil permet d\'ajouter des [matériaux](Material.md) au document actif et d\'attribuer un matériau à un objet [Arch](Arch_Workbench/fr.md). Un matériau contient toutes les propriétés d\'un certain matériau et contrôle la couleur de l\'objet auquel il est attaché. Les matériaux sont stockés dans un dossier **Materials** dans le document actif.

![](images/Arch_materials_01.jpg )



## Utilisation

1.  Sélectionnez un ou plusieurs objets pour leur attribuer un nouveau matériau.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Arch_SetMaterial.svg" width=16px> [Matériau](Arch_SetMaterial/fr.md)** dans la barre d\'outils.
    -   Utilisez les raccourcis clavier **M** puis **T**.
    -   Utilisez l\'entrée **Arch → Outils pour les matériaux → Matériau** dans le menu supérieur.
3.  Chargez un matériau prédéfini ou créez-en un nouveau en remplissant les champs.
4.  Cliquez sur le bouton **OK**.

## Options

-   Lors de la création d\'un nouveau matériau, un panneau de tâches vous permet de définir différentes options:

![](images/Arch_materials_02.jpg )

-   **Faire le choix prédéfini\...** : Choisissez un matériau prédéfini, et utilisez le tel quel, adaptez le ou modifiez le
-   **Nom** : Donnez un nom au matériau.
-   **Bouton d\'édition** : Cela ouvre le matériau actuel dans l\'[Éditeur de matériaux](FEM_MaterialEditor/fr.md) de FreeCAD qui vous permet de modifier de nombreuses propriétés supplémentaires et d\'ajouter vos propres propriétés personnalisées.
-   **Description** : Description des détails du matériau.
-   **Couleur** : Affiche les couleurs de matériau, si vous appliquez une autre couleur au matériau, tous les matériaux de ce type auront cette couleur.
-   **Couleur de la section** : Couleur d\'affichage pour le matériau, qui sera appliquée sur les pages TechDraw, lorsqu\'un objet avec ce matériau est coupé et que la propriété \"Display materials\" du plan de coupe contenant est définie sur True.
-   **Code standard** : Un nom et un numéro de spécification déterminé dans le système [Masterformat](https://en.wikipedia.org/wiki/MasterFormat) ou [Omniclass](http://www.omniclass.org/).
-   **Bouton du navigateur de code** : Pas encore implémenté - permettra d\'ouvrir la référence dans un navigateur Web.
-   **URL** : Une URL pour connaître les informations du matériau utilisé.
-   **Ouvre l\'URL dans un navigateur** : Ouvre l\'URL dans un navigateur web.



## Relation avec IFC 

Cela correspond à peu près à [IfcMaterial](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmaterial.htm).





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch SetMaterial/fr
