# App DocumentObjectGroup/it
## Introduzione

<img alt="" src=images/Folder.svg  style="width:32px;">

Un oggetto [App DocumentObjectGroup](App_DocumentObjectGroup/it.md) o formalmente un `App::DocumentObjectGroup`, è un elemento semplice che consente di raggruppare qualsiasi tipo di [App DocumentObject](App_DocumentObject/it.md) nella [vista ad albero](tree_view/it.md) indipendentemente dal tipo di dati.

È stato sviluppato per organizzare gli oggetti nella [vista ad albero](tree_view/it.md) in modo logico per l\'utente.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. La classe `App::DocumentObjectGroup* ha un'estensione che le consente di raggruppare qualsiasi tipo di oggetto; il gruppo di per se stesso non ha molte proprietà.`

## Utilizzo

1.  Premere il pulsante **[<img src=images/Std_Group.svg style="width:16px"> [Gruppo](Std_Group/it.md)** nella barra degli strumenti della struttura. Viene creato un gruppo vuoto.
2.  Per aggiungere degli oggetti a un gruppo, selezionarli nella [vista ad albero](tree_view/it.md), quindi trascinarli e rilasciarli sul gruppo.
3.  Per rimuovere degli oggetti da un gruppo, trascinarli fuori dal gruppo, sull\'etichetta del documento nella parte superiore della [vista ad albero](tree_view/it.md).

Vedere la pagina [Gruppo](Std_Group/it.md) per le informazioni complete, incluso il suo uso negli [Script](Std_Group/it#Script.md).

## Proprietà

Un [App DocumentObjectGroup](App_DocumentObjectGroup/it.md) (classe `App::DocumentObjectGroup`) è derivato dall\'oggetto base [App DocumentObject](App_DocumentObject/it.md) (classe `App::DocumentObject`), pertanto condivide tutte le proprietà di quest\'ultimo.

Vedere le proprietà nella pagina [Gruppo](Std_Group/it.md).


{{Std Base navi

}} {{Document objects navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > App DocumentObjectGroup/it
