# TechDraw LineGroup/it



<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Descrizione

I gruppi di linee vengono utilizzati per controllare l\'aspetto di vari tipi di linee.

### Usage

1.  Go to the preferences tab *[Annotation](TechDraw_Preferences#Annotation.md)*.
2.  Select in the field **Line Width Group** a LineGroup. These are the groups defined in the LineGroup definition csv file.

To change the LineGroups definition file

1.  Go to the preferences tab *[General](TechDraw_Preferences#General.md)*.
2.  Select in the field **Line Group File** a LineGroup definition file.

### Personalizzare i gruppi di linee 

Se si hanno i permessi di scrittura si può modificare `LineGroup.csv` per aggiungere altri Gruppi di linee (LineGroup).

Questo file in genere è in:


```python
$INSTALL_DIR/Mod/TechDraw/LineGroup/LineGroup.csv
```

Dove `$INSTALL_DIR` è la directory in cui è stato installato FreeCAD, per esempio


```python
/usr/share/freecad/Mod/TechDraw/LineGroup/LineGroup.csv
```

È possibile specificare i valori predefiniti preferiti nelle [Preferenze di TechDraw](TechDraw_Preferences/it.md).

## Prcorso del file LineGroup 

-   **Windows**: `C:\Program Files\FreeCAD\data\Mod\TechDraw\LineGroup\`
-   **Mac**: `/Applications/FreeCAD.app/Contents/Mod/TechDraw/LineGroup/`
-   **Linux**: `/usr/share/freecad/Mod/TechDraw/LineGroup/`
    -   ***freecad-daily PPA***: `/usr/share/freecad-daily/Mod/TechDraw/LineGroup/`

Nota: È stata aggiunta una nuova preferenza per consentire all\'utente di utilizzare il proprio file Gruppo di linee personale.


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


<div class="mw-translate-fuzzy">

## Note


</div>


<div class="mw-translate-fuzzy">

-   Il nome del LineGroup (ex FC 0,25mm) deve essere inserito esattamente come specificato nel file CSV.
-   La larghezza della linea in TechDraw è sempre specificata in mm, anche quando si utilizzano altri sistemi di unità.


</div>


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
