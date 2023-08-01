---
- TutorialInfo:/de
   Topic:Pfad Arbeitsbereich
   Level:Anfänger/Mittelmäßig
   Time:15 Minuten
   Author:Chrisb
   FCVersion:0.19
   Files:
---

# Path Walkthrough for the Impatient/de







## Ziel

Veranschaulichen der Erstellung eines <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> [Pfad Arbeitsbereich](Path_Workbench/de.md) Auftrags, abgeleitet von einem 3D Modell. Anschließend wird dialekt-richtiger G-Code für eine Ziel CNC Fräse erzeugt.



## Das 3D Modell 

1\. Das Projekt startet mit einem einfachen FreeCAD Modell entworfen im <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Part Design](PartDesign_Workbench/de.md) ein Würfel mit einer rechteckigen Tasche.

:   ![](images/Path-SquarePocketModel.png )



*Oben: Erstellt in der <img src="images/Workbench_PartDesign.svg" width=24px> 
 [Part Design](PartDesign_Workbench/de.md) einschließlich eines Körpers, eines Kastens mit einer Tasche, basierend auf einer in der  **![](images/)* XY Ebene**

orientierten Skizze.

2\. Ist das 3D-Modell fertiggestellt, wird mit der [Arbeitsbereichsauswahl](Std_Workbench/de.md) (Ausklappmenü) zum Arbeitsbereich <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> [Path](Path_Workbench/de.md) gewechselt.


<div class="mw-translate-fuzzy">

## Der Auftrag 

Der <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Auftrag](Path_Job/de.md) wird erstellt.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-JobCreationDialog.png )


</div>


<div class="mw-translate-fuzzy">

Klicke im Dialogfeld Auftragserstellung auf OK, um den Körper als Basismodell ohne Vorlage zu akzeptieren.


</div>



### Auftragseinrichtung


<div class="mw-translate-fuzzy">

Das Auftragsbearbeitungsfenster öffnet sich im Aufgabenfenster, und das Modellansichtsfenster zeigt das Material als einen Drahtgitterwürfel, der den Grundkörper umgibt. Der Einrichtungsreiter ist ausgewählt.


</div>



### Auftragsausgabe


<div class="mw-translate-fuzzy">

Der Ausgabereiter legt den Pfad, den Namen und die Erweiterung der Ausgabedatei sowie den Postprozessor fest. Für fortgeschrittene Benutzer können Postprozessor Argumente festgelegt werden - die Maus über den Hinweisen zeigt allgemeine Argumente an.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-JobOutput.png )


</div>



### Auftragswerkzeuge


<div class="mw-translate-fuzzy">

![](images/Path-JobTools.png )


</div>


<div class="mw-translate-fuzzy">

Wir ändern das Standardwerkzeug, indem wir es auswählen und auf die Schaltfläche Bearbeiten klicken. Dies öffnet das Werkzeugregelungsbearbeitungsfenster.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-ToolConfig.gif )


</div>


<div class="mw-translate-fuzzy">

Der dem Werkzeug gegebene Name und die Werkzeugnummer entsprechen der Werkzeugnummer der Maschine. Hier ist es Werkzeug Nr. 4. Die Werkzeugsteuerung ist für horizontale und vertikale Vorschübe von 2mm/s und eine Spindeldrehzahl von 2000 U/min ausgelegt.


</div>


<div class="mw-translate-fuzzy">

Wähle das Unterpaneel Werkzeug des Werkzeugsteuergeräts. Stelle den Durchmesser ein und - falls du das Simulationswerkzeug später verwenden möchtest - füge einen Schneidenwinkel und eine Schneidenhöhe hinzu.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-ToolAdd.gif )


</div>


<div class="mw-translate-fuzzy">

Die Werte werden mit OK bestätigt.


</div>


<div class="mw-translate-fuzzy">

Für einen einfachen Zugriff können alle Werkzeuge vordefiniert und über den [Werkzeugverwalter](Path_ToolLibraryEdit/de.md) ausgewählt werden.


</div>



### Auftragsarbeitsplan


<div class="mw-translate-fuzzy">

Der Arbeitsplanreiter beginnt leer und wird von der Abfolge der Auftragsvorgänge, Teilpfadbefehle und Pfadverschönerungen ausgefüllt. Die Reihenfolge dieser Elemente ist hier geordnet.


