---
 GuiCommand:
   Name: Std TransformManip
   Name/de: Std Bewegen
   MenuLocation: Bearbeiten , Bewegen
   Workbenches: Alle
   SeeAlso: Std_UserEditMode/de|Std BenutzerBearbeitungsModus

---

# Std TransformManip/de



## Beschreibung

Das Werkzeug **Std Bewegen** ermöglicht Rotations- und Verschiebungswerte inkrementell auf ein Objekt anzuwenden.

<img alt="" src=images/Std_TransformManip_Example.png  style="width:400px;">



## Anwendung

1.  Ein Objekt mit einer {{PropertyData/de|Placement}} auswählrn. Siehe [Hinweise](#Hinweise.md).
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Den Menüeintrag **Bearbeiten → <img src="images/Std_TransformManip.svg" width=16px> Bewegen** auswählen.
    -   Die Menüoption **<img src="images/Std_TransformManip.svg" width=16px> Bewegen** im Kontextmenü der [Baumansicht](Tree_view/de.md) auswählen.
    -   Ist der [Bearbeitungsmodus](Std_UserEditMode/de.md) auf **<img src="images/Std_UserEditModeTransform.svg" width=16px> Transformieren** gesetzt, kann ein Objekt in der Baumansicht doppelt angeklickt werden.
3.  Der Aufgaben-Dialog **Schrittweiten** wird geöffnet.
4.  Wahlweise die Schrittweiten der Parameter anpassen.
5.  Zum Bewegen hat man folgende Möglichkeiten:
    -   Die linke Maustaste auf einem Achspfeil drücken, halten und ziehen, um das Objekt entlang dieser Achse zu verschieben.
    -   Die linke Maustaste auf einem Ebenensymbol drücken, halten und ziehen, um das Objekt auf dieser Ebene zu verschieben.
    -   Die linke Maustaste auf einem Kugelsymbol drücken, halten und ziehen, um das Objekt um die zugehörige Achse zu drehen.
6.  Zum Beenden des Befehls hat man folgende Möglichkeiten:
    -   Die Schaltfläche **OK** drücken, um zu bestätigen und zu beenden.
    -   Die Schaltfläche **Abbrechen** drücken, um die ausgeführten Bewegungen rückgängig zu machen und zu beenden. {{Version/de|1.0}}



## Hinweise

-   Sobald das Objekt in der [3D-Ansicht](3D_view/de.md) verschoben/gedreht wird, werden diese Änderungen übernommen.
-   Einige Objekte mit einer {{PropertyData/de|Placement}}, wie z.B. Skizzen, oder Objekte, die an anderen Objekten befestigt sind, können nicht bewegt werden.
-   Es gibt keine Schaltfläche **Abbrechen** in {{VersionMinus/de|0.21}}, in diesen Versionen muss man zunächst die Schaltfläche **OK** drücken und anschließend den Befehl <img alt="" src=images/Std_Undo.svg  style="width:16px;"> [Rückgängig](Std_Undo/de.md) verwenden, um die Änderungen nachträglich rückgängig zu machen.



---
⏵ [documentation index](../README.md) > Std TransformManip/de
