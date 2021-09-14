# TechDraw LineGroup/ru







{{TOCright}}

## Обзор

LineGroups are used to control the appearance of various types of lines.

### Usage

1.  Go to the preferences tab *[Annotation](TechDraw_Preferences#Annotation.md)*.
2.  Select in the field **Line Width Group** a LineGroup. These are the groups defined in the LineGroup definition csv file.

To change the LineGroups definition file

1.  Go to the preferences tab *[General](TechDraw_Preferences#General.md)*.
2.  Select in the field **Line Group File** a LineGroup definition file.

### Customizing LineGroups 

If you have write permission you can edit `LineGroup.csv` to add your own LineGroups.

This file is usually in:


```python
$INSTALL_DIR/Mod/TechDraw/LineGroup/LineGroup.csv
```

Where `$INSTALL_DIR` is the directory where FreeCAD was installed, for example


```python
/usr/share/freecad/Mod/TechDraw/LineGroup/LineGroup.csv
```

You can specify your favorite defaults in the [TechDraw Preferences](TechDraw_Preferences.md).

## LineGroup File Path 

-   **Windows**: `C:\Program Files\FreeCAD\data\Mod\TechDraw\LineGroup\`
-   **Mac**: `/Applications/FreeCAD.app/Contents/Mod/TechDraw/LineGroup/`
-   **Linux**: `/usr/share/freecad/Mod/TechDraw/LineGroup/`
    -   ***freecad-daily PPA***: `/usr/share/freecad-daily/Mod/TechDraw/LineGroup/`

Note: A new preference has been added to allow you to use your own personal LineGroup file.


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

## Примечания

-   Line width in TechDraw is always specified in mm, even when using other unit systems.





{{TechDraw Tools navi

}}  
