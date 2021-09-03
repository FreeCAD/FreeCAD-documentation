---
- GuiCommand:/de
   Name:Arch Window
   Name/de:Arch Fenster
   MenuLocation:Architektur → Fenster
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**W** **I**
   SeeAlso:[Arch Wand](Arch_Wall/de.md), [Arch Hinzufügen](Arch_Add/de.md)
---

## Beschreibung

Ein [Arch Fenster](Arch_Window/de.md) ist ein Basisobjekt für alle Arten von \"einbettbaren\" Objekten, wie z.B. Fenster und Türen. Es ist so konzipiert, dass es entweder unabhängig ist oder in einer anderen Komponente \"untergebracht\" wird, wie z.B. einem [Arch Wänden](Arch_Wall/de.md), [Arch Strukturen](Arch_Structure/de.md) oder [Arch Dächern](Arch_Roof/de.md). Es hat eine eigene Geometrie, die aus mehreren festen Komponenten bestehen kann (üblicherweise aus einem Rahmen und inneren Platten), und definiert auch ein Volumen, das von den aufnehmenden Objekten abgezogen wird, um eine Öffnung zu erzeugen.

Fensterobjekte basieren auf geschlossenen 2D Objekten, wie z.B. [Entwurf Rechtecken](Draft_Rectangle/de.md) oder [Skizzen](Sketcher_Workbench/de.md), die zur Definition der inneren Fensterkomponenten verwendet werden. Das zugrundeliegende 2D Objekt muss also mehrere geschlossene Kantenzüge (Wire) enthalten, welche kombiniert werden können, um gefüllte Platten (ein Kantenzug) oder Rahmen (mehrere Kantenzüge) zu definieren.

Das Fensterwerkzeug besitzt mehrere **Voreinstellungen**; dies ermöglicht es dem Benutzer, gängige Arten von Fenstern und Türen mit bestimmten änderbaren Parametern zu erstellen, ohne dass der Benutzer die 2D Basisobjekte und Komponenten manuell erstellen muss.

Jede auf ein [Arch Fenster](Arch_Window/de.md) zutreffende Information gilt auch für eine [Arch Tür](Arch_Door/de.md), denn es ist das gleiche darunter liegende Objekt. Der Hauptunterschied zwischen einem Fenster und einer Tür besteht darin, dass die Tür eine interne Füllung hat, die undurchsichtig ist (die Tür selbst), während das Fenster eine teilweise durchsichtige Füllung hat (das Glas).

<img alt="" src=images/Arch_Window_example.jpg  style="width:600px;"> 
*Fenster auf Grundlage eines [Entwurf Rechtecks](Draft_Rectangle/de.md) konsturiert und in eine [Arch Wand](Arch_Wall/de.md) eingefügt. Das [Arch Hinzufügen](Arch_Add/de.md) eines Fensters zu einer Wand erzeugt automatisch einen passenden Wanddurchbruch in derselben.*

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;"> 
*Komplexes Fenster, das auf einer [Skizze](Sketcher_Workbench/de.md) konstruiert wird. Wenn du in den Bearbeitungsmodus des Fensters eintritts, kannst du verschiedene Komponenten erstellen, ihre Dicke einstellen und Drähte aus der Skizze auswählen und ihnen zuweisen.*

## Anwendung

### Eine Voreinstellung verwenden 

1.  Drücke die **<img src="images/Arch_Window.svg" width=16px> [Arch Fenster](Arch_Window/de.md)** Schaltfläche, oder drücke **W** dann **I** Tasten.
2.  Wähle eine der Voreinstellungen in der Liste aus.
3.  Fülle die gewünschten Parameter aus.
4.  In der [3D Ansicht](3D_view/de.md), Bewege das Fenster an die Stelle, an der du es platzieren möchtest. Wenn du den Mauszeiger über eine [Arch Wand](Arch_Wall/de.md) bewegst, sollte sich der Umriss des Fensters an der Fläche dieses Objekts ausrichten.
5.  Klick auf die [3D Ansicht](3D_view/de.md) mit der Maus oder drücke die **Eingabe** Taste dreimal, um die X, Y, Z Koordinaten der Platzierung zu bestätigen.


**Hinweis:**

