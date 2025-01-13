---
 GuiCommand:
   Name: FEM PostFilterLinearizedStresses
   Name/pl: Wykres linearyzacji naprężeń
   MenuLocation: Wyniki , Wykres linearyzacji naprężeń
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_PostPipelineFromResult/pl, FEM_PostFilterDataAlongLine/pl, FEM_tutorial/pl
---

# FEM PostFilterLinearizedStresses/pl



## Opis

Tworzy wykres linearyzacji naprężeń.

Więcej informacji na temat linearyzacji naprężeń można uzyskać na stronie opisującej [linearyzację naprężeń](https://www.graspengineering.com/what-is-stress-linearization/).

<img alt="" src=images/FEM_Stress-Linearization-Plot-Example.png  style="width:500px;">

*Wykres linearyzacji naprężeń.*



## Użycie

1.  Zaznacz wcześniej utworzony [filtr przycięcia linią](FEM_PostFilterDataAlongLine/pl.md) z wykreśloną jedną z następujących wielkości naprężenia:
    -   Mises,

    -   Tresca,

    -   Major principal *(maksymalne naprężenie główne)*,

    -   Intermediate principal *(pośrednie naprężenie główne)*,

    -   
        <small>(v1.0)</small> 
        
        : Naprężenie xx komponentu,

    -   
        <small>(v1.0)</small> 
        
        : Naprężenie xy komponentu,

    -   
        <small>(v1.0)</small> 
        
        : Naprężenie xz komponentu,

    -   
        <small>(v1.0)</small> 
        
        : Naprężenie yy komponentu,

    -   
        <small>(v1.0)</small> 
        
        : Naprężenie yz komponentu,

    -   
        <small>(v1.0)</small> 
        
        : Naprężenie zz komponentu.

    -   Minor principal (minimalne naprężenie główne).
2.  Uruchom narzędzie poprzez:
    -   Wciśnięcie przycisku **<img src="images/FEM_PostFilterLinearizedStresses.svg" width=16px> '''Wykres linearyzacji naprężeń'''**.
    -   Wybranie opcji **Wyniki → <img src="images/FEM_PostFilterLinearizedStresses.svg" width=16px> Wykres linearyzacji naprężeń**.
3.  Wykres XY ze zlinearyzowanymi wartościami naprężeń *(membranowe, membranowe+gnące i całkowite)* wzdłuż linii zostanie utworzony w osobnym oknie.

Wielkość naprężenia wykreślona w filtrze przycięcia linią zostanie użyta do obliczenia naprężeń zlinearyzowanych.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterLinearizedStresses/pl
