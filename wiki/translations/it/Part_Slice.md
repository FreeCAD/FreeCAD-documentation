---
 GuiCommand:
   Name: Part Slice
   Name/it: Part Affetta in composto
   MenuLocation: Parte , Dividi , Affetta in composto
   Workbenches: Part_Workbench/it
   Version: 0.17
   SeeAlso: Part_BooleanFragments/it, Part_XOR/it, Part_CompJoinFeatures/it, Part_Boolean/it
---

# Part Slice/it



## Descrizione

Lo strumento <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Affetta in composto](Part_Slice/it.md) serve per dividere le forme intersecandole con altre forme. Ad esempio, con un cubo e un piano, viene creato un composto di due solidi.

![600px](images/Part_Slice_Demo.png)



*Nella figura sopraː i pezzi sono stati separati manualmente dopo l'operazione, per rendere visibili le singole parti*

Ci sono due comandi per affettare una forma: <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Affetta in parti](Part_SliceApart/it.md) e <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Affetta in composto](Part_Slice/it.md). Entrambi creano una funzione parametrica Slice, che mette i pezzi tagliati in un composto, ma <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Affetta in parti](Part_SliceApart/it.md) esplode il composto risultante in oggetti separati. \"Affetta in composto\" è completamente parametrico e non crea problemi se il numero di pezzi cambia. \"Affetta in parti\" non aggiorna il numero di oggetti quando il numero di pezzi cambia.

La forma in uscita occupa lo stesso spazio dell\'originale, ma è divisa dove interseca le altre forme. I singoli pezzi sono raggruppati in un composto (o in un compsolid), quindi sembra che l\'oggetto sia ancora un unico pezzo. Per disporre dei singoli pezzi è necessario separare gli elementi del composto. Se si desidera accedere ai singoli pezzi in modo parametrico, è possibile utilizzare <img alt="" src=images/Part_CompoundFilter.svg  style="width:24px;"> [Part Filtra composto](Part_CompoundFilter/it.md). Per un utilizzo rapido e non parametrico usare <img alt="" src=images/Draft_Downgrade.svg  style="width:24px;"> [Draft Declassa](Draft_Downgrade/it.md).

Lo strumento dispone di tre modalità: \"Standard\", \"Split\", e \"CompSolid\". Non esiste un modulo di selezione, sono predefiniti ma è possibile accedervi dopo l\'operazione al livello delle fette risultanti.

Le modalità \"Standard\" e \"Split\" differiscono per l\'azione dello strumento su polilinee (wire), gusci (shell) e compsolid: se si usa \"Split\", essi sono separati; se si usa \"Standard\", essi sono mantenuti insieme (si ottengono dei segmenti in più).

La struttura del composto nelle modalità \"Split\" e \"Standard\" segue la struttura dei composti della forma da suddividere.

In modalità \"CompSolid\", il risultato è un compsolid (o un composto di compsolid, se i solidi risultanti formano più di un\'isola di connessione). Un compsolid è formato da un gruppo di solidi collegati dalle facce, esse si rapportano ai solidi come le polilinee (wire) si rapportano ai bordi (edge), e i gusci (shell) si rapportano alle facce, il nome è probabilmente l\'abbreviazione di \"solido composito\"

L\'azione complessiva dello strumento è molto simile a quella di <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Frammenti booleani](Part_BooleanFragments/it.md), tranne che il risultato contiene solo i pezzi dalla prima forma.



## Utilizzo

1.  Selezionare prima l\'oggetto da dividere, e poi alcuni oggetti con cui dividerlo.
    L\'ordine di selezione è importante. I composti con auto-intersezioni non sono ammessi (le auto-intersezioni a volte possono essere individuate facendo passare il composto attraverso lo strumento <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Frammenti booleani](Part_BooleanFragments/it.md))
2.  Richiamare il comando Part Affetta in diversi modi:
    -   Premere il pulsante <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Part Affetta](Part_Slice/it.md) nella barra degli strumenti Part
    -   Usare la voce **Parte → Dividi → Affetta in un composto** nel menu Parte




1.  Notaː Gli oggetti con cui si vuole tagliare (utensili) devono separare completamente l\'oggetto da tagliare. Quindi, per esempio, un cubo non può essere tagliato da una polilinea, ma da un piano derivato dall\'estrusione di una polilinea.

Viene creato un oggetto parametrico Slice. Vengono nascosti gli oggetti originali , e nella [Vista 3D](3D_view/it.md) viene mostrato il risultato dell\'intersezione.

### Struttura ad albero di Slice 

Il comando Affetta in composto crea un oggetto affettato. Nell\'esempio seguente un cubo viene affettato da una faccia.

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

1.  Passare nell\'ambiente [Sketcher](Sketcher_Workbench/it.md)
    -   Creare un nuovo schizzo. Disegnare un rettangolo che delimita la forma complessiva del puzzle.
    -   Chiudere lo schizzo.
        ![320px](images/slice_example_step1.png)
2.  Passare nell\'ambiente [Part](Part_Workbench/it.md).
    -   Selezionare lo schizzo, e scegliere **Part → <img src="images/Part_MakeFace.svg" width=24px> [Crea faccia da polilinea](Part_MakeFace/it.md)**.
        ![320px](images/slice_example_step2.png)
3.  Ritornare all\'ambiente <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/it.md)
    -   Creare un altro schizzo sullo stesso piano.
    -   Utilizzare lo strumento polilinea per disegnare le linee che divideranno il puzzle in pezzi.
        ![320px](images/slice_example_step3.png)
4.  Passare all\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md).
    -   Selezionare lo schizzo divisore, e applicare [Frammenti Booleani](Part_BooleanFragments/it.md). Questo inserisce i vertici nel punto in cui le linee dello schizzo divisore si intersecano. Per poter fare il passo successivo del lavoro è indispensabile avere questi vertici.
        ![320px](images/slice_example_step4.png)
5.  Selezionare la faccia rettangolare, ed i Frammenti booleani dello schizzo divisore, e applicare Affetta in composto.
    ![320px](images/slice_example_step5.png)
6.  Utilizzare [Esplodi composto](Part_ExplodeCompound/it.md) sulla faccia affettata, per dividere in singoli pezzi il composto creato da Affetta in composto.

**Nota:** I passaggi 5 e 6 possono essere eseguiti con un solo clic usando [Affetta in parti](Part_SliceApart/it.md)



## Note

-   Lo strumento è stato introdotto in FreeCAD v0.17.8053. FreeCAD deve essere compilato con OCC 6.9.0 o successivo; in caso contrario, lo strumento non sarà disponibile.
-   ̈Le proprietà sono accessibili sulle parti interne dell\'oggetto affettato, non a livello del risultato.
-   Gli oggetti che servono per affettare (utensili) devono separare completamente l\'oggetto da affettare. Quindi un cubo non può essere tagliato da una polilinea, ma, ad esempio, da un piano derivato dall\'estrusione della polilinea.
-   L\'oggetto affettato deve superare il controllo BOP. Vedere <img alt="" src=images/Part_CheckGeometry.svg  style="width:24px;"> [Part controlla geometria](Part_CheckGeometry/it.md).



## Script

Lo strumento può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione: 
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



## Tutorial

-   [FreeCad 0.18 Part WB using Slice and Slice Apart](https://www.youtube.com/watch?v=tzHkQaHgrfQ) (English language), author: Ha Gei

-   [FreeCAD Slice und Slice Apart und andere Tricks](https://www.youtube.com/watch?v=JJAL5JmqqKQ) (German language), author: Ha Gei



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Slice/it
