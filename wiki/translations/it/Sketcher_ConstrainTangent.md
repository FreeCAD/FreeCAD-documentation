---
 GuiCommand:
   Name: Sketcher ConstrainTangent
   Name/it: Sketcher Vincolo tangente
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo tangente o collineare
   Workbenches: Sketcher_Workbench/it
   Shortcut: **T**
   SeeAlso: 
---

# Sketcher ConstrainTangent/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Sketcher Vincolo tangente](Sketcher_ConstrainTangent/it.md) vincola due bordi, o un bordo e un asse, ad essere tangenti. Le linee vengono trattate come infinite e anche le curve aperte vengono virtualmente estese. Il vincolo può anche connettere due bordi, costringendoli ad essere tangenti in corrispondenza del giunto. Se vengono selezionate due linee oppure una linea e il punto finale di un\'altra linea, le linee vengono rese collineari.



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ConstrainTangent.svg" width=16px> [Vincolo tangente o collineare](Sketcher_ConstrainTangent/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainTangent.svg" width=16px> Vincolo tangente o collineare** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Vincolo → <img src="images/Sketcher_ConstrainTangent.svg" width=16px> Vincolo tangente o collineare** dal menu contestuale.

    -   Usare la scorciatoia da tastiera: **T**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Effettuare una delle seguenti operazioni:
    -   Selezionare due bordi. I bordi possono essere qualsiasi bordo tranne una B-spline.
    -   Selezionare un punto e due bordi (in quest\'ordine).
    -   Selezionare un bordo, un punto e un altro bordo (idem).
5.  Viene aggiunto un vincolo Tangente. Se sono stati selezionati un punto e due bordi, è possibile aggiungere anche fino a due [Vincoli punto su oggetto](Sketcher_ConstrainPointOnObject.md). Vedere [Esempi](#Tra_due_bordi_in_un_punto.md).
6.  Facoltativamente, continuare a creare vincoli.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare due bordi (vedere sopra).
    -   Selezionare due punti finali appartenenti a bordi diversi.
    -   Selezionare un bordo e il punto finale di un altro bordo (in qualsiasi ordine).
    -   Selezionare un punto e due bordi (idem).
2.  Richiamare lo strumento come spiegato sopra o con la seguente opzione aggiuntiva:
    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [3D view](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ConstrainTangent.svg" width=16px> Vincolo tangente o collineare** dall\'elenco menu contestuale.
3.  Viene aggiunto un vincolo Tangente. Se sono stati selezionati un punto e due bordi, è possibile aggiungere anche fino a due [Vincoli punto su oggetto](Sketcher_ConstrainPointOnObject/it.md). Vedere [Esempi](#Tra_due_bordi_in_un_punto.md).



## Esempi



### Tra due bordi 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:400px;">

I due bordi sono resi tangenti. Se uno dei bordi è una [conica](Sketcher_Workbench/it#Sketcher_CompCreateConic.md), viene aggiunto un [Oggetto punto](Sketcher_CreatePoint/it.md) che ha un [Vincolo punto su oggetto](Sketcher_ConstrainPointOnObject/it.md) con entrambi i bordi (estesi).

Non è consigliabile ricostruire il punto di tangenza creando manualmente un punto e vincolandolo a giacere su entrambe le curve. Funzionerà, ma la convergenza sarà decisamente più lenta, più discontinua e richiederà circa il doppio delle iterazioni per convergere rispetto al normale. Se è necessario il punto di tangenza, selezionare invece due bordi e un punto esistente.



### Tra due punti finali 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:400px;">

I punti finali vengono resi coincidenti e l\'angolo tra i bordi in quel punto viene impostato su 180° (giunto liscio) o 0° (giunto stretto), a seconda del posizionamento dei bordi prima dell\'applicazione del vincolo.



### Tra bordo e punto finale 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:400px;">

Il punto finale di un bordo è vincolato a giacere sull\'altro bordo e i bordi vengono resi tangenti in quel punto



### Tra due bordi in un punto 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:400px;">

I due bordi vengono resi tangenti in un dato punto. Il punto può essere qualsiasi punto, ad es. il centro di un cerchio, il punto finale di un bordo o l\'origine, può appartenere a uno dei bordi e può anche essere un [Oggetto punto](Sketcher_CreatePoint/it.md). Se necessario, vengono aggiunti [Vincoli punto su oggetto](Sketcher_ConstrainPointOnObject/it.md) per garantire che il punto si trovi su entrambi i bordi (estesi). Questi vincoli aggiuntivi sono chiamati [vincoli di supporto](Sketcher_helper_constraint/it.md).

Rispetto alla tangenza diretta, questo vincolo è più lento, perché sono coinvolti più gradi di libertà, ma se è necessario il punto di tangenza, è consigliato perché offre una migliore convergenza.



### Tra due linee 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width:400px;">

Le due linee sono rese collineari.



## Script

Il Vincolo tangente può essere creato da [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando quanto segue: 
```python
# direct tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,icurve2))

# point-to-point tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2))

# tangent-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('TangentViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` dove:

  - `Sketch` è un oggetto schizzo

  - `icurve1`, `icurve2` sono due numeri interi che identificano le curve da rendere tangenti. Gli interi sono indici nello schizzo (i valori, restituiti da `Sketch.addGeometry`).

  - `pointpos1`, `pointpos2` dovrebbe essere `1` per il punto iniziale e `2` per il punto finale.

  - `geoidpoint` e `pointpos` in `TangentViaPoint` sono gli indici che specificano il punto di tangenza.

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `incurve1`, `incurve2`, `pointpos1`, `pointpos2`, `geoidpoint` e `pointpos` e contiene ulteriori esempi su come creare vincoli da script Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainTangent/it
