---
 GuiCommand:
   Name: Sketcher ToggleConstruction
   Name/it: Geometria di costruzione
   MenuLocation: Schizzo , Geometrie Sketcher , Geometria di costruzione
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **N**
   SeeAlso: 
---

# Sketcher ToggleConstruction/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:24px;"> [Sketcher Geometria di costruzione](Sketcher_ToggleConstruction/it.md) attiva/disattiva gli strumenti di creazione della geometria nella/dalla modalità di costruzione oppure attiva/disattiva la geometria selezionata nella/dalla geometria di costruzione.

La geometria di costruzione è contrassegnata con un [colore](Sketcher_Preferences/it#Appearance.md) (blu predefinito) e un tipo di linea ({{Version/it|1.0}}) dedicati. La geometria di costruzione non è visibile all\'esterno dello schizzo, ha lo scopo di aiutare a definire i vincoli e altre geometrie all\'interno dello schizzo stesso. Le linee di costruzione possono tuttavia essere utilizzate come asse di rotazione da [PartDesign Rivoluzione](PartDesign_Revolution/it.md).

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">



## Utilizzo



### Attiva/disattiva strumenti 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> [Geometria di costruzione](Sketcher_ToggleConstruction/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Geometria Sketcher → <img src="images/Sketcher_ToggleConstruction.svg" width=16px> Geometria di costruzione** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> Geometria di costruzione** dal menu contestuale.
    -   Usare la scorciatoia da tastiera: **G** quindi **N**.
3.  La modalità degli strumenti di creazione della geometria viene attivata:
    -   In modalità normale le icone dei menu e delle barre degli strumenti sono bianche e creano una geometria regolare (colore predefinito bianco). L\'icona di questo strumento è quindi: <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:16px;">.
    -   In modalità costruzione le icone del menu e della barra degli strumenti sono blu e creano la geometria di costruzione (colore predefinito blu). L\'icona di questo strumento è quindi: <img alt="" src=images/Sketcher_ToggleConstruction_Constr.svg  style="width:16px;">.



### Attiva/disattiva geometria 

1.  Selezionare uno o più elementi nello schizzo.
2.  Richiamare lo strumento come descritto sopra o con la seguente opzione aggiuntiva:
    -   Fare clic con il pulsante destro del mouse nella sezione **Elementi** della finestra [Dialogo Sketcher](Sketcher_Dialog/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> Geometria di costruzione** dal menu contestuale.
3.  Gli elementi selezionati vengono modificati dalla geometria normale alla geometria di costruzione o viceversa. Il loro aspetto cambia di conseguenza.
4.  La modalità degli strumenti di creazione della geometria non viene modificata.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/it
