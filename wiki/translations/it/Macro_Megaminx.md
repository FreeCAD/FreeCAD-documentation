# Macro Megaminx/it
{{Macro
|Name=Macro_Megaminx
|Name/it=Macro Megaminx
|Icon=Macro_Megaminx.png
|Description=Questa macro crea un Megaminx virtuale [https://en.wikipedia.org/wiki/Megaminx Megaminx].
|Author=aleph0
|SeeAlso=[Macro Rubik Cube](Macro_Rubik_Cube/it.md)
|Date=2019-02-17
|FCVersion=0.18 and higher
|Download=[https://www.freecadweb.org/wiki/images/4/43/Macro_Megaminx.png ToolBar Icon]
}}



## Descrizione

Questa macro crea un documento di FreeCAD contenente un [Megaminx](https://en.wikipedia.org/wiki/Megaminx) virtuale e consente di manipolarlo. Mostra sei viste del Megaminx includendo ciascuna delle dodici facce almeno una volta. Ci sono varie frecce (ognuna con un tooltip che verrà visualizzato quando ci si passa sopra con il mouse). Cliccando sulle frecce si può ruotare le facce del Megaminx, ruotare l\'intero Megaminx, oppure ruotare o riflettere la cronologia che mantiene le rotazioni che sono state fatte. C\'è anche un menu Megaminx che viene mostrato a destra della barra dei menu purché si abbia almeno un documento Megaminx aperto. Dal menu è possibile visualizzare del testo di aiuto, ripristinare il Megaminx al suo stato iniziale (risolto), annullare l\'ultima rotazione (e rimuoverla dalla cronologia), copiare la cronologia negli appunti, scorrere la cronologia, randomizzare il Megaminx, e abilitare o disabilitare l\'eco delle rotazioni nella visualizzazione report. Tutte queste funzioni possono anche essere richiamate digitando gli appositi comandi nella finestra della console Python.

La cronologia salvata negli appunti può essere incollata nella finestra della console Python o copiata in un file che può essere richiamato come macro nel documento Megaminx attivo. Si può avere più di uno Documento Megaminx aperto alla volta, ma solo uno può essere attivo.

## Script

ToolBar icon <img alt="" src=images/Macro_Megaminx.png  style="width:64px;">


{{Codeextralink|https://raw.githubusercontent.com/rparkins999/Megaminx/master/Megaminx.FCMacro}}

**Macro_Megaminx.FCMacro**

![](images/Macro_Megaminx.png )






## Utilizzo

Scaricare il codice da <https://github.com/rparkins999/Megaminx> nella directory delle macro. Eseguire la macro per creare un documento Megaminx. Una volta creato ci si può giocare. Le funzioni di cronologia possono essere utilizzate per costruire e salvare operatori (ovvero algoritmi) che eseguono trasformazioni utili su Megaminx. Un insieme adeguato di queste funzioni ti fornirà una soluzione completa. La funzione step_history può essere utilizzata per aiutarti ad applicare un operatore su un vero Megaminx.



---
⏵ [documentation index](../README.md) > Macro Megaminx/it
