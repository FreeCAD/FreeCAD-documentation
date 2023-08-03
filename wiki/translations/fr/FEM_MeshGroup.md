---
 GuiCommand:
   Name: FEM MeshGroup
   Name/fr: FEM Groupe de maillage FEM
   MenuLocation: Maillage , Groupe de maillage FEM
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM MeshGroup/fr

## Description

Groupe de maillage FEM permet à l\'utilisateur de créer des groupes de sommets, arêtes, surfaces et éléments. Il est utile en cas d\'utilisation de FreeCAD comme pré-processeur pour exporter un maillage organisé et étiqueté. Le maillage est alors utilisable par des codes de résolution externes où les groupes de maillage peuvent être utilisés plus facilement pour définir les conditions aux limites et attribuer les propriétés liées au solveur. Il est possible d\'utiliser le nom d\'objet du groupe de maillage FreeCAD ou l\'étiquette comme nom de groupe lors de l\'exportation du maillage. Si l\'étiquette est choisie, l\'utilisateur doit faire attention à l\'utilisation de caractères spéciaux. Si le format d\'exportation du maillage n\'autorise pas l\'utilisation de caractères spéciaux, la solution de repli consiste à utiliser le nom de l\'objet du groupe de maillage.

Groupe de maillage FEM permet donc à FreeCAD d\'être utilisé avec des solveurs externes (ou des visionneurs tels que ParaView) lorsqu\'ils ne sont pas encore implémentés avec leur propre routine d\'écriture de cas dans FreeCAD.

## Utilisation

1.  Pour activer la fonction, il faut d\'abord fournir un <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> [FEM Maillage FEM à partir d\'une forme de Gmsh](FEM_MeshGmshFromShape/fr.md).
2.  Ensuite, sélectionnez l\'objet Mesh dans la [Vue en arborescence](Tree_view/fr.md) et
    -   Soit appuyez sur le bouton <img alt="" src=images/FEM_MeshGroup.svg  style="width:24px;"> de la barre d\'outils FEM
    -   Soit sélectionnez l\'option **Maillage → <img src="images/FEM_MeshGroup.svg" width=24px> Groupe de maillage FEM** dans le menu déroulant.
3.  Sélectionnez si le groupe est nommé ou étiqueté.
    -   Si **Nom** est sélectionné, le nom du MeshGroup est utilisé lors de l\'exportation du maillage.
    -   Si **Etiquette** est sélectionné, le nom de l\'étiquette spécifiée sera utilisé lors de l\'exportation du maillage.
4.  Cliquez sur le bouton **OK**.
5.  Fermez la tâche.

    :   Résultat : Vous devriez maintenant voir un nouvel objet `FEMMeshGroup` sous l\'objet `FEMMeshGMSH` dans votre conteneur d\'analyse actif.
6.  Double-cliquez sur l\'objet parent `FEMMeshGMSH` dans l\'arborescence du modèle et appuyez sur **Appliquer** pour forcer un recalcul/réétiquetage du maillage.
7.  Fermez la tâche.

## Remarques

-   Une fois que le maillage a été créé, vous pouvez modifier la propriété du label à l\'aide de l\'[Éditeur de propriétés](Property_editor/fr.md).
-   Après avoir modifié une propriété, vous devez rouvrir le dialogue Gmsh et cliquer sur le bouton **Appliquer**. (Vous pouvez laisser la boîte de dialogue ouverte pendant la modification des propriétés).
-   Vous pouvez créer autant de groupes de mailles différents que nécessaire.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM MeshGroup/fr
