---
 GuiCommand:
   Name: Part ExplodeCompound
   Name/de: Part VerbundSprengen
   MenuLocation: Formteil , Verbund , Verbundteile extrahieren
   Workbenches: Part_Workbench/de
   Version: 0.18
   SeeAlso: Part_Compound/de, Draft_Downgrade/de
---

# Part ExplodeCompound/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> **Part VerbundSprengen** teilt einen Verbund aus Formen auf, um jede enthaltene Form (Kind) als separates Objekt zur Verfügung zu stellen. Die Kinder werden automatisch in eine [Gruppe](Std_Group/de.md) aufgenommen, wenn es mehr als ein Kind gibt.

Es ist halbparametrisch: Die Formen der Kinder werden aktualisiert, wenn sich die Quellverbindung ändert, aber wenn sich die Anzahl der Kinder in der Verbindung ändert, wird in der Auflösung werden entweder einige Formen fehlen oder redundante Objekte in einem Fehlerzustand besitzen.

Die Positionierung der extrahierten Formen folgt den Positionierungen der Originale und der Positionierungseigenschaft jedes Kindes.

Das Werkzeug wird auch nicht verbundene Formen in ihre untergeordneten Bestandteile zerlegen: Mischkörper zu Festkörpern, Festkörper zu Schalen, Schalen zu Flächen, Flächen zu Drähten, Drähte zu Kanten, Kanten zu Knoten.



## Anwendung

1.  Eine einzelnen Verbund auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_ExplodeCompound.svg" width=16px> [Verbundobjekt sprengen](Part_ExplodeCompound/de.md)** drücken.
    -   Den Menüeintrag **Part → Verbund → Verbundobjekt sprengen** auswählen.



## Anwendungsfälle

-   Die Positionen von Formen anpassen, die mit <img alt="" src=images/Draft_OrthoArray.svg  style="width:16px;"> [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de.md) erstellt wurden.
-   Die Bestandteile aus dem Ergebnis von <img alt="" src=images/Part_Slice.svg  style="width:16px;"> [Part Zerschneiden](Part_Slice/de.md) und <img alt="" src=images/Part_Cut.svg  style="width:16px;"> [Part Schneiden](Part_Cut/de.md) entnehmen.
-   Einzelne Konturen aus Skizzen und Flächen mit mehreren Konturen entnehmen.
-   Einen reinen Festkörper aus einem Festkörper-in-Verbund erhalten, zur Verwendung im Arbeitsbereich <img alt="" src=images/Workbench_FEM.svg  style="width:16px;"> [FEM](FEM_Workbench/de.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ExplodeCompound/de
