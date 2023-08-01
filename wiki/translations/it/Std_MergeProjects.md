---
- GuiCommand:/it
   Name:Std_MergeProjects
   Name/it:Unisci progetti
   MenuLocation:File → Unisci progetti...
   Workbenches:Tutti
---

# Std MergeProjects/it



## Descrizione

Il comando **Unisci progetti** aggiunge il contenuto di un file FreeCAD nel documento attivo.



## Utilizzo

1.  Selezionare l\'opzione **File → <img src="images/Std_MergeProjects.svg" width=16px> Unisci progetti...** dal menu.
2.  Selezionare un file FreeCAD nella finestra di dialogo.
3.  Premere il pulsante **Apri**.



## Opzioni

-   Premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.



## Note

-   Un progetto non può essere unito a se stesso, la selezione del file corrente non è consentita.
-   FreeCAD cambia automaticamente i nomi interni e, a seconda delle preferenze, le etichette degli oggetti per evitare conflitti di nomi.



## Preferenze

-   L\'ultima posizione del file utilizzato è memorizzata in: **Strumenti → Modifica parametri ... → BaseApp → Preferenze → Generale → FileOpenSavePath**.
-   Le etichette duplicate sono consentite se **Strumenti → Modifica parametri ... → BaseApp → Preferenze → Documento → DuplicateLabels** è impostato su `True`. Questa impostazione può essere modificata anche nell\'[editor delle preferenze](Preferences_Editor/it#Documento.md).

## Scripting


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per unire un progetto utilizzare il metodo {{Incode|mergeProject}} dell\'oggetto documento.


```python
import FreeCAD

FreeCAD.ActiveDocument.mergeProject("Path_to_FCStd_project_file")
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std MergeProjects/it
