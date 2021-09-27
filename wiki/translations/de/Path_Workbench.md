# <img alt="Pfad Arbeitsbereichssymbol" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/de


{{TOCright}}

## Einführung

Der <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Pfad Arbeitsbereich](Path_Workbench/de.md) wird verwendet, um Maschinenanweisungen für [CNC Maschinen](https://en.wikipedia.org/wiki/CNC_router) aus einem FreeCAD 3D Modell zu erstellen. Diese erzeugen reale 3D Objekte auf CNC Maschinen wie Fräsmaschinen, Drehbänken, Laserschneidern oder ähnlichem. Typischerweise handelt es sich bei den Anweisungen um einen [G-code](https://en.wikipedia.org/wiki/G-code) Dialekt. Hier wird ein [allgemeines Beispiel für die Simulation einer CNC Drehbank Werkzeugpfadfolge](https://www.ange-softs.com/SIMULCNCHTML/index.html) vorgestellt.

<img alt="" src=images/pathwb.png  style="width:600px;">

Der FreeCAD Pfad Arbeitsbereich Arbeitsablauf erstellt diese Maschinenanweisungen wie folgt:

-   Ein 3D Modell ist das Basisobjekt, das typischerweise mit einer oder mehreren der Arbeitsbereiche <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;">

[Part Design](PartDesign_Workbench/de.md), <img alt="Workbench_Part.svg" src=images/Workbench_Part.svg  style="width:24px;"> 
_ erstellt wird.

-   Ein _ und es folgen bestimmte Befehle, die die Geschwindigkeit und die Bewegungen steuern (normalerweise G-code).
-   Die Werkzeuge werden entsprechend den Anforderungen der Arbeitsauftragsabläufe ausgewählt.
-   Fräsbahnen werden z.B. mit [Kontur](Path_Profile/de.md) und [Tasche](Path_Pocket_3D/de.md) Abläufen erzeugt. Diese [Bahnobjekte](Path_objects/de.md) verwenden den internen FreeCAD G-code Dialekt, unabhängig von der CNC Maschine.
-   Exportiere den Job mit einem G-code, der zu Ihrer Maschine passt. Dieser Schritt wird *Nachbearbeitung* genannt; es sind unterschiedliche Nachbearbeitungsprozessoren verfügbar.

## Allgemeine Konzepte 

Der Pfad Arbeitsbereich erzeugt einen G-code, der die Pfade definiert, die zum Fräsen des durch das 3D Modell auf der Zielfräse in [Der Pfad Auftragsvorgang FreeCAD G-code Dialekt](Path_scripting/de#Das_FreeCAD_Interne_GCode_Format.md), die später durch Auswahl des entsprechenden Postprozessors in den entsprechenden Dialekt für die Ziel CNC Steuerung übersetzt wird.

Der G-code wird aus den in einem Pfadauftrag enthaltenen Anweisungen und Operationen generiert. Der Auftrags Arbeitsablauf listet diese in der Reihenfolge ihrer Ausführung auf. Die Liste wird durch Hinzufügen von Pfadoperationen, Pfadaufbereitungen, Pfadteilbefehlen und Pfadänderungen aus dem Pfadmenü oder den GUI Schaltflächen ausgefüllt.

Der Path Arbeitsbereich enthält einen Werkzeugverwalter (Bibliothek, Werkzeugtabelle), eine G-code Überprüfung und Simulationswerkzeuge. Es verknüpft den Postprozessor und erlaubt den Im- und Export von Auftragsvorlagen.

Der Pfad Arbeitsbereich hat externe Abhängigkeiten einschließlich:

1.  Die FreeCAD 3D Modell Einheiten sind im **Bearbeiten → Einstellungen → Allgemein → Einheiten Reiter Einheiteneinstellungen** festgelegt. Die Postprozessor Konfiguration legt die endgültigen G-code Einheiten fest.
2.  Der Pfad der Makrodatei und die geometrischen Toleranzen werden im **Bearbeiten → Einstellungen →  Pfad → Arbeitsauftag Einstellungen** definiert.
3.  Die Farben werden im Register **Bearbeiten → Einstellungen →Pfad → Pfad  Farben** definiert.
4.  Die Parameter der Halte Merker werden in dem **Bearbeiten → Einstellungen → Pfad → Aufbereitungen** Reiter definiert.
5.  Dass die Qualität des Basis 3D Modells die Anforderungen an die Pfad Arbeitsbereich unterstützt, wird durch Prüfe Geometrie bestätigt.

## Begrenzungen

Einige aktuelle Begrenzungen, derer du dir bewusst sein solltest, sind:

-   Die meisten der Pfadwerkzeuge sind keine echten 3D Werkzeuge, sondern nur 2,5D fähig. Das bedeutet, dass sie eine festgelegte 2D Form nehmen und diese bis zu einer bestimmten Tiefe herunterschneiden können. Es gibt jedoch zwei Werkzeuge, die echte 3D Pfade erzeugen: **<img src="images/Path_3DPocket.svg" width=24px> [3D Tasche](Path_Pocket_3D/de.md)** und **<img src="images/Path_3DSurface.svg" width=24px> [3D Oberfläche](Path_3DSurface/de.md)** (was ab November 2020 noch ein [experimentelle Funktion](Path_experimental/de.md) ist).
-   Der größte Teil des Pfad Arbeitsbereichs ist für eine einfache, standardmäßige 3-Achsen (xyz) CNC Fräse/Router ausgelegt, aber Drehwerkzeuge sind in 0.19\_pre in Entwicklung.
-   Die meisten Operationen im Pfad Arbeitsbereich geben nur Pfade zurück, die auf einem Standard Endfräser Werkzeug/Bit basieren, unabhängig vom zugewiesenen Werkzeug/Bit Typ in einer bestimmten Werkzeugsteuerung, mit Ausnahme der **<img src="images/Path_Engrave.svg" width=24px> [Gravur](Path_Engrave/de.md)** und **<img src="images/Path_3DSurface.svg" width=24px> [3D Oberfläche](Path_3DSurface/de.md)** Operationen.
-   Die Operationen innerhalb des Pfad Arbeitsbereichs kennen keine Spannmechanismen, die zur Befestigung des Modells an deiner Maschine verwendet werden. Überprüfe und simuliere daher die von dir erzeugten Bahnen, bevor du den Code an deine Maschine sendest. Wenn nötig, modelliere deine Spannmechanismen in FreeCAD, um die erzeugten Bahnen besser überprüfen zu können. Achte auf mögliche Kollisionen mit Spannern oder anderen Hindernissen entlang der Bahnen.

## Einheiten

Die Handhabung von Einheiten kann im Pfad Arbeitsbereich verwirrend sein. Es gibt mehrere Punkte, die verstanden werden müssen:

1.  FreeCAD Basiseinheiten für Länge und Zeit sind \'mm\' und \'s\' bzw. Geschwindigkeit ist \'mm/s\'. Diese Einheiten speichert FreeCAD intern unabhängig von allem anderem.
2.  Das standardmäßige Einheitensystem nutzt diese Basiseinheiten. Wenn du das Standard Einheitensystem benutzt und eine Vorschubgeschwindigkeit ohne eine Einheitenfolge eingibst, wird es als \'mm/s\' interpretiert.
3.  Die meisten CNC Maschinen erwarten aber Einheiten in der Form \'mm/min\'oder \'Zoll/min\'. Die meisten Postprozessoren konvertieren die Einheiten automatisch, wenn der Maschinencode generiert wird.

Schemata:

1.  Schemaänderungen in den Einstellungen ändert die Standardeinheitszeichenkette für die Eingabefelder. Wenn Du ein Pfad Anwender bist und es vorziehst, metrisch zu konstruieren, wird dringend empfohlen, das Schema \"Metrische Kleinteile & CNC\" zu verwenden. Wenn du in US Einheiten konstruierst, funktionieren entweder die Einheiten Britisches Dezimal und US Bauwesen
2.  Ändern des bevorzugten Einheitenschemas hat keine Auswirkung auf die Ausgabe, hilft aber, Eingabefehler zu vermeiden

Ausgabe:

1.  Die Generierung der korrekten Einheiten in der Ausgabe liegt in der Verantwortung des Postprozessors und geschieht nur bei diesem Vorgang.
2.  Die Einheiten für die Maschine bei der Ausgabe sind komplett unabhängig von der gewählten Einheitendarstellung.
3.  Postprozessoren erzeugen entweder metrische Einheiten (G21), imperiale Einheiten (G20) oder sind konfigurierbar.
4.  Konfigurierbare Postprozessoren generieren standardmäßig metrische Einheiten (G21).
5.  Wenn bei konfigurierbaren Postprozessoren imperiale Einheiten ausgegeben werden sollen, muss dies über Argumente in der Job-Output Konfiguration eingestellt werden (z.B.: \--inches für linuxcnc). Die Einstellungen können in einem Job Template gespeichert werden und als Standard Template benutzt werden, um es in Zukunft automatisch zu verwenden.

Pfad Untersuchen:

1.  Wenn du das Werkzeug zum Untersuchen des Pfades benutzt, wird als Einheit \'mm/s\' benutzt, da der Postprozessor noch nicht angewendet wurde.

## Höhen und Tiefen 

Viele der Befehle haben unterschiedliche Höhen und Tiefen:

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Sichtreferenz für Tiefeneigenschaften (Einstellungen)*

## Befehle

Some commands are experimental and not available by default. To enable them see [Path experimental](Path_experimental.md).

### Projektbefehle

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Auftrag](Path_Job/de.md): Erstellt einen neuen CNC Auftrag.

-   <img alt="" src=images/Path_PostProcess.svg  style="width:32px;"> [Nach Prozess](Path_Post/de.md): Exportiert ein Projekt in G-code.

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> _. {{Version/de|0.19}}

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Export Vorlage](Path_ExportTemplate/de.md): Den aktuellen Auftrag als Vorlage exportieren.

