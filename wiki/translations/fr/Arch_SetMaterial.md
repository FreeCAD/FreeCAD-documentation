---
- GuiCommand:/fr
   Name:Arch SetMaterial
   Name/fr:Arch Matériaux
   MenuLocation:Arch → Outils matériaux → Matériau
   Workbenches:[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   Shortcut:**M** **T**
   SeeAlso:[Arch Outils matériaux](Arch_CompSetMaterial/fr.md), [Arch Matériaux multiples](Arch_MultiMaterial/fr.md)
---

# Arch SetMaterial/fr

## Description

L\'outil Matériau permet d\'ajouter des [matériaux](Material/fr.md) dans le document actif et attribue un matériau à un objet [Arch](Arch_Workbench/fr.md). Les matériaux peuvent prendre toutes les propriétés d\'un certain matériel, et contrôler la couleur de l\'objet auquel il est attaché. Les données sont stockées dans le dossier **Matériaux** dans le document actif.

![](images/Arch_materials_01.jpg )

## Utilisation

1.  Sélectionnez un ou plusieurs objets pour leur attribuer un nouveau matériau.
2.  Appelez la commande de plusieurs manières:
    -   Appuyez sur le bouton **<img src="images/Arch_SetMaterial.svg" width=16px> [Matériau](Arch_SetMaterial/fr.md)** dans la barre d\'outils.
    -   Utilisez les raccourcis clavier **M** puis **T**.
    -   Utilisez l\'entrée **Arch → Outils matériaux → Matériau** dans le menu supérieur.
3.  Chargez un matériau prédéfini ou créez-en un nouveau en remplissant les champs.
4.  Cliquez sur le bouton **OK**.

## Options

-   Lors de la création d\'un nouveau matériau, un panneau de tâches vous permet de définir différentes options:

![](images/Arch_materials_02.jpg )

-   **Choose preset**: Choisissez un matériau prédéfini, et utilisez le tel quel, adaptez le ou modifiez le
-   **Name**: Donnez un nom au matériau.
-   **Edit button**: Cela ouvre le matériau actuel dans l\'[Editeur de matériaux](Material_editor/fr.md) de FreeCAD qui vous permet de modifier de nombreuses propriétés supplémentaires et d\'ajouter vos propres propriétés personnalisées.
-   **Description**: Description des détails du matériau.
-   **Color**: Affiche les couleurs de matériau, si vous appliquez une autre couleur au matériau, tous les matériaux de ce type auront cette couleur.
-   **Section Color**: Couleur d\'affichage pour le matériau, qui sera appliquée sur les pages TechDraw, lorsqu\'un objet avec ce matériau est coupé et que la propriété \"Display materials\" du plan de section contenant est définie sur True .
-   **Code**: Un nom et un numéro de spécification déterminé dans le système [Masterformat](https://en.wikipedia.org/wiki/MasterFormat) ou [Omniclass](http://www.omniclass.org/).
-   **Code browser button**: Pas encore implémenté - permettra d\'ouvrir la référence dans un navigateur Web.
-   **URL**: Une URL pour connaître les informations du matériau utilisé.
-   **URL button**: Ouvre l\'URL dans un navigateur web.

## Relation avec IFC 

Cela correspond à peu près à [IfcMaterial](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmaterial.htm).

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SetMaterial/fr
