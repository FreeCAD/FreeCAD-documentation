---
- GuiCommand:/pl
   Name:Std ProjectUtil
   Name/pl:Std: Narzędzie projektu
   MenuLocation:Przybory → Narzędzia projektu ...
   Workbenches:wszystkie
---

# Std ProjectUtil/pl



## Opis

Za pomocą polecenia **Narzędzie projektu** można wyodrębnić pliki z pliku projektu FreeCAD *(***.FCStd**), który w rzeczywistości jest plikiem \[<https://en.wikipedia.org/wiki/Zip_(file_format)>* ZIP\], i po ręcznej edycji utworzyć z nich nowy plik projektu.

![](images/Project_utility_en.png ) 
*Okno dialogowe Narzędzia projektu*



## Użycie



### Wyodrębnienie projektu 

1.  Wybierz z menu opcję **Przybory → <img src="images/Std_ProjectUtil.svg" width=16px> Narzędzie projektu ...**.
2.  Otworzy się okno dialogowe Narzędzie projektu.
3.  Naciśnij przycisk **...** po prawej stronie **Wyodrębnij projekt → Źródło**.
4.  Wybierz plik ***.FCStd**, który chcesz edytować.
5.  Naciśnij przycisk **...** po prawej stronie **Wyodrębnij projekt → Miejsce docelowe**.
6.  Wybierz folder, do którego ma zostać wyodrębniony plik projektu. Wskazane jest wybranie pustego folderu.
7.  Naciśnij przycisk **Rozpakuj**.
8.  Naciśnij przycisk **Zamknij**, aby zamknąć okno dialogowe.



### Edycja samodzielna 

Ważne jest, aby zdać sobie sprawę, że pliki wewnątrz pliku projektu FreeCAD są ze sobą powiązane. Edycja tylko jednego pliku zazwyczaj prowadzi do błędów. Aby dokonać spójnych edycji w wielu plikach, użyj dobrego edytora kodu, takiego jak [Notepad++](http://notepad-plus-plus.org/) (dla systemu operacyjnego Windows) lub [Notepadqq](https://notepadqq.com/s/) *(dla systemu operacyjnego Linux)*.



### Utwórz projekt 

1.  Wybierz z menu opcję **Przybory → <img src="images/Std_ProjectUtil.svg" width=16px> Narzędzie projektu ...**.
2.  Otworzy się okno dialogowe Narzędzie projektu.
3.  Naciśnij przycisk **...** na prawo od **Utwórz projekt → Źródło**.
4.  Wybierz plik **Document.xml**. Polecenie automatycznie znajdzie wszystkie powiązane pliki.
5.  Naciśnij przycisk **...** po prawej stronie **Utwórz projekt → Miejsce docelowe**.
6.  Wybierz folder, w którym ma zostać utworzony nowy plik projektu.
7.  Naciśnij przycisk **Utwórz**.
8.  W wybranym folderze tworzony jest nowy plik projektu o ustalonej nazwie, **project.fcstd**. Nie ma ostrzeżenia, jeśli plik o tej nazwie już istnieje.
9.  Opcjonalnie zaznacz pole wyboru {{CheckBox|TRUE|Wczytaj plik projektu po utworzeniu}}.
10. Naciśnij przycisk **Zamknij**, aby zamknąć okno dialogowe.



## Uwagi

-   Więcej informacji na temat formatu pliku projektu FreeCAD znajduje się na stronie [Format pliku FCStd](File_Format_FCStd/pl.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ProjectUtil/pl
