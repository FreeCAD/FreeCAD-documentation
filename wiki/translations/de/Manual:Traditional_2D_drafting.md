 


{{Manual:TOC/de}}


<div class="mw-translate-fuzzy">

Möglicherweise bist du an FreeCAD interessiert, weil du bereits einige Erfahrung beim technischen Zeichnen hast, zum Beispiel mit Software wie [AutoCAD](https://de.wikipedia.org/wiki/AutoCAD). Oder du weist schon etwas über Design oder ziehst es vor, Dinge zu zeichnen, bevor du diese baust. In jedem Fall bietet FreeCAD einen eher herkömmlichen Arbeitsbereich, mit Werkzeugen, die in den meisten 2D CAD Anwendungen zu finden sind: Der [Entwurf Arbeitsbereich](Draft_Module/de.md).


</div>

Obwohl der Entwurf Arbeitsbereich Abläufe aus der herkömmlichen 2D CAD Welt übernimmt, ist er überhaupt nicht darauf beschränkt. All seine Werkzeuge funktionieren im gesamten 3D Bereich und viele der Entwurf Werkzeuge, z.B. <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Verschieben](Draft_Move/de.md) oder <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Drehen](Draft_Rotate/de.md), sind allgemein überall in FreeCAD verfügbar, weil sie oftmals viel intuitiver sind, als wenn die Einstellungen manuell geändert werden müssten.

Unter den vom Entwurf Arbeitsbereich angebotenen Werkzeugen findest du herkömmliche Werkzeuge wie <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Linie](Draft_Line/de.md), <img alt="" src=images/Draft_Circle.svg  style="width:16px;"> [Kreis](Draft_Circle/de.md), oder <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Polygonzug](Draft_Wire/de.md) (Polylinie), Änderungswerkzeuge wie <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Verschieben](Draft_Move/de.md), <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Drehen](Draft_Rotate/de.md) oder <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Versetzen](Draft_Offset/de.md), die/das[Arbeitsebene/Gittersystem](Draft_SelectPlane/de.md) festzulegen, das es Ihnen erlaubt, genau zu definieren, in welcher Ebene du arbeitest, und ein komplettes [Objektfang System](Draft_Snap/de.md), das es sehr einfach macht, Elemente zu zeichnen und präzise zueinander zu positionieren.

Um den Arbeitsablauf und die Möglichkeiten des Entwurf Arbeitsbereichs zu präsentieren, werden wir eine einfache Übung durchlaufen, deren Ergebnis diese kleine Zeichnung sein wird, die den Grundriss eines kleinen Hauses zeigt, das nur eine Küchenzeile enthält (ein ziemlich absurder Grundriss, aber wir können hier machen, was wir wollen, nicht wahr?):

![](images/Exercise_cabin_01.jpg )

-   Wechsle zum **Entwurf Arbeitsbereich**
-   Wie in jeder Technischen Zeichnungsanwendung ist es sinnvoll, die Umgebung korrekt einzurichten, denn dadurch werden Sie viel Zeit sparen. Passen Sie [Raster/Arbeitsebene](Draft_SelectPlane/de.md), [Texte](Draft_Text/de.md) und [Bemaßungen](Draft_Dimension/de.md) Einstellungen an Ihre Erfordernisse an im Menü **Bearbeiten → Einstellungen → Entwurf**. In dieser Übung werden wir allerdings so tun, als hätten wir die Standardwerte beibehalten.

![](images/Freecad_draft_options_01.jpg )

-   Eine Option könnte allerdings deine Aufmerksamkeit erfordern: die \"**Fülle Objekte wann immer möglich mit Flächen**\" Option. Wenn diese aktiviert ist, werden geschlossene Objekte wie Rechtecke oder Kreise als Standard mit einer Fläche gefüllt, was den Objektfang mit darunter liegenden Objekten erschwert. Du kannst jetzt diese Option deaktivieren, oder später die Eigenschaft \"**Fläche schaffen**\" jedes einzelnen Objekts deaktivieren, um die Flächenfüllung zu verhindern.

-   Der Draft-Arbeitsbereich hat auch zwei spezielle Symbolleisten: Eine mit **visuellen Einstellungen**, wo du die aktuelle Arbeitsebene setzen, den [Konstruktionsmodus](Draft_ToggleConstructionMode/de.md) an/aus, die Linienfarbe, Flächenfarbe, Liniendicke und Textgröße für neue Objekte setzen kannst und eine weitere mit **Fangorten**. Dort kannst du das Raster ein-/ausschalten und individuelle [Fangorte](Draft_Snap/de.md) setzen/aufheben:

![](images/Draft_toolbars.jpg )

