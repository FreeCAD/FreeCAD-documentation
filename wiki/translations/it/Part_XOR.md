---
 GuiCommand:
   Name: Part_XOR
   Name/it: Part XOR booleano
   MenuLocation: Part , Dividi , XOR booleano
   Workbenches: Part_Workbench/it
   Version: 0.17
   SeeAlso: Part_BooleanFragments/it, Part_Slice/it, Part_CompJoinFeatures/it, Part_Boolean/it
---

# Part XOR/it



## Descrizione

Il comando <img alt="" src=images/Part_XOR.svg  style="width:24px;"> **Part XOR booleano** rimuove la geometria condivisa da un numero pari di oggetti e lascia uno spazio vuoto tra gli oggetti coinvolti. Per due oggetti rappresenta una versione simmetrica di [Part Sottrai](Part_Cut/it.md).

<img alt="" src=images/Part_XOR-01.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Part_XOR-02.png  style="width:300px;"> 
*Tre oggetti sovrapposti → Oggetto risultato*



## Utilizzo

1.  Selezionare due o più oggetti. È anche possibile selezionare un [Part Composto](Part_Compound/it.md) contenente due o più oggetti.
2.  Esistono diversi modi per richiamare il comando:
    -   Selezionare l\'opzione **Parte → Dividi → <img src="images/Part_XOR.svg" width=16px> XOR booleano** dal menu.
    -   Premere il pulsante **<img src="images/Part_XOR.svg" width=16px> [XOR booleano](Part_XOR/it.md)**.



## Note

-   Gli spazi vuoti sono difficili da rilevare se gli oggetti selezionati non hanno facce complanari. Per verificare il risultato XOR è quindi possibile utilizzare [Piano di taglio](Std_ToggleClipPlane/it.md).



## Proprietà



## Script





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part XOR/it
