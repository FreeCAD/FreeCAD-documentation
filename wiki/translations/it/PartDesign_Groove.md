# PartDesign Groove/it
---
 GuiCommand:   Name: PartDesign_Groove   Name/it: Scanalatura   Workbenches: PartDesign Workbench/it   PartDesign---


</div>

## Descrizione

Questo strumento rivoluziona uno schizzo selezionato o un oggetto 2D attorno ad un dato asse, asportando del materiale dall\'oggetto di supporto.

![](images/PartDesign_Groove_example.svg )



*A sinistra lo schizzo (A) è ruotato attorno all'asse (B); a destra la scanalatura risultante sul solido (C).*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare lo schizzo da ruotare.

    :   È possibile utilizzare una faccia di un solido esistente. {{VersionPlus/it|0.17}}
    :   Lo schizzo deve essere mappato sulla faccia planare di un solido esistente o di una funzione di Part Design, altrimenti viene visualizzato un messaggio di errore. {{VersionMinus/it|0.16}}
2.  Premere il pulsante **<img src="images/PartDesign_Groove.svg" width=24px> '''Scanalatura'''**.
3.  Impostare i parametri della scanalatura (vedere la prossima sezione).
4.  Premere **OK**.


</div>

## Opzioni

Quando si crea una scanalatura, i dialoghi **Parametri Groove** offrono diversi parametri che specificano come deve essere ruotato lo sketch.

+++
| ![](images/Partdesign_groove_parameters_it.png ) | ### Assi                                                                                                                                                                                                                                                                                                                                      |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                              |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                | Questa opzione specifica l\'asse attorno al quale deve essere ruotato lo schizzo.                                                                                                                                                                                                                                                             |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | -   **Vertical sketch axis**: seleziona l\'asse verticale dello schizzo.                                                                                                                                                                                                                                                                      |
|                                                                                | -   **Horizontal sketch axis**: seleziona l\'asse orizzontale dello schizzo.                                                                                                                                                                                                                                                                  |
|                                                                                | -   **Sketch axis**: seleziona una linea di costruzione contenuta nello schizzo utilizzato da Scanalatura. La prima linea di costruzione creata nello schizzo viene etichettata come *Sketch axis 0*. L\'elenco a discesa contiene un asse dello schizzo personalizzato per ogni linea di costruzione. {{VersionMinus/it|0.16}} |
|                                                                                | -   **Construction line**: seleziona una linea di costruzione contenuta nello schizzo utilizzato da Scanalatura. L\'elenco a discesa contiene una voce per ogni linea di costruzione. La prima linea di costruzione creata nello schizzo viene etichettata *Construction line 1*. {{VersionPlus/it|0.17}}                       |
|                                                                                | -   **Base (X/Y/Z) axis**: v0.17 e superiore seleziona l\'asse X, Y o Z dell\'origine del corpo; {{VersionPlus/it|0.17}}                                                                                                                                  |
|                                                                                | -   **Select reference\...**: v0.17 e superiore consente di selezionare nella vista 3D un bordo di un corpo o una [linea di riferimento](PartDesign_Line/it.md). {{VersionPlus/it|0.17}}                                                          |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                | </div>                                                                                                                                                                                                                                                                                                                                        |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                | ### Angolo                                                                                                                                                                                                                                                                                                                                    |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | Questa opzione specifica l\'angolo di rotazione dello schizzo. Per ottenere una scanalatura completa occorre impostare un angolo di 360°. Non è possibile specificare angoli negativi (se è necessario usare l\'opzione **Invertito**) o angoli maggiori di 360°.                                                                             |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | ### Simmetrico al piano                                                                                                                                                                                                                                                                                                 |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | La rivoluzione si estende per metà dell\'angolo specificato in entrambe le direzioni rispetto al piano di schizzo.                                                                                                                                                                                                                            |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | ### Invertito                                                                                                                                                                                                                                                                                                                                 |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | La direzione di rivoluzione viene invertita.                                                                                                                                                                                                                                                                                                  |
+++

## Proprietà

Sotto sono riportate le proprietà che possono essere definite dopo la creazione della funzione. Le proprietà Dati *Base* e *Axis* non sono editabili.


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Angle}}: angolo di rotazione. Vedere [Angolo](#Angolo.md).

-    {{PropertyData/it|Label}}: etichetta data all\'operazione, può essere cambiata a piacere.

-    {{PropertyData/it|Midplane}}: true o false. Vedere [Simmetrica al piano](#Simmetrica_al_piano.md).

-    {{PropertyData/it|Reversed}}: true o false. Vedere [Invertita](#Invertita.md).

-    {{PropertyData/it|Refine}}: true o false. Se impostato su true, pulisce il solido dai bordi residui lasciati dalle funzioni. Per maggiori dettagli vedere [Affina forma](Part_RefineShape/it.md). {{VersionPlus/it|0.17}}


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/it
