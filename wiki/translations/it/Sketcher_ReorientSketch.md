---
 GuiCommand:
   Name: Sketcher_ReorientSketch
   Name/it: Sketcher Riposiziona lo schizzo
   MenuLocation: Schizzo , Riposiziona lo schizzo
   Workbenches: Sketcher_Workbench/it, PartDesign_Workbench/it
   SeeAlso: Sketcher_MapSketch/it, Sketcher_NewSketch/it
---

# Sketcher ReorientSketch/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:24px;"> [Riposiziona lo schizzo](Sketcher_ReorientSketch/it.md) posiziona uno schizzo su uno dei piani principali con un offset opzionale. Può essere utilizzato anche per staccare uno schizzo.



## Utilizzo

1.  Selezionare uno schizzo.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ReorientSketch.svg" width=16px> [Riposiziona lo schizzo](Sketcher_ReorientSketch/it.md)** (non disponibile in [PartDesign ](PartDesign_Workbench/it.md)).
    -   Selezionare l\'opzione **Schizzo → <img src="images/Sketcher_ReorientSketch.svg" width=16px> Riposiziona lo schizzo** dal menu.
3.  Nel caso in cui lo schizzo è supportato:
    1.  Si apre la finestra di dialogo **Lo schizzo ha un supporto**.
    2.  Premere il pulsante **Sì** per staccare lo schizzo.
4.  Si apre la finestra di dialogo **Orientamento**.
5.  Facoltativamente, premere il pulsante **Annulla** per staccare solamente lo schizzo e completare l\'operazione.
6.  Specificare il piano per l\'orientamento. Il piano è relativo al sistema di coordinate locali in cui si trova lo schizzo:
    -   Se la casella di controllo **Direzione inversa** non è selezionata:
        -   In alto: **Piano XY**
        -   Di fronte: **Piano XZ**
        -   A destra: **Piano YZ**
    -   Se la casella di controllo **Direzione inversa** è selezionata:
        -   In basso: **Piano XY**
        -   Dietro: **Piano XZ**
        -   A sinistra: **Piano YZ**
7.  Facoltativamente modificare l\' **Offset**. L\'offset viene misurato lungo l\'asse Z, Y o X del sistema di coordinate locale.
8.  Premere il pulsante **OK**.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ReorientSketch/it
