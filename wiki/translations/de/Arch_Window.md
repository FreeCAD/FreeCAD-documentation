---
 GuiCommand:
   Name: Arch Window
   Name/de: Arch Fenster
   MenuLocation: 3D/BIM , Fenster
   Workbenches: BIM_Workbench/de
   Shortcut: **W** **I**
   SeeAlso: 
---

# Arch Window/de



## Beschreibung

Das Werkzeug **Arch Fenster** ist ein Basisobjekt für alle Arten von \"einbettbaren\" Objekten, wie z.B. Fenster und Türen. Es ist so konzipiert, dass es entweder unabhängig ist oder in einer anderen Komponente \"untergebracht\" wird, wie z.B. einer [Arch-Wand](Arch_Wall/de.md), [Arch-Struktur](Arch_Structure/de.md) oder einem [Arch-Dach](Arch_Roof/de.md). Es hat eine eigene Geometrie, die aus mehreren festen Komponenten bestehen kann (üblicherweise aus einem Rahmen und inneren Platten), und definiert auch ein Volumen, das von den aufnehmenden Objekten abgezogen wird, um eine Öffnung zu erzeugen.

Fensterobjekte basieren auf geschlossenen 2D Objekten, wie z.B. [Entwurf Rechtecken](Draft_Rectangle/de.md) oder [Skizzen](Sketcher_Workbench/de.md), die zur Definition der inneren Fensterkomponenten verwendet werden. Das zugrundeliegende 2D Objekt muss also mehrere geschlossene Kantenzüge (Wire) enthalten, welche kombiniert werden können, um gefüllte Platten (ein Kantenzug) oder Rahmen (mehrere Kantenzüge) zu definieren.

