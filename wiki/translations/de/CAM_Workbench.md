# <img alt="Symbol des Arbeitsbereichs CAM" src=images/Workbench_CAM.svg  style="width:64px;"> CAM Workbench/de






## Einleitung

Der Arbeitsbereich <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [CAM](CAM_Workbench/de.md) wird verwendet, um Maschinenanweisungen für [CNC-Maschinen](https://de.wikipedia.org/wiki/CNC-Maschine) aus einem FreeCAD-3D-Modell zu erstellen. Diese erzeugen reale 3D-Objekte auf CNC-Maschinen wie Fräsmaschinen, Drehbänken, Laserschneidern oder ähnlichen. Typischerweise handelt es sich bei den Anweisungen um einen [G-Code](https://de.wikipedia.org/wiki/Computerized_Numerical_Control#DIN/ISO-Programmierung_bzw._G-Code)-Dialekt. Hier ein allgemeines Beispiel: [Simulation einer Abfolge von Werkzeugwegen einer CNC-Drehbank](https://www.ange-softs.com/SIMULCNCHTML/index.html).

<img alt="" src=images/pathwb.png  style="width:600px;">

Der FreeCAD-Arbeitsbereich CAM erstellt diese Maschinenanweisungen mit folgendem Arbeitsablauf:

-   Ein 3D-Modell ist das Basisobjekt, das üblicherweise mit einem oder mehreren der Arbeitsbereiche <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md), <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) oder <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md) erstellt wird.
-   Ein [CAM-Auftrag](CAM_Job/de.md) wird im Arbeitsbereich CAM erstellt. Dieser enthält alle erforderlichen Informationen, die zur Erstellung des benötigten G-Codes für die Bearbeitung des Arbeitsauftrags auf einer CNC-Fräse erforderlich sind: Er listet Halbzeuge (Rohmaterial), einen bestimmten [Satz Werkzeuge](CAM_ToolBitLibraryOpen/de.md) für die Fräse und er folgt bestimmten Amweisungen, die Geschwindigkeit und Bewegungen steuern (normalerweise G-Code).
-   [CAM-Werkzeuge](CAM_Tools/de.md) werden den Anforderungen der Arbeitsabläufe entsprechend ausgewählt.
-   Fräsbahnen werden z.B. mit den Arbeitsabläufen für [Profil](CAM_Profile/de.md) und [Tasche 3D](CAM_Pocket_3D/de.md) erstellt. Diese CAM-Objekte verwenden FreeCADs internen G-code-Dialekt, unabhängig von der CNC-Maschine.
-   Den Auftrag mit einem zur Maschine passenden G-Code exportieren. Dieser Schritt wird *Post-Processing* (Nachbereitung) genannt. Es stehen mehrere Post-Prozessoren zur Verfügung.



## Allgemeine Konzepte 

