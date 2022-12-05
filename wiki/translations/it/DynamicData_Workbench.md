# <img alt="L\'icona dell\'ambiente aggiuntivo DynamicData" src=images/DynamicData_workbench_icon.svg  style="width:64px;"> DynamicData Workbench/it


{{TOCright}}

## Presentazione

DynamicData è un [ambiente aggiuntivo](External_workbenches/it.md) con cui è possibile creare un oggetto contenitore per contenere proprietà personalizzate.

Con questo workbench si possono creare delle nuove [proprietà](property/it.md) personalizzate di qualsiasi dei tipi supportati da FreeCAD. Ad esempio una proprietà Length o una proprietà [Posizionamento](Placement/it.md). Queste proprietà personalizzate possono quindi essere utilizzate nelle [Espressioni](Expressions/it.md) proprio come qualsiasi altra proprietà. Ad esempio, è possibile creare una proprietà Lunghezza chiamata \"Larghezza\" e fare riferimento ad essa quando si vincola un elemento dello schizzo. Quindi, quando la proprietà \"Larghezza\" viene modificata, il vincolo dello schizzo si aggiorna automaticamente. Questo è simile al modo in cui si può usare un foglio di calcolo, ma è più interattivo in quanto le proprietà possono essere modificate continuando a vedere la vista 3D e consente anche una più ampia varietà di tipi di proprietà.

Alcune funzioni includono:

-   la possibilità di importare i vincoli con il loro nome da uno schizzo
-   la possibilità di copiare le proprietà o impostare valori delle proprietà da un oggetto all\'altro
-   gli oggetti contenitore rimangono compatibili con le installazioni di FreeCAD che non hanno il workbench installato

## Installazione

Questo ambiente di lavoro può essere installato da [Addon Manager](Std_AddonMgr/it.md). Per l\'installazione manuale vedi [Installare ulteriori ambienti di lavoro](Installing_more_workbenches/it.md).

## Link

-   Codice sorgente ospitato su GitHub: [github.com](https://github.com/mwganson/DynamicData)
-   [Documentazione ufficiale completa](https://github.com/mwganson/DynamicData/blob/master/README.md)

## Ambienti esterni 

Gli ambienti di FreeCAD sono facili da programmare in [Python](Python.md), quindi ci sono molte persone che sviluppano ambienti aggiuntivi al di fuori degli sviluppatori principali di FreeCAD.

La pagina [ambienti complementari](external_workbenches/it.md) ha alcune informazioni e tutorial su alcuni di essi, e il progetto [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) mira a raccoglierli e renderli facilmente installabili da FreeCAD.

Sono in fase di sviluppo ulteriori nuovi ambienti.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > DynamicData Workbench/it
