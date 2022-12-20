---
- GuiCommand:/pl
   Name:Mesh TrimByPlane
   Name/pl:Siatka Przytnij siatkę płaszczyzną
   MenuLocation:Siatki → Cięcie → Przytnij siatkę
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Przetnij siatkę](Mesh_PolyCut/pl.md), [Przytnij siatkę](Mesh_PolyTrim/pl.md)
---

# Mesh TrimByPlane/pl

## Opis

Polecenie **Przytnij siatkę płaszczyzną** wycina z obiektu siatkowego ściany i części ścian po jednej stronie płaszczyzny.

## Użycie

1.  Wybierz pojedynczy obiekt siatki i pojedynczą [Płaszczyznę części](Part_Plane/pl.md). Płaszczyzna *(jej przedłużenie)* powinna przecinać obiekt siatki.

2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Mesh_TrimByPlane.svg" width=16px> '''Przytnij siatkę płaszczyzną'''**.
    -   Wybierz z menu polecenie **Siatki → Cięcie → <img src="images/Mesh_TrimByPlane.svg" width=16px> Przytnij siatkę płaszczyzną**.

3.  Otwiera się okno dialogowe **Przytnij płaszczyzną**.

4.  
    **Wybierz stronę, którą chcesz pozostawić**, naciskając jeden z przycisków:

    -   
        {{button|Poniżej}}
        

    -   
        {{button|Powyżej}}
        

    -   
        {{button|Rozdziel}}
        
        : usuwa ściany i części ścian nad płaszczyzną i tworzy zawierający je nowy obiekt siatki.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh TrimByPlane/pl
