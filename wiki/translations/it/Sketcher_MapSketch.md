---
 GuiCommand:
   Name: Sketcher MapSketch
   Name/it: Sketcher Associa schizzo
   MenuLocation: Schizzo , Associa schizzo...
   Workbenches: Sketcher_Workbench/it, PartDesign_Workbench/it
   SeeAlso: Sketcher_ReorientSketch/it, Sketcher_NewSketch/it
---

# Sketcher MapSketch/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_MapSketch.svg  style="width:24px;"> [Sketcher Associa schizzo](Sketcher_MapSketch/it.md) associa uno schizzo alla geometria selezionata.

I casi d\'uso tipici sono:

-   Lo schizzo è stato creato su un piano standard (XY, XZ o YZ) e lo si desidera collegare alla faccia di un solido per eseguire su di esso una nuova lavorazione.
-   Lo schizzo è stato collegato a una faccia specifica di un solido ma è necessario collegarlo a una faccia diversa.
-   Un modello danneggiato deve essere riparato.

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">



## Utilizzo

1.  Selezionare un oggetto con una forma, o uno o più vertici, bordi e/o facce e/o un piano.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_MapSketch.svg" width=16px> [Associa schizzo...](Sketcher_MapSketch/it.md)**.
    -   Selezionare l\'opzione **Sketch → <img src="images/Sketcher_MapSketch.svg" width=16px> Associa schizzo...** dal menu.
3.  Si apre la finestra di dialogo **Seleziona schizzo**.
4.  Selezionare uno schizzo dall\'elenco a discesa.
5.  Premere il pulsante **OK**.
6.  Si apre la finestra di dialogo **Associa schizzo**.
7.  Selezionare un [metodo di associazione](Part_EditAttachment/it#Attachment_modes.md) dall\'elenco a discesa. Oppure selezionare **Non associare** per staccare lo schizzo.
8.  Premere il pulsante **OK**.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher MapSketch/it
