# Path Helix/it
---
- GuiCommand:   Name:Path Helix   Name/it:Elica   Workbenches:[[Path Workbench/it   Path]]|MenuLocation:Path - Elica   Shortcut:   SeeAlso:---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Il comando Elica aggiunge un\'operazione di interpolazione elicoidale al lavoro. Comandi G-Code dell\'uscita di interpolazione dell\'elica in senso orario (G2). Comandi G-Code dell\'uscita in senso antiorario (G3). La percentuale di passaggio sopra specifica lo spostamento concentrico come percentuale del diametro dello strumento.


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

-   Selezionare lo strumento Helix dal Path-\>menu dal pulsante GUI e premere.
-   Scegli un controller Tool dalla finestra di dialogo di selezione pop-up e conferma premendo OK.
-   Tutti i fori disponibili nel modello di lavoro saranno disponibili per l\'elaborazione, elencati nella scheda Geometria di base. Confermare che l\'elenco corrisponda ai fori destinati all\'elaborazione e regolare aggiungere, abilitare o disabilitare, se necessario. I fori possono essere aggiunti selezionando le facce dei muri dei fori.
-   Assicurati che le profondità, la profondità finale siano corrette, e aggiusta se non.
-   Assicurarsi che Altezze, Alette di sicurezza e distanze siano corrette e regolate in caso contrario.
-   Nella scheda Operazione, specificare Start From, Direction, e Step Over percentuale.


</div>

## Options

Extra Offset adds a margin of material to be left unmachined. This is typically to allow a light finishing pass as a separate operation.

## Comments

-   Step Down is not respected exactly. It is always rounded to give a complete number of turns from Start Depth to Final Depth.
-   Similarly Step Over is not respected exactly. It is always rounded to give a number of equal steps.

The feedrate parameter is constant across all cuts and is based on the position of the tool\'s axis, thus actual feedrate of the cutting edge of the tool can vary considerably between the inner most cut and the outside surface. If the job dimensions produce a path diameter smaller than the tool diameter, this can lead to much faster cutting speeds than the feedrate given for the tool in the tool controller. This may need to considered when selecting \"feed and speeds\" for the job.

## Properties

### Data

Empty

### View

Empty

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example:


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Helix/it
