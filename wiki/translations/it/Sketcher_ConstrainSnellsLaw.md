---
 GuiCommand:
   Name: Sketcher ConstrainSnellsLaw
   Name/it: Sketcher Vincolo di rifrazione
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo di rifrazione 
   Workbenches: Sketcher_Workbench/it
   Shortcut: **K** **W**
   Version: 0.15
---

# Sketcher ConstrainSnellsLaw/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [Sketcher Vincolo di rifrazione](Sketcher_ConstrainSnellsLaw/it.md) vincola due linee a seguire la legge di rifrazione della luce mentre penetra attraverso un\'interfaccia dove si incontrano due materiali con indici di rifrazione diversi. Vedere [Legge di Snell](http://en.wikipedia.org/wiki/Snell%27s_law).

<img alt="" src=images/Snells_law2_witheq.svg  style="width:" height="400px;"> 
*Legge di Snell*



## Utilizzo

<img alt="" src=images/Sketcher_SnellsLaw_Example1.png  style="width:500px;"> 
*La sequenza dei clic è indicata da frecce gialle con numeri, n1 e n2 mostrano dove sono gli indici di rifrazione*

1.  Preparare due linee per rappresentare un raggio di luce e un bordo che funga da interfaccia. Le linee dovrebbero trovarsi su lati diversi dell\'interfaccia. L\'interfaccia può essere una [linea](Sketcher_CreateLine/it.md), un [arco](Sketcher_CreateArc/it.md), una [circonferenza](Sketcher_CreateCircle/it.md) o una [conica](Sketcher_CompCreateConic/it.md).
2.  Selezionare un punto finale della prima linea, un punto finale della seconda linea e il bordo dell\'interfaccia. Prendere nota dell\'ordine di selezione dei punti finali.
3.  Esistono diversi modi per richiamare lo strumento:
    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainSnellsLaw.svg" width=16px> Vincolo di rifrazione (legge di Snell)** dal menu.
    -   Usare la scorciatoia da tastiera: **K** quindi **W**.
4.  Si apre la finestra di dialogo **Vincolo di rifrazione**.
5.  Inserire il **Rapporto n2/n1**. Dove **n2** è per il supporto in cui risiede la seconda linea selezionata e **n1** è per il supporto della prima linea.
6.  Viene aggiunto il vincolo della legge di Snell. Se richiesto, i punti finali vengono resi [coincidenti](Sketcher_ConstrainCoincident/it.md) e vincolati [sull\'interfaccia](Sketcher_ConstrainPointOnObject/it.md). Questi vincoli aggiuntivi sono chiamati [vincoli di supporto](Sketcher_helper_constraint/it.md).



## Note

-   L\'attuale vincolo Legge di Snell usa l\'equazione per un piano n1\*sin(theta1) = n2\*sin(theta2). I punti terminali devono essere resi coincidenti e posizionati sul\'interfaccia usando altri vincoli, altrimenti il comportamento sarà indefinito. I vincoli di supporto necessari vengono aggiunti automaticamente in base alle correnti coordinate degli elementi.
-   In Python i vincoli di supporto devono essere aggiunti manualmente (vedere [Script](#Script.md)).
-   I vincoli di supporto possono essere eliminati temporaneamente per consentire di spostare i punti finali, questo può essere utile nel caso in cui si voglia realizzare un raggio riflesso o dei raggi birifrangenza.
-   Diversamente dalla realtà, gli indici di rifrazione sono associati ai raggi di luce, ma non ai lati del contorno. Ciò è utile per emulare birifrangenza, costruire percorsi di diverse lunghezze d\'onda dovuti alla rifrazione, e costruire facilmente l\'angolo di insorgenza della riflessione interna totale.
-   Entrambi i raggi possono essere sullo stesso lato dell\'interfaccia, e soddisfare comunque l\'equazione del vincolo. Questo è un non senso fisico, a meno che il rapporto n2 / n1 sia 1.0, nel qual caso il vincolo emula un riflesso.
-   Come raggi sono accettati anche gli archi di cerchio e di ellisse. Ma questo è da considerarsi un non senso fisico.



## Script

Il vincoli possono essere creati da [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando il seguente comando:


```python
Sketch.addConstraint(Sketcher.Constraint('SnellsLaw',line1,pointpos1,line2,pointpos2,interface,n2byn1))
```

dove:

  - `Sketch` è un oggetto schizzo

  - `line1` e `pointpos1` sono due numeri interi che identificano il punto finale della linea nel mezzo con indice di rifrazione *n1*. `line1` è l\'indice della linea nello schizzo (il valore restituito da Sketch.addGeometry) e `pointpos1` dovrebbe essere 1 per il punto iniziale e 2 per il punto finale.

  - `line2` e `pointpos2` sono gli indici che specificano il punto finale della seconda linea (nel mezzo *n2*)

  - `interface` è l\'indice che specifica la linea che indica la posizione dell\'interfaccia tra il mezzo *n1* e il mezzo *n2*

  - `n2byn1` è un numero in virgola mobile uguale al rapporto degli indici di rifrazione *n2/n1*

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `line1`, `pointpos1`, `line2`, `pointpos2` e `interface` e contiene ulteriori esempi su come creare vincoli da script Python.

Esempio:


```python
import Sketcher
import Part
import FreeCAD

StartPoint = 1
EndPoint = 2

f = App.activeDocument().addObject("Sketcher::SketchObject","Sketch")

# add geometry to the sketch
icir = f.addGeometry(Part.Circle(App.Vector(-547.612366,227.479736,0),App.Vector(0,0,1),68.161979))
iline1 = f.addGeometry(Part.LineSegment(App.Vector(-667.331726,244.127090,0),App.Vector(-604.284241,269.275238,0)))
iline2 = f.addGeometry(Part.LineSegment(App.Vector(-604.284241,269.275238,0),App.Vector(-490.940491,256.878265,0)))
# add constraints
# helper constraints:
f.addConstraint(Sketcher.Constraint('Coincident',iline1,EndPoint,iline2,StartPoint)) 
f.addConstraint(Sketcher.Constraint('PointOnObject',iline1,EndPoint,icir)) 
# the Snell's law:
f.addConstraint(Sketcher.Constraint('SnellsLaw',iline1,EndPoint,iline2,StartPoint,icir,1.47))

App.ActiveDocument.recompute() 
```



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSnellsLaw/it
