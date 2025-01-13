---
 GuiCommand:
   Name: PartDesign AdditivePipe
   Name/de: PartDesign RohrHinzufügen
   MenuLocation: Part Design , Objekt hinzufügen , Rohr
   Workbenches: PartDesign_Workbench/de
   Version: 0.17
   SeeAlso: PartDesign_AdditiveLoft/de, PartDesign_SubtractivePipe/de
---

# PartDesign AdditivePipe/de



## Beschreibung

**RohrHinzufügen** erstellt einen Festkörper im aktiven Bauteil, indem eine oder mehrere Skizzen (auch als Querschnitte bezeichnet) entlang eines offenen oder geschlossenen Pfads verschoben werden. Wenn das Bauteil bereits Formelemente enthält, wird das Rohr (AdditivePipe-Objekt) mit ihnen vereinigt.

![](images/PartDesign_AdditivePipe_example.svg ) 
*Links: Querschnitt (A) wird entlang des Pfades (C) in den Querschnitt (B) überführt. Rechts: Das Ergebnis, ein AdditivePipe-Objekt.*



## Anwendung

Das obige Beispielbild zeigt zwei verschiedene Querschnittsformen. Im folgenden Text wird das Verfahren mit nur einer einzigen Form beschrieben. Das ergibt ein Teil mit dem gleichen Querschnitt entlang des gesamten Pfades.

1.  Zwei separate Skizzen erstellen;
    -   eine für den Pfad, z.B. zwei Linien, die durch eine Kurve verbunden sind, wie im obigen Bild,
    -   eine für die Querschnittsform, z.B. ein Kreis als erste Form in der obigen Abbildung. Anstatt einer Skizze kann auch die Fläche eines 3D-Objekts verwendet werden. ({{Version/de|0.20}})
    -   Beide Formen in 3D richtig **anordnen**. Es wird empfohlen den Ursprung der Querschnittsskizze auf die Linie des Pfades zu legen. Die beiden Skizzen sollten in den meisten Fällen **orthogonal** sein. Dies kann mit der Funktion \'Map Mode\' erfolgen (beide Skizzen mit der **Leertaste** sichtbar machen. Die Querschnittsskizze auswählen. Unter Eigenschaften/Daten/MapMode auswählen. Auf die auf der rechten Seite erscheinende Schaltfläche **...** klicken. Im Dialogfeld Attachment einen Knoten der Pfadskizze und dann den passenden Modus auswählen, um die beiden Skizzen richtig auszurichten).
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
3.  Die Schaltfläche (hinzuzufügendes) **<img src="images/PartDesign_AdditivePipe.svg" width=16px> [Rohr](PartDesign_AdditivePipe/de.md)** drücken.
    -   Den Menüeintrag **PartDesign → Objekte hinzufügen → <img src="images/PartDesign_AdditivePipe.svg" width=16px> Rohr** auswählen.
4.  Im Dialogfeld **Element auswählen** eine Skizze auswählen, die als Querschnitt verwendet werden soll, und auf **OK** klicken.
    -   Alternativ kann entweder eine einzelne Skizze oder die Fläche eines 3D-Objekts ({{Version/de|0.20}}) ausgewählt werden, bevor das Werkzeug gestartet wird. Dann wird dieser Dialog nicht geöffnet.
    -   In den **Rohrparametern** unter **Pfad der Austragung** die Schaltfläche **Objekt** drücken.
5.  Die Skizze, die als Pfad verwendet werden soll, in der 3D-Ansicht auswählen. In diesem Fall wird die gesamte Skizze als Pfad verwendet.
    -   Alternativ können einzelne Kanten der Skizze durch drücken von **Kante hinzufügen** und Auswahl von Kanten in der 3D-Ansicht ausgewählt werden. Nicht vergessen, dass die Schaltfläche **Kante hinzufügen** für jede Kante erneut gedrückt werden muss. Es muss eine durchgehende Linie ohne Verzweigungen ausgewählt werden.
