---
 GuiCommand:
   Name: Spreadsheet SetAlias
   Name/it: Spreadsheet Alias
   MenuLocation: -
   Workbenches: Spreadsheet_Workbench/it
   Shortcut: **Ctrl**+**Shift**+**A**
   Version: 0.17
---

# Spreadsheet SetAlias/it



## Descrizione

Lo strumento <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> **Spreadsheet Alias** apre una finestra di dialogo per impostare un alias per una cella. Invece di utilizzare il nome esatto della cella come A2, B3 o C4, è possibile utilizzare un nome personalizzato.



## Utilizzo

1.  Assicurarsi che ci sia un [foglio di calcolo](Spreadsheet_CreateSheet/it.md) attivo.
2.  Selezionare una cella.
3.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **[<img src=images/Spreadsheet_SetAlias.svg style="width:16px"> [Alias](Spreadsheet_SetAlias/it.md)**.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**Shift**+**A**.
4.  Inserire un alias:
    -   Solo caratteri alfanumerici e underscore (da `A` a `Z`, da `a` a `z`, da `0` a {{ incode\|9}} e `_`) sono consentiti.
    -   Il primo carattere deve essere una lettera.
    -   L\'utilizzo di 1 o 2 lettere maiuscole seguite da 1 a 5 numeri, ad esempio `AB123`, non è consentito poiché questo è considerato un indirizzo di cella.
    -   Le sequenze di caratteri che sono unità di misura non sono consentite. Ad esempio `W` è un alias non valido in quanto è l\'unità di misura del [Watt](https://en.wikipedia.org/wiki/Watt). Poiché FreeCAD supporta molte unità di misura, è meglio evitare alias brevi. Vedere [Espressioni](Expressions/it#Unità.md).
    -   L\'uso delle costanti matematiche `pi` e `e` come alias può portare ad errori e dovrebbe essere evitato.
    -   Non utilizzare spazi negli alias poiché porteranno anche a errori.





{{Spreadsheet_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Spreadsheet](Spreadsheet_Workbench.md) > Spreadsheet SetAlias/it
