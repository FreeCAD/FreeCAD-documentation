---
- GuiCommand:/fr
   Name:Arch PipeConnector
   Name/fr:Arch Connecteur tuyau
   MenuLocation:Arch → Outils pour la tuyauterie → Connecteur
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**P** **C**
   Version:0.17
   SeeAlso:[Arch Tuyau](Arch_Pipe/fr.md), [Arch Equipement](Arch_Equipment/fr.md)
---

# Arch PipeConnector/fr

## Description

Cet outil vous permet de créer des raccords entre deux ou plusieurs [Tuyaux](Arch_Pipe/fr.md) sélectionnés.

## Utilisation

1.  Sélectionnez 2 or 3 [Arch Tuyaux](Arch_Pipe/fr.md). Si vous avez sélectionné trois tubes, deux doivent être parfaitement alignés.
2.  Cliquez le bouton **<img src="images/Arch_PipeConnector.svg" width=16px> [Connecteur](Arch_PipeConnector/fr.md)** ou pressez la touche **P** puis **C**.

## Propriétés

-    {{PropertyData/fr|Radius}}: Le rayon de la courbe de la connexion

## Travail typique 

Reportez-vous aux informations sur [Tuyaux](Arch_Pipe/fr.md) pour en savoir plus sur l\'utilisation des tuyaux et la création de connecteurs.

## Script


**Voir aussi:**

[API](Arch_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Connecteur peut être utilisé dans une [macro](macros/fr.md) ou depuis la console [Python](Python/fr.md) en utilisant la fonction suivante: 
```python
Connector = makePipeConnector(pipes, radius=0, name="Connector")
```

-   Crée un objet `Connector` à partir du `pipes` donné qui est une liste de [Tubes](Arch_Pipe/fr.md) et éventuellement un rayon `radius` de courbure.
    -   Les objets de base ([Filaire](Draft_Wire/fr.md)) des [Tuyaux](Arch_Pipe/fr.md) doivent partager un noeud final afin de créer un connecteur lisse et approprié.

Exemple: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(-1000, 0, 0)
p2 = FreeCAD.Vector(-2000, 0, 0)
p3 = FreeCAD.Vector(-2000, 0, 0)
p4 = FreeCAD.Vector(-2000, -1000, 0)
p5 = FreeCAD.Vector(-2000, -1000, 0)
p6 = FreeCAD.Vector(-4000, -1000, 0)
Line1 = Draft.makeWire([p1, p2])
Line2 = Draft.makeWire([p3, p4])
Line3 = Draft.makeWire([p5, p6])

Pipe1 = Arch.makePipe(Line1, 150)
Pipe2 = Arch.makePipe(Line2, 150)
Pipe3 = Arch.makePipe(Line3, 150)
FreeCAD.ActiveDocument.recompute()

Conn = Arch.makePipeConnector([Pipe1, Pipe2])
Conn2 = Arch.makePipeConnector([Pipe2, Pipe3])
FreeCAD.ActiveDocument.recompute()

Line4 = Draft.move(Line1, FreeCAD.Vector(-500, 1000, 0), copy=True)
Line5 = Draft.move(Line2, FreeCAD.Vector(-500, 1000, 0), copy=True)
Pipe4 = Arch.makePipe(Line4, 100)
Pipe5 = Arch.makePipe(Line5, 100)
FreeCAD.ActiveDocument.recompute()

Conn3 = Arch.makePipeConnector([Pipe4, Pipe5], radius=400)
FreeCAD.ActiveDocument.recompute()
```

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch PipeConnector/fr