-   Alle Fang Schaltflächen zu setzen ist bequem, es macht aber auch das Zeichnen langsamer, weil mehr Berechnungen durchgeführt werden, während du den Mauszeiger bewegst. Es ist oftmals besser, nur die zu setzen, die du tatsächlich benötigst.

-   Lass uns damit beginnen, den **Konstruktionsmodus** einzuschalten, der es uns erlaubt, einige Leitlinien zu ziehen, auf denen wir unsere endgültige Geometrie zeichnen werden.
-   Wenn Du möctest, setze die **Arbeitsebene** auf **XY**. Wenn du das tust, wird sich die Arbeitsebene nicht ändern, unabhängig von der aktuellen Ansicht. Wenn nicht, wird sich die Arbeitsebene automatisch an die aktuelle Ansicht anpassen, und du solltest darauf achten, dass du in der Draufsicht bleiben, wenn du in der XY (Grund) Ebene zeichnen willst.
-   Dann wähle das <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Rechteck](Draft_Rectangle/de.md) Werkzeug und zeichnen ein Rechteck, Startpunkt (0,0,0) und Größe 2m x 2m (Z bleibt bei Null). Beachte, dass die meisten der Entwurf Befehle mit den zwei-Zeichen Tastaturkürzeln eingegeben werden können, ohne die Maus zu berühren. Für unser erstes 2x2m Rechteck geht das wie folgt: re 0 **Enter** 0 **Enter** 0 **Enter** 2m **Enter** 2m **Enter** 0 **Enter**.
-   Dupliziere das Rechteck nach innen mit 15cm Abstand mit dem <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Versatz](Draft_Offset/de.md) Werkzeug, aktivieren den Kopiermodus und setze einen Abstand von 15cm:

![](images/Exercise_cabin_02.jpg )

-   Wir können dann mit dem <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Linie](Draft_Line/de.md)-Werkzeug eine Reihe von senkrechten Linien zeichnen, um festzulegen, wo unsere Türen und Fenster hinkommen (beachte, dass das \"Relativ\"-Kästchen bei diesem Schritt nicht aktiviert sein sollte). Die Kreuzung dieser Linien mit unseren zwei Rechtecken ergeben hilfreiche Schnittpunkte, an denen wir unsere Wände einrasten können. Zeichne die erste Linie vom Punkt (15cm, 1m, 0) zu Punkt (15cm, 3m, 0).
-   Dupliziere diese Linie fünf Mal mit dem <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Verschieben](Draft_Move/de.md)-Werkzeug und aktiviertem Kopieren-Modus. Aktiviere ebenfalls den Relativ-Modus, der es erlaubt, Bewegungen in relativen Abständen zu definieren, was einfacher ist als die exakte Position jeder Linie zu berechnen. Führe jede Verschieben-Operation der Reihe nach auf der Linie durch, die direkt vorher erstellt wurde. Gib jeder Kopie einen beliebigen Startpunkt, oder belasse ihn z.B. bei (0,0,0) und den folgenden relativen Endpunkten:
    -   line001: x: 10cm
    -   line002: x: 120cm
    -   line003: x: -55cm, y: -2m
    -   line004: x: 80cm
    -   line005: x: 15cm

![](images/Exercise_cabin_03.jpg )

-   Das ist alles, was wir jetzt brauchen, so dass wir den Konstruktionsmodus ausschalten können. Überprüfen Sie, dass all die gerade erzeugten Objekte in einer \"Konstruktions\" Gruppe zusammengefasst sind, denn das erleichtert das einfache Verstecken oder auch das spätere Löschen.
-   Lassen Sie uns mit dem <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Polygonzug](Draft_Wire/de.md) Werkzeug die beiden Wandteile zeichnen. Stelle sicher, dass der <img alt="" src=images/Snap_Intersection.svg  style="width:16px;"> [Schnittpunktfang](Draft_Snap/de.md) aktiviert ist, weil wir die Schnittpunkte von Linien und Rechtecken fangen wollen. Zeichne wie folgt zwei Polygonzüge durch anklicken aller Punkte der Umrisslinien. Zum Schließen klicke entweder erneut auf den ersten Punkt oder drücke die **Schließen** Schaltfläche:

![](images/Exercise_cabin_04.jpg )

-   Wir können ihre Standardfarbe grau in eine schöne Schraffur ändern, indem beide Wände selektiert, die \"Muster\" Eigenschaft auf **Einfach** und die **Mustergröße** auf beispielsweise **0,005** (oder einen anderen Wert) gesetzt werden.

![](images/Exercise_cabin_05.jpg )