Der Arbeitsbereich CAM erzeugt G-Code, der die Bewegungsbahnen (Pfade), die zum Fräsen des durch das 3D-Modell repräsentierten Projekts auf der zu verwendenden Fräse benötigt werden, in [FreeCADs G-Code-Dialekt der CAM-Job-Operations](CAM_scripting/de#FreeCADs_internes_G-Code-Format.md) festlegt, der später in den entsprechenden Dialekt für die zu verwendende CNC-Steuerung übersetzt wird, indem der passende Postprozessor ausgewählt wird.

Der G-code wird aus den in einem CAM-Auftrag enthaltenen Anweisungen und Operationen generiert. Der Arbeitsablauf des Auftrags listet diese in der Reihenfolge ihrer Ausführung auf. Die Liste wird durch Hinzufügen von CAM-Operationen, Pfadaufbereitungen, Ergänzungsbefehlen und Pfadänderungen aus dem CAM-Menü oder den GUI-Schaltflächen ausgefüllt.

Der Arbeitsbereich CAM enthält einen Werkzeugverwalter (Bibliothek, Werkzeugtabelle), eine G-Code-Überprüfung und Simulationswerkzeuge. Es verknüpft den Postprozessor und erlaubt den Im- und Export von Auftragsvorlagen.

Der Arbeitsbereich CAM besitzt externe Abhängigkeiten einschließlich:

1.  FreeCADs 3D-Modell-Einheiten sind unter **Bearbeiten → Einstellungen... → Allgemein → Sprache und Zahlenformat → Standard-Einheitensystem** festgelegt. Die Postprozessor-Konfiguration legt die endgültigen G-code-Einheiten fest.
2.  Der Pfad der Makrodatei und die geometrischen Toleranzen werden unter **Bearbeiten → Einstellungen... →  CAM → Auftagseinstellungen** definiert.
3.  Die Farben werden unter **Bearbeiten → Einstellungen... →CAM → GUI** definiert.
4.  Die Parameter der Haltestege werden unter **Bearbeiten → Einstellungen... → CAM → Aufbereitungen** definiert.
5.  Dass die Qualität des 3D-Basismodells die Anforderungen des Arbeitsbereichs CAM unterstützt, wird durch Geometrie prüfen bestätigt.



## Einschränkungen

Einige aktuelle Einschränkungen, derer man sich bewusst sein sollte, sind:

-   Die meisten der CAM-Werkzeuge sind keine echten 3D-Werkzeuge, sondern nur 2,5D fähig. Das bedeutet, dass sie eine festgelegte 2D-Form nehmen und diese bis zu einer bestimmten Tiefe herunterschneiden können. Es gibt jedoch zwei Werkzeuge, die echte 3D-Pfade erzeugen: **<img src="images/CAM_3DPocket.svg" width=24px> [3D-Tasche](CAM_Pocket_3D/de.md)** und **<img src="images/CAM_Surface.svg" width=24px> [3D-Oberfläche](CAM_Surface/de.md)** (das im November 2020 noch immer eine [experimentelle Funktion](CAM_experimental/de.md) ist).
-   Der größte Teil des Arbeitsbereichs CAM ist für eine einfache, standardmäßige 3-Achsen- (xyz) CNC-Fräse ausgelegt, aber Dreh-(maschinen-)werkzeuge sind seit 0.19_pre in Entwicklung.
-   Die meisten Operationen im Arbeitsbereich CAM geben nur Pfade zurück, die auf einem Standard-Schaftfräser-Werkzeug bzw. -Bit basieren, ohne Rücksicht auf einen, in einer bestimmten Werkzeugsteuerung zugewiesenen, Werkzeug- bzw. Bit-Typ, mit Ausnahme der Operationen **<img src="images/CAM_Engrave.svg" width=24px> [Gravur](CAM_Engrave/de.md)** und **<img src="images/CAM_Surface.svg" width=24px> [3D-Oberfläche](CAM_Surface/de.md)**.
-   Die Operationen innerhalb des Arbeitsbereichs CAM kennen keine Spannvorrichtungen, die zur Befestigung des Modells an einer Maschine verwendet werden. Überprüfe und simuliere daher die erzeugten Bahnen, bevor der Code an deine Maschine gesendet wird. Wenn nötig, eine Spannvorrichtungen in FreeCAD modellieren, um die erzeugten Bahnen besser überprüfen zu können. Auf mögliche Kollisionen mit Spannern oder anderen Hindernissen entlang der Bahnen achten.



## Einheiten

Der Umgang mit Einheiten im Arbeitsbereich CAM kann verwirrend sein. Es gibt mehrere Punkte, die verstanden werden müssen:

1.  FreeCADs Basiseinheiten für Länge und Zeit sind \'mm\' und \'s\' bzw. Geschwindigkeit ist \'mm/s\'. Diese Einheiten speichert FreeCAD intern, unabhängig von allem anderem.
2.  Das standardmäßige Einheitensystem nutzt diese Basiseinheiten. Wird das Standard-Einheitensystem benutzt und eine Vorschubgeschwindigkeit ohne Einheit eingegeben, wird sie als \'mm/s\' interpretiert.
3.  Die meisten CNC-Maschinen erwarten aber Vorschubgeschwindigkeiten in \'mm/min\' oder \'Zoll/min\'. Die meisten Postprozessoren konvertieren die Einheiten automatisch, wenn sie den Maschinencode generieren.

Schemata:

1.  Schemaänderungen in den Einstellungen ändert die Standardeinheitszeichenkette für die Eingabefelder. Wenn ein CAM-Anwender es vorzieht, metrisch zu konstruieren, wird dringend empfohlen, das Schema \"Metrische Kleinteile & CNC\" zu verwenden. Wird in US-Einheiten konstruiert, funktionieren entweder Britisches Dezimal und US-Bauwesen.
2.  Ändern des bevorzugten Einheitenschemas hat keine Auswirkung auf die Ausgabe, hilft aber, Eingabefehler zu vermeiden.

Ausgabe:

1.  Die Generierung der korrekten Einheiten in der Ausgabe liegt in der Verantwortung des Postprozessors und geschieht nur bei diesem Vorgang.
2.  Die Einheiten für die Maschine bei der Ausgabe sind komplett unabhängig von der gewählten Einheitendarstellung.
3.  Postprozessoren erzeugen entweder metrische Einheiten (G21), imperiale Einheiten (G20) oder sind konfigurierbar.
4.  Konfigurierbare Postprozessoren generieren standardmäßig metrische Einheiten (G21).
5.  Soll der konfigurierbare Postprozessor imperialen G-code (G20) ausgegeben, muss das korrekte Argument in der Job-Output-Konfiguration (d.h. \--inches for linuxcnc) eingestellt werden. Dies kann in einer Auftragsvorlage gespeichert werden und als Standardvorlage eingestellt werden, um sie für zukünftige Aufträge automatisch zu verwenden.

CAM Untersuchen:

1.  Wird das Werkzeug CAM Inspect zum Betrachten des G-codes eingesetzt, wird als Einheit \'mm/s\' angezeigt, da der Postprozessor noch nicht angewendet wurde.



## Höhen und Tiefen 

Viele der Befehle haben unterschiedliche Höhen und Tiefen:

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visuelle Referenz für Tiefeneinstellungen*



## Befehle

Einige Befehle sind experimentell und standardmäßig nicht verfügbar. Um sie zu aktivieren, siehe [CAM experimentell](CAM_experimental/de.md).



### Projektbefehle

-   <img alt="" src=images/CAM_Job.svg  style="width:32px;"> [Auftrag](CAM_Job/de.md): Erstellt einen neuen CNC-Auftrag.

-   <img alt="" src=images/CAM_Post.svg  style="width:32px;"> [Nachbereitung](CAM_Post/de.md): Exportiert ein Projekt in G-code.

-   <img alt="" src=images/CAM_Sanity.svg  style="width:32px;"> [CAM-Auftrag auf typische Fehler überprüfen](CAM_Sanity/de.md): Überprüft den ausgewählten Auftrag auf fehlende Werte.

-   <img alt="" src=images/CAM_ExportTemplate.svg  style="width:32px;"> [Exportvorlage](CAM_ExportTemplate/de.md): Exportiert den aktuellen Auftrag als Vorlage.



### Werkzeugbefehle

-   <img alt="" src=images/CAM_Inspect.svg  style="width:32px;"> [CAM-Befehle untersuchen](CAM_Inspect/de.md): Zeigt den G-code zur Überprüfung an.

-   <img alt="" src=images/CAM_Simulator.svg  style="width:32px;"> [CAM Simulator](CAM_Simulator/de.md): Zeigt die Fräsbearbeitung wie sie auf der Maschine durchgeführt wird.

-   <img alt="" src=images/CAM_SimulatorGL.svg  style="width:32px;"> [CAM SimulatorGL](CAM_SimulatorGL/de.md): Aktiviert den neuen, verbesserten CAM-Simulator. {{Version/de|1.0}}

-   <img alt="" src=images/CAM_SelectLoop.svg  style="width:32px;"> [Beenden der Auswahlschleife](CAM_SelectLoop/de.md): Vervollständigt eine Schleife aus zwei ausgewählten Kanten.

-   <img alt="" src=images/CAM_OpActive.svg  style="width:32px;"> [Umschalten des aktiven Zustands der Bearbeitung](CAM_OpActiveToggle/de.md): Aktiviert oder deaktiviert eine Pfadbearbeitung.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](CAM_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](CAM_ToolBitDock.md): Toggles the ToolBit Dock.


