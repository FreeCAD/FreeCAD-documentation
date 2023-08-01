---
- GuiCommand:/it   Name:Part SliceApart
   Name/it:Affetta in parti
   MenuLocation:Part → Dividi → Affetta in parti
   Workbenches:[Part](Part_Workbench/it.md)
   Version:0.18.15506
   SeeAlso:[Affetta in composto](Part_Slice/it.md), [Esplodi il composto](Part_ExplodeCompound/it.md)
---

# Part SliceApart/it


</div>

## Descrizione

Strumento per dividere le forme per intersezione con altre forme. Ad esempio, per un cubo e un piano, vengono creati due solidi. ![600px](images/Part_Slice_Demo.png)



* Nella figura sopra, i pezzi sono stati separati manualmente dopo l'operazione, per rendere visibili le singole parti.*

[Affetta in parti](Part_SliceApart/it.md) è uguale a <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Affetta in composto](Part_Slice/it.md) seguito da <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> [Esplodi composto](Part_ExplodeCompound/it.md). Mentre \"Affetta in composto\" è completamente parametrico e non crea problemi mentre il numero di pezzi cambia, \"Affetta in parti\" non aggiorna il numero di oggetti quando il numero di pezzi cambia. Entrambi creano la funzione parametrica Slice, che mette i pezzi tagliati in un composto, ma \"Affetta in parti\" esplode il composto risultante in oggetti separati.

Le forme di uscita occupano lo stesso spazio dell\'originale. Ma sono divise dove si intersecano con altre forme. I pezzi divisi sono pezzi individuali.

Per ulteriori informazioni, visitare la pagina [Affetta in composto](Part_Slice/it.md).

### Struttura ad albero di Affetta in parti 

Il comando Affetta una parte crea più di un solo oggetto affettato. Nell\'esempio seguente un cubo viene affettato da una faccia.

Vengono create le fette e per ogni fetta viene creato un [CompoundFilter](Part_CompoundFilter/it.md), quindi la stessa porzione è presente più volte, sotto ad ogni CompoundFilter. Tutti questi CompoundFilters sono uniti in un Composto.

![](images/Part_SliceApartTree.png )

## Esempio

-   Creare un puzzle: vedere i passaggi da 1 a 6 dell\'esempio [Affetta in composto](Part_Slice/it.md).

## Script

Lo strumento può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:

`BOPTools.SplitFeatures.makeSlice(name)`

Impostare la modalità su **split** per dividere in parti

-   Crea una funzione Slice vuota. Le proprietà \'Base\' e \'Tools\' devono essere assegnate esplicitamente, in seguito.
-   Restituisce l\'oggetto appena creato.

Slice può essere applicato anche a forme piane, senza la necessità di avere un document object, attraverso: 
```pythonBOPTools.SplitAPI.slice(base_shape, tool_shapes, mode, tolerance = 0.0)``` Questo può essere utile per creare delle funzioni personalizzate con script Python.

Esempio: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeSlice(name= 'Slice')
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tools = FreeCADGui.Selection.getSelection()[1:]
}}

Lo strumento è implementato in Python, vedere see **/Mod/Part/BOPTools/SplitFeatures.py** ([GitHub link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/SplitFeatures.py)) nella directory di installazione di FreeCAD.

## Note

Affetta in parti è stato introdotto in FreeCAD v0.18.15506. FreeCAD deve essere compilato con OCC 6.9.0 o successivo; in caso contrario, lo strumento non è disponibile.

## Video-Tutorials 

-   <https://www.youtube.com/watch?v=tzHkQaHgrfQ> : FreeCad 0.18 PART WB using SLICE and SLICE APART (English language), author: Ha Gei

-   <https://www.youtube.com/watch?v=JJAL5JmqqKQ> : FreeCAD Slice und Slice Apart und andere Tricks (German lanuage), author: Ha Gei


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part SliceApart/it
