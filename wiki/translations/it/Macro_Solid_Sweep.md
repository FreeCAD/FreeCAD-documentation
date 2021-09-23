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


<div class="mw-translate-fuzzy">

## Come si usa 

-   Creare due elementi 2D del tipo indicato sotto, uno per la sezione e uno per la traiettoria.
-   Selezionare, nella struttura del progetto o nella vista 3D, prima la traiettoria e poi il profilo. L\'ordine è importante!
-   Aprire Gestione Macro, selezionare la macro e fare clic su \"Esegui\".
-   Nella struttura del progetto viene creato un oggetto Sweep.


</div>


<div class="mw-translate-fuzzy">

## Elementi 2D supportati 

-   Contorni polilinee
-   <img alt="" src=images/Sketcher_NewSketch.png  style="width:32px;"> [Schizzi](Sketcher_Workbench/it.md)
-   ![](images/Draft_BSpline.png ) [BSpline](Draft_BSpline/it.md)
-   Primitive 2D del menu *Part → <img alt="" src=images/Part_CreatePrimitives.png  style="width:32px;"> [Crea Primitive](Part_CreatePrimitives/it.md)\...* (circonferenza, elica)


</div>

## Avvertenze

-   La **sezione** deve essere un profilo chiuso altrimenti il risultato non sarà un solido.
-   Non è necessario che la sezione sia posizionata sulla traiettoria, ma è preferibile che sia normale (perpendicolare) alla traiettoria.
-   La **traiettoria** può essere sia un profilo aperto che chiuso (cerchi, o segmenti e archi), ma tutti gli elementi devono essere tangenti o la forma risultante è inaspettata. Ad esempio, una traiettoria con angoli retti (come un rettangolo) non produce un solido.
-   Se il solido diventa contorto, modificare la macro e impostare il valore *isFrenet* a 0 (zero) e riprovare.
-   Impostando nella macro la variabile *makeSolid* a 0 (zero) si produce un insieme di superfici con le estremità aperte.

## La macro 

ToolBar Icon ![](images/Macro_Solid_Sweep.png )

**Macro\_Solid\_Sweep.FCMacro**


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

Grazie a [Wmayer](User:Wmayer.md) per il suo aiuto nella stesura di questo script.

In [questa sezione del forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=1222&start=50#p11120) si trovano due esempi di utlizzo e si trovano anche i collegamenti per scaricare i file FCStd.

Lo stesso argomento viene trattato anche in [questa discussione](http://forum.freecadweb.org/viewtopic.php?f=3&t=1461) con ragguagli su [Frenet](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).

Utilizzando una elica come traiettoria, tramite uno sweep solido si può creare la filettatura di un bullone.
