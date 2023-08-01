---
- GuiCommand:/de
   Name:Draft FlipDimension
   Name/de:Draft MaßKippen
   MenuLocation:Änderung → Bemaßung umkehren
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
---

# Draft FlipDimension/de

## Beschreibung

Der Befehl <img alt="" src=images/Draft_FlipDimension.svg  style="width:24px;"> **Draft MaßKippen** schwenkt die Maßzahlen (Maßtexte) ausgewählter [Draft-Maße](Draft_Dimension/de.md) 180° um die Maßlinie. Es kann verwendet werden, um Maße zu korrigieren, die gespiegelt erscheinen. Der Befehl funktioniert nicht ordentlich mit Winkelmaßen.

## Anwendung

1.  Ein oder mehrere [Draft-Maße](Draft_Dimension/de.md) auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_FlipDimension.svg" width=16px> [Bemaßung umkehren](Draft_FlipDimension/de.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_FlipDimension.svg" width=16px> Bemaßung umkehren** auswählen.

## Hinweise

-   [Draft Maße](Draft_Dimension.md) haben auch eine {{PropertyData/de|Flip Text}}. Auf `True` gesetzt, wird der Text 180° um die Normalenrichtung geschwenkt. Das kann mit dem Effekt aus diesem Befehl kombiniert werden.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um ein [Draft Maß](Draft_Dimension/de.md) zu kippen, invertiert man seine Eigenschaft `Normal`.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 0, 0)
p3 = App.Vector(500, 300, 0)
dimension = Draft.make_dimension(p1, p2, p3)
dimension.ViewObject.FontSize = 200

dimension.Normal = dimension.Normal.negative()
doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft FlipDimension/de
