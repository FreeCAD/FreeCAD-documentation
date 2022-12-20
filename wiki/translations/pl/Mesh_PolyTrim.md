---
- GuiCommand:/pl
   Name:Mesh PolyTrim
   Name/pl:Siatka Przytnij
   MenuLocation:Siatki → Cięcie → Przytnij siatkę
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Przetnij](Mesh_PolyCut/pl.md), [Przytnij siatkę płaszczyzną](Mesh_TrimByPlane/pl.md)
---

# Mesh PolyTrim/pl

## Opis

Polecenie **Przytnij siatkę** przycina ściany i części ścian z obiektów siatkowych.

## Użycie

1.  Podczas wykonywania polecenia nie można zmienić [widoku 3D](3D_view.md). Wskazane jest, aby najpierw prawidłowo ustawić widok 3D.
2.  Wybierz jeden lub więcej obiektów siatkowych.
3.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_PolyTrim.svg" width=16px> '''Przytnij siatkę'''**.
    -   Wybierz z menu opcję **Siatki → Cięcie → <img src="images/Mesh_PolyTrim.svg" width=16px> Przytnij siatkę**.
4.  Zdefiniuj wielokąt wybierając punkty w oknie widoku 3D.
5.  Wybierz opcję z menu kontekstowego widoku 3D:
    -   
        **Wewnętrzny**
        
        : usuwa ściany i części ścian znajdujące się wewnątrz wielokąta.

    -   
        **Zewnętrzny**
        
        : usuwa ściany i części ścian, które znajdują się poza wielokątem.

    -   
        **Rozdziel**
        
        : usuwa ściany i części ścian znajdujące się poza wielokątem i tworzy zawierający je nowy obiekt siatki.

    -   
        **Anuluj**
        
        : anuluje polecenie.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh PolyTrim/pl
