---
- GuiCommand:/it   Name:Std_UnitsCalculator   Name/it:Convertitore di unità   MenuLocation:Strumenti → Convertitore di unità...   Workbenches:Tutti   SeeAlso:---

## Descrizione

Il comando **Convertitore di unità** apre la finestra di dialogo per convertire i valori da un sistema di unità di misura ad un altro.

![](images/Units_Calculator_it.png ) *La finestra di dialogo del Convertitore di unità*

## Utilizzo

1.  Selezionare l\'opzione **Strumenti → <img src="images/Std_UnitsCalculator.svg" width=16px> Convertitore di unità...** dal menu.
2.  Viene visualizzata la finestra di dialogo Convertitore di unità. Per ulteriori informazioni, vedere le [Opzioni](#Opzioni.md).
3.  La finestra di dialogo non è modale, il che significa che può rimanere aperta mentre si continua a lavorare in FreeCAD.
4.  Premere il pulsante **Chiudi** per chiudere la finestra di dialogo.

## Opzioni

### Riga superiore 

1.  Immettere un valore con le unità nella prima casella di input. Per esempio {{Value|10 mm}}.
    -   Le unità con esponenti devono essere inserite usando la notazione {{Value|^}}. Ad esempio {{Value|1 m^2}}.
    -   Se il valore di input non può essere riconosciuto o se le unità sono sconosciute, nella casella **=\>** viene visualizzato il messaggio \"Errore di sintassi\".
2.  Immettere le unità di destinazione nella casella di input **come**. Per esempio {{Value|in}}.
    -   Se le unità sono sconosciute, nella casella **=\>** viene visualizzato il messaggio \"Errore di sintassi\".
    -   Se il tipo di unità nella prima e nella seconda casella di input non corrispondono, nella casella **=\>** viene visualizzato il messaggio \'unità non corrispondenti\'. Nell\'esempio le unità corrispondono in quanto \'mm\' e \'in\' sono entrambe unità di lunghezza.
3.  Se non ci sono errori di input, la casella **=\>** mostra immediatamente il risultato. Per i valori di esempio il risultato è {{Value|0,394 in}}.
4.  Facoltativamente, premere il pulsante **Copia** per copiare il contenuto della casella **=\>** negli appunti. Ad esempio, è possibile incollare il valore in un pannello delle azioni o in una finestra di dialogo di FreeCAD.

### Area di testo 

1.  La conversione eseguita nella riga superiore può essere copiata nell\'area di testo premendo **Invio** nella prima o nella seconda casella di input.
2.  L\'area di testo può contenere più conversioni e il suo contenuto può essere selezionato e copiato negli appunti con **Ctrl+C** e utilizzato in altri programmi.

### Quantità


**Questa nuova parte ({{Version/it|0.19**) del convertitore di unità presenta ancora alcuni bug.}}

1.  Selezionare un\'opzione dall\'elenco a discesa \"Sistema di unità\". Questo sarà il sistema di unità di destinazione. Selezionare **Sistema delle preferenze** per utilizzare il sistema di unità definito nelle [Preferenze](Preferences_Editor/it#Unità.md).
2.  Selezionare un\'opzione dall\'elenco a discesa **Categoria di unità**.
3.  Immettere un valore con le unità nella casella di input **Quantità**. Le unità devono corrispondere alla categoria dell\'unità.
    -   Se è stata selezionata la categoria di unità **Area**, l\'immissione di determinate unità è problematica. Ad esempio per inserire {{Value|m^2}} bisogna inserire prima {{Value|^2}}, posizionare il cursore prima del carattere {{Value|^}} e quindi inserire {{Value|m}}.
4.  Fare clic nella casella di input **Decimali** e premere **Invio** per convertire il valore nella casella di input **Quantità**.

## Note

-   Vedere la pagina [Espressioni](Expressions/it#Unità.md) per un elenco di tutte le unità conosciute.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
