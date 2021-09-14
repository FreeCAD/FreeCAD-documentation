# Report view/it



## Introduzione

La [Vista report](Report_view/it.md) è un pannello che mostra i messaggi di testo dei processi e degli strumenti di FreeCAD. È disponibile nel menu **{{StdMenu|[Visualizza](Std_View_Menu/it.md)** → Pannelli → Vista report}}.

Alcune proprietà di questo pannello, come il colore del testo e se visualizzarlo automaticamente in caso di avvisi o di errori, possono essere configurate nella scheda **Generali → Output** nell\'[editor delle preferenze](Preferences_Editor/it.md).

<img alt="" src=images/FreeCAD_Report_view.png  style="width:800px;">


*Vista report che mostra i messaggi quando FreeCAD è appena stato avviato.*

## Messagi


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

La vista report mostra i messaggi della classe interna `Console` di FreeCAD.

-    `FreeCAD.Console.PrintMessage("text")`, stampa qualsiasi tipo di messaggio informativo, che non implica alcun comportamento scorretto; ad esempio, stampa le coordinate dei punti, il risultato di un calcolo della distanza, il numero di vertici in una forma, ecc. Per impostazione predefinita, in colore nero.

-    `FreeCAD.Console.PrintWarning("text")`, stampa i messaggi che hanno lo scopo di avvisare l\'utente di comportamenti strani nell\'applicazione. Gli avvisi sono mostrati quando mancano alcune funzionalità ma il software funziona ancora in modo accettabile. Di default, in colore giallo.

-    `FreeCAD.Console.PrintError("text")`, stampa i messaggi di errore, vale a dire quando manca un componente critico che fa fallire una determinata operazione. Di default, in colore rosso.

-    `FreeCAD.Console.PrintLog("text")`, stampa i messaggi che vanno anche nei registri. Questi messaggi possono essere utili in seguito per risolvere un problema leggendo i registri, ad esempio quando si avvia o si chiude un ambiente. Di default, in colore blu.

Queste funzioni possono essere utilizzate direttamente dalla [console Python](Python_console/it.md), o tramite le [macro](Macros/it.md) e gli ambienti personalizzati.

<img alt="" src=images/FreeCAD_Report_view_example.png  style="width:800px;">


*Esempio di messaggi nella vista report: un messaggio generale, un avviso, un errore e un messaggio registrato.*

## Azioni

Fare clic con il tasto destro sulla vista del report per mostrare alcuni comandi:

-    **Opzioni**: registro, avviso, errore, reindirizza l\'output Python, reindirizza gli errori di Python, vai alla fine.

-    **Copia**: memorizza il testo selezionato negli appunti per un successivo incollaggio; è disabilitato se non è selezionato nulla.

-    **Seleziona tutto**: seleziona tutto il testo della vista report.

-    **Pulisci**: cancella tutti i messaggi nella vista report. Ciò è utile se si desidera risolvere uno problema che stampa i messaggi nella vista report e si desidera assicurarsi che non vi siano vecchi messaggi di problemi precedenti.

-    **Salva con nome**: salva i messaggi della vista report in un file di testo.


{{Interface navi

}} {{Std Base navi}} 
