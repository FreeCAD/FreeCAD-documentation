# <img alt="Symbol des externen Arbeitsbereichs Blech" src=images/Sheetmetal_workbench_icon.svg  style="width:64px;"> SheetMetal Workbench/de


{{TOCright}}

## Einführung

Der Arbeitsbereich <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> [Blech (Sheet Metal)](SheetMetal_Workbench/de.md) ist ein [Externer Arbeitsbereich](External_workbenches/de.md) und ist nicht Bestandteil der FreeCAD-Standardinstallation. Er wurde entwickelt, um Werkzeuge zum Erstellen und Abwickeln von Blechobjekten zur Verfügung zu stellen.

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

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Basisobjekt erstellen](SheetMetal_AddBase/de.md): Erzeugt ein Blech-Basisobjekt aus einer Skizze, entweder ein Profil oder eine Platine.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Kante ansetzen](SheetMetal_AddWall/de.md): Setzt eine Kante an jede ausgewählte Kantenfläche einer Grundfläche an. (Die Kante kann durch das Ändern des Winkels zu einem Falz gewandelt werden.)

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Fläche erweitern](SheetMetal_Extrude/de.md): Erweitert eine gewählte Kantenfläche in Richtung ihrer Flächennormalen. (Durch das Hinzufügen einer Konturskizze kann es dazu genutzt werden, verzahnte Geometrie zu erzeugen.)

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Abkanten](SheetMetal_AddFoldWall/de.md): Kantet eine Fläche entlang einer gewählten Linie mit einem vorgegebenen Biegeradius ab.

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Abwickeln](SheetMetal_Unfold/de.md): Ebnet ein gekantetes Blechobjekt und erzeugt einen Abwicklungskörper sowie eine Konturskizze mit Biegelinien (stellt ein Dialogfenster zum Festlegen von Parametern bereit).

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Abwickeln ohne Eingaben](SheetMetal_UnattendedUnfold/de.md): Ebnet ein gekantetes Blechobjekt und erzeugt einen Abwicklungskörper sowie eine Konturskizze mit Biegelinien (wenn die Parameter bereits festgelegt sind).

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Eckentlastung hinzufügen](SheetMetal_AddCornerRelief/de.md): Fügt einer Ecke einen Ausschnitt zur Eckentlastung hinzu.

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md): Erster Schritt um ein Schalenobjekt in ein abwickelbares Blechobjekt zu wandeln, fügt einer Ecke einen Entlastungsausschnitt hinzu.

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Stoß hinzufügen](SheetMetal_AddJunction/de.md): Zweiter Schritt um ein Schalenobjekt in ein abwickelbares Blechobjekt zu wandeln, fügt einen Stoß mit Spalt auf der Kante zweier Wände ein.

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Bogen einfügen](SheetMetal_AddBend/de.md): Dritter Schritt um ein Schalenobjekt in ein abwickelbares Blechobjekt zu wandeln, ersetzt scharfe Kanten durch runde Bögen.

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Skizze auf Blech](SheetMetal_SketchOnSheet/de.md): Schneidet den abgekanteten Flächen folgend skizzenbasierte Ausschnitte in ein Blechobjekt.

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Prägen](SheetMetal_Forming/de.md): Prägt Formen mit und ohne Löcher in eine Blechplatine.

## Kurzbeschreibung

Dieser Arbeitsbereich bietet Werkzeuge für zwei Hauptaufgaben:

-   Blechobjekte erstellen
-   Blechobjekte abwickeln

Dieser Abschnitt ist dazu gedacht, eine grobe Vorstellung davon zu vermitteln, wie die mitgelieferten Werkzeuge zu verwenden sind. Ausführlichere Informationen können auf der Seite der jeweiligen Werkzeuge (siehe oben) oder in den verknüpften Tutorien (siehe unten) gefunden werden.

### Erstellen eines Blechobjekts 

#### Mit einem Profil beginnen 

1.  Erstelle eine offene Polylinie (vorzugsweise mit dem Skizzierer).
2.  Verwende den <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Basis Wandung erstellen](SheetMetal_AddBase/de.md), um ein Blechprofil zu erstellen.

#### Mit einer Platine beginnen 

1.  Erstelle eine geschlossene Polylinie (vorzugsweise mit dem Skizzierer).
2.  Verwende den _ [Basis Wandung erstellen](SheetMetal_AddBase/de.md) Befehl, um einen Blechrohling zu erstellen.

#### Mit einem PartDesign Polster beginnen 

