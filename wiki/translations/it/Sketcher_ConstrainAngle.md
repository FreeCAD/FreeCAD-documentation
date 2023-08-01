---
- GuiCommand:/it
   Name:Sketcher_ConstrainAngle
   Name/it:Angolo
   Workbenches:[Schizzo](Sketcher_Workbench/it.md)
   Shortcut:**A**
   MenuLocation:Sketch → Vincoli → Angolo
   SeeAlso:[Lunghezza](Sketcher_ConstrainDistance/it.md), [Perpendicolare](Sketcher_ConstrainPerpendicular/it.md)
---

# Sketcher ConstrainAngle/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Il vincolo Angolo è un [vincolo valore](Sketcher_Workbench/it#Vincoli_dello_schizzo.md) destinato a fissare gli angoli in uno schizzo. È in grado di impostare le pendenze delle singole linee, gli angoli tra le linee, gli angoli di intersezioni di curve, e l\'ampiezza dei settori di cerchio.


</div>



## Utilizzo

Ci sono quattro modi diversi per applicare il vincolo:

1.  a una singola linea
2.  tra due linee
3.  a una intersezione di curve
4.  a archi di circonferenze


<div class="mw-translate-fuzzy">

Per applicare il vincolo angolo, si dovrebbe il seguire la seguente procedura:

1.  Selezionare una, due o tre entità nello schizzo. La modalità sarà scelta in funzione della selezione.
2.  Richiamare il comando in uno di questi modi:
    -   Cliccare sull\'icona **[<img src=images/Sketcher_ConstrainAngle.svg style="width:16px"> Angolo** della barra degli strumenti.
    -   Usare la scorciatoia da tastiera **A**.
    -   Usare la voce **Sketch → Vincoli → [<img src=images/Sketcher_ConstrainAngle.svg style="width:16px"> Angolo** dal menu principale.
3.  Si apre una finestra di dialogo di modifica del dato.
4.  Se necessario, modificare il valore. **Nota:** L\'angolo può essere inserito anche come una espressione che viene valutata e di cui viene memorizzato il risultato.
5.  Fare clic su **OK**.


</div>

Come per qualsiasi vincolo valore, è possibile modificare in seguito il valore dell\'angolo facendo doppio clic sul vincolo nella lista dei vincoli o nella vista 3D. Un valore negativo inverte la direzione dell\'angolo.



## Modalità di vincolo 



### Angolo di inclinazione di una linea 

**Selezioni accettate:** linea

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:600px;">

Il vincolo imposta l\'angolo polare della direzione della linea. È l\'angolo tra la linea e l\'asse X dello schizzo.




<div class="mw-translate-fuzzy">

### Ampiezza di un arco (v0.15) 


</div>

**Selezioni accettate:** arco di circonferenza

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:600px;">

In questa modalità, il vincolo fissa l\'ampiezza di un arco di circonferenza.



### Tra due linee 

**Selezioni accettate:** linea + linea

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:600px;">

In questa modalità, il vincolo imposta l\'angolo tra due linee. Non è necessario che le linee siano intersecanti.




<div class="mw-translate-fuzzy">

### Nell\'intersezione tra due curve (angolo-nel-punto) (v0.15) 


</div>

**Selezioni accettate:** qualsiasi linea/curva + qualsiasi linea/curva + qualsiasi punto

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:600px;">

In questa modalità, l\'angolo tra due curve è vincolato nel punto della loro intersezione. Il punto di intersezione può essere anche sull\'estensione delle curve. Il punto di intersezione in cui applicare il vincolo deve essere definito esplicitamente, poiché tipicamente le curve si intersecano in più punti.


<div class="mw-translate-fuzzy">

Affinchè il vincolo funzioni correttamente, il punto deve appartenere a entrambe le curve. Quindi, appena il vincolo viene invocato, il punto viene automaticamente vincolato su entrambe le curve, e l\'angolo tra le curve viene vincolato nel punto. Se è necessario viene aggiunto un [vincolo di supporto](Sketcher_helper_constraint/it.md). I vincoli di supporto sono dei normali vincoli che possono essere aggiunti o cancellati manualmente. Nell\'immagine dell\'esempio precedente non ci sono vincoli di supporto, perché il punto selezionato è già l\'intersezione delle curve.


</div>



## Script


<div class="mw-translate-fuzzy">

I vincoli di angolo possono essere creati con le [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) utilizzando la seguente funzione:


</div>


```python
# line slope angle
Sketch.addConstraint(Sketcher.Constraint('Angle',iline,angle))

# angular span of arc
Sketch.addConstraint(Sketcher.Constraint('Angle',iarc,angle))

# angle between lines
Sketch.addConstraint(Sketcher.Constraint('Angle',iline1,pointpos1,iline2,pointpos2,angle))

# angle-via-point (no helper constraints are added automatically when from python)
Sketch.addConstraint(Sketcher.Constraint('AngleViaPoint',icurve1,icurve2,geoidpoint,pointpos,angle))
```

Dove:

  - `Sketch` è un oggetto sketch

  - `iline, iline1, iline2` sono i numeri interi che specificano le linee con i loro numeri ordinali in `Sketch`.

  - `pointpos1, pointpos2` dovrebbero essere 1 per il punto iniziale e 2 per il punto finale. La scelta dei punti finali consente di impostare l\'angolo interno (o esterno), e incide su come il vincolo viene disegnato nello schermo.

  - `geoidpoint` e `pointpos` in `AngleViaPoint` sono gli indici che specificano il punto di intersezione.

  - `angle` è il valore dell\'angolo in radianti. L\'angolo è valutato tra i vettori tangenti, in senso antiorario. I vettori tangenti sono orientati dall\'inizio verso la fine per le linee (o viceversa quando nella modalità angolo tra linee viene fornito il punto finale), e lungo la direzione antioraria per cerchi, archi ed ellissi. Quantity è anche accettata come un angolo (e.g. `App.Units.Quantity('45 deg')`)

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `iline`, `iline1`, `iline2`, `pointpos1`, `pointpos2`, `geoidpoint` and `pointpos` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainAngle/it
