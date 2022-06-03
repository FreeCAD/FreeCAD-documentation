# Manual:Parametric objects/it
<div class="mw-translate-fuzzy">





</div>


{{Manual   *TOC/it}}

FreeCAD è stato progettato per la modellazione parametrica. Ciò significa che la geometria che si crea, invece di essere liberamente modellabile, è prodotta da regole e parametri. Ad esempio, un cilindro può essere prodotto da raggio e altezza. Con questi due parametri, il programma ha informazioni sufficienti per realizzare il cilindro.

In FreeCAD gli oggetti parametrici sono in realtà delle piccole parti di un programma che viene eseguito ogni volta che uno dei parametri viene modificato. Gli oggetti possono avere un sacco di parametri di diversi tipi   * numeri (interi come 1, 2, 3 o valori in virgola mobile come 3,1416), dimensioni reali (1 mm, 2,4 m, 4.5 ft), coordinate (x, y, z), stringhe di testo (\"ciao!\") o anche un altro oggetto.

Questo ultimo tipo permette di costruire rapidamente complesse catene di operazioni, basando ogni nuovo oggetto su uno precedente, e aggiungendo ad esso delle nuove funzioni.

Nell\'esempio sottostante, un oggetto cubico solido (Pad) è basato su una forma 2D rettangolare (Schizzo) e ha una lunghezza di estrusione. Con queste due proprietà viene prodotta una forma solida estrudendo la forma di base alla distanza determinata. Dopo è possibile utilizzare questo oggetto come base per ulteriori operazioni, come, ad esempio, per disegnare una nuova forma 2D su una delle sue facce (Sketch001) e poi fare una sottrazione (tasca), fino ad arrivare all\'oggetto finale.

Tutte le operazioni intermedie (forme 2D, pad, tasche, ecc) sono ancora lì presenti, e si può ancora cambiare qualsiasi dei loro parametri in qualsiasi momento. Se è necessario, viene ricostruita l\'intera catena (ricalcolata) .

![](images/Parametric_objects.jpg )

Due cose importanti che è necessario sapere   *

1.  Il ricalcolo non è sempre automatico. Le operazioni pesanti, che modificano una grande parte del documento, e quindi richiedono un po\' di tempo, non vengono eseguite automaticamente. Invece, l\'oggetto (e tutti gli oggetti che dipendono da esso) vengono contrassegnati per il ricalcolo (su di loro viene visualizzata una piccola icona blu nella vista ad albero). Quindi per ricalcolare tutti gli oggetti contrassegnati è necessario premere il pulsante Ricalcola (o **Modifica->Aggiorna**).
2.  L\'albero delle dipendenze deve sempre scorrere nella stessa direzione. I loop sono vietati. Vedere [DAG](Glossary#Directed_Acyclic_Graph.md), e [Vista DAG](DAG_view/it.md). Si può avere un oggetto A che dipende dall\'oggetto B che dipende dall\'oggetto C. Ma non si può avere l\'oggetto A che dipende dall\'oggetto B che a sua volta dipende dall\'oggetto A. Questa sarebbe una dipendenza circolare. Tuttavia, si possono avere molti oggetti che dipendono dallo stesso oggetto, ad esempio gli oggetti B e C che dipendono entrambi da A. Il menu **Strumenti -> Grafico delle dipendenze** mostra un grafico delle dipendenza come nell\'immagine qui sopra. Può essere utile per individuare eventuali problemi.

In FreeCAD non tutti gli oggetti sono parametrici. Spesso, le geometrie che si importano da altri file non contengono alcun parametro, e sono dei semplici oggetti non parametrici. Tuttavia, questi oggetti possono essere utilizzati come base o punto di partenza per creare dei nuovi oggetti parametrici, a seconda, ovviamente, di cosa richiede l\'oggetto parametrico e la qualità della geometria importata.

Tutti gli oggetti, parametrici o no, hanno comunque un paio di parametri di base, come ad esempio un Nome, che è unico nel documento e non può essere modificato, una Etichetta, che è invece un nome definito dall\'utente e che può essere modificato, e un [posizionamento](placement/it.md), che definisce la sua posizione nello spazio 3D.

Infine, vale la pena di notare che gli oggetti parametrici personalizzati sono [ facili da programmare in Python](Scripted_objects/it.md).

**Approfondimenti**


<div class="mw-translate-fuzzy">

-   [L\'editor delle proprietà](Property_editor/it.md)
-   [Come programmare oggetti parametrici](Scripted_objects/it.md)
-   [Posizionare gli oggetti in FreeCAD](Placement/it.md)
-   [Abilitare il grafico delle dipendenze](Std_DependencyGraph/it.md)


</div>


<div class="mw-translate-fuzzy">





</div>

[Category   *Poweruser Documentation](Category_Poweruser_Documentation.md) [Category   *Tutorials](Category_Tutorials.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/it
