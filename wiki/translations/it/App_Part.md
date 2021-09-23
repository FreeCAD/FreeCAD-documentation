# App Part/it


## Introduzione

<img alt="" src=images/Geofeaturegroup.svg  style="width:32px;">

Un oggetto [App Part](App_Part/it.md), o formalmente un `App::Part`, è un elemento che consente di raggruppare degli oggetti nello spazio 3D.

È stato sviluppato per essere utilizzato negli assiemi, in quanto ha una **Origin** che funge da riferimento posizionale per gli oggetti raggruppati.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. La classe `App::Part* è un semplice contenitore che ha una posizione nello spazio 3D e ha un'origine per controllare il posizionamento degli oggetti raggruppati sotto di essa.`

## Utilizzo

1.  Premere il pulsante **<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/it.md)**. Viene creata una parte vuota che diventa automaticamente *[attiva](Std_Part/it#Stato_attivo.md)*.
2.  Per aggiungere oggetti a una parte, trascinarli e rilasciarli sulla parte nella [vista ad albero](tree_view/it.md).
3.  Per rimuovere oggetti da una parte, trascinarli fuori dalla parte e sull\'etichetta del documento nella parte superiore della [vista ad albero](tree_view/it.md).

Vedere la pagina [Std Part](Std_Part/it.md) per le informazioni complete, incluso il suo uso negli [Script](Std_Part/it#Script.md).

## Proprietà

Una classe [App Part](App_Part/it.md) (`App::Part`) è derivata dalla classe base [App GeoFeature](App_GeoFeature/it.md) (`App::GeoFeature`), pertanto condivide la maggior parte delle proprietà di quest\'ultima.

Vedere l\'elenco completo delle proprietà nella pagina [Std Part](Std_Part/it.md).


{{Std Base navi

}} {{Document objects navi}} 