1.  Erstelle eine geschlossene Polylinie (vorzugsweise mit dem Skizzierer).
2.  Verwende den <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Polster](PartDesign_Pad/de.md) Befehl, um einen prismatischen Körper zu erstellen.
3.  Die <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [PartDesign Wandstärke](PartDesign_Thickness/de.md) wird es zu einem Objekt mit konstanter Dicke.
4.  Um es abwickelbar zu machen, braucht es einige Lücken oder Verbindungen zwischen den Wandungen:
    1.  Die <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> [Entlastung erzeugen](SheetMetal_AddRelief/de.md) schneidet ausgewählte Ecken ab.
    2.  Der <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> [Anbindungen erzeugen](SheetMetal_AddJunction/de.md) erzeugt Anbindungen mit Lücken zwischen angrenzenden Wandungen, die getrennt werden müssen.
    3.  Der <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> [Biegung erzeugen](SheetMetal_AddBend/de.md) erzeugt zylindrische Verbindungen für die verbleibenden Wandungen, die verbunden bleiben müssen.

Einige Parameter werden vom Elternobjekt (von den Elternobjekten) übernommen, aber es ist besser die entsprechenden Parameter bei jedem Schritt zu überprüfen.

Nun sollte geprüft werden, ob das resultierende Blechobjekt abgewickelt werden kann.(siehe unten [\...abwickeln](#Ein_Blechobjekt_abwickeln.md)).

#### Weitere Elemente hinzufügen 

Die abwickelbaren Blech-Basisobjekte können erweitert werden:

1.  Den Befehl <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> [Fläche erweitern](SheetMetal_Extrude/de.md) verwenden, um Flächen zu vergrößern.
2.  Der Befehl <img alt="" src=images/SheetMetal_AddWall.svg  style="width:16px;"> [Kante ansetzen](SheetMetal_AddWall/de.md) fügt dem bestehenden Objekt neue Kanten oder Falze hinzu.
3.  Den Befehl <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:16px;"> [Eckentlastung hinzufügen](SheetMetal_AddCornerRelief/de.md) verwenden, um Eckentlastungen hinzuzufügen oder umzuformen.
4.  Der Befehl <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:16px;"> [Abkanten](SheetMetal_AddFoldWall/de.md) kantet eine Fläche entlang einer gewählten Linie ab, d.h. er trimmt die Fläche an besagter linie, setzt die abgeschnittene Seite um und verbindet beide mit einem zylindrischen Übergang.
5.  Der Befehl <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Skizze auf Blech](SheetMetal_SketchOnSheet/de.md) schneidet Löcher in das Objekt, beginnend an der ausgewählten Fläche und dann den angrenzenden Flächen und Verbindungen folgend.
6.  Der Befehl <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Prägen](SheetMetal_Forming/de.md) Prägt (oder Stanzt) ein Formobjekt in eine Fläche.

:   

    :   Nach der Erzeugung eines WallForming-Objekts ist das Blechobjekt **nicht länger abwickelbar**!

Einige Werkzeuge aus anderen Arbeitsbereichen können verwendet werden, um Löcher hinzuzufügen oder Kanten umzuformen.

### Abwickeln eines Blechobjekts 

Um ein Blechobjekt abzuwickeln, verwendet man das Werkzeug <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> _.

Das Ergebnis ist ein 3D-Objekt, wahlweise mit Kontur inklusive Biegelinien.

### Beispiele

Bis Seiten mit Tutorials innerhalb des Wikis zur Verfügung stehen, gibt es eine Seite mit [Beispielen](SheetMetal_Examples/de.md).

<img alt="" src=images/SheetMetal_Example-01.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-02.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:100px;">

## Begrenzungen

