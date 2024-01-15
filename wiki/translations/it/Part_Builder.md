---
 GuiCommand:
   Name: Part Builder
   Name/it: Genera forme
   MenuLocation: Parte , Genera una forma...
   Workbenches: Part_Workbench/it
   SeeAlso: Part_Primitives/it
---

# Part Builder/it



## Descrizione

Uno strumento per creare forme più complesse da varie primitive geometriche parametriche.



## Utilizzo

Questo strumento può creare i seguenti oggetti:



### Bordo da due vertici 

1.  Selezionare due vertici
2.  Fare clic su **Crea**

![](images/Edge_from_verts-1.gif )



### Polilinea da bordi 

1.  Selezionare una serie di bordi adiacenti nella [vista 3D](3D_view/it.md)
2.  Fare clic su **Crea**

![](images/Wire_from_edges-1.gif )



### Faccia da vertici 

1.  Selezionare i vertici che delimitano la faccia nella [vista 3D](3D_view/it.md)
2.  Selezionare se la faccia deve essere planare
3.  Fare clic su **Crea**
4.  L\'oggetto verrà creato nella [vista 3D](3D_view/it.md) e sarà elencato nella [vista ad albero](Tree_view/it.md)

![](images/Face_from_verts.gif )



### Faccia da bordi 

1.  Selezionare una serie chiusa di bordi che delimitano la faccia nella [vista 3D](3D_view/it.md)
2.  Selezionare se la faccia deve essere planare
3.  Fare clic su **Crea**
4.  L\'oggetto verrà creato nella [vista 3D](3D_view/it.md) e sarà elencato nella [vista ad albero](Tree_view/it.md)

![](images/Face_from_edges.gif )



### Guscio da facce 

1.  Selezionare le facce nella [vista 3D](3D_view/it.md)
2.  Selezionare se la forma deve essere rifinita
3.  Selezionare se tutte le facce devono essere incluse nel guscio
4.  Fare clic su **Crea**
5.  L\'oggetto verrà creato nella [vista 3D](3D_view/it.md) e sarà elencato nella [vista ad albero](Tree_view/it.md)



### Solido da guscio 

1.  Selezionare se la forma deve essere rifinita
2.  Fare clic su **Crea**
3.  L\'oggetto verrà creato nella [vista 3D](3D_view/it.md) e sarà elencato nella [vista ad albero](Tree_view/it.md)



## Note

Un possibile flusso di lavoro potrebbe essere:

-   Disegnare un modello a fil di ferro della forma utilizzando gli strumenti in <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md) (ad esempio linee e polilinee)
-   Creare tutte le facce con \"faccia dai bordi\"
-   Creare un \"guscio da facce\"
-   Creare un \"solido da guscio\"



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Builder/it
