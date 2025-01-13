---
 GuiCommand:
   Name: Sketcher NewSketch
   Name/it: Sketcher Crea schizzo
   MenuLocation: Schizzo , Crea uno schizzo
   Workbenches: Sketcher_Workbench/it
   SeeAlso: PartDesign_NewSketch/it, Sketcher_MapSketch/it, Sketcher_ReorientSketch/it
---

# Sketcher NewSketch/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Crea schizzo](Sketcher_NewSketch/it.md) crea un nuovo schizzo e apre la finestra [Dialogo Sketcher](Sketcher_Dialog/it.md) per modificarlo.

Si noti che <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/it.md) ha il proprio strumento [nuovo schizzo](PartDesign_NewSketch/it.md). Quando si lavora su un [Corpo di PartDesign](PartDesign_Body/it.md) dovrebbe essere usato quello strumento.



## Utilizzo

1.  Se lo schizzo deve essere [associato](Part_EditAttachment/it.md) alla geometria esistente: selezionare un oggetto con una forma, o uno o più vertici, bordi e/o facce e/o un piano.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_NewSketch.svg" width=16px> [Crea schizzo](Sketcher_NewSketch/it.md)**.
    -   Selezionare l\'opzione **Sketch → <img src="images/Sketcher_NewSketch.svg" width=16px> Crea schizzo** dal menu.
3.  Se è stata selezionata la geometria:
    1.  Si apre la finestra di dialogo **Associazione Schizzo**.
    2.  Selezionare un [metodo di associazione](Part_EditAttachment/it#Attachment_modes.md) dall\'elenco a discesa. Oppure selezionare **Non associare** per ignorare la selezione.
    3.  Premere il pulsante **OK**.
4.  Se non è presente alcuna selezione o è stato selezionato **Non associare** nel passaggio precedente:
    1.  Si apre la finestra di dialogo **Scegli orientamento**.
    2.  Specificare il piano per l\'orientamento. Il piano è relativo al sistema di coordinate locali in cui si trova lo schizzo:
        -   Se la casella di controllo **Inverti direzione** non è selezionata:
            -   In alto: **Piano XY**
            -   Davanti: **XZ-Plane**
            -   Destra: **Piano YZ**
        -   Se la casella di controllo **Direzione inversa** è selezionata:
            -   In basso: **Piano XY**
            -   Posteriore: **XZ-Plane**
            -   A sinistra: **Piano YZ**
    3.  Facoltativamente modificare l**Offset**. L\'offset viene misurato lungo l\'asse Z, Y o X del sistema di coordinate locale.
    4.  Premere il pulsante **OK**.
5.  Viene creato uno schizzo.
6.  Lo schizzo viene messo in modalità di modifica e si apre la finestra di [Dialogo Sketcher](Sketcher_Dialog.md).
7.  Per terminare la modalità di modifica, vedere <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:16px;"> [Sketcher Esci](Sketcher_LeaveSketch/it.md).



## Note

-   Gli schizzi esistenti possono essere associati a (diversi) oggetti con [Sketcher Mappa schizzo](Sketcher_MapSketch/it.md) o staccati e riorientati con [Sketcher Riposiziona schizzo](Sketcher_ReorientSketch/it.md).





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher NewSketch/it
