# Arch Window/it
---
- GuiCommand:/it   Name:Arch Window   Name/it:Finestra   Workbenches:[MenuLocation:Arch → Finestra   Shortcut:**W** **I**   SeeAlso:[[Arch Wall/it|Muro](Arch_Workbench/it___Architettura]].md), [Aggiungi componente](Arch_Add/it.md)---

## Descrizione

La [Finestra](Arch_Window/it.md) è l\'oggetto di base per tutti i tipi di oggetti \"incorporabili\", quali le finestre, le porte, ecc.. È progettato per essere un elemento indipendente, oppure \"ospitato\" all\'interno di un altro componente come ad esempio in un [Muro](Arch_Wall/it.md), in una [Struttura](Arch_Structure/it.md), o in un [Tetto](Arch_Roof/it.md). Esso ha una propria geometria, che può essere formata da diversi componenti solidi (ad es. il telaio o i pannelli interni), e definisce anche un volume da sottrarre all\'oggetto ospite, in modo da creare un\'apertura. Il volume da sottrarre viene calcolato automaticamente.

Le finestre sono basate su oggetti 2D chiusi, quali ad esempio, dei rettangoli di [Draft](Draft_Rectangle/it.md) o di [Schizzo](Sketcher_Workbench/it.md), ambienti che sono utilizzati anche per definire i componenti interni. L\'oggetto 2D di base deve contenere diversi contorni chiusi, che possono essere combinati per formare dei pannelli pieni (richiedono un contorno) o delle cornici (richiedono più contorni).

Lo strumento Finestra dispone anche di diversi **preset**, che permettono di realizzare porte o finestre da un elenco di parametri, senza la necessità di creare manualmente gli oggetti 2D di base e componenti. Le finestre possono anche essere creati da zero, disegnando prima un oggetto di base 2D.

Tutte le informazioni applicabili alle [finestre](Arch_Window/it.md) si applicano anche alle [porte](Arch_Door/it.md), poiché sono costruite sullo stesso oggetto sottostante. La principale differenza tra una finestra e una porta è che la porta ha un pannello interno che viene mostrato opaco (la porta stessa), mentre la finestra ha un pannello parzialmente trasparente (il vetro).

<img alt="" src=images/Arch_Window_example.jpg  style="width:600px;"> 
*Finestra costruita su un [Rettangolo Draft](Draft_Rectangle/it.md), quindi inserita in un  [Muro di Arch](Arch_Wall/it.md). Usando l'operazione [Aggiungi](Arch_Add/it.md) si ritaglia automaticamente un'apertura corretta nel muro ospitante.*

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;"> 
*Finestra complessa costruita sopra uno [Schizzo](Sketcher_Workbench/it.md). Quando si accede alla modalità di modifica della finestra, è possibile creare diversi componenti, impostare il loro spessore e selezionare e assegnare ad essa i contorni di uno schizzo.*

## Utilizzo

### Utilizzare i modelli preimpostati 

1.  Premere il pulsante **<img src="images/Arch_Window.svg" width=16px> [Finestra](Arch_Window/it.md)** , oppure i tasti **W** e poi **I**.
2.  Selezionare uno dei preset nella lista.
3.  Compilare i parametri desiderati.
4.  Nella [vista 3D](3D_view/it.md), spostare la finestra nella posizione in cui si desidera posizionarla. Se si sposta il puntatore su un [muro](Arch_Wall/it.md), il contorno della finestra dovrebbe allinearsi con la faccia di quell\'oggetto.

#### Additional presets 


<div class="mw-translate-fuzzy">


**Note:**

se si installa la \"Parts Library\" da [AddonManager](Std_AddonMgr/it.md), lo strumento finestra cercherà in questa libreria ulteriori preimpostazioni. Questi preset sono dei file di FreeCAD contenenti una singola finestra basata su uno schizzo parametrico che ha i vincoli definiti. Si possono aggiungere ulteriori preset nella directory `parts_library` in modo che vengano trovati dallo strumento finestra.


</div>


{{FileName|$ROOT_DIR/Mod/parts_library/Architectural Parts/Doors/Custom/}}

{{FileName|$ROOT_DIR/Mod/parts_library/Architectural Parts/Windows/Custom/}}

It is also possible to place custom windows and doors in your user {{FileName|Arch}} directory. <small>(v0.20)</small> 


{{FileName|$ROOT_DIR/Mod/Arch/Doors/Custom/}}

{{FileName|$ROOT_DIR/Mod/Arch/Windows/Custom/}}


