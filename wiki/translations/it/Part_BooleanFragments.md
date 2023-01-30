# Part BooleanFragments/it
---
- GuiCommand:/it   Name:Part BooleanFragments   Name/it:Frammenti booleani   MenuLocation:Part → Dividi → Frammenti booleani   Workbenches:[SeeAlso:[[Part_Slice/it   Affetta in composto](Part_Workbench/it___Part]].md), [Part XOR](Part_XOR/it.md), [Congiungi](Part_CompJoinFeatures/it.md), [Operazione booleana](Part_Boolean/it.md)|Version:0.17.8053---


</div>



## Descrizione

Strumento per calcolare tutti i frammenti che possono derivare dall\'applicazione delle operazioni booleane tra le forme in ingresso. Ad esempio, per due sfere intersecanti, vengono generati tre solidi non sovrapposti, ma a contatto.

![600px](images/Part_BooleanFragments_Demo.png)


<div class="mw-translate-fuzzy">

(Nella figura sopra, i pezzi sono stati separati manualmente dopo l\'operazione, per rendere visibili le singole parti)


</div>


<div class="mw-translate-fuzzy">

La forma in uscita è sempre un composto. Il contenuto del composto dipende dai tipi di forme di ingresso e dalla modalità in cui l\'operazione viene eseguita. Ciò significa che non si ottiene immediatamente l\'accesso ai singoli pezzi del risultato, ma i pezzi rimangono raggruppati insieme. I singoli pezzi possono essere estratti dividendo il composto con [Scomponi](Draft_Downgrade/it.md).


</div>

Lo strumento dispone di tre modalità: \"Standard\", \"Split\", e \"CompSolid\".

Le modalità \"Standard\" e \"Split\" differiscono per l\'azione dello strumento su wire, shell e compsolid: se si usa \"Split\", essi sono separati; se si usa \"Standard\", essi sono mantenuti insieme (si ottengono dei segmenti in più).

La struttura del composto nelle modalità \"Split\" e \"Standard\" segue la struttura dei composti in ingresso. Cioè, se si forniscono due composti, ciascuno contenente una sfera come su nell\'esempio precedente, anche il risultato contiene due composti, ciascuno contenente i pezzi della sfera originariamente contenuta. Ciò significa che nel risultato il pezzo comune è ripetuto due volte. Solo se le sfere in ingresso sono entrambi dei non composti, il risultato contiene il pezzo comune una volta sola.

In modalità \"CompSolid\", i solidi vengono uniti in un compsolid (il compsolid è formato da un gruppo di solidi collegati dalle facce, esse si rapportano ai solidi come le polilinee (wire) si rapportano ai bordi (edge), e i gusci (shell) si rapportano alle facce, il nome è probabilmente l\'abbreviazione di \"solido composito\"). L\'output è un composto non-annidato di compsolidi



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare gli oggetti da intersecare.
    L\'ordine di selezione non è importante, poiché l\'azione dello strumento è simmetrica. È sufficiente selezionare un sotto-forma di ogni oggetto (ad esempio una faccia). Inoltre, è possibile selezionare un composto contenente diverse forme collegate, ad es. una [Schiera](Draft_Array/it.md).
2.  Avviare il comando Frammenti booleani di Part.


</div>


<div class="mw-translate-fuzzy">

Viene creato un oggetto parametrico Boolean Fragments. Vengono nascosti gli oggetti originali , e nella vista 3D viene mostrato il risultato dell\'intersezione.


</div>



## Proprietà


{{TitleProperty|Boolean Fragments}}

-    **Objects**: Elenco degli oggetti da intersecare. Generalmente, sono necessari almeno due oggetti, ma va anche bene un unico composto contenente le forme di intersecare. (da FreeCAD v0.17.8053, questa proprietà non viene visualizzata nell\'editor delle proprietà, e si può accedere solo tramite Python).

-    **Mode**: \"Standard\", \"Split\", o \"CompSolid\". \"Standard\" è il default. Standard e Split differiscono per l\'azione dello strumento sull\'aggregazione delle forme; se \"Split\", essi sono separati; se \"Standard\", essi sono mantenuti insieme (si ottengono dei segmenti in più).

-    **Tolerance**: valore di \"confusione\". Questa è una tolleranza supplementare da applicare durante la ricerca delle intersezioni, oltre alle tolleranze memorizzate nelle forme in ingresso.

## Implementation details 


<div class="mw-translate-fuzzy">

## Dettagli dell\'implementazione 

Lo strumento Boolean Fragments in \"Modalità Standard\" è un General Fuse Operator (GFA) di OpenCascade. Esso accetta una combinazione di tutti tipi di forme probabili, e la logica dell\'output è piuttosto complicata. Vedere [OpenCascade user guide: Boolean operations](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__boolean_operations.html).


</div>

Per le modalità \"Split\" e \"CompSolid\", la post-elaborazione in più è fatta da FreeCAD.



## Script


<div class="mw-translate-fuzzy">

Lo strumento può essere utilizzato nelle [macro](macros/it.md) e dalla console python utilizzando la seguente funzione:


</div>

**BOPTools.SplitFeatures.makeBooleanFragments(name)**

-   Crea una funzione BooleanFragments vuota. Le proprietà \'Objects\' devono essere assegnate in modo esplicito, in seguito.
-   Restituisce l\'oggetto appena creato.

BooleanFragments può essere applicato anche a forme piane, senza la necessità di avere un document object, attraverso:


{{code|code=
import BOPTools.SplitAPI
BOPTools.SplitAPI.booleanFragments(list_of_shapes, mode, tolerance = 0.0)

# OR, for Standard mode:

list_of_shapes = [App.ActiveDocument.Sphere.Shape, App.ActiveDocument.Sphere001.Shape]
pieces, map = list_of_shapes[0].generalFuse(list_of_shapes[1:], tolerance)
# pieces receives a compound of shapes; map receives a list of lists of shapes, defining list_of_shapes <--> pieces correspondence 
}}

Questo può essere utile per creare delle funzioni personalizzate con script Python.

Esempio: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeBooleanFragments(name= 'BooleanFragments')
j.Objects = FreeCADGui.Selection.getSelection() 
}}

Lo strumento stesso è implementato in Python, vedere /Mod/Part/BOPTools/SplitFeatures.py nell\'installazione di FreeCAD.



## Note

Lo strumento è stato introdotto in FreeCAD v0.17.8053. FreeCAD deve essere compilato con OCC 6.9.0 o superiore; altrimenti lo strumento non è disponibile.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part BooleanFragments/it