Falls du die \"Parts Library\" über den [Erweiterungsverwalter](AddonManager/de.md) installierst, wird das Fenster-Werkzeug diese Bibliothek nach weiteren Voreinstellungen durchsuchen. Diese Voreinstellungen sind FreeCAD-Dateien, die jeweils ein einzelnes Fenster basierend auf einer parametrisierten Skizze mit benannten Beschränkungen enthalten. Du kannst zusätzliche Voreinstellungen im `parts_library`-Verzeichnis platzieren, so dass sie vom Fenster-Werkzeug gefunden werden.


```python
$ROOT_DIR/Mod/parts_library/Architectural\ Parts/Doors/Custom/
$ROOT_DIR/Mod/parts_library/Architectural\ Parts/Windows/Custom/
```

Das `$ROOT_DIR` ist das Benutzerverzeichnis, wo die FreeCAD-Konfiguration, Makros und externe Arbeitsbereiche gespeichert werden.

-   Unter Linux ist es normalerweise `/home/username/.FreeCAD/`
-   Unter Windows ist es normalerweise `C:\users\Benutzername\Anwendungsdaten\FreeCAD\`
-   Unter Mac OSX ist es normalerweise `/Benutzer/Benutzername/Bibliothek/Einstellungen/FreeCAD/`

### Erzeugung von Anfang an 

1.  Wählen Sie (optional) eine Fläche des Arch-Objekts, wo Sie das Fenster einfügen möchten.
2.  Wechseln Sie zum [Sketcher-Arbeitsbereich](Sketcher_Workbench/de.md).
3.  Erzeugen Sie eine neue Skizze.
4.  Zeichnen Sie ein oder mehrere geschlossene Linienzüge (Schleifen).
5.  Schließen Sie die Skizze.
6.  Wechseln Sie zurück zum [Arch-Arbeitsbereich](Arch_Workbench/de.md).
7.  Drücken Sie den **<img src="images/Arch_Window.png" width=16px> [Fenster](Arch_Window/de.md)**-Button oder drücken Sie **W**, dann **I**.
8.  Um die Fensterkomponenten und verschiedene Eigenschaften anzupassen, aktivieren Sie das [Aufgaben-Paneel](Task_panel/de.md) durch Doppelklick auf das erstellte Objekt in der [Baumansicht](Tree_view/de.md).


**Hinweis:**

Achten Sie bei der Erstellung der Skizze genau auf die Erstellungsreihenfolge der Schleifen; die Nummerierung der \"Linienzüge\" in der [Baumansicht](Tree_view/de.md) (\"Windows elements\") hängt hiervon ab.

## Voreinstellungen

Die folgenden Voreinstellungen sind verfügbar:

Image:ParametersDoorGlass.svg\|Glastür Image:ParametersDoorSimple.svg\|Einfache Tür Image:ParametersWindowDouble.svg\|Doppelfenster Image:ParametersWindowFixed.svg\|Festes Fenster Image:ParametersWindowSimple.svg\|Einzelfenster Image:ParametersWindowStash.svg\|Schiebefenster

## Teilkomponenten

Fenster können drei Arten von Komponenten enthalten: Rahmen, Füllungen und Lüftungsschlitze. Füllungen und Lüftungsschlitze werden aus einer geschlossenen Linie extrudiert, während Rahmen aus zwei oder mehr geschlossenen Kantenzügen bestehen, welche jeder extrudiert und anschließend die kleineren vom größten subtrahiert werden. Im Editiermodus (Doppelklick auf die Baumansicht) können Fensterkomponenten erzeugt, geändert und gelöscht werden. Die Komponenten besitzen folgende Eigenschaften:

-   **Name**: der Komponentenname
-   **Type**: der Komponententyp. Dies kann \"Frame\" (Rahmen), \"Glass panel\" (Glasfüllung), \"Solid panel\" (massive Füllung) oder \"Louvres\" (Lüftungsschlitz) sein.
-   **Wires**: eine durch Kommata getrennte Liste von Drähten, auf denen die Komponente basiert
-   **Thickness**: die Extrusionsdicke der Komponente
-   **Z Offset**: der Abstand zwischen der Komponente und ihrer 2D-Drähte
-   **Hinge**: Dies erlaubt es, eine Kante des Basis-2D-Objekts auszuwählen, diese als Scharnier (hinge) für diese Komponente und die nächsten in der Liste zu setzen
-   **Opening mode**: Wenn in dieser Komponente oder einer früheren in der Liste ein Scharnier definiert wurde, erlaubt das Setzen des \"Opening mode\" das Fenster als \"offen\" erscheinen zu lassen oder 2D-Symbole für \"zu-öffnend\" in Drauf- oder Seitenansichten anzuzeigen.

<img alt="" src=images/Arch_Window_options.jpg  style="width:600px;">

## Optionen

-   Fenster teilen die gemeinsamen Eigenschaften und Verhaltensweisen aller [Arch-Komponenten](Arch_Component/de.md)
-   Falls das **Auto-include**-Ankreuzfeld auf dem Fenstererstellungs-Aufgabenpaneel nicht aktiviert ist, wird das Fenster bei der Erstellung in kein Host-Objekt eingefügt
-   Füge ein Fenster in eine [Wand](Arch_Wall/de.md) ein, indem du beide auswählst und dann die **<img src="images/Arch_Add.svg" width=16px> [Hinzufügen](Arch_Add/de.md)**-Schaltfläche drückst.
-   Entferne ein Fenster aus einer [Wand](Arch_Wall/de.md), indem du das Fenster auswählst und dann die **<img src="images/Arch_Remove.svg" width=16px> [Komponente Entfernen](Arch_Add/de.md)**-Schaltfläche drückst.
-   Beim Verwenden von Voreinstellungen ist es oft bequem, die [Entwurf Fang](Draft_Snap/de.md)-Option \"Nächste\" einzuschalten, so dass du dein Fenster an eine vorhandene Fläche einrasten lassen kannst.
-   Das durch ein Fenster erzeugte Loch in einem Host-Objekt wird durch zwei Eigenschaften festgelegt: {{PropertyData/de|Hole Depth}} and {{PropertyData/de|Hole Wire}} ({{Version/de|0.17}}). Die Hole Wire-Nummer ist in der 3D-Ansicht des Fenster-Aufgabenpaneels sichtbar nach einem Doppelklick auf das Fenster in der Baumansicht
-   Fenster können [MehrfachMaterial](Arch_MultiMaterial/de.md) verwenden. Das Fenster wird im beigefügten Mehrfachmaterial für jede Fenster-Komponente nach Materialebenen mit gleichem Namen suchen und sie benutzen. Bspw. wird eine Komponente namens \"OuterFrame\" in dem beigefügten Mehrfachmaterial nach einer Materialebene namens \"OuterFrame\" suchen. Wenn solch eine Materialebene gefunden wird, wird dieses Material der OuterFrame-Komponente zugeordnet. Der \"Thickness\"-Wert der Materialebene wird nicht beachtet.

## Öffnungen


**Siehe auch:**

[Tutorium für offene Fenster](Tutorial_for_open_windows/de.md)

Türen und Fenster können im 3D-Modell teilweise oder vollständig geöffnet erscheinen oder mit \"zu öffnend\"-Symbolen sowohl in Drauf- und/oder Seitenansichten dargestellt werden. Deshalb werden diese auch in \"extrahierten\" 2D-Ansichten angezeigt, die durch [Form in 2D-Ansicht](Draft_Shape2DView/de.md) oder [TechDraw-Arbeitsbereich](TechDraw_Workbench/de.md) oder [Zeichnung-Arbeitsbereich](Drawing_Workbench/de.md) generiert werden. Um dies zu erreichen, muss für wenigstens eine der Fensterkomponenten ein Scharnier und ein Öffnungsmodus definiert sein (siehe [Teilkomponenten](#Building_components/de.md) oben). Dann kann mit Hilfe der **Opening**-, **Symbol Plan**- oder **Symbol Elevation**-Eigenschaften das Aussehen des Fensters konfiguriert werden.

<img alt="" src=images/Arch_window_openings.png  style="width:600px;"> 
*Eine Tür, die den Symbolplan, die Symbolhöhe und die Öffnungseigenschaften bei der Arbeit zeigt*

## Festlegen von Fenstertypen 

Fenster kann auch andere Werkzeuge nutzen, insbesondere [PartDesign](PartDesign_Workbench/de.md) Arbeitsabläufe, um einen Typ zu definieren. Ein Typ ist ein Objekt, das die Form des Fensters definiert. Dies eignet sich besonders gut für die Arbeit mit [Anwendung Part](App_Part/de.md):

<img alt="" src=images/Arch_window_type_example.png  style="width:800px;">

[Lade die oben gezeigte Beispieldatei herunter](https://github.com/FreeCAD/Examples/blob/master/Arch_Example_Files/Window_Type.FCStd)

### Beispiel Arbeitsablauf 

-   Erstelle ein Fenster-Rahmen-Objekt, eine Glasscheibe oder jede andere Fenster-Komponente, die du brauchst, mit den Werkzeugen des [Part](Part/de.md)- oder [PartDesign](PartDesign_Workbench/de.md)-Arbeitsbereichs
-   Erstelle bspw. eine rechteckige Basisskizze für dein Fenster, dann eine Profilskizze für den Rahmen und eine [Austragung](Part_Sweep/de.md), um das Profil um die Basisskizze herumzuführen. Erstelle einen [Versatz2D](Part_Offset2D/de.md) von der Basisskizze, [extrudiere](Part_Extrude/de.md) dann zur Erstellung der Glasscheibe
-   Stelle sicher, dass alle Teile einen eindeutigen, aussagekräftigen Namen haben (z.B. \"Rahmen\" oder \"Glasscheibe\")
-   Erstelle einen [App Teil](App_Part/de.md) und platziere alle Subkomponenten darin
-   Erstelle einen Volumenkörper (volume), um ihn von der Wand zu subtrahieren, z.B. durch Extrudieren der Basisskizze. Füge diesen Volumenkörper dem Teil hinzu. Stelle sicher, dass dieser Volumenkörper ausgeschaltet ist
-   Falls FreeCAD v0.19 oder später verwendet wird, kannst du durch Rechtsklick in der Eigenschaftenansicht \"Alle anzeigen\" aktivieren und drei Eigenschaften zu deinem App Teil hinzufügen. Füge die folgenden Eigenschaften hinzu (alle von ihnen sind optional, die Gruppe spielt keine Rolle):
    -   **Height** als PropertyLength und verbinde sie z.B. mit einer vertikalen Beschränkung deiner Basisskizze
    -   **Width** als PropertyLength und verbinde sie z.B. mit einer horizontalen Beschränkung deiner Basisskizze
    -   **Subvolume** als PropertyLink und verbinde sie z.B. mit dem Volumenkörper, den wir oben erstellt haben
    -   **Tag** als PropertyString

### Werkstoffe

Unser Fenster-Typ ist nun fertig. Wir können Fenster-Objekte daraus erstellt durch einfache Auswahl des App-Teils und drücken der Fenster-Schaltfläche. Die \"Height\"-, \"Width\"-, \"Subvolume\"- und \"Tag\"-Eigenschaften des Fensters werden mit dem entsprechenden Eigenschaften des App-Teils verbunden, soweit vorhanden.

Um Materialien für typbasierte Fenster zu erstellen:

-   Erstelle ein [MehrfachMaterial](Arch_MultiMaterial/de.md)
-   Erstelle einen Eintrag im Mehrfachmaterial für jede Komponente deines App-Teils, z.B. ein \"Rahmen\", eine \"Glasscheibe\" wie oben benutzt. Stelle sicher, exakt den gleichen Namen zu benutzen
-   Ordne dieses Mehrfachmaterial jedem Fenster zu, das vom gleichen Typ abgeleitet ist

Du kannst einen beliebig anderen Arbeitsablauf verwenden, solange du folgende wichtige Punkte berücksichtigst:

-   Das Typ-Objekt muss ein Objekt sein, ungeachtet des Typs ([App Teil](App_Part/de.md), [Körper](PartDesign_Body/de.md), [Verbund](Part_Compound/de.md) oder auch ein weiteres [Fenster](Arch_Window/de.md))
-   Das Typ-Objekt muss eine \"Subvolume\"-Eigenschaft (verbunden mit der Fenster-Subvolume-Eigenschaft) für Öffnungen in Host-Objekten haben, um zu funktionieren
-   Das Typ-Objekt muss eine \"Group\"-Eigenschaft mit unterschiedlichen \"Kindern\" haben, deren Namen mit den Namen von Mehrfachmaterial-Elementen übereinstimmen, um zu funktionieren

## Eigenschaften

-    {{PropertyData/de|Height}}: Die Höhe dieses Fensters

-    {{PropertyData/de|Width}}: Die Breite dieses Fensters

-    {{PropertyData/de|Hole Depth}}: Die Tiefe der Öffnung (hole), die durch dieses Fenster im Host-Objekt erzeugt wird

-    {{PropertyData/de|Hole Wire}}: Die Nummer des Linienzuges des Basisobjekts, das für die Erstellung einer Öffnung im Host-Objekt dieses Fensters benutzt wird. Dieser Wert kann grafisch gesetzt werden durch doppelklicken des Fensters in der Baumansicht. Durch Setzen eines Wertes von 0 wählt das Fenster automatisch den größten Linienzug für die Öffnung

-    {{PropertyData/de|Window Parts}}: Eine String-Liste (fünf Zeichenketten pro Komponente zum Setzen der o.g. Komponentenoptionen)

-    {{PropertyData/de|Louvre Width}}: Falls eine der Komponenten auf \"Louvres\" gesetzt ist, definiert diese Eigenschaft die Breite der Lüftungsschlitzelemente

-    {{PropertyData/de|Louvre Spacing}}: Falls eine der Komponenten auf \"Louvres\" gesetzt ist, definiert diese Eigenschaft den Abstand zwischen den Lüftungsschlitzelementen

-    {{PropertyData/de|Opening}}: Alle Komponenten mit gesetzter \"Opening Mode\"-Eigenschaft und definiertem Scharnier in dieser oder einer vorherigen Komponente in der Liste werden als n% offen erscheinen. n wird durch den gesetzten Wert definiert

-    {{PropertyData/de|Symbol Plan}}: Zeigt 2D-Symbole für \"zu öffnend\" in der Draufsicht

-    {{PropertyData/de|Symbol Elevation}}: Zeigt 2D-Symbole für \"zu öffnend\" in Seitenansichten

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Fensterwerkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit der folgenden Funktion verwendet werden: 
```python
Window = makeWindow(baseobj=None, width=None, height=None, parts=None, name="Window")
```

-   Erzeugt ein `Window`-Objekt basierend auf einem `baseobj`, das ein(e) wohlgeformte(r), geschlossene(r) [Linienzug](Draft_Wire/de.md) oder [Skizze](Sketcher_Sketch/de.md) sein sollte.
-   Falls verfügbar, sollten `width`, `height` und `name` des Fensters gesetzt werden.
-   Falls `baseobj` keine geschlossene Form ist, kann das Werkzeug keinen korrekten Volumenkörper erzeugen.

Beispiel: 
```python
import FreeCAD, Draft, Arch

