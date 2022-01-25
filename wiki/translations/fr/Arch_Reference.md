---
- GuiCommand:/fr
   Name:Arch Reference
   Name/fr:Arch Référence externe
   MenuLocation:Arch → Référence externe
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[Arch Partie de bâtiment](Arch_BuildingPart/fr.md)
---

# Arch Reference/fr

## Description

<img alt="" src=images/Arch_reference_screenshot.png  style="width:800px;">

L\'outil Référence vous permet de placer dans le document actuel un objet qui copie sa forme et ses couleurs à partir d\'un objet basé sur l\'[Atelier Part](Part_Workbench/fr.md) (y compris [Arch Partie de bâtiment](Arch_BuildingPart/fr.md)) stocké dans un autre fichier FreeCAD. Si ce fichier FreeCAD change, l\'objet de référence est marqué pour être rechargé.

## Utilisation

1.  Appuyez sur le bouton **<img src="images/Arch_Reference.svg" width=16px> '''Crééer un objet de référence externe'''**,
2.  Appuyez sur le bouton \"Choisir un fichier\...\" et sélectionnez un fichier FreeCAD existant,
3.  Sélectionnez l\'un des objets à base de pièce inclus dans la liste déroulante,
4.  Appuyer sur **OK**.

## Options

-   L\'objet de référence peut être déplacé et pivoté, la position actuelle sera conservée après le rechargement de l\'objet.
-   Si l\'objet original est déplacé dans le fichier contenant, ce mouvement sera reflété dans l\'objet de référence.
-   En cliquant avec le bouton droit de la souris sur un objet de référence dans l\'arborescence, vous avez le choix entre recharger l\'objet d\'origine ou ouvrir le fichier qui le contient.
-   Pour référencer plusieurs objets à la fois, placez-les dans un [Arch Partie de bâtiment](Arch_BuildingPart/fr.md).
-   Lorsque vous désactivez la propriété de vue **Update Colors** de la référence, les couleurs d\'origine ne sont plus rechargées, vous pouvez donc les modifier en toute sécurité.

## Propriétés

-    {{PropertyData/fr|File}}: fichier de base sur lequel ce composant est construit

-    {{PropertyData/fr|Part}}: la partie à utiliser à partir du fichier de base.

-    {{PropertyView/fr|Update Colors}}: Si la valeur est true, les couleurs du fichier lié seront mises à jour.

## Script

L\'outil Reference peut être utilisé à l\'intérieur d\'une [macro](macros/fr.md), et à partir de la console Python, en utilisant la fonction suivante : 
```python
makeReference ([file_path,object_name])
```

crée un objet de référence à partir de l\'objet donné dans le fichier donné.

Exemple: 
```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd","myPart")
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Reference/fr
