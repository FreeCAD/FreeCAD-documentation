# TopoShape API/it
**(novembre 2018) Queste informazioni potrebbero essere incomplete e obsolete. Per l'API più recente, consulta la [https://www.freecadweb.org/api documentazione API generata automaticamente].**

Il TopoShape è l\'oggetto madre del Part Module. Tutti i tipi di forma (filo, faccia, solido, ecc\...) del modulo Parte sono TopoShapes e condividono i seguenti attributi e metodi. Esempio: 
```python
import Part
sh = Part.makeBox(10,10,10)
print sh.Faces
for f in sh.Faces:
   print f.Edges
```


{{APIProperty|Area|L'area totale delle facce della shape.}}


{{APIProperty|BoundBox|Il BoundBox dell'oggetto}}


{{APIProperty|CenterOfMass|Il centro di massa del sistema attuale. Se il campo gravitazionale è uniforme, è il centro di gravità. Le coordinate restituite per il centro di massa sono espresse nel sistema di coordinate cartesiane assolute.}}


{{APIProperty|CompSolids|Elenca le shape successive in questa shape.}}


{{APIProperty|Compounds|Elenca i Coumpounds in questa shape.}}


{{APIProperty|Edges|Elenca gli Edges in questa shape.}}


{{APIProperty|Faces|Elenca le face in questa shape.}}


{{APIProperty|Length|Lunghezza totale degli edges della shape.}}


{{APIProperty|Matrix|L'attuale trasformazione dell'oggetto come matrice}}


{{APIProperty|Orientation|l'orientamento della shape.}}


{{APIProperty|Placement|L'attuale trasformazione dell'oggetto come placement}}


{{APIProperty|ShapeType|Il tipo di shape.}}


{{APIProperty|Shells|Elenca le shape successive in questa shape.}}


{{APIProperty|Solids|Elenco delle shape successive in questa shape.}}


{{APIProperty|Vertexes|Elenco dei vertexes in questa shape.}}


{{APIProperty|Volume|Volume totale dei solid della shape.}}


{{APIProperty|Wires|Elenco dei wire in ​​questa forma.}}


{{APIFunction|approximate| |Approssima una curva B-Spline da questo wire|un oggetto BSplineCurve}}


{{APIFunction|check| |Controlla la shape e segnala gli errori nella struttura della shape. Questo è un controllo più dettagliato rispetto a come fatto in isValid().| }}


{{APIFunction|common|TopoShape|Intersezione di questo e una data topo-shape.|a TopoShape}}


{{APIFunction|complement| |Calcola il complemento dell'orientamento di questa shape, ovvero inverte lo stato interno/esterno dei boundary di questa shape.|a TopoShape}}


{{APIFunction|copy| |Crea una copia di questa shape|a TopoShape}}


{{APIFunction|cut|TopoShape|Differenza tra questa e una determinata topo-shape.|a TopoShape}}


{{APIFunction|distToShape| TopoShape |Calcola la distanza minima tra questo e una data TopoShape.|float<minimum distance>,list<nearest points>,list<nearest subshapes & parameters> }}


{{APIFunction|exportBrep| string |Esporta il contenuto di questa shape in un file BREP. BREP è un formato nativo di CasCade.| }}


{{APIFunction|exportIges| string |Esporta il contenuto di questa shape in un file IGES.| }}


{{APIFunction|exportStep| string |Esporta il contenuto di questa shape in un file STEP.| }}


{{APIFunction|exportStl| string |Esporta il contenuto di questa shape in un file mesh STL.| }}


{{APIFunction|extrude|Vector|Estrude la shape lungo una direzione.|a TopoShape}}


{{APIFunction|fuse|TopoShape|Unione di questa e di una data topo shape.|a TopoShape}}


{{APIFunction|getAllDerivedFrom| |Restituisce tutte le discendenze di questo tipo di oggetto|a list}}


{{APIFunction|hashCode| |Questo valore viene calcolato dal valore del riferimento alla shape sottostante e dalla posizione. L'orientamento non viene preso in considerazione.|a string}}


{{APIFunction|isClosed| |Controlla se la shape è chiusa.|a boolean}}


{{APIFunction|isDerivedFrom|string|Restituisce vero se il tipo indicato è un padre|boolean}}


{{APIFunction|isEqual|TopoShape|Restituisce vero se entrambe le shape condividono la stessa TShape, hanno la stessa posizione e hanno lo stesso orientamento.|a boolean}}


{{APIFunction|isInside|Vector,float,Boolean|Controlla se un point si trova all'interno di un solid con una certa tolleranza. Se il 3° parametro è True un point su una face è considerato interno|a boolean}}


{{APIFunction|isNull| |Controlla se la shape è null.|a boolean}}


{{APIFunction|isPartner|TopoShape|Restituisce True se entrambe le shape condividono la stessa TShape, ma possono avere una Location diversa e un Orientation diverso.|a boolean}}


{{APIFunction|isSame|TopoShape|Controlla se entrambe le shape condividono la stessa geometria, vero se entrambe le shape condividono la stessa TShape e hanno la stessa Location, ma potrebbero avere un Orientation diverso.|a boolean}}


{{APIFunction|isValid| |Controlla se la shape è valida, cioè né nulla, né vuota né corrotta.|a boolean}}


{{APIFunction|makeFillet|float,TopoShape|Restituisce un nuovo oggetto basato su una TopoShape, ma con un raccordo di raggio "float" applicato a ciascun bordo.|a TopoShape}}


{{APIFunction|makeHomogenousWires|wire|Rende omogeneo questo e il wire dato in modo che abbiano lo stesso numero di bordi| a wire}}


{{APIFunction|makeOffset|float|Compensa la shape di una determinata quantità|a TopoShape}}


{{APIFunction|makePipe|wire|Crea una pipe scorrendo lungo un wire.|a TopoShape}}


{{APIFunction|makePipeShell|wire|Crea un loft definito da profili lungo una wire.|a TopoShape}}


{{APIFunction|makeShapeFromMesh|mesh|Crea una shape composta dai dati mesh. Nota: questo dovrebbe essere usato solo per mesh piuttosto piccole.|a TopoShape}}


{{APIFunction|makeThickness|list,float,float|Crea un solid cavo partendo da un solid iniziale e da una serie di face su questo solid che devono essere rimosse. Le restanti face del solid diventano le pareti del solid cavo, il cui spessore è definito al momento della costruzione. Gli argomenti da passare sono un elenco di face da rimuovere, lo spessore dei muri e un valore di tolleranza.|a TopoShape}}


{{APIFunction|nullify| |Distrugge il riferimento alla shape sottostante archiviata in questa shape. Di conseguenza, questa shape diventa nulla.|}}


{{APIFunction|project|TopoShape|Proietta una shape su questa shape|a TopoShape}}


{{APIFunction|read|string|Legge un file IGES, STEP o BREP.|a TopoShape}}


{{APIFunction|reverse| |Inverte l'orientamento di questa forma.| }}


{{APIFunction|revolve|Vector, Vector, float|Ruota la shape attorno a un asse di un determinato angolo. es: Part.revolve(Vector(0,0,0),Vector(0,0,1),360) ruota la shape attorno all'asse Z di 360 gradi.|a TopoShape}}


{{APIFunction|rotate|Vector<position>, Vector<direction>, float<angle>|Ruota questa shape in base ai gradi angolari attorno a un asse specificato dalla posizione e dalla direzione. es: Shp.rotate(Vector(0,0,0),Vector(0,0,1),180) ruota la shape attorno all'asse Z di 180 gradi.| }}


{{APIFunction|scale|float<factor>, [Vector<centre>]|Ridimensiona uniformemente questa forma in base ad un fattore. Facoltativamente specificare il centro della trasformazione in scala.| }}


{{APIFunction|section|TopoShape|Sezione di questo con una data topo-shape.|a TopoShape}}


{{APIFunction|sewShape| |Cuce la forma se c'è uno spazio vuoto.| }}


{{APIFunction|tessellate|float|Tassella la forma e restituisce un elenco di vertice e indici di face. Il float dato è la tolleranza.|a list}}


{{APIFunction|toNurbs| |Conversione della geometria completa di una shape in geometria NURBS. Ad esempio, tutte le curve che supportano edge della forma base vengono convertite in curve BSpline e tutte le superfici che supportano le sue face vengono convertite in superfici BSpline.|a NURBS curve}}


{{APIFunction|transformGeometry|matrix|Applica la trasformazione geometrica su una copia della shape. La trasformazione da applicare è definita come matrice 4x4. La geometria sottostante delle seguenti shape può trasformarsi in una curva che supporta un bordo della shape o una superficie che supporta una face della shape. Ad esempio, un cerchio può essere trasformato in un'ellisse quando si applica una trasformazione di affinità. Può anche succedere che il cerchio venga rappresentato come una curva b-spline. La trasformazione viene applicata a tutte le curve che supportano i bordi della shape e a tutte le superfici che supportano le face della shape. Nota: se si desidera trasformare una shape senza modificarne la geometria sottostante, utilizzare i metodi trasla o ruota.|a TopoShape}}


{{APIFunction|transformShape|matrix|Applica la trasformazione su una shape senza modificare la geometria sottostante.| }}


{{APIFunction|translate|Vector|Applica la traslazione alla posizione corrente di questa forma.| }}


{{APIFunction|writeInventor| |Scrive la mesh nel formato OpenInventor in una stringa.|a string}}

Alcuni attributi e metodi si applicano solo a determinati TopoShapes. Questi elementi si applicano ai bordi (TopoShapeEdge).


{{APIProperty|FirstParameter|Il valore del parametro a un'estremità di Edge. Non necessariamente al vertice[0]. [http://en.wikipedia.org/wiki/Parametric_equations See Parametric Equations]}}


{{APIProperty|LastParameter|Il valore del parametro all'altra estremità di Edge. Non necessariamente al vertice[1].}}


{{APIFunction|getParameterByLength|Float|Mappa l'intervallo [0,Length] sull'intervallo [FirstParameter,LastParameter]|Float }}


{{APIFunction|valueAt|Float|Restituisce il vettore 3D corrispondente al valore di un parametro.|Vector}}


{{APIFunction|parameterAt|Vertex,[Face]|Restituisce il valore del parametro corrispondente a un vertice (punto 3D).|Float}}


{{APIFunction|tangentAt|Float|Restituisce il vettore di direzione della tangente al bordo in corrispondenza del valore di un parametro (se esiste).|Vector}}


{{APIFunction|normalAt|Float|Restituisce il vettore di direzione della normale al bordo in corrispondenza del valore di un parametro (se esiste in modo univoco).|Vector}}


{{APIFunction|curvatureAt|Float|Restituisce la curvatura del bordo in corrispondenza di un valore del parametro.|Float}}


{{APIFunction|centerOfCurvatureAt|Float|Restituisce il centro (punto 3D) del cerchio osculatore in corrispondenza di un valore del parametro.|Vector}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > TopoShape API/it
