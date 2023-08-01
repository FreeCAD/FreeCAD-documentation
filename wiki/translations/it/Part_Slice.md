# Part Slice/it
---
- GuiCommand:   Name:Part Slice   Name/it:Affetta in composto   MenuLocation:Part → Dividi → Affetta in composto   Workbenches:[SeeAlso:[[Part_BooleanFragments/it|Frammenti Booleani](Part_Workbench/it___Part]].md), [Part XOR](Part_XOR/it.md), [Giunzione](Part_CompJoinFeatures/it.md), [Operazioni booleane](Part_Boolean/it.md)---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Strumento<img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Affetta in composto](Part_Slice/it.md) serve per dividere le forme intersecandole con altre forme. Ad esempio, con un cubo e un piano, viene creato un composto di due solidi.


</div>

![600px](images/Part_Slice_Demo.png)



*Nella figura sopra, i pezzi sono stati separati manualmente dopo l'operazione, per rendere visibili le singole parti*


<div class="mw-translate-fuzzy">

Ci sono due comandi per affettare una forma: <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Affetta in parti](Part_SliceApart/it.md) e <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Affetta in composto](Part_Slice/it.md). Entrambi creano una funzione parametrica Slice, che mette i pezzi tagliati in un composto, ma <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Affetta in parti](Part_SliceApart/it.md) esplode il composto risultante in oggetti separati. \"Affetta in composto\" è completamente parametrico e non crea problemi se il numero di pezzi cambia. \"Affetta in parti\" non aggiorna il numero di oggetti quando il numero di pezzi cambia.


</div>


<div class="mw-translate-fuzzy">

La forma in uscita occupa lo stesso spazio dell\'originale, ma è divisa dove interseca le altre forme. I singoli pezzi sono raggruppati in un composto (o in un compsolid), quindi sembra che l\'oggetto sia ancora un unico pezzo. Per disporre dei singoli pezzi è necessario separare gli elementi del composto. Se si desidera accedere ai singoli pezzi in modo parametrico, è possibile utilizzare <img alt="" src=images/Part_CompoundFilter.svg  style="width:24px;"> [Filtra composto di Part](Part_CompoundFilter/it.md). Per un utilizzo rapido e non parametrico usare <img alt="" src=images/Draft_Downgrade.svg  style="width:24px;"> [Degrada](Draft_Downgrade/it.md) di Draft.


</div>

Lo strumento dispone di tre modalità: \"Standard\", \"Split\", e \"CompSolid\". Non esiste un modulo di selezione, sono predefiniti ma è possibile accedervi dopo l\'operazione al livello delle fette risultanti.

Le modalità \"Standard\" e \"Split\" differiscono per l\'azione dello strumento su wire, shell e compsolid: se si usa \"Split\", essi sono separati; se si usa \"Standard\", essi sono mantenuti insieme (si ottengono dei segmenti in più).

La struttura del composto nelle modalità \"Split\" e \"Standard\" segue la struttura dei composti della forma da suddividere.

In modalità \"CompSolid\", il risultato è un compsolid (o un composto di compsolid, se i solidi risultanti formano più di un\'isola di connessione). Un compsolid è formato da un gruppo di solidi collegati dalle facce, esse si rapportano ai solidi come le polilinee (wire) si rapportano ai bordi (edge), e i gusci (shell) si rapportano alle facce, il nome è probabilmente l\'abbreviazione di \"solido composito\"


<div class="mw-translate-fuzzy">

L\'azione complessiva dello strumento è molto simile a quella di <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Frammenti booleani](Part_BooleanFragments/it.md), tranne che il risultato contiene solo i pezzi dalla prima forma.


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare prima l\'oggetto da dividere, e poi alcuni oggetti con cui dividerlo.
    L\'ordine di selezione è importante. I composti con auto-intersezioni non sono ammessi (le auto-intersezioni a volte possono essere individuate facendo passare il composto attraverso lo strumento <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Frammenti booleani](Part_BooleanFragments/it.md))
2.  Avviare il comando <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Affetta in composto](Part_Slice/it.md).


</div>


<div class="mw-translate-fuzzy">

1.  Notaː Gli oggetti con cui si vuole tagliare (utensili) devono separare completamente l\'oggetto da tagliare. Quindi, per esempio, un cubo non può essere tagliato da un filo, ma da un piano derivato da un filo estruso.


</div>


<div class="mw-translate-fuzzy">

Viene creato un oggetto parametrico Slice. Vengono nascosti gli oggetti originali , e nella vista 3D viene mostrato il risultato dell\'intersezione.


</div>


<div class="mw-translate-fuzzy">

### Struttura ad albero di Slice 

