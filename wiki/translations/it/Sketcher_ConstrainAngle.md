---
 GuiCommand:
   Name: Sketcher ConstrainAngle
   Name: Sketcher Vincolo angolo
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo angolo
   Workbenches: Sketcher_Workbench/it
   Shortcut: **K** **A**
   SeeAlso: Sketcher_ConstrainPerpendicular/it
---

# Sketcher ConstrainAngle/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;"> [Sketcher Vincolo angolo](Sketcher_ConstrainAngle/it.md) fissa l\'angolo tra due bordi (le linee vengono quindi trattate come infinite e anche le curve aperte sono virtualmente estese), l\'angolo di una linea con l\'asse orizzontale dello schizzo o con l\'angolo di apertura di un arco circolare.



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](Sketcher_Preferences/it#General.md) **Vincoli dimensionali** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del pulsante **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare il pulsante **<img src="images/Sketcher_ConstrainAngle.svg" width=16px> Vincolo angolo** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/Sketcher_ConstrainAngle.svg" width=16px> [Vincolo angolo](Sketcher_ConstrainAngle/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainAngle.svg" width=16px> Vincolo angolo** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Dimensione → [16px](Immagine:Sketcher_ConstrainAngle.svg.md) Vincolo angolo** dall\'elenco menu contestuale.

    -   Usare la scorciatoia da tastiera: **K** quindi **A**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Effettuare una delle seguenti operazioni:
    -   Selezionare due linee.
    -   Selezionare un punto e due bordi (in quest\'ordine).
    -   Selezionare uno spigolo, un punto e uno spigolo (idem).
5.  Se viene creato un [vincolo dimensionale guida](Sketcher_ToggleDrivingConstraint/it.md), a seconda delle [preferenze](Sketcher_Preferences/it#Display.md), si apre una finestra di dialogo per [modificarne il valore](Sketcher_Workbench/it#Edit_constraints.md). Un valore negativo invertirà la direzione dell\'angolo.
6.  Viene aggiunto un vincolo Angolo. Se sono stati selezionati un punto e due bordi, è possibile aggiungere anche fino a due [Vincoli punto su oggetto](Sketcher_ConstrainPointOnObject/it.md). Vedere [Esempi](#Tra_due_bordi_in_un_punto.md).
7.  Facoltativamente, continuare a creare vincoli.
8.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare una singola linea.
    -   Selezionare un singolo arco circolare.
    -   Selezionare due linee.
    -   Selezionare un punto e due bordi (in qualsiasi ordine).
2.  Richiamare lo strumento come spiegato sopra.
3.  Facoltativamente [modificare il valore del vincolo](Sketcher_Workbench/it#Edit_constraints.md).
4.  Viene aggiunto un vincolo Angolo. Se sono stati selezionati un punto e due bordi, è possibile aggiungere anche fino a due [Vincoli Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md). Vedere [Esempi](#Tra_due_bordi_in_un_punto.md).



## Esempi



### Linea singola 

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:400px;">

L\'angolo della linea con l\'asse X positivo dello schizzo è fissato.



### Arco circolare singolo 

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:400px;">

L\'angolo di apertura dell\'arco è fissato.



### Tra due linee 

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:400px;">

L\'angolo tra le due linee è fissato. Non è necessario che le linee si intersechino.



### Tra due bordi in un punto 

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:400px;">

L\'angolo tra i due bordi in un dato punto è fissato. Il punto può essere qualsiasi punto, ad es. il centro di un cerchio, il punto finale di un bordo o l\'origine, può appartenere a uno o entrambi i bordi e può anche essere un [oggetto Point](Sketcher_CreatePoint/it.md). Se necessario, vengono aggiunti [Vincoli Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md) per garantire che il punto si trovi su entrambi i bordi (estesi). Questi vincoli aggiuntivi sono chiamati [vincoli di supporto](Sketcher_helper_constraint/it.md).



## Script

Il Vincolo angolo può essere creato da [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando quanto segue: 
```python
# line slope angle
Sketch.addConstraint(Sketcher.Constraint('Angle',iline,angle))

# angular span of arc
Sketch.addConstraint(Sketcher.Constraint('Angle',iarc,angle))

# angle between lines
Sketch.addConstraint(Sketcher.Constraint('Angle',iline1,pointpos1,iline2,pointpos2,angle))

# angle-via-point (no helper constraints are added automatically when from python)
Sketch.addConstraint(Sketcher.Constraint('AngleViaPoint',icurve1,icurve2,geoidpoint,pointpos,angle))
``` Dove:

  - `Sketch` è un oggetto sketch

  - `iline, iline1, iline2` sono i numeri interi che specificano le linee con i loro numeri ordinali in `Sketch`.

  - `pointpos1, pointpos2` dovrebbero essere 1 per il punto iniziale e 2 per il punto finale. La scelta dei punti finali consente di impostare l\'angolo interno (o esterno), e incide su come il vincolo viene disegnato nello schermo.

  - `geoidpoint` e `pointpos` in `AngleViaPoint` sono gli indici che specificano il punto di intersezione.

  - `angle` è il valore dell\'angolo in radianti. L\'angolo è valutato tra i vettori tangenti, in senso antiorario. I vettori tangenti sono orientati dall\'inizio verso la fine per le linee (o viceversa quando nella modalità angolo tra linee viene fornito il punto finale), e lungo la direzione antioraria per cerchi, archi ed ellissi. Quantity è anche accettata come un angolo (e.g. `App.Units.Quantity('45 deg')`)

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `iline`, `iline1`, `iline2`, `pointpos1`, `pointpos2`, `geoidpoint` e `pointpos` e contiene ulteriori esempi su come creare vincoli da script Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainAngle/it
