# Macro Solid Sweep/it
{{Macro/it
|Name=Solid Sweep
|Icon=Macro_Solid_Sweep.png
|Translate=Sweep solido
|Description=Crea un solido estrudendo un profilo lungo un percorso.
|Author=Normandc
|Version=1.0
|Date=2011-12-03
|FCVersion=Tutte versione
|Download=[https://www.freecadweb.org/wiki/images/6/6d/Macro_Solid_Sweep.png Icona per la ToolBar]
}}

## Descrizione

Questa macro crea un solido estrudendo un profilo 2D lungo una traiettoria precedentemente selezionata nella vista 3D.

Gli elementi 2D possono essere creati attraverso i normali strumenti della GUI di FreeCAD.

Notare che il solido risultante non è parametrico. Se si decide di modificare il profilo o il percorso, si deve nuovamente eseguire la macro.

Nella seguente figura tutte le estrusioni sono realizzate utilizzando la stessa sagoma, ma tre percorsi diversi.

<img alt="Alcuni esempi di estrusioni, tutte sono realizzate utilizzando la stessa sezione, ma su tre diverse traiettorie." src=images/Solid_sweep.png‎  style="width:500px;">

## Utilizzo

1.  Creare due elementi 2D del tipo indicato sotto, uno per la sezione e uno per la traiettoria.
2.  Selezionare, nella [Vista ad albero](Tree_view/it.md) del progetto o nella [Vista 3D](3D_view/it.md), prima la traiettoria e poi il profilo. (**L\'ordine è importante!**):
    1.  La traiettoria
    2.  Poi il profilo

-   Aprire il [Gestore Macro](Macros/it.md)

1.  Selezionare la **Solid Sweep** macro
2.  Cliccare **Esegui**

**Risultato:** Un oggetto **Sweep** viene creato nella struttura del progetto

## Elementi 2D supportati 

-   Contorni polilinee
-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Schizzi](Sketcher_Workbench/it.md)
-   <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [BSpline](Draft_BSpline/it.md)
-   Primitive 2D del menu *Part → <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Crea Primitive](Part_Primitives/it.md)\...* (circonferenza, elica)

## Avvertenze

-   La **sezione** deve essere un profilo chiuso altrimenti il risultato non sarà un solido.
-   Non è necessario che la sezione sia posizionata sulla traiettoria, ma è preferibile che sia normale (perpendicolare) alla traiettoria.
-   La **traiettoria** può essere sia un profilo aperto che chiuso (cerchi, o segmenti e archi), ma tutti gli elementi devono essere tangenti o la forma risultante è inaspettata. Ad esempio, una traiettoria con angoli retti (come un rettangolo) non produce un solido.
-   Se il solido diventa contorto, modificare la macro e impostare il valore *isFrenet* a 0 (zero) e riprovare.
-   Impostando nella macro la variabile *makeSolid* a 0 (zero) si produce un insieme di superfici con le estremità aperte.

## La macro 

ToolBar Icon ![](images/Macro_Solid_Sweep.png )

**Macro_Solid_Sweep.FCMacro**


{{MacroCode|code=
import Part, FreeCAD, math, PartGui, FreeCADGui
from FreeCAD import Base

# get the selected objects, with first selection for the trajectory and second for the section
s = FreeCADGui.Selection.getSelection()
try:
     shape1=s[0].Shape
     shape2=s[1].Shape
except:
     print "Wrong selection"

traj = Part.Wire([shape1])
section = Part.Wire([shape2])

# create Part objec in the current document
myObject=App.ActiveDocument.addObject("Part::Feature","Sweep")

# variable makeSolid = 1 to create solid, 0 to create surfaces
makeSolid = True #1
isFrenet = True #1

# create a 3D shape and assigh it to the current document
Sweep = Part.Wire(traj).makePipeShell([section],makeSolid,isFrenet)
myObject.Shape = Sweep

}}

## Crediti

Grazie a [Wmayer](User_Wmayer.md) per il suo aiuto nella stesura di questo script.

In [questa sezione del forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=1222&start=50#p11120) si trovano due esempi di utlizzo e si trovano anche i collegamenti per scaricare i file FCStd.

Lo stesso argomento viene trattato anche in [questa discussione](http://forum.freecadweb.org/viewtopic.php?f=3&t=1461) con ragguagli su [Frenet](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).

Utilizzando una elica come traiettoria, tramite uno sweep solido si può creare la filettatura di un bullone.



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Solid Sweep/it
