---
 GuiCommand:
   Name: Sketcher CarbonCopy
   Name/it: Copia carbone
   MenuLocation: Schizzo , Strumenti Sketcher , Crea copia carbone
   Workbenches: Sketcher Workbench/it
   Shortcut: **G** **W**
   Version: 0.17
---

# Sketcher CarbonCopy/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:24px;"> [Sketcher Copia carbone](Sketcher_CarbonCopy/it.md) copia tutta la geometria e i vincoli da un altro schizzo nello schizzo attivo.

I vincoli dimensionali che esistono prima della funzione di copia rimangono collegati ai vincoli dimensionali dello schizzo originale attraverso le [espressioni](Expressions/it.md).



## Utilizzo

1.  Assicurarsi di essere nella modalità di modifica di uno [schizzo](Sketcher_NewSketch/it.md) esistente. Questo schizzo è il destinatario dell\'operazione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CarbonCopy.svg" width=16px> [Crea copia carbone](Sketcher_CarbonCopy/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Strumenti Sketcher → <img src="images/Sketcher_CarbonCopy.svg" width=16px> Crea copia carbone** dal menu.
    -   Usare la scorciatoia da tastiera: **G** quindi **W**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Scegliere un bordo da un altro schizzo. Questo schizzo è la fonte dell\'operazione. Vedere [Note](#Note.md).
5.  Gli elementi geometrici e i vincoli vengono copiati nello schizzo attivo.
6.  Questo strumento viene sempre eseguito in modalità continua: facoltativamente copiare schizzi aggiuntivi.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-   Nell\'[Ambiente PartDesign](PartDesign_Workbench/it.md) è possibile selezionare lo schizzo da copiare dall\'esterno del [Corpo](PartDesign_Body/it.md) dello schizzo attualmente attivo, ma solo se il tasto **Ctrl** è tenuto premuto durante la selezione.
-   Lo schizzo da copiare in copia carbone deve essere piano parallelo allo schizzo attualmente attivo. In caso contrario, durante la selezione è necessario tenere premuti i tasti **Ctrl** e **Alt**. Questo funziona anche per gli schizzi situati al di fuori del corpo attivo.
-   Se la [geometria di costruzione](Sketcher_ToggleConstruction/it.md) è attiva, la geometria copiata viene creata come geometria di costruzione.
-   Viene copiato lo schizzo completo, non è possibile selezionarne solo una porzione. Ma dopo la copia è possibile eliminare gli elementi indesiderati.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/it
