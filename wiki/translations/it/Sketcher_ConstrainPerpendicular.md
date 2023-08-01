# Sketcher ConstrainPerpendicular/it
---
- GuiCommand:   Name: Sketcher ConstrainPerpendicular   Name/it: Perpendicolare   Workbenches: [PartDesign](Sketcher_Workbench/it___Schizzo]],_[[PartDesign_Workbench/it.md)|MenuLocation: PartDesign - Schizzo - Perpendicolare   Shortcut: **N**   SeeAlso: [Angolo](Sketcher_ConstrainAngle/it.md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Il vincolo Perpendicolare fa sì che due linee siano perpendicolari tra loro, o che due curve siano perpendicolari al loro incrocio. Le linee sono considerate infinite, e gli archi sono considerati cerchi completi o ellissi complete. Il vincolo è anche in grado di collegare due curve, costringendole perpendicolari nel punto di unione, in modo simile al vincolo [Tangente](Sketcher_ConstrainTangent/it.md).


</div>

## Utilizzo

Ci sono quattro modi diversi per applicare il vincolo:

1.  tra due curve (non disponibile per tutte le curve)
2.  tra due punti finali di curve
3.  tra una curva e il punto finale di un\'altra curva
4.  tra due curve in un punto definito dall\'utente

Per applicare il vincolo perpendicolare, si dovrebbe usare la seguente procedura:

-   Selezionare due o tre entità nello schizzo.
-   Invocare il vincolo facendo clic sull\'icona nella barra degli strumenti, oppure selezionando la voce del menu, oppure usando la scorciatoia da tastiera.


<div class="mw-translate-fuzzy">

### Tra due curve (perpendicolarità diretta) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode1.png  style="width:600px;">


</div>

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode1.png  style="width:600px;">

Due curve vengono rese perpendicolari nel punto della loro intersezione (sia reale, che sull\'estensione delle curve). Il punto di intersezione è implicito. Questa modalità si applica se sono state selezionate due curve.

**Selezioni accettate:**

-   linea + linea, cerchio, arco
-   cerchio, arco + cerchio, arco

Se tra le curve selezionate la \"perpendicolarità diretta\" non è supportata (ad esempio, tra una linea e un\'ellisse), nello schizzo viene automaticamente aggiunto un punto di supporto e viene applicata la \"perpendicolarità nel punto\".

Diversamente dalla tangenza, per costruire il punto di ortogonalità è bene creare un punto e vincolarlo a giacere su entrambe le curve (vincolando il punto nell\'intersezione).


<div class="mw-translate-fuzzy">

### Tra due punti finali (perpendicolarità punto con punto) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode2.png  style="width:600px;">


</div>

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode2.png  style="width:600px;">

In questo modo, i punti finali sono coincidenti, e la congiunzione avviene ad angolo retto. Questa modalità viene applicata quando sono stati selezionati due punti finali di due curve.

**Selezioni accettate:**

-   punto finale di linea/arco/arco-di-ellisse + punto finale di linea/arco/arco-di-ellisse, cioè due punti finali di qualsiasi due curve


<div class="mw-translate-fuzzy">

### Tra una curva e un punto finale (perpendicolarità punto con curva) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode3.png  style="width:600px;">


</div>

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode3.png  style="width:600px;">

In questo modo, il punto finale di una curva è vincolato a giacere sull\'altra curva, e le curve sono forzate ad essere perpendicolari nel punto. Questa modalità viene applicata quando sono stati selezionati una curva e un punto finale di un\'altra curva.

**Selezioni accettate:**

-   linea, cerchio, arco, ellisse, arco-di-ellisse + punto finale di linea/arco/arco-di-ellisse (qualsiasi curva + punto finale di qualsiasi curva)


<div class="mw-translate-fuzzy">

### Tra due curve nel punto (perpendicolarità nel punto) (v0.15) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode4.png  style="width:600px;">


</div>

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode4.png  style="width:600px;">

Questo modo rende perpendicolari due curve, e il punto di tangenza è monitorato. Questa modalità viene applicata quando sono state selezionate due curve e un punto.

**Selezioni accettate:**

-   qualsiasi linea/curva + qualsiasi linea/curva + qualsiasi punto

\"Qualsiasi punto\" può essere un punto generico, o un punto di qualcosa, ad esempio il centro di un cerchio, il punto finale di un arco, o l\'origine.


<div class="mw-translate-fuzzy">

Affinchè il vincolo funzioni correttamente, il punto deve appartenere a entrambe le curve. Così, quando il vincolo viene invocato, il punto viene vincolato automaticamente su entrambe le curve, e le curve sono forzate perpendicolari nel punto. Se è necessario sono anche aggiunti dei [vincoli di supporto](Sketcher_helper_constraint/it.md) che sono dei normali vincoli e possono essere aggiunti o eliminati manualmente.


</div>

Rispetto alla perpendicolarità diretta, questo vincolo è più lento, perché coinvolge molti gradi di libertà, ma supporta le ellissi.

La posizione del punto selezionato prima di applicare il vincolo serve al solutore per sapere dove deve applicare la perpendicolarità.

## Script


<div class="mw-translate-fuzzy">

I vincoli di perpendicolarità possono essere creati con le [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) utilizzando la seguente funzione:


</div>


```python
# direct perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,icurve2))

# point-to-point perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2))

# perpendicular-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('PerpendicularViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
```


<div class="mw-translate-fuzzy">

Dove:

  - Sketch è un oggetto sketch

  - icurve1, icurve2 sono due numeri interi che identificano le curve da rendere perpendicolari. I numeri interi sono gli indici nello schizzo (il valore, reso da Sketch.addGeometry).

  - pointpos1, pointpos2 dovrebbe essere 1 per il punto iniziale e 2 per il punto finale.

  - geoidpoint and pointpos in PerpendicularViaPoint sono gli indici che specificano il punto di perpendicolarità.


</div>

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `icurve1`, `icurve2`, `pointpos1`, `pointpos2` and `geoidpoint`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPerpendicular/it
