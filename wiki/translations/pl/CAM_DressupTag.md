---
 GuiCommand:
   Name: CAM DressupTag
   Name/pl: CAM: Ulepszenie - znacznik
   MenuLocation: CAM , Operacje wykańczające dla ścieżki , Znacznik
   Workbenches: CAM_Workbench/pl
   SeeAlso: CAM_DressupRampEntry/pl, CAM_DressupDogbone/pl, CAM_DressupDragKnife/pl
---

# CAM DressupTag/pl



## Opis

Narzędzie <img alt="" src=images/CAM_DressupTag.svg  style="width:24px;"> **Ulepszenie - pola mocujące** koryguje istniejącą ścieżkę *(zazwyczaj ścieżkę skrawania konturu 2D)*, aby pozostawić znaczniki, które utrzymują część w miejscu. Bez nich część *(która nie jest przymocowana do podstawy)* może w sposób niekontrolowany zostać wyrwana z maszyny podczas końcowego skrawania. Znaczniki są przeznaczone do odłamania ręcznie *(lub za pomocą dłuta)*, a następnie spiłowania na płasko w celu wykończenia części.

Objaśnienie działania tego narzędzia jest dostępne w formie wideo pod tym linkiem: <https://www.youtube.com/watch?v=JZ4prlR6sps>



## Użycie

1.  Wybierz kontur lub obiekty ścieżki profilu.
2.  Wybierz opcję **CAM → Operacje wykańczające dla ścieżki → <img src="images/CAM_DressupTag.svg" width=16px> Znacznik** z menu.



## Opcje

-   **Kąt** : Kontroluje kąt zagłębienia i wynurzenia gdy znacznik jest tworzony.
-   **Wysokość** : Kontroluje wysokość szczytu znacznika od spodu cięcia profilu.
-   **Promień** : Promień zaokrąglenia dla znacznika.
-   **Współczynnik segmentacji** : Liczba segmentów do aproksymacji zaokrąglonego znacznika.
-   **Szerokość** : Całkowita szerokość znacznika.

Znaczniki są automatycznie generowane jako równomiernie rozłożone wzdłuż konturu, zaczynając od największej krawędzi. Masz możliwość usunięcia dowolnych z nich lub zmiany ich położenia, tak że pojawiają się na wypukłych częściach zadania, gdzie łatwiej będzie spiłować nadmiarowy materiał.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM DressupTag/pl
