---
 GuiCommand:
   Name: Std New
   Name/pl: Std: Nowy
   MenuLocation: Plik , Nowy
   Workbenches: Wszystkie
   Shortcut: **Ctrl**+**N**
   SeeAlso: Std_Open/pl, Std_Import/pl
---

# Std New/pl

## Opis

Polecenie **Std Nowy** tworzy nowy pusty dokument i ustawia go jako dokument aktywny.

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_New.svg" width=16px> [Nowy](Std_New/pl.md)**.
    -   Wybierz z menu opcję **Plik → <img src="images/Std_New.svg" width=16px> Nowy**.
    -   Użyj skrótu klawiaturowego: **Ctrl**+**N**.

## Ustawienia

-   Program FreeCAD będzie tworzył nowy dokument przy uruchamianiu, jeśli parametr **Przybory → Edycja parametrów ... → BaseApp → Preferencje → Dokument → CreateNewDoc** jest ustawiony na wartość {{TRUE/pl}}. To ustawienie można również zmienić w [Edytorze ustawień](Preferences_Editor/pl#Dokument.md).
-   Niektóre właściwości dokumentu: nazwiska autorów, nazwę firmy i informacje o licencji, można wstępnie ustawić w programie przez [Edytor ustawień](Preferences_Editor/pl#Dokument.md).

## Właściwości

Większość właściwości można również zmienić w oknie dialogowym polecenia [Informacja o projekcie](Std_ProjectInfo/pl.md).

-    **Komentarz**: Wszelkie uwagi, które mogą mieć zastosowanie.

-    **Firma**: Nazwa firmy. **Możliwość wstępnego ustawienia**.

-    **Utworzony przez**: Imię i nazwisko autora. **Możliwość wstępnego ustawienia**.

-    **Data utworzenia**: Automatyczny datownik. **Nie można edytować**.

-    **Nazwa pliku**: Pełna ścieżka dostępu do pliku. Jeżeli dokument nie został zapisany, wartość jest pusta.. **Nie można edytować**.

-    **Id**: Jeszcze nie wdrożono.

-    **Etykieta**: Nazwa, która będzie wyświetlana w oknie [Widoku drzewa](Tree_view/pl.md). Domyślnie jest to nazwa dokumentu.

-    **Ostatnio zmodyfikowany przez**: Imię i nazwisko autora. **Możliwość wstępnego ustawienia**.

-    **Data ostatniej modyfikacji**: Automatyczny datownik. **Nie można edytować**.

-    **Licencja**: Rodzaj licencji projektu. **Możliwość wstępnego ustawienia**.

-    **URL licencji**: Adres URL licencji. **Możliwość wstępnego ustawienia**.

-    **Pokaż ukryte**: Jeśli parametr ma wartość prawda, elementy, które zostały ukryte w oknie [Widoku drzewa](Tree_view/pl.md), zostaną wyświetlone. Ukrywanie elementów w drzewie może być przydatne podczas pracy nad większymi modelami.

-    **Czubek**: Jeszcze nie wdrożono.

-    **Nazwa czubka**: Jeszcze nie wdrożono.

-    **Katalog przejściowy**: Katalog tymczasowy używany do odzyskiwania danych. **Nie można edytować**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć nowy dokument, należy użyć metody `newDocument([nazwa], [hidden<nowiki>=</nowiki>False])` aplikacji FreeCAD. Nazwa dokumentu musi być unikalna, co jest sprawdzane automatycznie. Jeśli nie zostanie podana żadna nazwa, dokument zostanie nazwany \"Bez tytułu\". Jeśli użyto metody `hidden<nowiki>=</nowiki>True`, nowy dokument nie będzie wyświetlany w GUI i nie pojawi się dla niego żadna zakładka.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'test.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveAs(fnm)

FreeCAD.closeDocument(doc.Name)

doc = FreeCAD.open(fnm)
doc.save()

FreeCAD.closeDocument(doc.Name)
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std New/pl
