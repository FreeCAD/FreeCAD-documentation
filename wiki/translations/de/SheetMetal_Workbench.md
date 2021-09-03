


{{UnfinishedDocu

}} <img alt="Blech Externer Arbeitsbereich Symbol" src=images/Sheetmetal_workbench_icon.svg  style="width:128px;">

## Überblick


{{TOCright}}

<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> **Blech** ist ein [Externer Arbeitsbereich](external_workbenches/de.md) entwickelt zum Entwerfen und Abwickeln von Blechteilen. Daher ist es nicht Teil der Standard FreeCAD Installation.

<img alt="" src=images/SheetMetal_Example.png  style="width:600px;"> 
*Das mit dem Blech Erweiterung gebaute Blechmodell (hinten); davor der abgewickelte Volumenkörper; Im Vordergrund die Abwicklungsskizze mit Biegelinien für den Export nach DXF.*

Wenn der Export nach DXF zur Steuerung von Maschinen (z. B. Laserschneiden) verwendet wird, muss die DXF Datei geändert werden, um die Linien zu entfernen, die die Falten anzeigen, da diese Linien möglicherweise zum Schneiden durch die Maschine verwendet werden.

## Einrichtung

Dieser Arbeitsbereich kann über den [Erweiterungsverwalter](Std_AddonMgr/de.md) installiert werden. Für die manuelle Installation siehe [Weitere Arbeitsbereiche installieren](Installing_more_workbenches.md).

## Werkzeuge

Eine detaillierte Beschreibung der Werkzeuge kann unter [Blog des Autors](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/) gefunden werden.

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Basisprofil erstellen](SheetMetal_AddBase/de.md): Erzeugt eine Blechwandung aus einer Skizze.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Kante hinzufügen](SheetMetal_AddWall/de.md): Erweitert eine Seitenfläche des Bleches um eine Kante (Flansch, (Blech-) Streifen).

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Kante verlängern](SheetMetal_Extrude/de.md): Erweitert eine Seitenfläche entlang der Flächennormalen.

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Abkanten](SheetMetal_AddFoldWall/de.md): Biegt eine Fläche entlang einer gewählten Linie mit vorgegebenem Radius.

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Abwickeln](SheetMetal_Unfold/de.md): Ebnet ein gekantetes Blechobjekt und erzeugt einen Abwicklungskörper und eine Skizze (stellt ein Fenster zum Festlegen von Parametern bereit).

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Unattended Abwickeln](SheetMetal_UnattendedUnfold/de.md): Ebnet ein gekantetes Blechobjekt und erzeugt einen Abwicklungskörper und eine Skizze (wenn die Parameter bereits festgelegt sind).

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Eckentlastung hinzufügen](SheetMetal_AddCornerRelief/de.md): Fügt einer Ecke einen Ausschnitt zur Eckentlastung hinzu.

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md): Fügt einer Ecke einen Entlastungsausschnitt hinzu.

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Stoß hinzufügen](SheetMetal_AddJunction/de.md): Fügt einen Stoß mit Spalt auf der Kante zweier Wände ein.

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Biegung hinzufügen](SheetMetal_AddBend/de.md): Fügt eine Ausrundung an Stelle einer eckigen Kante ein.

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Skizze auf Blech](SheetMetal_SketchOnSheet/de.md): Schneidet ein Loch in ein Blechobjekt, auf Basis einer Skizze.

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Wand einprägen](SheetMetal_Forming/de.md): Werkzeug fügt eine Einprägung hinzu.

## Zwei sich gegenseitig ergänzende Werkzeuge {#zwei_sich_gegenseitig_ergänzende_werkzeuge}

### Erstelle ein Basisprofil {#erstelle_ein_basisprofil}

Omega förmiges Werkzeug: Mache ein Teil aus einer einfachen mehrzeiligen Linie, die in Skizze oder Entwurf erstellt wurde, gib ihm Höhe und Dicke mittig, links oder rechts von dieser Linie, achte darauf, keine Selbstüberschneidung in geschlossenen Faltungen von weniger Raum als die Materialstärke zu erzeugen.

### Falten entlang einer Linie {#falten_entlang_einer_linie}

Falte eine \"flache\" Grundplatte entlang einer Linie (von einer Linie durchkreuztes Rechteck): wähle die Fläche, dann die Linie und das Werkzeug, wähle den Winkel, den Radius, die Seite, die Position der Faltung relativ zur Linie ist nicht sehr gut definiert; es scheint, dass die Linie die Schnittkante in der Verlängerung der 2 Flächen ist.

## Begrenzungen

