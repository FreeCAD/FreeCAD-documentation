---
 GuiCommand:
   Name: CAM DressupDogbone
   Name/pl: CAM: Ulepszenie - nadcięcie w narożnikach
   MenuLocation: CAM , Operacje wykańczające ścieżki , Nadcięcie w narożnikach
   Workbenches: CAM_Workbench/pl
   SeeAlso: CAM_DressupTag/pl, CAM_DressupRampEntry/pl, CAM_DressupDragKnife/pl 
---

# CAM DressupDogbone/pl



## Opis

Narzędzie <img alt="" src=images/CAM_DressupDogbone.svg  style="width:24px;"> [Nadcięcie w narożnikach](CAM_DressupDogbone/pl.md) wykańcza istniejącą ścieżkę aby nadciąć narożniki w wewnętrznych kątach operacji profilu lub konturu. Cylindryczny nóż nie może ciąć całkowicie w narożnik o ostrym kącie bez kolizji z modelem. W pewnych przypadkach może być preferowane naruszenie modelu i upewnienie się, że materiał w narożniku jest usuwany. Jest to szczególnie konieczne gdy części będą się przecinać/zakleszczać.



## Użycie

1.  Wybierz obiekty konturu lub ścieżki profilu [CAM](CAM_Workbench/pl.md).
2.  Wybierz opcję **CAM → Operacje wykańczające ścieżki → <img src="images/CAM_DressupDogbone.svg" width=16px> Nadcięcie w narożnikach** z menu.



## Opcje

-   **Side**: Która strona ścieżki będzie modyfikowana.
-   **Style**: Styl nadcięcia (Dogbone, T-Bone Poziomy, T-Bone Pionowy, T-Bone Długa Krawędź, T-Bone Krótka Krawędź).
-   **Incision**: Algorytm używany do obliczania długości nadcięcia.
-   **Custom**: Jeśli nacięcie jest niestandardowe, właściwość niestandardowa jest używana do ustawienia długości.



## Ograniczenia

Nadcięcie w narożnikach wymaga prostego segmentu ścieżki (G1) przed i po narożniku, w którym nadcięcie ma być wstawione.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM DressupDogbone/pl
