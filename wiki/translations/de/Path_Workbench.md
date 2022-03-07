# <img alt="Pfad Arbeitsbereichssymbol" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/de


{{TOCright}}

## Einführung

Der <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Arbeitsbereich Path](Path_Workbench/de.md) wird verwendet, um Maschinenanweisungen für [CNC Maschinen](https://en.wikipedia.org/wiki/CNC_router) aus einem FreeCAD 3D Modell zu erstellen. Diese erzeugen reale 3D Objekte auf CNC Maschinen wie Fräsmaschinen, Drehbänken, Laserschneidern oder ähnlichem. Typischerweise handelt es sich bei den Anweisungen um einen [G-code](https://en.wikipedia.org/wiki/G-code) Dialekt. Hier wird ein [allgemeines Beispiel für die Simulation einer CNC Drehbank Werkzeugpfadfolge](https://www.ange-softs.com/SIMULCNCHTML/index.html) vorgestellt.

<img alt="" src=images/pathwb.png  style="width:600px;">

Der FreeCAD Arbeitsbereich Path erstellt diese Maschinenanweisungen mit folgendem Arbeitsablauf:

-   Ein 3D Modell ist das Basisobjekt, das typischerweise mit einer oder mehreren der Arbeitsbereiche <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design](PartDesign_Workbench/de.md), <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) oder <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md) erstellt wird.
-   Ein [Path Auftrag](Path_Job/de.md) wird im Arbeitsbereich Path erstellt. Dieser enthält alle Informationen, die zur Erzeugung des notwendigen G-codes für die Bearbeitung des Arbeitsauftrags auf einer CNC Fräse erforderlich sind: es gibt Rohmaterial, die Fräse hat einen bestimmten [Werkzeugsatz](Path_ToolLibraryEdit/de.md) und es folgen bestimmte Befehle, die die Geschwindigkeit und die Bewegungen steuern (normalerweise G-code).
-   Die Werkzeuge werden entsprechend den Anforderungen der Arbeitsauftragsabläufe ausgewählt.
-   Fräsbahnen werden z.B. mit [Kontur](Path_Profile/de.md) und [Tasche](Path_Pocket_3D/de.md) Abläufen erzeugt. Diese Bahnobjekte verwenden den internen FreeCAD G-code Dialekt, unabhängig von der CNC Maschine.
-   Der [Path Auftrag](Path_Job/de.md) wird mit einem Post Processor als G-code exportiert. Der eingesetzte Post Processor muss zur verwendeten Maschine passen, da dieser den FreeCAD intern verwendeten G-code in den \"Dialekt\" der Maschine übersetzt.

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


<div class="mw-translate-fuzzy">

Einige aktuelle Begrenzungen, derer du dir bewusst sein solltest, sind:

-   Die meisten der Pfadwerkzeuge sind keine echten 3D Werkzeuge, sondern nur 2,5D fähig. Das bedeutet, dass sie eine festgelegte 2D Form nehmen und diese bis zu einer bestimmten Tiefe herunterschneiden können. Es gibt jedoch zwei Werkzeuge, die echte 3D Pfade erzeugen: **<img src="images/Path_3DPocket.svg" width=24px> [3D Tasche](Path_Pocket_3D/de.md)** und **<img src="images/Path_Surface.svg" width=24px> [3D Oberfläche](Path_Surface/de.md)** (was ab November 2020 noch ein [experimentelle Funktion](Path_experimental/de.md) ist).
-   Der größte Teil des Pfad Arbeitsbereichs ist für eine einfache, standardmäßige 3-Achsen (xyz) CNC Fräse/Router ausgelegt, aber Drehwerkzeuge sind in 0.19\_pre in Entwicklung.
-   Die meisten Operationen im Pfad Arbeitsbereich geben nur Pfade zurück, die auf einem Standard Endfräser Werkzeug/Bit basieren, unabhängig vom zugewiesenen Werkzeug/Bit Typ in einer bestimmten Werkzeugsteuerung, mit Ausnahme der **<img src="images/Path_Engrave.svg" width=24px> [Gravur](Path_Engrave/de.md)** und **<img src="images/Path_Surface.svg" width=24px> [3D Oberfläche](Path_Surface/de.md)** Operationen.
-   Die Operationen innerhalb des Pfad Arbeitsbereichs kennen keine Spannmechanismen, die zur Befestigung des Modells an deiner Maschine verwendet werden. Überprüfe und simuliere daher die von dir erzeugten Bahnen, bevor du den Code an deine Maschine sendest. Wenn nötig, modelliere deine Spannmechanismen in FreeCAD, um die erzeugten Bahnen besser überprüfen zu können. Achte auf mögliche Kollisionen mit Spannern oder anderen Hindernissen entlang der Bahnen.


