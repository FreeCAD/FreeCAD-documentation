---
- GuiCommand:Addon/it
   Name:BIM Views
   Name/it:Viste BIM
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/it.md)
   Addon:BIM
   MenuLocation:Gestione - Viste
---

# BIM Views/it

## Descrizione

Il gestore delle viste e dei livelli BIM è una finestra agganciabile che si apre sotto la normale visualizzazione ad albero, che contiene tutte le [Parti di edificio](Arch_BuildingPart/it.md) e tutti i [Piani Proxy](Draft_WorkingPlaneProxy/it.md) del modello.

Lo scopo di questa finestra è permettere di accedere velocemente ai propri livelli e alle configurazioni del piano di lavoro, senza la necessità di navigare nell\'albero per trovarli.

<img alt="" src=images/BIM_views_screenshot.png  style="width:800px;">

## Utilizzo

Il gestore delle viste BIM mostrerà tutti i livelli (parti dell\'edificio) e i proxy del piano di lavoro del tuo documento. Può essere agganciato ovunque nell\'interfaccia di FreeCAD o lasciato in una finestra autonoma. Le parti dell\'edificio mostreranno anche il loro livello (la coordinata Z del loro posizionamento).

-   Premendo Ctrl+9 o facendo clic sul pulsante **Viste BIM** nell\'angolo in basso a destra dello schermo viene visualizzato o nascosto il gestore Viste BIM
-   Facendo clic su qualsiasi voce si seleziona l\'oggetto corrispondente
-   Facendo doppio clic sull\'altezza di un livello puoi modificarlo
-   Facendo doppio clic sul nome di qualsiasi oggetto si imposta su di esso il piano di lavoro e, se l\'opzione **Ripristina vista** dell\'oggetto è attivata ed è stata memorizzata una configurazione della vista, anche quel punto di vista è ripristinato
-   Facendo clic sul pulsante **Aggiungi un nuovo livello** viene creato un nuovo [livello](Arch_BuildingPart.md)
-   Facendo clic sul pulsante **Aggiungi un nuovo piano di lavoro proxy** viene creato un nuovo [piano di lavoro proxy](Draft_WorkingPlaneProxy.md)
-   Facendo clic sul pulsante **Elimina** si elimina l\'elemento selezionato
-   Facendo clic sul pulsante **Attiva/disattiva** si attiva/disattiva un livello selezionato (come usando la barra spaziatrice)
-   Facendo clic sul pulsante **Isola** si disattivano tutti i livelli tranne quello selezionato
-   Facendo clic sul pulsante **Salva posizione telecamera** vengono memorizzate le impostazioni di visualizzazione correnti nell\'oggetto selezionato, consentendo di ripristinarlo se la sua proprietà **Ripristina vista** è impostata su True
-   Facendo clic sul pulsante **Rinomina** è possibile rinominare un oggetto selezionato



---
![](images/Button_right.svg) [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > BIM Views/it
