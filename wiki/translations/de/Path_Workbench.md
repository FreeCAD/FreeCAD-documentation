# <img alt="Symbol des Arbeitsbereichs Path" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/de






## Einleitung

Der Arbeitsbereich <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Path](Path_Workbench/de.md) wird verwendet, um Maschinenanweisungen für [CNC-Maschinen](https://en.wikipedia.org/wiki/CNC_router) aus einem FreeCAD-3D-Modell zu erstellen. Diese erzeugen reale 3D-Objekte auf CNC-Maschinen wie Fräsmaschinen, Drehbänken, Laserschneidern oder ähnlichen. Typischerweise handelt es sich bei den Anweisungen um einen [G-Code](https://en.wikipedia.org/wiki/G-code)-Dialekt. Hier wird ein [allgemeines Beispiel für die Ablaufsimulation eines Werkzeugpfades einer CNC-Drehbank](https://www.ange-softs.com/SIMULCNCHTML/index.html) vorgestellt.

<img alt="" src=images/pathwb.png  style="width:600px;">

Der FreeCAD-Arbeitsbereich Path erstellt diese Maschinenanweisungen mit folgendem Arbeitsablauf:

-   Ein 3D-Modell ist das Basisobjekt, das typischerweise mit einem oder mehreren der Arbeitsbereiche <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design](PartDesign_Workbench/de.md), <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) oder <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md) erstellt wird.
-   Ein [Path Auftrag](Path_Job/de.md) wird im Arbeitsbereich Path erstellt. Dieser enthält alle Informationen, die zur Erzeugung des notwendigen G-Codes für die Bearbeitung des Arbeitsauftrags auf einer CNC-Fräse erforderlich sind: Es gibt Rohmaterial, die Fräse hat einen bestimmten [Werkzeugsatz](Path_ToolLibraryEdit/de.md) und sie folgt bestimmten Befehlen, die die Geschwindigkeit und die Bewegungen steuern (normalerweise G-Code).
-   [Path Werkzeuge](Path_Tools/de.md) werden den Anforderungen der Arbeitsauftragsabläufe entsprechend ausgewählt.
-   Fräsbahnen werden erzstellt, z.B. mit den Abläufen [Kontur](Path_Profile/de.md) und [Tasche](Path_Pocket_3D/de.md). Diese Bahnobjekte verwenden FreeCADs internen G-code-Dialekt, unabhängig von der CNC-Maschine.
-   Den Auftrag mit einem zur Maschine passenden G-Code exportieren. Dieser Schritt wird *Post-Processing* (Nachbereitung) genannt. Es stehen mehrere Post-Prozessoren zur Verfügung.



## Allgemeine Konzepte 

