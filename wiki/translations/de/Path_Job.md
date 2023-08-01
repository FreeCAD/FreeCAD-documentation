---
- GuiCommand:
   Name:Path Job
   Name/de:Path Auftrag
   MenuLocation:Pfad - Auftrag
   Workbenches:[Pfad](Path_Workbench/de.md)
   Shortcut:**P** **J**
---

# Path Job/de



## Beschreibung


<div class="mw-translate-fuzzy">

Das Auftrag Werkzeug erstellt ein neues Auftragsobjekt im aktiven Dokument. Das Auftragsobjekt enthält die folgenden Informationen:

1.  Eine Liste mit Werkzeug-Controller-Definitionen, in der die Geometrie, Vorschübe und Geschwindigkeiten für die Pfadbearbeitungswerkzeuge angegeben sind.
2.  Eine schrittweise Arbeitsablaufliste von Pfadoperationen.
3.  Ein Basiskörper - ein Klon, der für den Versatz verwendet wird.
4.  Ein Schaft, der das Rohmaterial darstellt, der zum Pfad Arbeitsbereich gefräst wird.
5.  Ein Einrichtungsdatenblatt, das die von den Pfadoperationen verwendeten Eingaben, einschließlich statischer Werte und Formeln, enthält.
6.  Konfigurationsparameter, die den Zielpfad des ausgegebenen G-Code Auftrags, den Dateinamen und die Dateierweiterung sowie den [Postprozessor](Path_Post/de.md) angeben (der zur Erzeugung des entsprechenden Dialekts für die Ziel-CNC-Steuerung und zur Anpassung von Einheiten, Werkzeugänderungen, Parken usw. verwendet wird).


</div>



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen
    -   Die Schaltfläche **<img src="images/Path_Job.svg" width=16px> [Path Auftrag](Path_Job/de.md)** Drücken.
    -   Den Menüeintrag **Path → <img src="images/Path_Job.svg" width=16px> Auftrag** auswählen.
    -   Das Tastaturkürzel **P** dann **J**.

Die Auftrags GUI hat fünf horizontal ausgerichtete Reiter: **Allgemein**, **Ausgabe**, **Einrichten**, **Werkzeuge**, und **Arbeitsplan**. Der Benutzer kann jederzeit die Optionen **OK** oder **Abbrechen** innerhalb des Dialogs verwenden.



## Allgemein

![](images/Job_1.jpg )

-   **Kennzeichen**: Der Name des Auftragsobjekts wie es in der Baumansicht angezeigt wird.
-   **Modell**: Das Basisobjekt, das durch seine Form die Pfade des Jobs definiert. Wenn es sich um ein Part Design Objekt handelt, ist es normalerweise der Body, den Du hier auswählst. Wenn du ein Element in der Baumstruktur *vorher* ausgewählt hast, klicke auf das Symbol \"Auftrag hinzufügen\", das Element ist hier bereits eingetragen. Du kannst es ändern, indem du ein anderes Element aus dem Ausklappmenü auswählst.
-   **Beschreibung**: Du kannst hier einige Notizen zu dem Auftrag hinzufügen. Die Notizen dienen nur zu deiner Information und haben keine Auswirkung auf den Pfad.



## Ausgabe

![](images/Job_2.jpg )

-   **Ausgabedatei**: Lege den Namen, die Erweiterung und den Dateipfad der G-Code Ausgabe fest. Du kannst die folgenden Platzhalter verwenden:
    -   **%D** Verzeichnis des aktiven Dokuments
    -   **%d** Name des aktiven Dokuments (ohne Erweiterung)
    -   **%M** Benutzer Makro Verzeichnis
    -   **%j** Name des Auftrags

-   **Prozessor**: Wähle den [Postprozessor](Path_Post/de.md) für deine Maschine aus.
-   **Argumente**: Füge bei Bedarf Argumente für den [Postprozessor](Path_Post/de.md) hinzu.



## Einrichtung

![](images/Job_3.jpg )

-   **Bestand**: Lege die Größe und Form des Rohmaterials fest.
-   **Orientierung**\': Ausgewählte Kante oder Fläche wird verwendet, um die Basis oder den Schaft entsprechend zu orientieren.
-   **Ausrichtung**\': Wähle einen Knotenpunkt aus, um den Ursprung festzulegen oder die Basis oder das Lager zu verschieben.



## Werkzeuge

![](images/Job_4.jpg )

Füge das/die Werkzeug(e) aus deiner [Werkzeugtabelle](Path_ToolLibraryEdit/de.md) hinzu, welche du für die Arbeitsgänge bei diesem Auftrag benötigst.

Nachdem ein Werkzeug hinzugefügt wurde, kannst du den Vorschub und die Spindeldrehzahl einstellen/ändern, wenn du bei diesem Auftrag einen anderen Vorschub benötigst. Eine Änderung hier ändert nicht die in der Werkzeugtabelle gespeicherten Parameter.

Das Standardwerkzeug kannst du löschen, wenn du ein eigenes Werkzeug hinzugefügt hast.



## Arbeitsplan

![](images/Job_5.jpg )

Wenn du eine Aufgabe hast, die mehr als eine Pfadoperation umfasst, kannst du festlegen, in welcher Reihenfolge die Arbeitsgänge ausgeführt werden sollen. Um die Reihenfolge zu ändern, wähle einen Vorgang aus und drücke die Auf- oder Abwärtstaste.





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Job/de
