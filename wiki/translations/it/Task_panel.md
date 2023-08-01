# Task panel/it
## Introduzione


<div class="mw-translate-fuzzy">

Il [pannello delle attivitàzioni](task_panel/it.md) appare nella scheda **Azioni** della [vista combinata](combo_view/it.md). È uno spazio personalizzabile in grado di contenere qualsiasi tipo di widget grafico come finestre secondarie espandibili, tabelle, campi di input, caselle di controllo, caselle di selezione, caselle di testo, caselle di testo, pulsanti, etichette, immagini e altri elementi, secondo l\'[ambiente](Workbenches/it.md) e lo strumento attualmente attivi.


</div>


<div class="mw-translate-fuzzy">

![](images/FreeCAD_Combo_view_Task_panel.png )


</div>


<div class="mw-translate-fuzzy">



*Il pannello delle azioni che mostra i vari comandi con  [PartDesign](PartDesign_Workbench/it.md) attivo.*


</div>

## Lavorare con il pannello delle azioni 

Un pannello delle azioni si apre quando viene attivato uno strumento che richiede l\'input dell\'utente, premendo un pulsante della barra degli strumenti o facendo doppio clic su un oggetto. Se lo strumento non necessita dell\'input dell\'utente, produce il suo risultato o termina, ma non visualizza un pannello delle azioni.

L\'input dell\'utente può essere costituita da qualsiasi cosa come testo, coordinate di punti 3D, elementi di un elenco, facce di una forma o opzioni per modificare il modo in cui lo strumento funziona.

![](images/FreeCAD_Combo_view_Task_panel_Sketcher.png )


<div class="mw-translate-fuzzy">



*Il pannello delle azioni che si apre quando viene modificato uno [schizzo](Sketcher_Workbench/it.md). Vengono presentati vari tipi di informazioni come messaggi del risolutore, opzioni per la griglia, vincoli ed elementi geometrici.*


</div>


<div class="mw-translate-fuzzy">

Esistono molti comandi che richiedono la selezione di forme o oggetti presenti nel documento; per tali casi il pannello delle azioni attende che l\'utente selezioni gli oggetti appropriati dalla [vista ad albero](tree_view/it.md) o nella [vista 3D](3D_view/it.md). Quando un pannello azioni è aperto, è possibile passare alla scheda **Modello** per visualizzare la [vista ad albero](tree_view/it.md) per scegliere un oggetto; una volta fatto ciò, è possibile tornare alla scheda **Azioni** per procedere con il comando. Il pannello delle azioni viene normalmente chiuso facendo clic su un pulsante **OK** o **Chiudi** o premendo il tasto **Esc** sulla tastiera per interrompere il comando.


</div>

![](images/FreeCAD_Combo_view_Task_panel_ArchComponent.png )


<div class="mw-translate-fuzzy">



*Il pannello delle azioni che si apre quando si modifica un [Componente Arch](Arch_Component/it.md). Il pannello attende che l'utente selezioni gli oggetti che possono essere aggiunti o sottratti dal componente.*


</div>


<div class="mw-translate-fuzzy">

In particolare, il passaggio dalla scheda **Azioni** alla scheda **Modello** non termina il comando attivo; l\'azione rimane ancora in esecuzione in background. L\'utente è responsabile della corretta conclusione o interruzione del comando attivo prima di iniziare una nuova azione; lasciare un\'azione in esecuzione può produrre errori quando si tenta di avviare altri strumenti.


</div>

## Notes

-   Users migrating from other CAD solutions that use the **ESC** key as part of their workflow may get different results in FreeCAD. When **ESC** is pressed in FreeCAD the task panel that has the focus will close. To disable this functionality, please see [Fine tuning](Fine-tuning#Escape_Key.md) and [Sketcher Preferences](Sketcher_Preferences#General.md).


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > Task panel/it
