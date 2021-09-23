# SheetMetal Workbench/de

 

<img alt="Symbol des externen Arbeitsbereichs Blech" src=images/Sheetmetal_workbench_icon.svg  style="width:128px;">


{{TOCright}}

## Einführung

Der Arbeitsbereich <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> [Blech (Sheet Metal)](SheetMetal_Workbench/de.md) ist ein [Externer Arbeitsbereich](external_workbenches/de.md) und ist nicht Bestandteil der FreeCAD-Standardinstallation. Er wurde entwickelt, um Werkzeuge zum Erstellen und Abwickeln von Blechteilen zur Verfügung zu stellen.

Merkmale von Blechobjekten:

-   Sie haben eine konstante Wandstärke
-   Sie können abgewickelt werden, wenn sie nur aus ebenen Flächen und zylindrischen Verbindungen bestehen

Das Abwicklungswerkzeug ist in beiden Versionen nicht auf Teile beschränkt, die mit Werkzeugen dieser Arbeitsumgebung erstellt wurden, sondern kann auch mit Objekten aus den Arbeitsbereichen [Part](Part_Workbench/de.md) and [PartDesign](PartDesign_Workbench/de.md) umgehen, die den oben genannten Merkmalen entsprechen.

<img alt="" src=images/SheetMetal_Example.png  style="width:600px;"> 
*Das mit der Blech-Erweiterung gebaute Blechmodell (hinten); davor der abgewickelte Volumenkörper; Im Vordergrund die Abwicklungsskizze mit Biegelinien für den DXF-Export.*

Wenn der DXF-Export zur Steuerung von Maschinen (z. B. Laserschneiden) verwendet wird, muss die DXF Datei geändert werden, um die Biegelinien zu entfernen, da diese Linien von der Maschine (irrtümlich) als Schnittkontur interpretiert werden könnten.

## Einrichtung

Dieser Arbeitsbereich kann über den [Erweiterungsverwalter](Std_AddonMgr/de.md) installiert werden. Für die manuelle Installation siehe [Weitere Arbeitsbereiche installieren](Installing_more_workbenches.md).

## Werkzeuge

Eine detaillierte Beschreibung der Werkzeuge kann unter [Blog des Autors](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/) gefunden werden. Sie ist jetzt etwas veraltet, da inzwischen einige neue Werkzeuge hinzugekommen sind.

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Basisprofil erstellen](SheetMetal_AddBase/de.md): Erzeugt ein Blechprofil aus einer Skizze.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Kante ansetzen](SheetMetal_AddWall/de.md): Setzt eine weitere Kante an eine gewählte Randfläche des Blechobjekts an.

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Fläche erweitern](SheetMetal_Extrude/de.md): Erweitert eine Seitenfläche entlang der Flächennormalen.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Abkanten](SheetMetal_AddFoldWall/de.md): Biegt eine Fläche entlang einer gewählten Linie mit vorgegebenem Radius.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Abwickeln](SheetMetal_Unfold/de.md): Ebnet ein gekantetes Blechobjekt und erzeugt einen Abwicklungskörper und eine Skizze (stellt ein Fenster zum Festlegen von Parametern bereit).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Abwickeln ohne Eingaben](SheetMetal_UnattendedUnfold/de.md): Ebnet ein gekantetes Blechobjekt und erzeugt einen Abwicklungskörper und eine Skizze (wenn die Parameter bereits festgelegt sind).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Eckentlastung hinzufügen](SheetMetal_AddCornerRelief/de.md): Fügt einer Ecke einen Ausschnitt zur Eckentlastung hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md): Fügt einer Ecke einen Entlastungsausschnitt hinzu.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Stoß hinzufügen](SheetMetal_AddJunction/de.md): Fügt einen Stoß mit Spalt auf der Kante zweier Wände ein.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Bogen einfügen](SheetMetal_AddBend/de.md): Fügt eine Ausrundung an Stelle einer eckigen Kante ein.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Skizze auf Blech](SheetMetal_SketchOnSheet/de.md): Schneidet ein Loch in ein Blechobjekt, auf Basis einer Skizze.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Prägen](SheetMetal_Forming/de.md): Werkzeug fügt eine Einprägung hinzu.


</div>

## Brief description 

This workbench provides tools for the two main tasks:

-   Create sheet metal objects
-   Unfold sheet metal objects

This section is meant to give a rough idea of how to use the supplied tools. More detailed information can be found on each tool\'s own page (see above) or in the linked tutorials (see below).

### Create a sheet metal object 

#### Start with a profile 

1.  Create an open polyline (preferably with the sketcher)
2.  Use the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase.md) command to create a sheet metal profile.

#### Start with a blank 

1.  Create a closed polyline (preferably with the sketcher)
2.  Use the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase.md) command to create a sheet metal blank.

#### Start with a PartDesign Pad 