### Werkzeugbefehle

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [G-Code untersuchen](Path_Inspect/de.md): Zeigt den G-code zur Überprüfung.

-   <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [CAM Simulator](Path_Simulator/de.md): Zeigt die Fräsbearbeitung wie sie auf der Maschine durchgeführt wird.

-   <img alt="" src=images/Path_SelectLoop.svg  style="width:32px;"> [Beenden der Auswahlschleife](Path_SelectLoop/de.md): Vervollständigt eine Schleife aus zwei ausgewählten Kanten.

-   <img alt="" src=images/Path_OpActive.svg  style="width:32px;"> [Umschalten des aktiven Zustands der Bearbeitung](Path_OpActiveToggle/de.md): Aktiviert oder deaktiviert eine Pfadbearbeitung.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock. <small>(v0.19)</small> 

### Grundlegende Bearbeitungen 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile/de.md) (Neu in 0.19): Erzeugt eine Profilbearbeitung des gesamten Modells oder von einer oder mehreren ausgewählten Flächen oder Kanten. Diese Bearbeitung kombiniert die bereits vorhandenen Kontur-, Profilflächen- und Profilkantenbearbeitungen.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Pocket.svg  style="width:32px;"> [Tasche](Path_Pocket_Shape/de.md): Erzeugt eine Taschenbearbeitung aus einer oder mehreren ausgewählten Taschen


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Bohren](Path_Drilling/de.md): Führt einen Bohrzyklus durch


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Face.svg  style="width:32px;"> [Fläche fräsen](Path_MillFace/de.md): Erzeugt einen Oberflächenpfad


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Helix](Path_Helix/de.md): Erzeugt eine spiralförmige Bahn


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptiv](Path_Adaptive/de.md): Erstellt eine adaptive Räum- und Profilierungsoperation


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Nut](Path_Slot/de.md) (Neu in 0.19): Erzeugt eine Nutenfräsbearbeitung aus ausgewählten Formelementen oder benutzerdefinierten Punkten


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Gravieren](Path_Engrave/de.md): Erstellt einen Gravurpfad


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [VGravur](Path_Vcarve/de.md): Erzeugt einen Pfad für eine 3D Tasche