Rect1 = Draft.makeRectangle(length=900, height=3000)
Window = Arch.makeWindow(Rect1)
FreeCAD.ActiveDocument.recompute()
```

Sie können auch aus einer Vorlage ein Fenster erzeugen. 
```python
Window = makeWindowPreset(windowtype, width, height, h1, h2, h3, w1, w2, o1, o2, placement=None)
```

-   Erstellt ein `Fenster` objekt basierend auf `Fenstertyp`, die einer der Namen sein sollte, die in `Arch.WindowPresets` festgelegt ist
    -   Einige dieser Voreinstellungen sind: `"Fixed"`, `"Offen 1-Fensterscheibe"`, `"Offen 2-Fensterscheiben"`, `"Fensterflügel 2-Fensterscheiben"`, `"Schiebe 2-Fensterscheiben"`, `"Einfache Tür"`, `"Glastür"`, `"Schiebe 4-Fensterscheiben"`.

-    `Breite`und `Höhe` lege die Gesamtgröße des Objekts mit Einheiten in Millimetern fest.

-   Die Parameter `h1`, `h2`, `h3` (vertikale Versatze), `w1`, `w2` (Breiten), `o1`, und `o2` (horizontale Versatze) gib verschiedene Abstände in Millimetern an und hänge von der Art der erstellten Voreinstellung ab.

-   Wenn eine `PLatzierung` angegeben wird, wird es verwendet.

Beispiel: 
```python
import FreeCAD, Arch

base = FreeCAD.Vector(2000, 0, 0)
Axis = FreeCAD.Vector(1, 0, 0)
place=FreeCAD.Placement(base, FreeCAD.Rotation(Axis, 90))

Door = Arch.makeWindowPreset("Simple door",
                             width=900, height=2000,
                             h1=100, h2=100, h3=100, w1=200, w2=100, o1=0, o2=100,
                             placement=place)
```









