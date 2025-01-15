---
 GuiCommand:
   Name: Sketcher ToggleDrivingConstraint
   Name/it: Sketcher Attiva/disattiva vincolo di guida/riferimento
   Workbenches: Sketcher Workbench/it
   Shortcut: **K** **X**
   Version: 0.16
   SeeAlso: Sketcher_ToggleActiveConstraint/it
---

# Sketcher ToggleDrivingConstraint/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:24px;"> [Sketcher Attiva/disattiva vincolo di guida/riferimento](Sketcher_ToggleDrivingConstraint/it.md) alterna gli [strumenti di creazione di vincoli dimensionali](Sketcher_Workbench/it#Sketcher_CompDimensionTools.md) tra la modalità di guida e quella di riferimento oppure alterna i vincoli dimensionali selezionati tra quelli modalità.

Contrariamente ai vincoli guida, i vincoli di riferimento non vincolano lo schizzo, il loro valore dipende da altri vincoli e sono guidati. Possono essere utili per verificare le misurazioni. Possono essere utilizzati in [espressioni](Expressions/it.md), ma non nello schizzo stesso.

![](images/Sketcher_ToggleConstraint_example.png ) 
*Un vincolo guida di distanza orizzontale (50 mm), un vincolo guida di distanza verticale (30 mm) e un vincolo guida di angolo (75°) sono stati impostati per definire il profilo; è stata aggiunta una quota di riferimento sul segmento di linea obliqua per conoscerne la lunghezza (31,0583 mm).*



## Utilizzo



### Attiva/disattiva strumenti 

1.  Assicurarsi che non siano stati selezionati vincoli dimensionali.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> [Attiva/disattiva vincolo di guida/riferimento](Sketcher_ToggleDrivingConstraint/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> Attiva/disattiva vincolo di guida/riferimento** dal menu.
    -   Usare la scorciatoia da tastiera: **K** quindi **X**.
3.  La modalità degli strumenti di creazione dei vincoli dimensionali viene attivata:
    -   In modalità guida le icone del menu e della barra degli strumenti sono rosse e creano vincoli di guida (predefinito [color](Sketcher_Preferences/it#Appearance.md) rosso). L\'icona di questo strumento è quindi: <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:16px;">.
    -   In modalità riferimento le icone dei menu e della barra degli strumenti sono blu e creano vincoli di riferimento (colore predefinito blu). L\'icona di questo strumento è quindi: <img alt="" src=images/Sketcher_ToggleConstraint_Driven.svg  style="width:16px;">.



### Attiva/disattiva vincoli 

1.  Selezionare uno o più vincoli dimensionali.
2.  Richiamare lo strumento come descritto sopra o con una delle seguenti opzioni aggiuntive:
    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [3D view](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> Attiva/disattiva vincolo di guida/riferimento** da il menu contestuale.

    -   Fare clic con il pulsante destro del mouse sulla sezione **Vincoli** della [Finestra di dialogo Sketcher](Sketcher_Dialog/it.md) e selezionare l\'opzione **Attiva/disattiva da/in riferimento** dal menu contestuale.
3.  I vincoli selezionati vengono modificati dalla modalità di guida alla modalità di riferimento o viceversa. Il loro aspetto cambia di conseguenza.
4.  La modalità degli strumenti di creazione dei vincoli dimensionali non viene modificata.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/it