</div>

### 3D Operations 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_3DPocket.svg  style="width:32px;"> [3D Tasche](Path_Pocket_3D/de.md): Erzeugt einen Pfad für eine 3D Tasche


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-3DSurface.svg  style="width:32px;"> [3D Oberfläche](Path_3DSurface/de.md): Erstellt einen Pfad für eine 3D Oberfläche (experimentell, 0.19 )


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Wasserlinie](Path_Waterline/de.md): Erzeugt einen Wasserlinienpfad für eine 3D Oberfläche (experimentell, 0.19)


</div>


<div class="mw-translate-fuzzy">

### Pfad Aufbereitung 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Randaufbereitung](Path_DressupBoundary/de.md): Fügt eine Randaufbereitungsänderung einem ausgewählten Pfad hinzu


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDogbone.svg  style="width:32px;"> [Hundeknochen Aufbereitung](Path_DressupDogbone/de.md): Fügt eine Hundeknochen Aufbereitungsänderung einem ausgewählten Pfad hinzu


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [Ziehmesser Aufbereitung](Path_DressupDragKnife/de.md): Fügt eine Ziehmesser Aufbereitungsänderung einem ausgewählten Pfad hinzu


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [Lead In Dressup](Path_DressupLeadInOut/de.md): Fügt einen Einführungs- und/oder Ausführungspunkt einem ausgewählten Pfad hinzu


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [Ramp Entry Dressup](Path_DressupRampEntry/de.md): Fügt dem ausgewählten Pfad eine vertikale Anfahrrampe hinzu


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Tag Dressup](Path_DressupTag.md): Fügt dem ausgewählten Pfad eine Erweiterung für Haltestege zu


