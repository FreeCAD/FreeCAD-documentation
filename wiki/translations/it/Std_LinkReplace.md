---
 GuiCommand:
   Name: Std LinkReplace
   Name/it: Sostituisci con il link
   MenuLocation: Nessuna
   Workbenches: Tutti
   Version: 0.19
   SeeAlso: Std_LinkMake/it, Std_LinkMakeRelative/it, Std_LinkUnlink/it
---

# Std LinkReplace/it

## Descrizione


**Lo strumento [<img src=images/Std_LinkReplace.svg style="width:16px"> [Sostituisci con il link](Std_LinkReplace/it.md)**

sostituisce un oggetto all\'interno di un altro con una versione [App Link](App_Link/it.md) del primo oggetto.

Questa operazione agisce sui \"figli\" di un oggetto \"genitore\" come si vede nella [vista ad albero](tree_view/it.md). Ad esempio, dati due oggetti (A e B) che partecipano a una **[<img src=images/Part_Boolean.svg style="width:16px"> [operazione booleana](Part_Boolean/it.md)**, ad esempio C = A + B, l\'oggetto A può essere sostituito da un link, in modo che C = A_link + B.

Questa operazione può essere eseguita per sostituire con un link gli oggetti nidificati che si trovano in un [assemblaggio](assembly/it.md) complesso, il che può essere più efficiente se l\'oggetto nidificato viene utilizzato molte volte in diversi sottoassiemi. L\'operazione inversa è **[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Annulla il link](Std_LinkUnlink/it.md)**. Per creare un link generico vedere **[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea un link](Std_LinkMake/it.md)**.

## Utilizzo

1.  Assicurarsi di avere un oggetto all\'interno di un altro. Ad esempio, si consideri che è stata realizzata una **[<img src=images/Part_Fuse.svg style="width:16px"> [Unione](Part_Fuse/it.md)** con due oggetti creati in precedenza, una **[<img src=images/Part_Sphere.svg style="width:16px"> [sfera](Part_Sphere/it.md)** e un **[<img src=images/Part_Cylinder.svg style="width:16px"> [cilindro](Part_Cylinder/it.md)**.
2.  Selezionare la <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [sfera](Part_Sphere/it.md) nella [vista ad albero](tree_view/it.md).
3.  Premere **[<img src=images/Std_LinkReplace.svg style="width:16px"> [Sostituisci con il link](Std_LinkReplace/it.md)**.

L\'originale <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [Sfera](Part_Sphere/it.md) deve ora essere al di fuori del **[<img src=images/Part_Fuse.svg style="width:16px"> [Unione](Part_Fuse/it.md)**, e all\'interno ci deve essere invece un Link (una piccola freccia in sovraimpressione viene visualizzata nell\'icona).

![](images/Std_Link_tree_replace_fuse_1_example.png ) ![](images/Std_Link_tree_replace_fuse_2_example.png )



*Un oggetto all'interno di un altro viene sostituito da un link; ora il link è all'interno e l'oggetto reale è posizionato all'esterno.*

Questo può essere fatto anche con oggetti contenuti all\'interno di {{button|[<img src=images/Std_Part.svg style="width:16px"> [Parti](Std_Part/it.md)}} e {{button|[<img src=images/Std_Group.svg style="width:16px"> [Gruppi](Std_Group/it.md)}}.

![](images/Std_Link_tree_replace_part_1_examples.png ) ![](images/Std_Link_tree_replace_part_2_examples.png )



*Un oggetto all'interno di un contenitore viene sostituito da un link; ora il link è all'interno e l'oggetto reale è posizionato all'esterno.*

## Proprietà

Questo comando crea un nuovo [App Link](App_Link/it.md); le sue proprietà sono descritte in {{button|[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea un link](Std_LinkMake/it.md)}}.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkReplace/it
