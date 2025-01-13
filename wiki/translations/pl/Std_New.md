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

Zapoznaj się z informacjami na stronie: [Edytor preferencji](Preferences_Editor/pl.md).

-   Domyślnie FreeCAD uruchamia się bez nowego dokumentu. Sprawdź opcję **Edycja → Preferencje ... → Ogólne → Dokument → Utwórz nowy dokument w trakcie uruchamiania**, aby zmienić to zachowanie.
-   Niektóre właściwości dokumentu: nazwa autora, nazwa firmy i informacje o licencji, mogą być wstępnie ustawione: **Edycja → Preferencje ... → Ogólne → Dokument → Prawa autorskie i licencja**.



## Właściwości

Zobacz również: [Edytor właściwości](Property_editor/pl.md).

Większość właściwości można również zmienić w oknie dialogowym polecenia [Informacja o projekcie](Std_ProjectInfo/pl.md).



### Dane


{{TitleProperty|Baza}}

-    **Komentarz|String**: Wszelkie uwagi, które mogą mieć zastosowanie.

-    **Firma|String**: Nazwa firmy. **Możliwość wstępnego ustawienia**.

-    **Utworzony przez|String**: Imię i nazwisko autora. **Możliwość wstępnego ustawienia**.

-    **Data utworzenia|String**: Automatyczny datownik. *(tylko do odczytu)*

-    **Nazwa pliku|String**: Pełna ścieżka dostępu do pliku. Jeżeli dokument nie został zapisany, wartość jest pusta *(tylko do odczytu)*.

-    **Id|String**: Jeszcze nie wdrożono.

-    **Etykieta|String**: Nazwa, która będzie wyświetlana w oknie [Widoku drzewa](Tree_view/pl.md). Zastąpiona nazwą dokumentu po ponownym otwarciu.

-    **Ostatnio zmodyfikowany przez|String**: Imię i nazwisko autora. **Możliwość wstępnego ustawienia**.

-    **Data ostatniej modyfikacji|String**: Automatyczny datownik. *(tylko do odczytu)*

-    **Licencja|String**: Rodzaj licencji projektu. **Możliwość wstępnego ustawienia**.

-    **URL licencji|String**: Adres URL licencji. **Możliwość wstępnego ustawienia**.

-    **Materiał|Map|Ukryte**: Mapa z właściwościami materiału.

-    **Meta|Map|Hidden**: Mapa z dodatkowymi informacjami meta.

-    **Pokaż ukryte|Bool**: Jeśli wartość ta wynosi {{true/pl}}, elementy, które zostały ukryte w [Widoku drzewa](Tree_view/pl.md) i tak zostaną wyświetlone. Ukrywanie elementów w drzewie może być przydatne podczas pracy na większych modelach.

-    **Czubek|Link**: Jeszcze nie zaimplementowane.

-    **Nazwa czubka|String**: Jeszcze nie zaimplementowane.

-    **Katalog przejściowy|String**: Katalog przejściowy używany do odzyskiwania danych *(tylko do odczytu)*.

-    **Uid|UUID|Hidden**: UUID dokumentu (tylko do odczytu).

-    **UkładJednostek|Enumeration**: System jednostek dokumentu. Wartość początkowa zależy od [Domyślny układ jednostek](Preferences_Editor/pl#Ogólne.md). {{Version/pl|1.0}}.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

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





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std New/pl
