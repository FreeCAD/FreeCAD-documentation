# FreeCAD and Mesh Import/de
{{TOCright}}



## Nach dem Import 

Nach dem Import ist das Modell (für FreeCAD) nur eine Baugruppe von Flächen. Du möchtest das Modell vielleicht in eine Form konvertieren, die FreeCAD erkennt und die in FreeCAD geändert werden kann.

Um dies zu tun:

1.  Zum Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) wechseln.
2.  Das Netz auswählen und den Menüeintrag **Part → [Form aus Netz erstellen](Part_ShapeFromMesh/de.md)** auswählen oder die Schaltfläche <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:24px;"> [Form aus Netz erstellen](Part_ShapeFromMesh/de.md) drücken.
3.  Im Dialog **OK** anklicken.
4.  Die neu erstellte Form auswählen.
5.  Den Menüeintrag **Part → [In Festkörper umwandeln](Part_MakeSolid/de.md)** auswählen.
6.  Den neu erstellten Festkörper auswählen.
7.  Den Menüeintrag **Part → [Form aufbereiten](Part_RefineShape/de.md)** oder die Schaltfläche <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Form aufbereiten](Part_RefineShape/de.md) drücken.

**Hinweis**: Der letzte Schritt ist nicht notwendig, aber er reinigt den Festkörper von den meisten seiner Restkanten auf ebenen und zylindrischen Oberflächen.



## Fehler

### \"cannot convert because shape is not a shell\" 

Nun, deine Schale scheint Fehler zu haben, vielleicht ist sie nicht geschlossen (hat Löcher). Da die Möglichkeiten des Arbeitsbereichs Mesh (Netz) in FreeCAD derzeit etwas eingeschränkt sind, solltest du vielleicht versuchen, dein Modell mit Software von Drittanbietern zu untersuchen und zu reparieren. Danach kannst du versuchen, dein Modell erneut zu importieren und zu konvertieren.



## Drittanbieterprogramme

-   [Meshlab](http://meshlab.sourceforge.net/)
    -   Lizenz: Open Source (GPL V2)
    -   Läuft unter Windows 32/64 bit, Linux und macOS
-   [netFabb basic](http://www.netfabb.com/downloadcenter.php?basic=1)
    -   Lizenz: Freeware
    -   Läuft unter Windows XP/7/8, Linux and macOS



## Anleitungen

-   [Import aus STL oder OBJ](Import_from_STL_or_OBJ/de.md)
-   [Export nach STL oder OBJ](Export_to_STL_or_OBJ/de.md)



## Verwandt

-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and Mesh Import/de
