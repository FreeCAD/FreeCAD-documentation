# Selection API/pl

 {{VeryImportantMessage|''(Październik 2019)'' Nie edytuj tych stron. Informacje są niekompletne i nieaktualne. Najnowsze API można znaleźć w [https://www.freecadweb.org/api automatycznie generowana dokumentacja API], lub wygenerować dokumentację samodzielnie, śledząc dokument [Dokumentacja źródłowa](Source_documentation/pl.md).}}

Moduł podrzędny wyboru jest częścią modułu FreeCADGui. Przykład: 
```python
import FreeCADGui
sel = FreeCADGui.Selection.getSelection()
```


{{APIFunction|addSelection|FreeCAD.Object|Dodaje obiekt do zaznaczenia| }}


{{APIFunction|clearSelection|[string]|Czyści wybór podanej nazwy dokumentu. Jeżeli nie podano żadnego dokumentu, to czyszczony jest cały wybór.| }}


{{APIFunction|getSelection|[string]|Zwraca listę wybranych obiektów dokumentu dla podanej nazwy dokumentu. Jeśli nie podano żadnego dokumentu, zwracana jest pełna lista wybranych obiektów.|a list of document objects in the order they were selected.}}


{{APIFunction|getSelectionEx|[string]|Zwraca listę wybranych obiektów dla podanej nazwy dokumentu. Jeśli nie zostanie podany żaden dokument, zwrócony zostanie kompletny wybór. Używane do wyboru obiektów podrzędnych ''(np. niektóre krawędzie ściany)''.|a list of SelectionObjects in the order they were selected}}


{{APIFunction|isSelected|FreeCAD.Object|Sprawdza, czy dany obiekt jest zaznaczony| }}


{{APIFunction|removeSelection|FreeCAD.Object|Usuwa obiekt z zaznaczenia| }}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