-   Wir können jetzt die Konstruktionsgeometrie ausblenden, indem wir durch rechtsklicken der Konstruktiongruppe und **Auswahl ausblenden** wählen.
-   Lass uns nun die Fenster und Türen zeichnen. Stelle sicher, dass das <img alt="" src=images/Snap_Midpoint.svg  style="width:16px;"> [Mittelpunktsfang](Draft_Snap/de.md) aktiviert ist und zeichne sechs Linien wie folgt:

![](images/Exercise_cabin_06.jpg )

-   Wir werden jetzt die Türlinie ändern, um ein geöffnete-Tür-Symbol zu erzeugen. Starten Sie durch drehen der Linie mit dem <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Drehen](Draft_Rotate/de.md) Werkzeug. Klicken Sie den Endpunkt der Linie als Rotationszentrum, mit einem Startwinkel (Base angle) von **0** und einer Drehung (Rotation) von **-90**.
-   Dann erzeugen Sie einen Öffnungsbogen mit dem <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Kreisbogen](Draft_Arc/de.md) Werkzeug. Nehmen Sie den gleichen Punkt als Drehzentrum wie im vorigen Schritt, klicken Sie auf den anderen Endpunkt der Linie zur Festlegung des Radius, dann Start- und Endpunkt wie folgt:

![](images/Exercise_cabin_07.jpg )

-   Wir können jetzt mit dem Einbau einiger Möbel starten. Beginnen wir mit einer Theke, indem wir von der oberen linken, inneren Ecke ein Rechteck mit einer Breite von 170cm und einer Höhe von -60cm zeichnen. Auf dem folgenden Bild ist die **Transparency**-Eigenschaft des Rechtecks auf 80% gesetzt, um ihm ein nettes Möbelaussehen zu geben.
-   Dann lassen Sie uns ein Waschbecken und ein Kochfeld hinzufügen. Diese Art von Symbolen zu zeichnen kann ziemlich langweilig sein, und normalerweise sind sie im Internet einfach zu finden, z.B. auf <http://www.cad-blocks.net> . Im **Downloads**-Abschnitt unten haben wir einfachheitshalber ein Waschbecken (sink) und ein Kochfeld (cookertop) für dieses Projekt abgetrennt und als DXF Dateien gespeichert. Sie können diese beiden Dateien durch Besuch der Links aufrufen, und durch Rechtsklick auf **Raw** und dann **save as** herunterladen.
-   Einfügen einer DXF-Datei in ein geöffnetes FreeCAD-Dokument kann entweder über die **Datei → Import** Menü Option erfolgen oder durch drag-and-drop der DXF Datei aus dem Dateiexplorer in das FreeCAD Fenster. Der Inhalt der DXF Datei erscheint möglicherweise nicht direkt in der Mitte Ihrer aktuellen Ansicht, abhängig von den Einstellungen in der DXF Datei. Sie können über das Menü **Ansicht → Standardansichten → Einpassen** ausführen, um herauszuzoomen und die importierten Objekte zu finden. Fügen Sie die beiden DXF Dateien ein und verschieben diese an eine passende Stelle auf der Arbeitsfläche:

![](images/Exercise_cabin_08.jpg )

-   Wir können nun mit dem <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Bemaßung](Draft_Dimension/de.md) Werkzeug eine Reihe von Bemaßungen anbringen. Bemaßungen werden durch Klicken von drei Punkten gezeichnet: Der Startpunkt, ein Endpunkt und ein dritter Punkt zur Platzierung der Bemaßungslinie. Um waagerechte oder senkrechte Bemaßungen zu erstellen, selbst wenn die ersten beiden Punkte nicht fluchtend sind, drücken Sie **Shift** beim Anklicken des zweiten Punktes.
-   Sie können die Position eines Bemaßungstextes durch doppelklicken der Bemaßung in der Baumansicht ändern. Ein Kontrollpunkt erlaubt es Ihnen, den Text in der Zeichenfläche zu verschieben. In unserer Übung wurden die \"0.15\"-Texte zur besseren Übersicht verschoben.
-   Sie können den Inhalt des Bemaßungstextes durch Anpassung der **Override** Eigenschaft ändern. In unserem Beispiel wurden die Bemaßungstexte von Tür und Fenster geändert, um die Höhe anzugeben:

![](images/Exercise_cabin_09.jpg )

