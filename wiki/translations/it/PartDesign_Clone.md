---
- GuiCommand:/it
   Name:PartDesign Clone
   Name/it:PartDesign Clone
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:Part Design → Crea un clone
   Version:0.17
   SeeAlso:[Draft clone](Draft_Clone/it.md)
---

# PartDesign Clone/it


</div>

## Descrizione

**PartDesign Clone** crea una copia collegata di un oggetto selezionato che seguirà eventuali modifiche future all\'oggetto originale (tranne il posizionamento). Ad esempio, un caso d\'uso è quando si desidera eseguire una [operazione booleana](PartDesign_Boolean/it.md) su un oggetto creato in un altro ambiente. Sono accettati la maggior parte di tipi di oggetti, purché siano solidi singoli. Se si devono clonare più oggetti (ad es. dei Corpi) o un [Contenitore di Part](Std_Part/it.md), si può usare il [Clone di Draft](Draft_Clone/it.md). Notare che Part Design imposta il posizionamento del clone su zero (sia la traslazione cartesiana che gli orientamenti spaziali), mentre Draft calcola e imposta i valori numerici del posizionamento e dell\'orientamento correnti degli oggetti clonati rispetto al contenitore degli oggetti clonati.

![*Clone of the inner gear while being translated in 3D space as an independent object*](images/clone.png ) 
*Clone dell'ingranaggio interno mentre viene traslato nello spazio 3D come oggetto indipendente*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Nell\'albero del modello, selezionare l\'oggetto da clonare.
2.  Premere i pulsante **[<img src=images/PartDesign_Clone.svg style="width:24px"> '''Crea un clone'''**.


</div>

## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Base Feature}}: imposta l\'oggetto originale su cui si basa il clone. Per sostituirlo, premere il tasto **...** per ottenere l\'elenco degli oggetti disponibili.

-    {{PropertyData/it|Placement}}: definisce l\'orientamento e la posizione del Clone nello spazio 3D. Vedere [Posizionamento](Placement/it.md).

-    {{PropertyData/it|Label}}: etichetta data all\'oggetto Clone. Modificabile a piacere.


</div>

## Limitazioni


<div class="mw-translate-fuzzy">

-   Per un clone di PartDesign può essere usato solo un singolo oggetto.
-   Sono supportati solo gli oggetti costituiti da un singolo solido. Quindi, i [composti](Glossary#Compound.md) come i [contenitori di Part](Std_Part/it.md), i [composti di Part](Part_Compound/it.md) o le [schiere di Draft](Draft_Array/it.md) non sono supportati.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Clone/it
