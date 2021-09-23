# Macro Manage Navigational Style2/it
 {{Macro
|Name=Macro Manage Navigational Styles2
|Icon=Macro_Manage_Navigational_Styles2.png
|Translate=Stile di navigazione 2
|Description=Questa macro consente di modificare Inventor stile di navigazione durante l'utilizzo dello Sketcher. <br/> Quando si utilizza lo Sketcher, il menu del pulsante destro viene ridefinito per contenere le opzioni relative allo Sketcher. Di conseguenza, l'opzione per modificare lo stile di navigazione, disponibile all'esterno dello Sketcher, non è disponibile nello Sketcher.
|Author=PiffPoof
|Version=1.0
|Date=2015-01-17
|FCVersion=Tutte
|Download=[https://www.freecadweb.org/wiki/images/1/1c/Macro_Manage_Navigational_Styles2.png ToolBar icon]
|SeeAlso=[Stile di navigazione 1](Macro_Manage_Navigational_Style/it.md)
}}

## Descrizione

Quando si utilizza Sketcher il tasto destro del tasto viene ridefinito per contenere le opzioni relative a Sketcher. Di conseguenza, in Sketcher non è disponibile la possibilità di cambiare lo stile di navigazione che è disponibile al di fuori di esso.

## Installazione

Ci sono due brevi codici, ciascuno dei quali costituisce una macro indipendente. L\'installazione si realizza copiando i due codici nella directory appropriata delle Macro. Dopo si può invocare il comando dal menu Macro. È utile aggiungerle entrambe a una barra in modo da renderle facilmente disponibili durante l\'utilizzo di Sketcher.

-   per informazioni su come installare il codice delle macro vedere la pagina [Come installare le macro](How_to_install_macros/it.md)
-   per informazioni su come installarla abbinata a un pulsante in una barra degli strumenti vedere la pagina [Personalizzare la barra degli strumenti](Customize_Toolbars/it.md)

## Utilizzo

Fare clic sul pulsante della barra degli strumenti associato alle macro, o richiamarle dal menu Macro. Il modo di navigazione cambia, ma la loro esecuzione non è confermata da nulla di visibile.

## Interfaccia utente 

Non c\'è veramente nessuna interfaccia utente e neppure nessuna conferma che lo stile di navigazione è stato modificato. La conferma si ha quando, nella successiva manipolazione della vista, i movimenti del mouse sono interpretati nello stile di navigazione selezionato.

## Script

-   l\'icona e il codice della macro per cambiare lo stile di navigazione in \'Inventor\'

![](images/Macro_Manage_Navigational_Styles2.png )

**Macro\_Manage\_Navigational\_Styles2\_Inventor.FCMacro**


{{MacroCode|code=
# change to Inventor Navigational Style
p=App.ParamGet("User parameter:BaseApp/Preferences/View")
p.SetString("NavigationStyle","Gui::InventorNavigationStyle")
}}




