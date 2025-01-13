---
 GuiCommand:
   Name: Part Section
   Name: Part Seziona
   MenuLocation: Parte , Seziona
   Workbenches: Part_Workbench/it
   SeeAlso: Part_CrossSections/it
---

# Part Section/it



## Descrizione

Il comando <img alt="" src=images/Part_Section.svg  style="width:24px;"> **Part Seziona** restituisce la geometria delle linee di intersezione di due oggetti. Il risultato è completamente parametrico.

-   Un\'intersezione di due solidi/facce dà come risultato una o più linee di sezione.
-   Un\'intersezione di due linee, o di una linea e di un solido/faccia, dà come risultato uno o più punti.

![](images/PartSection1_it.png ) 
*Un cubo sezionato con un cilindro*



## Utilizzo

1.  Selezionare due oggetti.
2.  Il primo oggetto sarà il **Base** della Sezione, ma l\'ordine di selezione non ha alcun impatto sul risultato.
3.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **![](images/)_[Seziona](Part_Section/it.md)**.
    -   Selezionare l\'opzione **Parte → ![](images/)_Seziona**_dal_menu.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Part Seziona deriva da un oggetto [Part Feature](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{Properties_Title|Base}}

-    **Base|Link**: collegamento al primo oggetto.

-    **Tool|Link**: collegamento al secondo oggetto.


{{Properties_Title|Boolean}}

-    **History|ShapeHistory|hidden**: \"Cronologia delle forme\".

-    **Refine|Bool**: \"Perfeziona la forma (ripulisci i bordi ridondanti) dopo questa operazione booleana\". Il valore predefinito è determinato dalla preferenza **Perfeziona automaticamente il modello dopo l'operazione basata su schizzo**. Vedere [Preferenze PartDesign](PartDesign_Preferences/it#Generale.md).


{{Properties_Title|Section}}

-    **Approximation|Bool**: approssima i bordi di output.



## Link

Per creare sezioni con un piano di sezione vedere <img alt="" src=images/Part_CrossSections.svg  style="width:16px;"> [Sezioni](Part_CrossSections/it.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Section/it
