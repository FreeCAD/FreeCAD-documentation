# Tutorial for open windows/de
{{TutorialInfo/de
|Topic=Architektur
|Level=Anfänger
|Time=60 Minuten
|Author=[https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx]
|FCVersion=0.18 or höher
|Files=none
}}

## Einleitung

Dieses Tutorium zeigt, wie man [Arch Fenster](Arch_Window/de.md) und Türen in einem Gebäudemodell platziert, wie man sie in der 3D Ansicht als offen anzeigt und wie man eine 2D Zeichnung (Grund- und Aufriss) für das Modell erstellt. Es verwendet die [Entwurf Arbeitsbereich](Draft_Workbench/de.md), [Architektur Arbeitsbereich](Arch_Workbench/de.md) und den [Technisches Zeichnen Arbeitsbereich](TechDraw_Workbench/de.md).

Häufig verwendete Werkzeuge sind: [Entwurf Gitter](Draft_Snap_Grid/de.md), [Entwurf Fang](Draft_Snap/de.md), [Entwurf Draht](Draft_Wire/de.md), [Arch Wand ](Arch_Wall/de.md), [Arch Fenster](Arch_Window/de.md), [Arch Schnittebene](Arch_SectionPlane/de.md) und [TechDraw ArchAnsicht](TechDraw_NewArch/de.md).

Siehe auch die folgende Seite für einige Videos über das Ausrichten von Fenstern.

