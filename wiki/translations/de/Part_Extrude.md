---
- GuiCommand:/de
   Name:Part Extrude
   Name/de:Part Extrudieren
   MenuLocation:Formteil → Extrudieren...
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Draft Trimex](Draft_Trimex/de.md), [PartDesign Pad](PartDesign_Pad/de.md)
---

# Part Extrude/de



## Beschreibung

**Part Extrudieren** erweitert eine Form durch einen bestimmten Abstand in einer bestimmten Richtung. Der Typ der Ausgabeform ändert sich abhängig vom Typ der Eingabeform und der gewählten Optionen.

In den meisten üblichen Szenarien wird im Folgenden der erwartete Ausgabeformtyp aus einem gegebenen Eingabeformtyp aufgelistet,

-   extrudieren eines Knotens (Punkt) wird ein gerade Kante (Linie) erzeugen
-   extrudieren einer offenen Kante (z.B. Linie, Bogen) wird eine offene Fläche (z.B. Ebene) erzeugen
-   extrudieren einer geschlossenen Kante (z.B. Kreis) wird wahlweise eine geschlossene Fläche (z.B. einen Zylinder mit offenem Ende) oder falls der Parameter *Festkörper* `True` ist, einen Festkörper (z.B. einen geschlossenen Festkörperzylinder) erzeugen
-   extrudieren eines offenen Drahts (z.B. Entwurf Draht) wird wahlweise eine offene Hülle (mehrere verbundene Flächen) erzeugen
-   extrudieren eines geschlossenen Linienzuges (z.B. Draft Linienzug) wird wahlweise eine Hülle (mehrere angeschlossene Flächen) oder wenn der Parameter *Festkörper* `True` ist, einen Festkörper erzeugen
-   extrudieren einer Fläche (z.B. Ebene) wird einen Festkörper (z.B. Quader) erzeugen
-   extrudieren eines **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Entwurf Form Zeichenfolge](Draft_ShapeString.md)** wird einen Verbund von Festkörpern (die Zeichenfolge ist ein Verbund der Buchstaben, die ebenfalls Festkörper sind) erzeugen
-   extrudieren einer Hülle von Flächen wird ein Verbundfestkörper erzeugt

![600px](images/Part_Extrude_demo.png)



*Beispiele für Extrusionen*



## Anwendung

1.  Die Formen in der [3D-Ansicht](3D_view/de.md) oder in der [Baumansicht](Tree_view/de.md) auswählen.

2.  Die Schaltfläche **<img src="images/Part_Extrude.svg" width=16px> [Extrudieren](Part_Extrude/de.md)** in der Symbolleiste drücken oder den Menüeintrag **Part → Extrudieren** auswählen.

