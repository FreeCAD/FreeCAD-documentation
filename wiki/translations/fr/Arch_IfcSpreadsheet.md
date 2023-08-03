---
 GuiCommand:
   Name: Arch_IfcSpreadsheet
   Name/fr: Arch Tableur IFC
   MenuLocation: Arch , Utilitaires , Créer une feuille de calcul IFC
   Workbenches: Arch_Workbench/fr
   Shortcut: **I** **P**
   SeeAlso: Arch_IFC/fr, Arch_IfcExplorer/fr
---

# Arch IfcSpreadsheet/fr

## Description

Cet outil crée une feuille de calcul pour stocker les propriétés [IFC](Arch_IFC/fr.md) d\'un objet.



## Utilisation

1.  Sélectionner un objet.
2.  Lancer la commande en utilisant plusieurs méthodes :
    -   En appuyant sur le bouton **<img src="images/Arch_IfcSpreadsheet.svg" width=16px> Créer une feuille de tableur IFC** dans la barre d\'outils.
    -   Utiliser le raccourci clavier **I** puis **P**.
    -   Utiliser l\'entrée **Arch → Utilitaires → <img src="images/Arch_IfcSpreadsheet.svg" width=16px> Créer une feuille de tableur IFC** du menu supérieur.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Cet outil peut être utilisé dans une [macro](Macros/fr.md) et utilisé dans la console [Python](Python/fr.md) en utilisant la fonction : 
```python
spreadsheet = makeIfcSpreadsheet(archobj=None)
```

-   Crée un objet `spreadsheet`. Vous pouvez éventuellement donner un `archobj`.

Exemple: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

spreadsheet = Arch.makeIfcSpreadsheet(Wall)
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch IfcSpreadsheet/fr
