---
- GuiCommand:/it
   Name:Std_SaveCopy
   Name/it:Salva una copia
   MenuLocation:File → Salva una copia...
   Workbenches:All
   SeeAlso:[Salva con nome](Std_SaveAs/it.md), [Salva](Std_Save/it.md)
---

# Std SaveCopy/it



## Descrizione

Il comando **Salva una copia** salva una copia del documento attivo con un nuovo nome di file.



## Utilizzo

1.  Selezionare **File →  <img src="images/Std_SaveCopy.svg" width=16px> Salva una copia...** nel menu.
2.  Immettere un nome per il file nella finestra di dialogo.
3.  Premere il pulsante **Salva**.



## Opzioni

-   Premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.



## Preferenze

-   L\'ultima posizione del file utilizzato viene memorizzata in: **Strumenti → Modifica parametri... → BaseApp → Preferences → General → FileOpenSavePath**.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per salvare una copia di un documento, utilizzare il metodo `saveCopy` dell\'oggetto documento.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'testCopy.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveCopy(fnm)
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SaveCopy/it
