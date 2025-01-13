---
 GuiCommand:
   Name: Std LinkSelectLinkedFinal
   Name/it: Vai all'oggetto collegato più profondo
   MenuLocation: Visualizza , Navigazione dei collegamenti , Vai all'oggetto collegato più profondo
   Workbenches: All
   Shortcut: **S** **D**
   Version: 0.19
   SeeAlso: Std_LinkSelectLinked/it, Std_LinkSelectAllLinks/it, Std_SelBack/it, Std_SelForward/it
---

# Std LinkSelectLinkedFinal/it



## Descrizione

Il comando **Vai all\'oggetto collegato più profondo** seleziona l\'**Linked Object**, l\'oggetto sorgente, di un oggetto [App Link](App_Link/it.md), un collegamento. Ma se l\'oggetto di origine è anch\'esso un collegamento, viene al suo posto selezionato l\'oggetto collegato. Questo viene ripetuto finché l\'oggetto collegato non è un collegamento. Questo oggetto di origine finale è l\'oggetto collegato più in profondità.



## Utilizzo

1.  Selezionare un collegamento.
2.  Esistono diversi modi per richiamare il comando:
    -   Selezionare l\'opzione **Visualizza → Navigazione dei collegamenti → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> Vai all'oggetto collegato più profondo** dal menu.
    -   Selezionare l\'opzione **Azioni collegamento → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> Vai all'oggetto collegato più profondo** dal menu contestuale [Vista ad albero](Tree_view/it.md).
    -   Usare la scorciatoia da tastiera: **S** quindi **D**.
3.  Viene selezionato l\'oggetto con il collegamento più profondo. Se questo oggetto appartiene a un documento esterno, quel documento viene attivato.
4.  Facoltativamente utilizzare <img alt="" src=images/Std_SelBack.svg  style="width:16px;"> [Indietro](Std_SelBack/it.md) per riselezionare il collegamento.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std LinkSelectLinkedFinal/it
