---
- GuiCommand:/de
   Name:Part Compound‏‎
   Name/de:Part Verbund
   MenuLocation:Formteil → Verbund → Erzeuge Verbund
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.14
   SeeAlso:[Part Verschmelzen](Part_Fuse/de.md), [Part VerbundFiltern](Part_CompoundFilter/de.md), [Part VerbundSprengen](Part_ExplodeCompound/de.md)
---

# Part Compound/de

## Description


<div class="mw-translate-fuzzy">

## Beschreibung

Dieser Befehl erzeugt einen Verbund aus jeder Art topologischer Formen. Dies können Festkörper oder Polygonnetze oder jede andere Art topologischer Formen sein.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Anwendung

1.  Markiere die topologischen Formen, die dem Verbund in der [Baumansicht](Tree_view/de.md)

hinzugefügt werden sollen

1.  Wähle den **Formteil → Verbund → Erzeuge Verbund** Eintrag im Part Menü oder klicke auf die <img alt="" src=images/Part_Compound.svg  style="width:24px;"> Schaltfläche.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Hinweise

Ein Verbund, der sich berührende oder sich überschneidende Formen enthält, ist **ungültig** für Boolesche Operationen. Aufgrund von möglichen Ausführungsproblemen wird standardmäßig keine Prüfung der Formen auf Überschneidung durchgeführt. Automatische Geometrieprüfung (verfügbar für Boolesche Operationen) ist für den Part Verbund ebenfalls deaktiviert.


</div>

Um diese Prüfung einzuschalten, gehe zu {{MenuCommand/de|Werkzeuge → Parameter bearbeiten → Einstellungen..... → Mod → Teil → PrüfeGeometrie→ RunBOPCheck}} und setze den Parameter auf `true`.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/de
