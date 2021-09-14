# TechDraw LineGroup/de







{{TOCright}}

## Übersicht

LinienGruppen werden verwendet, um das Aussehen verschiedener Arten von Linien zu steuern.

### Anwendung

1.  Gehe auf den Einstellungen Reiter *[Anmerkung](TechDraw_Preferences/de#Anmerkung.md)*.
2.  Wähle im Feld **Linienbreitengruppe** eine LinienGruppe aus. Dies sind die Gruppen, die in der LinienGruppen Definition csv Datei definiert sind.

Zum ändern der LinienGruppen-Definitionsdatei

1.  Gehe auf den Einstellungsreiter *[Allgemein](TechDraw_Preferences/de#Allgemein.md)*.
2.  Wähle im Feld **Linien Gruppen Datei** eine LinienGrupppen Definitionsdatei aus.

### Anpassen von LinienGruppen 

Wenn du Schreibberechtigung hast, kannst du `LineGroup.csv` bearbeiten, um deine eigenen LinienGruppen hinzuzufügen.

Diese Datei ist normalerweise in:


```python
$INSTALL_DIR/Mod/TechDraw/LineGroup/LineGroup.csv
```

wobei `$INSTALL_DIR` das Verzeichnis ist, in dem FreeCAD installiert wurde, z.B.


```python
/usr/share/freecad/Mod/TechDraw/LineGroup/LineGroup.csv
```

Du kannst deine bevorzugten Standardeinstellungen in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) angeben.

## LinienGruppe Dateipfad 

-   **Windows**: `C:\Program Files\FreeCAD\data\Mod\TechDraw\LineGroup\`
-   **Mac**: `/Applications/FreeCAD.app/Contents/Mod/TechDraw/LineGroup/`
-   **Linux**: {`/usr/share/freecad/Mod/TechDraw/LineGroup/`}
    -   ***freecad-daily PPA***: `/usr/share/freecad-daily/Mod/TechDraw/LineGroup/`

Hinweis: Eine neue Einstellung wurde hinzugefügt, die es dir erlaubt, deine eigene persönliche LinienGruppe Datei zu verwenden.


```python
;FreeCAD LineGroup Definitions
;Format: *GroupName,thin,graphic,thick,extra
;thin: hidden lines
;graphic: dimensions, centerlines
;thick: visible lines
;extra: not implemented
```


```python
*FC 0.25mm,0.13,0.18,0.25,0.50
*FC 0.35mm,0.18,0.25,0.35,0.70
*FC 0.50mm,0.25,0.35,0.50,1.0
*FC 0.70mm,0.35,0.50,0.70,1.4
*FC 1.00mm,0.50,0.70,1.00,2.00
```

## Hinweis

-   Die Linienbreite in TechDraw ist immer in mm angegeben, auch bei Verwendung anderer Einheitensysteme.





{{TechDraw Tools navi

}}  
