---
- GuiCommand   */fr
   Name   *Arch_IfcSpreadsheet
   Name/fr   *Arch Tableur IFC
   MenuLocation   *Arch → Utilitaires → Créer une feuille de calcul IFC
   Workbenches   *[Arch](Arch_Workbench/fr.md)
   Shortcut   ***I** **P**
   SeeAlso   *[Arch IFC](Arch_IFC/fr.md), [Arch Explorateur IFC](Arch_IfcExplorer/fr.md)
---

# Arch IfcSpreadsheet/fr

## Description

Cet outil crée une feuille de calcul pour stocker les propriétés [IFC](Arch_IFC/fr.md) d\'un objet.

## Comment l\'utiliser 

1.  Sélectionnez un objet.
2.  Lancer la commande en utilisant plusieurs méthodes   *
    -   En appuyant sur le bouton **<img src="images/Arch_IfcSpreadsheet.svg" width=16px> Créer une feuille de tableur IFC** dans la barre d\'outils.
    -   Utilisation du raccourci clavier **I** puis **P**.
    -   Utilisation de l\'entrée **Arch → Utilitaires → <img src="images/Arch_IfcSpreadsheet.svg" width=16px> Créer une feuille de tableur IFC** dans le menu supérieur.

## Script


**Voir aussi   ***

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Cet outil peut être utilisé dans une [macro](Macros/fr.md) et utilisé dans la console [Python](Python/fr.md) en utilisant la fonction    * 
```python
spreadsheet = makeIfcSpreadsheet(archobj=None)
```

-   Crée un objet `spreadsheet`. Vous pouvez éventuellement donner un `archobj`.

Exemple   * 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

spreadsheet = Arch.makeIfcSpreadsheet(Wall)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch IfcSpreadsheet/fr
