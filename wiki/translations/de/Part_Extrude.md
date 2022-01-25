---
- GuiCommand:/de
   Name/de:Part Extrudieren
   MenuLocation:Part → Extrudieren
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Trimex](Draft_Trimex/de.md)
---

# Part Extrude/de


</div>

![600px](images/Part_Extrude_demo.png)

## Beschreibung

**Part Extrudieren** erweitert eine Form durch einen bestimmten Abstand in einer bestimmten Richtung. Der Typ der Ausgabeform ändert sich abhängig vom Type der Eingabeform und der gewählten Optionen.

In den meisten üblichen Szenarien wird im Folgenden der erwartete Ausgabeformtyp aus einem gegebenen Eingabeformtyp aufgelistet,

-   extrudieren eines Knotens (Punkt) wird ein gerade Kante (Linie) erzeugen
-   extrudieren einer offenen Kante (z.B. Linie, Bogen) wird eine offene Fläche (z.B. Ebene) erzeugen
-   extrudieren einer geschlossenen Kante (z.B. Kreis) wird wahlweise eine geschlossene Fläche (z.B. einen Zylinder mit offenem Ende) oder falls der Parameter *Festkörper* `True` ist, einen Festkörper (z.B. einen geschlossenen Festkörperzylinder) erzeugen
-   extrudieren eines offenen Drahts (z.B. Entwurf Draht) wird wahlweise eine offene Hülle (mehrere verbundene Flächen) erzeugen
-   extrudieren eines geschlossenen Linienzuges (z.B. Draft Linienzug) wird wahlweise eine Hülle (mehrere angeschlossene Flächen) oder wenn der Parameter *Festkörper* `True` ist, einen Festkörper erzeugen
-   extrudieren einer Fläche (z.B. Ebene) wird einen Festkörper (z.B. Quader) erzeugen
-   extrudieren eines **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Entwurf Form Zeichenfolge](Draft_ShapeString.md)** wird einen Verbund von Festkörpern (die Zeichenfolge ist ein Verbund der Buchstaben, die ebenfalls Festkörper sind) erzeugen
-   extrudieren einer Hülle von Flächen wird ein Verbundfestkörper erzeugt


<div class="mw-translate-fuzzy">

## Anwendung