</div>

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

Einige Befehle sind experimentell und standardmäßig nicht verfügbar. Um sie zu aktivieren, siehe [Pfad experimentell](Path_experimental/de.md).

### Projektbefehle

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Auftrag](Path_Job/de.md): Erstellt einen neuen CNC Auftrag.

-   <img alt="" src=images/Path_PostProcess.svg  style="width:32px;"> [Nach Prozess](Path_Post/de.md): Exportiert ein Projekt in G-code.

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> [Überprüfen des Pfadauftrags auf allgemeine Fehler](Path_Sanity/de.md): Überprüft den gewählten Auftrag auf fehlende Werte. [/de**Experimentell**](Path_experimental.md). {{Version/de|0.19}}

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Export Vorlage](Path_ExportTemplate/de.md): Den aktuellen Auftrag als Vorlage exportieren.

### Werkzeugbefehle

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [G-Code untersuchen](Path_Inspect/de.md): Zeigt den G-code zur Überprüfung.

-   <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [CAM Simulator](Path_Simulator/de.md): Zeigt die Fräsbearbeitung wie sie auf der Maschine durchgeführt wird.

-   <img alt="" src=images/Path_SelectLoop.svg  style="width:32px;"> [Beenden der Auswahlschleife](Path_SelectLoop/de.md): Vervollständigt eine Schleife aus zwei ausgewählten Kanten.

-   <img alt="" src=images/Path_OpActive.svg  style="width:32px;"> [Umschalten des aktiven Zustands der Bearbeitung](Path_OpActiveToggle/de.md): Aktiviert oder deaktiviert eine Pfadbearbeitung.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock. <small>(v0.19)</small> 

### Grundlegende Bearbeitungen 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile/de.md): Erzeugt eine Profilbearbeitung des gesamten Modells oder von einer oder mehreren ausgewählten Flächen oder Kanten. {{Version/de|0.19}}

-   <img alt="" src=images/Path_Pocket.svg  style="width:32px;"> [Taschenform](Path_Pocket_Shape/de.md): Erzeugt eine Taschenbearbeitung aus einer oder mehreren ausgewählten Taschen.

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Bohren](Path_Drilling/de.md): Führt einen Bohrzyklus durch.

-   <img alt="" src=images/Path_Face.svg  style="width:32px;"> [Fläche](Path_MillFace/de.md): Erzeugt einen Oberflächenpfad

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Helix](Path_Helix/de.md): Erzeugt eine spiralförmige Bahn.

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptiv](Path_Adaptive/de.md): Erstellt eine adaptive Räum- und Profilierungsbearbeitung.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Nut](Path_Slot/de.md): Erzeugt eine Nutenbearbeitung aus ausgewählten Formelementen oder benutzerdefinierten Punkten. [**Experimentell**](Path_experimental/de.md). {{Version/de|0.19}}

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Gravieren](Path_Engrave/de.md): Erstellt einen Gravurpfad.

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [VGravur](Path_Vcarve/de.md): Erzeugt einen Gravurpfad unter Verwendung einer V-Werkzeugform. {{Version/de|0.19}}

### 3D Bearbeitungen 

-   <img alt="" src=images/Path_3DPocket.svg  style="width:32px;"> [3D Tasche](Path_Pocket_3D/de.md): Erzeugt einen Pfad für eine 3D Tasche.

-   <img alt="" src=images/Path_Surface.svg  style="width:32px;"> [3D Oberfläche](Path_Surface/de.md): Erstellt einen Pfad für eine 3D Oberfläche. [**Experimentell**](Path_experimental/de.md). {{Version/de|0.19}}

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Wasserlinie](Path_Waterline/de.md): Erzeugt einen Wasserlinienpfad für eine 3D Oberfläche. [**Experimentell**](Path_experimental/de.md). {{Version/de|0.19}}

