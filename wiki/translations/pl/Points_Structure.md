---
 GuiCommand:
   Name: Points Structure
   Name/pl: Punkty: Uporządkowana chmura punktów
   MenuLocation: Punkty , Uporządkowana chmura punktów
   Workbenches: Points_Workbench/pl
---

# Points Structure/pl



## Opis

Polecenie **Uporządkowana chmura punktów** tworzy strukturyzowaną chmurę punktów z punktów istniejącej rozproszonej chmury punktów. Strukturyzowana chmura punktów ma tę zaletę, że znacznie łatwiejsza jest teselacja.

Polecenie działa tylko dla chmur punktów, których punkty, patrząc z określonego kierunku, zorganizowane są w regularną siatkę 2D. Takie chmury punktów są zazwyczaj produkowane przez [structured-light 3D scanners](https://en.wikipedia.org/wiki/Structured-light_3D_scanner) i nie posiadają podcięć. W przypadku złożonych obiektów należy połączyć chmury punktów z wielu różnych kierunków widzenia.



## Użycie

1.  Polecenie zakłada, że kierunek widzenia chmury punktów jest równoległy do osi Z globalnego układu współrzędnych. Jeśli tak nie jest: dostosuj odpowiednio obiekt chmury punktów **Umiejscowienie**.
2.  Wybierz obiekt chmury punktów.
3.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Points_Structure.svg" width=16px> '''Uporządkowana chmura punktów'''**.
    -   Wybierz z menu opcję **Punkty → Uporządkowana chmura punktów**.



## Właściwości

Zobacz stronę [Konwertuj na punkty](Points_Convert/pl.md).





{{Points Tools navi

}}



---
⏵ [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Structure/pl
