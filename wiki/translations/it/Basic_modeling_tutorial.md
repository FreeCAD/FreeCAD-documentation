# Basic modeling tutorial/it
{{TutorialInfo/it
|Topic= Introduzione alla modellazione
|Level= Base
|Time= 15 minuti
|Author=_
|FCVersion=qualsiasi
|Files=nessuno
}}

## Introduzione

In questa guida introduttiva alla modellazione si mostra come modellare un profilo angolare. Si deve sapere che FreeCAD è composto da diversi moduli di disegno, e come in molti altri software CAD, sovente ci sono più modi di fare le cose. Qui, esploreremo due metodi.

## Prima di iniziare 

Ricordare che FreeCAD è ancora in fase di sviluppo, quindi potrebbe risultare meno efficace di altre applicazioni CAD, inoltre può capitare di scoprirne dei difetti o di subire dei blocchi dell\'applicazione. FreeCAD permette comunque di salvare file di backup. Il numero dei file di backup può essere stabilito nella finestra di dialogo delle preferenze accessibile con *Modifica -\> Preferenze -\> Documento*. Si consiglia di creare almeno 2 o 3 file di backup finché non si conosce bene FreeCAD.

Salvare sovente il proprio lavoro, e di tanto in tanto salvarlo con un nome diverso, in modo da poter sempre recuperare una copia di \"sicurezza\"; inoltre, essere preparati alla possibilità che alcuni comandi possano dare risultati diversi da quelli attesi.

## Introduzione alle tecniche di modellazione 

La prima tecnica di modellazione solida (quella di base) è la _. Si lavora con le forme primitive, quali cubi, cilindri, sfere e coni, combinandole tra di loro per costruire la propria geometria, sottraendo una forma dall\'altra, o intersecandole. Questi strumenti sono disponibili nel [Modulo Parte](Part_Workbench/it.md). Inoltre è possibile applicare delle trasformazioni alle forme, come per esempio, dei raccordi o degli smussi sui bordi. Anche questi strumenti si trovano nel [Modulo Parte](Part_Workbench/it.md).

La seconda tecnica usa strumenti più avanzati. Si inizia disegnando un profilo 2D che successivamente viene estruso o rivoluzionato.

Qui iniziamo cercando di fare una barra di profilato angolare, adatto ad esempio per un tavolo, con questi 2 metodi.


<div class="mw-translate-fuzzy">

## Primo Metodo - Geometria costruttiva dei solidi 

1.  Cominciare con il [Modulo Parte](Part_Workbench/it.md) ![](images/Switch_PartWorkbench.JPG ) (Menu **Visualizza -\> Ambiente -\> Parte**)
2.  Se non c\'è un nuovo documento di FreeCAD aperto (la maggior parte della finestra di FreeCAD è grigia), dal menu a discesa fare clic su **File → Nuovo** o fare clic sull\'icona <img alt="" src=images/Document-new.png  style="width:32px;"> **Crea un nuovo documento vuoto**.
3.  Cliccare sul pulsante <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cubo](Part_Box/it.md) per creare un Cubo (Parallelepipedo)
4.  Selezionarlo nello spazio 3D, o cliccare sull\'oggetto nella scheda *Progetto* a sinistra, poi, per modificare le sue dimensioni,
5.  Fare clic sulla scheda *Dati* nella parte inferiore, e fissare i valori di lunghezza, larghezza e altezza a 50 mm, 50 mm e 750 mm. *(vedere fig. 1.1)* **Notare**: *quando sono state scattate queste immagini, le proprietà erano ordinate in modo diverso, con l\'altezza al primo posto*.
6.  Ora il parallelepipedo riempie la maggior parte della vista 3D. Cliccare su <img alt="" src=images/Std_ViewFitAll.svg  style="width:32px;"> [Adatta la vista](Std_ViewFitAll/it.md) per adattare la vista al solido appena creata.
7.  Creare una seconda scatola allo stesso modo, ma con valori L=40, W=40 e H=750 mm. Per impostazione predefinita questa seconda scatola viene sovrapposta alla prima. *(vedere fig. 1.2)*
8.  Ora è possibile sottrarre il secondo solido dal primo. Selezionare per prima la prima forma (denominata Box), poi selezionare la seconda (denominata Box001), l\'ordine di selezione è importante! (Verificare nell\'albero del progetto che entrambe le forme siano selezionate. **Ricordare** che in modalità di navigazione Inventor, il comando **Ctrl** + click non esegue la selezione multipla, eventualmente [Passare](Mouse_Model/it.md) alla modalità CAD o Blender).
9.  Nella barra degli strumenti dell\'ambiente Parte, fare clic sul pulsante<img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Taglia](Part_Cut/it.md).


