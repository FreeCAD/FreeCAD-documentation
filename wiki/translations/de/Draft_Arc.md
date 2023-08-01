---
- GuiCommand:
   Name:Draft Arc
   Name/de:Draft Bogen
   MenuLocation:Entwurf - Bogenwerkzeuge - Kreisbogen
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Version:0.7
   Shortcut:**A** **R**
   SeeAlso:[Draft Bogen 3Punkte](Draft_Arc_3Points/de.md), [Draft Kreis](Draft_Circle/de.md)
---

# Draft Arc/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> **Draft Bogen** erstellt einen Kreisbogen auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) aus Mittelpunkt, Radius, Anfangswinkel und Öffnungswinkel. Der Radius und die Winkel können durch Indizieren der Punkte festgelegt werden.

Ein Draft-Bogen ist eigentlich ein [Draft-Kreis](Draft_Circle/de.md) mit einer {{PropertyData/de|First Angle}} die nicht identisch ist mir der {{PropertyData/de|Last Angle}}.

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;"> 
*Ein durch vier Punkte festgelegter Bogen aus Mittelpunkt, Radius, Startpunkt und letztem Punkt des Bogens*



## Anwendung

Siehe auch: [Entwurf Ablage](Draft_Tray/de.md), [Entwurf Fang](Draft_Snap/de.md) und [Entwurf beschränken](Draft_Constrain/de.md).


<div class="mw-translate-fuzzy">

## Anwendung 

1.  Drücke den **<img src="images/Draft_Arc.svg" width=16px> [Bogen](Draft_Arc/de.md)
** Taste oder drücke **A**, dann **R**
2.  Klicke einen ersten Punkt in der 3D Ansicht oder tippe eine Koordinate und drücke den **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** Taste.
3.  Klicke einen zweiten Punkt in der 3D Ansicht oder gib einen Wert für den Radius ein.
4.  Klicke einen dritten Punkt in der 3D Ansicht oder gib einen Startwinkel ein.
5.  Klicke einen vierten Punkt in der 3D Ansicht oder gib einen Öffnungswinkel ein.


</div>



## Optionen

Die im Aufgabenpaneel verfügbaren Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die Standardtastenkürzel.


<div class="mw-translate-fuzzy">

## Optionen 

-   Die primäre Anwendung des Kreisbogen-Werkzeugs erfolgt durch Auswahl von vier Punkten: dem Mittelpunkt, einem Punkt auf dem Umkreis, dem Startwinkel und dem Endpunkt.
-   Durch Drücken von **Alt** kannst Du eine Tangente anstatt eines Punkts zur Definition des Basiskreises des Bogens auswählen. Du kannst deshalb verschiedene Kreisarten durch Auswahl von ein, zwei oder drei Tangenten erstellen.
-   Die Richtung des Kreisbogens hängt von der Bewegung Deiner Maus ab. Wenn Du sie nach Eingabe des dritten Punkts im Uhrzeigersinn bewegst, wird auch der Kreisbogen im Uhrzeigersinn erstellt. Um ihn gegen den Uhrzeigersinn zu erstellen, bewege die Maus einfach zurück über den dritten Punkt, bis der Kreisbogen in die andere Richtung gezeichnet wird.
-   Um Koordinaten manuell einzugeben, gibt einfach die Ziffern ein, drücke dann **Enter** zwischen den X-, Y- und Z-Komponenten. Du kannst den **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen**-Button drücken, wenn Du die gewünschten Werte zum Einfügen des Punkts hast.

-   Drücke **T** oder klicke das Ankreuzkästchen zum de/aktivieren des **'''Nächstes'''**-Buttons. Wenn der Fortsetzungsmodus aktiviert ist, wird das Kreisbogen-Tool nach Beenden des Bogens neugestartet, um das Zeichnen eines weiteren ohne erneutes Drücken des Werkzeug-Buttons zu ermöglichen.
-   Halte **Strg** während des Zeichnens, um das Einrasten Deines Punkts an der nächsten Einrastposition zu erzwingen, unabhängig vom Abstand.
-   Halte **Shift** während des Zeichnens, um Deinen Punkt horizontal oder vertikal in Relation zum Mittelpunkt einzuschränken.
-   Drücke **Esc** oder den **'''Schließen'''**-Button, um den aktuellen Linien-Befehl abzubrechen.


</div>



## Hinweise

-   Ein Bogen kann mit dem [Bearbeiten](Draft_Edit/de.md)-Befehl geändert werden.



## Einstellungen

Siehe auch: [Einstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   To change the number of decimals used for the input of coordinates, radii and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.



## Eigenschaften

Siehe [Draft Kreis](Draft_Circle/de#Properties.md).



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen eines Draft-Bogens wird die Methode `make_circle` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeCircle`.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

arc1 = Draft.make_circle(200, startangle=0, endangle=90)
arc2 = Draft.make_circle(500, startangle=20, endangle=160)
arc3 = Draft.make_circle(750, startangle=-30, endangle=-150)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Arc/de
