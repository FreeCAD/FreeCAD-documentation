---
- GuiCommand:/de
   Name:PartDesign AdditivePipe
   Name/de:PartDesign RohrHinzufügen
   MenuLocation:Part Design → Objekt hinzufügen → Rohr
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign AustragungHinzufügen](PartDesign_AdditiveLoft/de.md), [PartDesign RohrAbziehen](PartDesign_SubtractivePipe/de.md)
---

# PartDesign AdditivePipe/de



## Beschreibung

**RohrHinzufügen** erstellt einen Volumenkörper im aktiven Bauteil, indem eine oder mehrere Skizzen (auch als Querschnitte bezeichnet) entlang eines offenen oder geschlossenen Pfads verschoben werden. Wenn das Bauteil bereits Formelemente enthält, wird das Rohr (AdditivePipe-Objrkt) mit ihnen vereinigt.

![](images/PartDesign_AdditivePipe_example.svg ) 
*Links: Querschnitt (A) wird entlang des Pfades (C) in den Querschnitt (B) überführt. Rechts: Das Ergebnis, ein AdditivePipe-Objekt.*



## Anwendung

Das obige Beispielbild zeigt zwei verschiedene Querschnittsformen. Im folgenden Text wird das Verfahren mit nur einer einzigen Form beschrieben. Das ergibt ein Teil mit dem gleichen Querschnitt entlang des gesamten Pfades.

1.  Zwei separate Skizzen erstellen;
    -   eine für den Pfad, z.B. zwei Linien, die durch eine Kurve verbunden sind, wie im obigen Bild,
    -   eine für die Querschnittsform, z.B. ein Kreis als erste Form in der obigen Abbildung. Anstatt einer Skizze kann auch die Fläche eines 3D-Objekts verwendet werden. ({{Version/de|0.20}})
    -   Beide Formen in 3D richtig **anordnen**. Es wird empfohlen den Ursprung der Querschnittsskizze auf die Linie des Pfades zu legen. Die beiden Skizzen sollten in den meisten Fällen **orthogonal** sein. Dies kann mit der Funktion \'Map Mode\' erfolgen (beide Skizzen mit der **Leertaste** sichtbar machen. Die Querschnittsskizze auswählen. Unter Eigenschaften/Daten/MapMode auswählen. Auf die auf der rechten Seite erscheinende Schaltfläche **...** klicken. Im Dialogfeld Attachment einen Knoten der Pfadskizze und dann den passenden Modus auswählen, um die beiden Skizzen richtig auszurichten).
2.  Die Schaltfläche (additives) **<img src="images/PartDesign_AdditivePipe.svg" width=24px> [Rohr](PartDesign_AdditivePipe/de.md)** drücken.
3.  Im Dialogfeld **Element auswählen** eine Skizze auswählen, die als Querschnitt verwendet werden soll, und auf **OK** klicken.
    -   Alternativ kann entweder eine einzelne Skizze oder die Fläche eines 3D-Objekts ({{Version/de|0.20}}) ausgewählt werden, bevor die Schaltfläche Rohr gedrückt wird. In diesem Fall erscheint das Dialogfeld \"Element auswählen\" nicht.
    -   In den **Rohrparametern** unter **Pfad der Austragung** die Schaltfläche **Objekt** drücken.
4.  Die Skizze, die als Pfad verwendet werden soll, in der 3D-Ansicht auswählen. In diesem Fall wird die gesamte Skizze als Pfad verwendet.
    -   Alternativ können einzelne Kanten der Skizze durch drücken von **Kante hinzufügen** und Auswahl von Kanten in der 3D-Ansicht ausgewählt werden. Nicht vergessen, dass die Schaltfläche **Kante hinzufügen** für jede Kante erneut gedrückt werden muss. Es muss eine durchgehende Linie ohne Verzweigungen ausgewählt werden.
5.  Die anderen Einstellungen sollten in den meisten Fällen mit den Standardeinstellungen funktionieren.
6.  Auf {{button|OK}} klicken.

Um mehr als einen Querschnitt zu verwenden, beginnt man mit der ersten Querschnittsskizze wie oben beschrieben, stellt dann unter **Abschnittstransformation** den Transformationsmodus auf *Mehrere Abschnitte*, drückt **Schnitt hinzufügen** und wählt dann eine Skizze in der [3D-Ansicht](3D_view/de.md) aus. Dieser Vorgang wird für jeden zusätzlichen Querschnitt wiederholt.



## Optionen

\'\'\'Abschnitt Transformation\"\':

-   Wähle **Konstant**, um ein einzelnes Profil zu verwenden
-   Wähle **Mehrere Abschnitte**, um mehrere Profile zu verwenden

**Ausrichtung des Abschnitts**:

