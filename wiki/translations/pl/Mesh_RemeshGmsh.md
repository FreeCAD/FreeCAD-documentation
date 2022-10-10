---
- GuiCommand   */pl
   Name   *Mesh RemeshGmsh
   Name/pl   *Siatka   * Ulepsz przez Gmsh
   MenuLocation   *Siatki → Ulepszanie ...
   Workbenches   *[Siatka](Mesh_Workbench/pl.md)
   Version   *0.19
   SeeAlso   *[Siatka z kształtu](Mesh_FromPartShape/pl.md)
---

# Mesh RemeshGmsh/pl

## Opis

Polecenie **Ulepsz \...** ponownie przetwarza obiekt siatkowy przy użyciu generatora siatek [Gmsh](https   *//gmsh.info/). Nowa siatka może być drobniejsza lub grubsza.

## Użycie

1.  Wybierz pojedynczy obiekt siatki.
2.  Istnieje kilka sposobów na wywołanie polecenia   *
    -   Naciśnij przycisk **<img src="images/Mesh_RemeshGmsh.svg" width=16px> [Ulepsz ...](Mesh_RemeshGmsh/pl.md)**.
    -   Wybierz opcję z menu **Siatki → <img src="images/Mesh_RemeshGmsh.svg" width=16px> Ulepsz ...**.
3.  Otwiera się panel zadań **Ponów tworzenie siatki przez Gmsh**.
4.  Określ wymagane ustawienia. Zobacz strony [ustawienia Gmsh](Mesh_FromPartShape/pl#Generator_Gmsh.md) oraz [Siatka z kształtu](Mesh_FromPartShape/pl.md).
5.  Naciśnij przycisk **Zastosuj**, aby przebudować obiekt siatkowy.
6.  Opcjonalnie zmień jedno lub więcej ustawień i ponownie naciśnij przycisk **Zastosuj**, aż nowa siatka będzie ci odpowiadać.
7.  Naciśnij przycisk **Zamknij**, aby zamknąć panel zadań i zakończyć polecenie.

## Uwagi

-   W niektórych przypadkach to polecenie spowoduje powstanie siatki z odwróconymi normalnymi. Można to poprawić poleceniem [Odwróć wektory normalne](Mesh_FlipNormals/pl.md).

## Właściwości

Zapoznaj się z informacjami na stronie   * [cecha siatki](Mesh_Feature/pl.md).





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemeshGmsh/pl
