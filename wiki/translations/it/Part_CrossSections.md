---
 GuiCommand:
   Name: Part SectionCross
   Name/it: Part Sezioni
   MenuLocation: Parte , Sezioni...
   Workbenches: Part_Workbench/it
   SeeAlso: Part_Section/it
---

# Part CrossSections/it



## Descrizione

L\'utilità **Sezioni** crea una o più sezioni attraverso la forma selezionata, parallele ad uno dei piani globali predefiniti (XY, XZ o YZ).



## Utilizzo

1.  Selezionare una forma.
2.  Premere il pulsante **[<img src=images/Part_CrossSections.svg style="width:24px"> '''Sezioni...'''**.
3.  Definire il piano guida.
4.  Definire la posizione (altezza della sezione trasversale).
5.  Facoltativamente, selezionare **Sezioni** per creare più di una sezione trasversale:
    -   Selezionando \"Su entrambi i lati\" le sezioni trasversali sono distribuite su ciascun lato della posizione del piano di guida.
    -   Impostare il numero di sezioni.
6.  Premere **OK**.



## Note

-   Gli oggetti [App Link](App_Link/it.md) collegati ai tipi di oggetto appropriati e i contenitori [App Part](App_Part/it.md) con gli oggetti visibili appropriati all\'interno possono essere utilizzati anche come oggetti di origine. {{Version/it|0.20}}
-   L\'oggetto risultante non è parametrico, cioè non è legato alla forma originale.
-   Viene creato un singolo oggetto, anche con più di una sezione trasversale.



## Esempio

![Selezionare un oggetto](images/SectionCross1.png )

![Finestra di dialogo](images/SectionCross2.png )

![Risultato](images/SectionCross3.png )





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CrossSections/it
