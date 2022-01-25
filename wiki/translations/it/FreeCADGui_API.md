# FreeCADGui API/it
**(Ottobre 2019) Non modificare queste pagine. Le informazioni sono incomplete e obsolete. Per l'API più recente, consultare la [https://www.freecadweb.org/api documentazione API autogenerata] o generare la documentazione autonomamente. Vedere [Documentazione del codice sorgente](Source_documentation/it.md).**

Questo modulo è la controparte del modulo FreeCAD. Contiene tutto ciò che riguarda l\'interfaccia utente e le viste 3D. Esempio: 
```python
import FreeCAD as App
import FreeCADGui as Gui

# get the 3D model document
doc = App.ActiveDocument    

# get the visual representation model document
gui_doc = Gui.ActiveDocument

gui_doc.activateWorkbench("myWorkbench")
```


{{APIFunction|activateWorkbench|string|Attiva un ambiente di lavoro per nome|nulla}}


{{APIFunction|activeDocument| | |il documento attivo o Nulla se non esiste}}


{{APIFunction|activeWorkbench| | |l'oggetto workbench attivo}}


{{APIFunction|addCommand|string, object|Aggiunge un comando di FreeCAD. String è il nome del comando e object è il nome della classe che definisce il comando| }}


{{APIFunction|addIcon|string, string or list|Aggiunge al sistema un'icona come nome del file o in formato XPM| }}


{{APIFunction|addIconPath|string|Aggiunge al sistema un nuovo percorso per trovare i file di icone| }}


{{APIFunction|addPreferencePage|string,string|Aggiunge un modulo di interfaccia utente per la finestra delle preferenze. Il primo argomento specifica il nome del file e il secondo indica il nome del gruppo| }}


{{APIFunction|addWorkbench|string, object|Aggiunge un ambiente di lavoro con un nome definito. La stringa è il nome del banco di lavoro e l'oggetto è il nome della classe che definisce l'ambiente| }}


{{APIFunction|createDialog|string|Apre un file UI, Interfaccia Utente| }}


{{APIFunction|getDocument|string|Ottiene un documento con il suo nome|il documento}}


{{APIFunction|getWorkbench|string|Ottiene un ambiente di lavoro con il suo nome |l'ambiente}}


{{APIFunction|insert|string|Apre una macro, un file Inventor o VRML|il documento}}


{{APIFunction|listWorkbenches| |Mostra un elenco di tutti gli ambienti di lavoro|una lista}}


{{APIFunction|open|string|Apre un file macro, Inventor o VRML|il documento aperto}}


{{APIFunction|removeWorkbench|string|Rimuove un ambiente di lavoro per nome| }}


{{APIFunction|runCommand|string|Esegue un comando di FreeCAD per nome| }}


{{APIFunction|updateGui| |Aggiorna la finestra principale e tutte le sue finestre| }}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > FreeCADGui API/it