Der Arbeitsbereich Path erzeugt G-Code, der die Bewegungsbahnen (Pfade), die zum Fräsen des durch das 3D-Modell repräsentierten Projekts auf der Zielfräse benötigt werden, in [FreeCADs G-Code-Dialekt](Path_scripting/de#FreeCADs_internes_G-Code-Format.md) festlegt, der später in den entsprechenden Dialekt für die Ziel-CNC-Steuerung übersetzt wird, indem der passende Postprozessor ausgewählt wird.

Der G-code wird aus den in einem Pfadauftrag enthaltenen Anweisungen und Operationen generiert. Der Arbeitsablauf des Auftrags listet diese in der Reihenfolge ihrer Ausführung auf. Die Liste wird durch Hinzufügen von Pfadoperationen, Pfadaufbereitungen, Pfadergänzungsbefehlen und Pfadänderungen aus dem Pfadmenü oder den GUI-Schaltflächen ausgefüllt.

Der Arbeitsbereich Path enthält einen Werkzeugverwalter (Bibliothek, Werkzeugtabelle), eine G-Code-Überprüfung und Simulationswerkzeuge. Es verknüpft den Postprozessor und erlaubt den Im- und Export von Auftragsvorlagen.

Der Pfad Arbeitsbereich hat externe Abhängigkeiten einschließlich:

1.  Die FreeCAD 3D Modell Einheiten sind im **Bearbeiten → Einstellungen → Allgemein → Einheiten Reiter Einheiteneinstellungen** festgelegt. Die Postprozessor Konfiguration legt die endgültigen G-code Einheiten fest.
2.  Der Pfad der Makrodatei und die geometrischen Toleranzen werden im **Bearbeiten → Einstellungen →  Pfad → Arbeitsauftag Einstellungen** definiert.
3.  Die Farben werden im Register **Bearbeiten → Einstellungen →Pfad → Pfad  Farben** definiert.
4.  Die Parameter der Halte Merker werden in dem **Bearbeiten → Einstellungen → Pfad → Aufbereitungen** Reiter definiert.
5.  Dass die Qualität des Basis 3D Modells die Anforderungen an die Pfad Arbeitsbereich unterstützt, wird durch Prüfe Geometrie bestätigt.



## Einschränkungen

Einige aktuelle Einschränkungen, derer du dir bewusst sein solltest, sind:

-   Die meisten der Pfadwerkzeuge sind keine echten 3D-Werkzeuge, sondern nur 2,5D fähig. Das bedeutet, dass sie eine festgelegte 2D-Form nehmen und diese bis zu einer bestimmten Tiefe herunterschneiden können. Es gibt jedoch zwei Werkzeuge, die echte 3D-Pfade erzeugen: **<img src="images/Path_3DPocket.svg" width=24px> [3D-Tasche](Path_Pocket_3D/de.md)** und **<img src="images/Path_Surface.svg" width=24px> [3D-Oberfläche](Path_Surface/de.md)** (die im November 2020 noch immer [experimentelle Funktionen](Path_experimental/de.md) sind).
-   Der größte Teil des Arbeitsbereichs Pfad ist für eine einfache, standardmäßige 3-Achsen- (xyz) CNC-Fräse ausgelegt, aber Dreh-(maschinen-)werkzeuge sind seit 0.19_pre in Entwicklung.
-   Die meisten Operationen im Arbeitsbereich Pfad geben nur Pfade zurück, die auf einem Standard-Schaftfräser-Werkzeug bzw. -Bit basieren, ohne Rücksicht auf einen, in einer bestimmten Werkzeugsteuerung zugewiesenen, Werkzeug- bzw. Bit-Typ, mit Ausnahme der Operationen **<img src="images/Path_Engrave.svg" width=24px> [Gravur](Path_Engrave/de.md)** und **<img src="images/Path_Surface.svg" width=24px> [3D-Oberfläche](Path_Surface/de.md)**.
-   Die Operationen innerhalb des Arbeitsbereichs Pfad kennen keine Spannvorrichtungen, die zur Befestigung des Modells an einer Maschine verwendet werden. Überprüfe und simuliere daher die erzeugten Bahnen, bevor du den Code an deine Maschine sendest. Wenn nötig, modelliere deine Spannvorrichtungen in FreeCAD, um die erzeugten Bahnen besser überprüfen zu können. Achte auf mögliche Kollisionen mit Spannern oder anderen Hindernissen entlang der Bahnen.



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
*Visuelle Referenz für Tiefeneinstellungen*



## Befehle

Einige Befehle sind experimentell und standardmäßig nicht verfügbar. Um sie zu aktivieren, siehe [Pfad experimentell](Path_experimental/de.md).



### Projektbefehle

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Auftrag](Path_Job/de.md): Erstellt einen neuen CNC Auftrag.

-   <img alt="" src=images/Path_PostProcess.svg  style="width:32px;"> [Nach Prozess](Path_Post/de.md): Exportiert ein Projekt in G-code.

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> [Path-Auftrag auf typische Fehler überprüfen](Path_Sanity/de.md): Überprüft den ausgewählten Auftrag auf fehlende Werte.

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Export Vorlage](Path_ExportTemplate/de.md): Den aktuellen Auftrag als Vorlage exportieren.