3.  Richtung, Länge und wahlweise weitere Parameter einstellen (siehe den folgenden Abschnitt [Parameter](#Parameter.md) für weitere Einzelheiten).

4.  
    **OK**klicken.

Alternativ kann die Auswahl auch nach dem Start des Werkzeugs erfolgen, durch Auswahl einer oder mehrerer Formen aus der Liste im [Aufgabenbereich](Task_panel/de.md).

Der Modellbaum zeigt so viele Extrusionsobjekte wie vorher ausgewählte Formen. Jede Eingabeform wird unterhalb des jeweiligen Extrusionsobjekte abgelegt.



## Parameter

Die Extrusionsform wird durch die folgenden Parameter festgelegt, die nach ihrer Erstellung im [Eigenschafteneditor](Property_editor/de.md) bearbeitet werden können.

-   **Basis**: Die Eingangsform (die Form, auf die Part Extrudieren angewendet wurde).

-   **Dir**: Die Richtung, in die die Form extrudiert werden soll. Falls **Dir Mode** auf \'Custom\' gesetzt ist, kann **Dir** geändert werden. Andernfalls ist **Dir** nur-lesen und wird aus der verbundenen Form berechnet.

-   **Dir Link**: Parametrische Verbindung zu einer Kante (Linie), die die Extrusionsrichtung festlegt.

-   **Dir Mode**: legt fest, wie **Dir** kontrolliert wird. \'Custom\' bedeutet, **Dir** ist änderbar. \'Edge\' bedeutet, Dir wird aus einer über **Dir Link** verbundenen Kante (Linie) ermittelt. \'Normal\' bedeutet, Dir ist senkrecht zur Ebene der Eingabeform.

-   **Length Fwd**: Die zu extrudierende Länge. Falls sowohl **Length Fwd** und **Length Rev** Null sind, wird die Länge des **Dir**-Vektors verwendet.

-   **Length Rev**: Zusätzliche zu extrudierende Länge gegen **Dir**.

-   **Solid**: Falls `True`, wird das Extrudieren einer geschlossenen Kante oder eines geschlossenen Linienzuges einen Festkörper ergeben. Falls `False`, wird eine Hülle entstehen.

-   **Reversed**: Kehrt die Extrusionsrichtung um (gegen **Dir**).

-   **Symmetric**: wenn True, ist die Extrusion an der Eingangsform zentriert, und die Gesamtlänge ist **Länge Fwd**. **Länge Rev**\' wird ignoriert.

-   **Neigungswinkel**\' und **Neigungswinkel Rev**\': wendet einen Winkel auf die Extrusion an, so dass die Seiten der Extrusion um den angegebenen Winkel verzogen werden. Positiver Winkel bedeutet, dass sich der Querschnitt ausdehnt. **Neigungswinkel Rev**: legt die Verjüngung für den entgegengesetzten Teil der Extrusion fest (der Teil aus **Länge Rev**).
    -   
        {{Version/de|0.20}}
        
        Innere Strukturen erhalten einen gegenläufigen Schrägungswinkel. Dies dient dazu, die Konstruktion von Gussformen und Gussteilen zu unterstützen.

    -   
        {{VersionMinus/de|0.19}}
        
        Abgeschrägte Extrusion wird nur für Formen ohne innere Strukturen unterstützt. Abschrägen funktioniert nicht gut, wenn die extrudierte Form B-Splines enthält.

-   **Flächer Hersteller Klasse**\': legt den C++ Klassennamen des Flächen Hersteller Codes fest, der bei der Herstellung von Festkörpern aus Drähten verwendet wird. Diese Eigenschaft dient hier hauptsächlich der Aufrechterhaltung der Abwärtskompatibilität. Nicht antasten, es sei denn, du weißt, was du tust.

-   **Placement**: Die Standard-[Positionierungsparameter](Placement/de.md).

-   **Label**: Bezeichnung die in der [Baumansicht](Tree_view/de.md) angezeigt wird (nicht verfügbar bei der Erstellung der Extrusion).



## Aufgabendialog

![](images/Part_Extrude_dialog.png )

-    **OK**: Schaltfläche erzeugt die Extrusion und schließt den Dialog.

-    **Schließen**Schaltfläche schließt den Dialog, ohne etwas zu tun.

-    **Anwenden**Schaltfläche erzeut die Extrusion, schließt aber nicht den Dialog. Nach Auswahl einer weiteren Form in der Liste am Schluss kann eine weitere Extrusionen erfolgen. Mehrfaches Klicken auf **Apply** erzeugt mehrere Extrusionen.

-   \'Richtung\' Radioknöpfe: Legt den Weg fest, wie die Extrusionsrichtung berechnet wird.

-   Schaltfläche **Select**: anklicken und danach eine Kante in der [3D-Ansicht](3D_view/de.md) auswählen. Diese Kante wird im Textfeld neben der Schaltfläche im Format \"ObjectName:EdgeN\" erscheinen. Der Link kann auch manuell eingetippt werden. Die X-, Y- und Z-Werte werden entsprechend der Kantenrichtung eingetragen.

-    **X**, **Y**, **Z** Schaltflächen: Klicke *x* Schaltfläche, um die Extrusionsrichtung auf +*x* Achse zu setzen. Erneutes klicken setzt sie auf -*x* Achse.

-    **X**, **Y**, **Z** Eingabefelder: Setzt oder zeigt den Richtungsvektor der Extrusion. Wenn beide Längen Null sind, setzt die Länge dieses Vektor die Extrusionslänge. Die Längen sind immer in mm, unabhängig von Einheiteneinstellungen.

-   Längen Felder: Setzt die Extrusionslänge. Diese Eingabefelder berücksichtigen Einheiteneinstellungen.

-   Symmetrisch: breitet die Extrusion in beide Richtungen aus, so dass das Profil in der Mitte verbleibt.

-   Außenneigungswinkel: positiver Winkel bedeutet, dass das Profil am anderen Ende der Extrusion erweitert wird.

-   Erzeuge Festkörper Ankreuzkästchen: Wenn aktiviert, wird die Extrusion eines geschlossenen Linienzugs oder einer geschlossenen Kante einen Festkörper ergeben. Es ist wird standardmäßig aktiviert, wenn vor dem Aufruf von Part Extrusion ein geschlossener Linienzug ausgewählt wurde.

-   Formliste: Hier werden die zu extrudierenden Formen ausgewählt. Bei der Auswahl von mehreren Objekte werden mehrere Extrusionsobjekte erstellt.



## Hinweise

-   [App-Link](App_Link/de.md)-Objekte, die auf geeignete Objektarten verweisen und [App-Part](App_Part/de.md)-Container, die geeignete sichtbare Objekte enthalten, können auch als Profile und zum Feslegen der Richtung verwendet werden. {{Version/de|0.20}}

-   Der Aufgaben-Dialog bietet noch keine Vorschau. **Anwenden** erzeugt mit jedem Klick darauf ein Extrusionsobjekt, das als Vorschau nützlich sein kann; sie bleiben jedoch erhalten und ein weiteres wird erzeugt, wenn **OK** angeklickt wird. [Rückgängig](Std_Undo/de.md) kann nützlich sein, um sie zu bereinigen, bevor **OK** geklickt wird.



## Vergleich mit PartDesign Aufpolsterung 

[PartDesign Aufpolsterung](PartDesign_Pad/de.md) ist auch eine Extrusionsfunktion, aber es gibt wichtige Unterschiede:

-   Part Extrudieren erstellt immer eine eigenständige Form. PartDesign Aufpolsterung vereinigt das Ergebnis immer mit dem Rest des Körpers.
-   Part Extrudieren ist es egal, wo es sich im Baum befindet. PartDesign Aufpolsterung kann nur innerhalb eines [PartDesign Körpers](PartDesign_Body/de.md) existieren.
-   Part Extrudieren kann jedes Objekt, das eine Part-Geometrie enhält extrudieren ([OpenCASCADE](OpenCASCADE/de.md)-Form), Außer Festkörper und Verbundkörper.
-   Part Extrudieren kann einzelne Flächen von anderen Objekten Extrudieren. PartDesign Aufpolsterung akzeptiert nur entweder Skizzen-Objekte oder Flächen von PartDesign-Objekten als Profil.





{{Part_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Extrude/de
