---
- GuiCommand:/de
   Name:PartDesign AdditivePipe
   Name/de:PartDesign AdditiveAusformung
   MenuLocation:Part Design → Additive Ausformung
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign Additives Rohr](PartDesign_AdditivePipe/de.md), [PartDesign Subtraktive Ausformung](PartDesign_SubtractiveLoft/de.md)
---

# PartDesign AdditivePipe/de


</div>

## Beschreibung

\'\'\' Additives Rohr \'\'\'erstellt einen Volumenkörper im aktiven Bauteil, indem eine oder mehrere Skizzen (auch als Querschnitte bezeichnet) entlang eines offenen oder geschlossenen Pfads verschoben werden. Wenn das Bauteil bereits Formelemente enthält, wird das additive Rohr mit ihnen zusammengeführt.

![](images/PartDesign_AdditivePipe_example.svg )


<div class="mw-translate-fuzzy">

*Links: Querschnittskizze (A) wird über die Pfadskizze (C) in die Querschnittskizze (C) ausgetragen; rechts das daraus resultierende Rohr.*


</div>

## Anwendung

Das obige Beispielbild zeigt zwei verschiedene Querschnittsformen. Im folgenden Text wird das Verfahren nur mit einer einzigen Form beschrieben. Dadurch wird ein Teil mit dem gleichen Querschnitt entlang des gesamten Pfades erreicht.

1.  Erstelle zwei separate Skizzen;
    -   eine für den Pfad, z.B. zwei Linien, die durch eine Kurve verbunden sind, wie im obigen Bild,
    -   eine für die Querschnittsform, z.B. ein Kreis als erste Form in der obigen Abbildung.
    -   **Ordne** die beiden Formen in 3D richtig an. Es wird empfohlen den Ursprung der Querschnittsskizze auf die Linie des Pfades zu legen. Die beiden Skizzen sollten in den meisten Fällen **orthogonal** sein. Dies kann mit der \'Map Modus\' Funktion erfolgen (mache beide Skizzen mit **Leertaste** sichtbar. Wähle die Querschnittsskizze aus. Wähle Eigenschaften/Datenreiter/MapModus. Klicke auf die erscheinende Schaltfläche **...** auf der rechten Seite. Wähle im Dialogfeld Anlage einen Knoten der Pfadskizze aus und wähle den richtigen Modus, um die beiden Skizzen richtig auszurichten).
2.  Drücke die **<img src="images/PartDesign_AdditivePipe.svg" width=24px> [Additives Rohr](PartDesign_AdditivePipe/de.md)** Schaltfläche.
3.  Wähle im Dialogfeld **Funktion auswählen** eine Skizze, die als Querschnitt verwendet werden soll, und klicke auf **OK**.
    -   Alternativ kann die Querschnittsskizze ausgewählt werden, bevor die Schaltfläche Additives Rohr gedrückt wird. In diesem Fall erhälst du kein Dialogfeld \"Funktion auswählen\".
    -   Drücke in den **Rohrparametern** unter **Pfad zum austragen** die **Objekt** Schaltfläche.
4.  Wähle die Skizze, die als Pfad in der 3D Ansicht verwendet werden soll. In diesem Fall wird die gesamte Skizze als Pfad verwendet.
    -   Alternativ können einzelne Kanten der Skizze durch drücken von


**Kante hinzufügen**

und Auswahl von Kanten in der 3D Ansicht ausgewählt werden. Beachte, dass du für jede Kante erneut die **Kante hinzufügen** drücken musst. Du musst eine durchgehende Linie ohne Verzweigungen auswählen.

1.  Die anderen Einstellungen sollten in den meisten Fällen mit den Standardeinstellungen funktionieren.
2.  Klicke auf **OK**.

Um mehr als einen Querschnitt zu verwenden, beginne mit der ersten Querschnittsskizze wie oben beschrieben. Stelle dann unter **Abschnittstransformation** den Transformationsmodus auf *Mehrfachabschnitt*; drücke **Abschnitt hinzufügen** und wähle dann eine Skizze in der [3D Ansicht](3D_view/de.md). Wiederhole diesen Vorgang für jeden zusätzlichen Querschnitt.

## Options


<div class="mw-translate-fuzzy">

## Optionen

\'\'\'Abschnitt Transformation\"\':

-   Wähle **Konstant**, um ein einzelnes Profil zu verwenden
-   Wähle **Mehrfachabschnitt**, um mehrere Profile zu verwenden

**Abschnittausrichtung**:

