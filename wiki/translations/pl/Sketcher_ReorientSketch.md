---
 GuiCommand:
   Name: Sketcher ReorientSketch
   Name/pl: Szkicownik: Zmień orientację szkicu
   MenuLocation: Szkic , Zmień orientację szkicu ...
   Workbenches: Sketcher_Workbench/pl, PartDesign_Workbench/pl
   SeeAlso: Sketcher_MapSketch/pl, Sketcher_NewSketch/pl
---

# Sketcher ReorientSketch/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:24px;"> **Zmień orientację szkicu** umieszcza szkic na jednej z głównych płaszczyzn z opcjonalnym przesunięciem. Może być również użyte do odłączenia szkicu.



## Użycie

Wybierz szkic. Istnieje kilka sposobów na uruchomienie narzędzia:

-   Naciśnij przycisk **<img src="images/Sketcher_ReorientSketch.svg" width=16px> '''Zmień orientację szkicu''** *(niedostępny w środowisku [Projekt Części](PartDesign_Workbench/pl.md))*.
-   Wybierz opcję **Szkic → <img src="images/Sketcher_ReorientSketch.svg" width=16px> Zmień orientację szkicu** z menu.

Jeśli szkic jest dołączony:

-   Otwiera się okno dialogowe **Podparcie szkicu**.
-   Naciśnij przycisk **Tak**, aby odłączyć szkic.

Otwiera się okno dialogowe **Wybierz orientację**. Opcjonalnie naciśnij przycisk **Anuluj**, aby jedynie odłączyć szkic i zakończyć narzędzie. Określ płaszczyznę orientacji. Płaszczyzna jest względna do lokalnego układu współrzędnych, w którym znajduje się szkic:

-   Jeśli pole wyboru **Odwróć kierunek** nie jest zaznaczone:

 * Góra: **Płaszczyzna XY**
 * Przód: **Płaszczyzna XZ**
 * Prawo: **Płaszczyzna YZ**

-   Jeśli pole wyboru **Odwróć kierunek** jest zaznaczone:

 * Dół: **Płaszczyzna XY**
 * Tył: **Płaszczyzna XZ**
 * Lewo: **Płaszczyzna YZ**

Opcjonalnie zmień **Przesunięcie**. Przesunięcie jest mierzone wzdłuż osi Z, Y lub X lokalnego układu współrzędnych. Naciśnij przycisk **OK**.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ReorientSketch/pl
