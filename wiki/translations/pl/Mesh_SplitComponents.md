---
- GuiCommand:
   Name: Mesh SplitComponents
   Name/pl: Siatka: Rozbij na komponenty
   MenuLocation: Siatki -> Rozbij na komponenty
   Workbenches: Mesh_Workbench/pl
   Version: 0.19
   SeeAlso: Mesh_Merge/pl
---

# Mesh SplitComponents/pl



## Opis

Polecenie **Rozbij na komponenty** dzieli obiekt siatki na jego komponenty. Komponent siatki to kompletna grupa połączonych powierzchni. Dla każdego komponentu tworzony jest nowy nieparametryczny obiekt siatki, [cecha siatki](Mesh_Feature/pl.md). Jeśli oryginalny obiekt siatki zawiera tylko jeden komponent, co zwykle ma miejsce, tworzony jest pojedynczy nowy obiekt siatki, będący faktycznie jego kopią. To polecenie jest odpowiednikiem polecenia [Scal siatkę](Mesh_Merge/pl.md).



## Użycie

1.  Wybierz jeden lub więcej obiektów siatki.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_SplitComponents.svg" width=16px> '''Rozbij na komponenty'''**.
    -   Wybierz z menu opcję **Siatki → <img src="images/Mesh_SplitComponents.svg" width=16px> Rozbij na komponenty**.



## Właściwości

Zapoznaj się z informacjami na stronie: [cecha siatki](Mesh_Feature/pl.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh SplitComponents/pl
