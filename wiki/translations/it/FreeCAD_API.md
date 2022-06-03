# FreeCAD API/it
**(Ottobre 2019) Non modificare queste pagine. Le informazioni sono incomplete e obsolete. Per l'API più recente, consultare la [https   *//www.freecadweb.org/api documentazione API autogenerata] o generare la documentazione autonomamente. Vedere [Documentazione del codice sorgente](Source_documentation/it.md).**

Questo è il modulo principale (root) di FreeCAD. Può anche essere chiamato con \"App\" dall\'interprete FreeCAD. Contiene tutto quello che serve per manipolare i documenti e il loro contenuto (oggetti).

Esempio   * 
```python
import FreeCAD
print FreeCAD.listDocuments()
mydoc = FreeCAD.activeDocument()
```


<div class="mw-translate-fuzzy">


{{APIFunction|ConfigDump| |Stampa un dizionario contenente tutto l'ambiente di configurazione di FreeCAD.| }}


{{APIFunction|ConfigGet|[string]|Restituisce il valore della chiave data. Se non si specifica nessuna chiave, viene restituita la configurazione completa|Una stringa.}}


{{APIFunction|ConfigSet|string, string|Imposta la chiave data (prima stringa) al valore dato (seconda stringa).| }}


{{APIFunction|Version| |Stampa la versione di FreeCAD.| }}


{{APIFunction|activeDocument| |Restituisce il documento attivo o Nulla se non vi è alcun documento attivo.|Un documento di FreeCAD.}}


{{APIFunction|addExportType|string, string|Aggiunge a FreeCAD un nuovo tipo di file di esportazione. La prima stringa deve essere formattata come in questo esempio   * "Documento di Word (*.doc)". La seconda stringa è il nome di uno script / modulo python che contiene una funzione export().| }}


{{APIFunction|addImportType|string, string|Aggiunge a FreeCAD un nuovo tipo di file importazione, funziona allo stesso modo di addExportType, il modulo di gestione python deve contenere una funzione open() e/o una funzione import().| }}


{{APIFunction|closeDocument|Document name|Chiude un dato documento| }}


{{APIFunction|getDocument|Document name|Restituisce un documento o solleva un'eccezione se non vi è alcun documento con il nome dato.| }}


{{APIFunction|getExportType|string|Restituisce il nome del modulo che può esportare il tipo di file specificato.| Una stringa.}}


{{APIFunction|getImportType|string|Restituisce il nome del modulo che può importare il tipo di file specificato.|Una stringa.}}


{{APIFunction|listDocuments| |Restituisce un dizionario di nomi e di puntatori di oggetti di tutti i documenti.|Un dizionario di nomi e di puntatori di oggetti.}}


{{APIFunction|newDocument|[string]|Crea e restituisce un nuovo documento con un determinato nome. Il nome del documento deve essere univoco, e viene controllato automaticamente. Se non viene fornito nessun nome, il documento sarà "Senza titolo".|Il documento appena creato.}}


{{APIFunction|open|string|Vedere openDocument| }}


{{APIFunction|openDocument|filepath|Crea e restituisce un documento e carica un file di progetto nel documento. L'argomento stringa deve puntare ad un file esistente. Se il file non esiste o il file non può essere caricato viene generata una eccezione di I /O. In questo caso il documento creato viene mantenuto, ma sarà vuoto.|Il documento di FreeCAD aperto.}}


{{APIFunction|setActiveDocument|Document name|Imposta il documento attivo con il suo nome.| }}


</div>


 

[Category   *API](Category_API.md) [Category   *Poweruser Documentation](Category_Poweruser_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > FreeCAD API/it
