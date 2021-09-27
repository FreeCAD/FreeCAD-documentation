# Manual:Creating renderings/it
{{Manual:TOC/it}}

Nell\'ambito della grafica computerizzata, la parola [rendering](https://en.wikipedia.org/wiki/Rendering_%28computer_graphics%29) è usata per descrivere una bella immagine prodotta da un modello 3D. Naturalmente, si potrebbe dire che quello che si vede nella vista FreeCAD 3D è già bello. Ma chi ha visto un recente film di Hollywood sa che con un computer è possibile produrre immagini che sono quasi indistinguibili da una fotografia.

Ovviamente, la produzione di immagini fotorealistiche richiede molto lavoro, oltre a un\'applicazione 3D che offra strumenti specifici a tale scopo, come controlli precisi per i materiali e l\'illuminazione. Poiché FreeCAD è un\'applicazione orientata più verso la modellazione tecnica, non dispone di strumenti di rendering avanzati.

Fortunatamente, il mondo open-source offre molte applicazioni per la produzione di immagini realistiche. Probabilmente il più famoso è [Blender](http://www.blender.org), che è molto popolare e ampiamente utilizzato nei film e nei giochi. I modelli 3D possono essere esportati da FreeCAD molto facilmente e fedelmente e poi importati in Blender, dove è possibile aggiungere materiali e illuminazione realistici, e produrre le immagini finali o anche le animazioni.


<div class="mw-translate-fuzzy">

Alcuni altri strumenti di rendering open-source sono fatti per essere utilizzati all\'interno di un\'altra applicazione, e si occupano di fare i complessi calcoli per produrre delle immagini realistiche. Tramite il suo ambiente [Raytracing](Raytracing_Workbench.md), FreeCAD può utilizzare due di questi strumenti di rendering: [POV-Ray](https://en.wikipedia.org/wiki/POV-Ray) e [Luxrender](https://en.wikipedia.org/wiki/LuxRender). POV-Ray è un progetto molto vecchio, ed è considerato un classico motore di [raytracing](https://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29), mentre LuxRender è molto più recente, ed è classificato come un [unbiased](https://en.wikipedia.org/wiki/Unbiased_rendering) renderer. Entrambi hanno i loro punti di forza e di debolezza, a seconda del tipo di immagine di cui si vuole ottenere il rendering. Il modo migliore per conoscerli è quello di guardare gli esempi sui siti web di entrambi i motori.


</div>

### Installazione

Prima di poter utilizzare l\'ambiente Raytracing in FreeCAD, si deve installare una di queste due applicazioni di rendering sul proprio sistema. Questo di solito è molto semplice, entrambi forniscono gli installatori per molte piattaforme e di solito sono inclusi nei repository software della maggior parte delle distribuzioni Linux.

Dopo che POV-Ray o Luxrender sono installati, è necessario impostare il percorso per il loro eseguibile principale nelle preferenze FreeCAD. Questo di solito è necessario solo su Windows e Mac. Su Linux, FreeCAD li cerca e individua nelle posizioni standard. Per trovare la posizione degli eseguibili POVRAY o LuxRender basta semplicemente cercare nel sistema i file denominati povray (o povray.exe in Windows) o luxrender (o luxrender.exe in Windows).

![](images/Exercise_raytracing_01.jpg )

In questa schermata Preferenze si può anche impostare la dimensione desiderata dell\'immagine che si vuole produrre.

### Rendering con PovRay 

Per la produrre il rendering con PovRay e LuxRender useremo il tavolo che abbiamo modellato nel capitolo _.

-   Iniziare caricando il file table.FCStd modellato in precedenza o dal link in fondo a questo capitolo.
-   Premere sulla freccia verso il basso piccolo accanto al pulsante <img alt="" src=images/Raytrace_New.svg  style="width:16px;"> [Nuovo progetto Povray](Raytracing_New/it.md), e scegliere il modello 
**RadiosityNormal**
-   Potrebbe apparire un messaggio di avviso che indica che l\'attuale vista 3D non è in modalità prospettiva e quindi il rendering sarà diverso. Correggere questo scegliendo **No**, scegliere il menu **Visualizza-\>Vista in prospettiva** e scegliere nuovamente il modello RadiosityNormal.
-   Dopo aver creato un nuovo progetto si può provare anche altri modelli, semplicemente modificando la sua proprietà **Template**.
-   È stato creato un nuovo progetto:

![](images/Exercise_raytracing_02.jpg )


<div class="mw-translate-fuzzy">

-   Il nuovo progetto ha adottato il punto di vista della vista 3D come era al momento in cui abbiamo premuto il pulsante. Possiamo cambiare la vista in qualsiasi momento, e aggiornare la posizione della vista memorizzata nel progetto Povray, premendo il pulsante <img alt="" src=images/Raytracing_ResetCamera.png  style="width:16px;"> [Reset camera](Raytracing_ResetCamera/it.md).
-   L\'ambiente Raytracing funziona nello stesso modo dell\'ambiente _:


</div>

![](images/Exercise_raytracing_03.jpg )


<div class="mw-translate-fuzzy">

-   Le viste hanno adottato i valori di colore e la trasparenza dei loro pezzi originali, ma, se lo si desidera, è possibile cambiare la situazione nelle proprietà di ogni singola vista.
-   Ora siamo pronti per produrre il primo render Povray. Premere il pulsante <img alt="" src=images/Raytracing_Render.png  style="width:16px;"> [Render](Raytracing_Render/it.md).
-   Nota per gli utenti windows: quando si riceve (in Povray) un avvertimento che dice \"Le restrizioni I/O proibiscono l\'accesso in scrittura \...\"
    -   aprire Povray
    -   scegliere \"Options \> Script I/O Restrictions\" e assicurarsi che sia impostato su \"No Restrictions\"
    -   riprovare il rendering
-   Viene chiesto di dare un nome al file e di indicare il percorso per l\'immagine .png che verrà salvata da Povray.
-   Povray si apre e calcola l\'immagine.
-   Quando questo è fatto, è sufficiente fare clic sull\'immagine per chiudere la finestra Povray. L\'immagine risultante viene caricata in FreeCAD:


</div>

![](images/Exercise_raytracing_04.jpg )

### Rendering con LuxRender 


<div class="mw-translate-fuzzy">

-   Il rendering con LuxRender funziona quasi allo stesso modo. Possiamo lasciare aperto il nostro file e creare il nuovo progetto con LuxRender nello stesso file, o ricaricarlo per ripartire da zero.
-   Premere sulla piccola freccia verso il basso accanto al pulsante <img alt="" src=images/Raytracing_Lux.png  style="width:16px;"> [Nuovo progetto Luxrender](Raytracing_Lux/it.md) e scegliere il modello **LuxOutdoor**.
-   Selezionare tutti i componenti del tavolo. Se il progetto Povray è ancora nel documento, accertarsi di selezionare anche il progetto lux stesso, in modo che le viste create nella fase successiva non vadano per errore nel progetto sbagliato.
-   Premere il pulsante <img alt="" src=images/Raytracing_InsertPart.png  style="width:16px;"> [Inserisci parte](Raytracing_InsertPart/it.md).
-   Selezionare il progetto LuxRender, e premere il pulsante <img alt="" src=images/Raytracing_Render.png  style="width:16px;"> [Render](Raytracing_Render/it.md).
-   LuxRender funziona in modo diverso rispetto a Povray. Quando si avvia il rendering, l\'applicazione LuxRender si apre e inizia subito il rendering:


</div>

![](images/Exercise_raytracing_05.jpg )

-   Se si lascia questa finestra aperta, LuxRender continua il calcolo e il rendering all\'infinito, affinando progressivamente l\'immagine. Spetta a voi decidere quando l\'immagine ha raggiunto una qualità sufficiente per le vostre esigenze, e fermare il rendering.
-   Sul pannello di sinistra ci sono anche molti controlli con cui interagire. Tutti questi controlli cambiano l\'aspetto dell\'immagine mentre viene eseguito il rendering, in tempo reale, senza fermare il rendering.
-   Quando si ritiene che la qualità è abbastanza buona, basta premere **Render-\>stop**, e poi **File-\>Export to image-\>Tonemapped low dynamic range** per salvare l\'immagine di rendering di un file PNG.


<div class="mw-translate-fuzzy">

È possibile estendere notevolmente le possibilità di rendering di FreeCAD con la creazione di nuovi modelli per Povray o LuxRender. Questo è spiegato nella [documentazione di Raytracing](Raytracing_Workbench/it.md).


</div>

**Download**

-   Il modello del tavolo: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>
-   Il file prodotto nel corso di questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/render.FCStd>

**Approfondimenti**


<div class="mw-translate-fuzzy">

-   [L\'ambiente Raytracing](Raytracing_Workbench/it.md)
-   [Blender](http://www.blender.org)
-   [POV-Ray](http://www.povray.org)
-   [Luxrender](http://www.luxrender.net)


</div>


<div class="mw-translate-fuzzy">





</div>

{{Raytracing Tools navi}} 

_

---
[documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Creating renderings/it
