# Manual:Parametric objects/it
{{Manual:TOC}}

FreeCAD utilizza un approccio di modellazione parametrica, in cui la geometria degli oggetti è governata da regole e parametri sottostanti anziché essere modellata liberamente. Ciò significa che le dimensioni e le caratteristiche di ciascun componente sono definite da parametri, che istruiscono il programma su come generare la geometria. Ad esempio, per creare un cilindro, vengono specificati parametri come raggio e altezza. Con questi valori, FreeCAD genera la forma geometrica precisa.

In FreeCAD, gli oggetti parametrici sono essenzialmente piccoli script programmabili che vengono eseguiti quando un parametro viene modificato. Questi parametri possono variare ampiamente, inclusi numeri interi e a virgola mobile, valori dimensionali del mondo reale come millimetri, metri o piedi, coordinate (espresse come x, y, z), stringhe di testo o persino riferimenti ad altri oggetti. Tale versatilità nei parametri consente la creazione di modelli complessi attraverso una serie di operazioni concatenate in cui ogni nuovo oggetto deriva le sue caratteristiche da quello precedente, introducendo anche attributi aggiuntivi.

Ad esempio, consideriamo la creazione di un oggetto cubico solido tramite la modellazione parametrica. Iniziamo con una forma rettangolare 2D di base etichettata come \"piastra\". di lunghezza l e larghezza w. Questo schizzo definisce la base del proprio oggetto cubico. Successivamente, definiamo un\'operazione di \"Estrusione\", o \"Pad\", specificando la distanza per spingere o tirare lo schizzo in un oggetto 3D. Il risultato è una forma cubica solida basata sulla forma dello schizzo e sulla distanza di estrusione specificata.

![](images/FreeCAD_022_PArametricDesignPlate.png )

Sulla faccia superiore dela piastra disegnamo un cerchio di un dato diametro d. Quindi utilizziamo questo cerchio per creare una tasca (rimuovere materiale) dalla piastra originale.

![](images/FreeCAD_022_ParametricDesignPocket.png )

Se si decidesse di modificare una delle dimensioni della piastra o del cerchio, anche l\'oggetto finale verrebbe modificato. Grazie all\'utilizzo di un approccio di progettazione parametrica, non è necessario rifare l\'oggetto dall\'inizio.

1.  Il ricalcolo non è sempre automatico. Le operazioni pesanti, che modificano una grande parte del documento, e quindi richiedono un po\' di tempo, non vengono eseguite automaticamente. Invece, l\'oggetto (e tutti gli oggetti che dipendono da esso) vengono contrassegnati per il ricalcolo (su di loro viene visualizzata una piccola icona blu nella vista ad albero). Quindi per ricalcolare tutti gli oggetti contrassegnati è necessario premere il pulsante Ricalcola (o **Modifica->Aggiorna**).
2.  L\'albero delle dipendenze deve sempre scorrere nella stessa direzione. I loop sono vietati. Vedere [DAG](Glossary#Directed_Acyclic_Graph.md), e [Vista DAG](DAG_view/it.md). Si può avere un oggetto A che dipende dall\'oggetto B che dipende dall\'oggetto C. Ma non si può avere l\'oggetto A che dipende dall\'oggetto B che a sua volta dipende dall\'oggetto A. Questa sarebbe una dipendenza circolare. Tuttavia, si possono avere molti oggetti che dipendono dallo stesso oggetto, ad esempio, gli oggetti B e C che dipendono entrambi da A. Il menu **Strumenti -> Grafico delle dipendenze** mostra un grafico delle dipendenza come nell\'immagine qui sopra. Può essere utile per individuare eventuali problemi.

Nel processo di modellazione parametrica di FreeCAD, l\'esame dell\'albero delle dipendenze di un oggetto fornisce una visione chiara della costruzione sequenziale e delle relazioni all\'interno di un modello. Alla base della struttura nell\'esempio sopra c\'è lo \"Schizzo della piastra\", che funge da base per la forma iniziale del modello. Viene quindi applicata un\'operazione di \'Pad\', che aggiunge materiale a questo schizzo fondamentale, creando di fatto una struttura tridimensionale dalla base bidimensionale.

Successivamente, sulla superficie appena formata viene disegnato uno \"schizzo circolare\". Questo cerchio costituisce la base per la successiva operazione \'Pocket\'. L\'operazione di tasca rimuove strategicamente il materiale dalla struttura, ritagliando essenzialmente una porzione in base allo schizzo del cerchio. Questo processo di aggiunta e quindi sottrazione di materiale consente di integrare perfettamente geometrie e caratteristiche complesse nel modello di base.

Attraverso questa sequenza di operazioni, partendo dallo schizzo di base, aggiungendo volume con una estrusione e creando caratteristiche dettagliate con schizzi e tasche aggiuntivi, l\'oggetto finale prende forma. Ogni passaggio di questa catena dipende dal suo predecessore, illustrando la natura interconnessa della progettazione parametrica in FreeCAD.

![](images/FreeCAD_022_ParametricDesignDependGraph.png )

In FreeCAD non tutti gli oggetti sono parametrici. Spesso, le geometrie che si importano da altri file non contengono parametri, e sono dei semplici oggetti non parametrici. Tuttavia, questi oggetti possono essere utilizzati come base o punto di partenza per creare dei nuovi oggetti parametrici, a seconda, ovviamente, di cosa richiede l\'oggetto parametrico e la qualità della geometria importata.

Tutti gli oggetti, parametrici o no, hanno comunque un paio di parametri di base, come ad esempio un Nome, che è unico nel documento e non può essere modificato, una Etichetta, che è invece un nome definito dall\'utente e che può essere modificato, e un [posizionamento](placement/it.md), che definisce la sua posizione nello spazio 3D.

Infine, vale la pena di notare che gli oggetti parametrici personalizzati sono [ facili da programmare in Python](Scripted_objects/it.md).

**Approfondimenti**

-   [L\'editor delle proprietà](Property_editor/it.md)
-   [Come programmare oggetti parametrici](Scripted_objects/it.md)
-   [Posizionare gli oggetti in FreeCAD](Placement/it.md)
-   [Abilitare il grafico delle dipendenze](Std_DependencyGraph/it.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/it
