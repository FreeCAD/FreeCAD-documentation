---
- GuiCommand:
   Name:Part ExplodeCompound
   Name/de:Part VerbundSprengen
   MenuLocation:Formteil → Verbund → Verbundteile extrahieren
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.18
   SeeAlso:[Part Verbund](Part_Compound/de.md), [Draft Herabstufen](Draft_Downgrade/de.md)
---

# Part ExplodeCompound/de



## Beschreibung

Werkzeug zum Aufteilen von Formverbünden, um jede enthaltene Form (Kind) als separates Objekt im Modellbaum verfügbar zu machen. Die Kinder werden automatisch in eine [Gruppe](Std_Group/de.md) aufgenommen, wenn es mehr als ein Kind gibt.

Es ist halbparametrisch: Die Formen der Kinder werden aktualisiert, wenn sich die Quellverbindung ändert, aber wenn sich die Anzahl der Kinder in der Verbindung ändert, wird in der Auflösung werden entweder einige Formen fehlen oder redundante Objekte in einem Fehlerzustand besitzen.

Die Positionierung der extrahierten Formen folgt den Positionierungen der Originale und der Positionierungseigenschaft jedes Kindes.

Das Werkzeug wird auch nicht verbundene Formen in ihre untergeordneten Bestandteile zerlegen: Mischkörper zu Festkörpern, Festkörper zu Schalen, Schalen zu Flächen, Flächen zu Drähten, Drähte zu Kanten, Kanten zu Knoten.



## Anwendung

1.  Rufe das Formteil SprengeVerbund Werkzeug auf verschiedene Weise auf:
    -   Drücke auf die <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> Schaltfläche in der Part Werkzeugleiste.
    -   Verwendung des **Formteil → Verbund → Verbundteile extrahieren** Eintrags im Part Menü



## Anwendungsfälle

-   Korrektur der Positionen von Formen, die von <img alt="" src=images/Draft_OrthoArray.svg  style="width:24px;"> [Entwurf rechtwinklige(r) Anordnung](Draft_Array/de.md) erstellt wurden
-   Erhalten von geteilten Stücken aus dem Ergebnis von <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Part Scheibe](Part_Slice/de.md) und <img alt="" src=images/Part_Cut.svg  style="width:24px;"> [Part Schneiden](Part_Cut/de.md)
-   Erhalten individueller Konturen aus Mehrfachkonturskizzen und Flächen
-   Erhalten eines reinen Festkörpers aus einem Festkörper-in-Verbund zur Verwendung in <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM Arbeitsbereich](FEM_Workbench/de.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ExplodeCompound/de
