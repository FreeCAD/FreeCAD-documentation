---
 GuiCommand:
   Name: Std TextDocument
   Name/pl: Std: Dodaj dokument tekstowy
   MenuLocation: Przybory , Dodaj dokument tekstowy
   Workbenches: wszystkie
   Version: 0.19
   SeeAlso: Draft_ShapeString/pl, Draft_Text/pl
---

# Std TextDocument/pl



## Opis

Polecenie **Dodaj dokument testowy** tworzy obiekt zdolny do przechowywania dowolnego tekstu. Element ten może być użyty do zapisania ogólnych informacji lub specyfikacji modelu.



## Użycie

1.  Wybierz z menu opcję **Przybory → Dodaj dokument tekstowy**.
2.  Kliknij dwukrotnie nowo utworzony obiekt w oknie [widoku drzewa](Tree_view/pl.md), aby otworzyć zakładkę, w której będziesz mógł napisać tekst.
3.  Dodaj tekst.
4.  Zamknij zakładkę i zapisz plik, gdy zostaniesz o to poproszony.



## Właściwości



### Widok


{{TitleProperty|Edytor}}

-    **Nazwa czcionki|Font**: nazwa czcionki, na przykład, {{Value|Ubuntu Mono}}.

-    **Rozmiar czcionki|Float**: rozmiar czcionki w punktach, na przykład, {{Value|11}}.

-    **Tylko do odczytu|Bool**: domyślnie ustawia się na wartość {{FALSE/pl}}. Jeśli ustawimy wartość {{TRUE/pl}}, tekst nie może być edytowany.

-    **Podświetlenie składni|Enumeration**: domyślnie ustawiona jest wartość {{Value|Brak}}. Jeśli ustawimy wartość na {{Value|Python}}, tekst będzie podświetlany jak w [konsoli Python](Python_console/pl.md).



## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć na stronie [Część: właściwość](Part_Feature/pl.md).

Obiekt `App::TextDocument` jest tworzony za pomocą metody `addObject()` dokumentu. Gdy obiekt TextDocument istnieje, jego informacje tekstowe są przechowywane w jego atrybucie `Text`. Atrybut ten może być użyty w innych obiektach, na przykład jako ciąg znaków dla funkcji **<img src="images/Draft_ShapeString.svg" width=16px> [Kształt z tekstu](Draft_ShapeString/pl.md)**.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::TextDocument", "Text_document")
obj.Text = "textual information"
App.ActiveDocument.recompute()

obj2 = Draft.makeShapeString(obj.Text, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
App.ActiveDocument.recompute()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std TextDocument/pl
