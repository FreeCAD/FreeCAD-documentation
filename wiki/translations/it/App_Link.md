# App Link/it
{{TOCright}}

## Introduzione

<img alt="" src=images/Link.svg  style="width:32px;">

Un <img alt="" src=images/Link.svg  style="width:32px;"> [App Link](App_Link/it.md), o formalmente un `App::Link`, è un tipo di oggetto che fa riferimento o si collega a un altro oggetto, nello stesso documento o in un altro documento. È appositamente progettato per duplicare in modo efficiente un singolo oggetto più volte, il che aiuta nella creazione di [assemblaggi](assembly/it.md) complessi da sottoassiemi più piccoli e da più componenti riutilizzabili come viti, dadi e dispositivi di fissaggio simili.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. L'oggetto `App::Link* è un componente principale del sistema, non dipende da alcun ambiente, ma può essere utilizzato con la maggior parte degli oggetti creati in tutti gli ambienti.`

## Utilizzo

1.  Selezionare un oggetto nella [vista ad albero](tree_view/it.md) o nella [vista 3D](3D_view/it.md) per il quale si desidera creare un link.
2.  Premere il pulsante **[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea link](Std_LinkMake/it.md)**. L\'oggetto prodotto ha la stessa icona dell\'oggetto originale, ma ha una freccia sovrapposta che indica che è un collegamento.

Vedere la pagina [Crea link](Std_LinkMake/it.md) per le informazioni complete, compreso il suo utilizzo negli [Script](Std_LinkMake/it#Script.md).

## Proprietà

Un oggetto [App Link](App_Link/it.md) (classe `App::Link`) è derivato dall\'oggetto base [App DocumentObject](App_DocumentObject.md) (classe `App::DocumentObject`), pertanto condivide tutte le proprietà di quest\'ultimo.

Vedere l\'elenco completo delle proprietà nella pagina [Crea link](Std_LinkMake/it.md).


{{Std Base navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > App Link/it
