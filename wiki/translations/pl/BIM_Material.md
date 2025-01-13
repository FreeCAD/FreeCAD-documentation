---
 GuiCommand:
   Name: BIM Material
   Name/pl: Materiał BIM
   MenuLocation: Zarządzaj , Materiał
   Workbenches: BIM_Workbench/pl
---

# BIM Material/pl



## Opis

Pokazuje okno dialogowe **Materiał BIM**. To okno dialogowe pozwala szybko i łatwo przeprowadzić operacje związane z materiałami ze szczególnym skupieniem na wydajnej pracy z wieloma obiektami i wieloma materiałami.

1.  Utwórz nowy [materiał](Arch_SetMaterial/pl.md) lub [materiał wielowarstwowy](Arch_MultiMaterial/pl.md)
2.  Przypisz istniejący materiał lub materiał wielowarstwowy do wskazanych obiektów.

<img alt="" src=images/BIM_materials_screenshot.png  style="width:600px;">



*Menadżer materiałów*



## Użycie

1.  (Opcjonalnie) wybierz jeden lub więcej obiektów.
2.  Wciśnij przycisk **<img src="images/BIM_Material.svg" width=16px> [Materiał](BIM_Material/pl.md)** na pasku narzędzi.

-   Jeśli nie ma żadnego materiału w aktywnym dokumencie, okno menadżera materiałów nie zostanie wyświetlone a utworzony zostanie [nowy materiał](Arch_SetMaterial/pl.md).
-   Jeśli jest przynajmniej jeden materiał lub materiał wielowarstwowy w dokumencie, okno menadżera materiałów zostanie otwarte.



## Narzędzia menadżera materiałów 

Menadżer materiałów pozwala na:

-   **Wyszukiwanie materiałów po nazwie**: Użyj pola wyszukiwania
-   **Przypisywanie materiału do wybranego obiektu/obiektów**: Kliknięcie OK z wybranym materiałem przypisze go do wskazanego obiektu/obiektów
-   **Tworzenie [materiałów](Arch_SetMaterial/pl.md)**: Wciśnij przycisk **Utwórz nowy materiał**
-   **Tworzenie [materiałów wielowarstwowych](Arch_MultiMaterial/pl.md)**: Wciśnij przycisk **Utwórz nowy materiał wielowarstwowy**
-   **Usuwanie materiału**: Wybierz materiał i kliknij na nim prawym przyciskiem myszy a następnie wybierz \"Usuń\"
-   **Usuwanie nieużywanych materiałów**: Wciśnij przycisk **Usuń nieużywane**. Wszystkie materiały, które nie są używane przez żadne obiekty zostaną usunięte
-   **Łączenie zduplikowanych materiałów**: Wciśnij przycisk **Połącz duplikaty**. Łączy materiały z dokładnie takimi samymi nazwami (np. Beton i Beton) lub takimi samymi nazwami z przyrostkiem numerycznym (np. Beton i Beton001)
-   **Zmienianie nazwy materiału**: Kliknij prawym przyciskiem myszy na materiale i wybierz \"Zmień nazwę\"
-   **Duplikowanie materiału**: Kliknij prawym przyciskiem myszy na materiale i wybierz \"Duplikuj\". To utworzy pełną, niezależną kopię wybranego materiału z tymi samymi ustawieniami
-   **Łączenie dwóch materiałów**: Kliknij prawym przyciskiem myszy na materiale i wybierz \"Dołącz do\...\", a następnie wskaż inny materiał. Ten pierwszy zostanie usunięty a wszystkie obiekty, które go używały zostaną przypisane do drugiego





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Material/pl