</div>



### Grundlegende Bearbeitungen 

-   <img alt="" src=images/CAM_Profile.svg  style="width:32px;"> [Profile](CAM_Profile/de.md): Erzeugt eine Profilbearbeitung des gesamten Modells oder von einer oder mehreren ausgewählten Flächen oder Kanten.

-   <img alt="" src=images/CAM_Pocket.svg  style="width:32px;"> [Taschenform](CAM_Pocket_Shape/de.md): Erzeugt eine Taschenbearbeitung aus einer oder mehreren ausgewählten Taschen.

-   <img alt="" src=images/CAM_Drilling.svg  style="width:32px;"> [Bohren](CAM_Drilling/de.md): Führt einen Bohrzyklus durch.

-   <img alt="" src=images/CAM_MillFace.svg  style="width:32px;"> [Fläche](CAM_MillFace/de.md): Erzeugt einen Oberflächenpfad

-   <img alt="" src=images/CAM_Helix.svg  style="width:32px;"> [Helix](CAM_Helix/de.md): Erzeugt eine wendelförmige Bahn.

-   <img alt="" src=images/CAM_Adaptive.svg  style="width:32px;"> [Adaptiv](CAM_Adaptive/de.md): Erstellt eine adaptive Räum- und Profilierungsbearbeitung.