Il comando Affetta in composto crea un oggetto affettato. Nell\'esempio seguente un cubo viene affettato da una faccia.


</div>

Vengono create le fette e tutte le fette sono unite in un composto.

![](images/Part_SliceTree.png )



## Proprietà


{{TitleProperty|Slice}}

-    **Base**: L\'oggetto da dividere.

-    **Tools**: Elenco di oggetti con cui dividere. (da FreeCAD v0.17.8053, questa proprietà non viene visualizzata nell\'editor delle proprietà, e si può accedere solo tramite Python).

-    **Mode**: \"Standard\", \"Split\", o \"CompSolid\". \"Split\" è il default. Standard e Split differiscono per l\'azione dello strumento sull\'aggregazione delle forme; se \"Split\", essi sono separati; altrimenti essi sono mantenuti insieme (si ottengono dei segmenti in più).

-    **Tolerance**: Valore di \"confusione\". Questa è una tolleranza supplementare da applicare durante la ricerca delle intersezioni, oltre alle tolleranze memorizzate nelle forme in ingresso.

̈Notaː Le proprietà sono accessibili sull\'oggetto interno delle sezioni, non sul livello del risultato.



## Esempio



## Creare un puzzle 


<div class="mw-translate-fuzzy">

1.  Passare nell\'ambiente [Schizzo](Sketcher_Workbench/it.md)
    -   Creare un nuovo schizzo. Disegnare un rettangolo che delimita la forma complessiva del puzzle.
    -   Chiudere lo schizzo.
        ![320px](images/slice_example_step1.png)
2.  Passare nell\'ambiente [Part](Part_Workbench/it.md).
    -   Selezionare lo schizzo, e scegliere Part -\> Crea faccia da schizzo (nel menu).
        ![320px](images/slice_example_step2.png)
3.  Passare nell\'ambiente Schizzo
    -   Creare un altro schizzo sullo stesso piano.
    -   Utilizzare lo strumento polilinea per disegnare le linee che divideranno il puzzle in pezzi.
        ![320px](images/slice_example_step3.png)
4.  Passare nell\'ambiente Part.
    -   Selezionare lo schizzo divisore, e applicare [Frammenti Booleani](Part_BooleanFragments/it.md). Questo inserisce i vertici nel punto in cui le linee dello schizzo divisore si intersecano. Per poter fare il passo successivo del lavoro è indispensabile avere questi vertici.
        ![320px](images/slice_example_step4.png)
5.  Selezionare la faccia rettangolare, ed i Frammenti booleani dello schizzo divisore, e applicare Affetta in composto.
    ![320px](images/slice_example_step5.png)
6.  Utilizzare [Esplodi composto](Part_ExplodeCompound/it.md) sulla faccia affettata, per dividere in singoli pezzi il composto creato da Affetta in composto.


</div>


<div class="mw-translate-fuzzy">

**Nota:** I passaggi 5 e 6 possono essere eseguiti con un solo clic usando [Affetta in parti](Part_SliceApart/it.md)


</div>



## Note


<div class="mw-translate-fuzzy">

Lo strumento è stato introdotto in FreeCAD v0.17.8053. FreeCAD deve essere compilato con OCC 6.9.0 o superiore; altrimenti lo strumento non è disponibile.


</div>



## Script


<div class="mw-translate-fuzzy">

Lo strumento può essere utilizzato nelle [macro](macros/it.md) e dalla console python utilizzando la seguente funzione:


</div>


```pythonBOPTools.SplitFeatures.makeSlice(name)```

-   Crea una funzione Slice vuota. Le proprietà \'Objects\' devono essere assegnate in modo esplicito, in seguito.
-   Restituisce l\'oggetto appena creato.

Slice può essere applicato anche a forme piane, senza la necessità di avere un document object, attraverso: 
```pythonBOPTools.SplitAPI.slice(base_shape, tool_shapes, mode, tolerance = 0.0)``` Questo può essere utile per creare delle funzioni personalizzate con script Python.

Esempio: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeSlice(name= 'Slice')
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tools = FreeCADGui.Selection.getSelection()[1:]
}}

Lo strumento è implementato in Python, vedere see **/Mod/Part/BOPTools/SplitFeatures.py** ([GitHub link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/SplitFeatures.py)) nella directory di installazione di FreeCAD.

## Tutorials

-   [FreeCad 0.18 Part WB using Slice and Slice Apart](https://www.youtube.com/watch?v=tzHkQaHgrfQ) (English language), author: Ha Gei

-   [FreeCAD Slice und Slice Apart und andere Tricks](https://www.youtube.com/watch?v=JJAL5JmqqKQ) (German language), author: Ha Gei


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Slice/it
