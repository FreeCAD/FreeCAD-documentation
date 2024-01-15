---
 TutorialInfo:e
   Topic: Pfad Arbeitsbereich
   Level: Anfänger/Mittelmäßig
   Time: 15 Minuten
   Author: Chrisb
   FCVersion: 0.19
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

## Der Auftrag 

3\. Jetzt den [Auftrag](Path_Job/de.md) erstellen durch Auswahl einer der folgenden Methoden:

-   Die Schaltfläche **![](images/)_[Job](Path_Job.md)** drücken.
-   Das Tastaturkürzel **P** dann **J**.
-   Den Menüeintrag **Path → Auftrag** auswählen.

![](images/Path-JobCreationDialog.png )

:   

    :   
        
*Oben: Dialog [Path-Auftrag](Path_Job.md) erstellen*
        

4\. Dies öffnet ein Dialogfeld Auftrag erstellen. In diesem Dialog **OK** anklicken, um den Körper (Body-Objekt) als Basismodell ohne Vorlage zu akzeptieren.



### Auftragseinrichtung

5\. Das Auftragsbearbeitungsfenster öffnet sich im Aufgabenfenster, und das Modellansichtsfenster zeigt das Material als einen Drahtgitterwürfel, der den Grundkörper umgibt. Der Einrichtungsreiter ist ausgewählt.



### Auftragsausgabe

6\. Der Ausgabereiter legt den Pfad, den Namen und die Erweiterung der Ausgabedatei sowie den Postprozessor fest. Für fortgeschrittene Benutzer können Postprozessor-Argumente angepasst werden (der Mauszeiger darüber zeigt QuickInfos zu den allgemeinen Argumenten an).

:   ![](images/Path-JobOutput.png )

:   
    
*Oben: Dialog [Auftrag](Path_Job/de.md) bearbeiten mit ausgewähltem Ausgabe-Reiter*
    



### Auftragswerkzeuge

:   ![](images/Path-JobTools.png )

:   
    
*Oben: Dialog [Ausgabe](Path_Job/de.md) bearbeiten mit ausgewähltem Werkzeuge-Reiter*
    

7\. Das Standardwerkzeug anpassen, indem es ausgewählt und auf die Schaltfläche **Bearbeiten** geklickt wird. Dies öffnet das Fenster für die Werkzeugsteuerung.

:   ![](images/Path-ToolConfig.gif )

:   
    
*Above: Dialog [Auftrag](Path_Job/de.md) bearbeiten, Werkzeuge, Unterbereich Steuerung*
    

8\. Der dem Werkzeug gegebene Name und die Werkzeugnummer entsprechen der Werkzeugnummer der Maschine. Im Dialog (siehe oben) ist es Werkzeug Nr. 4. Die Werkzeugsteuerung ist für horizontale und vertikale Vorschübe von `2 mm/s` und eine Spindeldrehzahl von `2000 U/min` ausgelegt.

9\. Das Unterbereich Werkzeug der Werkzeugsteuerung auswählen. Den Durchmesser festlegen (und - falls das Werkzeug <img alt="" src=images/Path_Simulator.svg  style="width:24px;"> [Path Simulator](Path_Simulator/de.md) später verwendet werden soll: einen Schneidenwinkel und eine Schneidenhöhe hinzufügen).

:   ![](images/Path-ToolAdd.gif )

:   
    
*Oben: Dialog [Path Auftrag](Path_Job/de.md) bearbeiten, Werkzeuge, Unterbereich Werkzeug*
    

10\. Die Werte werden mit **OK** bestätigt.

Hinweis: Für einen einfachen Zugriff können alle Werkzeuge vordefiniert und mit dem<img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:24px;"> [Werkzeug-Bibliothek-Editor ](Path_ToolLibraryEdit/de.md) ausgewählt werden.



### Auftragsarbeitsplan

Der Reiter Arbeitsplan wird anfangs leer dargestellt. Er wird dann von der Abfolge von Auftragsvorgängen, Teilpfadbefehlen und Pfadverschönerungen ausgefüllt. Die Reihenfolge dieser Elemente wird hier geordnet.

Dieser Baum wird nach der Konfiguration des Auftrags angezeigt, sobald der Pfadauftrag aufgeklappt ist:

:   ![](images/Path-TreeWithJob.png )



## Die Pfadabläufe 

