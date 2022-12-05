---
- GuiCommand:/pl
   Name:Mesh HarmonizeNormals
   Name/pl:Siatka: Porządkuj wektory normalnych
   MenuLocation:Siatka → Porządkuj wektory normalnych
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Odwróć wektory normalnych](Mesh_FlipNormals/pl.md)
---

# Mesh HarmonizeNormals/pl

## Opis

Polecenie **Porządkuj wektory normalne** ujednolica normalne obiektów siatkowych.

## Użycie

1.  Wybierz jeden lub więcej obiektów siatki.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_HarmonizeNormals.svg" width=16px> [Porządkuj wektory normalnych](Mesh_HarmonizeNormals/pl.md)**.
    -   Wybierz z menu opcję **Siatki → <img src="images/Mesh_HarmonizeNormals.svg" width=16px> Porządkuj wektory normalnych**.

## Uwagi

-   To polecenie może spowodować powstanie siatki z odwróconymi normalnymi. Polecenie [Odwróć wektory normalnych](Mesh_FlipNormals/pl.md) może być użyte do poprawy tego stanu rzeczy.
-   Dla wyraźnego wskazania orientacji powierzchni obiektów siatkowych upewnij się, że właściwość **Lighting** obiektów siatkowych jest ustawiona na wartość {{Value|One side}}. Kolor tylnej strony ich ścian będzie wtedy zależał od ustawień podświetlenia: **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Kolor podświetlenia - Intensywność**. Zobacz informacje na stronie: [Edytor ustawień](Preferences_Editor/pl#Widok_3D.md).





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh HarmonizeNormals/pl
