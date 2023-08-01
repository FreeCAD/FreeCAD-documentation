---
- GuiCommand:
   Name:Points Structure
   Name/pl:Punkty: Uporządkowana chmura punktów
   MenuLocation:Punkty - Uporządkowana chmura punktów
   Workbenches:[Punkty](Points_Workbench/pl.md)
---

# Points Structure/pl

## Opis

Polecenie **Uporządkowana chmura punktów** tworzy ustrukturyzowaną chmurę punktów z punktów istniejącej rozproszonej chmury punktów. Ustrukturyzowana chmura punktów ma tę zaletę, że znacznie łatwiejsza jest teselacja.

Polecenie działa tylko dla chmur punktów, których punkty, patrząc z określonego kierunku, zorganizowane są w regularną siatkę 2D. Takie chmury punktów są zazwyczaj produkowane przez [structured-light 3D scanners](https://en.wikipedia.org/wiki/Structured-light_3D_scanner) i nie posiadają podcięć. W przypadku złożonych obiektów należy połączyć chmury punktów z wielu różnych kierunków widzenia.

## Użycie

1.  Polecenie zakłada, że kierunek widzenia chmury punktów jest równoległy do osi Z globalnego układu współrzędnych. Jeśli tak nie jest: dostosuj odpowiednio obiekt chmury punktów **Umiejscowienie**.
2.  Wybierz obiekt chmury punktów.
3.  Wybierz z menu opcję **Punkty → Uporządkowana chmura punktów**.

## Właściwości

Zobacz stronę [Konwertuj na punkty](Points_Convert/pl.md).





{{Points Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Structure/pl