11\. Es werden zwei Bearbeitungen hinzugefügt, um Fräsbahnen für diesen Pfadauftrag zu erzeugen. Der Ablauf [Profil](Path_Profile/de.md) erzeugt eine Bahn um den Kasten herum und der Ablauf [Tasche](Path_Pocket_Shape/de.md) erzeugt eine Bahn für die Innentasche.

12\. Fürs Erste werden wir es einfach halten. Die Schaltfläche <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profil](Path_Profile/de.md) öffnet das Konturpaneel. Nach der Bestätigung mit **OK** unter Verwendung der Standardwerte, wird der der grüne Pfad um das Objekt herum sichtbar.

13\. Den Taschenboden auswählen und dann mit der Schaltfläche <img alt="" src=images/Path_Pocket_Shape.svg  style="width:32px;"> [Tasche](Path_Pocket_Shape/de.md) das Fenster Taschenform öffnen. Die Standardwerte für Basisgeometrie, Tiefen und Höhen werden verwendet und das Unter-Panel Operation ausgewählt sowie die Schrittweite in Prozent auf 50 eingestellt.

:   ![](images/Path-PocketOperation.gif )

:   
    
*Oben: Dialog Taschenform mit dem ausgewählten Unterbereich Operation*
    

14\. Das Muster wird in \"Versatz\" geändert, und die Auftragsausführung wird für die Taschenkonfiguration mit **OK** bestätigt.

Das Ergebnis ist ein Modell mit zwei Pfaden:

:   ![](images/Path-WalkThroughResult.gif )

:   
    
*Oben: Ergebnis mit einem Modell mit zwei Bewegungsbahnen*
    



## Pfade überprüfen 

Es gibt zwei Möglichkeiten, die erstellten Pfade zu überprüfen. Der G-Code kann überprüft werden, einschließlich der Hervorhebung der entsprechenden Pfadsegmente. Der Fräsprozess des Bahnauftrags kann auch simuliert werden, um die idealisierten Werkzeugbahnen zu demonstrieren, die für die Werkzeuggeometrien zum Fräsen des Rohteils erforderlich sind.

Um den G-Code zu untersuchen, wird das Werkzeug <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [Pfadbefehle untersuchen](Path_Inspect/de.md) verwendet. Durch Auswählen der entsprechenden G-Code-Zeilen innerhalb des G-Code-Inspektionsfensters werden einzelne Pfadsegmente hervorgehoben.

:   ![](images/Path-InspectWindow.gif )

:   
    
*Above: Das Werkzeug [Pfadbefehle untersuchen](Path_Inspect.md) öffnet den Dialog G-Code-Inspektion*
    

Um die Simulation zu beginnen wird das Werkzeug <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [Path Simulator](Path_Simulator/de.md) verwendet.

Geschwindigkeit und Genauigkeit einstellen und die Simulation mit der <img alt="" src=images/Path_BPlay.svg  style="width:24px;"> Wiedergabetaste (Play) starten.

:   ![](images/Path-Simulation.gif )

:   
    
*Oben: [Path Simulator](Path_Simulator.md) in Betrieb*
    

Soll die Simulation beendet werden, wird die Schaltfläche **Abbrechen** angeklickt, dadurch wird das für die Simulation erstellte Material entfernt. Wird **OK** angeklickt, wird dieses Objekt in deinem Auftrag behalten.



## Nachbearbeitung des Auftrags 

Der letzte Schritt zur Erzeugung von G-Code für die Zielfräse ist die Nachbearbeitung des Auftrags. Dabei werden die G-Codes in eine Datei ausgegeben, die auf die Ziel CNC Maschinensteuerung hochgeladen werden kann. So rufst du den Postprozessor auf:

-   Das Auftragsobjekt in der [Baumansicht](Tree_view/de.md) auswählen.
-   Das Werkzeug <img alt="" src=images/Path_PostProcess.svg  style="width:32px;"> [Path Nachbearbeitung](Path_Post.md) zum Nachbearbeiten der Datei auswählen. Dies öffnet ein G-Code Fenster, in dem die endgültige Ausgabedatei vor dem Speichern überprüft werden kann.

:   ![](images/Path-PostOutput.gif )

:   
    
*Oben: G-Code-Fenster, das die Überprüfung der endgültigen Ausgabedatei erlaubt*
    


{{Path Tools navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Walkthrough for the Impatient/de
