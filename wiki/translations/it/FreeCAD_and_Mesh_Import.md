# FreeCAD and Mesh Import/it
## Post-Import 


<div class="mw-translate-fuzzy">

## Operazioni dopo l\'importazione 

Dopo l\'importazione, per FreeCAD, il modello è solo un insieme di facce. Si potrebbe desiderare di convertire il modello in una forma riconoscibile e modificabile da FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Per fare questo:

1.  Passare nel\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/it.md)
2.  Selezionare la mesh e andare in **Part → [Crea forma da mesh](Part_ShapeFromMesh/it.md)** o premere il pulsante <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:24px;"> [Forma da mesh](Part_ShapeFromMesh/it.md)
3.  Cliccare **OK** nel dialogo
4.  Selezionare la forma appena creata
5.  Andare in **Part → [Converti in solido](Part_MakeSolid/it.md)**
6.  Selezionare il solido appena creato
7.  Andare in **Part → [Affina forma](Part_RefineShape/it.md)** o premere il pulsante <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Affina forma](Part_RefineShape/it.md)


</div>

**Nota:** L\'ultimo passaggio non è obbligatorio, ma serve a pulire il solido della maggior parte dei bordi residui rimasti sulle superfici piane e cilindriche.



## Errori

### \"cannot convert because shape is not a shell\" 


<div class="mw-translate-fuzzy">

### Ottengo il messaggio di errore \"cannot convert because shape is not a shell\" ! E adesso? 

Il guscio (shell dell\'oggetto mesh) sembra avere degli errori, forse non è chiuso (ha dei buchi). Dato che le capacità dell\'ambiente mesh di FreeCAD per ora sono un po\' limitate, si potrebbe desiderare di provare ad esaminare e riparare il modello con un software di terze parti. Dopo aver fatto questo, si può di nuovo provare a importare e trasformare il modello.


</div>




<div class="mw-translate-fuzzy">

## Programmi di terza parte 

-   [Meshlab](http://meshlab.sourceforge.net/)
    -   Licenza: Open Source (GPL V2)
    -   Funziona su Windows 32/64 bit, Linux e Mac OS X


</div>


<div class="mw-translate-fuzzy">

-   [netFabb basic](http://www.netfabb.com/downloadcenter.php?basic=1)
    -   Licenza: Freeware
    -   Funziona su Windows XP/7/8, Linux e Mac OS X


</div>

## Tutorials


<div class="mw-translate-fuzzy">

## Tutorial

-   [Importare da STL o OBJ](Import_from_STL_or_OBJ/it.md)
-   [Esportare in STL o OBJ](Export_to_STL_or_OBJ/it.md)


</div>



## Correlazioni

-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and Mesh Import/it