-   [Der Arbeitsbereich, der zum Erstellen von Architekturprojekten verwendet wird, heißt Arch](http://help-freecad-jpg87.fr/04_arch_ind.php)

## Einrichtung

1\. Öffne FreeCAD, erstelle ein neues, leeres Dokument und wechsel zum [Architektur-Arbeitsbereich](Arch_Workbench/de.md).

2\. Stelle sicher, dass Deine Einheiten im Menü **Bearbeiten → Einstellungen → Allgemein → Einheiten** korrekt eingestellt sind. Zum Beispiel ist `MKS (m/kg/s/Grad)` gut geeignet, um mit den Abständen in einem typischen Gebäude umzugehen; setze außerdem die Anzahl der Nachkommastellen auf `4`, um auch die kleinsten Teile eines Meters zu berücksichtigen.

3\. Benutze die Schaltfläche **<img src="images/Draft_Grid.svg" width=16px> [Entwurfsraster ein-/ausschalten](Draft_ToggleGrid/de.md)**, um ein Raster mit ausreichender Auflösung einzublenden. Das Erscheinungsbild des Rasters kannst Du im Menü **Bearbeiten → Einstellungen → Draft → Raster und einrasten → Raster** ändern. Setze \"Hauptlinien alle\" auf `20`, \"Rasterabstand\" auf `50 mm` und \"Rastergröße\" auf `1000 Linien` (das Raster wird damit eine Fläche von 50m x 50m abdecken).

4\. [Zoome im 3D-Ansichtsfenster heraus](Std_ViewZoomOut/de.md), wenn Du zu nahe am Raster bist.

Jetzt sind wir bereit, ein einfaches Gebäude mit geschlossenen Wänden, 2 Türen und 2 Fenstern zu erstellen.

## Wände erstellen 

5\. Benutze das [Draft:Drahtwerkzeug](Draft_Wire/de.md), um einen geschlossenen Linienzug zu erstellen. Gehe gegen den Uhrzeigersinn vor.

:   5.1. Erster Punkt bei (0, 0, 0); gib im Dialog ein: **0** **m** **Enter**, **0** **m** **Enter**, **0** **m** **Enter**.
:   5.2. Zweiter Punkt bei (3, 0, 0). Drücke **X** um die Bewegung auf die X-Achse einzuschränken; gib den Wert ein: **3** **m** **Enter**.
:   5.3. Dritter Punkt bei (3, 4, 0). Drücke **Y** um die Bewegung auf die Y-Achse einzuschränken; gib den Wert ein: **4** **m** **Enter**.
:   5.4. Vierter Punkt bei (0, 4, 0). Drücke **X** um die Bewegung auf die X-Achse einzuschränken; gib den Wert ein: **-** **3** **m** **Enter**.
:   5.5. Drücke **O** um den Linienzug zu schließen und das Werkzeug zu beenden.
:   5.6. Drücke auf dem Nummernblock **0** um eine [isometrische Projektion](Std_ViewIsometric/de.md) des Modells zu erhalten.
:   
    **Hinweis:**Die Punkte können auch mit dem Mauscursor durch Anklicken der Rasterschnittpunkte unter Zuhilfenahme der [Draft:Fang](Draft_Snap/de.md)-Werkzeugleiste und der [Raster](Draft_Snap_Grid/de.md)-Methode definiert werden.

6\. Wähle den Linienzug `DWire` aus und verändere die Eigenschaft **Make Face** auf `False`.

7\. Wähle den Linienzug `DWire` aus und klicke auf das Werkzeug [Arch:Wand](Arch_Wall/de.md); die Wände werden unverzüglich erstellt mit einer voreingestellten Breite (Dicke) von 0.2 m und einer Höhe von 3 m.

:   
    **Note:**Wenn die Eigenschaft **Make Face** des Linienzugs `DWire` auf `True` eingestellt ist, wird dieser Schritt einen soliden Block erstellen anstatt nur die Kontur des Linienzugs `DWire` zu nutzen.

<img alt="" src=images/01_T01_wire_wall.png  style="width:600px;"> 
*align=center|Basis-Polygon für die Wände; es ist ein geschlossener Linienzug, welcher nicht als Fläche definiert ist*

<img alt="" src=images/02_T01_just_wall.png  style="width:600px;"> 
*align=center|Die aus dem Linienzug konstruierten Wände*

## Türen und Fenster platzieren 

8\. Klicke auf das Werkzeug [Arch:Fenster](Arch_Window/de.md), wähle die Voreinstellung (preset) `Simple door` aus und ändere die Höhe auf 2 m.

:   8.1. Ändere die Fangmethode auf [Mittelpunkt](Draft_Snap_Midpoint/de.md) und versuche die untere Kante der vorderen Wand auszuwählen. Wenn nötig verdrehe die [Ansicht](Std_View_Menu/de.md), um die Kante und nicht die Wandoberfläche anklicken zu können; wenn der Mittelpunkt aktiv ist, klicke um die Tür zu platzieren.
:   8.2. Klicke noch einmal auf das Werkzeug [Arch:Fenster](Arch_Window/de.md) und platziere eine weitere Tür, aber diesmal am Mittelpunkt der rückseitigen Wand; verdrehe dazu die [Ansicht](Std_View_Menu/de.md) soweit wie nötig.

<img alt="" src=images/03_T01_wall_place_door_rear.png  style="width:600px;"> 
*align=center|Fangen des Mittelpunktes der unteren Wandkante um die Tür zu platzieren*

9\. Klicke auf das Werkzeug [Arch:Fenster](Arch_Window/de.md); wähle die Voreinstellung `Open 1-pane` (1flg. Fenster) und ändere die `Sill height` (Brüstungshöhe) auf 1 m.

:   9.1. Behalte die Fangmethode [Mittelpunkt](Draft_Snap_Midpoint/de.md) bei und versuche die untere Kante der linken Wand auszuwählen. Wenn nötig verdrehe die [Ansicht](Std_View_Menu/de.md), um die Kante und nicht die Wandoberfläche anklicken zu können; wenn der Mittelpunkt aktiv ist, klicke um das Fenster zu platzieren.





:   
    **Hinweis:**Die `Sill height` (Brüstungshöhe) ist der Abstand vom Fußboden bis zur unteren Fensterkante. Für Türen ist die `Sill height` gewöhnlich 0 m weil Türen normalerweise bis zum Fußboden reichen; andererseits haben Fenster üblicherweise einen Abstand von 0,5 m bis 1,5 m zum Fußboden.





:   9.2 Klicke noch einmal auf das Werkzeug [Arch:Fenster](Arch_Window/de.md) und platziere ein weiteres Fenster, aber diesmal am Mittelpunkt der rechten Wand; verdrehe dazu die [Ansicht](Std_View_Menu/de.md) soweit wie nötig. Stelle diesmal die Fensterbreite auf 1,5 m ein und die `Sill height` (Brüstungshöhe) wieder auf 1 m.

<img alt="" src=images/04_T01_wall_place_door_side_right.png  style="width:600px;"> 
*align=center|Fangen des Mittelpunktes der unteren Wandkante um das Fenster zu platzieren*

:   
    **Hinweis:**Der Parameter `Sill height` (Brüstungshöhe) kann nur während des ursprünglichen Erzeugens eines Fensters mittels Voreinstellung (preset) eingegeben werden. Ist das Fenster erst einmal eingefügt, lässt sich seine Lage durch Editieren der Eigenschaft **Position** `[x, y, z]` der zugrundeliegenden [Skizze](Sketcher_Sketch.md) modifizieren.





:   9.3. Verschiebe nun des Fenster `Window001` ein Stück höher. Wähle die zugrunde liegende Skizze `Sketch003` aus und ändere seine **Position** von `[3.1 m, 2.0 m, 1.0 m]` auf `[3.1 m, 2.0 m, 1.6 m]`. Das gesamte Fenster `Window001` sollte sich nun nach oben bewegen. Die Wandöffnung kann ggf. noch an seiner vorherigen Position angezeigt werden. Wenn das passiert, klicke mit der rechten Maustaste auf das `Wall`-Element, wähle `Markieren, um neu zu berechnen` aus und drücke dann **Ctrl**+**R** um das Modell zu [aktualisieren](Std_Refresh/de.md).

<img alt="" src=images/04.1_T01_wall_built.png  style="width:600px;"> 
*align=center|erstellte Wände mit Türen und Fenstern*


**Hinweis:**

Beim Platzieren eines Fensters oder einer Tür mittels der Voreinstellung (preset) bewege das Element über die [Wand](Arch_Wall/de.md) und warte, bis sich das Element parallel zur Wand ausgerichtet hat. Ziele auf die untere Wandkante und nutze den Parameter `Sill height`, um den Abstand vom Fußboden einzustellen. Falls dies schwierig ist, benutze die Fangmethode [\"Nächste\"](Draft_Snap_Near/de.md) der [Fang](Draft_Snap/de.md)-Werkzeugleiste, um das Element überall auf der Oberfläche einer Wand einzufügen, und justiere danach seine **Position** manuell wie oben beschrieben. Zu viele gleichzeitig aktive [Fang](Draft_Snap/de.md)-Modi können Probleme beim Platzieren des Elementes verursachen - versuche es deshalb nur mit jeweils einer aktiven Option.


**Hinweis 2:**

Mitunter wird das Fenster außerhalb der [Wand](Arch_Wall/de.md) platziert. Solange es jedoch parallel zu dieser Wand ist, solltest Du imstande sein, seine Position manuell zu korrigieren.

## Die Türen öffnen 

10\. Wähle im Modellbaum den unter `Tür` liegenden `Sketch` und drücke **Space** oder ändere die Eigenschaft **Visibility** auf `True`

11\. Doppelklicke im Modellbaum auf `Tür`, um mit dem Editieren zu beginnen.

:   11.1. Innerhalb des Dialoges `Fensterelemente` sind zwei Felder: `Kantenzüge` und `Komponenten`.
:   
    **Hinweis:**bei einer vordefinierten einfachen Tür gibt es zwei Kantenzüge: `Wire0` und `Wire1` sowie zwei Komponenten: `OuterFrame` und `Door`. Eine benutzerspezifisch designte [Tür](Arch_Door/de.md) kann mehr Kantenzüge und Komponenten haben.





:   11.2. Klicke erst auf Komponente `Door` und dann die **Bearbeiten**-Schaltfläche. Das zeigt die Eigenschaften der `Door`-Komponente wie `Name`, `Typ`, `Kantenzüge`, `Dicke`, `Versatz`, `Gelenk` (Scharnier) und `Öffnungsmodus`.
:   11.3. Wähle in der 3D-Ansicht eine vertikale Kante des sichtbaren Sketches der Tür aus, klicke dann die Schaltfläche **ausgewählte Kante erhalten**. Die Schaltfläche sollte sich verändern und nun den Namen der ausgewählten Kante anzeigen, zum Beispiel **Edge8**.
:   11.4. Ändere den `Öffnungsmodus` in **Arc 90** oder eine andere Option.
:   11.5. Klicke auf die Schaltfläche **+Erstelle/aktualisiere Komponente** und dann **Schließen** um das Bearbeiten der Tür zu abzuschließen. Der Sketch wird wieder unsichtbar geschaltet.

![](images/05_T01_window_edit.png ) 
*align=center|Dialog zum Bearbeiten eines Fensters oder einer Tür*

![](images/06_T01_window_edit_component.png ) 
*align=center|Dialog zum Bearbeiten der Einzelkomponenten eines Fensters oder einer Tür*

<img alt="" src=images/06.1_T01_window_edit_wire_door_front.png  style="width:600px;"> 
*align=center|als Gelenk (Scharnier-/Bandseite) einer Tür ausgewählte vertikale Kante des Sketches*

12\. Wähle `Tür` und gib der Eigenschaft **Opening** einen Wert von 45. Das Türblatt sollte sich ins Innere das Gebäudes öffnen.

13\. Wähle `Tür` und verändere die Eigenschaft **Symbol Elevation** auf `True`. Die Spitze des erzeugten Linienzuges zeigt an, nach welcher Seite sich die Tür öffnet; dies ist einfacher zu erkennen, wenn Du in die _ wechselst.

14\. Wiederhole nun die Schritte mit der `Tür001` und dem zugrundeliegenden `Sketch001` um diese Tür 75 Grad ins Gebäudeinnere öffnen zu lassen. Aktiviere auch die Symbole in Ansicht und Grundriss.

![](images/07_T01_window_property_view.png ) 
*align=center|Eigenschaftsdialog der Tür zur Veränderung von Öffnungswinkel, Ansichts- und Grundriss-Symbol sowie anderer Optionen*

<img alt="" src=images/08_T01_window_symbol_elevation.png  style="width:600px;"> 
*align=center|Tür mit Öffnungssymbol in Ansicht*

<img alt="" src=images/09_T01_window_symbol_plan.png  style="width:600px;"> 
*align=center|Tür mit Öffnungssymbol im Grundriss*

## Die Fenster öffnen 

15\. Wähle im Modellbaum den unter `Window` liegenden `Sketch002` und drücke **Space** oder ändere die Eigenschaft **Visibility** auf `True`.

16\. Doppelklicke im Modellbaum auf `Window`, um mit dem Editieren zu beginnen.

:   16.1. Klicke auf die Komponente `InnerFrame` und dann auf die Schaltfläche **Bearbeiten**.





:   16.2. Wähle in der 3D-Ansicht eine vertikale Kante des `Sketch002` des Fensters aus. Die Linienzüge, welche für den äußeren `OuterFrame` und den inneren `InnerFrame` Rahmen stehen, liegen sehr eng nebeneinander, also [Zoome hinein](Std_ViewZoomIn/de.md) so nah wie möglich an die Skizze um den zugehörigen Linienzug auszuwählen. Klicke dann die Schaltfläche **ausgewählte Kante erhalten**. Die Schaltfläche sollte sich verändern und nun den Namen der ausgewählten Kante anzeigen, zum Beispiel **Edge12**.
:   
    **Hinweis:**Wenn zu viele Körper auf dem Bildschirm vorhanden sind, so dass es schwierig ist, eine einzelne Kante auszuwählen, wechsel zum [Drahtgitter-Modus](Std_DrawStyle/de.md), um die Flächen dieser Körper auszublenden, so dass nur noch Linien, Kanten und Konturen zu sehen sind.





:   16.3. Verändere `Öffnungsmodus` zu `Arc 90 inv` oder eine andere Option.

17\. Wähle `Window` und gib der Eigenschaft **Opening** einen Wert von 45. Der die transparente Glasscheibe beinhaltende Fensterflügel sollte sich ins Innere das Gebäudes öffnen.

18\. Wähle `Window` und verändere die Eigenschaft **Symbol Elevation** auf `True`. Die Spitze des erzeugten Linienzuges zeigt an, nach welcher Seite sich das Fenster öffnet; dies ist einfacher zu erkennen, wenn Du in die _ wechselst.

19\. Wiederhole nun die Schritte mit dem `Window001` und dem zugrundeliegenden `Sketch003`, um dieses Fenster 75 Grad öffnen zu lassen. Aktiviere auch die Symbole in Aufriss und Grundriss. Picke diesmal nicht eine vertikale Linie des `InnerFrame` als Scharnier sondern die obere horizontale Linie. Das bedeutet, dass sich dieses Fenster anders öffnet als das andere. Das Aufriss-Symbol wird besser von der [rechten Seitenansicht](right_side_view.md) zu sehen sein. Das Grundriss-Symbol wird besser von der [Frontansicht](Std_ViewFront/de.md) zu sehen sein. Falls die Wand den Blick versperren sollte, kannst Du ihre **Transparency** auf einen Wert wie 85 ändern, um durch sie hindurch sehen zu können. Alternativ kannst Du den **Display Mode** auf `Drahtgitter` ändern, um nur die Kanten anzeigen zu lassen. <img alt="" src=images/06.2_T01_window_edit_wire_side_right.png  style="width:600px;"> 
*align=center|als Scharnier für das Fenster ausgewählte horizontale Kante des Sketches*

<img alt="" src=images/10_T01_window_all_symbol_axonometric.png  style="width:600px;"> 
*align=center|Auf- und Grundriss-Symbole für alle Elemente, isometrische Darstellung*

<img alt="" src=images/11_T01_window_all_symbol_top.png  style="width:600px;"> 
*align=center|Auf- und Grundriss-Symbole für alle Elemente, Draufsicht*

## Erstellung eines Grundrissplans des Gebäudes 

20\. Noch im [Architektur-Arbeitsbereich](Arch_Workbench/de.md) wähle im Modellbaum alle Elemente, also die [Wände](Arch_Wall/de.md), die beiden [Fenster](Arch_Window/de.md) und die beiden [Türen](Arch_Door/de.md), aus. Benutze anschließend das [Schnittebenen-Werkzeug](Arch_SectionPlane/de.md), um ein `Section`-Element zu erstellen.


**Hinweis:**

Ändere die Eigenschaft **Arrow size** der Schnittebene auf einen größeren Wert, zum Beispiel auf `200 mm`, damit die Blickrichtung des Schnittes in der 3D-Ansicht klarer sichtbar ist.

<img alt="" src=images/11.1_T01_Arch_SectionPlane_all.png  style="width:600px;"> 
*align=center|Schnittebene, welche solide Objekte einschl. Wände, Türen und Fenster durchschneidet*

21\. Wechsel zum _ eine neue Seite ein; es wird ein neues `Page`-Objekt erzeugt und die Ansicht wechselt zu dieser Seite. Die eingefügte Seite ist eine Standard-DIN A4-Seite im Querformat mit einem einfachen Rahmen. Verwende das Werkzeug [TechDraw: Neue Vorlagenauswahl](TechDraw_PageTemplate/de.md), wenn Du eine neue Seite unter Verwendung einer speziellen [SVG](SVG/de.md)-Vorlage erstellen möchtest.

22\. Wähle `Section` aus und verwende das Werkzeug [TechDraw: Arch-Ansicht](TechDraw_ArchView/de.md), um ein `ArchView`-Objekt auf der Seite zu erzeugen. Höchstwahrscheinlich wird das neue Objekt auf der Seite nicht sichtbar sein, weil es einen sehr großen Maßstab von `1`, also 1:1, hat. Dies bedeutet, dass jeder Meter im Modell auch als 1 Meter in der Seitenansicht dargestellt wird. Da die Seitengröße nur 0,297 m x 0,210 m beträgt, sind die meisten Abmessungen zu groß, um in ihrer natürlichen Größe auf diese Seite zu passen.

23\. Wähle das `ArchView`-Objekt und ändere die Eigenschaft **Scale** auf `0.02`, was gleichbedeutend mit 1:50 ist, einem gebräuchlichen Maßstab für typische Gebäude. Das bedeutet, dass jeder Meter im Modell als 20mm auf der Seite dargestellt wird. Das Objekt sollte im Zentrum der Seite auftauchen und kann auf eine bessere Position am linken Rand bewegt werden. Es sollten beide Türen geöffnet dargestellt sein, jedoch nur das linke Fenster. Der Grund dafür, dass das rechte Fenster in dieser Projektion nicht erscheint, liegt darin, dass die durch `Section` definierte Ebene dieses Fenster im Modell nicht schneidet.

<img alt="Section view of the building, A4 sheet, scale 1:50" src=images/12_T01_TechDraw_window_all_symbols.png  style="width:600px;"> 
*align=center|Schnittebene, welche solide Objekte einschl. Wände, Türen und Fenster durchschneidet*

24\. Wechsel zurück zum [Arch-Arbeitsbereich](Arch_Workbench/de.md), wähle erneut alle Komponenten im Modellbaum aus und benutze das [Schnittebenen-Werkzeug](Arch_SectionPlane/de.md), um ein zweites `Section001`-Element zu erzeugen.

:   24.1. Wähle `Section001` aus und ändere die Eigenschaft **Position** auf `[1.5 m, 2.0 m, 1.8 m]`. Diese 2. Ebene schneidet nun durch alle Objekte.
:   24.2. Wechsel zurück zum [TechDraw-Arbeitsbereich](TechDraw_Workbench/de.md). Wähle `Section001`, benutze [Arch Ansicht](TechDraw_ArchView/de.md), um `ArchView001` zu erzeugen und setze **Scale** auf `0.02`. Der neue Zeichnungsausschnitt in der TechDraw-Seite zeigt nun alle Öffnungen, welche in den [Wänden](Arch_Wall/de.md) von den Türen und Fenster erzeugt wurden.


**Hinweis:**

Setze **All On** für [TechDraw:ArchView](TechDraw_ArchView.md)-Objekte auf `True`, damit alle von der Schnittebene geschnittenen Elemente in der TechDraw-Seite sichtbar sind, unabhängig von ihrem Sichtbarkeits-Status in der 3D-Modellansicht. Des Weiteren kann die Option **Show Fill** auf `True` gesetzt werden, um die Schnittflächen der von der Ebene geschnittenen Körper schattiert darzustellen.

<img alt="" src=images/13_T01_TechDraw_window_all_symbols_higher.png  style="width:600px;"> 
*align=center|Schnittansicht des Gebäudes, mit einer zweiten Schnittdarstellung, Format DIN A4 , Maßstab 1:50*

## Erstellung einer Aufriss-Projektion des Gebäudes 

25\. Gehe zurück zum [Architektur-Arbeitsbereich](Arch_Workbench/de.md). wähle im Modellbaum alle Elemente, also die [Wände](Arch_Wall/de.md), die beiden [Fenster](Arch_Window/de.md) und die beiden [Türen](Arch_Door/de.md), aus. Benutze anschließend das [Schnittebenen-Werkzeug](Arch_SectionPlane/de.md), um ein drittes `Section002` - Element zu erstellen.

:   25.1. Drehe die `Section002`, so dass sie das Gebäude vertikal durchschneidet. Ändere dazu die Eigenschaften **Axis** auf `[1, 0, 0]` sowie **Angle** auf `90`.
:   25.2. Ändere **Position** auf `[1.5 m, -1 m, 1.5 m]`, so dass die Ebene dann vor dem Gebäude liegt.

<img alt="" src=images/14.1_T01_Arch_SectionPlane_three.png  style="width:600px;"> 
*align=center|Schnittebenen, welche die massiven Objekte schneiden bzw. auf das Gebäude schauen*

26\. Gehe zurück zum _ mit `Section002`; denke daran, den Maßstab auf `0.02` (1:50) einzustellen. Ändere **Rotation** auf `-90`, um die Ausrichtung der Projektion zu korrigieren. Ordne den `ArchView002` neben den anderen Ansichten auf der Seite an. Diese dritte Projektion schaut von vorn auf das Gebäude.

<img alt="" src=images/14_T01_TechDraw_window_all_symbols_elevation.png  style="width:600px;"> 
*align=center|Schnittansicht des Gebäudes, mit zwei Draufsichten und einem Aufriss, Format DIN A4, Maßstab 1:50*

## Interaktion zwischen Arch- und TechDraw-Arbeitsbereichen 

Zum Zeitpunkt der Erstellung dieses Dokumentes (FreeCAD 0.18, November 2018) kann der _ eingefügten und durch das Werkzeug [TechDraw:Arch-Ansicht](TechDraw_ArchView/de.md) dargestellten Elemente vom [Arch-Arbeitsbereich](Arch_Workbench/de.md) kontrolliert wird.

Der _ (`ArchView`) dargestellt werden. Aus diesem Grund sollten auf die Darstellung von Architekturelementen bezogene Fehlerberichte und Funktionsanfragen bei beiden Arbeitsbereichen eingereicht werden.

Für zukünftige FreeCAD-Versionen ist eine engere Interaktion zwischen beiden Arbeitsbereichen geplant. Für diese Versionen wird erwartet, dass seit langem bestehende Probleme gelöst werden, wie zum Beispiel die Charakteristika von Linien und Flächen (Linienbreite, Linienfarbe, Flächenfarbe, Schraffuren u.a.).


{{Tutorials navi

}}   {{TechDraw Tools navi}}

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > Tutorial for open windows/de