<div class="mw-translate-fuzzy">

La `$ROOT_DIR` è la directory dell\'utente in cui sono archiviati la configurazione, le macro e gli ambienti di lavoro esterni di FreeCAD.

-   Su Linux di solito è `/home/username/.FreeCAD/`
-   Su Windows di solito è `C:\Users\username\Application Data\FreeCAD\`
-   Su Mac OSX di solito è `/Users/username/Library/Preferences/FreeCAD/`


</div>

### Creare dall\'inizio 

1.  Opzionalmente, selezionare una faccia sull\'oggetto Arch in cui si desidera inserire la finestra.
2.  Passare nell\'ambiente [Sketcher](Sketcher_Workbench/it.md).
3.  Creare un nuovo schizzo.
4.  Disegnare uno o più contorni chiusi (loop).
5.  Chiudere lo schizzo.
6.  Tornare nell\'ambiente [Arch](Arch_Workbench/it.md).
7.  Premere il pulsante **<img src="images/Arch_Window.svg" width=16px> [Finestra](Arch_Window/it.md)** , o premere i tasti **W** e poi **I**.
8.  Per regolare i componenti della finestra e le varie proprietà, entrare nella finestra del [pannello Azioni](task_panel/it.md) facendo doppio clic sull\'oggetto creato nella [vista ad albero](tree_view/it.md).


<div class="mw-translate-fuzzy">


**Nota:**

quando si crea lo schizzo, prestare molta attenzione all\'ordine di creazione dei contorni; la numerazione dei \"segmenti\" nel [ pannello delle azioni](task_panel/it.md) (\"Elementi della finestra\") dipende da questo.


</div>

## Presets

Sono disponibili i seguenti modelli preimpostati:

Image:ParametersDoorGlass.svg\|Glass door Image:ParametersDoorSimple.svg\|Simple door Image:ParametersWindowDouble.svg\|Double-opening window Image:ParametersWindowFixed.svg\|Fixed window Image:ParametersWindowSimple.svg\|Single-opening window Image:ParametersWindowStash.svg\|Sash-opening window

## Creare i componenti 

La finestra può includere 3 tipi di componenti: i pannelli, le cornici e le persiane.

I pannelli e le persiane sono costituiti da un contorno chiuso che viene estruso. Le cornici sono formate da 2 o più contorni chiusi, entrambi estrusi, e quello più piccolo viene {{KEY/it|<img src="images/Arch_Remove.png" width=16px> [sottratto](_Arch_Remove/it.md)}} al più grande.

È possibile accedere, creare, modificare ed eliminare i componenti di una finestra in modalità di modifica (doppio clic sull\'oggetto finestra nella struttura ad albero).

I componenti hanno le seguenti proprietà:

-   **Name** : Un nome per il componente
-   **Type**: Il tipo di componente. Può essere \"Frame\", \"Glass panel\" \"Solid panel\", o \"Louvres\"
-   **Wires** : Un elenco, separato da virgole, dei contorni su cui si basa il componente
-   **Thickness** : Lo spessore di estrusione del componente
-   **Z Offset** : La distanza tra il componente e la sua linea di base 2D
-   **Hinge**: Ciò consente di selezionare un bordo nell\'oggetto 2D di base, quindi impostare tale bordo come cerniera per questo componente e quelli successivi nell\'elenco
-   **Opening mode**: Se in questo componente o in qualsiasi altro precedente nell\'elenco è stata definita una cerniera, l\'impostazione della modalità di apertura consente alla finestra di apparire aperta o di visualizzare i simboli di apertura 2D in pianta o in elevazione.

<img alt="" src=images/Arch_Window_options.jpg  style="width:600px;">

## Opzioni


<div class="mw-translate-fuzzy">

-   Gli elementi Finestra condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md)
-   Se la casella **Auto-include** nel riquadro delle azioni di creazione della finestra non è selezionata, la finestra non verrà inserita in nessun oggetto ospite durante la creazione.
-   Per inserire la finestra selezionata in un [muro](Arch_Wall/it.md), selezionare entrambi, poi premere il pulsante **<img src="images/Arch_Add.svg" width=16px> [Aggiungi](Arch_Add/it.md)**.
-   Per rimuovere la finestra selezionata da un muro selezionare la finestra, poi premere il pulsante **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi](Arch_Remove/it.md)**.
-   Quando si utilizzano i preset, di solito conviene attivare lo [Snap](Draft_Snap/it.md) \"Vicino\", in questo modo è possibile agganciare la finestra a una faccia esistente.
-   L\'apertura creata da una finestra nel suo oggetto ospite è determinata da due proprietà: **Hole Depth** e **Hole Wire** ({{Version/it|0.17}}). Il numero del Hole Wire può essere selezionato nella vista 3D dal pannello delle finestre disponibili quando si fa doppio clic sulla finestra nella vista ad albero
-   La Finestra può utilizzare i [ Multi-Materiali](Arch_MultiMaterial/it.md). La finestra cerca nei multi-materiali allegati gli strati di materiale con lo stesso nome per ciascuna delle sue componenti e se è presente lo utilizza. Ad esempio, un componente denominato \"OuterFrame\" cerca nel Multi-Materiale collegato

uno strato di materiale denominato \"OuterFrame\". Se trova questo materiale lo attribuisce al componente OuterFrame. Il valore dello spessore dello strato di materiale viene ignorato.


</div>

## Aperture


**Vedere anche:**

il [Tutorial per finestre aperte](Tutorial_for_open_windows/it.md).

Le porte e le finestre possono apparire parzialmente o completamente aperte nel modello 3D oppure si possono visualizzare i simboli di apertura sia in pianta che in altezza. Di conseguenza, queste appariranno anche nelle viste in 2D estratte e generate da [Draft Viste 2D](Draft_Shape2DView/it.md) o [TechDraw](TechDraw_Workbench/it.md) o [Drawing](Drawing_Workbench/it.md). Per ottenere ciò, almeno uno dei componenti della finestra deve avere una cerniera e una modalità di apertura definita (vedere la sezione precedente \"Componenti dell\'edificio\"). Quindi, usando le proprietà **Opening**, **Symbol Plan** o **Symbol Elevation**, si può configurare l\'aspetto della finestra:

<img alt="" src=images/Arch_window_openings.png  style="width:600px;"> 
*Una porta che mostra da sinistra a destra  come lavorano le proprietà Symbol Plan, Symbol Elevation e Opening*

## Defining window types 

Windows can also take advantage of other tools, specifically [PartDesign](PartDesign_Workbench.md) workflows, to define a type. A type is an object that defines the shape of the window. This is specially well suited to work with [App Parts](App_Part.md):

<img alt="" src=images/Arch_window_type_example.png  style="width:800px;">

[Download the example file shown above](https://github.com/FreeCAD/Examples/blob/master/Arch_Example_Files/Window_Type.FCStd)

### Example workflow 

-   Create a window frame object, a glass panel, and any other window component you need, using [Part Workbench](Part.md) or [PartDesign](PartDesign_Workbench.md) tools.
-   For example, create a base rectangular sketch for your window, then a profile sketch for the frame, and create a [Part Sweep](Part_Sweep.md) to sweep the profile around the base sketch. Create a [Part Offset2D](Part_Offset2D.md) from the base sketch, then a [Part Extrude](Part_Extrude.md) to create the glass panel
-   Make sure all these pieces have a unique, meaningful name (for example, \"Frame\" or \"Glass Panel\")
-   Create an [App Part](App_Part.md), and place all your subcomponents in it
-   Create a volume to be subtracted from the wall, for example by extruding the base sketch. Add this volume to the App Part. Make sure the volume is turned off
-   If using FreeCAD version 0.19 or later, you can add 3 properties to your App Part, by right-clicking its properties view, and check \"Show All\". Add the following properties (all of them are optional, the group doesn\'t matter):
    -   **Height** as a PropertyLength and link it, for example, to a vertical constraint of your base sketch
    -   **Width** as a PropertyLength and link it, for example, to a horizontal constraint of your base sketch
    -   **Subvolume** as a PropertyLink and link it to the volume to be subtracted that we created above
    -   **Tag** as a PropertyString

### Materials

Our window type is now ready. We can create window objects from it, simply by selecting the App Part and pressing the window button. The \"Height\", \"Width\", \"Subvolume\" and \"Tag\" properties of the window will be linked to the corresponding property of the App Part, if existing.

To build a material for type-based windows:

-   Create a [multi-material](Arch_MultiMaterial.md)
-   Create one entry in the multi-material for each component of your App Part. For example, one \"Frame\", one \"Glass panel\" as we used above. Make sure to use the exact same name.
-   Attribute that multi-material to each of the windows derived from the same type

You can use any other kind of workflow than the one described above, the important points to remember are:

-   The type object must be one object, no matter the type (App Part, PartDesign Body, Part Compound, or even another Arch Window)
-   The type object must have a \"Subvolume\" property (linked to the window\'s Subvolume property) for openings in host objects to work
-   The type object must have a \"Group\" property with different children with same names as multi-material items for multi-materials to work

## Proprietà

-    {{PropertyData/it|Height}}: L\'altezza di questa finestra

-    {{PropertyData/it|Width}}: La larghezza di questa finestra

-    {{PropertyData/it|Hole Depth}}: La profondità dell\'apertura creata dalla finestra nel suo oggetto ospite

-    {{PropertyData/it|Hole Wire}}: Il numero del contorno (wire) dell\'oggetto base utilizzato per creare un\'apertura nell\'oggetto che ospita questa finestra. Questo valore può essere impostato graficamente facendo doppio clic sulla finestra nella vista ad albero. Impostando il valore 0, la finestra per creare il foro seleziona automaticamente il suo contorno più grande.

-    {{PropertyData/it|Window Parts}}: Una lista di stringhe (5 stringhe per ogni componente, che stabiliscono le opzioni dei componenti di cui sopra).

-    {{PropertyData/it|Louvre Width}}: Se uno dei componenti è impostato su \"Louvres\", questa proprietà definisce la dimensione delle lamelle della persiana

-    {{PropertyData/it|Louvre Spacing}}: Se uno dei componenti è impostato su \"Louvres\", questa proprietà definisce la spaziatura tra le lamelle

-    {{PropertyData/it|Opening}}: Tutti i componenti che hanno la loro modalità di apertura impostata e che hanno una cerniera definita in essi o in un componente precedente nell\'elenco, appaiono aperti di una percentuale definita da questo valore

-    {{PropertyData/it|Symbol Plan}}: Mostra il simbolo 2D di apertura nel piano

-    {{PropertyData/it|Symbol Elevation}}: Mostra il simbolo 2D di apertura nell\'elevazione

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[API Arch](Arch_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>

Lo strumento Finestra può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


```python
Window = makeWindow(baseobj=None, width=None, height=None, parts=None, name="Window")
```

-   Crea un oggetto `Window` basato su un `baseobj`, che deve essere un [Wire](Draft_Wire/it.md) o uno [Sketcher Schizzo](Sketcher_Sketch/it.md) chiuso.
-   Se disponibile, imposta `width`, `height`, e `name` (label) della finestra.
-   Se `baseobj` non è una forma chiusa, lo strumento non può creare un oggetto solido corretto.

Esempio: 
```python
import FreeCAD, Draft, Arch

