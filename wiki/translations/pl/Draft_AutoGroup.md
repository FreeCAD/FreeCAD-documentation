---
 GuiCommand:
   Name: Draft AutoGroup
   Name/pl: Rysunek Roboczy: Grupowanie automatyczne
   Empty: 1
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Version: 0.17
   SeeAlso: Draft_Layer/pl, Std_Group/pl
---

# Draft AutoGroup/pl



## Opis

Polecenie **Grupowanie automatyczne** zmienia aktywną [warstwę](Draft_Layer/pl.md) lub, [opcjonalnie](#Ustawienia.md), aktywną [grupę](Std_Group/pl.md) lub podobny do grupy obiekt [architektury](Arch_Workbench/pl.md). Nowe obiekty [Rysunku roboczego](Draft_Workbench/pl.md) i [Architrktury](Arch_Workbench/pl.md) są automatycznie umieszczane w tej aktywnej warstwie lub grupie.

Polecenie to było pierwotnie przeznaczone dla grup, stąd jego nazwa, ale zostało przeprojektowane w wersji FreeCAD 0.19, kiedy wprowadzono system warstw. Ponieważ obsługa warstw jest teraz domyślna dla polecenia, pozostała część tej strony skupi się głównie na warstwach.

![](images/Draft_tray_menu.png ) 
*Menu warstw w tacce narzędziowej.*



## Użycie

1.  Opcjonalnie wybierz warstwę, którą chcesz aktywować w [widoku drzewa](Tree_view/pl.md).
2.  Polecenie można wywołać na kilka sposobów:
    -   Nacisnąć przycisk w ![](images/Draft_tray_button_layer.png ) [tacce narzędziowej](Draft_Tray/pl.md). Przycisk ten może wyglądać inaczej. Jeśli jest aktywna warstwa, wyświetli jej nazwę i ikonę z **kolorem linii** i **kolorem kształtu** warstwy.
    -   Jeśli zaznaczyłeś warstwę: wybierz opcję **<img src="images/button_right.svg" width=16px> Aktywuj tę warstwę** z menu kontekstowego [Widok drzewa](Tree_view/pl.md).
3.  Jeśli warstwa nie została jeszcze wybrana, otworzy się menu warstw. Wykonaj jedną z następujących czynności:
    -   Wybierz **Brak**, aby pracować bez aktywnej warstwy.
    -   Wybierz istniejącą warstwę do uaktywnienia.
    -   Wybierz **Dodaj nową warstwę**, aby utworzyć nową warstwę. Wybranie tej opcji nie spowoduje zmiany aktywnej warstwy.
4.  Jeśli aktywna warstwa została zmieniona, przycisk w [tacce narzędziowej](Draft_Tray/pl.md) zostanie zaktualizowany.



## Uwagi

-   Nową [warstwę](Draft_Layer.md) można również utworzyć, klikając prawym przyciskiem myszy kontener warstwy w [widoku drzewa](Tree_view/pl.md) i wybierając opcję **<img src="images/Draft_NewLayer.svg" width=16px> Dodaj nową warstwę** z menu kontekstowego.
-   Jeśli [tryb konstrukcyjny](Draft_ToggleConstructionMode/pl.md) jest włączony, aktywna [warstwa](Draft_Layer/pl.md) jest ignorowana.



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md).

-   To polecenie może opcjonalnie obsługiwać również grupy: **Edycja → Preferencje ... → Rysunek Roboczy → Ogólne → Dołącz grupy do listy warstw**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Jeśli środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) jest aktywne, obiekt aplikacji FreeCADGui posiada właściwość `draftToolBar`. Obiekt `draftToolBar` posiada właściwość `autogroup`, która zawiera nazwę aktywnej grupy automatycznej lub `Brak`, jeśli żadna grupa nie jest aktywna. Aby zmienić aktywną grupę automatyczną, użyj metody `setAutoGroup` obiektu `draftToolBar`. Aby umieścić obiekty w aktywnej grupę automatyczną, użyj metody `autogroup` modułu Draft.


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

layer = Draft.make_layer()
Gui.draftToolBar.setAutoGroup(layer.Name)

Draft.autogroup(polygon1)
Draft.autogroup(polygon2)
Draft.autogroup(polygon3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AutoGroup/pl
