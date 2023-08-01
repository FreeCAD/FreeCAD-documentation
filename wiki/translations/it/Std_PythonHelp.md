---
- GuiCommand:
   Name:Std PythonHelp
   Name/it:Documentazione dei moduli Python
   MenuLocation:Aiuto - Documentazione automatica dei moduli Python
   Workbenches:Tutti
   SeeAlso:[Documentazione di scripting Python](Std_FreeCADPowerUserHub/it.md)
---

# Std PythonHelp/it



## Descrizione

Il comando **Documentazione automatica dei moduli Python** avvia un server Web che comunica con il browser Internet predefinito del sistema tramite un socket locale. Il server Web visualizza le informazioni sui moduli [Python](Python/it.md) disponibili, le classi e le funzioni di FreeCAD. Le pagine richieste vengono generate automaticamente.

Il web server è basato sul modulo [pydoc](https://docs.python.org/3.8/library/pydoc.html#module-pydoc) di Python, e quindi estrae le docstring dei file Python (`.py` ) e la documentazione testuale definita nei wrapper Python (`.xml`) che espongono il codice C++ sottostante.



## Utilizzo

1.  Selezionare l\'opzione **Aiuto → <img src="images/Std_PythonHelp.svg" width=16px> Documentazione automatica dei moduli Python** dal menu.
2.  Fare clic su uno dei collegamenti per accedere alla documentazione di una classe o funzione specifica.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std PythonHelp/it