Rect1 = Draft.makeRectangle(length=900, height=3000)
Window = Arch.makeWindow(Rect1)
FreeCAD.ActiveDocument.recompute()
```

Si può anche creare una finestra da un modello preimpostato. 
```python
Window = makeWindowPreset(windowtype, width, height, h1, h2, h3, w1, w2, o1, o2, placement=None)
```

-   Crea un oggetto `Window` basato su un `windowtype`, che deve essere uno dei nomi definiti in `Arch.WindowPresets`.
    -   Alcuni di questi preset sono: `"Fixed"`, `"Open 1-pane"`, `"Open 2-pane"`, `"Sash 2-pane"`, `"Sliding 2-pane"`, `"Simple door"`, `"Glass door"`, `"Sliding 4-pane"`.

-    `width`e `height` definiscono le dimensioni totali dell\'oggetto, con unità in millimetri.

-   I parametri `h1`, `h2`, `h3` (vertical offsets), `w1`, `w2` (widths), `o1`, e `o2` (horizontal offsets) specificano le diverse distanze in millimetri e dipendono dal tipo di preset che si sta creando.

-   Se `placement` è dato, è usato.

Esempio: 
```python
import FreeCAD, Arch

base = FreeCAD.Vector(2000, 0, 0)
Axis = FreeCAD.Vector(1, 0, 0)
place=FreeCAD.Placement(base, FreeCAD.Rotation(Axis, 90))

Door = Arch.makeWindowPreset("Simple door",
                             width=900, height=2000,
                             h1=100, h2=100, h3=100, w1=200, w2=100, o1=0, o2=100,
                             placement=place)
```


{{docnav/it|[Riferimento esterno](Arch_Reference/it.md)|[Piano di sezione](Arch_SectionPlane/it.md)|[Arch](Arch_Workbench/it.md)|IconL=Arch_Reference.svg |IconC=Workbench_Arch.svg |IconR=Arch_SectionPlane.svg}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Window/it
