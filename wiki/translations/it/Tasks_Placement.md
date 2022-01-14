# Tasks Placement/it
## Descrizione


<div class="mw-translate-fuzzy">

Opzioni della scheda **Posizionamento**. Queste opzioni riguardano soltanto la posizione dell\'oggetto nello spazio, non riguardano altri attributi della forma. Internamente il posizionamento viene memorizzato come una posizione, e una rotazione (asse di rotazione e angolo trasformati in un quaternione [1](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)). Sebbene ci siano diversi modi di specificare una rotazione, per esempio con un centro di rotazione, questo è usato solo per influenzare il calcolo della rotazione e non viene memorizzato per le operazioni successive. Allo stesso modo, se viene specificato un asse di rotazione (1,1,1), esso può essere normalizzato se conservato nel quaternione e in seguito apparire nella forma (0.58, 0.58, 0.58) durante l\'esplorazione dell\'oggetto


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

La funzione **Posizionamento** può essere attivata in diversi modi:

-   [Con uno script](Python_scripting_tutorial#Vecteurs_et_Positions.md) Python nella console e la sua [API](Placement_API.md).

:   ![Scripting Placement as y/p/r and Matrix](images/PlacePyConv10.png )

-   oppure, dalla finestra **Vista combinata → Proprietà → Dati → Posizionamento → **...****,

:   ![Task\_Placement](images/_Tache_Placement_fr_01.png )

-   oppure dal menu **Modifica → Posizionamento\...**.


</div>

### Nella Vista combinata → Dati 


<div class="mw-translate-fuzzy">

-   Cliccare su una forma per selezionarla.
-   Fare clic su **Placement** per selezionare la voce, cliccare sul titolo, non sulla freccia <img alt="Tache\_Placement" src=images/Tache_Placement_01_fr_00.png  style="width:256px;">. Appare un pulsante con tre puntini **...**: ![ 256px \| Tache\_Placement](images/_Tache_Placement_01_fr_00.png ) .
-   Fare clic su questo pulsante per visualizzare la scheda **Azioni di Posizionamento**.


</div>


<div class="mw-translate-fuzzy">


:   ![](images/Tache_Placement_en_02.png )





</div>

### Options


{{TitleProperty|Translation}}


<div class="mw-translate-fuzzy">

### Opzioni


{{TitleProperty|Traslazione}}

-    {{TasksTag/it| X }}: <img alt="Traslazione in direzione X (Cliccare sull\'immagine per ingrandirla)" src=images/Tache_Placement_Translation_X_fr.gif  style="width:150px;"> Sposta il sistema di coordinate dell\'oggetto nella direzione **X** (in avanti o all\'indietro), rispetto alle coordinate degli assi di origine **0, 0, 0**.

-    {{TasksTag/it| Y }}: <img alt="Traslazione in direzione Y (Cliccare sull\'immagine per ingrandirla)" src=images/Tache_Placement_Translation_Y_fr.gif  style="width:150px;"> Sposta il sistema di coordinate dell\'oggetto nella direzione **Y** (a destra o a sinistra), rispetto alle coordinate degli assi di origine **0, 0, 0**.

-    {{TasksTag/it| Z }}: <img alt="Traslazione in direzione **Y** (Cliccare sull\'immagine per ingrandirla)" src=images/Tache_Placement_Translation_Z_fr.gif  style="width:150px;"> Sposta il sistema di coordinate dell\'oggetto nella direzione **Z** (in alto o in basso), rispetto alle coordinate degli assi di origine **0, 0, 0**.


</div>


{{TitleProperty|Center}}


<div class="mw-translate-fuzzy">


{{TitleProperty|Centro: }}

-    {{TasksTag/it| X }}: Sposta il centro di rotazione nella direzione **X**, rispetto alle coordinate dell\'oggetto selezionato. (default: 0,0,0).

-    {{TasksTag/it| Y }}: Sposta il centro di rotazione nella direzione **Y**, rispetto alle coordinate dell\'oggetto selezionato. (default: 0,0,0).

-    {{TasksTag/it| Z }}: Sposta il centro di rotazione nella direzione **Z**, rispetto alle coordinate dell\'oggetto selezionato. (default: 0,0,0).

-    {{TasksTag/it| Utente ... }}: Permette di modificare i tre assi (**X, Y, Z**) in una sola operazione <img alt="Definito dall\'utente" src=images/Part_Revolve_fr_06.png  style="width:96px;">.


</div>


{{TitleProperty|Rotation}}


<div class="mw-translate-fuzzy">


{{TitleProperty|Rotazione: }}

Per regolare i parametri di **rotazione** sono disponibili due metodi:


</div>


<div class="mw-translate-fuzzy">

-   Prima opzione. Selezionare **Asse di rotazione con angolo** <img alt="Tache\_Placement Opzioni asse di rotazione e angolo" src=images/Tache_Placement_fr_05.png  style="width:256px;"> (opzione di default).
    -   
        {{TasksTag/it| Asse : X }}
        
        : La rotazione viene eseguita sull\'asse **X**.

    -   
        {{TasksTag/it| Asse : Y }}
        
        : La rotazione viene eseguita sull\'asse **Y**.

    -   
        {{TasksTag/it| Asse : Z }}
        
        : La rotazione viene eseguita sull\'asse **Z**.

    -   
        {{TasksTag/it| Angolo }}
        
        : Angolo di rotazione in **gradi** da **-360,00°** a **360,00°**. (Di default: **0,00°**).


</div>


<div class="mw-translate-fuzzy">

-   Seconda opzione. Selezionare **Angoli di Eulero** <img alt="Tache\_Placement Opzione Angoli di Eulero" src=images/Tache_Placement_fr_04.png  style="width:256px;">.


</div>


<div class="mw-translate-fuzzy">

Questa opzione può essere più facile da usare, tuttavia, anche per questo modo, ci sono alcune cose importanti da ricordare:

Le rotazioni positive sono in senso **orario**, se viste dal punto di origine, verso l\'esterno, nel verso positivo di un asse. Ovvero, le rotazioni positive sono in senso **antiorario** se viste da un asse positivo verso il punto di origine.


</div>


<div class="mw-translate-fuzzy">

:\* [Imbardata](http://it.wikipedia.org/wiki/Lacet_(mouvement)) : Il movimento di imbardata è la rotazione orizzontale di un veicolo attorno ad un asse verticale. Convenzionalmente l\'asse di imbardata è l\'asse Z e l\'angolo di imbardata è indicato dall\'angolo **ψ**.

:\* [Beccheggio](http://it.wikipedia.org/wiki/Tangage) : Il beccheggio è il movimento di oscillazione muso-coda o prua-poppa attorno ad un asse orizzontale. Convenzionalmente l\'asse di beccheggio è l\'asse Y ed è indicato dall\'angolo **θ**.

:\* [Rollio](http://it.wikipedia.org/wiki/Roulis) : Il rollio è il movimento oscillatorio di un veicolo attorno al proprio asse longitudinale. Convenzionalmente l\'asse di rollio corrisponde all\'asse X ed è indicato dall\'angolo **φ**.


</div>


<div class="mw-translate-fuzzy">

Le rotazioni sono riferite alle **coordinate del corpo** di un oggetto nello spazio 3D.

Per essere riferite alle **coordinate dello spazio 3D**, le etichette dovrebbero essere **Posizione**, **Altitudine** e **Elevazione** oppure **Azimut**, **Inclinazione** e **Elevazione**.

Sono i **Tait-Bryan angles**. Per maggiori informazioni si può consultare [Angoli di Eulero](http://it.wikipedia.org/wiki/Angles_d'Euler).


</div>


<div class="mw-translate-fuzzy">

![ left \| Option Euler angles](images/_Tache_Placement_it_03.png ) 


</div>


<div class="mw-translate-fuzzy">

![Left\|Imbardata](images/Tache_Placement_Lacet_fr_Mini.gif )

-    {{TasksTag/it|Imbardata}}: Imbardata è la rotazione intorno all\'asse Z, da destra a sinistra e viceversa. (L\'imbardata è l\'angolo **Psi ψ**). Valore da **-360,00°** a **360,00°** (Di default: **0,00°**).


</div>


<div class="mw-translate-fuzzy">

![Left\|Beccheggio](images/Tache_Placement_Tangage_fr_Mini.gif )

-    {{TasksTag/it|Beccheggio}}: Beccheggio è la rotazione intorno all\'asse Y, alzare o abbassare il naso. Valore da **-360,00°** a **360,00°** (Di default: **0,00°**).


</div>


<div class="mw-translate-fuzzy">

![Left\|Rollio](images/Tache_Placement_Roulis_fr_Mini.gif )

-    {{TasksTag/it|Rollio}}: Rollio è la rotazione intorno all\'asse X, dondolare le ali. Valore da **-360,00°** a **360,00°** (Di default: **0,00°**).


</div>


<div class="mw-translate-fuzzy">

-    {{TasksTag/it| Applica le modifiche incrementali al posizionamento dell'oggetto }}: Quando viene selezionata, questa opzione azzera **virtualmente** i parametri, per consentire di inserire i valori senza dover fare dei calcoli con i parametri originali della forma.
    Dopo aver confermato con ** OK **, i valori inseriti si sommano ai valori della forma.


</div>


<div class="mw-translate-fuzzy">

-   Il pulsante ** Ripristina **, riporta tutti i valori a **0,0,0**.


</div>

## Link e Esempi 


<div class="mw-translate-fuzzy">

Nel tutorial [Aeroplane](Aeroplane/it.md) si trova un esempio pratico di utilizzo di questo comando.


</div>


<div class="mw-translate-fuzzy">

Ulteriori informazioni si trovano nella pagina [Posizionamento](Placement/it.md)


</div>




[<img src="images/Property.png" style="width:16px"> Command\_Reference](Category_Command_Reference.md)

---
[documentation index](../README.md) > [Command_Reference](Category_Command_Reference.md) > Tasks Placement/it
