


{{TOCright}}

## Introduzione

FreeCAD può essere importato come modulo [Python](Python/it.md) in altri programmi o in una console autonoma di Python, insieme con tutti i suoi moduli e componenti. E\' anche possibile importare l\'interfaccia utente di FreeCAD come modulo Python, ma con alcune restrizioni indicate nelle [avvertenze](Embedding_FreeCAD/it#Avvertenze.md).

## Utilizzare FreeCAD senza GUI 


<div class="mw-translate-fuzzy">

Una prima, diretta, facile e utile applicazione che si può fare di questo è quella di importare i documenti di FreeCAD in un vostro programma. Nell\'esempio che segue, si importa la geometria Parte di un documento di FreeCAD in [Blender](http://www.blender.org). Ecco lo script completo. Spero che sarete impressionati dalla sua semplicità:


</div>


{{Code|lang=python|code=
<nowiki>
FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
 
def import_fcstd(filename):
   try:
       import FreeCAD
   except ValueError:
       Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
   else:
       scene = Blender.Scene.GetCurrent()
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()

def main():
   Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                        Blender.sys.makename(ext='.fcstd'))    
 
# This lets you import the script without running it
if __name__=='__main__':
   main()
</nowiki>
}}


<div class="mw-translate-fuzzy">

La prima parte importante è fare in modo che Python trovi la nostra libreria di FreeCAD. Se la trova, tutti i moduli di FreeCAD, come il modulo Parte, che useremo anche, saranno automaticamente disponibili. Così noi prendiamo semplicemente la variabile sys.path, che è il posto dove Python cerca i moduli, e vi aggiungiamo il percorso di FreeCAD lib. Questa modifica è solo temporanea, e sarà persa quando chiuderemo il nostro interprete Python. Un altro modo potrebbe essere quello di creare un collegamento alla propria libreria di FreeCAD in uno dei percorsi di ricerca di Python. Io ho posto il percorso in una costante (FREECADPATH) in modo che per un altro utente dello script sarà più facile configurarlo per il proprio sistema.


</div>


{{Code|lang=python|code=
FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
}}


<div class="mw-translate-fuzzy">

Quando siamo sicuri che la libreria viene caricata (la sequenza try/except), possiamo lavorare con FreeCAD, allo stesso modo come faremmo all\'interno dell\'interprete Python di FreeCAD. Apriamo il documento FreeCAD che è passato a noi dalla funzione main(), e facciamo una lista dei suoi oggetti. Poi, siccome abbiamo deciso di preoccuparci solo della geometria del pezzo, controlliamo se la proprietà Type di ogni oggetto contiene \"Parte\", e dopo la *tasselliamo*.


</div>


{{Code|lang=python|code=
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
}}

Il tassellamento produce una lista di vertici e un elenco di facce definite dai vertici indicizzati. Questo è perfetto, poiché è esattamente lo stesso modo in cui Blender definisce i Mesh. Quindi, il nostro compito è ridicolmente semplice, basta aggiungere il contenuto di entrambi gli elenchi ai vertici e alle facce di una mesh di Blender. Quando tutto è fatto, basta ridisegnare lo schermo, e questo è tutto!


{{Code|lang=python|code=
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()
}}


<div class="mw-translate-fuzzy">

Ovviamente questo script è molto semplice (in realtà ne ho fatto uno più avanzato [qui](http://yorik.orgfree.com/scripts/import_freecad.py)), è probabile che si voglia estenderlo, per esempio per importare anche oggetti mesh, o importare la geometria di una parte che non ha facce, o importare altri formati di file che FreeCAD è in grado di leggere. Si potrebbe anche voler esportare la geometria in un documento di FreeCAD, cosa che può essere fatto allo stesso modo. Si potrebbe anche voler costruire un dialogo per permettere all\'utente di scegliere cosa importare, ecc.. La bellezza di tutto questo risiede proprio nel fatto che lasciate lavorare FreeCAD in ombra, mentre i suoi risultati sono presentati nel programma di vostra scelta.


</div>


**Note:**

checkout [Headless FreeCAD](Headless_FreeCAD.md) for running FreeCAD without the GUI.

## Utilizzare FreeCAD con GUI 

Dalla versione 4.2, Qt ha la capacità affascinante di incorporare i plug-in della GUI dipendenti da Qt in applicazioni ospite (host) non-Qt e condividere il ciclo di eventi dell\'ospite.

In particolare, per FreeCAD questo significa che esso può essere importato (incorporato) all\'interno di un\'altra applicazione con tutta la sua interfaccia utente dentro un\'altra applicazione ospite la quale ha, a questo punto, il pieno controllo di FreeCAD.

L\'intero codice python per ottenere questo ha solo due linee:


```python
import FreeCADGui 
FreeCADGui.showMainWindow()
```

Se l\'applicazione ospite è basata su Qt, allora questa soluzione dovrebbe funzionare su tutte le piattaforme che supportano Qt. Tuttavia, l\'ospite deve basarsi sulla stessa versione Qt di FreeCAD perché altrimenti si potrebbe incorrere in errori di esecuzione inaspettati.

Per le applicazioni non-Qt, tuttavia, ci sono alcune limitazioni di cui è necessario essere a conoscenza. Questa soluzione probabilmente non funziona con tutti gli altri toolkit. Per Windows funziona fintanto che l\'applicazione ospite è basata direttamente su Win32 o su qualsiasi altro toolkit che utilizza internamente l\'API Win32, come wxWidgets, MFC o WinForms. Al fine di farla funzionare sotto X11 l\'applicazione ospite deve linkare la libreria \"glib\".

Notare che, questa soluzione, naturalmente, non funziona per nessuna applicazione da console perché non c\'è nessun ciclo di eventi in esecuzione.

## Avvertenze

Anche se è possibile importare FreeCAD con un interprete Python esterno, questo non è uno scenario di utilizzo comune e richiede una certa cura. In generale, è meglio usare il Python incluso con FreeCAD, eseguire FreeCAD da linea di comando, o come un sottoprocesso. Vedere [Avvio e configurazione](Start_up_and_Configuration/it.md) per maggiori informazioni sulle ultime due opzioni.

Dato che il modulo Python di FreeCAD viene compilato da C ++ (invece di essere un puro modulo Python), esso può essere importato solo da un interprete Python compatibile. Generalmente questo significa che l\'interprete Python deve essere compilato con lo stesso compilatore C che è stato utilizzato per costruire FreeCAD. Le informazioni sul compilatore utilizzato per costruire un interprete Python (compreso quello costruito con FreeCAD) si possono trovare nel seguente modo: 
```python
>>> import sys
>>> sys.version
'2.7.13 (default, Dec 17 2016, 23:03:43) \n[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]'
```

## Related

-   [Headless FreeCAD](Headless_FreeCAD.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
