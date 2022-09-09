# TechDraw LineGroup/de
{{TOCright}}

## Übersicht

Liniengruppen werden verwendet, um die Darstellung verschiedener Linienarten zu steuern.

### Anwendung

1.  Zum Reiter *[Anmerkung](TechDraw_Preferences/de#Anmerkung.md)* der Einstellungen wechseln.
2.  Im Feld **Liniengruppe** eine Liniengruppe auswählen. Dies sind die Gruppen, die in der CSV-Datei LineGroup definiert sind.

Zum ändern der Liniengruppendatei

1.  Zum Reiter *[Allgemein](TechDraw_Preferences/de#Allgemein.md)* der Einstellungen wechseln.
2.  Im Feld **Liniengruppendatei** eine Liniengruppendatei auswählen.

### Liniengruppen anpassen 

Wenn man Schreibberechtigung hat, kann man `LineGroup.csv` bearbeiten, um eigene Liniengruppen hinzuzufügen.

Diese Datei befindet sich normalerweise in   *


```python
$INSTALL_DIR/Mod/TechDraw/LineGroup/LineGroup.csv
```

Dabei ist `$INSTALL_DIR` das Verzeichnis, in dem FreeCAD installiert wurde, z.B.


```python
/usr/share/freecad/Mod/TechDraw/LineGroup/LineGroup.csv
```

Die eigenen bevorzugten Standardeinstellungen können in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) angeben werden.

## Pfad der LineGroup-Datei 

-   **Windows**   * `C   *Program Files\FreeCAD\data\Mod\TechDraw\LineGroup\`
-   **Mac**   * `/Applications/FreeCAD.app/Contents/Mod/TechDraw/LineGroup/`
-   **Linux**   * {`/usr/share/freecad/Mod/TechDraw/LineGroup/`}
    -   ***freecad-daily PPA***   * `/usr/share/freecad-daily/Mod/TechDraw/LineGroup/`

Hinweis   * Eine neue Einstellung wurde hinzugefügt, die es erlaubt, eine eigene persönliche Liniengruppendatei zu verwenden.


```python
;FreeCAD LineGroup Definitions
;Format   * *GroupName,thin,graphic,thick,extra
;thin   * hidden lines
;graphic   * dimensions, centerlines
;thick   * visible lines
;extra   * not implemented
```


```python
*FC 0.25mm,0.13,0.18,0.25,0.50
*FC 0.35mm,0.18,0.25,0.35,0.70
*FC 0.50mm,0.25,0.35,0.50,1.0
*FC 0.70mm,0.35,0.50,0.70,1.4
*FC 1.00mm,0.50,0.70,1.00,2.00
```

## Hinweis

-   Die Linienbreite in TechDraw wird immer in mm angegeben, auch bei Verwendung anderer Einheitensysteme.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LineGroup/de