-   Der Arbeitsbereich ist betroffen von dem mit FreeCAD verbundenen [topological naming issue](Glossary#Topological_Naming.md). Wenn bei der Bearbeitung einer in der Geschichte des Teils früheren Biegung die Flächen neu nummeriert werden, können die folgenden Biegungen betroffen sein und die Flächen vertauscht werden. Wenn die Biegungsmerkmale nicht brechen, kannst Du darauf doppelklicken, um ein Dialogfeld zu erhalten, in dem du die richtige Fläche in der [3D Ansicht](3D_view/de.md) auswählen und die Biegung aktualisieren kannst.
-   Das Entfalten Werkzeug hat einige Einschränkungen und versagt in bestimmten komplexen Situationen. Wenn es fehlschlägt, versuche eine andere Fläche auszuwählen.
-   Häufiger Crash Fall: Treffe viele Vorsichtsmaßnahmen, um nicht in die Gelenke (die Faltungen) weder entlang der Flächen oder in den Winkeln einzuschneiden noch Löcher oder Ausklinkungen durch die Winkel zu machen.

## Tutorien


<div class="mw-collapsible mw-collapsed toccolours" style="width:800px">

### Blech Tutorium von meme2704 {#blech_tutorium_von_meme2704}

Das folgende Tutorium ist aus dem in [Links](#Links.md) erwähnten PDF Tutorium nachgebildet.


<div class="mw-collapsible-content">

#### Vorstellung des Arbeitsbereichs {#vorstellung_des_arbeitsbereichs}

Nach dem herunterladen und installieren der Erweiterung, öffne sie. ![](images/sm1.png )

#### 1. Arbeitsgang

-   Hole die Grundlage: benutze entweder die Arbeitsbereiche \"Part\" oder \"Entwurf\", mache 1 Skizze, die alle Löcher und eventuelle Schnitte enthält, extrudiere diese Grundlage auf die Dicke der Platte.
-   Denk daran, dass die Kanten immer zusätzlich sein werden genauso wie die Falzradien.

![](images/sm2.png )

#### 2. Arbeitsgang {#arbeitsgang_1}

-   Öffne den Blech Arbeitsbereich.
-   Wähle 1 Dicke der Kante (Kante) der Grundplatte und klicke auf das Werkzeug \"Biegen\". 90° Vorgabe Biegewinkel kann von 0 bis 90 ° geändert werden.
-   Die Kantenhöhe beträgt standardmäßig 10 mm und kann von 0,1 bis xxx mm bearbeitet werden.
-   Der Biegeradius entspricht standardmäßig der Dicke und kann von 0,1 bis xx mm (niemals 0) geändert werden.
-   Spalt1, Spalt2 ist das Zurückziehen der gefalteten Kante aus der Ecke der Basis (0 akzeptieren).
-   Standard umkehren: Falschfalten auf Z +, Wahr auf ZReliefd schneidet die Ecke zwischen der Falte und der Basis (inaktiv, wenn Spalt = 0).
-   Reliefw fügt 1 Schlitz zwischen dem Zuschnitt und der Kante hinzu (inaktiv, wenn reliefd = 0).

![](images/sm3.png ) Wiederhole diesen Vorgang so oft, wie Seiten zum biegen vorhanden sind.
Falten 1 Wiederholung mit Gebrauch von \"vergrößern\".
![](images/sm4a.png ) Um eine wieder hinzuzufügen, wiederhole den gleichen Arbeitsgang, indem die Dicke der betreffenden Kante ausgewählt wird.
Um den Abstand zwischen 2 Kanten zu verringern, verwende \"ausdehnen\", um den Abstand zwischen den beiden Kanten zu verringern.
Wähle die Dicke und gib die Länge an, die hinzugefügt werden soll.
Beachte, dass wenn die Verlängerung der 1. Kante vor dem Falzen der Wiederholung erfolgt, dies nicht berücksichtigt wird. Wenn der Verlängerung eine identische Faltung hinzugefügt wird, wird dies korrekt angezeigt, aber das Abwickeln wird nicht durchgeführt.
Falzen von einer 2. Kante:
Jetzt müssen wir die beiden Kanten trennen, da sie sonst zusammenlaufen und sich nicht mehr entfalten lassen.
\* Erste Methode: Entfernen einer Kante vornehmen.

-   -   Gib einen Wert an, der geringfügig größer als Spalt1 (oder Spalt2) ist. Bei Null besteht noch Verbindung.

-   2\. Methode einen Schnitt bei 45 ° machen, siehe weiter, dieses Werkzeug verwenden.

![](images/sm5a.png )

#### Entfalten

Wähle eine Referenzfläche (hier die orangene Fläche) und klicke auf die Schaltfläche in der Werkzeugleiste.
Wir erhalten den blauen Teil, von dem es ausreicht, die Werte X, Y oder Z zu ändern, um ihn als Ganzes zu sehen.
![](images/sm6.png )

#### Schneide die Umschläge bei 45 ° {#schneide_die_umschläge_bei_45}

Nach dem Falten der Umschläge ohne das ein Rücknahme gemacht wurde, dadurch erscheint die Form. ![](images/sm7a.png ) Um es zu tun muss bei 45 ° geteilt werden (oder die folgenden Halbierenden Umschläge sind ungleich breit).
\* Erstelle eine neuen Skizze bezogen auf den gemeinsamen Teil der beiden Umschläge.

-   Erstelle einen verknüpften Anschlag, durch Wahl der Außenkante des \"Scharniers\".
-   Zeichne ein Dreieck, dessen Spitze am Ende begrenzt ist und eine Seite in 45 ° ausgerichtet ist, geben Sie der kleinen Seite 1 Mindestbreite (0,1 mm sind ausreichend) und fertigen Sie eine Tasche an.

Achten Sie darauf, nicht das \"Scharnier\" zu zerkratzen, bei dem die Nacktheit die Spitze des Dreiecks am Rand der Faltlinie gebunden hat. ![](images/sm8a.png ) Abwicklung ![](images/sm9.png )

#### Kanten und Umschläge durchstechen {#kanten_und_umschläge_durchstechen}

Machen Sie diese Löcher und Schnitte nach dem Falten und vor dem Entfalten.
Achten Sie immer darauf, die Falzlinien nicht zu \"zerkratzen\".
![](images/sm10.png )

#### Verdrahtete Umschläge herstellen {#verdrahtete_umschläge_herstellen}

Mache eine Falte an der Kante der Seite, bei 45 ° von 0,1 mm Länge, dann eine andere umgekehrt bei 45 ° der Länge des benachbarten Umschlags, dann verlängere die gegenüberliegende Seite, sie wird übergehen und sie werden nicht zusammengeführt.
![](images/sm11.png )

#### Sonderfall derselben durchstochenen Kante {#sonderfall_derselben_durchstochenen_kante}

In diesem speziellen Fall funktioniert das Entfalten nur, indem die gelbe Fläche als Referenz ausgewählt wird.
![](images/sm12.png )

#### Sonderfall Loch überspannt die Falten {#sonderfall_loch_überspannt_die_falten}

Zuvor wurde mehrmals gesagt, dass es nicht notwendig ist, die Faltlinien zu schneiden.
Was macht man ?
![](images/sm13.png )

-   Mache die Basis mit seinem halbrunden Loch und mache die beiden halbseitigen und die beiden halben Falten getrennt.
-   Mache dann eine Verlängerung auf einer der Seiten der Breite der Öffnung minus 0,1 mm, die beiden Kanten bleiben somit getrennt.
-   Dann auf dieser Verlängerung (in grün) die Kontur des Schnitts zeichnen und eine Tasche machen
-   Das Ergebnis ist das rote Stück darüber, und die Entfaltung funktioniert, bleibt die Linie, die die beiden Kanten zuvor getrennt hat

![](images/sm14.png )


</div>


</div>

## Videos

-   [The Elegant Sheet Metal Workbench](https://www.youtube.com/watch?v=xidvQYkC4so) von Joko Engineering

## Verweise

-   [Macro Sheet Metal Unfolder](Macro_Sheet_Metal_Unfolder.md), das ursprüngliche Makro, auf dem das Entfaltungswerkzeug basiert.
-   [Sheet Metal Arbeitsbereich](https://forum.freecadweb.org/viewtopic.php?t=11303) Ankündigung im FreeCAD Forum
-   [Ein englisches und französisches Tutorial im PDF Format](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) im FreeCAD Forum
-   Dateien:
-   Fehler melden/ Merkmale anfordern: <https://github.com/shaise/FreeCAD_SheetMetal/issues>

## Referenzen

-   Autoren:
    -   Falt Werkzeuge: Urheberrecht 2015-2018 liegt bei Shai Seger
    -   Abwicklungs-Werkzeuge: Urheberrecht 2014 liegt bei Ulrich Brammer
-   Lizenz: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
-   Offizieller Blog: [Sheet metal Addon for FreeCAD](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/)
-   Quellcode auf github: <https://github.com/shaise/FreeCAD_SheetMetal>

## Externe Arbeitsbereiche {#externe_arbeitsbereiche}

FreeCAD Arbeitsbereiche sind einfach in [Python](Python.md) zu programmieren. Daher entwickeln viele Leute zusätzliche Arbeitsbereiche außerhalb der FreeCAD Hauptentwickler.

Auf der Seite [external workbenches](external_workbenches.md) findest Du einige Informationen und Tutorien zu einigen von ihnen. Das Projekt [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) hat zum Ziel, diese zusammenzustellen und leicht installierbar aus FreeCAD heraus zu machen.

Neue Arbeitsbereiche sind in der Entwicklung, bleib dran!

[Category:SheetMetal{{\#translation:}}](Category:SheetMetal.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)
