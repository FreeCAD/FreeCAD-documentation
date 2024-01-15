# Draft Constrain/it
## Descrizione

Oltre all\'inserimento delle coordinate o all\'uso degli [agganci](Draft_Snap/it.md) (snap), esiste una funzione chiamata vincolo che aiuta a disegnare con precisione in ambiente <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md) e <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench/it.md). Per ogni punto successivo è possibile vincolare il movimento del cursore alla direzione X, Y o Z del sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). Questo può essere utilizzato ad esempio per creare una linea perfettamente verticale.

I vincoli sono disponibili con la maggior parte dei comandi [Draft](Draft_Workbench/it.md) e [Arch](Arch_Workbench/it.md).

![](images/Draft_Constrain_taskpanel_example.png ) 
*Mentre il cursore è vincolato, il pannello delle attività blocca i valori che non vengono modificati*



## Utilizzo vincoli orizzontali e verticali 

1.  Scegliere un comando [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) per creare la propria geometria.
2.  Scegliere un primo punto. È necessario un punto precedente.
3.  Effettuare una delle seguenti operazioni:
    -   Per un vincolo orizzontale: spostare il cursore a sinistra o a destra del punto precedente.
    -   Per un vincolo verticale: spostare il cursore sopra o sotto il punto precedente.
4.  Tenere premuto **Shift**.
5.  Il cursore è ora vincolato.
6.  Scegliere il punto successivo.
7.  Se il comando è ancora attivo: facoltativamente rilasciare **Shift** per disabilitare il vincolo.
8.  Rilasciare sempre **Shift** al termine del comando.



## Utilizzo vincoli X, Y e Z 

1.  Scegliere un comando [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) per creare la propria geometria.
2.  Scegliere un primo punto. È necessario un punto precedente.
3.  Premere **X**, **Y** o **Z** per specificare la direzione.
4.  Il cursore è ora vincolato.
5.  Scegliere il punto successivo.
6.  Se il comando è ancora attivo, opzionalmente, eseguire una delle seguenti operazioni:
    -   Premere lo stesso tasto per disabilitare il vincolo.
    -   Premere uno degli altri due tasti per vincolare in una direzione diversa.
7.  I vincoli X, Y e Z vengono automaticamente disabilitati al termine del comando.



## Note

-   I vincoli possono essere combinati con gli [agganci](Draft_Snap/it.md).
-   Il comando [Draft Offset](Draft_Offset/it.md) e il comando [Draft Taglia/Estendi](Draft_Trimex/it.md) utilizzano un diverso tipo di vincolo, ovvero per limitare l\'operazione a un determinato segmento.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Il tasto predefinito **Modalità di Vincolo**, **Shift**, può essere modificato: **Modifica → Preferenze... → Draft → Griglia e agganci  → Modalità di Vincolo**.
-   Le scorciatoie **X**, **Y** e **Z** possono essere modificate: **Modifica → Preferenze... → Draft → Interfaccia →  Scorciatoie comandi**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Constrain/it