-   Standard

    :   Dadurch bleibt die Querschnittsform senkrecht zum Pfad erhalten. Dies ist die Standardeinstellung.
-   Fixiert
    -   Ausrichtung festgelegt durch das erste Profil und durchgehend konstant. Dadurch wird die Ausrichtung auf den Pfadnormalenvektor deaktiviert. Das bedeutet, dass sich die Querschnittsform nicht mit dem Pfad dreht. Streiche entlang eines Kreises, um den Effekt zu sehen.
-   Frenet
    -   Erstelle eine minimal mögliche Verdrehung des Profils. Für weitere Informationen siehe [Frenet-Serret Formeln](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).
-   Zusatz
    -   Gib einen sekundären Pfad zur Führung des Rohrs an.
    -   Für jeden Punkt **P** entlang des Austragungspfades wird es einen entsprechenden Punkt **Q** auf dem Hilfspfad geben.
    -   Wenn das Profil ausgetragen wird, wird es so transformiert, dass die Linie **PQ** die Normale des Austragungspfades ist.
    -   Wenn **Krümmung** eingestellt ist, werden die **Q** Punkte proportional entlang des Austragungspfades skaliert, unabhängig von dessen Länge.
-   Binormale
    -   Binormalvektor in X, Y und Z angeben

**Eckübergang**

-   Transformiert.
-   Rechte Ecke
-   Runde Ecke



## Eigenschaften

-    {{PropertyData/de|Label}}: Benennung des Features, kann beliebig geändert werden.

-    {{PropertyData/de|Refine}}: true oder false. Wenn der Wert auf \"true\" gesetzt ist, wird der Volumenkörper von verbleibenden Kanten bereinigt, die von Features übrig geblieben sind. Siehe [Part RefineShape](Part_RefineShape/de.md) für weitere Details.

-    {{PropertyData/de|Sections}}: listet die verwendeten Schnitte auf.

-    {{PropertyData/de|Spine Tangent}}: true oder false (Standard). True erweitert den Pfad um tangentiale Kanten.

-    {{PropertyData/de|Auxilary Spine tangent}}: true oder false (Standard). True erweitert den Hilfspfad um tangentiale Kanten.

-    {{PropertyData/de|Auxiliary Curvelinear}}: true oder false (Standard). True berechnet normal zwischen äquidistanten Punkten auf beiden Trägern.

-    {{PropertyData/de|Mode}}: Profilmodus. Siehe [ Optionen](#Optionen.md).

-    {{PropertyData/de|Binormal}}: binormaler Vektor für den entsprechenden Orientierungsmodus.

-    {{PropertyData/de|Transition}}: Übergangsmodus. Optionen sind *Transformiert*, *Rechte Ecke* oder *Runde Ecke*.

-    {{PropertyData/de|Transformation}}: *Constant* verwendet einen einzelnen Querschnitt. *Multisection* verwendet zwei oder mehr Querschnitte. *Linear*, *S-Form* und *Interpolation* sind zur Zeit nicht funktionsfähig.



## Hinweise

-   Um die Form des Rohres besser steuern zu können, wird empfohlen, dass alle Querschnitte die gleiche Anzahl von Segmenten haben. Beispielsweise kann bei einem Rohr zwischen einem Rechteck und einem Kreis der Kreis in 4 zusammenhängende Bögen aufgeteilt werden.
-   Das Rohr kann mit einem einzelnen Knotenpunkt ([vertex](Glossary#V.md)) einer Skizze oder eines Körpers beginnen oder enden. {{Version/de|0.20}}
-   Wird ein Knotenpunkt als Querschnitt ausgewählt, muss es der letzte Abschnitt des Rohres sein. Andernfalls würde der Rohrkörper aus zwei an der spitze verbundenen Festkörpern bestehen. Dies würde gegen die Definition eines 3D-Objekts des CAD-Kernels verstoßen. Die Reihenfolge der Abschnitte kann durch verschieben dieser Abschnitte innerhalb der Liste angepasst werden.
-   Der Pfad kann nur von einer einzelnen Skizze, einem Formelement oder einem FormBinder stammen. Soll über mehrere Kanten verschiedener Skizzen ausgetragen werden, wird ein **[<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [SubShapeBinder](PartDesign_SubShapeBinder/de.md)** verwendet.
-   Der Pfad darf keine Verzweigungen oder T-Verbindungen usw. enthalten. Schleifen sind in Ordnung.
-   Es kann zu Problemen führen, wenn der Querschnitt in 3D nicht senkrecht zum Pfad steht.
-   Ein Querschnitt kann nicht auf derselben Ebene liegen wie der unmittelbar vorhergehende.
-   Es ist nicht möglich, unzusammenhängende oder sich kreuzende Konturen zu verwenden.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePipe/de
