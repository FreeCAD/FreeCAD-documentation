---
- GuiCommand:
   Name: Std Refresh
   Name/pl: Std: Odśwież
   MenuLocation: Edycja -> Odśwież
   Workbenches: wszystkie
   Shortcut: **F5**
---

# Std Refresh/pl



## Opis

Polecenie **Std Odśwież** wykonuje ponowne przeliczenie aktywnego dokumentu. Ikonka polecenia jest nieaktywna, jeśli dokument nie wymaga ponownego obliczenia.



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Std_Refresh.svg" width=16px> [Odśwież](Std_Refresh/pl.md)**.
    -   Wybierz z menu opcję **Edycja → <img src="images/Std_Refresh.svg" width=16px> Odśwież**.
    -   Użyj skrótu klawiaturowego: **F5**.



## Opcje

-   Aby wymusić przeliczenie zaznacz dokument lub jeden lub więcej obiektów w oknie [widoku drzewa](Tree_view/pl.md), wybierz z menu kontekstowego opcję **<img src="images/Std_MarkToRecompute.svg" width=16px> Zaznacz do przeliczenia** i wywołaj polecenie.
-   Dla obiektów, ale nie dla dokumentów, można również wybrać opcję **Przelicz obiekt** z tego samego menu kontekstowego.



## Uwagi

-   Makro, które wymusza ponownie przeliczenie aktywnego dokumentu, można znaleźć na stronie: [Makrodefinicja: Wymuszaj ponowne obliczenia](Macro_ForceRecompute/pl.md).



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby ponownie przeliczyć aktywny dokument, należy użyć metody `recompute` obiektu *document*.


```python
import FreeCAD

doc = FreeCAD.newDocument()
doc.recompute()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Refresh/pl
