---
 GuiCommand:
   Name: Part_RefineShape
   Name/it: Part Affina forma
   MenuLocation: Parte , Crea una copia , Affina forma
   Workbenches: Part_Workbench/it
   SeeAlso: 
---

# Part RefineShape/it



## Descrizione

Il comando <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> **Part Affina forma** crea copie parametriche con una forma affinata dagli oggetti selezionati. Rimuove i bordi non necessari da facce piane e cilindriche.

![](images/PartRefineShape_it.png ) 
*Originale con 11 facce (a sinistra) e copia affinata con 7 facce (a destra).*



## Utilizzo

1.  Seleziona uno o più oggetti.
2.  Seleziona l\'opzione **Parte → Crea una copia → <img src="images/Part_RefineShape.svg" width=16px> Affina forma** dal menu.
3.  Per ogni oggetto viene creata una copia parametrica ripulita
4.  Gli oggetti originali sono nascosti.



## Note

-   Questo comando può essere utilizzato come ultimo passaggio in un flusso di lavoro tradizionale di [geometria solida costruttiva](constructive_solid_geometry/it.md).
-   Potrebbe essere utile ripulire il modello prima di applicare altre funzionalità, come [raccordi](Part_Fillet/it.md).
-   La pulizia di un oggetto può impedire alle stampanti 3D di stampare bordi indesiderati una volta che l\'oggetto viene esportato in un formato mesh.
-   Questo comando può essere utilizzato anche dopo aver convertito una mesh in una forma ([Part Forma da mesh](Part_ShapeFromMesh/it.md)).
-   Per impostazione predefinita, questo comando crea copie parametriche (collegate). Esiste il parametro [fine-tuning](Fine-tuning/it.md) per modificarlo in copie non parametriche. Maggiori informazioni sul comportamento della copia parametrica/non parametrica possono essere trovate sul forum in questa discussione [1](https://forum.freecad.org/viewtopic.php?t=42993).
-   Alcune informazioni interessanti su ciò che accade con il posizionamento e su come accedere tramite Python possono essere trovate sul forum in questa discussione [2](https://forum.freecad.org/viewtopic.php?t=77568#p675456).



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Part Affina Forma deriva da un oggetto [Funzione Part](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Refine}}

-    **Source|Link**: specifica il collegamento alla la forma sorgente.



## Script

Il comando Pyhton per ripulire una forma è il seguente:


```python
shape.removeSplitter()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/it
