---
- GuiCommand:/it
   Name:Constraint SnellsLaw
   Name/it:Rifrazione
   MenuLocation:Sketch → Sketcher Constraints → Rifrazione (Legge di Snell)
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   Version:0.15
---

# Sketcher ConstrainSnellsLaw/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Vincola due linee a disporsi secondo la legge della rifrazione di un raggio di luce che attraversa un\'interfaccia, ovvero nella transizione tra due materiali con differenti indici di rifrazione. Per maggiori informazioni si può consultare la pagina sulla [Legge di Snell](http://http://it.wikipedia.org/wiki/Legge_di_Snell) di Wikipedia. <img alt="Snell\'s law" src=images/Snells_law2_witheq.svg  style="width:200px;"> 


</div>

<img alt="" src=images/Snells_law2_witheq.svg  style="width:" height="400px;">



*Snell's Law*

## Utilizzo

<img alt="" src=images/Sketcher_SnellsLaw_Example1.png  style="width:500px;"> 
*The sequence of clicks is indicated by yellow arrows with numbers. n1, n2 are only labels to show where the indices of refraction are.*


<div class="mw-translate-fuzzy">

-   Servono due linee che rappresentino un raggio di luce e una curva che funga da interfaccia. Le linee devono essere su lati diversi dell\'interfaccia.
-   Selezionare l\'estremità di una linea, il punto finale di un\'altra linea e il bordo dell\'interfaccia. L\'interfaccia può essere una linea, un cerchio, un arco, una ellisse o un arco di ellisse. Stare attenti all\'ordine di selezione dei punti finali.
-   Richiamare il vincolo. Appare una finestra di dialogo in cui si deve indicare il rapporto tra gli indici di rifrazione n2/n1. L\'indice n2 si riferisce al mezzo in cui risiede la linea del secondo punto finale selezionato, n1 si riferisce alla prima linea.
-   Prima di applicare il vincolo legge di Snell, i punti finali devono essere resi coincidenti e vincolati sull\'interfaccia, se non lo sono.


</div>


<div class="mw-translate-fuzzy">

Notare che ci sono diversi [autovincoli](Sketcher_helper_constraint/it.md) che vengono aggiunti automaticamente (punto-su-oggetto, coincidenza, ecc.). Essi possono essere eliminati se causano la ridondanza, o essere aggiunti manualmente se non sono stati aggiunti automaticamente. Per l\'attuale vincolo di Rifrazione, i punti finali delle linee devono coincidere e trovarsi sull\'interfaccia, altrimenti il suo comportamento è imprevedibile.


</div>


<div class="mw-translate-fuzzy">

Utilizzando lo strumento [polilinea](Sketcher_CreatePolyline/it.md) <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;">, è possibile velocizzare il disegno dei raggi di luce. In questo caso, è possibile selezionare due punti finali coincidenti con il rettangolo di selezione.


</div>

## Remarks


<div class="mw-translate-fuzzy">

## Osservazioni

-   L\'attuale vincolo Legge di Snell usa l\'equazione per un piano n1\*sin(theta1) = n2\*sin(theta2). I punti terminali devono essere resi coincidenti e posizionati sul\'interfaccia usando altri vincoli. I vincoli di supporto necessari vengono aggiunti automaticamente in base alle correnti coordinate degli elementi.
-   Python non aggiunge automaticamente i vincoli di supporto. Essi devono essere aggiunti manualmente con lo script (vedere l\'esempio nella sezione Scripting).
-   I vincoli di supporto possono essere eliminati temporaneamente per consentire di spostare i punti finali, questo può essere utile nel caso in cui si voglia realizzare un raggio riflesso o dei raggi birifrangenza.
-   Diversamente dalla realtà, gli indici di rifrazione sono associati ai raggi di luce, ma non ai lati del contorno. Ciò è utile per emulare birifrangenza, costruire percorsi di diverse lunghezze d\'onda dovuti alla rifrazione, e costruire facilmente l\'angolo di insorgenza della riflessione interna totale.
-   Entrambi i raggi possono essere sullo stesso lato dell\'interfaccia, e soddisfare comunque l\'equazione del vincolo. Questo è un non senso fisico, a meno che il rapporto n2 / n1 sia 1.0, nel qual caso il vincolo emula un riflesso.
-   Come raggi sono accettati anche gli archi di cerchio e di ellisse (non senso fisico).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Scripting 

I vincoli possono essere creati con le [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) utilizzando la seguente funzione:


</div>


```python
Sketch.addConstraint(Sketcher.Constraint('SnellsLaw',line1,pointpos1,line2,pointpos2,interface,n2byn1))
```


<div class="mw-translate-fuzzy">

Dove:

  - Sketch è un oggetto sketch

  - line1 e pointpos1 sono due numeri interi che indicano il punto finale della linea nel mezzo con l\'indice di rifrazione *n1*. line1 è l\'indice della linea nello sketch (il valore, restituito da Sketch.addGeometry), e pointpos1 dovrebbe essere 1 per il punto iniziale e 2 per il punto finale.

  - line2 e pointpos2 sono gli indici che specificano i punti della seconda linea (nel mezzo *n2*)

  - n2byn1 è un numero a virgola mobile dato dal rapporto tra gli indici di rifrazione *n2*/*n1*


</div>

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `line1`, `pointpos1`, `line2`, `pointpos2` and `interface` and contains further examples on how to create constraints from Python scripts.

Esempio:


```python
import Sketcher
import Part
import FreeCAD

StartPoint = 1
EndPoint = 2
MiddlePoint = 3

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


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSnellsLaw/it