6.  Die anderen Einstellungen sollten in den meisten Fällen mit den Standardeinstellungen funktionieren.
7.  Auf {{button|OK}} klicken.

Um mehr als einen Querschnitt zu verwenden, beginnt man mit der ersten Querschnittsskizze wie oben beschrieben, stellt dann unter **Abschnittstransformation** den Transformationsmodus auf *Mehrere Abschnitte*, drückt **Schnitt hinzufügen** und wählt dann eine Skizze in der [3D-Ansicht](3D_view/de.md) aus. Dieser Vorgang wird für jeden zusätzlichen Querschnitt wiederholt.



## Optionen

**Querschnittsänderung**:

-   **Konstant** auswählen, um ein einzelnes Profil zu verwenden
-   **Über mehrere Querschnitte** auswählen, um mehrere Profile zu verwenden

**Ausrichtung der Querschnitte**:

-   Standard

    :   Dies behält die Ausrichtung der Querschnittsform senkrecht zum Pfad bei. Dies ist die Standardeinstellung.
-   Starr
    -   Die Ausrichtung wird durch das erste Profil festgelegt und bleibt durchgehend konstant. Dadurch wird die Ausrichtung auf den Pfadnormalenvektor deaktiviert. Das bedeutet, dass sich die Querschnittsform nicht mit dem Pfad dreht. Wird die Form entlang eines Kreises ausgetragen, ist der Effekt deutlich zu sehen.
-   Frenet
    -   Erstellt die kleinstmögliche Verdrehung des Profils. Für weitere Informationen siehe [Frenet-Serret-Formeln](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).
-   Steuerkurve
    -   Einen sekundären Pfad zum Führen des Rohrs angeben.
    -   Für jeden Punkt **P** entlang des Austragungspfades gibt es einen entsprechenden Punkt **Q** auf dem Hilfspfad.
    -   Wenn das Profil ausgetragen wird, wird es so ausgerichtet, dass die Linie **PQ** im rechten Winkel zum Austragungspfad verläuft.
    -   Wenn **Gekrümmte Äquivalenz** eingestellt ist, werden die **Q** Punkte entlang des Austragungspfades proportional skaliert, unabhängig von dessen Länge.
-   Binormale
    -   Den binormalen Vektor in X, Y und Z angeben

**Eckübergang**

-   Transformiert.
-   Rechte Ecke
-   Runde Ecke



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein PartDesign-AdditivePipe-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|Add Sub Shape|PartShape|Hidden}}:

-    {{PropertyData/de|Base Feature|Link|Hidden}}:

-    {{PropertyData/de|_Body|LinkHidden|Hidden}}:


{{TitleProperty|Part Design}}

-    {{PropertyData/de|Refine}}: true oder false. Wenn auf true gesetzt, werden Festkörper von Kanten befreit, die nach erfolgten Formelementoperationen übriggeblieben sind. Siehe [Part FormAufbereiten](Part_RefineShape/de.md) für weitere Einzelheiten.


{{TitleProperty|Sketch Based}}

-    {{PropertyData/de|Profile|LinkSub}}: Referenz zur Skizze.

-    {{PropertyData/de|Midplane|Bool}}: Symmetrisch zur Skizzenebene extrudieren.

-    {{PropertyData/de|Reversed|Bool}}: Kehrt die Extrusionsrichtung um.

-    {{PropertyData/de|Up To Face|LinkSub}}: Fläche an der das Formelement endet.

-    {{PropertyData/de|Allow Multi Face|Bool}}: Mehrere Flächen im Profil zulassen.


{{TitleProperty|Sweep}}

-    {{PropertyData/de|Sections|LinkSubList}}: Listet die verwendeten Querschnitte.

-    {{PropertyData/de|Spine|LinkSub}}: Rückgratkurve (Pfad) an der entlang die Querschnitte verschoben werden.

