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



## Beschreibung

Dieser Befehl erstellt einen Verbund aus Objekten mit einer topologischen Form wie Festkörper und andere Objekte mit Flächen und/oder Kanten. Er kann keine Netze verarbeiten, da sie keine topologische Form besitzen.



## Anwendung

1.  Die topologischen Formen markieren, die dem Verbund in der [Baumansicht](Tree_view/de.md) hinzugefügt werden sollen.
2.  Den Menüeintrag **Part → Verbund → Erzeuge Verbund** im Part-Menü auswählen oder die Schaltfläche <img alt="" src=images/Part_Compound.svg  style="width:24px;"> drücken.



## Hinweise

Ein Verbund, der sich berührende oder sich überschneidende Stücke enthält, ist **ungültig** für Boolesche Operationen. Aufgrund von möglichen Problemen mit der Rechenleistung wird standardmäßig nicht geprüft, ob sich die Stücke überschneiden. Eine automatische Geometrieprüfung (verfügbar für Boolesche Operationen) ist für den Part-Verbund ebenfalls deaktiviert.

Um diese Prüfung einzuschalten, gehe zu **Werkzeuge → Parameter bearbeiten → Einstellungen..... → Mod → Teil → PrüfeGeometrie→ RunBOPCheck** und setze den Parameter auf `true`.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/de
