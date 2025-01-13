---
 GuiCommand:
   Name: Sketcher CreateBSpline
   Name/it: Sketcher Crea B-spline dai punti di controllo
   MenuLocation: Schizzo , Geometrie Sketcher , Crea B-spline
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **B** **B**
   Version: 0.17
   SeeAlso: Sketcher_CreatePeriodicBSpline/it
---

# Sketcher CreateBSpline/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:24px;"> [Sketcher Crea B-spline](Sketcher_CreateBSpline/it.md) crea una curva [B-spline](B-Splines/it.md) dai punti di controllo. {{Version/it|1.0}}: o facoltativamente tramite i punti nodo.

![](images/Sketcher_CreateBSpline_Example.png ) 
*Curva B-spline (bianca) definita da 5 punti di controllo.<br>
Il poligono di controllo (verde) collega i punti di controllo (contrassegnati con cerchi di peso giallo scuro).<br>
Il numero 3 (verde, senza parentesi) al centro si riferisce al [grado](Sketcher_BSplineIncreaseDegree/it#Description.md) della B-spline.<br>
I numeri (1) e (4) (verde, tra parentesi tonde) si riferiscono alla [molteplicità](Sketcher_BSplineDecreaseKnotMultiplicity/it#Description.md) dei punti nodo.<br>
I numeri [1.00] (verde, tra parentesi quadre) si riferiscono ai pesi dei punti di controllo.*



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CreateBSpline.svg" width=16px> [B-spline dai punti di controllo](Sketcher_CreateBSpline/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Geometrie Sketcher → <img src="images/Sketcher_CreateBSpline.svg" width=16px> Crea B-spline** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_CreateBSpline.svg" width=16px> Crea B-spline** dal menu contestuale. {{Version/it|1.0}}
    -   Usare la scorciatoia da tastiera: **G** quindi **B**, quindi **B**.
2.  Il cursore si trasforma in una croce con l\'icona dello strumento.
3.  La sezione **Parametri B-spline** ({{Version/it|1.0}}) è stata aggiunta nella parte superiore della finestra [Dialogo Sketcher](Sketcher_Dialog/it.md).
4.  Facoltativamente, premere il tasto **M** o selezionare dall\'elenco a discesa nella sezione dei parametri per modificare la modalità dello strumento:
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:16px;"> **Da punti di controllo**:
        1.  Modifica facoltativamente il **Grado** (possibile anche dopo aver posizionato i punti):
            -   Inserire un numero maggiore di zero.
            -   Premere il tasto **U** per aumentare il grado.
            -   Premere il tasto **J** per diminuire il grado.
    -   <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:16px;"> **Per nodi**: {{Version/it|1.0}}
        1.  Le B-spline tramite nodi vengono sempre create con grado 3. Ma il loro grado può essere modificato in seguito. Vedere [Note](#Note.md).
5.  Facoltativamente, premere il tasto **R** o selezionare la casella **Periodico** per creare una B-spline chiusa (possibile anche dopo che i punti sono stati selezionati). {{Version/it|1.0}}
6.  Scegliere diversi punti.
7.  Facoltativamente, premere il tasto **F** prima di terminare per eliminare l\'ultimo punto. {{Version/it|1.0}}
8.  Fare clic con il pulsante destro del mouse o premere **Esc** per terminare l\'input.
9.  Viene creata la B-spline, incluso un insieme di geometrie interne (cerchi di peso e punti di nodo).
10. Se lo strumento viene eseguito in [modalità continua](Sketcher_Workbench/it#Continue_modes.md):
    1.  Facoltativamente, continuare a creare B-spline.
    2.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-   Gli elementi della geometria interna possono essere cancellati. Possono essere ricreati in qualsiasi momento con [Sketcher Mostra o Nascondi la geometria interna](Sketcher_RestoreInternalAlignmentGeometry/it.md).
-   Dopo aver creato una B-spline, è possibile definire il peso dei punti di controllo modificando i raggi dei cerchi del peso. I vincoli di uguaglianza sui cerchi devono prima essere eliminati. Il vincolo del raggio è arbitrario, il peso dei punti di controllo sarà definito dai raggi relativi dei cerchi. Funziona in modo simile alla gravità: più un cerchio è grande rispetto agli altri, più la curva sarà attratta da quel punto di controllo.
-   Il grado di una B-spline creata può essere [aumentato](Sketcher_BSplineIncreaseDegree/it.md) o [diminuito](Sketcher_BSplineDecreaseDegree/it.md), e la molteplicità dei suoi nodi può essere allo stesso modo [aumentata](Sketcher_BSplineIncreaseKnotMultiplicity/it.md) o [diminuita](Sketcher_BSplineIncreaseKnotMultiplicity/it.md).
-   La visibilità del [grado](Sketcher_BSplineDegree/it.md), del [poligono di controllo](Sketcher_BSplinePolygon/it.md), del [pettine di curvatura](Sketcher_BSplineComb/it.md), della [molteplicità dei nodi](Sketcher_BSplineKnotMultiplicity/it.md) e del [peso del punto di controllo](Sketcher_BSplinePoleWeight/it.md) può essere attivato/disattivato da Barra degli strumenti [Visualizzazione dello Schizzo](Sketcher_Workbench/it#Sketcher_visivo.md).



## Limitazioni

-   Al momento non sono supportati diversi vincoli.
-   La molteplicità dei nodi definita potrebbe non essere sempre rispettata:
    -   Per una spline periodica, il primo nodo (coincidente con l\'ultimo) ha sempre molteplicità pari a 2.
    -   Per una spline non periodica, il primo e l\'ultimo nodo hanno sempre una molteplicità pari a 4.
    -   Se i punti subito prima e subito dopo hanno molteplicità \>=3, il tratto tra questi due è completamente continuo e questo punto (centrale) sarà vincolato solo con il punto sull\'oggetto. Se è necessario un nodo, considerare l\'utilizzo dello strumento [inserisci nodo](Sketcher_BSplineInsertKnot/it.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSpline/it