### Werkzeugbefehle

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [Path-Befehle untersuchen](Path_Inspect/de.md): Zeigt den G-code zur Überprüfung an.

-   <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [CAM Simulator](Path_Simulator/de.md): Zeigt die Fräsbearbeitung wie sie auf der Maschine durchgeführt wird.

-   <img alt="" src=images/Path_SelectLoop.svg  style="width:32px;"> [Beenden der Auswahlschleife](Path_SelectLoop/de.md): Vervollständigt eine Schleife aus zwei ausgewählten Kanten.

-   <img alt="" src=images/Path_OpActive.svg  style="width:32px;"> [Umschalten des aktiven Zustands der Bearbeitung](Path_OpActiveToggle/de.md): Aktiviert oder deaktiviert eine Pfadbearbeitung.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries.

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock.



### Grundlegende Bearbeitungen 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile/de.md): Erzeugt eine Profilbearbeitung des gesamten Modells oder von einer oder mehreren ausgewählten Flächen oder Kanten.

-   <img alt="" src=images/Path_Pocket.svg  style="width:32px;"> [Taschenform](Path_Pocket_Shape/de.md): Erzeugt eine Taschenbearbeitung aus einer oder mehreren ausgewählten Taschen.

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Bohren](Path_Drilling/de.md): Führt einen Bohrzyklus durch.

-   <img alt="" src=images/Path_MillFace.svg  style="width:32px;"> [Fläche](Path_MillFace/de.md): Erzeugt einen Oberflächenpfad

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Helix](Path_Helix/de.md): Erzeugt eine spiralförmige Bahn.

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptiv](Path_Adaptive/de.md): Erstellt eine adaptive Räum- und Profilierungsbearbeitung.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Nut](Path_Slot/de.md): Erzeugt eine Nutenbearbeitung aus ausgewählten Formelementen oder benutzerdefinierten Punkten. [**Experimentell**](Path_experimental/de.md).

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Gravieren](Path_Engrave/de.md): Erstellt einen Gravurpfad.

-   <img alt="" src=images/Path_Deburr.svg  style="width:32px;"> [Deburr](Path_Deburr.md): Creates a deburr path.

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [VGravur](Path_Vcarve/de.md): Erzeugt einen Gravurpfad unter Verwendung einer V-Werkzeugform.



### 3D-Bearbeitungen 

-   <img alt="" src=images/Path_Pocket_3D.svg  style="width:32px;"> [3D-Tasche](Path_Pocket_3D/de.md): Erzeugt einen Pfad für eine 3D-Tasche.

-   <img alt="" src=images/Path_Surface.svg  style="width:32px;"> [3D Oberfläche](Path_Surface/de.md): Erstellt einen Pfad für eine 3D-Oberfläche. [**Experimentell**](Path_experimental/de.md).

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Wasserlinie](Path_Waterline/de.md): Erzeugt einen Wasserlinienpfad für eine 3D-Oberfläche. [**Experimentell**](Path_experimental/de.md).



### Pfad Aufbereitung 

-   <img alt="" src=images/Path_DressupAxisMap.svg  style="width:32px;"> [Axis Map](Path_DressupAxisMap.md): Remaps one axis to another.

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Begrenzung](Path_DressupPathBoundary/de.md): Fügt eine Randaufbereitungsänderung einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/Path_DressupDogbone.svg  style="width:32px;"> [Hundeknochen](Path_DressupDogbone/de.md): Fügt eine Hundeknochen-Aufbereitungsänderung einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [Schleppmesser](Path_DressupDragKnife/de.md): Fügt eine Schleppmesser-Aufbereitungsänderung einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [An/Abfahren](Path_DressupLeadInOut/de.md): Fügt einen Anfahr- und/oder Abfahrpunkt einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [Eingangsrampe](Path_DressupRampEntry/de.md): Fügt dem ausgewählten Pfad eine vertikale Anfahrrampe hinzu.

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Haltesteg](Path_DressupTag/de.md): Fügt dem ausgewählten Pfad eine Erweiterung für Haltestege zu.