-   Lassen Sie uns mit dem <img alt="" src=images/Draft_Text.svg  style="width:16px;"> [Text](Draft_Text/de.md) Werkzeug etwas Beschreibungstext hinzufügen. Klicken Sie einen Punkt, um den Text zu positionieren und geben Sie die Textzeile(n) ein, drücken Sie Enter nach jeder Zeile. Zweimal Enter beendet die Eingabe.
-   Die Hinweislinien (auch \"leaders\" genannt), die die Texte mit dem Objekt verbinden, das sie beschreiben, werden einfach mit dem Polygonzug-Werkzeug erstellt. Zeichnen Sie Polygonzüge von der Textpositition bis zum Ort, der beschrieben wird. Dann können Sie eine Kugel oder Pfeil am Ende des Polygonzuges setzen, indem die **Endpfeil** Eigenschaft auf **True** gesetzt wird.

![](images/Exercise_cabin_10.jpg )

-   Unsere Zeichnung ist jetzt fertig! Da noch eine Reihe von Objekten vorhanden ist, wäre es klug, etwas aufzuräumen und alles in Gruppen zu restrukturieren, damit andere Leute diese Datei einfacher verstehen können:

![](images/Exercise_cabin_11.jpg )

-   Wir können nun unser Werk durch Platzierung auf einem Zeichenblatt ausdrucken, das wir später in diesem Manual zeigen werden oder unsere Zeichnung durch Export in eine DXF-Datei direkt für andere CAD-Anwendungen bereitstellen. Wählen Sie einfach unsere \"Grundriss\"-Gruppe, im Menü **Datei → Export** und dort das Autodesk DXF Format. Die Datei kann in einer beliebigen anderen 2D CAD Anwendung wie [LibreCAD](http://www.librecad.org) geöffnet werden. Möglicherweise werden Sie einige Unterschiede feststellen, abhängig von den Konfigurationen jeder Anwendung.

![](images/Exercise_cabin_12.jpg )


<div class="mw-translate-fuzzy">

-   Das Wichtigste am Entwurf Arbeitsbereich ist jedoch, dass die Geometrie, die du mit ihr erstellst, als Basis verwendet oder einfach in 3D Objekte extrudiert werden kann, indem du einfach das <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part\_Extrude](Part_Extrude.md) Werkzeug aus dem [Part Arbeitsbereich](Part_Workbench/de.md) oder, um im Entwurf zu bleiben, das <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Trimex](Draft_Trimex/de.md) (Trimmen/Strecken/Extrudieren) (engl.: Trim/Extend/Extrude) Werkzeug, das unter der Haube eine Teileextrusion durchführt, diese aber \"nach Entwurfsart\", d.h. es ermöglicht dir die Extrusionslänge grafisch anzeigen und fangen zu lassen. Experimentiere mit dem Extrudieren unserer Wände wie unten gezeigt.
-   Durch Drücken der <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [Arbeitsebene](Draft_SelectPlane/de.md) Schaltfläche kannst du nach der Auswahl einer Fläche eines Objekts auch die Arbeitsebene irgendwo platzieren und somit Entwurfsobjekte in verschiedenen Ebenen zeichnen, z.B. oben auf die Wände. Diese können dann extrudiert werden, um andere 3D Festkörper zu bilden. Experimentiere damit die Arbeitsebene auf eine der Oberseiten der Wände zu setzen, zeichne dann einige Rechtecke dort oben.


</div>

![](images/Exercise_cabin_13.jpg )

-   Alle Arten von Öffnungen können auch genauso leicht durch Zeichnen von Draft-Objekten auf den Wandflächen, Extrudieren der Objekte und dann Benutzen der booleschen Werkzeuge des Part-Arbeitsbereichs erzeugt werden, um diese vom Volumenkörper zu subtrahieren, wie wir im vorigen Kapitel sahen.

Im Wesentlichen bietet der Entwurf Arbeitsbereich grafische Möglichkeiten, um einfache Part-Operationen zu erledigen. Während Sie im Part-Arbeitsbereich normalerweise Objekte mit ihren Platzierungsparametern positionieren, können Sie das im Entwurf Arbeitsbereich direkt am Bildschirm tun. Es gibt Zeiten, wenn das Eine besser ist, und andere Zeiten, während man das Andere vorzieht. Vergessen Sie nicht, dass Sie [Angepasste Werkzeugleisten](Interface_Customization/de.md) in einem der Arbeitsbereiche anlegen können, Werkzeuge aus dem anderen hinzufügen können, und das Beste aus beiden Welten bekommen.

## Herunterladen

-   Die während dieser Übung erstellte Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.FCStd>
-   Die Waschbecken-DXF-Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/sink.dxf>
-   Die Kochfeld-DXF-Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cooktop.dxf>
-   Die endgültige von dieser Übung produzierte DXF-Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf>

## Verwandt


<div class="mw-translate-fuzzy">

-   [Der Entwurf Arbeitsbereich](Draft_Module/de.md)
-   [Fang](Draft_Snap/de.md)
-   [Die Entwurf Arbeitsebene](Draft_SelectPlane/de.md)


</div>




[Category:Tutorials{{\#translation:}}](Category:Tutorials.md) [Category:Draft{{\#translation:}}](Category:Draft.md)
