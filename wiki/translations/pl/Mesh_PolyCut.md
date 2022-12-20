---
- GuiCommand:/pl
   Name:Mesh PolyCut
   Name/pl:Siatka Przetnij
   MenuLocation:Siatki → Cięcie → Przetnij siatkę
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Przytnij](Mesh_PolyTrim/pl.md), [Przytnij siatkę płaszczyzną](Mesh_TrimByPlane/pl.md)
---

# Mesh PolyCut/pl

## Opis

Polecenie **Przetnij** wycina z obiektów siatkowych całe ściany.

## Użycie

1.  Podczas wykonywania polecenia nie można zmienić [widoku 3D](3D_view/pl.md). Wskazane jest, aby najpierw prawidłowo ustawić widok 3D.
2.  Wybierz jeden lub więcej obiektów siatkowych.
3.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_PolyCut.svg" width=16px> ''Przetnij siatkę''**.
    -   Wybierz z menu opcję **Siatki → Cięcie → <img src="images/Mesh_PolyCut.svg" width=16px> Przetnij siatkę**.
4.  Zdefiniuj wielokąt wybierając punkty w oknie widoku 3D.
5.  Wybierz opcję z menu kontekstowego widoku 3D:
    -   
        **Wewnętrzny**
        
        : usuwa ściany, które są *(częściowo)* wewnątrz wielokąta.

    -   
        **Zewnętrzny**
        
        : usuwa ściany, które znajdują się całkowicie poza wielokątem.

    -   
        **Rozdziel**
        
        : usuwa ściany i części ścian znajdujące się poza wielokątem i tworzy zawierający je nowy obiekt siatki.

    -   
        **Anuluj**
        
        : anuluje polecenie.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh PolyCut/pl
