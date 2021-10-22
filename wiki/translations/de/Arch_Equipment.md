---
- GuiCommand:/de
   Name:Arch Equipment
   Name/de:Arch Ausstattung
   MenuLocation:Arch → Ausstattung
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**E** **Q**
   SeeAlso:[Arch 3 Ansichten](Arch_3Views/de.md)
---

# Arch Equipment/de

## Beschreibung

Das Ausstattungwerkzeug bietet einen einfachen und bequemen Weg, nichttragende, einzelstehende Elemente wie Möbelstücke, Sanitärgegenstände oder elektrische Geräte zu Deinen Projekten hinzuzufügen. Ausstattungen basieren auf [Part Formen](Part_Workbench/de.md), die es erlauben, von der Solidität und den Möglichkeiten von BRep Geometrien zu profitieren und nette Ansichten von Drauf- und Schnittansichten zu erzeugen.

![](images/Arch_equipment_example.jpg ) 
*Möbelobjekte, die in einem  [Arch Ausstattung](Arch_Equipment.md) Objekt eingeschlossen sind. Die flachen Projektionen können mit dem [Entwurf Shape2DAnsicht](Draft_Shape2DView/de.md) Werkzeug erhalten werden.*

Seit v0.17 können Ausstattungsobjekte auch eine {{PropertyData/de|HiRes}}-Eigenschaft haben, woran ein [Netz](Mesh_Workbench/de.md)-Objekt angeheftet werden kann. Ausstattungsobjekte können dann veranlasst werden, dieses Netz anstatt ihrer Form in der 3D-Ansicht anzuzeigen, um so beliebige hochauflösende Netz-Objekte wie detaillierte Möbelstücke zu verwenden, die üblicherweile auf Web-Seiten zu finden sind.

![](images/Arch_equipment_mesh.jpg ) 
*Möbelobjekte innerhalb eines [Arch Ausstattung](Arch_Equipment/de.md) Objekts, mit einem beigefügten hochauflösenden Netz*

Durch Nutzung des Arch OBJ Exporteurs können alle Ausstattungsobjekte im Netz Anzeige Modus als Netz anstatt als Form exportiert werden.

## Anwendung

1.  Wähle eine [Part](Part_Workbench/de.md) Form und optional ein [Netz](Mesh_Workbench/de.md) Objekt.
2.  Drücke die **<img src="images/Arch_Equipment.svg" width=16px> [Ausstattung](Arch_Equipment/de.md)** Schaltfläche oder drücke **E**, dann **Q** Tasten.

## Optionen

-   Ausstattungen teilen die allgemeinen Eigenschaften und Verhaltensweisen aller [Arch-Komponenten](Arch_Component/de.md)

## Eigenschaften

-    {{PropertyData/de|Model}}: Eine Beschreibung des Modells dieser Ausstattung.

-    {{PropertyData/de|Url}}: Ein URL der Produktseite, wo mehr Informationen zu dieser Ausstattung gefunden werden können.

-    {{PropertyData/de|Mesh}}: Eine für diese Ausstattung zu verwendende [Netz](Mesh_Workbench/de.md)-Darstellung. Wenn gesetzt, wird der **Netz**-Anzeige-Modus verfügbar.

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Ausstattungswerkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole mit der folgenden Funktion verwendet werden: 
```python
Equipment = makeEquipment(baseobj=None, placement=None, name="Equipment")
```

-   Erstellt ein `Equipment`-Objekt aus dem gegebenen `baseobj`, das ein `Part`- oder `Mesh`-Objekt sein kann.
-   Wenn ein `Placement` angegeben ist, wird es benutzt.
-   Es liefert `None` zurück, falls die Operation fehlschlägt.

Beispiel: 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 500
Box.Width = 2000
Box.Height = 600

Equip = Arch.makeEquipment(Box)
FreeCAD.ActiveDocument.recompute()
```

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Equipment/de
