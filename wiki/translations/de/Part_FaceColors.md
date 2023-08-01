---
- GuiCommand:
   Name:Part FaceColors
   Name/de:Part FlächenFarben
   MenuLocation:Kontextmenü - Farben setzen
   Workbenches:[Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md)
   SeeAlso:[Std Erscheinungsbild](Std_SetAppearance/de.md)
---

# Part FaceColors/de



## Beschreibung

Die Funktion **FlächenFarben** ermöglicht es, für jede Fläche oder Oberfläche eines Objekts eine Farbe zu definieren. Auf diese Weise können einem Teil mehrere Farben zugewiesen werden. Um ganze Teile einzufärben, wird stattdessen die Funktion *[Std Darstellung](Std_SetAppearance/de.md)* verwendet.



## Verwendung

Flächen einfärben:

1.  Ein Objekt mit der rechten Maustaste in der [Baumansicht](Tree_view/de.md) anklicken. Wenn das Objekt die Flächenfarben-Funktionalität (FaceColors) unterstützt, findet man im Kontextmenü den Eintrag **Farben festlegen\...** zum Anklicken.
2.  Fläche(n) auswählen:
    -   Eine einzelne Fläche wird mit einem einfachen Klick ausgewählt.
    -   Mehrere Flächen auswählen:
        -   
            **Ctrl**
            
            gedrückt halten und mehrere Flächen anklicken.

        -   Die Schaltfläche **Rechteckauswahl** im Aufgabenbereich drücken. Dann kann mit der Maus in der [3D-Ansicht](3D_view/de.md) ein Auswahlrechteck aufgezogen werden. Jede Fläche, die sich teilweise im Auswahlrechteck befindet, wird ausgewählt.
3.  Im Aufgabenbereich eine Farbe für die ausgewählten Flächen festlegen. {{Version/de|0.20}}: Der Farbe kann durch Ändern des Wertes für den \"Alphakanal\" eine Transparenz zugeordnet werden.
4.  Die Schaltfläche **OK** drücken, um den Aufgabenbereich zu schließen und die Änderungen zu akzeptieren.

Um alle Flächenfarben zurückzusetzen:

1.  Klicke auf **Auf Standard setzen**. Dadurch werden die Farben aller Flächen des Teils auf die Standardfarbe gesetzt. Die Schaltfläche funktioniert sofort, d. h., du kannst dies nicht mit der **Abbrechen** Schaltfläche rückgängig machen.

![](images/Part_FaceColors-dialog.png ) 
*Der Aufgabenbereich Festlegen der Farben pro Fläche*



---
![](images/Button_right.svg) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Command_Reference](Category_Command_Reference.md) > [Part](Part_Workbench.md) > Part FaceColors/de
