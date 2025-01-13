---
 GuiCommand:
   Name: CAM DressupRampEntry
   Name/pl: CAM: Ulepszenie - parkowanie narzędzia
   MenuLocation: CAM , Operacje wykańczające ścieżki , Parkowanie narzędzia
   Workbenches: CAM_Workbench/pl
   SeeAlso: CAM_DressupTag/pl, CAM_DressupDogbone/pl, CAM_DressupDragKnife/pl
---

# CAM DressupRampEntry/pl



## Opis

Narzędzie <img alt="" src=images/CAM_DressupRampEntry.svg  style="width:24px;"> [Parkowanie narzędzia](CAM_DressupRampEntry/pl.md) wykańcza istniejącą ścieżkę aby dodać parkowanie narzędzia.



## Użycie

1.  Wybierz obiekty konturu lub ścieżki profilu.
2.  Wybierz opcję **CAM → Operacje wykańczające ścieżki → <img src="images/CAM_DressupRampEntry.svg" width=16px> RampEntry** z menu.



## Właściwości

-   **Ramp Feed Rate** : Może być bieżącą prędkością posuwu pionowego lub poziomego, albo jakąś inną wartością niestandardową.
-   **Angle** : Kąt rampy względem osi pionowej. Mniejsza wartość sprawia, że rampa jest bardziej stroma.
-   **Method** : Używana do wyboru różnych trybów parkowania:
    -   *RampMethod1*: schodzi w dół pod kątem rampy, a następnie przesuwa się poziomo do punktu docelowego
    -   *RampMethod2*: najpierw przesuwa się poziomo, a potem schodzi w dół pod kątem rampy do punktu docelowego
    -   *RampMethod3*: schodzi w dół zygzakiem
    -   *Helix*: schodzi spiralnie
-   **Dressup Start Depth** : Odległość powyżej poziomu docelowego, gdzie zaczyna się parkowanie
-   **Use Start Depth** : Oznacza, że parkowanie nie rozpoczyna się powyżej poziomu zapasu. Jeśli nie zostanie ustawiona na prawda, pierwsza rampa może być bardziej stroma niż oczekiwano.

<img alt="" src=images/Ramp_method_1.png  style="width:" height="250px;"> <img alt="" src=images/Ramp_method_2.png  style="width:" height="250px;"> <img alt="" src=images/Ramp_method_3.png  style="width:" height="250px;"> 
*Od lewej do prawej: metody rampowania 1, 2 i 3*

<img alt="" src=images/Ramp_method_Helix.png  style="width:" height="250px;"> 
*Metoda rampowania Helisa*





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM DressupRampEntry/pl
