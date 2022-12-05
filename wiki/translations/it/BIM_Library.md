---
- GuiCommand:Addon/it
   Name:BIM_Library
   Name/it:Libreria BIM
   MenuLocation:Modellazione 3D → Libreria
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/it.md)
   Addon:BIM
   SeeAlso:[Arredo](Arch_Equipment/it.md)
---

# BIM Library/it

## Descrizione

Lo strumento Libreria BIM consente di posizionare nel modello corrente un oggetto della [Libreria di parti di FreeCAD](Parts_Library/it.md), che deve essere installata tramite <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md) per essere disponibile con questo strumento.

<img alt="" src=images/BIM_Library_screenshot.png  style="width:800px;"> 
*Sopra: vista della finestra di dialogo '''Browser della libreria''' nel [pannello delle azioni](Task_panel/it.md) a sinistra*

## Utilizzo

1.  Premere il pulsante **<img src="images/BIM_Library.png" width=16px> '''Libreria BIM'''
**

    :   Risultato: nella [vista combinata](Combo_view/it.md) → [pannello delle azioni](Task_panel/it.md) viene visualizzata una finestra di dialogo denominata **Browser della libreria**
2.  Fare clic su un file del Browser della libreria
3.  Fare doppio clic su di esso o premere il pulsante **Inserisci**
4.  Fare clic su un punto nella [vista 3D](3D_view/it.md) o inserire manualmente una coordinata per posizionare l\'oggetto

## Opzioni

-   Sono supportati i file [FCStd](FCStd/it.md), [STEP](STEP/it.md) e [BREP](BREP/it.md). Solo i file STEP e BREP sono posizionabili. I file FCStd non permettono di scegliere un posizionamento, in quanto potrebbero essere composti da una serie complessa di oggetti con posizioni significative. Quando si sceglie un file FCStd, il suo contenuto viene inserito nella posizione definita nel file.
-   Gli oggetti STEP e BREP sono inseriti come <img alt="Arch Equipment" src=images/Arch_Equipment.svg  style="width:24px;"> [Arredi](Arch_Equipment/it.md) senza una forma di base separata. Aggiungendo successivamente una forma base a questi oggetti si distrugge la loro forma corrente.
-   Posizionando un oggetto, si può scegliere il loro punto di inserimento tra l\'originale (il punto (`0,0,0`) definito nel file), in alto, in mezzo, in basso, a sinistra, al centro o a destra.
-   La ibreria può funzionare offline, nel qual caso si basa sull\'addon della Libreria delle parti da installare (e aggiornare dall\'utente), oppure online, nel qual caso naviga direttamente da [Parts Library Git repository](https://github.com/FreeCAD/FreeCAD-library) e permette di scaricare direttamente da lì.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > BIM Library/it
