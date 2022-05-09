# Part Mirror/it
---
- GuiCommand   */it   Name   *Part_Mirror   Name/it   *Specchia   MenuLocation   *Parte → Specchia...   Workbenches   *[[Part_Workbench/it   Parte]]|SeeAlso   *---


</div>

## Descrizione

Crea un nuovo oggetto (un duplicato) di un oggetto di tipo **Parte** che è una riflessione dell\'oggetto originale (sorgente). L\'oggetto duplicato viene creato tramite un piano di riflessione. Il piano di riflessione può essere un piano standard (XY, YZ o XZ), o qualsiasi piano parallelo ad un piano standard.

Esempio   *

![L\'oggetto originale](images/PARTMirrorBeforev11.png )

![L\'originale e il duplicato (riflesso rispetto al piano **YZ**)](images/PARTMirrorAfterv11.png ) 

## Utilizzo

![](images/PARTMirrorDialogv11.png )

1.  Selezionare l\'oggetto sorgente nella lista.
2.  Selezionare un **Piano di specchiatura**.
3.  Premere **OK** per creare il duplicato.




## Opzioni

Le caselle **Punto base** possono essere utilizzate per spostare il piano di specchiatura parallelamente al piano standard selezionato (scostamento). Solo una delle caselle **X**, **Y**, o **Z** è attiva per un determinato piano.

  Piano Standard   Punto Base     Effetto
    
  **XY**           **Z**          Sposta il piano lungo l\'asse **Z**.
  **XY**           **X**, **Y**   Nessun effetto.
  **XZ**           **Y**          Sposta il piano lungo l\'asse **Y**.
  **XZ**           **X**, **Z**   Nessun effetto.
  **YZ**           **X**          Sposta il piano lungo l\'asse **X**.
  **YZ**           **Y**, **Z**   Nessun effetto.

## Notes


<div class="mw-translate-fuzzy">

## Limitazioni

-   Al momento non è possibile usare dei piani arbitrari, non paralleli ai piani standard, come piani di specchiatura.


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/it