1.  Create a closed polyline (preferably with the sketcher)
2.  Use the <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad.md) command to create a prismatic body.
3.  The <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [PartDesign Thickness](PartDesign_Thickness.md) command will make it an object of constant thickness.
4.  To make it unfoldable it needs some gaps or connections between the walls:
    1.  The <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> [Make Relief](SheetMetal_AddRelief.md) command will cut off selected corners.
    2.  The <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> [Make Junction](SheetMetal_AddJunction.md) command will create junctions with gaps between adjoining walls that need to be disjoined.
    3.  The <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> [Make Bend](SheetMetal_AddBend.md) command will create cylindrical connections for the remaining walls that need to stay joined.

Some parameters will be inherited from the parent object(s) but it is better to check the relevant parameters at each stage.

It should now be checked if the resulting sheet metal object can be unfolded. (see [Unfold\...](#Unfold_a_sheet_metal_object.md) below).

#### Adding more features 

The unfoldable basic sheet metal objects can be extended:

1.  Use the <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> [Extend Face](SheetMetal_Extrude.md) command to enlarge walls.
2.  The <img alt="" src=images/SheetMetal_AddWall.svg  style="width:16px;"> [Make Wall](SheetMetal_AddWall.md) command will add new walls to the existing object.
3.  Use the <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:16px;"> [Add Corner Relief](SheetMetal_AddCornerRelief.md) command to add or reshape corner reliefs.
4.  The <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:16px;"> [Fold a Wall](SheetMetal_AddFoldWall.md) command will fold a wall at a chosen line, i.e. it will trimm a wall at said line, relocate the cut away side, and rejoin them with a cylindrical connection.
5.  Use the <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Sketch on Sheet metal](SheetMetal_SketchOnSheet.md) command to cut holes into the object starting on a chosen wall and then following the adjoined walls and connections.
6.  The <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming.md) command will stamp a shape into a wall.

Several tools from other workbenches can be used to add holes or to reshape edges.

### Unfold a sheet metal object 

To unfold a sheet metal object aktivate the <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) or the <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:16px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md) tool.

The result will be a 3D object with an optional outline sketch including bend lines.

### Examples

Until tutorial pages are available on this wiki there is an [Examples](SheetMetal_Examples.md) page.

<img alt="" src=images/SheetMetal_Example-01.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-02.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:100px;">

## Begrenzungen

