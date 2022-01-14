# DynamicData Workbench/it
<div class="mw-translate-fuzzy">



*align=center|L'icona dell'ambiente aggiuntivo DynamicData*


</div>


{{TOCright}}

## Presentazione

DynamicData è un [ambiente aggiuntivo](External_workbenches/it.md) con cui è possibile creare un oggetto contenitore per contenere proprietà personalizzate.

Con questo workbench si possono creare delle nuove [proprietà](property/it.md) personalizzate di qualsiasi dei tipi supportati da FreeCAD. Ad esempio una proprietà Length o una proprietà [Posizionamento](Placement/it.md). Queste proprietà personalizzate possono quindi essere utilizzate nelle [Espressioni](Expressions/it.md) proprio come qualsiasi altra proprietà. Ad esempio, è possibile creare una proprietà Lunghezza chiamata \"Larghezza\" e fare riferimento ad essa quando si vincola un elemento dello schizzo. Quindi, quando la proprietà \"Larghezza\" viene modificata, il vincolo dello schizzo si aggiorna automaticamente. Questo è simile al modo in cui si può usare un foglio di calcolo, ma è più interattivo in quanto le proprietà possono essere modificate continuando a vedere la vista 3D e consente anche una più ampia varietà di tipi di proprietà.

Alcune funzioni includono:

-   la possibilità di importare i vincoli con il loro nome da uno schizzo
-   la possibilità di copiare le proprietà o impostare valori delle proprietà da un oggetto all\'altro
-   gli oggetti contenitore rimangono compatibili con le installazioni di FreeCAD che non hanno il workbench installato

## Installazione


<div class="mw-translate-fuzzy">

Questo ambiente può essere facilmente installato e aggiornato dal <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md) disponibile in FreeCAD 0.17 e superiore. Per gli utenti di FreeCAD 0.16 e per altri metodi di installazione, fare riferimento alla pagina [Installare componenti aggiuntivi](Installing/it#Installare_componenti_aggiuntivi.md).


</div>

## Link

-   Codice sorgente ospitato su GitHub: [github.com](https://github.com/mwganson/DynamicData)
-   [Documentazione ufficiale completa](https://github.com/mwganson/DynamicData/blob/master/README.md)

## Ambienti esterni 

Gli ambienti di FreeCAD sono facili da programmare in [Python](Python.md), quindi ci sono molte persone che sviluppano ambienti aggiuntivi al di fuori degli sviluppatori principali di FreeCAD.

La pagina [ambienti complementari](external_workbenches/it.md) ha alcune informazioni e tutorial su alcuni di essi, e il progetto [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) mira a raccoglierli e renderli facilmente installabili da FreeCAD.

Sono in fase di sviluppo ulteriori nuovi ambienti.




[<img src="images/Property.png" style="width:16px"> Addons](Category_Addons.md) [<img src="images/Property.png" style="width:16px"> External Workbenches](Category_External_Workbenches.md)

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > DynamicData Workbench/it
