---
 GuiCommand:
   Name: Arch Reference
   Name/fr: Arch Référence externe
   MenuLocation: 3D/BIM , Outils 3D génériques , Référence externe
   Workbenches: BIM_Workbench/fr
   SeeAlso: 
---

# Arch Reference/fr

## Description

L\'outil **Arch Référence externe** vous permet de placer un objet dans le document en cours qui copie sa forme et ses couleurs à partir d\'un objet issu de l\'[atelierPart](Part_Workbench/fr.md) (y compris [Arch Partie de bâtiment](Arch_BuildingPart/fr.md)) enregistré dans un autre fichier FreeCAD. Si ce fichier FreeCAD change, l\'objet de référence est marqué pour être rechargé.

<img alt="" src=images/Arch_reference_screenshot.png  style="width:600px;">



## Utilisation

1.  Appuyez sur le bouton **<img src="images/Arch_Reference.svg" width=16px> [Référence externe](Arch_Reference/fr.md)**,
2.  Appuyez sur le bouton \"Choisir un fichier\...\" et sélectionnez un fichier FreeCAD existant,
3.  Sélectionnez l\'un des objets à base de pièce inclus dans la liste déroulante,
4.  Appuyer sur **OK**.

## Options

-   L\'objet de référence peut être déplacé et pivoté, la position en cours sera conservée après le rechargement de l\'objet.
-   Si l\'objet original est déplacé dans le fichier contenant, ce mouvement sera reflété dans l\'objet de référence.
-   En cliquant avec le bouton droit de la souris sur un objet de référence dans l\'arborescence, vous avez le choix entre recharger l\'objet d\'origine ou ouvrir le fichier qui le contient.
-   Pour référencer plusieurs objets à la fois, placez-les dans un [Arch Partie de bâtiment](Arch_BuildingPart/fr.md).
-   Lorsque vous désactivez la propriété de vue **Update Colors** de la référence, les couleurs d\'origine ne sont plus rechargées, vous pouvez donc les modifier en toute sécurité.



## Propriétés

-    **File**: fichier de base sur lequel ce composant est construit

-    **Part**: l\'item à utiliser à partir du fichier de base.

-    **Update Colors**: si la valeur est true, les couleurs du fichier lié seront mises à jour.



## Script

L\'outil Reference externe peut être utilisé à l\'intérieur d\'une [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md), en utilisant la fonction suivante :


```python
reference = makeReference([filepath], [partname], [name])
```

Crée un objet `reference` nommé `name` à partir de l\'objet `partname` dans le fichier `filepath`. Tous les arguments sont facultatifs.

Exemple :


```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd", "myPart")
```



---
⏵ [documentation index](../README.md) > Arch Reference/fr
