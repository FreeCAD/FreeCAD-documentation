 {{Macro/it
|Name=Macro_Megaminx
|Name/it=Macro Megaminx
|Icon=Macro_Megaminx.png
|Description=Questa macro crea un Megaminx virtuale
|Author=aleph0
|SeeAlso=[Macro Rubik Cube](Macro_Rubik_Cube/it.md)
|Date=2019-02-17
|FCVersion=0.18 and higher
|Download=[https://www.freecadweb.org/wiki/images/4/43/Macro_Megaminx.png ToolBar Icon]
}}

## Descrizione

Questa macro crea un documento di FreeCAD contenente una Megaminx virtuale (vedi <https://en.wikipedia.org/wiki/Megaminx>) e ti consente di farlo manipolarlo. Visualizza sei viste del Megaminx incluso ciascuno delle dodici facce almeno una volta. Ci sono varie frecce (ognuna con una descrizione comandi che verrà visualizzata finché si passa con il mouse passarci sopra con il mouse). Facendo clic sulle frecce è possibile ruotare le facce di Megaminx, ruota l\'intera Megaminx o ruota o riflette la cronologia che mantiene delle rotazioni che hai fatto finora. Là è anche un menu Megaminx che viene mostrato a destra della barra dei menu purché sia ​​aperto almeno un documento Megaminx. Dal menu è possibile visualizzare un testo di aiuto, ripristinare il Megaminx al suo stato iniziale (risolto), annullare l\'ultima rotazione (e rimuoverlo da la cronologia), copia la cronologia negli appunti, passa attraverso cronologia, randomizza Megaminx e abilita o disabilita l\'eco di rotazioni alla vista report. Tutte queste funzioni possono anche essere invocato digitando i comandi appropriati nella finestra della console di Python.

Una cronologia salvata negli Appunti può essere incollata in Python finestra della console o copiata in un file che può essere chiamato come macro nel documento Megaminx attivo. Puoi averne più di uno Documento Megaminx aperto alla volta, anche se solo uno può essere attivo.

## Script


{{Codeextralink|https://raw.githubusercontent.com/rparkins999/Megaminx/master/Megaminx.FCMacro}}

ToolBar icon <img alt="" src=images/Macro_Megaminx.png  style="width:64px;">

**Macro\_Megaminx.FCMacro**

![](images/Macro_Megaminx.png )




## Utilizzo

Scarica il codice da <https://github.com/rparkins999/Megaminx> nella tua macro directory. Esegui la macro su creare un documento Megaminx. Quindi puoi giocarci. È possibile utilizzare le funzioni della cronologia costruire e salvare operatori (ovvero algoritmi) che apportano utili trasformazioni su Megaminx. Un set adatto di questi ti darà una soluzione completa. Step\_history La funzione può essere utilizzata per aiutarti a riprodurre un operatore su un vero Megaminx.
