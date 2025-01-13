---
 GuiCommand:
   Name: Part ReverseShape
   Name/it: ‏‎Part Inverti forma
‎   MenuLocation: Parte , Inverti forma
   Workbenches: Part_Workbench/it
---

# Part ReverseShape/it



## Descrizione

Il comando <img alt="" src=images/Part_ReverseShape.svg  style="width:24px;"> **Part Inverti forma** crea copie parametriche dagli oggetti selezionati con normali delle facce invertite.



## Utilizzo

1.  Selezionare uno o più oggetti.
2.  Selezionare l\'opzione **Parte → <img src="images/Part_ReverseShape.svg" width=16px> Inverti forme** dal menu.
3.  Per ciascun oggetto selezionato viene creata una forma invertita.



## Note

-   Gli oggetti [App Link](App_Link/it.md) collegati ai tipi di oggetto appropriati e i contenitori [App Part](App_Part/it.md) con gli oggetti visibili appropriati all\'interno possono essere utilizzati anche come oggetti di origine. {{Version/it|0.20}}
-   Per vedere l\'effetto del comando, modificare la proprietà **Lighting** della forma invertita in {{Value|On side}} e, se necessario, modificare **Modifica → Preferenze... → Visualizzazione → Vista 3D → Rendering → Colore di retroilluminazione**.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Part Inverti forma deriva da un oggetto [Funzione Part](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Reverse}}

-    **Source|Link**: specifica il collegamento alla la forma sorgente.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ReverseShape/it
