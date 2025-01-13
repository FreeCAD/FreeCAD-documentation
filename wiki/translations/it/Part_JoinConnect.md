---
 GuiCommand:
   Name: Part JoinConnect
   Name/it: Part Congiungi
   MenuLocation: Part , Giunzione , Congiungi oggetti
   Workbenches: Part_Workbench/it
   SeeAlso: Part_JoinEmbed/it, Part_JoinCutout/it, Part_Boolean/it, Part_Thickness/it
---

# Part JoinConnect/it



## Descrizione

Lo strumento <img alt="" src=images/Part_JoinConnect.svg  style="width:24px;"> **Part Congiungi** unisce due oggetti vuoti internamente, ad esempio dei tubi. Si possono anche unire gusci (shell) e wire.

![600px](images/JoinFeatures_Connect.png)



## Utilizzo

1.  Selezionare due oggetti da unire. L\'ordine di selezione non è importante. È sufficiente selezionare una qualsiasi sotto-forma di ciascun oggetto (ad esempio, delle facce). È inoltre possibile selezionare un composto contenente tutte le forme da collegare, ad esempio una [Serie ortogonale](Draft_OrthoArray/it.md).
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Part_JoinConnect.svg" width=16px> [Congiungi oggetti](Part_JoinConnect/it.md)**.
    -   Selezionare l\'opzione **Part → Giunzione → <img src="images/Part_JoinConnect.svg" width=16px> Congiungi oggetti** dal menu.
3.  Viene creato un oggetto parametrico Connect. Gli oggetti originali vengono nascosti e il risultato della connessione viene mostrato nella [Vista 3D](3D_view/it.md).



## Proprietà


{{TitleProperty|Connect}}

-    **Objects**: Elenco degli oggetti da collegare. In generale, sono necessari almeno due oggetti, ma va bene anche un singolo composto contenente le forme da collegare. (Da FreeCAD v0.17.8053, questa proprietà non viene visualizzata nell\'[editor delle proprietà](Property_editor/it.md), e si può accedere solo tramite [Python](Part_JoinConnect/it#Script.md)).

-    **Refine**: Stabilisce se alla forma finale deve applicare l\'operazione [Affina](Part_RefineShape/it.md), oppure no. Il valore di default è stabilito dalla casella di controllo \'Affina automaticamente la forma dopo l\'operazione booleana\' nelle [preferenze di PartDesign](PartDesign_Preferences/it.md).

-    **Tolerance**: valore di \"confusione\". Questa è una tolleranza supplementare da applicare durante la ricerca di intersezioni, oltre alle tolleranze memorizzate nelle forme di ingresso.



## Esempio

1.  Creare un tubo applicando uno [Spessore](Part_Thickness/it.md) a un [cilindro](Part_Cylinder/it.md):
    ![320px](images/JoinFeatures_Example_step1.png)
2.  Creare un nuovo tubo di diametro inferiore e [posizionarlo](Placement/it.md) in modo da perforare la parete del primo tubo:
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Selezionare il primo tubo, poi il secondo tubo (l\'ordine di selezione non è importante), infine selezionare l\'opzione \'Congiungi oggetti\' dalla barra degli strumenti a discesa degli strumenti di Giunzione.
    ![320px](images/JoinFeatures_Example_step3_Connect.png)
4.  Per visualizzare gli interni, utilizzare uno degli strumenti di sezione: [Piano di taglio](Std_ToggleClipPlane/it.md) del menu Visualizza, [Piano di sezione](Arch_SectionPlane/it.md) di Arch, o [Piano di taglio](Arch_CutPlane/it.md) di Arch. Nell\'immagine seguente, è stato utilizzato il Piano si sezione di Arch.
    ![320px](images/JoinFeatures_Example_step4_Connect.png)



## Algoritmo

Gli algoritmi sottostanti agli strumenti di Giunzione sono abbastanza semplici, ed è importante comprenderli per utilizzarli correttamente. L\'algoritmo di Connect, in particolare, è un po\' più complesso di altri, ma generalmente è sufficiente pensarlo come una variante simmetrica dell\'algoritmo di [Incorpora](Part_JoinEmbed/it#Algoritmo.md)

1\. Ogni oggetto è diviso in pezzi dagli incroci con altri oggetti. (vedere [Part Frammenti booleani](Part_BooleanFragments/it.md))

2\. Di tutte le parti di un oggetto, viene conservata solo la più grande; tutto il resto viene scartato.

3\. I pezzi delle intersezione che toccano almeno due oggetti vengono aggiunti ai risultati. Quindi, i pezzi sono uniti insieme per formare il risultato di Connect.



### Note

-   Se al passo 1 ogni oggetto rimane in un unico pezzo, il risultato di Congiungi è equivalente a una [unione](Part_Fuse.md) di oggetti.
-   Ora, tutti i composti sono esplosi prima della congiunzione. Ciò significa che i composti che si intersecano, che non sono validi per tutte le altre operazioni booleane, sono validi per Congiungi. (Questo può essere modificato in futuro.)
-   Il pezzo \"più grande\" è quello che ha la massa maggiore. Cioè, per i solidi sono confrontati i volumi, per i gusci e le facce sono confrontate le zone, e così via.
-   Da FreeCAD v0.17.8053, e con la versione 6.9.0 di OCC, Congiungi è quasi veloce come tutte le altre operazioni booleane. Per le versioni precedenti, Congiungi è circa 5 volte più lento di una normale operazione booleana, e funziona solo su solidi.



## Script

Gli strumenti di Giunzione possono essere utilizzati in [macro](Macros/it.md) e dalla [Console Python](Python_console.md) utilizzando la seguente funzione:

**BOPTools.JoinFeatures.makeConnect(name)**

-   Crea una funzione Connect vuota (o altra funzione Join, secondo la modalità passata). La proprietà \'Objects\' deve essere assegnata in modo esplicito, in seguito.
-   Restituisce l\'oggetto appena creato.

Connect può essere applicato anche a forme piane, senza la necessità di avere un oggetto documento, tramite:

**Part.BOPTools.JoinAPI.connect(list_of_shapes, tolerance = 0.0)**

Questo può essere utile per creare funzioni personalizzate con script Python.

Esempio:


{{code|code=
import Part
j = Part.BOPTools.JoinFeatures.makeConnect(name= 'Connect')
j.Objects = FreeCADGui.Selection.getSelection()
}}

Lo strumento è implementato in Python, vedere **/Mod/Part/BOPTools/JoinFeatures.py** ([Github link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/JoinFeatures.py)) in cui è installato FreeCAD.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinConnect/it
