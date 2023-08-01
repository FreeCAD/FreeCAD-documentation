# PartDesign Revolution/it
---
- GuiCommand:   Name:PartDesign Revolution   Name/it:Rivoluzione   MenuLocation:PartDesign → Rivoluzione   Workbenches:[PartDesign](PartDesign_Workbench/it.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Lo strumento **Rivoluzione** crea un solido ruotando uno schizzo selezionato o un oggetto 2D attorno ad un dato asse.


</div>

![](images/PartDesign_Revolution_example.svg )


<div class="mw-translate-fuzzy">

*Sopra: lo schizzo (A) è ruotato di 270 gradi in senso antiorario attorno all\'asse (B); a destra è mostrato il solido risultante (C).*


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Seleziona lo schizzo da rivoluzionare. v0.17 e superiore In alternativa, è possibile utilizzare una faccia di un solido esistente.
2.  Premere il pulsante **<img src="images/PartDesign_Revolution.svg" width=24px> '''Rivoluzione'''**.
3.  Impostare i parametri Rivoluzione (vedere la sezione successiva).
4.  Premere **OK**.


</div>

## Options


<div class="mw-translate-fuzzy">

## Opzioni in Parametri rivoluzione 

Durante la creazione di una rivoluzione, il dialogo **Parametri rivoluzione** permette di specificare diversi parametri per stabilire come deve essere ruotato il disegno.


</div>

+++
| ![](images/partdesign_revolution_parameters.png ) | ### Axis                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                  | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                  | +++ |
|                                                                                  | | ![](images/Partdesign_revolution_parameters_it.png ) | ### Assi                                                                                                                                                                                                                                                                                                                                                                                             | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               | |
|                                                                                  | |                                                                                        | Questa opzione specifica l\'asse attorno al quale deve essere ruotato lo schizzo.                                                                                                                                                                                                                                                                                                                             | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               | |
|                                                                                  | |                                                                                        | -   **Asse verticale dello schizzo**: seleziona l\'asse verticale dello schizzo.                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                        | -   **Asse orizzontale dello schizzo**: seleziona l\'asse orizzontale dello schizzo.                                                                                                                                                                                                                                                                                                                          | |
|                                                                                  | |                                                                                        | -   **Sketch axis**: v0.16 e precedenti seleziona una linea di costruzione contenuta nello schizzo utilizzato da Rivoluzione. La prima linea di costruzione creata nello schizzo viene etichettata *Schizzo asse 0*. L\'elenco a discesa contiene un asse dello schizzo personalizzato per ogni linea di costruzione.                    | |
|                                                                                  | |                                                                                        | -   **Linea di costruzione**: v0.17 e successive seleziona una linea di costruzione contenuta nello schizzo utilizzato da Rivoluzione. L\'elenco a discesa contiene una voce per ogni linea di costruzione. La prima linea di costruzione creata nello schizzo verrà etichettata *Linea di costruzione 1*.                              | |
|                                                                                  | |                                                                                        | -   **Asse (X/Y/Z) di base**: v0.17 e successive seleziona l\'asse X, Y o Z dell\'origine del corpo;                                                                                                                                                                                                                                    | |
|                                                                                  | |                                                                                        | -   **Seleziona riferimento\...**: v0.17 e successive consente di selezionre un bordo del corpo o una [linea di riferimento](PartDesign_Line/it.md) nella vista 3D.                                                                                                                                                             | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                     | |
|                                                                                  | |                                                                                        | </div>                                                                                                                                                                                                                                                                                                                                                                                                        | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                            | |
|                                                                                  | |                                                                                        | ### Angle                                                                                                                                                                                                                                                                                                                                                                                           | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                     | |
|                                                                                  | |                                                                                        | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                            | |
|                                                                                  | |                                                                                        | ### Angolo                                                                                                                                                                                                                                                                                                                                                                                         | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               | |
|                                                                                  | |                                                                                        | Questa opzione specifica l\'angolo di rivoluzione dello schizzo. Per ottenere una rivoluzione completa occorre impostare un angolo di 360°. Le immagini della sezione [esempi](#Examples/it.md) documentano alcune delle possibilità utilizzando diversi angoli di rotazione. Non è possibile specificare angoli negativi (se è necessario usare l\'opzione **Invertita**) o angoli maggiori di 360°. | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               | |
|                                                                                  | |                                                                                        | ### Simmetrica al piano                                                                                                                                                                                                                                                                                                                                                               | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               | |
|                                                                                  | |                                                                                        | Se selezionato, la rivoluzione si estende per metà dell\'angolo specificato in entrambe le direzioni rispetto al piano di schizzo.                                                                                                                                                                                                                                                                            | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               | |
|                                                                                  | |                                                                                        | ### Invertita                                                                                                                                                                                                                                                                                                                                                                                   | |
|                                                                                  | |                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               | |
|                                                                                  | |                                                                                        | Se selezionato, la direzione di rotazione viene invertita passando da quella predefinita in senso orario a quella antioraria.                                                                                                                                                                                                                                                                                 | |
|                                                                                  | +++ |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                  | </div>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                  | ### Symmetric to plane                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                  | If checked, the revolution will extend half of the specified angle in both directions from the sketch plane.                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                  | ### Reversed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                  | If checked, the direction of revolution is reversed from default clockwise to counterclockwise.                                                                                                                                                                                                                                                                                                                                                                                                            |
+++



## Proprietà

Sotto sono riportate le proprietà che possono essere definite dopo la creazione della funzione. Le proprietà *Base* e *Axis* non sono editabili.


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Angle}}: angolo di rotazione. vedere [Angolo](#Angolo.md).

-    {{PropertyData/it|Label}}: etichetta data all\'operazione, può essere cambiata a piacere.

-    {{PropertyData/it|Midplane}}: true o false. Vedere [Simmetrica al piano](#Simmetrica_al_piano.md).

-    {{PropertyData/it|Reversed}}: true o false. Vedere [Invertita](#Invertita.md).

-    {{PropertyData/it|Refine}}: v0.17 e successive true o false. Se impostato su true, pulisce il solido dai bordi residui lasciati dalle funzioni. Per maggiori dettagli vedere [Affina forma](Part_RefineShape/it.md).


</div>



## Esempi


<div class="mw-translate-fuzzy">

![Esempio di Rivoluzione creata utilizzando una linea di costruzione come asse di rivoluzione: In questa immagine l\'angolo è di 75° e la rivoluzione è attorno alla linea di costruzione (Sketch axis 0)](images/PartDesign_Revolution_axis_fromconstructionlines1.jpg ) 


</div>

## Useful links 


<div class="mw-translate-fuzzy">

## Link utili 

Un [esempio](http://forum.freecadweb.org/viewtopic.php?f=3&t=3674) dettagliato di utlizzo disponibile nel forum.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/it