Das Werkzeug Fenster besitzt mehrere [Voreinstellungen](#Voreinstellungen.md). Diese ermöglichen dem Benutzer, gängige Arten von Fenstern und Türen mit bestimmten änderbaren Parametern zu erstellen, ohne dass der Benutzer die 2D-Basisobjekte und Komponenten manuell erstellen muss.

Jede auf ein Arch-Fenster zutreffende Information gilt auch für eine [Arch-Tür](Arch_Door/de.md), da es sich um das gleiche zugrundeliegende Objekt handelt.

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;"> 
*Komplexes Fenster, das auf einer [Skizze](Sketcher_Workbench/de.md) konstruiert wird. Wenn du in den Bearbeitungsmodus des Fensters eintritts, kannst du verschiedene Komponenten erstellen, ihre Dicke einstellen und Drähte aus der Skizze auswählen und ihnen zuweisen.*



## Anwendung



### Eine Voreinstellung verwenden 

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Arch_Window.svg" width=16px> [Fenster](Arch_Window/de.md)** drücken.
    -   Den Menüeintrag **3D/BIM → <img src="images/Arch_Window.svg" width=16px> Fenster** auswählen.
    -   Das Tastaturkürzel **W** dann **I**.
2.  Eine der Voreinstellungen in der Liste auswählen.
3.  Die gewünschten Parameter ausfüllen.
4.  In der [3D-Ansicht](3D_view/de.md) das Fenster an die Stelle bewegen, an der es positioniert werden soll. Wenn der Mauszeiger über eine [Arch-Wand](Arch_Wall/de.md) bewegt wird, sollte sich der Umriss des Fensters an der Fläche dieses Objekts ausrichten.
5.  Mit der Maus in die [3D-Ansicht](3D_view/de.md) klicken oder dreimal die **Eingabe**-Taste drücken, um die X-, Y-, Z-Koordinaten der Positionierung zu bestätigen.



#### Zusätzliche Voreinstellungen 

Falls die [Parts Library](Parts_Library_Workbench/de.md) mit dem [Addon-Manager](Std_AddonMgr/de.md) installiert wurde, wird das Werkzeug Fenster diese Bibliothek nach weiteren Voreinstellungen durchsuchen. Diese Voreinstellungen sind FreeCAD-Dateien, die jeweils ein einzelnes Fenster basierend auf einer parametrisierten Skizze mit benannten Randbedingungen enthalten. Es können zusätzliche Voreinstellungen im **parts_library**-Verzeichnis abgelegt werden, so dass sie vom Werkzeug Fenster gefunden werden.


**$ROOT_DIR/Mod/parts_library/Architectural Parts/Doors/Custom/**

**$ROOT_DIR/Mod/parts_library/Architectural Parts/Windows/Custom/**

-    **$ROOT_DIR**ist das Benutzerverzeichnis in dem FreeCADs Konfigurationsdateien, Makros und externe Arbeitsbereiche gespeichert werden. Es wird gefunden, wenn man `FreeCAD.getUserAppDataDir()` in der [Python-Konsole](Python_console/de.md) eingibt.

    -   Unter Linux ist es normalerweise **/home/username/.local/share/FreeCAD/** ({{VersionPlus/de|0.20}}) oder **/home/username/.FreeCAD/** ({{VersionMinus/de|0.19}})
    -   Unter Windows ist es normalerweise **C:\Users\username\Application Data\FreeCAD\**
    -   Unter Mac OSX ist es normalerweise **/Users/username/Library/Preferences/FreeCAD/**

-   Der Name des Unterverzeichnisses **Custom** ist nur ein Vorschlag; jeder beliebige Name kann verwendet werden, aber die Dateien müssen in einem oder mehreren Unterverzeichnissen innerhalb der Verzeichnisse **Doors** oder **Windows** abgelegt werden.



### Ein individuelles Fenster erstellen 

1.  Wahlweise eine Fläche des Arch-Objekts auswählen, wo das Fenster eingefügt werden soll.
2.  Zum Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) wechseln.
3.  Eine neue Skizze erstellen.
4.  Einen oder mehrere geschlossene Linienzüge (Schleifen) zeichnen. Man sollte genau auf die Auswahlreihenfolge dieser Schleifen achten, die Nummerierung von Linienzügen im [Aufgaben-Bereich](Task_panel/de.md) (\"Window elements\") hängt davon ab.
5.  Die Skizze schließen.
6.  Zurück zum Arbeitsbereich [BIM](BIM_Workbench/de.md) wechseln.
7.  Das Werkzeug wie oben beschrieben aufrufen.
8.  Um die Fensterkomponenten und verschiedene Eigenschaften anzupassen, wird der [Aufgaben-Bereich](Task_panel/de.md) Fenster durch Doppelklick auf das erstellte Objekt in der [Baumansicht](Tree_view/de.md) geöffnet.
9.  Es ist zu beachten, dass, da Komponenten die einer drehbaren Komponente folgen auch drehbar sind, alle unbeweglichen Komponenten wie die äußeren Rahmen und fest verbaute Glasscheiben vor den drehbaren Komponenten festgelegt werden müssen. Und eine Glasscheibe in einem drehbaren Rahmen muss nach diesem Rahmen und vor allen weiteren Komponenten festgelegt werden



## Voreinstellungen

Die folgenden Voreinstellungen sind verfügbar:

Image:ParametersWindowFixed.svg\|Feststehendes Fenster Image:ParametersWindowSimple.svg\|Einzelfenster Image:ParametersWindowDouble.svg\|Doppelfenster Image:ParametersWindowStash.svg\|Schiebefenster Image:ParametersWindowDouble.svg\|Schiebefenster, seitwärts Image:ParametersDoorSimple.svg\|Einfache Tür Image:ParametersDoorGlass.svg\|Glastür Image:ParametersWindowDouble.svg\|Doppelfenster Image:ParametersWindowSimple.svg\|Einzelfenster Image:ParametersOpening.svg\|Nur Öffnung {{Version/de|1.0}}



## Teilkomponenten

Fenster können vier Arten von Komponenten enthalten: Rahmen, opake Füllungen Glasfüllungen und Lüftungsschlitze. Füllungen und Lüftungsschlitze werden aus einem geschlossenen Linienzug extrudiert, während Rahmen aus zwei oder mehr geschlossenen Linienzügen bestehen, die jeweils für sich extrudiert werden und anschließend die kleineren vom größten subtrahiert werden. Im Bearbeitungsmodus (Doppelklick in der Baumansicht) können Fensterkomponenten erzeugt, geändert und gelöscht werden. Die Komponenten besitzen folgende Eigenschaften:

-   **Name**: der Komponentenname
-   **Type**: der Komponententyp. Dies kann \"Frame\" (Rahmen), \"Glass panel\" (Glasfüllung), \"Solid panel\" (massive Füllung) oder \"Louvres\" (Lüftungsschlitz) sein.
-   **Wires**: eine durch Kommata getrennte Liste von Drähten, auf denen die Komponente basiert
-   **Thickness**: die Extrusionsdicke der Komponente
-   **Z Offset**: der Abstand zwischen der Komponente und ihrer 2D-Drähte
-   **Hinge**: Dies erlaubt es, eine Kante des Basis-2D-Objekts auszuwählen, diese als Scharnier (hinge) für diese Komponente und die nächsten in der Liste zu setzen
-   **Opening mode**: Wenn in dieser Komponente oder einer früheren in der Liste ein Scharnier definiert wurde, erlaubt das Setzen des \"Opening mode\" das Fenster als \"offen\" erscheinen zu lassen oder 2D-Symbole für \"zu-öffnend\" in Drauf- oder Seitenansichten anzuzeigen.

<img alt="" src=images/Arch_Window_options.jpg  style="width:600px;">



## Optionen

-   Fenster besitzen die allgemeinen Eigenschaften und Verhaltensweisen aller [Arch-Komponenten](Arch_Component/de.md)
-   Ist die Checkbox **Automatisch in Host-Objekt einfügen** unter Fensteroptionen im Aufgaben-Bereich nicht aktiviert, wird das Fenster bei der Erstellung in kein Host-Objekt eingefügt
-   Ein Fenster in eine [Wand](Arch_Wall/de.md) einfügen, indem beide ausgewählt werden und dann die Schaltfläche **<img src="images/Arch_Add.svg" width=16px> [Hinzufügen](Arch_Add/de.md)** gedrückt wird.
-   Ein Fenster aus einer [Wand](Arch_Wall/de.md) entfernen, indem das Fenster ausgewählt und dann die Schaltfläche **<img src="images/Arch_Remove.svg" width=16px> [Komponente Entfernen](Arch_Add/de.md)** gedrückt wird.
-   Beim Verwenden von Voreinstellungen ist es oft praktisch, [Draft EinrastenInDerNähe](Draft_Snap/de.md) einzuschalten, so dass dein Fenster auf einer vorhandenen Fläche einrasten kann.
-   Das durch ein Fenster erzeugte Loch in seinem Host-Objekt wird durch zwei Eigenschaften festgelegt: {{PropertyData/de|Hole Depth}} und {{PropertyData/de|Hole Wire}} ({{Version/de|0.17}}). Die Hole Wire-Zahl kann in der 3D-Ansicht im Aufgaben-Bereich des Fensters ausgewählt werden, nachdem das Fenster mit einem Doppelklick in der Baumansicht aktiviert wurde.
-   Fenster können [MehrfachMaterial](Arch_MultiMaterial/de.md) verwenden. Das Fenster wird im beigefügten Mehrfachmaterial für jede Fenster-Komponente nach Materialebenen mit gleichem Namen suchen und sie benutzen. Bspw. wird eine Komponente namens \"OuterFrame\" in dem beigefügten Mehrfachmaterial nach einer Materialebene namens \"OuterFrame\" suchen. Wenn solch eine Materialebene gefunden wird, wird dieses Material der OuterFrame-Komponente zugeordnet. Der \"Thickness\"-Wert der Materialebene wird nicht beachtet.



## Öffnungen


**Siehe auch:**

[Tutorium für offene Fenster](Tutorial_for_open_windows/de.md)

Türen und Fenster können im 3D-Modell teilweise oder vollständig geöffnet erscheinen oder mit \"zu öffnen\"-Symbolen sowohl in Drauf- und/oder Seitenansichten dargestellt werden. Deshalb werden diese auch in \"extrahierten\" 2D-Ansichten angezeigt, die mit [Form2DAnsicht](Draft_Shape2DView/de.md) oder im Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) generiert werden. Um dies zu erreichen, muss für wenigstens eine der Fensterkomponenten ein Scharnier und ein Öffnungsmodus definiert sein (siehe [Teilkomponenten](#Building_components/de.md) oben). Dann kann mit Hilfe der {{PropertyData/de|Opening}}, der {{PropertyData/de|Symbol Plan}} oder der {{PropertyData/de|Symbol Elevation}} das Aussehen des Fensters konfiguriert werden.

<img alt="" src=images/Arch_window_openings.png  style="width:600px;"> 
*Eine Tür, die den Symbolplan, die Symbolhöhe und die Öffnungseigenschaften bei der Arbeit zeigt*



## Festlegen von Fenstertypen 

Fenster kann auch andere Werkzeuge nutzen, insbesondere [PartDesign](PartDesign_Workbench/de.md) Arbeitsabläufe, um einen Typ zu definieren. Ein Typ ist ein Objekt, das die Form des Fensters definiert. Dies eignet sich besonders gut für die Arbeit mit [Anwendung Part](App_Part/de.md):

<img alt="" src=images/Arch_window_type_example.png  style="width:800px;">

[Lade die oben gezeigte Beispieldatei herunter](https://github.com/FreeCAD/Examples/raw/master/Arch_Example_Files/Window_Type.FCStd)



### Beispiel Arbeitsablauf 

-   Ein Fensterrahmen-Objekt, eine Glasscheibe und jede andere Fenster-Komponente, die benötigt wird, mit den Werkzeugen der Arbeitsbereiche [Part](Part_Workbench/de.md) oder [PartDesign](PartDesign_Workbench/de.md) erstellen.
-   Z.B. eine rechteckige Basisskizze für das Fenster erstellen, dann eine Profilskizze für den Rahmen und eine [Austragung](Part_Sweep/de.md) erstellen, um das Profil um die Basisskizze herumzuführen. Von der Basisskizze einen [2DVersatz](Part_Offset2D/de.md) erstellen und diesen [extrudieren](Part_Extrude/de.md) zum Erstellen der Glasscheibe.
-   Sicherstellen, dass alle Teile einen eindeutigen, aussagekräftigen Namen haben (z.B. \"Rahmen\" oder \"Glasscheibe\")
-   Ein [App-Part](App_Part/de.md) erstellen und alle Unterkomponenten darin platzieren.
-   Einen Volumen(körper) erstellen, um es von der Wand abzuziehen, z.B. durch Extrudieren der Basisskizze. Dieses Volumen zum App-Part hinzufügen. Sicherstellen, dass dieser Volumenkörper ausgeschaltet ist
-   Wird FreeCAD Version 0.19 oder neuer verwendet, können mit einen Rechtsklick im Eigenschafteneditor und dem Auswählen von \"Alle anzeigen\" 3 Eigenschaften zum App-Part hinzugefügt werden. Die folgenden Eigenschaften hinzufügen (alle sind optional, die Gruppe spielt keine Rolle):
    -   **Height** als PropertyLength hinzufügen und z.B. mit einer vertikalen Randbedingung der Basisskizze verbinden.
    -   **Width** als PropertyLength hinzufügen und z.B. mit einer horizontalen Randbedingung deiner Basisskizze verbinden.
    -   **Subvolume** als PropertyLink hinzufügen und z.B. mit dem Volumenkörper verbinden, den wir oben erstellt haben
    -   **Tag** als PropertyString hinzufügen.

Unser Fenster-Typ ist nun fertig. Wir können Fenster-Objekte daraus erstellt durch einfache Auswahl des App-Teils und drücken der Fenster-Schaltfläche. Die \"Height\"-, \"Width\"-, \"Subvolume\"- und \"Tag\"-Eigenschaften des Fensters werden mit dem entsprechenden Eigenschaften des App-Teils verbunden, soweit vorhanden.



### Werkstoffe

Um Materialien für typbasierte Fenster zu erstellen:

-   Erstelle ein [MehrfachMaterial](Arch_MultiMaterial/de.md)
-   Erstelle einen Eintrag im Mehrfachmaterial für jede Komponente deines App-Teils, z.B. ein \"Rahmen\", eine \"Glasscheibe\" wie oben benutzt. Stelle sicher, exakt den gleichen Namen zu benutzen
-   Ordne dieses Mehrfachmaterial jedem Fenster zu, das vom gleichen Typ abgeleitet ist

Du kannst einen beliebig anderen Arbeitsablauf verwenden, solange du folgende wichtige Punkte berücksichtigst:

-   Das Typ-Objekt muss ein Objekt sein, ungeachtet des Typs ([App Teil](App_Part/de.md), [Körper](PartDesign_Body/de.md), [Verbund](Part_Compound/de.md) oder auch ein weiteres [Fenster](Arch_Window/de.md))
-   Das Typ-Objekt muss eine \"Subvolume\"-Eigenschaft (verbunden mit der Fenster-Subvolume-Eigenschaft) für Öffnungen in Host-Objekten haben, um zu funktionieren
-   Das Typ-Objekt muss eine \"Group\"-Eigenschaft mit unterschiedlichen \"Kindern\" haben, deren Namen mit den Namen von Mehrfachmaterial-Elementen übereinstimmen, um zu funktionieren



## Eigenschaften



### Daten


{{TitleProperty|Window}}

-    {{PropertyData/de|Area|Area}}: Der Flächeninhalt dieses Fensters.

-    {{PropertyData/de|Frame|Length}}: Die Rahmengröße (Dicke/Tiefe) dieses Fensters.

-    {{PropertyData/de|Height|Length}}: Die Höhe dieses Fensters.

-    {{PropertyData/de|Hole Depth|Length}}: Die Tiefe der Öffnung (hole), die durch dieses Fenster im Host-Objekt erzeugt wird.

-    {{PropertyData/de|Hole Wire|Integer}}: Die Nummer des Linienzuges des Basisobjekts, das für die Erstellung einer Öffnung im Host-Objekt dieses Fensters eingesetzt wird. Dieser Wert kann grafisch gesetzt werden, wenn das Fenster in der Baumansicht doppelt angeklickt wird. Durch Setzen eines Wertes auf 0 wählt das Fenster automatisch den größten Linienzug für die Öffnung.

-    {{PropertyData/de|Hosts|LinkList}}: Die Objekte (z.B. Wände), die dieses Fenster aufnehmen.

-    {{PropertyData/de|Louvre Spacing|Length}}: Wenn eine der Komponenten auf \"Louvres\" (Kiemen) gesetzt ist, legt diese Eigenschaft den Abstand zwischen den Kiemenelementen fest.

-    {{PropertyData/de|Louvre Width|Length}}: Wenn eine der Komponenten auf \"Louvres\" (Kiemen) gesetzt ist, legt diese Eigenschaft die Breite der Kiemenelemente fest.

-    {{PropertyData/de|Normal|Vector}}: Die Richtung der Normale dieses Fensters, die durch das Werkzeug Fenster im interaktiven Modus gesetzt wird (hardcoded). Bemerkung: Auf (0,0,0) setzen, damit das Fenster die Richtung der Normale automatisch herleitet; dies ist nützlich, wenn der Anwender die Basisskizze des Fensters dreht, z.B. wenn seine Host-Wand gedreht wurde.

-    {{PropertyData/de|Offset|Length}}: Die Größe des Abstands (von der Basisskizze) dieses Fensters.

-    {{PropertyData/de|Opening|Percent}}: Alle Komponenten, für die ein Öffnungsart angegeben ist, und vorausgesetzt sie oder eine vorherige Komponente enthalten eine Definition für ein Scharnier, werden zu einem mit diesem Wert festgelegten Prozentsatz geöffnet dargestellt.

-    {{PropertyData/de|Preset|Integer|Hidden}}: Die Kennzahl der Voreinstellung auf der dieses Fenster basiert.

-    {{PropertyData/de|Subvolume|Link}}: Ein optionales Objekt, das ein Volumen festlegt, das von den Hosts dieses Fensters abgezogen wird. object that defines a volume to be subtracted from hosts of this window.

-    {{PropertyData/de|Symbol Elevation|Bool}}: Zeigt 2D-Symbole für Öffnungsart der Fenster im Aufriss.

-    {{PropertyData/de|Symbol Plan|Bool}}: Zeigt 2D-Symbole für Öffnungsart der Fenster im Grundriss.

-    {{PropertyData/de|Width}}: Die Breite dieses Fensters.

-    {{PropertyData/de|Window Parts|StringList|Hidden}}: Die Komponenten dieses Fensters (5 Zeichenketten pro Komponente).



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Fenster kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit der folgenden Funktion verwendet werden:


```python
Window = makeWindow(baseobj=None, width=None, height=None, parts=None, name="Window")
```

-   Erzeugt ein `Window`-Objekt basierend auf einem `baseobj`, das ein(e) wohlgeformte(r), geschlossene(r) [Linienzug](Draft_Wire/de.md) oder [Skizze](Sketcher_Workbench/de.md) sein sollte.
-   Falls verfügbar, sollten `width`, `height` und `name` des Fensters gesetzt werden.
-   Falls `baseobj` keine geschlossene Form ist, kann das Werkzeug keinen korrekten Festkörper erzeugen.

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

-   Erstellt ein `Fenster`-Objekt basierend auf `Fenstertyp`, der einem der Namen entsprechen sollte, die in `Arch.WindowPresets` festgelegt sind.

-    `Breite`und `Höhe` legen die Gesamtgröße des Objekts mit Einheiten in Millimetern fest.

-   Die Parameter `h1`, `h2`, `h3` (vertikale Versatze), `w1`, `w2` (Breiten), `o1`, und `o2` (horizontale Versatze) geben verschiedene Abstände in Millimetern an und hängen von der Art der Voreinstellung ab, die erstellt wird.

-   Wenn eine `Positionierung` angegeben wurde, wird sie verwendet.

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



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Window/de