-   <img alt="" src=images/CAM_Slot.svg  style="width:32px;"> [Nut](CAM_Slot/de.md): Erzeugt eine Nutenbearbeitung aus ausgewählten Formelementen oder benutzerdefinierten Punkten. [**Experimentell**](CAM_experimental/de.md).

-   <img alt="" src=images/CAM_Engrave.svg  style="width:32px;"> [Gravieren](CAM_Engrave/de.md): Erstellt einen Gravurpfad.

-   <img alt="" src=images/CAM_Deburr.svg  style="width:32px;"> [Entgraten](CAM_Deburr/de.md): Erstellt eine Bahn zum Entgraten.

-   <img alt="" src=images/CAM_Vcarve.svg  style="width:32px;"> [VGravur](CAM_Vcarve/de.md): Erzeugt einen Gravurpfad unter Verwendung einer V-Werkzeugform.



### 3D-Bearbeitungen 

-   <img alt="" src=images/CAM_Pocket_3D.svg  style="width:32px;"> [3D-Tasche](CAM_Pocket_3D/de.md): Erzeugt einen Pfad für eine 3D-Tasche.

-   <img alt="" src=images/CAM_Surface.svg  style="width:32px;"> [3D Oberfläche](CAM_Surface/de.md): Erstellt einen Pfad für eine 3D-Oberfläche. [**Experimentell**](CAM_experimental/de.md).

-   <img alt="" src=images/CAM_Waterline.svg  style="width:32px;"> [Wasserlinie](CAM_Waterline/de.md): Erzeugt einen Wasserlinienpfad für eine 3D-Oberfläche. [**Experimentell**](CAM_experimental/de.md).



### Pfadaufbereitung


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupAxisMap.svg  style="width:32px;"> [Axis Map](CAM_DressupAxisMap.md): Remaps one axis to another.


</div>

-   <img alt="" src=images/CAM_DressupPathBoundary.svg  style="width:32px;"> [Begrenzung](CAM_DressupPathBoundary/de.md): Fügt eine Randaufbereitungsänderung einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/CAM_DressupDogbone.svg  style="width:32px;"> [Hundeknochen](CAM_DressupDogbone/de.md): Fügt eine Hundeknochen-Aufbereitungsänderung einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/CAM_DressupDragKnife.svg  style="width:32px;"> [Schleppmesser](CAM_DressupDragKnife/de.md): Fügt eine Schleppmesser-Aufbereitungsänderung einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/CAM_DressupLeadInOut.svg  style="width:32px;"> [An/Abfahren](CAM_DressupLeadInOut/de.md): Fügt einen Anfahr- und/oder Abfahrpunkt einem ausgewählten Pfad hinzu.

-   <img alt="" src=images/CAM_DressupRampEntry.svg  style="width:32px;"> [Eingangsrampe](CAM_DressupRampEntry/de.md): Fügt dem ausgewählten Pfad eine vertikale Anfahrrampe hinzu.

-   <img alt="" src=images/CAM_DressupTag.svg  style="width:32px;"> [Haltesteg](CAM_DressupTag/de.md): Fügt dem ausgewählten Pfad eine Erweiterung für Haltestege zu.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupZCorrect.svg  style="width:32px;"> [Z Depth Correction](CAM_DressupZCorrect.md): Corrects the Z depth using Probe Map.


</div>



### Ergänzende Befehle 

-   <img alt="" src=images/CAM_Fixture.svg  style="width:32px;"> [Vorrichtung](CAM_Fixture/de.md): Ändert die Position der Vorrichtung.

-   <img alt="" src=images/CAM_Comment.svg  style="width:32px;"> [Kommentar](CAM_Comment/de.md): Fügt einen Kommentar in den G-Code eines Pfades ein.

-   <img alt="" src=images/CAM_Stop.svg  style="width:32px;"> [Halt](CAM_Stop/de.md): Fügt einen Halt der Maschine ein.

