---
- GuiCommand:/de
   Name:Part Cut
   Name/de:Part Differenz
   MenuLocation:Formteil → Boolesche Operationen → Differenz
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Boolesche Operation](Part_Boolean/de.md), [Part Vereinigung](Part_Fuse/de.md), [Part Schnitt](Part_Common/de.md)
---

# Part Cut/de

## Beschreibung

Beschneidet ausgewählte Part-Objekte, wobei das letzte vom ersten abgezogen (subtrahiert) wird. Diese Operation ist voll parametrisch und die Komponenten können modifiziert und das Ergebnis neu berechnet werden.

**Hinweis:** Dieser Befehl ist eine automatisierte Form des <img alt="" src=images/Part_Booleans.svg  style="width:24px;"> [Boolesche Operation](Part_Boolean/de.md).

[480px\|left\|Schneiden](IMAGE:Part_Cut_01.png.md)

## Anwendung

1.  Wähle zwei Formen
2.  Rufe den Part Schneiden Befehl auf verschiedene Weise auf:
    -   Drücke die **![](images/) '''Schneiden'''** Schaltfläche in der Part Werkzeugleiste
    -   Verwende den {{MenuCommand/de|Part → Boolesche operation → Schneiden}} Eintrag aus dem Part Menü

## Unterstützte Eingaben 

Eingabeobjekte müssen [OpenCASCADE](OpenCASCADE/de.md) Formen sein. Beispiele: Sachen, die mit den Arbeitsbereichen Part, PartDesign, Skizzierer erstellt wurden. Keine Polygonnetze (es sei denn, diese wurden in Formen umgewandelt) - für Polygonnetze gibt es spezielle boolesche Werkzeuge im Arbeitsbereich Netzkonstruktion.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/de
