---
- GuiCommand:
   Name: Std LinkUnlink
   Name/it: Annulla il link
   MenuLocation: Nessuna
   Workbenches: Tutti
   Version: 0.19
   SeeAlso: [Crea un link](Std_LinkMake/it.md), [Crea un link relativo](Std_LinkMakeRelative/it.md), [Sostituisci con un link](Std_LinkReplace/it.md)
---

# Std LinkUnlink/it

## Descrizione

Lo strumento **[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Annulla il link](Std_LinkUnlink/it.md)** è essenzialmente l\'operazione opposta a **[<img src=images/Std_LinkReplace.svg style="width:16px"> [Sostituisci con un link](Std_LinkReplace/it.md)**.

Questa operazione viene utilizzata per rimuovere un collegamento da un contenitore come **[<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)**, e posizionare invece l\'oggetto reale all\'interno.

## Utilizzo

1.  Assicurarsi di avere un link all\'interno di un contenitore, ad esempio, un link a una **[<img src=images/Part_Sphere.svg style="width:16px"> [sfera](Part_Sphere/it.md)** all\'interno di una **[<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)**.
2.  Selezionare il link interno nella [vista ad albero](tree_view/it.md).
3.  Premere **[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Annulla il link](Std_LinkUnlink/it.md)**.

L\'originale <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [Sfera](Part_Sphere/it.md) deve ora essere dentro **[<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)**, e il Link deve essere fuori. Ora questo collegamento può essere cancellato se non è più necessario, e non rovinerà il contenitore.

![](images/Std_Link_tree_replace_1_example.png ) ![](images/Std_Link_tree_unlink_1_example.png )



*Un link all'interno di un altro oggetto viene scollegato e l'oggetto reale viene invece posizionato all'interno.*

![](images/Std_Link_tree_replace_2_example.png ) ![](images/Std_Link_tree_unlink_2_example.png )



*Un link all'interno di un gruppo viene scollegato e l'oggetto reale viene invece posizionato all'interno.*





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkUnlink/it
