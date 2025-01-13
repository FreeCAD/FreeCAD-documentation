---
 GuiCommand:
   Name: TechDraw SpreadsheetView
   Name/it: TechDraw Vista di un foglio di calcolo
   MenuLocation: TechDraw , Viste da altri ambienti di lavoro , Vista di foglio di calcolo
   Workbenches: TechDraw_Workbench/it, Spreadsheet_Workbench/it
---

# TechDraw SpreadsheetView/it



## Descrizione

Lo strumento **TechDraw Vista di un Foglio di calcolo** consente di posizionare la visualizzazione di un [foglio di calcolo](Spreadsheet_Workbench/it.md) selezionato su una [Pagina](TechDraw_Workbench/it.md).


{{Version/it|1.0}}

: Anche lo strumento [TechDraw Vista](TechDraw_View/it.md) può creare una Vista Foglio di calcolo.

![](images/TechDraw_Spreadsheetview.png ) 
*Elemento Foglio di calcolo inserito nella pagina di disegno TechDraw*



## Utilizzo

1.  Selezionare un foglio di calcolo nella [Vista ad albero](Tree_view/it.md).
2.  Se nel documento sono presenti più pagine di disegno: facoltativamente aggiungere la pagina desiderata alla selezione selezionandola nella [Vista ad albero](Tree_view/it.md).
3.  Selezionare l\'opzione **TechDraw → Viste da altri ambienti di lavoro → <img src="images/TechDraw_SpreadsheetView.svg" width=16px> Inserisci Vista Foglio di calcolo** dal menu.
4.  Se nel documento sono presenti più pagine di disegno e se nessuna pagina è visualizzata nell\'[Area vista principale](Main_view_area/it.md) e non si ha ancora selezionato una pagina, si apre la finestra di dialogo **Scelta pagina**:
    1.  Selezionare la pagina desiderata.
    2.  Premere il pulsante **OK**.
5.  Viene inserita una Vista Foglio di calcolo.
6.  Regolare l\'intervallo di celle della vista modificando le sue proprietà **Cell Start** e **Cell End**.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Una Vista Foglio di calcolo, formalmente un oggetto {{Incode|TechDraw::DrawViewSpreadsheet}}, ha le [proprietà](TechDraw_View/it#Properties_Part_View.md) comuni a tutti i tipi di vista. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Drawing view}}

-    **Symbol|String|Hidden**: Il codice SVG che definisce questo simbolo.

-    **Testi modificabili|StringList|Hidden**: Valori di sostituzione per le stringhe modificabili in questo simbolo. Non utilizzato.

-    **Owner|Link**: Feature a cui è collegato questo simbolo. {{Version/it|1.0}}


{{TitleProperty|Spreadsheet}}

-    **Source|Link**: Il foglio di calcolo da aggiungere alla pagina.

-    **Cell Start|String**: La cella in alto a sinistra dell\'intervallo di celle da includere in questa visualizzazione.

-    **Cell End|String**: La cella in basso a destra dell\'intervallo di celle da includere in questa visualizzazione.

-    **Font|Font**: Il nome del carattere utilizzato per i testi.

-    **Text Color|Color**: Il colore di testi e linee per i quali non è specificato alcun colore nel foglio di calcolo.

-    **Text Size|Float**: La dimensione del carattere dei testi.

-    **Line Width|Float**: La larghezza dei bordi della cella.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/it
