---
- GuiCommand:/it
   Name:TechDraw_SpreadsheetView
   Name/it:Vista di foglio di calcolo
   MenuLocation:TechDraw → Vista di foglio di calcolo
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Foglio di calcolo](Spreadsheet_Workbench/it.md)
---

# TechDraw SpreadsheetView/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento ti consente di posizionare una vista di un [foglio di calcolo](Spreadsheet_Workbench/it.md) selezionato in una [Pagina](TechDraw_Workbench/it.md).


</div>

![](images/TechDraw_Spreadsheetview.png ) 
*Elemento Figlio di calcolo inserito nella pagina di disegno TechDraw*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Nell\'albero, selezionare un foglio di calcolo che si desidera mettere su un foglio di disegno
2.  Premere il pulsante **<img src="images/TechDraw_SpreadsheetView.svg" width=16px> [Vista foglio di calcolo](TechDraw_SpreadsheetView.md)
**


</div>

## Notes

-   In {{VersionMinus|0.19}} some characters in spreadsheet cells will cause errors when displayed in a Spreadsheet View. These characters have to be XML encoded. Currently known characters are: {{Incode|&}} (replace with {{Incode|&amp;amp;}}) and {{Incode|&lt;}} (replace with {{Incode|&amp;lt;}}). See also this [discussion](https://forum.freecadweb.org/viewtopic.php?p=629853#p629885) in the forum.



## Proprietà

See also [TechDraw View](TechDraw_View#Properties.md).

### Data


{{TitleProperty|Spreadsheet}}


<div class="mw-translate-fuzzy">

-    **Source**: Il foglio di calcolo da aggiungere alla pagina

-    **Cell Start**: La cella in alto a sinistra dell\'intervallo di celle da includere in questa vista

-    **Cell End**: La cella in basso a destra dell\'intervallo di celle da includere in questa vista

-    **Font**: Il nome del carattere utilizzato per i testi

-    **Color**: Il colore delle linee e dei testi che non hanno colori specificati nel foglio di calcolo

-    **Font Size**: La dimensione del carattere dei testi

-    **Line Width**: La larghezza dei bordi delle celle


</div>


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/it
