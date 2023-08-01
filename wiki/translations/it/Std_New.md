# Std New/it
---
- GuiCommand:   Name:Std_New   Name/it:Nuovo   MenuLocation:File → Nuovo   Workbenches:Tutti   Shortcut:**Ctrl**+**N**   SeeAlso:[Apri](Std_Open/it.md), [Importa](Std_Import/it.md)---

## Descrizione

Il comando **Nuovo** crea un nuovo documento vuoto e lo rende il documento attivo.

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_New.svg" width=16px> '''Nuovo'''**.
    -   Selezionare l\'opzione **File → <img src="images/Std_New.svg" width=16px> Nuovo** dal menu.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**N**.

## Preferenze

-   FreeCAD crea un nuovo documento all\'avvio se **Strumenti → Modifica parametri... → BaseApp → Preferenze → Documento → CreateNewDoc** è impostato su `True`. Questa impostazione può essere modificata anche nell\'[editor delle preferenze](Preferences_Editor/it#Documento.md).
-   Alcune proprietà del documento: nome dell\'autore, nome dell\'azienda e le informazioni sulla licenza, possono essere preimpostate nell\'[editor delle preferenze](Preferences_Editor/it#Documento.md).

## Proprietà

Molte proprietà possono anche essere modificate nella finestra di dialogo del comando [Informazioni sul progetto](Std_ProjectInfo/it.md).

-    **Comment**: Qualsiasi commento applicabile.

-    **Company**: Nome della ditta. **Può essere preimpostato**.

-    **Created By**: Nome dell\'autore. **Può essere preimpostato**.

-    **Creation Date**: Data automatica. **Non modificabile**.

-    **File Name**: Il percorso completo del file. Vuoto se il documento non è stato salvato. **Non modificabile**.

-    **Id**: Non ancora implementato.

-    **Label**: Il nome che apparirà nella [vista ad albero](Tree_view/it.md). Di default, il nome del documento.

-    **Last Modified By**: Nome dell\'autore. **Può essere preimpostato**.

-    **Last Modified Date**: Data automatica. **Non modificabile**.

-    **License**: Tipo di licenza. **Può essere preimpostato**.

-    **License URL**: URL della licenza. **Può essere preimpostato**.

-    **Show Hidden**: Se vero, gli elementi che sono stati nascosti nella [vista ad albero](Tree_view/it.md) verranno comunque visualizzati. Nascondere gli oggetti nell\'albero può essere utile quando si lavora su modelli molto grandi.

-    **Tip**: Non ancora implementato.

-    **Tip Name**: Non ancora implementato.

-    **Transient Dir**: La directory temporanea utilizzata per i dati di recupero. **Non modificabile**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per creare un nuovo documento usa il metodo `newDocument([name], [hidden<nowiki>=</nowiki>False])` dell\'applicazione FreeCAD. Il nome del documento deve essere univoco, che viene verificato automaticamente. Se non viene fornito alcun nome, il documento sarà denominato \"Senza titolo\". Se viene utilizzato `hidden<nowiki>=</nowiki>True`, il nuovo documento non verrà visualizzato nella GUI e non verrà visualizzata alcuna scheda.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'test.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveAs(fnm)

FreeCAD.closeDocument(doc.Name)

doc = FreeCAD.open(fnm)
doc.save()

FreeCAD.closeDocument(doc.Name)
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std New/it