-    {{PropertyData/de|Spine Tangent|Bool}}: true oder false (Standardwert). True erweitert die Rückgratkurve, wobei auch tangential anschließende Kanten verwendet werden.

-    {{PropertyData/de|Auxiliary Spine|LinkSub|Hidden}}: Führungskurve (sekundärer Pfad) zum Ausrichten (der Querschnitte) des Sweep-Objekts um die Rückgratkurve herum.

-    {{PropertyData/de|Auxiliary Spine Tangent|Bool}}: true oder false (Standardwert). True erweitert die Führungskurve, wobei auch tangential anschließende Kanten verwendet werden.

-    {{PropertyData/de|Auxiliary Curvelinear|Bool}}: true oder false (Standardwert). True berechnet die Normale zwischen Punkten mit gleichen Abständen auf Rückgratkurve und Führungskurve.

-    {{PropertyData/de|Mode|Enumeration}}: Profilmodus. Zur Auswahl stehen *Fixed*, *Frenet*, *Auxiliary* oder *Binormal*. Siehe [Optionen](#Optionen.md).

-    {{PropertyData/de|Binormal|Vector}}: Binormaler Vektor für den zugehörigen Ausrichtungsmodus.

-    {{PropertyData/de|Transition|Enumeration}}: Übergangsmodus. Zur Auswahl stehen *Transformed*, *Right Corner* oder *Round Corner*.

-    {{PropertyData/de|Transformation|Enumeration}}: *Constant* verwendet einen einzelnen Querschnitt. *Multisection* verwendet zwei oder mehr Querschnitte. *Linear*, *S-shape* und *Interpolation* funktionieren aktuell (noch) nicht.



## Hinweise

-   Um die Form des Rohres besser steuern zu können, wird empfohlen, dass alle Querschnitte die gleiche Anzahl von Segmenten haben. Beispielsweise kann bei einem Rohr zwischen einem Rechteck und einem Kreis der Kreis in 4 zusammenhängende Bögen aufgeteilt werden.
-   Das Rohr kann mit einem einzelnen Knotenpunkt ([vertex](Glossary#V.md)) einer Skizze oder eines Körpers beginnen oder enden. {{Version/de|0.20}}
-   Wird ein Knotenpunkt als Querschnitt ausgewählt, muss es der letzte Abschnitt des Rohres sein. Andernfalls würde der Rohrkörper aus zwei an der spitze verbundenen Festkörpern bestehen. Dies würde gegen die Definition eines 3D-Objekts des CAD-Kernels verstoßen. Die Reihenfolge der Abschnitte kann durch verschieben dieser Abschnitte innerhalb der Liste angepasst werden.
-   Der Pfad kann nur von einer einzelnen Skizze, einem Formelement oder einem FormBinder stammen. Soll über mehrere Kanten verschiedener Skizzen ausgetragen werden, wird ein [Teilformbinder](PartDesign_SubShapeBinder/de.md) verwendet.
-   Der Pfad darf keine Verzweigungen oder T-Verbindungen usw. enthalten. Schleifen sind in Ordnung.
-   Es kann zu Problemen führen, wenn der Querschnitt in 3D nicht senkrecht zum Pfad steht.
-   Ein Querschnitt kann nicht auf derselben Ebene liegen wie der unmittelbar vorhergehende.
-   Es ist nicht möglich, unzusammenhängende oder sich kreuzende Konturen zu verwenden.
-   Enthält die Skizze innere Geometrie, sollte die Reihenfolge, in der die Skizzengeometrien erstellt werden, für alle Querschnitte gleich sein. Entweder beginnt man alle Querschnitte mit der inneren Geometrie oder man beginnt alle mit der äußeren. Andernfalls wird ein ungültiges Rohrobjekt erstellt, bei dem sich innere und äußere Wandungen überkreuzen.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePipe/de
