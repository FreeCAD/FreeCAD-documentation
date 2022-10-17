# Path scripting/it
{{TOCright}}

## Introduzione

L\'ambiente Path offre strumenti per importare, creare, manipolare e esportare [percorsi delle macchine utensili](http   *//en.wikipedia.org/wiki/G-code) in FreeCAD. Con esso, l\'utente è in grado di importare, visualizzare e modificare i programmi GCode esistenti, generare percorsi di forme 3D, ed esportare questi percorsi utensile in Gcode.


<div class="mw-translate-fuzzy">

Allo stato attuale, però, lo sviluppo dell\'ambiente Path è appena iniziato, e non offre la funzionalità molto avanzate che si trovano in alcune alternative commerciali. Tuttavia, la sua ampia interfaccia di script Python rende facile modificare o sviluppare degli strumenti più potenti, e quindi per ora è rivolto più agli utenti con una certa conoscenza di script Python che agli utenti finali.


</div>

## Avvio rapido 

Gli oggetti Path (percorso) di FreeCAD sono fatti di una sequenza di comandi di movimento. Un utilizzo tipico è questo   *


```python
>>> import Path
>>> c1 = Path.Command("g1x1")
>>> c2 = Path.Command("g1y4")
>>> c3 = Path.Command("g1 x2 y2") # spaces end newlines are not considered
>>> p = Path.Path([c1,c2,c3])
>>> o = App.ActiveDocument.addObject("Path   *   *Feature","mypath")
>>> o.Path = p
>>> print p.toGCode()
```


<div class="mw-translate-fuzzy">

## Formato del GCode all\'interno di FreeCAD 


</div>

Un concetto preliminare che importante da afferrare. La maggior parte della realizzazione sottostanti si basa prevalentemente sui comandi di movimento che hanno gli stessi nomi dei comandi GCode, ma non sono destinati ad avvicinarsi all\'implementazione di un particolare controller. Abbiamo scelto nomi come \'G0\' per rappresentare i movimento in \'rapida\' o \'G1\' per rappresentare i movimenti di \'alimentazione\' per motivi di prestazioni (efficienza nel salvataggio dei file) e per ridurre al minimo il lavoro necessario per tradurre in/da altri formati GCode. Dal momento che il mondo CNC parla migliaia di dialetti GCode, abbiamo scelto di iniziare con un sottoinsieme molto semplificato di esso. Si potrebbe descrivere il formato GCode di FreeCAD come una forma \"macchina-agnostica\" di GCode.

All\'interno dei file .FCStd, i dati Path vengono salvati direttamente in quella forma di GCode.

