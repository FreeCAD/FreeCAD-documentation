---
 GuiCommand:
   Name: Part TransformedCopy
   Name/de: Part TransformierteKopie
   MenuLocation: Part , Kopie erstellen , Transformierte Kopie erstellen
   Workbenches: Part Workbench/de
   Version: 0.19
   Siehe auch: Part_SimpleCopy/de
---

# Part TransformedCopy/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_TransformedCopy.svg  style="width:24px;"> [Part TransformierteKopie](Part_TransformedCopy/de.md) erstellt nichtparametrische Kopien von Objekten. Er ist gedacht für Objekte, die in Behältern eingebettet sind.

The **Placement** of the copies is adjusted, accounting for the placement of the container(s), so that their position and rotation relative to the global coordinate system is the same as that of the original objects. If the selected objects are not nested, or nested in a container with a default placement, this command produces the same results as [Part SimpleCopy](Part_SimpleCopy.md).



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Den Menüeintrag **Part → Kopie erstellen → <img src="images/Part_TransformedCopy.svg" width=16px> [Transformierte Kopie erstellen](Part_TransformedCopy/de.md)** auswählen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Die erstellten Objekte sind [Part Formelemente](Part_Feature/de.md) ohne weitere Eigenschaften.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part TransformedCopy/de