</div>

Dieser Baum wird nach der Konfiguration des Auftrags angezeigt, sobald der Pfadauftrag aufgeklappt ist:


<div class="mw-translate-fuzzy">

![](images/Path-TreeWithJob.png )


</div>



## Die Pfadabläufe 


<div class="mw-translate-fuzzy">

Es werden zwei Bearbeitungen hinzugefügt, um Fräsbahnen für diesen Pfadauftrag zu erzeugen. Der Ablauf [Kontur](Path_Profile/de.md) erzeugt eine Bahn um den Kasten herum und der Ablauf [Tasche](Path_Pocket_Shape/de.md) erzeugt eine Bahn für die Innentasche.


</div>


<div class="mw-translate-fuzzy">

Fürs Erste werden wir es einfach halten. Die <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Kontur](Path_Profile/de.md) Schaltfläche öffnet das Konturpaneel. Nach der Bestätigung mit OK unter Verwendung der Standardwerte siehst du, dass der grüne Pfad um das Objekt herum sichtbar ist.


</div>


<div class="mw-translate-fuzzy">

Auswählen des Taschenbodens und dann der <img alt="" src=images/Path_Pocket.svg  style="width:32px;"> [Tasche](Path_Pocket_Shape/de.md) Schaltfläche öffnet das Taschenfor Fenster. Die Standardwerte für Basisgeometrie, Tiefen und Höhen werden verwendet, und das Unter-Panel Operation ist ausgewählt und die Schrittweite in Prozent ist auf 50 eingestellt.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-PocketOperation.gif )


</div>


<div class="mw-translate-fuzzy">

Das Muster wird in \"Versatz\" geändert, und die Auftragsausführung wird für die Taschenkonfiguration mit OK bestätigt.


</div>

Das Ergebnis ist ein Modell mit zwei Pfaden:


<div class="mw-translate-fuzzy">

![](images/Path-WalkThroughResult.gif )


</div>



## Pfade überprüfen 

Es gibt zwei Möglichkeiten, die erstellten Pfade zu überprüfen. Der G-Code kann überprüft werden, einschließlich der Hervorhebung der entsprechenden Pfadsegmente. Der Fräsprozess des Bahnauftrags kann auch simuliert werden, um die idealisierten Werkzeugbahnen zu demonstrieren, die für die Werkzeuggeometrien zum Fräsen des Rohteils erforderlich sind.


<div class="mw-translate-fuzzy">

Um den G-Code zu untersuchen, verwende das <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> Werkzeug . Durch Auswählen der entsprechenden G-Code Zeilen innerhalb des G-Code Inspektionsfensters werden einzelne Pfadsegmente hervorgehoben.

![](images/Path-InspectWindow.gif )


</div>


<div class="mw-translate-fuzzy">

Um die Simulation zu beginnen verwende das <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [Pfad Simulator](Path_Simulator/de.md) Werkzeug.


</div>


<div class="mw-translate-fuzzy">

Stelle Geschwindigkeit und Genauigkeit ein und starte die Simulation mit der Wiedergabetaste.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-Simulation.gif )


</div>


<div class="mw-translate-fuzzy">

Wenn du die Simulation beenden möchtest, klicke auf die Schaltfläche Abbrechen, dadurch wird das für die Simulation erstellte Material entfernt. Wenn du auf Ok klickst, wird dieses Objekt in deinem Auftrag behalten.


</div>



## Nachbearbeitung des Auftrags 

Der letzte Schritt zur Erzeugung von G-Code für die Zielfräse ist die Nachbearbeitung des Auftrags. Dabei werden die G-Codes in eine Datei ausgegeben, die auf die Ziel CNC Maschinensteuerung hochgeladen werden kann. So rufst du den Postprozessor auf:


<div class="mw-translate-fuzzy">

-   Wähle das Auftragsobjekt im Baum aus
-   Wähle das Pfadnachbearbeitungswerkzeug <img alt="" src=images/Path_PostProcess.svg  style="width:32px;"> zur Nahbearbeitung der Datei aus. Dadurch wird ein G-Code Fenster geöffnet, in dem die endgültige Ausgabedatei vor dem Speichern überprüft werden kann.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-PostOutput.gif )


</div>


{{Path Tools navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Walkthrough for the Impatient/de
