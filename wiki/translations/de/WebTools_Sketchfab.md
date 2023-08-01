---
- GuiCommand:
   Name: WebTools Sketchfab
   Name/de: WebWerkzeuge Sketchfab
   MenuLocation: WebWerkzeuge - Sketchfab
   Workbenches: [Arbeitsbereich WebWerkzeuge](WebTools_Workbench/de.md)
---

# WebTools Sketchfab/de

## Beschreibung

Dieses Werkzeug erlaubt dir Objekte zu exportieren und auf dein [SketchFab](http://www.sketchfab.com) Konto hochzuladen. {{Version/de|0.17}}

![](images/Sketchfab_exporter.jpg )

## Anwendung

1.  Erstelle dir ein Konto auf [SketchFab](http://www.sketchfab.com), wenn du noch keins hast. Kostenlose Konten sind in Ordnung, kostenpflichtige Konten bieten mehr Funktionen als die Möglichkeit, private Modelle und größere maximale Upload Größen zu haben.
2.  Bereite ein Modell vor, das du hochladen möchtest
3.  Klicke auf <img alt="" src=images/WebTools_Sketchfab.svg  style="width:32px;"> in der Hauptwerkzeugleiste der [Arbeitsbereich WebWerkzeuge](WebTools_Workbench/de.md)
4.  Fülle die Felder aus. Name und API Schlüssel sind Pflichtfelder.
5.  Klicke die Schaltfläche \"Hochladen\".

## Optionen

-   Du benötigst einen Sketchfab API Schlüssel für diesen Exporteur, um dich mit deinem Sketchfab Konto verbinden zu können. Durch drücken auf die \"Beziehen\" Schaltfläche, wirst du zu deiner Sketchfab Einstellungsseite weitergeleitet, wo dieser API Schlüssel (der für dein Konto einzigartig ist) angegeben ist. Kopiere den Schlüssel und füge ihn in das Feld \"API Schlüssel\" im Exporteur ein. Dieser Wert wird von FreeCAD gespeichert, so dass du dies nur einmal tun musst
-   Das Namensfeld ist obligatorisch, die anderen Felder können leer gelassen werden.
-   Der Exporteur bietet mehrere verschiedene Exportformate an. Welches für dich am besten geeignet ist, hängt von der Art des Modells und dem gewünschten Ergebnis ab; es wird empfohlen, zu testen, welches Format für dich am besten geeignet ist. Im Allgemeinen hast du mit OBJ + MTL eine bessere Kontrolle über die Materialien, während IV (OpenInventor) ein Ergebnis liefert, das der FreeCAD 3D Ansicht ähnlicher ist.
-   Sobald dein Modell hochgeladen ist, bietet Sketchfab eine ziemlich fortschrittliche Oberfläche, auf der du Materialien, Beleuchtung und Umgebung weiter konfigurieren kannst.
-   Wenn du die Schaltfläche \"Hochladen\" drückst, verwandelt sich die Schaltfläche nach Abschluss des Hochladens in eine Schaltfläche \"Modell online ansehen\", die du direkt zur Modellseite auf Sketchfab führt, wenn du darauf klickst.
-   Einige Formate, wie OBJ, werden von Sketchfab und FreeCAD unterschiedlich interpretiert. FreeCAD geht davon aus, dass die Z Achse nach oben zeigt, während Sketchfab davon ausgeht, dass sie in Richtung der Person hinter dem Bildschirm zeigt. Um dieses Problem zu beheben, verwendet der Exporteur nach dem Hochladen die Sketchfab API, um das Modell in die richtige Position zu drehen. Wenn dieser Vorgang fehlschlägt, wirst du gewarnt, aber dein Modell wird trotzdem korrekt hochgeladen. Du kannst das Modell in der Sketchfab Oberfläche manuell drehen, durch drücken des rechten Pfeils neben der \"X\" Achse im \"Modellausrichtung\"sreiter.



---
⏵ [documentation index](../README.md) > WebTools Sketchfab/de