</div>

![Fig. 1.1 Il primo solido](images/Tutorial-normand01.jpg )

![Fig. 1.2 La seconda forma, sovrapposta e pronta per essere sottratta dalla prima](images/Tutorial-normand02.jpg )

![Fig. 1.3 Dopo l\'operazione di taglio](images/Tutorial-normand03.jpg )

Ora si dispone del primo angolare *(fig. 1.3)*.

Notare che, nella scheda *Progetto* a sinistra, entrambi i cubi sono stati sostituiti da un oggetto \"Cut\". In realtà, non sono scomparsi, ma piuttosto sono raggruppati nell\'oggetto Cut. Fare clic sul segno **+** di fronte ad esso, e osservare che entrambi i cubi sono presenti, ma in colore grigio (nascosti) *(Fig. 1.4)*. Se si fa clic su uno dei due elementi e poi si preme la barra spaziatrice, esso viene mostrato. La barra spaziatrice [commuta la visibilità](Std_ToggleVisibility/it.md) degli oggetti selezionati. *(Fig. 1.5)*

L\'angolare orientato in questo modo non piace? Basta solo modificare la posizione della forma **Box001**. Selezionarlo, visualizzarlo, e nella scheda Dati, fare clic sul **+** di fronte a *Placement*, quindi espandere la voce *Posizione*, e cambiare le coordinate X e Y. Premere **Invio**, nascondere nuovamente la forma Box001 e ora l\'orientamento dell\'angolare è diverso. *(Fig. 1.5)*. È anche possibile modificare qualsiasi dimensione della forma, e l\'oggetto **Cut** viene automaticamente aggiornato.

![Fig. 1.4 L\'operazione **Cut** salvaguarda le forme originali (i cubi)](images/Tutorial-normand04.jpg )

![Fig. 1.5 Si possono visualizzare le forme originali ](images/Tutorial-normand05.jpg )

Infine, possiamo arrotondare gli spigoli dell\'angolare per renderlo più realistico, utilizzando lo strumento <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Arrotonda](Part_Fillet/it.md). 
*(Fig. 1.6)*

![Fig. 1.6 Gli spigoli arrotondati](images/Tutorial-normand06.jpg )

## Secondo metodo - Estrusione di un profilo 

Con questo metodo si inizia disegnando un profilo 2D. È necessario attivare l\'ambiente di lavoro [Disegno 2D o Draft](Draft_Workbench/it.md) (menu **Visualizza -\> Ambiente -\> Draft**) ![](images/Switch_DraftWorkbench.JPG ).

-   Se non c\'è un nuovo documento di FreeCAD aperto (la maggior parte della finestra FreeCAD è grigia), dal menu a discesa fare clic su File → Nuovo o fare clic sull\'icona <img alt="" src=images/Document-new.png  style="width:32px;"> **Crea un nuovo documento vuoto**.

### Impostare il piano di lavoro 

Per prima cosa bisogna definire su quale [piano di lavoro](Draft_SelectPlane/it.md) si vuole disegnare il profilo.

1.  Individuare la barra degli strumenti visualizzata di seguito. A seconda delle preferenze di Draft, può essere sotto la barra principale degli strumenti, a sinistra o a destra.

    :   ![](images/DraftPlaneAuto.png )
2.  Premere il pulsante **Auto** (potrebbe essere etichettato \"None\").
3.  A seconda delle preferenze di Draft, questo espande una finestra di dialogo **Seleziona piano** nel pannello laterale delle Azioni o una barra orizzontale con l\'etichetta \"comando attivo: **Seleziona piano**\". Vedere le [Note sul pulsante di selezione del piano di Draft](#Note_sul_pulsante_di_selezione_del_piano_di_Draft.md) per vedere le schermate che mostrano le due modalità espanse.
4.  Lasciare il campo \'\' Offset \'\' al valore zero.
5.  Premere il pulsante **XY** per impostare il piano di lavoro su XY. Questo chiude il pannello Azioni o i pulsanti espansi. Ora il pulsante \"Auto\" è contrassegnato come \"Top\" per mostrare che questo è il piano attivo.

### Disegnare il profilo 

1.  Selezionare lo strumento <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [DWire (polilinea)](Draft_Wire/it.md).
2.  Attivare le caselle \"Relativo\" e \"Pieno\".
3.  Invece di disegnare la forma nella vista 3D, inserire le coordinate nei campi *X globale*, *Y globale* e *Z globale*. Il processo è il seguente:
    1.  Cliccare nel campo *X globale*;
    2.  Immettere il valore indicato nel sottostante elenco dei punti e premere **TAB** per passare nel campo *Y globale*;
    3.  Inserire il valore *Y globale* e premere **TAB** per passare nel campo *Z globale*;
    4.  Nel campo *Z globale* lasciare il valore zero e premere **ENTER** per convalidare le coordinate del punto;
    5.  Ripetere per i successivi 5 punti.
        -   **Coordinate** (X, Y, Z)
        -   1° punto: 0, 0, 0
        -   2° punto: 50, 0, 0
        -   3° punto: 0,10, 0
        -   4° punto: -40, 0, 0 **Nota:** *in FreeCAD 0.16, c\'è un bug che rimuove il punto precedente quando si inserisce il segno meno nel campo di inserimento. Una soluzione alternativa è inserire un valore positivo, quindi posizionare il cursore prima del numero e aggiungere il segno meno. (Questo bug è stato risolto in v0.17)*
        -   5° punto: 0, 40, 0
        -   6° punto: -10, 0, 0
4.  Premere il pulsante **Chiudi** per chiudere il profilo. Ora nella scheda del modello si deve avere questo profilo, intitolato **DWire**:

![Fig. 1.7 La Polilinea base](images/Tutorial-normand07.jpg )

Premere il tasto **0** (zero) sul tastierino numerico per impostare la vista assonometrica.

### Estrudere il profilo 

Attivare l\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Parte](Part_Workbench/it.md) dal [selettore dell\'ambiente](Std_Workbench/it.md), o dal menu **[Visualizza](Std_View_Menu.md) → Ambiente → Part**.

Cliccare sullo strumento **<img src="images/Part_Extrude.svg" width=32px> [Estrusione](Part_Extrude/it.md)**.

Nella scheda \"Azioni\" a sinistra, selezionare l\'oggetto **Wire**. Quindi immettere la lunghezza desiderata, ad esempio 750 mm. Lasciare come direzione Z=1. Fare clic su **OK**. Ora, nella scheda \"Modello\", si dovrebbe avere un oggetto **Estrusione** *(fig. 1.8)*.

![Fig. 1.8 L\'oggetto estruso](images/Tutorial-normand08.jpg )

Questo secondo metodo richiede meno operazioni, ma è anche meno flessibile del precedente: per modificare la forma, è necessario modificare il contorno (la polilinea), operazione più complicata che modificare le primitive usate nel metodo precedente.

Ci sono ancora altri modi per ottenere lo stesso risultato! Ma spero che questi due esempi servano per iniziare ad usare FreeCAD. Nel corso dei lavori incontrerete certamente delle difficoltà (come è successo all\'autore di questa guida quando ha iniziato a usare FreeCAD, nonostante la sua esperienza con i CAD 3D), ma non esitate a fare domande nel [forum di FreeCAD](https://forum.freecadweb.org)!

### Note sul pulsante di selezione del piano di Draft 

L\'etichetta sul pulsante potrebbe essere diversa, secondo la versione e secondo cosa si stava facendo prima. L\'etichetta del pulsante può essere: \"Top\", \"Front\", \"Side\", \"None\" o rappresentare un Vettore tipo (0.0,0.0,1.0). Può anche essere vuota. Per esempio:

![Select Plane None](images/DraftPlaneNone.png )

![Select Plane Top](images/DraftPlaneTop.png )

![Select Plane View](images/DraftPlaneView.png )  Dopo aver premuto il pulsante, le opzioni vengono espanse in una delle seguenti configurazioni.

![I parametri **Seleziona piano** come sono mostrati nella scheda Azioni.](images/DraftPlaneTasks.png )

![I parametri **Seleziona piano** come sono mostrati nella barra degli strumenti](images/DraftPlaneToolbarMode.png ) 

Le istruzioni di cui sopra funzionano comunque, non importa quale etichetta compaia sul pulsante.


{{Tutorials navi

}}

---
[documentation index](../README.md) > Basic modeling tutorial/it