-   <img alt="" src=images/Path_DressupZCorrect.svg  style="width:32px;"> [Z Depth Correction](Path_DressupZCorrect.md): Corrects the Z depth using Probe Map.



### Ergänzende Befehle 

-   <img alt="" src=images/Path_Fixture.png  style="width:32px;"> [Vorrichtung](Path_Fixture/de.md): Ändert die Position der Vorrichtung.

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Kommentar](Path_Comment/de.md): Fügt einen Kommentar in den G-Code eines Pfades ein.

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Halt](Path_Stop/de.md): Fügt einen Halt der Maschine ein.

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Benutzerdefiniert](Path_Custom/de.md): Fügt benutzerdefinierten G-Code ein.

-   <img alt="" src=images/Path_Probe.svg  style="width:32px;"> [Probe](Path_Probe.md): Creates a Probing Grid from a job stock.

<img alt="Path_GcodeFromShape.svg" src=images/Path_GcodeFromShape.svg  style="width:32px;"> [Aus Form](Path_Shape/de.md): Erstellt ein  Pfadobjekt aus einem gewählten Part Objekt. [**Experimentell**](Path_experimental/de.md).



### Pfadänderungen

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Kopieren der Bearbeitung im Auftrag](Path_Copy/de.md): Erstellt eine parametrische Kopie eines gewählten Pfadobjekts.

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Anordnung](Path_Array.md): Erstellt eine Anordnung durch Duplizieren eines ausgewählten Pfades.

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Einfache Kopie](Path_SimpleCopy/de.md): Erstellt eine nichtparametrische Kopie eines ausgewählten Pfadobjekts.

### Specialty Operations 

-   <img alt="" src=images/Path_ThreadMilling.svg  style="width:32px;"> [Thread Milling](Path_ThreadMilling.md): Creates a Path Thread Milling operation from features of a base object. [**Experimental**](Path_experimental.md).



### Sonstiges

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Bereich](Path_Area/de.md): Erstellt einen Formelementbereich aus gewählten Objekten. [**Experimentell**](Path_experimental/de.md).

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Bereich Arbeitsebene](Path_Area_Workplane/de.md): Erstellt eine Formelementbereich Arbeitsebene. [**Experimentell**](Path_experimental/de.md).



### Veraltet

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:32px;"> [Werkzeugverwalter](Path_ToolLibraryEdit/de.md): Bearbeiten des Werkzeugverwalters. \'Altes\' Werkzeugsystem. {{VersionMinus/de|0.18}}



## ToolBit Architektur 

Verwalte Werkzeuge, Bits und die Werkzeugbibliothek. Basiert auf der ToolBit Architektur.

-   [Pfad Werkzeuge](Path_Tools/de.md)
-   [Pfad WerkzeugForm](Path_ToolShape/de.md)
-   [Pfad WerkzeugBit](Path_ToolBit/de.md)
-   [Pfad WerkzeugBit Bibliothek](Path_ToolBit_Library/de.md)
-   [Pfad WerkzeugController](Path_ToolController/de.md)



## Andere

-   [Path HäufigGestellteFragen](Path_FAQ/de.md): Der Arbeitsbereich Pfad teilt viele Konzepte mit anderen CAM-Softwarepaketen, hat aber seine eigenen Besonderheiten. Wenn etwas nicht stimmt, ist dies vielleicht ein guter Anfang.
-   [Path SetupSheet](Path_SetupSheet/de.md): Es kann ein SetupSheet verwendet werden zum Anpassen, wie die Werte verschiedener Eigenschaften von Operationen berechnet werden. to customize how various property values for operations are calculated.
-   [Path Postprozessor Anpassung](Path_Postprocessor_Customization/de.md): Hast Du eine spezielle Maschine, die die Daten der vorhandenen Postprozessoren nicht verwenden kann, musst Du eventuell deinen eigenen Postprozessoren schreiben.
-   [Path VierteAchse](Path_fourth_axis/de.md): Experimentelles Vier-Achs-Fräsen.



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
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/de