Tutte le traduzioni dai/nei dialetti del GCode di FreeCAD vengono effettuate tramite pre e post script. Ciò significa che, se si desidera lavorare con una macchina che utilizza uno specifico controller LinuxCNC, Fanuc, Mitusubishi o HAAS, ecc, si deve usare (o scrivere se è inesistente) un post processore per quel particolare controllo (vedere più avanti la sezione \"Importare ed esportare GCode).


<div class="mw-translate-fuzzy">

### Riferimenti GCode 


</div>

Le seguenti regole e linee guida definiscono il sottoinsieme di GCode utilizzato all\'interno di FreeCAD   *

-   I dati GCode, all\'interno degli oggetti Path di FreeCAD, sono separati in \"Commands\" (comandi). Un comando è definito dal nome del comando, che deve iniziare con G o M, e da argomenti(opzionali), che sono nella forma Lettera = Float (flottante), ad esempio X 0.02 o Y 3.5 o F 300. Questi sono esempi di tipici comandi Gcode in FreeCAD   *


<div class="mw-translate-fuzzy">

G0 X2.5 Y0 (Il nome del comando è G0, gli argomenti sono X=2.5 e Y=0)


</div>


<div class="mw-translate-fuzzy">

G1 X30 (Il nome del comando è G1, l\'unico argomento è X=30)


</div>


<div class="mw-translate-fuzzy">

G90 (Il nome del comando è G90, non ci sono argomentis)


</div>

-   Per la parte numerica di un comando G o M, sono supportate sia la forma \"G1\" sia \"G01\" .
-   In questo momento sono supportati solo i comandi che iniziano per G o M.
-   Per ora, sono accettati solo i millimetri. G20/G21 non sono considerati.
-   Gli argomenti sono sempre in ordine alfabetico. Questo significa che se si crea un comando con \"G1 X2 Y4 F300\", viene memorizzato come \"G1 F300 X2 Y4\"
-   Gli argomenti non possono essere ripetuti all\'interno di uno stesso comando. Ad esempio, \"G1 X1 X2 Y2 Y3\" non funziona. Deve essere diviso in due comandi, per esempio   * \"G1 X1 Y2, Y3 G1 X2\"
-   Gli argomenti X, Y, Z, A, B, C sono assoluti o relativi, secondo la modalità attiva G90/G91. Predefinito (se non specificato) è assoluto.
-   I, J, K sono sempre relativi all\'ultimo punto. K può essere omesso.
-   X, Y, o Z (e A, B, C) possono essere omessi. In questo caso, sono mantenuti le precedenti coordinate X, Y o Z.
-   I comandi GCode diversi da quelli elencati nella seguente tabella sono supportati, cioè, vengono salvati all\'interno dei dati del percorso ( naturalmente, a patto che siano conformi alle regole di cui sopra), ma non producono alcun risultato visibile sullo schermo. Ad esempio, è possibile aggiungere un comando G81, esso viene memorizzato, ma non visualizzato.

### Elenco dei comandi Gcode attualmente supportati 


<div class="mw-translate-fuzzy">

  Comando         Descrizione           Argomenti supportati
    
  G0              rapida                X,Y,Z,A,B,C
  G1              avanzamento normale   X,Y,Z,A,B,C
  G2              arco orario           X,Y,Z,A,B,C,I,J,K
  G3              arco antiorario       X,Y,Z,A,B,C,I,J,K
  G81, G82, G83   foratura              X,Y,Z,R,Q
  G90             coordinate assolute   
  G91             coordinate relative   
  (Message)       commento              


</div>

## L\'oggetto Command 

L\'oggetto Command rappresenta un comando Gcode. Ha tre attributi   * Name, Parameters e Placement (Nome,Parametri e posizione), e due metodi   * toGCode() e setFromGCode(). Internamente, contiene solo un nome e un dizionario di parametri. Il resto (posizionamento e gcode) viene calcolato da/a questi dati.


```python
>>> import Path
>>> c=Path.Command()
>>> c
Command  ( )
>>> c.Name = "G1"
>>> c
Command G1 ( )
>>> c.Parameters= {"X"   *1,"Y"   *0}
>>> c
Command G1 ( X   *1 Y   *0 )
>>> c.Parameters
{'Y'   * 0.0, 'X'   * 1.0}
>>> c.Parameters= {"X"   *1,"Y"   *0.5}
>>> c
Command G1 ( X   *1 Y   *0.5 )
>>> c.toGCode()
'G1X1Y0.5'
>>> c2=Path.Command("G2")
>>> c2
Command G2 ( )
>>> c3=Path.Command("G1",{"X"   *34,"Y"   *1.2})
>>> c3
Command G1 ( X   *34 Y   *1.2 )
>>> c3.Placement
Placement [Pos=(34,1.2,0), Yaw-Pitch-Roll=(0,0,0)]
>>> c3.toGCode()
'G1X34Y1.2'
>>> c3.setFromGCode("G1X1Y0")
>>> c3
Command G1 [ X   *1 Y   *0 ]
>>> c4 = Path.Command("G1X4Y5")
>>> c4
Command G1 [ X   *4 Y   *5 ]
>>> p1 = App.Placement()
>>> p1.Base = App.Vector(3,2,1)
>>> p1
Placement [Pos=(3,2,1), Yaw-Pitch-Roll=(0,0,0)]
>>> c5=Path.Command("g1",p1)
>>> c5
Command G1 [ X   *3 Y   *2 Z   *1 ]
>>> p2=App.Placement()
>>> p2.Base = App.Vector(5,0,0)
>>> c5
Command G1 [ X   *3 Y   *2 Z   *1 ]
>>> c5.Placement=p2
>>> c5
Command G1 [ X   *5 ]
>>> c5.x
5.0
>>> c5.x=10
>>> c5
Command G1 [ X   *10 ]
>>> c5.y=2
>>> c5
Command G1 [ X   *10 Y   *2 ]
```

## L\'oggetto Path 

L\'oggetto Path contiene un elenco di comandi


```python
>>> import Path
>>> c1=Path.Command("g1",{"x"   *1,"y"   *0})
>>> c2=Path.Command("g1",{"x"   *0,"y"   *2})
>>> p=Path.Path([c1,c2])
>>> p
Path [ size   *2 length   *3 ]
>>> p.Commands
[Command G1 [ X   *1 Y   *0 ], Command G1 [ X   *0 Y   *2 ]]
>>> p.Length
3.0
>>> p.addCommands(c1)
Path [ size   *3 length   *4 ]
>>> p.toGCode()
'G1X1G1Y2G1X1'

lines = """
G0X-0.5905Y-0.3937S3000M03
G0Z0.125
G1Z-0.004F3
G1X0.9842Y-0.3937F14.17
G1X0.9842Y0.433
G1X-0.5905Y0.433
G1X-0.5905Y-0.3937
G0Z0.5
"""

slines = lines.split('\n')
p = Path.Path()
for line in slines   *
    p.addCommands(Path.Command(line))

o = App.ActiveDocument.addObject("Path   *   *Feature","mypath")
o.Path = p

# but you can also create a path directly form a piece of gcode.
# The commands will be created automatically   *

p = Path.Path()
p.setFromGCode(lines)
```

Come scorciatoia, un oggetto Path può anche essere creato direttamente da una sequenza completa di GCode. Sarà diviso automaticamente in una sequenza di comandi.


```python
>>> p = Path.Path("G0 X2 Y2 G1 X0 Y2")
>>> p
Path [ size   *2 length   *2 ]
```

## La funzione Path 

La funzione Path è un oggetto documento di FreeCAD, che contiene un percorso, e lo rappresenta nella vista 3D.


```python
>>> pf = App.ActiveDocument.addObject("Path   *   *Feature","mypath")
>>> pf
<Document object>
>>> pf.Path = p
>>> pf.Path
Path [ size   *2 length   *2 ]
```

La funzione Path detiene inoltre una proprietà Placement. Cambiando il valore del posizionamento si cambia la posizione della funzionalità nella vista 3D, anche se le informazioni sul percorso sono invariate. La trasformazione è puramente visiva. Ciò consente, ad esempio, di creare un percorso attorno a una faccia che ha un particolare orientamento nel modello, e che non è lo stesso orientamento che il materiale da tagliare avrà sulla macchina CNC.

Tuttavia, i Path Compounds possono usufruire del Placement (posizionamento) dei propri figli (vedi sotto).


<div class="mw-translate-fuzzy">

## Gli utensili e la tabella utensili 


</div>

**NOTE   *** This type of tool usage is depreciated as of the 0.19 official release. In 0.19 the new ToolBit tool system was implemented to supersede this older, Legacy, system. Therefore, coding has changed from what is represented below. Please visit [Path Tools](Path_Tools.md) page for more information.

===Scripting \<= 0.18===

L\'oggetto strumento contiene le definizioni di un utensile CNC. L\'oggetto Tooltable contiene un elenco ordinato di strumenti. Le Tooltable sono unite come una proprietà alle funzioni Path Project, e possono anche essere modificate tramite l\'interfaccia grafica, facendo doppio clic su un progetto nella vista ad albero, e facendo clic sul pulsante \"Modifica tooltable\" nelle vista azioni che viene aperta.

Da questa finestra, le tooltable possono essere importate dai formati .xml di FreeCAD e .tooltable di HeeksCad, ed esportate nel formato .xml di FreeCAD.


```python
>>> import Path
>>> t1=Path.Tool()
>>> t1
Tool Default tool
>>> t1.Name = "12.7mm Drill Bit"
>>> t1
Tool 12.7mm Drill Bit
>>> t1.ToolType
'Undefined'
>>> t1.ToolType = "Drill"
>>> t1.Diameter= 12.7
>>> t1.LengthOffset = 127
>>> t1.CuttingEdgeAngle = 59
>>> t1.CuttingEdgeHeight = 50.8
>>> t2 = Path.Tool("my other tool",tooltype="EndMill",diameter=10)
>>> t2
Tool my other tool
>>> t2.Diameter
10.0
>>> table = Path.Tooltable()
>>> table
Tooltable containing 0 tools
>>> table.addTools(t1)
Tooltable containing 1 tools
>>> table.addTools(t2)
Tooltable containing 2 tools
>>> table.Tools
{1   * Tool 12.7mm Drill Bit, 2   * Tool my other tool}
>>> 
```

## Funzioni

### La funzione Path Compound 

Lo scopo di questa funzione è quello di raccogliere uno o più percorsi utensile e di associarlo/i con una tooltable. La funzione Compound si comporta anche come un gruppo standard di FreeCAD, in modo da poter aggiungere o rimuovere oggetti direttamente dalla visualizzazione struttura. È inoltre possibile riordinare gli elementi facendo doppio clic sull\'oggetto Compound nella struttura ad albero, e riordinare gli elementi nella vista azioni che viene aperta.


```python
>>> import Path
>>> p1 = Path.Path("G1X1")
>>> o1 = App.ActiveDocument.addObject("Path   *   *Feature","path1")
>>> o1.Path=p1
>>> p2 = Path.Path("G1Y1")
>>> o2 = App.ActiveDocument.addObject("Path   *   *Feature","path2")
>>> o2.Path=p2
>>> o3 = App.ActiveDocument.addObject("Path   *   *FeatureCompound","compound")
>>> o3.Group=[o1,o2]
```

Una caratteristica importante di Path Compounds è la possibilità di tenere conto o no della posizione dei percorsi dei loro figli, impostando la loro proprietà UsePlacements su True o False. In caso contrario, i dati Percorso dei loro figli saranno semplicemente aggiunti in sequenza. Se True, ogni comando dei percorsi figli, qualora contengano informazioni di posizione (G0, G1, ecc ..), prima di essere aggiunto verrà trasformato dal posizionamento.

Creating a compound with just one child path allows you therefore to turn the child path\'s Placement \"real\" (it affects the Path data).

### La funzione Path Project 

Il progetto Path è un tipo di Compound esteso, che ha un paio di ulteriori proprietà correlate alla macchina, come una tooltable. È fatto principalmente per essere il principale tipo di oggetto che si desidera esportare in Gcode quando la configurazione dell\'intero percorso è pronta. L\'oggetto Project è codificato in python, per cui il suo meccanismo di creazione è un po \'diverso   *


```python
>>> from PathScripts import PathProject
>>> o4 = App.ActiveDocument.addObject("Path   *   *FeatureCompoundPython","prj")
>>> PathProject.ObjectPathProject(o4)
>>> o4.Group = [o3]
>>> o4.Tooltable
Tooltable containing 0 tools
```

Il modulo Path dispone anche di un editor GUI per la tooltable che può essere chiamato in python, dandogli un oggetto che ha una proprietà ToolTable   *


```python
>>> from PathScripts import TooltableEditor
>>> TooltableEditor.edit(o4)
```


<div class="mw-translate-fuzzy">

### La funzione Path Shape 


</div>


<div class="mw-translate-fuzzy">

Questa funzione è un normale oggetto Path con una proprietà Shape aggiuntiva. Dando alla proprietà una forma Wire, il percorso verrà calcolato automaticamente dalla forma. Si noti che in questo caso il posizionamento viene impostato automaticamente al primo punto del wire, e quindi l\'oggetto non è più movibile modificando il suo posizionamento. Per spostarlo, si deve spostare la forma sottostante.


</div>


```python
>>> import Part
>>> import Path
>>> v1 = FreeCAD.Vector(0,0,0)
>>> v2 = FreeCAD.Vector(0,2,0)
>>> v3 = FreeCAD.Vector(2,2,0)
>>> v4 = FreeCAD.Vector(3,3,0)
>>> wire = Part.makePolygon([v1,v2,v3,v4])
>>> o = FreeCAD.ActiveDocument.addObject("Path   *   *Feature","myPath2")
>>> o.Path = Path.fromShape(wire)
>>> FreeCAD.ActiveDocument.recompute()
>>> p =  o.Path
>>> print(p.toGCode())
```

### Funzioni Python 

Le funzioni Path   *   *Feature e Path   *   *FeatureShape hanno una versione Python, chiamate rispettivamente, Path   *   *FeaturePython e Path   *   *FeatureShapePython, che possono essere utilizzate nel codice python per creare oggetti parametrici avanzati derivati da esse.

## Importare e esportare GCode 

### Formato nativo 

I file gcode possono essere importati ed esportati direttamente tramite l\'interfaccia grafica, utilizzandole voci \"Esporta\", \"Apri\" o \"Inserisci\" del menu. Quando il nome del file è acquisito, si apre una finestra che chiede quale script di elaborazione deve utilizzare. Può anche essere fatto in python   *

Le informazioni sul Percorso vengono memorizzate in oggetti Path utilizzando un sottoinsieme di gcode descritto nella sezione \"Formato del GCode all\'interno di FreeCAD\" di cui sopra. Questo sottoinsieme può essere importato o esportato \"come è\", o convertito in/da una particolare versione di GCode adatto alla vostra macchina.

Se si dispone di un programma di GCode molto semplice e standard, che compila le regole descritte nella sezione \"Formato del GCode all\'interno di FreeCAD\" di cui sopra, per esempio, il boomerang da <http   *//www.cnccookbook.com/GWESampleFiles.html> , esso può essere importato direttamente in un oggetto Path, senza traduzione (questo equivale a utilizzare l\'opzione \"None\" della finestra GUI)   *


```python
import Path
f = open("/path/to/boomerangv4.ncc")
s = f.read()
p = Path.Path(s)
o = App.ActiveDocument.addObject("Path   *   *Feature","boomerang")
o.Path = p
```

Allo stesso modo, è possibile ottenere le informazioni sul percorso come gcode \"agnostico\", e memorizzarle manualmente in un file   *


```python
text = o.Path.toGCode()
print text
myfile = open("/path/to/newfile.ngc")
myfile.write(text)
myfile.close()
```

Se serve un output diverso, però, è necessario convertire questo GCode agnostico in un formato adatto alla macchina. Questo è compito dello script di post-processing.

### Utilizzare gli script di pre e post-elaborazione 

Se si dispone di un file gcode scritto per una macchina particolare, che non è conforme alle regole interne utilizzate dai FreeCAD, descritte nella sezione \"Formato GCode interno a FreeCAD\" di cui sopra, si potrebbe non riuscire a importarlo e/o renderlo correttamente nella 3D vista. Per rimediare a questo, è necessario utilizzare uno script di pre-elaborazione, che converte dal formato di una specifica macchina al formato di FreeCAD.

Se si conosce il nome dello script di pre-elaborazione da utilizzare, è possibile importare il file usando, dalla console python questo   *


```python
import example_pre
example_pre.insert("/path/to/myfile.ncc","DocumentName")
```

Allo stesso modo, è possibile emettere un oggetto tracciato per GCode, utilizzando uno script post_processor in questo modo   *


```python
import example_post
example_post.export (myObjectName,"/path/to/outputFile.ncc")
```

### Scrivere script di elaborazione 

Gli script di pre e post-elaborazione si comportano come gli altri comuni importatori e esportatori di FreeCAD. Quando si sceglie uno script di /post elaborazione dalla finestra di dialogo, il processo di import/export viene reindirizzato allo script specificato. Gli script di pre-elaborazione devono contenere almeno i seguenti metodi open(nome del file) e insert(nome del file, nome del documento). Gli script di post-elaborazione devono implementare export(objectslist,filename).

Gli script vengono inseriti nella cartella Mod/Path/PathScripts o nella directory delle macro definita dell\'utente. Si può dare loro un nome a piacere, ma per convenzione, e per essere scelti dalla finestra di dialogo GUI, i nomi degli script di pre-elaborazione devono terminare con \"\_pre\", gli script di post-elaborazione con \"\_post\" (assicuratevi di usare il carattere sottolineato, non il trattino, altrimenti python non può importarli). Questo è un esempio molto, molto semplice di preprocessore. Esempi più complessi si trovano nella cartella Mod/Path/PathScripts   *


```python
def open(filename)   *
    gfile = __builtins__.open(filename)
    inputstring = gfile.read()
    # the whole gcode program will come in as one string,
    # for example   * "G0 X1 Y1\nG1 X2 Y2"
    output = ""
    # we add a comment
    output += "(This is my first parsed output!)\n"
    # we split the input string by lines
    lines = inputstring.split("\n")
    for line in lines   *
        output += line
        # we must insert the "end of line" character again
        # because the split removed it
        output += "\n"
    # another comment
    output += "(End of program)"
    import Path
    p = Path.Path(output)
    myPath = FreeCAD.ActiveDocument.addObject("Path   *   *Feature","Import")
    myPath.Path = p
    FreeCAD.ActiveDocument.recompute()
```

Pre e post-processori funzionano esattamente allo stesso modo. Fanno solo il contrario   * Gli script pre convertono da un GCode specifico al GCode \"agnostico\" di FreeCAD, mentre gli script post convertono dal GCode \"agnostico\" di FreeCAD al GCode specifico della macchina.

## Adding all faces of a ShapeString to the BaseFeature\'s list of a ProfileFromFaces operation 

This example is based on a [discussion in the german forum](https   *//forum.freecadweb.org/viewtopic.php?f=13&t=33310&p=279991#p279959).

### Prerequisites

-   Create a solid with ShapeString as Cutout
-   Create a Job using this solid as its BaseObject
-   Create a ProfileFromFaces operation named \"Profile_Faces\" with empty BaseGeometry.

### The code 

The following code will then add all faces from ShapeString and create the paths   *


```python
doc = App.ActiveDocument
list_of_all_element_faces = []
for i, face in enumerate(doc.ShapeString.Shape.Faces)   *
    list_of_all_element_faces.append('Face' + str(i + 1))


doc.Profile_Faces.Base = [(doc.ShapeString, tuple(list_of_all_element_faces))]
doc.recompute()
```





{{Path_Tools_navi

}} 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Path](Path_Workbench.md) > Path scripting/it
