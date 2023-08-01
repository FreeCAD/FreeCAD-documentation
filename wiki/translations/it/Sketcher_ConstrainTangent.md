---
- GuiCommand:
   Name:Sketcher ConstrainTangent
   Name/it:Sketcher VincoloTangente
   MenuLocation:Sketch - Sketcher Vincoli - Vincolo Tangente
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   Shortcut:**T**
   SeeAlso:[Sketcher Vincolo Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md)
---

# Sketcher ConstrainTangent/it

## Descrizione

Il vincolo Tangente costringe due curve ad essere tangenti. Le linee sono trattate come infinite, e gli archi sono trattati come cerchi o ellissi completi. Il vincolo è anche in grado di collegare due curve costringendole ad essere tangenti nella giunzione, e quindi rende levigata la loro congiunzione.

Tangent Constraint can also be used with two lines to make them colinear.

## Utilizzo

Ci sono cinque modi diversi in cui il vincolo può essere applicato:

1.  tra due curve (disponibile non per tutte le curve)
2.  tra due punti finali di una curva, facendo un giunto liscio
3.  tra una curva e un punto finale di un\'altra curva
4.  tra due curve in un punto definito dall\'utente
5.  tra due linee per creare una condizione di collinearità

Per applicare il vincolo di tangenza, si dovrebbe usare la seguente procedura:

-   Selezionare due o tre entità nello schizzo.
-   Invocare il vincolo facendo clic sull\'icona nella barra degli strumenti, oppure selezionando la voce del menu, oppure usando la scorciatoia da tastiera.

### Tra due curve (tangenza diretta) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:600px;">

Rende tangenti due curve, e il punto di tangenza è implicito. Questa modalità si applica se sono state selezionate due curve.

**Selezioni accettate:**

-   linea + linea, cerchio, arco, ellisse, arco-di-ellisse
-   cerchio, arco + cerchio, arco

Se tra le curve selezionate la \"tangenza diretta\" non è supportata (ad esempio, tra un cerchio e un\'ellisse), nello schizzo viene automaticamente aggiunto un punto di supporto e viene applicata la \"tangenza nel punto\".

Non è consigliabile ricostruire il punto di tangenza creando un punto e vincolandolo ad appartenere ad entrambe le curve. Questo metodo funziona, ma la convergenza è molto lenta, e richiede circa il doppio delle iterazioni di una convergenza normale. Se il punto di tangenza è proprio necessario conviene utilizzare gli altri modi di applicazione di questo vincolo.

### Tra due punti finali (tangenza punto con punto) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:600px;">


<div class="mw-translate-fuzzy">

In questa modalità, i punti finali sono resi coincidenti, e la giunzione è creata tangente; C1-liscio, o \"brusco\", a seconda del posizionamento delle curve prima dell\'applicazione del vincolo. Questa modalità viene applicata quando sono stati selezionati due punti finali di due curve.


</div>

**Selezioni accettate:**

-   punto finale di linea/arco/arco-di-ellisse + punto finale di linea/arco/arco-di-ellisse, cioè due punti finali di qualsiasi due curve

### Tra una curva e un punto finale (tangenza punto con curva) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:600px;">

In questo modo, il punto finale di una curva è vincolato a giacere sull\'altra curva, e le curve sono forzate ad essere tangenti nel punto. Questa modalità viene applicata quando sono stati selezionati una curva e un punto finale di un\'altra curva.

**Selezioni accettate:**

-   linea, cerchio, arco, ellisse, arco-di-ellisse + punto finale di linea/arco/arco-di-ellisse (qualsiasi curva + punto finale di qualsiasi curva)

### Tra due curve nel punto (tangenza nel punto) (v0.15) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:600px;">

In questo modo, sono rese tangenti due curve, e il punto di tangenza è monitorato. Questa modalità viene applicata quando sono state selezionate due curve e un punto.

**Selezioni accettate:**

-   qualsiasi linea/curva + qualsiasi linea/curva + qualsiasi punto

\"Qualsiasi punto\" può essere un punto generico, o un punto di qualcosa, ad esempio il centro di un cerchio, il punto finale di un arco, o l\'origine.

Affinchè il vincolo funzioni correttamente, il punto deve appartenere a entrambe le curve. Così, quando il vincolo viene invocato, il punto viene vincolato automaticamente su entrambe le curve, e le curve sono forzate tangenti nel punto. Se è necessario sono anche aggiunti dei [vincoli di supporto](Sketcher_helper_constraint/it.md). I vincoli di supporto sono dei normali vincoli e possono essere aggiunti o eliminati manualmente.

Rispetto alla tangenza diretta, questo vincolo è più lento, perché sono coinvolti i gradi di libertà, ma se il punto di tangenza è necessario, è la modalità consigliata perché offre una migliore convergenza rispetto alla tangenza diretta + punto su due curve.

La posizione del punto selezionato prima di applicare il vincolo serve al solutore per sapere dove deve applicare la tangenza. Con questo vincolo, si può costringere due ellissi a toccarsi in due posti.

### Tra due linee (collineari) 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width:600px;">

**Accepted selection:**

-   any line/vertex + any line/vertex

## Script


<div class="mw-translate-fuzzy">

I vincoli di tangenza possono essere creati con le [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) utilizzando la seguente funzione:


</div>


```python
# direct tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,icurve2))

# point-to-point tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2))

# tangent-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('TangentViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
```

Dove:

  - `Sketch` è un oggetto sketch

  - `icurve1`, `icurve2` sono due numeri interi che identificano le curve da rendere tangenti. I numeri interi sono gli indici nello schizzo (il valore, reso da `Sketch.addGeometry`).

  - `pointpos1`, `pointpos2` dovrebbe essere 1 per il punto iniziale e 2 per il punto finale.

  - `geoidpoint` e `pointpos` in `TangentViaPoint` sono gli indici che specificano il punto di tangenza.

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `incurve1`, `incurve2`, `pointpos1`, `pointpos2`, `geoidpoint` and `pointpos` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainTangent/it
