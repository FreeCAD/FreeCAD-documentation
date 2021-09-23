# FreeCAD and Mesh Import/de



{{TOCright}}

## Post-Import 


<div class="mw-translate-fuzzy">

## Nach dem Import 

Nach dem Import ist das Modell (für FreeCAD) nur eine Baugruppe von Flächen. Du möchtest das Modell vielleicht in eine Form konvertieren, die FreeCAD erkennt und die in FreeCAD geändert werden könnte.


</div>


<div class="mw-translate-fuzzy">

Um dies zu tun:

-   zum Teile Arbeitsbereich wechseln
-   Wähle das Netz aus und gehe zum Menü Teil \--\> Erzeuge Form aus Netz
-   Klicke auf OK, um den Dialog zu starten
-   Wähle die neu erstellte Form aus
-   Gehe zu Teil \--\> Umwandeln in einen Festkörper
-   Wähle den neu erstellten Festkörper aus
-   Gehe zu Teil \--\> Form verfeinern


</div>

**Hinweis**: Der letzte Schritt ist nicht notwendig, aber er reinigt den Festkörper von den meisten seiner Restkanten auf ebenen und zylindrischen Oberflächen.

## Fehler

### \"cannot convert because shape is not a shell\" 


<div class="mw-translate-fuzzy">

## \"kann nicht konvertieren, weil die Form keine Schale ist\" 

Nun, deine Schale scheint Fehler zu haben, vielleicht ist sie nicht geschlossen (hat Löcher). Da die Möglichkeiten des Mesh (Netz)-Arbeitsbereichs in FreeCAD derzeit etwas eingeschränkt sind, solltest du vielleicht versuchen, dein Modell mit Software von Drittanbietern zu untersuchen und zu reparieren. Danach kannst du versuchen, dein Modell erneut zu importieren und zu konvertieren.


</div>


<div class="mw-translate-fuzzy">

## Drittanbieterprogramme

-   [Meshlab](http://meshlab.sourceforge.net/)
    -   Lizenz: Quelloffen (GPL V2)
    -   Läuft unter Windows 32/64 Bit, Linux und Mac OS X


</div>


<div class="mw-translate-fuzzy">

-   [netFabb basic](http://www.netfabb.com/downloadcenter.php?basic=1)
    -   Lizenz: Freeware
    -   Läuft unter Windows XP/7/8, Linux und Mac OS X


</div>

## Tutorials


<div class="mw-translate-fuzzy">

## Tutorien

-   [Import aus STL oder OBJ](Import_from_STL_or_OBJ/de.md)
-   [Export nach STL oder OBJ](Export_to_STL_or_OBJ/de.md)


</div>

## Verwandt

-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)

[Category:User\_Documentation](Category:User_Documentation.md) [Category:File\_Formats](Category:File_Formats.md)
