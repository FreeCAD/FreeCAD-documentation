# Addon/it
## Introduzione

In FreeCAD e in questa documentazione, un addon è un componente che non fa parte dell\'installazione di base di FreeCAD, ma che può essere aggiunto al sistema con determinati metodi.

## I diversi tipi 

Esistono tre tipi di componenti aggiuntivi   *

-   Le [Macro](Macros/it.md)   * brevi frammenti di codice [Python](Python/it.md) che forniscono un nuovo strumento o funzionalità in un singolo file che termina con `.FCMacro`.
-   I Moduli   * un singolo file sorgente Python o una raccolta di file Python che estende il software in qualche modo. I moduli non definiscono necessariamente un \"ambiente di lavoro\" grafico ma possono fornire una funzione di supporto, ad esempio una libreria che esegue la conversione di formati o un codice che modifica l\'[interfaccia](interface/it.md) grafica.
-   Gli [Ambienti](External_workbenches/it.md)   * raccolte di file Python che forniscono [comandi GUI](Gui_Command/it.md) (strumenti) correlati, centrati su un argomento particolare, ad esempio strumenti per progettare cabine o strumenti per lavorare con l\'architettura o strumenti per progettare barche, ecc. Questi ambienti di lavoro di solito definiscono nuove barre degli strumenti in cui sono posizionati i pulsanti dei [comandi](Gui_Command/it.md).

Le macro sono installate nella directory `Macro/` dell\'utente, mentre i moduli e gli ambienti si trovano nella directory `Mod/`. {{Code|lang=bash|code=
$HOME/.FreeCAD/Macro/
$HOME/.FreeCAD/Mod/
}}

Le macro di solito all\'inizio sono un modo per semplificare o automatizzare l\'attività di disegno o modifica di un oggetto particolare. Se molte di queste macro vengono raccolte in una directory, e viene fornita la struttura per raccogliere tali strumenti, allora l\'intera directory può essere distribuita come un nuovo ambiente.

In altre parole, macro, moduli e ambienti sono essenzialmente la stessa cosa, pezzi di codice Python che estendono l\'installazione di base. Le macro sono in genere brevi utilità incentrate su una singola attività, mentre gli ambienti sono raccolte di strumenti organizzati e interfacce grafiche per eseguire attività correlate.

Se un ambiente è sufficientemente sviluppato ed è ben documentato, può essere incluso come [ambiente](workbenches/it.md) di base in FreeCAD.

## Installazione

A partire da FreeCAD 0.17, il modo consigliato per installare i componenti aggiuntivi è tramite <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr/it.md).

L\'installazione manuale è ancora possibile.

-   [Come installare le macro](How_to_install_macros/it.md)
-   [Installare ambienti aggiuntivi](Installing_more_workbenches/it.md)




[Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/it
