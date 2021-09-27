# Import from STL or OBJ/de
{{TutorialInfo/de
|Topic= Import von STL oder OBJ
|Level= Anfänger
|Time= 30 Minuten
|Author=r-frank
|FCVersion=0.16.6703
|Files=
}}

## Einführung

In diesem Tutorium werden wir behandeln, wie STL/OBJ-Dateien in FreeCAD importiert werden können. Da das Netzformat STL/OBJ dimensionslos ist, geht FreeCAD beim Import davon aus, dass die im Modell verwendeten Einheiten mm sind. Wenn dies nicht der Fall ist, musst du dein Modell entweder in der Anwendung skalieren, mit der es erstellt wurde (vor dem Export) oder du musst dein Modell in FreeCAD nach dem Import und der Umwandlung in einen Volumenkörper skalieren.

## Musterteil

Für dieses Tutorium kannst Du Deine eigene STL Datei verwenden oder auf diese Weise eine Demodatei erstellen:

-   Öffne FreeCAD
-   Erstelle ein neues Dokument
-   Wechsle zum Netz Arbeitsbereich
-   Füge einen Torus durch Klicken auf **Netze** → **<img src="images/Mesh_BuildRegularSolid.svg" width=32px> Regelmäßiger Volumenkörper... ** ein, Einstellungen wählen wie:
    -   Radius1: 10 mm
    -   Radius2: 2 mm
    -   Stichprobenahme: 50
-   Klicke auf **Erstellen** und dann auf **Schließen**
-   Speichere deine Datei mit **Datei** → **Speichern**, um eine FreeCAD Datei zu erhalten, die ein Netzobjekt enthält

Um eine STL oder OBJ Datei in FreeCAD zu importieren, erstelle ein neues FreeCAD Dokument und wähle **Datei** → **Import** aus dem oberen Menü aus.

## Bereinigen und Reparieren der STL/OBJ-Datei um den Import vorzubereiten 

Grunsätzlich importiert FreeCAD jede STL/OBJ-Datei. Aber unser Ziel ist es, einen Volumenkörper zu haben, der vermessen und verändert (Polster, Taschen hinzufügen) werden kann. Für eine erfolgreiche Umwandlung von Netz zu Volumenkörper müssen wir sicherstellen, daß das Netz \"wasserdicht\" ist (keine Löcher enthält) oder andere Fehler und Probleme vorliegen.
FreeCAD strebt nicht danach ein guter Netz Modellierer zu sein, es will ein guter Volumen Modellierer sein. FreeCAD verfügt über einige Funktionen für den Netzeinsatz im Netz Arbeitsbereich und dem OpenSCAD Arbeitsbereich (für einige Operationen muss OpenSCAD installiert und in den FreeCAD Einstellungen konfiguriert sein).
Einige Benutzer verwenden gerne Software von Drittanbietern für die Bereinigung und Reparatur von Netzen, zum Beispiel

-   [Netfabb Basic](http://www.netfabb.com/downloadcenter.php?basic=1) (Windows/Linux/Mac) - frei zur privaten Nutzung (automatische Netzrepaeratur verfügbar)
-   [Meshlab](http://meshlab.sourceforge.net/) (Windows/Linux/Mac) - Open Source

In diesem Tutorium werden wir den Netz Arbeitsbereich in FreeCAD benutzen, um das Netz unserer Musterdatei zu bereinigen/reparieren/überprüfen.

### Automatisches Testen und Reparieren 

-   Öffne FreeCAD und die FreeCAD-Musterdatei, die das Netzobjekt enthält
-   Wechsle in den Netz-Arbeitsbereich
-   Stelle sicher, dass das Netzobjekt in der Baumansicht ausgewählt ist
-   Wähle **Netze** → **Analysieren** → **Netz auswerten und analysieren...** aus dem obersten Menü
-   Stelle sicher, dass das Auswahlmenü in der rechten oberen Ecke den Namen des Netzobjektes anzeigt
-   Wenn der letzte Punkt in der Liste \"Alle oben genannten Tests zusammen\" lautet, klicke auf **Analysieren**
-   Die Texte neben den Kontrollkästchen werden sich ändern, um die Ergebnisse der verschiedenen Tests wiederzugeben.
-   Wenn Fehler entdeckt wurden, werden die entsprechenden Kontrollkästchen angekreuzt und du kannst **Reparieren** auswählen
-   Wähle **Schließen**, um das Menü zu beenden

### Normalen harmonisieren 

Die Harmonisierung der Normalen eines Netzobjekts kann wie folgt durchgeführt werden

-   Auswahl deines Netzobjekts in der Baumansicht
-   Wähle **Netze** → **<img src="images/Mesh_HarmonizeNormals.svg" width=32px> Normalen harmonisieren** aus dem oberen Menü.

Tip: Durch Wahl des Netzobjekts in der Baumansicht, zum Ansichtsreiter in der Eigenschaftsansicht gehen und \"Beleuchtung\" von \"Zwei Seiten\" auf \"Eine Seite\" wechseln, kannst du Dreiecke mit umgeklappten Normalen identifizieren. Wenn die Normalen in das Netz zeigen, wird das Dreieck schwarz dargestellt.

### Löcher schließen 

Du kannst Löcher in deinem Netzobjekt auch manuell schließen, durch

-   Wählen deines Netzobjekt in der Baumansicht
-   Wähle **Netze** → **Löcher füllen...** aus dem oberen Menü
-   Maximale Anzahl der auszufüllenden Kanten angeben (3 ist Standard)
-   Da STL und OBJ Netze sind, die aus Dreiecken bestehen, sollte die Standardanzahl der Kanten ausreichend sein

Eine andere Methode, Löcher in deinem Netzobjekt manuell zu schließen, wäre

-   Wähle dein Netzobjekt in der Baumansicht
-   Wähle **Netze** → **<img src="images/Mesh_FillInteractiveHole.svg" width=32px> Loch schließen** aus dem oberen Menü
-   Wähle eine der Kanten des Lochs im Netzobjekt in der 3D Ansicht
-   Rechtsklicke in der 3D Ansicht und wähle **Verlassen des Lochfüllmodus**, um den Befehl zu beenden

## Umwandlung Netz zu Volumenkörper 

-   Wechsle zu <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Arbeitsbereich](Part_Workbench/de.md)
-   Stelle sicher, dass dein Netzobjekt in der Baumansicht ausgewählt ist, ansonsten wähle es
-   Wähle **Formteil** → **<img src="images/Part_ShapeFromMesh.svg" width=32px> Form aus Netz erzeugen ...** aus dem oberen Menü
-   Toleranz für Form nähen angeben (0,1 ist Standard)
-   Es wird ein neues Objekt in der Baumansicht erstellt (mit blauem Formsymbol statt grünem Netzsymbol)
-   Wähle das neu erstellte Objekt in der Baumansicht
-   Wähle **Formteil** → **In Festkörper umwandeln** aus dem oberen Menü
-   Ein neues Objekt wird in der Baumansicht erzeugt, das (Solid) im Namen trägt, um anzuzeigen, dass es sich um einen Volumenkörper handelt

Da der erzeugte Festkörper keine Historie und keine bearbeitbaren Formelemente hat (wie eine einfache Kopie in FreeCAD) könntest du alle vorherigen Objekte aus der Baumansicht löschen. Dies würde deine Dateigröße klein halten \...

## Verweise

-   [Export nach STL oder OBJ](Export_to_STL_or_OBJ/de.md)
-   [Import Export](Import_Export/de.md)


 

_

---
[documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Import](Import_Workbench.md) > Import from STL or OBJ/de
