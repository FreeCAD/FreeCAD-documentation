 {{VeryImportantMessage|(Novembre 2018) Queste informazioni potrebbero essere incomplete e obsolete. Per l'ultima API, vedere la pagina [https://www.freecadweb.org/api Documentazione API autogenerata].}}

Il modulo Parte è il collegamento diretto tra FreeCAD e il kernel OpenCasCade. Fornisce principalmente [TopoShapes](TopoShape_API/it.md) che è il tipo principale di oggetto utilizzato da OpenCascade. Il modulo Parte contiene anche una serie di funzioni utili per creare e manipolare le TopoShapes. Esempio: 
```python
import Part
mycube = Part.makeBox(2,2,2)
Part.show(mycube)
```


{{APIFunction|__fromPythonOCC__|OCC.Object|Metodo di aiuto per convertire una forma pythonocc in una forma interna|Una Part.Shape}}


{{APIFunction|__sortEdges__|elenco di bordi | Metodo di aiuto per ordinare un elenco di spigoli non ordinati in modo che in seguito il vertice iniziale e finale di due spigoli consecutivi coincidano geometricamente. Restituisce un singolo elenco di spigoli e l'algoritmo si arresta dopo il primo set di spigoli collegati, il che significa che l'elenco di output può essere più piccolo dell'elenco di input. L'elenco ordinato può essere utilizzato per creare un Wire | un elenco di bordi}}


{{APIFunction|__toPythonOCC__|Part.Shape|Metodo di aiuto per convertire una forma interna in una forma pythonocc|una OCC.Shape}}


{{APIFunction|cast_to_shape|Part.Shape|Cast to the actual shape type| }}


{{APIFunction|export|list,string|Esportare un elenco di oggetti in un unico file.| }}


{{APIFunction|getSortedClusters|list of edges|Metodo Helper per ordinare e raggruppare una varietà di bordi| }}


{{APIFunction|insert|string,string|Inserire il file (percorso dato come primo argomento) nel dato documento (secondo argomento).| }}


{{APIFunction|makeBox|length,width,height,[pnt,dir]|Crea una scatola situata in pnt con le dimensioni (lunghezza, larghezza, altezza). Per impostazione predefinita, pnt è in Vettore(0,0,0) e dir è Vettore(0,0,1) |la forma creata}}


{{APIFunction|makeCircle|radius,[pnt,dir,angle1,angle2]|Crea un cerchio con un dato raggio. Per impostazione predefinita pnt  è Vettore(0,0,0), dir è Vettore(0,0,1), angle1 è 0 e angle2 è 360 |la forma creata}}


{{APIFunction|makeCompound|list|Crea un composto da un elenco di forme.|la forma creata}}


{{APIFunction|makeCone|radius1,radius2,height,[pnt,dir,angle]|Crea un cono con il raggio e altezza dati. Per impostazione predefinita pnt è Vettore(0,0,0), dir è Vettore(0,0,1) e l'angolo è di 360 |la forma creata}}


{{APIFunction|makeCylinder|radius,height,[pnt,dir,angle]|Crea un cilindro con un determinato raggio e l'altezza. Per impostazione predefinita pnt è Vettore(0,0,0), dir è Vettore(0,0,1) e l'angolo è di 360 | la forma creata}}


{{APIFunction|makeHelix|pitch,height,radius,[angle,lefthand,heightstyle]|Crea una forma elicoidale con ilpasso, l'altezza e il raggio dati. Di default crea una elica cilindrica destrorsa. Il parametro angolo diverso da zero produce una spirale conica. Lefthand True (Mancina Vero) produce una elica sinistrorsa. Heightstyle si applica solo alle eliche coniche. Heightstyle False (default) fa sì che il parametro di altezza sia interpretato come la lunghezza del lato del sottostante tronco. Heightstyle Vero fa sì che il parametro di altezza sia interpretato come l'altezza verticale della traiettoria elicoidale. Pitch è il "passo metrico" (avanzamento / giro). Per l'elica conica, raggio è il raggio minore.| La forma creata}}


{{APIFunction|makeLine|(x1,y1,z1),(x2,y2,z2)|Crea una linea tra due punti |la forma creata}}


{{APIFunction|makeLoft|shapelist<profiles>,[boolean<solid>,boolean<ruled>]|Crea una forma loft utilizzando l'elenco dei profili. Facoltativamente crea un solido (es superficie o guscio) o crea una superficie rigata.|La forma creata}}


{{APIFunction|makePlane|length,width,[pnt,dir]|Crea un piano. Per impostazione predefinita pnt è Vettore(0,0,0) e dir è Vettore(0,0,1) |la forma creata}}


{{APIFunction|makePolygon|list|Rende un poligono da un elenco di vettori |la forma creata}}


{{APIFunction|makeRevolution|Curve,[vmin,vmax,angle,pnt,dir]|Rende una forma di rivoluzione ruotando la curva o una porzione di esso attorno ad un dato asse in (pnt, dir). Per impostazione predefinita Vmin / Vmax sono impostati ai limiti della curva, l'angolo è di 360, pnt è Vettore(0,0,0) e dir è Vettore(0,0,1) |la forma creata}}


{{APIFunction|makeRuledSurface|Edge or Wire,Edge or Wire|Crea una superficie rigata da due spigoli (Edge) o contorni (Wire). Se vengono utilizzati dei contorni allora questi devono avere lo stesso numero di spigoli.|La forma creata}}


{{APIFunction|makeShell|list|Crea un guscio da una lista di facce. Note: Resulting shell should be manifold.   Non-manifold shells are not well supported.|la forma creata}}


{{APIFunction|makeSolid|Part.Shape|Crea un solido da dei gusci all'interno di una forma.|la forma creata}}


{{APIFunction|makeSphere|radius,[center_pnt, axis_dir, V_startAngle, V_endAngle, U_angle]|Rende una sfera (or partial sphere) con un determinato raggio. Per impostazione predefinita center_pnt è Vector(0,0,0), axis_dir è Vector(0,0,1), V_startAngle è 0, V_endAngle è 90 e U_angle è 360|la forma creata}}


{{APIFunction|makeTorus|radius1,radius2,[pnt,dir,angle1,angle2,angle]|Fa un toro con il raggio e gli angoli dati. Per impostazione predefinita pnt è Vettore(0,0,0), dir è Vettore (0,0,1), angle1 è 0, angle2 è 360 e l'angolo è di 360 |la forma creata}}


{{APIFunction|makeTube|edge,float|Crea un tubo.|la forma creata}}


{{APIFunction|open|string|Crea un nuovo documento e carica il file nel documento.| }}


{{APIFunction|read|string|Carica il file e restituisce la forma.|una forma}}


{{APIFunction|show|shape|Aggiunge la forma al documento attivo o ne crea uno se non esiste alcun documento.| }}


 

[Category:API{{\#translation:}}](Category:API.md) [Category:Poweruser Documentation{{\#translation:}}](Category:Poweruser_Documentation.md)