</div>


<div class="mw-translate-fuzzy">

### Teilbefehle


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Fixture.png  style="width:32px;"> [Vorrichtung](Path_Fixture/de.md): Ändert die Position der Vorrichtung


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Kommentar](Path_Comment/de.md): Fügt einen Kommentar in den G-Code eines Pfades ein.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Stop](Path_Stop/de.md): Fügt einen Maschinen Stop ein.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Custom](Path_Custom/de.md): Fügt benutzerdefinierten G-Code ein


</div>


<div class="mw-translate-fuzzy">

<img alt="Path_GcodeFromShape.svg" src=images/Path_GcodeFromShape.svg  style="width:32px;"> [Gcode aus einer Form](Path_Shapes.md): Erstellt ein  Pfadobjekt aus einem gewählten Part Objekt


</div>


<div class="mw-translate-fuzzy">

### Pfad Modifikation 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Kopieren](Path_Copy/de.md): Erstellt eine parametrische Kopie eines gewählten Pfadobjekts


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Anordnung](Path_Array.md): Erstellt eine Anordnung durch Duplizieren eines ausgewählten Pfades


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Einfache Kopie](Path_SimpleCopy/de.md): Erstellt eine nichtparametrische Kopie eines ausgewählten Pfadobjekts


</div>

### Miscellaneous


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Funktionsbereich](Path_Area/de.md): Erstellt einen Funktionsbereich aus gewählten Objekten


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Funktionsbereich Arbeitsebene](Path_Area_Workplane/de.md): Erstellt eine Funktionsbereich Arbeitsebene.


</div>

### Obsolete


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:32px;"> [Werkzeugverwalter](Path_ToolLibraryEdit/de.md): Den Werkzeugverwalter bearbeiten


</div>

## ToolBit architecture 

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture. <small>(v0.19)</small> 

-   [Path Tools](Path_Tools.md)
-   [Path ToolShape](Path_ToolShape.md)
-   [Path ToolBit](Path_ToolBit.md)
-   [Path ToolBit Library](Path_ToolBit_Library.md)
-   [Path ToolController](Path_ToolController.md)

## Other


<div class="mw-translate-fuzzy">

Der Pfad Arbeitsbereich teilt viele Konzepte mit anderen CAM Softwarepaketen, hat aber ihre eigenen Besonderheiten. Wenn etwas nicht stimmt, ist dies vielleicht ein guter Anfang.


</div>


<div class="mw-translate-fuzzy">

### Einstellungen


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgParameter.svg  style="width:32px;"> [Einstellungen\...](Path_Preferences.md): Einstellungen verfügbar in den Pfadwerkzeugen.


</div>

## Skripten


<div class="mw-translate-fuzzy">

Siehe [Path scripting/de](Path_scripting/de.md) Seite.


</div>

## Tutorials

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with Path.

## Videos

-   _.
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.





{{Path_Tools_navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/de
