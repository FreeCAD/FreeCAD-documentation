---
 GuiCommand:
   Name: FEM MeshGroup
   Name/fr: FEM Collecter un maillage
   MenuLocation: Maillage , Collecter un maillage
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM MeshGroup/fr

## Description

FEM Collecter un maillage permet à l\'utilisateur de créer des collectes de sommets, arêtes, surfaces et éléments. Il est utile en cas d\'utilisation de FreeCAD comme pré-processeur pour exporter un maillage organisé et étiqueté. Le maillage est alors utilisable par des codes de résolution externes où les collectes de maillages peuvent être utilisées plus facilement pour définir les conditions aux limites et attribuer les propriétés liées au solveur. Il est possible d\'utiliser le nom de l\'objet de la collecte du maillages de FreeCAD ou l\'étiquette comme nom de la collecte lors de l\'exportation du maillage. Si l\'étiquette est choisie, l\'utilisateur doit faire attention à l\'utilisation de caractères spéciaux. Si le format d\'exportation du maillage n\'autorise pas l\'utilisation de caractères spéciaux, la solution de repli consiste à utiliser le nom de l\'objet de la collecte de maillage.

FEM Collecter un maillage permet donc à FreeCAD d\'être utilisé avec des solveurs externes (ou des visionneurs tels que ParaView) lorsqu\'ils ne sont pas encore implémentés avec leur propre routine d\'écriture de cas dans FreeCAD.



## Utilisation

1.  Pour activer la fonction, il faut d\'abord fournir un <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> [maillage de Gmsh](FEM_MeshGmshFromShape/fr.md).
2.  Ensuite, sélectionnez l\'objet Mesh dans la [vue en arborescence](Tree_view/fr.md) et
    -   Soit appuyez sur le bouton **<img src="images/FEM_MeshGroup.svg" width=24px> [Collecter un maillage](FEM_MeshGroup/fr.md)** de la barre d\'outils FEM.
    -   Soit sélectionnez l\'option **Maillage → <img src="images/FEM_MeshGroup.svg" width=24px> Collecter un maillage** du menu déroulant.
3.  Sélectionnez si la collecte est nommé ou étiqueté.
    -   Si **Nom** est sélectionné, le nom de la collecte du maillage est utilisé lors de l\'exportation du maillage.
    -   Si **Étiquette** est sélectionné, le nom de l\'étiquette spécifiée sera utilisé lors de l\'exportation du maillage.
4.  Cliquez sur le bouton **Ajouter** et sélectionnez l\'entité géométrique (solide, face, arête ou sommet). Il est possible d\'ajouter d\'autres objets de ce type, mais ils doivent être du même type. La collecte du maillage sera constituée d\'entités de maillage sous-jacentes.
5.  Cliquez sur le bouton **OK**.

    :   Résultat : vous devriez maintenant voir un nouvel objet `FEMMeshGroup` sous l\'objet `FEMMeshGMSH` dans votre conteneur d\'analyse actif.
6.  Double-cliquez sur l\'objet parent `FEMMeshGMSH` dans l\'arborescence du modèle et appuyez sur **Appliquer** pour forcer un recalcul/réétiquetage du maillage.
7.  Fermez la tâche.



## Remarques

-   Une fois que le maillage a été créé, vous pouvez modifier la propriété du label à l\'aide de l\'[éditeur de propriétés](Property_editor/fr.md).
-   Après avoir modifié une propriété, vous devez rouvrir le dialogue Gmsh et cliquer sur le bouton **Appliquer**. (Vous pouvez laisser la fenêtre de dialogue ouverte pendant la modification des propriétés).
-   Vous pouvez créer autant de collectes de maillage différentes que nécessaire.
-   Par défaut, les collectes de maillage ne peuvent être exportés qu\'aux formats .med et .unv. Pour pouvoir les exporter au format .inp, il faut activer l\'option *Exporter les données de groupe* dans les [Préférences d\'exportation INP](Import_Export_Preferences/fr#INP.md).
    -   Le fait de définir l\'option *Éléments de maillage à exporter* sur *Les plus élevés* ou *FEM* garantit que les éléments d\'ordre inférieur qui ne sont pas utilisés pour l\'analyse (par exemple, les coques dans le cas d\'une analyse avec des solides) ne seront pas exportés.
    -   Pour exporter des ensembles de nœuds dans ce format, la propriété **Groups Of Nodes** de l\'[objet maillé avec Gmsh](FEM_MeshGmshFromShape/fr.md) doit être mis à {{true}}.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshGroup/fr