### Pfad Aufbereitung 

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Randaufbereitung](Path_DressupPathBoundary/de.md): Fügt eine Randaufbereitungsänderung einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/Path_DressupDogbone.svg  style="width:32px;"> [Hundeknochen Aufbereitung](Path_DressupDogbone/de.md): Fügt eine Hundeknochen Aufbereitungsänderung einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [Ziehmesser Aufbereitung](Path_DressupDragKnife/de.md): Fügt eine Ziehmesser Aufbereitungsänderung einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [EinAusAusführung Aufbereitung](Path_DressupLeadInOut/de.md): Fügt einen Einführungs- und/oder Ausführungspunkt einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [Anfahrrampen Aufbereitung](Path_DressupRampEntry/de.md): Fügt dem ausgewählten Pfad eine vertikale Anfahrrampe hinzu.

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Tag Aufbereitung](Path_DressupTag/de.md): Fügt dem ausgewählten Pfad eine Erweiterung für Haltestege zu.

### Ergänzende Befehle 

-   <img alt="" src=images/Path_Fixture.png  style="width:32px;"> [Vorrichtung](Path_Fixture/de.md): Ändert die Position der Vorrichtung.

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Kommentar](Path_Comment/de.md): Fügt einen Kommentar in den G-Code eines Pfades ein.

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Halt](Path_Stop/de.md): Fügt einen Halt der Maschine ein.

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Benutzerdefiniert](Path_Custom/de.md): Fügt benutzerdefinierten G-Code ein.

<img alt="Path_GcodeFromShape.svg" src=images/Path_GcodeFromShape.svg  style="width:32px;"> [Aus Form](Path_Shape/de.md): Erstellt ein  Pfadobjekt aus einem gewählten Part Objekt. [**Experimentell**](Path_experimental/de.md).

### Pfadänderungen

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Kopieren der Bearbeitung im Auftrag](Path_Copy/de.md): Erstellt eine parametrische Kopie eines gewählten Pfadobjekts.

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Anordnung](Path_Array.md): Erstellt eine Anordnung durch Duplizieren eines ausgewählten Pfades.

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Einfache Kopie](Path_SimpleCopy/de.md): Erstellt eine nichtparametrische Kopie eines ausgewählten Pfadobjekts.

### Sonstiges

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Bereich](Path_Area/de.md): Erstellt einen Formelementbereich aus gewählten Objekten. [**Experimentell**](Path_experimental/de.md).

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Bereich Arbeitsebene](Path_Area_Workplane/de.md): Erstellt eine Formelementbereich Arbeitsebene. [**Experimentell**](Path_experimental/de.md).

### Veraltet

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:32px;"> [Werkzeugverwalter](Path_ToolLibraryEdit/de.md): Bearbeiten des Werkzeugverwalters. \'Altes\' Werkzeugsystem. {{VersionMinus/de|0.18}}

## ToolBit Architektur 

Verwalte Werkzeuge, Bits und die Werkzeugbibliothek. Basiert auf der ToolBit Architektur. {{Version/de|0.19}}

-   [Pfad Werkzeuge](Path_Tools/de.md)
-   [Pfad WerkzeugForm](Path_ToolShape/de.md)
-   [Pfad WerkzeugBit](Path_ToolBit/de.md)
-   [Pfad WerkzeugBit Bibliothek](Path_ToolBit_Library/de.md)
-   [Pfad WerkzeugController](Path_ToolController/de.md)

## Andere


<div class="mw-translate-fuzzy">

Der Pfad Arbeitsbereich teilt viele Konzepte mit anderen CAM Softwarepaketen, hat aber ihre eigenen Besonderheiten. Wenn etwas nicht stimmt, ist dies vielleicht ein guter Anfang.


</div>

## Einstellungen

-   <img alt="" src=images/Std_DlgParameter.svg  style="width:32px;"> [Einstellungen\...](Path_Preferences/de.md): Einstellungen verfügbar für den Pfad Arbeitsbereich.

## Skripten

Siehe [Pfad Skripten](Path_scripting/de.md).

## Tutorien

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with Path.

## Videos

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): a playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [Path Workbench](Path_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.

## Roadmap

-   [Path Development Roadmap](Path_Development_Roadmap.md): Read this if you are a developer and want to contribute to Path.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/de