-   Der Arbeitsbereich ist betroffen von dem mit FreeCAD verbundenen [topological naming issue](Glossary#Topological_Naming.md). Wenn bei der Bearbeitung einer in der Geschichte des Teils früheren Biegung die Flächen neu nummeriert werden, können die folgenden Biegungen betroffen sein und die Flächen vertauscht werden. Wenn die Biegungsmerkmale nicht brechen, kannst Du darauf doppelklicken, um ein Dialogfeld zu erhalten, in dem du die richtige Fläche in der [3D Ansicht](3D_view/de.md) auswählen und die Biegung aktualisieren kannst.
-   Das Abwickelwerkzeug hat einige Einschränkungen und versagt in bestimmten komplexen Situationen. Wenn es fehlschlägt, versuche eine andere Fläche auszuwählen.
-   Häufiger Crash Fall: Treffe viele Vorsichtsmaßnahmen, um nicht in die Gelenke (die Faltungen) weder entlang der Flächen oder in den Winkeln einzuschneiden noch Löcher oder Ausklinkungen durch die Winkel zu machen.

## Tutorien


<div class="mw-collapsible mw-collapsed toccolours" style="width:800px">

### Blech Tutorium von meme2704 

Das folgende Tutorium ist aus dem in [Links](#Links.md) erwähnten PDF Tutorium nachgebildet.


<div class="mw-collapsible-content">

#### Vorstellung des Arbeitsbereichs 

Nach dem herunterladen und installieren der Erweiterung, öffne sie. ![](images/sm1.png )

#### 1. Arbeitsgang

-   Hole die Grundlage: benutze entweder die Arbeitsbereiche \"Part\" oder \"Entwurf\", mache 1 Skizze, die alle Löcher und eventuelle Schnitte enthält, extrudiere diese Grundlage auf die Dicke der Platte.
-   Denk daran, dass die Kanten immer zusätzlich sein werden genauso wie die Falzradien.

![](images/sm2.png )

#### 2. Arbeitsgang 

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
Jetzt müssen wir die 2 Kanten trennen, sonst vereinigen sie sich und die Abwicklung wird unmöglich.
\* Erste Methode: Entfernen einer Kante vornehmen.

-   -   Gib einen Wert an, der geringfügig größer als Spalt1 (oder Spalt2) ist. Bei Null besteht noch Verbindung.

-   2\. Methode einen Schnitt bei 45 ° machen, siehe weiter, dieses Werkzeug verwenden.

![](images/sm5a.png )

#### Abwicklung

Wähle eine Referenzfläche (hier die orangene Fläche) und klicke auf die Schaltfläche in der Werkzeugleiste.
Wir erhalten den blauen Teil, von dem es ausreicht, die Werte X, Y oder Z zu ändern, um ihn als Ganzes zu sehen.
![](images/sm6.png )

#### Schneide die Umschläge bei 45 ° 

Nach dem Falten der Umschläge ohne das ein Rücknahme gemacht wurde, dadurch erscheint die Form. ![](images/sm7a.png ) Um es zu tun muss bei 45 ° geteilt werden (oder die folgenden Halbierenden Umschläge sind ungleich breit).
\* Erstelle eine neuen Skizze bezogen auf den gemeinsamen Teil der beiden Umschläge.

-   Erstelle einen verknüpften Anschlag, durch Wahl der Außenkante des \"Scharniers\".
-   Zeichne ein Dreieck, dessen Spitze am Ende begrenzt ist und eine Seite in 45 ° ausgerichtet ist, geben Sie der kleinen Seite 1 Mindestbreite (0,1 mm sind ausreichend) und fertigen Sie eine Tasche an.

Achten Sie darauf, nicht das \"Scharnier\" zu zerkratzen, bei dem die Nacktheit die Spitze des Dreiecks am Rand der Faltlinie gebunden hat. ![](images/sm8a.png ) Abwicklung ![](images/sm9.png )

#### Kanten und Umschläge durchstechen 

Machen Sie diese Löcher und Schnitte nach dem Falten und vor dem Abwickeln.
Achten Sie immer darauf, die Falzlinien nicht zu \"zerkratzen\".
![](images/sm10.png )

#### Verdrahtete Umschläge herstellen 

Mache eine Falte an der Kante der Seite, bei 45 ° von 0,1 mm Länge, dann eine andere umgekehrt bei 45 ° der Länge des benachbarten Umschlags, dann verlängere die gegenüberliegende Seite, sie wird übergehen und sie werden nicht zusammengeführt.
![](images/sm11.png )

#### Sonderfall derselben durchstochenen Kante 

In diesem speziellen Fall funktioniert das Abwickeln nur, indem die gelbe Fläche als Referenz ausgewählt wird.
![](images/sm12.png )

#### Sonderfall Loch überspannt die Faltungen 

Zuvor wurde mehrmals gesagt, dass es nicht notwendig ist, die Faltlinien zu schneiden.
Was macht man ?
![](images/sm13.png )

-   Mache die Basis mit seinem halbrunden Loch und mache die beiden halbseitigen und die beiden halbgefalteten getrennt.
-   Mache dann eine Verlängerung auf einer der Seiten der Breite der Öffnung minus 0,1 mm, die beiden Kanten bleiben somit getrennt.
-   Dann auf dieser Verlängerung (in grün) die Kontur des Schnitts zeichnen und eine Tasche machen
-   Das Ergebnis ist das rote Stück darüber, und die Abwicklung funktioniert, bleibt die Linie, die die beiden Kanten zuvor getrennt hat

![](images/sm14.png )


</div>


</div>

## Videos

-   [The Elegant Sheet Metal Workbench](https://www.youtube.com/watch?v=xidvQYkC4so) von Joko Engineering

## Verweise

-   [Macro Sheet Metal Unfolder](Macro_Sheet_Metal_Unfolder.md), das ursprüngliche Makro, auf dem das Abwicklungswerkzeug basiert.
-   [Blech Arbeitsbereich](https://forum.freecadweb.org/viewtopic.php?t=11303) Ankündigung im FreeCAD Forum.
-   [Ein englisches und französisches Tutorium im PDF Format](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) im FreeCAD Forum.
-   Fehler melden/Funktionen anfragen: <https://github.com/shaise/FreeCAD_SheetMetal/issues>.

## Referenzen

-   Autoren:
    -   Falt Werkzeuge: Urheberrechtlich geschützt 2015-2018 durch Shai Seger
    -   Abwicklungswerkzeug: Urheberrechtlich geschützt 2014 durch Ulrich Brammer
-   Lizenz: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
-   Offizieller Blog: [Blech Erweiterung für FreeCAD](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/)
-   Quellcode auf github: <https://github.com/shaise/FreeCAD_SheetMetal>

_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal Workbench/de