-   Der Arbeitsbereich ist betroffen von dem mit FreeCAD verbundenen [topological naming issue](Glossary#Topological_Naming.md). Wenn bei der Bearbeitung einer in der Geschichte des Teils früheren Biegung die Flächen neu nummeriert werden, können die folgenden Biegungen betroffen sein und die Flächen vertauscht werden. Wenn die Biegungsmerkmale nicht brechen, kannst Du darauf doppelklicken, um ein Dialogfeld zu erhalten, in dem du die richtige Fläche in der [3D Ansicht](3D_view/de.md) auswählen und die Biegung aktualisieren kannst.
-   Das Entfalten Werkzeug hat einige Einschränkungen und versagt in bestimmten komplexen Situationen. Wenn es fehlschlägt, versuche eine andere Fläche auszuwählen.
-   Häufiger Crash Fall: Treffe viele Vorsichtsmaßnahmen, um nicht in die Gelenke (die Faltungen) weder entlang der Flächen oder in den Winkeln einzuschneiden noch Löcher oder Ausklinkungen durch die Winkel zu machen.

## Tutorien


<div class="mw-collapsible mw-collapsed toccolours" style="width:800px">

### Blech Tutorium von meme2704 

Das folgende Tutorium ist aus dem in [Links](#Links.md) erwähnten PDF Tutorium nachgebildet.


<div class="mw-collapsible-content">

#### Vorstellung des Arbeitsbereichs 

Nach dem herunterladen und installieren der Erweiterung, öffne sie. ![](images/sm1.png )

#### 1st operation 


<div class="mw-translate-fuzzy">

#### 1. Arbeitsgang

-   Hole die Grundlage: benutze entweder die Arbeitsbereiche \"Part\" oder \"Entwurf\", mache 1 Skizze, die alle Löcher und eventuelle Schnitte enthält, extrudiere diese Grundlage auf die Dicke der Platte.
-   Denk daran, dass die Kanten immer zusätzlich sein werden genauso wie die Falzradien.


</div>

![](images/sm2.png )

#### 2nd operation 


<div class="mw-translate-fuzzy">

#### 2. Arbeitsgang 

-   Öffne den Blech Arbeitsbereich.
-   Wähle 1 Dicke der Kante (Kante) der Grundplatte und klicke auf das Werkzeug \"Biegen\". 90° Vorgabe Biegewinkel kann von 0 bis 90 ° geändert werden.
-   Die Kantenhöhe beträgt standardmäßig 10 mm und kann von 0,1 bis xxx mm bearbeitet werden.
-   Der Biegeradius entspricht standardmäßig der Dicke und kann von 0,1 bis xx mm (niemals 0) geändert werden.
-   Spalt1, Spalt2 ist das Zurückziehen der gefalteten Kante aus der Ecke der Basis (0 akzeptieren).
-   Standard umkehren: Falschfalten auf Z +, Wahr auf ZReliefd schneidet die Ecke zwischen der Falte und der Basis (inaktiv, wenn Spalt = 0).
-   Reliefw fügt 1 Schlitz zwischen dem Zuschnitt und der Kante hinzu (inaktiv, wenn reliefd = 0).


</div>

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

#### Unfolding


<div class="mw-translate-fuzzy">

#### Entfalten

Wähle eine Referenzfläche (hier die orangene Fläche) und klicke auf die Schaltfläche in der Werkzeugleiste.
Wir erhalten den blauen Teil, von dem es ausreicht, die Werte X, Y oder Z zu ändern, um ihn als Ganzes zu sehen.


</div>

![](images/sm6.png )

#### Cut the flaps at 45° 


<div class="mw-translate-fuzzy">

#### Schneide die Umschläge bei 45 ° 

Nach dem Falten der Umschläge ohne das ein Rücknahme gemacht wurde, dadurch erscheint die Form.


</div>

![](images/sm7a.png ) Um es zu tun muss bei 45 ° geteilt werden (oder die folgenden Halbierenden Umschläge sind ungleich breit).
\* Erstelle eine neuen Skizze bezogen auf den gemeinsamen Teil der beiden Umschläge.

-   Erstelle einen verknüpften Anschlag, durch Wahl der Außenkante des \"Scharniers\".
-   Zeichne ein Dreieck, dessen Spitze am Ende begrenzt ist und eine Seite in 45 ° ausgerichtet ist, geben Sie der kleinen Seite 1 Mindestbreite (0,1 mm sind ausreichend) und fertigen Sie eine Tasche an.

Achten Sie darauf, nicht das \"Scharnier\" zu zerkratzen, bei dem die Nacktheit die Spitze des Dreiecks am Rand der Faltlinie gebunden hat. ![](images/sm8a.png ) Abwicklung ![](images/sm9.png )

#### Piercing edges and flaps 


<div class="mw-translate-fuzzy">

#### Kanten und Umschläge durchstechen 

Machen Sie diese Löcher und Schnitte nach dem Falten und vor dem Entfalten.
Achten Sie immer darauf, die Falzlinien nicht zu \"zerkratzen\".


</div>

![](images/sm10.png )

#### Make wired flaps 


<div class="mw-translate-fuzzy">

#### Verdrahtete Umschläge herstellen 

Mache eine Falte an der Kante der Seite, bei 45 ° von 0,1 mm Länge, dann eine andere umgekehrt bei 45 ° der Länge des benachbarten Umschlags, dann verlängere die gegenüberliegende Seite, sie wird übergehen und sie werden nicht zusammengeführt.


</div>

![](images/sm11.png )

#### Special case of this same pierced edge 


<div class="mw-translate-fuzzy">

#### Sonderfall derselben durchstochenen Kante 

In diesem speziellen Fall funktioniert das Entfalten nur, indem die gelbe Fläche als Referenz ausgewählt wird.


</div>

![](images/sm12.png )

#### Special case hole straddling the folds 


<div class="mw-translate-fuzzy">

#### Sonderfall Loch überspannt die Falten 

Zuvor wurde mehrmals gesagt, dass es nicht notwendig ist, die Faltlinien zu schneiden.
Was macht man ?


</div>

![](images/sm13.png )

-   Mache die Basis mit seinem halbrunden Loch und mache die beiden halbseitigen und die beiden halben Falten getrennt.
-   Mache dann eine Verlängerung auf einer der Seiten der Breite der Öffnung minus 0,1 mm, die beiden Kanten bleiben somit getrennt.
-   Dann auf dieser Verlängerung (in grün) die Kontur des Schnitts zeichnen und eine Tasche machen
-   Das Ergebnis ist das rote Stück darüber, und die Entfaltung funktioniert, bleibt die Linie, die die beiden Kanten zuvor getrennt hat

![](images/sm14.png )


</div>


</div>

## Videos


<div class="mw-translate-fuzzy">

## Videos 

-   [The Elegant Sheet Metal Workbench](https://www.youtube.com/watch?v=xidvQYkC4so) von Joko Engineering


</div>

## Verweise


<div class="mw-translate-fuzzy">

-   [Macro Sheet Metal Unfolder](Macro_Sheet_Metal_Unfolder.md), das ursprüngliche Makro, auf dem das Entfaltungswerkzeug basiert.
-   [Sheet Metal Arbeitsbereich](https://forum.freecadweb.org/viewtopic.php?t=11303) Ankündigung im FreeCAD Forum
-   [Ein englisches und französisches Tutorial im PDF Format](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) im FreeCAD Forum
-   Dateien:
-   Fehler melden/ Merkmale anfordern: <https://github.com/shaise/FreeCAD_SheetMetal/issues>


</div>

## Referenzen

-   Autoren:
    -   Falt Werkzeuge: Urheberrecht 2015-2018 liegt bei Shai Seger
    -   Abwicklungs-Werkzeuge: Urheberrecht 2014 liegt bei Ulrich Brammer
-   Lizenz: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
-   Offizieller Blog: [Sheet metal Addon for FreeCAD](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/)
-   Quellcode auf github: <https://github.com/shaise/FreeCAD_SheetMetal>

[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)