-   Standard

    :   Dadurch bleibt die Querschnittsform senkrecht zum Pfad erhalten. Dies ist die Standardeinstellung.
-   Fixiert
    -   Ausrichtung festgelegt durch das erste Profil und durchgehend konstant. Dadurch wird die Ausrichtung auf den Pfadnormalenvektor deaktiviert. Das bedeutet, dass sich die Querschnittsform nicht mit dem Pfad dreht. Streiche entlang eines Kreises, um den Effekt zu sehen.
-   Frenet
    -   Erstelle eine minimal mögliche Verdrehung des Profils. Für weitere Informationen siehe [Frenet-Serret Formeln](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).
-   zusätzlich
    -   Gib einen sekundären Pfad zur Führung des Rohrs an.
    -   Für jeden Punkt **P** entlang des Austragungspfades wird es einen entsprechenden Punkt **Q** auf dem Hilfspfad geben.
    -   Wenn das Profil ausgetragen wird, wird es so transformiert, dass die Linie **PQ** die Normale des Austragungspfades ist.
    -   Wenn **Krümmung** eingestellt ist, werden die **Q** Punkte proportional entlang des Austragungspfades skaliert, unabhängig von dessen Länge.
-   Binormal
    -   Binormalvektor in X, Y und Z angeben

**Eckübergang**

-   umgewandelt.
-   Rechts
-   Verrundet


</div>

## Eigenschaften

-    {{PropertyData/de|Label}}: Benennung des Features, kann beliebig geändert werden.

-    {{PropertyData/de|Refine}}: true oder false. Wenn der Wert auf \"true\" gesetzt ist, wird der Volumenkörper von verbleibenden Kanten bereinigt, die von Features übrig geblieben sind. Siehe [Part RefineShape](Part_RefineShape/de.md) für weitere Details.

-    {{PropertyData/de|Sections}}: listet die verwendeten Schnitte auf.

-    {{PropertyData/de|Spine Tangent}}: true oder false (Standard). True erweitert den Pfad um tangentiale Kanten.

-    {{PropertyData/de|Auxilary Spine tangent}}: true oder false (Standard). True erweitert den Hilfspfad um tangentiale Kanten.

-    {{PropertyData/de|Auxiliary Curvelinear}}: true oder false (Standard). True berechnet normal zwischen äquidistanten Punkten auf beiden Trägern.

-    {{PropertyData/de|Mode}}: Profilmodus. Siehe [ Optionen](#Optionen.md).

-    {{PropertyData/de|Binormal}}: binormaler Vektor für den entsprechenden Orientierungsmodus.

-    {{PropertyData/de|Transition}}: Übergangsmodus. Optionen sind \'\' Transformiert \'\', \'\' Rechte Ecke \'\' oder \'\' Runde Ecke \'\'.

-    {{PropertyData/de|Transformation}}: \'\' Constant \'\' verwendet einen einzelnen Querschnitt. \'\' Multisection \'\' verwendet zwei oder mehr Querschnitte. \'\' Linear \'\', \'\' S-Form \'\' und \'\' Interpolation \'\' sind zur Zeit nicht funktionsfähig.

## Begrenzungen


<div class="mw-translate-fuzzy">

-   Skizzen für Querschnitte müssen geschlossene Profile bilden.
-   Der Pfad kann nur von einer einzelnen Skizze, einer Funktion oder FormBinder stammen. Falls du entlang mehrerer Skizzen austragen möchtest, verwende einen **<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [SubShapeBinder](PartDesign_SubShapeBinder.md)**.
-   Der Pfad darf keine Verzweigungen oder T-Verbindungen usw. enthalten. Schleifen sind in Ordnung.
-   Es ist nicht möglich, einen Knoten als Querschnitt zu verwenden.
-   Es kann zu Problemen führen, wenn der Querschnitt nicht senkrecht zum Pfad in 3D steht (einige andere CAD Systeme betrachten den Ursprung des Querschnitts als Pfad und verlangen nicht, diese Skizze explizit zu platzieren).
-   Ein Querschnitt kann nicht auf der gleichen Ebene liegen wie die unmittelbar vorausgehende.
-   Um die Form des Rohres besser kontrollieren zu können, wird empfohlen, dass alle Querschnitte die gleiche Anzahl von Segmenten haben. Beispielsweise kann bei einem Rohr zwischen einem Rechteck und einem Kreis der Kreis in 4 zusammenhängende Bögen aufgeteilt werden.


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePipe/de