-   <img alt="" src=images/CAM_Custom.svg  style="width:32px;"> [Benutzerdefiniert](CAM_Custom/de.md): Fügt benutzerdefinierten G-Code ein.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Probe.svg  style="width:32px;"> [Probe](CAM_Probe.md): Creates a Probing Grid from a job stock.


</div>

-   <img alt="" src=images/CAM_Shape.svg  style="width:32px;"> [Aus Form](CAM_Shape/de.md): Erstellt ein Pfadobjekt aus einem gewählten Part Objekt. [**Experimentell**](CAM_experimental/de.md).



### Pfadänderung

-   <img alt="" src=images/CAM_Copy.svg  style="width:32px;"> [Kopieren der Bearbeitung im Auftrag](CAM_Copy/de.md): Erstellt eine parametrische Kopie eines gewählten Pfadobjekts.

-   <img alt="" src=images/CAM_Array.svg  style="width:32px;"> [Anordnung](CAM_Array.md): Erstellt eine Anordnung durch Duplizieren eines ausgewählten Pfades.

-   <img alt="" src=images/CAM_SimpleCopy.svg  style="width:32px;"> [Einfache Kopie](CAM_SimpleCopy/de.md): Erstellt eine nichtparametrische Kopie eines ausgewählten Pfadobjekts.


<div lang="en" dir="ltr" class="mw-content-ltr">

### Specialty Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ThreadMilling.svg  style="width:32px;"> [Thread Milling](CAM_ThreadMilling.md): Creates a CAM Thread Milling operation from features of a base object. [**Experimental**](CAM_experimental.md).


</div>



### Sonstiges

-   <img alt="" src=images/CAM_Area.svg  style="width:32px;"> [Bereich](CAM_Area/de.md): Erstellt einen Formelementbereich aus gewählten Objekten. [**Experimentell**](CAM_experimental/de.md).

-   <img alt="" src=images/CAM_Area_Workplane.svg  style="width:32px;"> [Bereich Arbeitsebene](CAM_Area_Workplane/de.md): Erstellt eine Formelementbereich Arbeitsebene. [**Experimentell**](CAM_experimental/de.md).



## ToolBit Architektur 

Verwalte Werkzeuge, Bits und die Werkzeugbibliothek. Basiert auf der ToolBit Architektur.

-   [CAM Werkzeuge](CAM_Tools/de.md)
-   [CAM WerkzeugForm](CAM_ToolShape/de.md)
-   [CAM WerkzeugBit](CAM_ToolBit/de.md)
-   [CAM WerkzeugBit Bibliothek](CAM_ToolBit_Library/de.md)
-   [CAM WerkzeugController](CAM_ToolController/de.md)



## Andere

-   [CAM HäufigGestellteFragen](CAM_FAQ/de.md): Der Arbeitsbereich CAM teilt viele Konzepte mit anderen CAM-Softwarepaketen, hat aber seine eigenen Besonderheiten. Wenn etwas nicht stimmt, ist dies vielleicht ein guter Anfang.
-   [CAM SetupSheet](CAM_SetupSheet/de.md): Es kann ein SetupSheet verwendet werden zum Anpassen, wie die Werte verschiedener Eigenschaften von Operationen berechnet werden.
-   [CAM Postprozessor Anpassung](CAM_Postprocessor_Customization/de.md): Hast Du eine spezielle Maschine, die die Daten der vorhandenen Postprozessoren nicht verwenden kann, musst Du eventuell deinen eigenen Postprozessoren schreiben.
-   [CAM VierteAchse](CAM_fourth_axis/de.md): Experimentelles Vier-Achs-Fräsen.



## Einstellungen

-   <img alt="" src=images/Preferences-cam.svg  style="width:32px;"> [Einstellungen\...](CAM_Preferences.md): Verfügbare Einstellungen für den Arbeitsbereich CAM.



## Skripten

Siehe [CAM Skripten](CAM_scripting/de.md).



## Anleitungen


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Walkthrough for the Impatient](CAM_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with CAM.


</div>

## Videos


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): A playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [CAM Workbench](CAM_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): A playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ): A playlist with a series of 8 videos in English by CAD CAM Lessons.
-   Also see the [Computer-Aided Manufacturing (CAM) section](Video_tutorials#Computer-Aided_Manufacturing_(CAM).md) of the [Video tutorials](Video_tutorials.md) wiki page.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Roadmap


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Development Roadmap](CAM_Development_Roadmap.md): Read this if you are a developer and want to contribute to CAM.


</div>





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [CAM](Category_CAM.md) > CAM Workbench/de
