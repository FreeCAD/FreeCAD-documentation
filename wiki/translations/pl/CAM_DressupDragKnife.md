---
 GuiCommand:
   Name: CAM DressupDragKnife
   Name/pl: CAM: Ulepszenie - rylec
   MenuLocation: CAM , Operacje wykańczające ścieżki , Rylec
   Workbenches: CAM_Workbench/pl
   SeeAlso: CAM_DressupTag/pl, CAM_DressupRampEntry/pl, CAM_DressupDogbone/pl
---

# CAM DressupDragKnife/pl



## Opis

Narzędzie **<img src="images/CAM_DressupDragKnife.svg" width=24px> [Rylec](CAM_DressupDragKnife/pl.md)** używa krawędzi tnącej zamontowanej na przegubie do cięcia materiałów arkuszowych, takich jak winyl, tektura czy skóra. Punkt tnący nie jest wyrównany z centrum wrzeciona, ale podąża za nim, gdy wrzeciono się porusza. Z powodu tego przesunięcia ścieżka musi zostać zmodyfikowana, aby wydłużyć ją poza punkt końcowy każdego segmentu. Dodatkowo, rylec nie jest zdolny do wykonywania bardzo ciasnych zakrętów. Aby to skompensować, wstawiany jest przegub \'akcja narożna\', który chwilowo unosi ostrze i obraca je na nową pozycję.

To narzędzie wykańcza istniejącą ścieżkę aby dodać akcje narożnikowe i przedłużenia krawędzi do cięcia rylcem.



## Użycie

1.  Wybierz obiekt konturu lub ścieżki profilu.
2.  Wybierz opcję **CAM → Operacje wykańczające ścieżki → <img src="images/CAM_DressupDragKnife.svg" width=16px> Rylec** z menu.



## Opcje

-   **Kąt Filtra** : Określa, jak ostry musi być kąt, zanim zostanie wstawiona akcja narożnikowa.
-   **Przesunięcie** : Wprowadź, o ile punkt ostrza jest przesunięty względem środka wrzeciona.
-   **Wysokość obrotu** : Określa, na jaką wysokość należy podnieść ostrze tnące podczas akcji narożnikowej. Jest to zależne od materiału i powinno być większe dla grubszych materiałów. Idealnie, punkt powinien pozostać lekko w materiale.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM DressupDragKnife/pl