1.  Wähle die Form(en) in der 3D Ansicht oder im Modell [Baumansicht](tree_view/de.md)
2.  Klicke auf das **<img src="images/Part_Extrude.svg" width=16px> '''Extrudieren'''** Symbol in der Werkzeugleiste oder gehe zum {{MenuCommand/de|Part → Extrudieren}} Menü
3.  Setze die Richtung und Länge und wahlweise andere Parameter (siehe den folgenden [Parameter](#Parameters/de.md) Abschnitt für weitere Einzelheitenn).
4.  Klicke OK.


</div>

Alternativ kann die Auswahl auch nach dem Start des Werkzeugs erfolgen, durch Wahl einer oder mehrerer Formen aus der Liste im [Aufgabenpaneel](Task_panel/de.md).

Der Modellbaum zeigt so viele Extrusionsobjekte wie vorher ausgewählte Formen. Jede Eingabeform wird unterhalb des jeweiligen Extrusionsobjekte abgelegt.

## Parameter

Die Extrusionsform wird durch die folgenden Parameter festgelegt, die nach ihrer Erstellung auf dem Datenreiter bearbeitet werden können.

-   **Basis**: Die Eingabeform (die Form, auf die Part Extrudieren angewendet wurde)

-   **Dir**: Die Richtung, in die die Form extrudiert werden soll. Falls **Dir Mode** auf \'Custom\' gesetzt ist, kann **Dir** geändert werden. Andernfalls ist **Dir** nur-lesen und wird aus der verbundenen Form berechnet.

-   **Dir Link**: Parametrische Verbindung zu einer Kante (Linie), die die Extrusionsrichtung setzt. Seit v0.17 wird diese Eigenschaft nicht mehr vom Eigenschafteneditor unterstützt.

-   **Dir Mode**: legt fest, wie **Dir** kontrolliert wird. \'Custom\' bedeutet, **Dir** ist änderbar. \'Edge\' bedeutet, Dir wird aus einer über **Dir Link** verbundenen Kante (Linie) ermittelt. \'Normal\' bedeutet, Dir ist senkrecht zur Ebene der Eingabeform.

-   **Length Fwd**: Die zu extrudierende Länge. Falls sowohl **Length Fwd** und **Length Rev** Null sind, wird die Länge des **Dir**-Vektors verwendet.

-   **Length Rev**: Zusätzliche zu extrudierende Länge gegen **Dir**.

-   **Solid**: Falls `True`, wird das Extrudieren einer geschlossenen Kante oder eines geschlossenen Linienzuges einen Festkörper ergeben. Falls `False`, wird eine Hülle entstehen.

-   **Reversed**: Kehrt die Extrusionsrichtung um (gegen **Dir**).

-   **Symmetric**: wenn True, ist die Extrusion an der Eingangsform zentriert, und die Gesamtlänge ist **Länge Fwd**. **Länge Rev**\' wird ignoriert.

-   **Neigungswinkel**\' und **Neigungswinkel Rev**\': wendet einen Winkel auf die Extrusion an, so dass die Seiten der Extrusion um den angegebenen Winkel verzogen werden. Positiver Winkel bedeutet, dass sich der Querschnitt ausdehnt. **Neigungswinkel Rev**: legt die Verjüngung für den umgekehrten Teil der Extrusion fest (der Teil aus **Länge Rev**). Ab v0.17 wird die geneigte Extrusion nur noch für Drähte ohne Löcher unterstützt. Neigung funktioniert nicht gut, wenn die extrudierte Form B-Splines enthält.

-   **Flächer Hersteller Klasse**\': legt den C++ Klassennamen des Flächen Hersteller Codes fest, der bei der Herstellung von Festkörpern aus Drähten verwendet wird. Diese Eigenschaft dient hier hauptsächlich der Aufrechterhaltung der Abwärtskompatibilität. Nicht antasten, es sei denn, du weißt, was du tust.

-   **Placement**: Die Standard-[placement](Placement.md)-Parameter


<div class="mw-translate-fuzzy">

-   **Label**: Bezeichnung die im Modell [Baumansicht](tree_view/de.md) angezeigt wird (nicht verfügbar bei der Extrusionserstellung)


</div>

## Aufgabendialog

![](images/Part_Extrude_dialog.png )

-    **OK**: Schaltfläche erzeugt die Extrusion und schließt den Dialog.

-    **Schließen**Schaltfläche schließt den Dialog, ohne etwas zu tun.

-    **Anwenden**Schaltfläche erzeut die Extrusion, schließt aber nicht den Dialog. Nach Auswahl einer weiteren Form in der Liste am Schluss kann eine weitere Extrusionen erfolgen. Mehrfaches Klicken auf **Apply** erzeugt mehrere Extrusionen.

-   \'Richtung\' Radioknöpfe: Legt den Weg fest, wie die Extrusionsrichtung berechnet wird.


<div class="mw-translate-fuzzy">

-    **Select**Schaltfläche: Klicke ihn und greife dann eine Kante in der [3D Ansicht](3D_view/de.md). Diese Kante wird im Textfeld neben dem Button erscheinen im Format \"ObjectName:EdgeN\". Du kannst auch den Link manuell eintippen. Die X, Y und Z Werte werden entsprechend der Kantenrichtung gefüllt.


</div>

-    **X**, **Y**, **Z** Schaltflächen: Klicke *x* Schaltfläche, um die Extrusionsrichtung auf +*x* Achse zu setzen. Erneutes klicken setzt sie auf -*x* Achse.

-    **X**, **Y**, **Z** Eingabefelder: Setzt oder zeigt den Richtungsvektor der Extrusion. Wenn beide Längen Null sind, setzt die Länge dieses Vektor die Extrusionslänge. Die Längen sind immer in mm, unabhängig von Einheiteneinstellungen.

-   Längen Felder: Setzt die Extrusionslänge. Diese Eingabefelder berücksichtigen Einheiteneinstellungen.

-   Symmetrisch: breitet die Extrusion in beide Richtungen aus, so dass das Profil in der Mitte verbleibt.

-   Außenneigungswinkel: positiver Winkel bedeutet, dass das Profil am anderen Ende der Extrusion erweitert wird.

-   Erzeuge Festkörper Ankreuzkästchen: Wenn aktiviert, wird die Extrusion eines geschlossenen Linienzugs oder einer geschlossenen Kante einen Festkörper ergeben. Es ist wird standardmäßig aktiviert, wenn vor dem Aufruf von Part Extrusion ein geschlossener Linienzug ausgewählt wurde.

-   Formliste: Hier werden die zu extrudierenden Formen ausgewählt. Bei der Auswahl von mehreren Objekte werden mehrere Extrusionsobjekte erstellt.


<div class="mw-translate-fuzzy">

## Hab Dichs 

Der Part Extrudieren Dialog bietet noch keine Vorschau. **Anwenden** erzeugt jedes Mal, wenn du darauf klickst, ein Extrusionsobjekt, das als Vorschau nützlich sein kann; sie bleiben jedoch erhalten und ein weiteres wird erzeugt, wenn du auf **OK** klickst. [Rückgängig](Std_Undo/de.md) kann nützlich sein, um sie vor dem **OK** Klicken zu bereinigen.


</div>


<div class="mw-translate-fuzzy">

Seit v0.17 kann eine Skizze, die aus PartDesign heraus erstellt wurde, nicht für die Teileextrusion verwendet werden, wenn sie sich innerhalb eines Körpers befindet (\"Verknüpfungen gehen außerhalb des zulässigen Bereichs\" Fehler)// (\"Links go out of allowed scope\" error). Um eine Skizze für die Teilextrusion zu verwenden, solltest du die Skizze aus dem Skizzierer Arbeitsbereich aus erstellen. Du kannst aber auch einfach eins aus PartDesign aus einem Körper herausziehen.


</div>


<div class="mw-translate-fuzzy">

Extrusion mit Neigungswinkel unterstützt keine Bohrungen. Es kann auch zu falschen Ergebnissen führen, wenn sich die Anzahl der Segmente im Profil infolge der Verjüngung ändert.


</div>


<div class="mw-translate-fuzzy">

## Vergleich mit [PartDesign Polster](PartDesign_Pad/de.md) 


</div>

PartDesign Polster ist ebenfalls ein Extrusionsmerkmal, aber es gibt wichtige Unterschiede.

Part Extrudieren erzeugt immer eine einzelne Form. PartDesign Polster verschmilzt das Ergebnis der Extrusion mit dem Rest des Körpers.


<div class="mw-translate-fuzzy">

Part Extrudieren funktioniert überall im Modellbaum, PartDesign Polster nur innerhalb eines [PartDesign Körpers](PartDesign_Body/de.md).


</div>

Part Extrudieren kann jedes Objekt mit Part Geometrie (OCC Form) extrudieren, außer Festkörpern und Verbundfestkörper. Und es kann keine einzelnen Oberflächen von anderen Objekten extrudieren. PartDesign Polster akzeptiert nur eine Skizze als Profil (und eine kleine Auswahl anderer Objekttypen) oder eine Fläche eines Festkörpers.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Extrude/de
