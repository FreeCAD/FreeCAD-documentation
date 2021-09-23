# FreeCADGui API/pl
 **''(Październik 2019)'' Nie edytuj tych stron. Informacje są niekompletne i nieaktualne. Najnowsze API można znaleźć w [https://www.freecadweb.org/api automatycznie generowana dokumentacja API], lub wygenerować dokumentację samodzielnie, śledząc dokument [Dokumentacja źródłowa](Source_documentation/pl.md).**

Moduł ten jest odpowiednikiem modułu FreeCAD. Zawiera wszystko co jest związane z interfejsem użytkownika i widokami 3D. Przykład: 
```python
import FreeCAD as App
import FreeCADGui as Gui

# get the 3D model document
doc = App.ActiveDocument    

# get the visual representation model document
gui_doc = Gui.ActiveDocument

gui_doc.activateWorkbench("myWorkbench")
```


{{APIFunction|activateWorkbench|string|aktywuje stanowisko pracy według nazwy|nothing}}


{{APIFunction|activeDocument| | |aktywny dokument lub Brak, jeśli nie istnieje}}


{{APIFunction|activeWorkbench| | |aktywny obiekt środowiska pracy}}


{{APIFunction|addCommand|string, object|dodaje polecenie FreeCAD. String jest nazwą polecenia, a object jest nazwą klasy definiującej polecenie.| }}


{{APIFunction|addIcon|string, string or list|dodaje do systemu ikonę w postaci nazwy pliku lub w formacie XPM| }}


{{APIFunction|addIconPath|string|dodaje nową ścieżkę do systemu, gdzie mają znajdować się pliki ikon| }}


{{APIFunction|addPreferencePage|string,string|dodaje formularz UI do okna dialogowego preferencji. Pierwszy argument określa nazwę pliku, a drugi nazwę grupy.| }}


{{APIFunction|addWorkbench|string, object|dodaje środowisko pracy pod określoną nazwą. String jest nazwą środowisko pracy, a object jest nazwą klasy definiującej to środowisko pracy.| }}


{{APIFunction|createDialog|string|otwiera plik UI| }}


{{APIFunction|getDocument|string|pobiera dokument według jego nazwy|the document}}


{{APIFunction|getWorkbench|string|pobiera środowisko pracy według jego nazwy|the workbench}}


{{APIFunction|insert|string|otwiera plik makrodefinicji, Inventor lub VRML|the document}}


{{APIFunction|listWorkbenches| |wyświetla listę wszystkich środowisk pracy|a list}}


{{APIFunction|open|string|otwiera plik makrodefinicji, Inventor lub VRML|the openend document}}


{{APIFunction|removeWorkbench|string|usuwa środowisko pracy według nazwy| }}


{{APIFunction|runCommand|string|uruchamia polecenie FreeCAD według nazwy| }}


{{APIFunction|updateGui| |aktualizuje okno główne i wszystkie jego okna| }}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
