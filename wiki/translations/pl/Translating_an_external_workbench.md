# Translating an external workbench/pl
W poniższych uwagach, `" kontekst"` powinien być nazwą twojego dodatku lub środowiska pracy, na przykład, `"MySuperAddon"` lub `"DraftPlus"`, lub cokolwiek innego. Wielkość liter ma tu znaczenie: na przykład `"Context"` to nie to samo co `"context"`. Ten kontekst sprawia, że wszystkie tłumaczenia twojego kodu będą zebrane pod tą samą nazwą, aby tłumacze mogli je łatwiej zidentyfikować. Oznacza to, że będą oni dokładnie wiedzieli, do którego dodatku lub środowiska pracy należy dany ciąg znaków.

**Uwaga**: Oto skrypt all-in-one, który automatyzuje całą procedurę opisaną poniżej *(zalecamy jednak przeczytanie procedury, aby wiedzieć, co skrypt powinien zrobić)*: <https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Przygotowywanie źródeł 

### Informacje ogólne 

-   Dodaj folder `translations/`. Możesz nadać mu inną nazwę, ale tak będzie łatwiej, ponieważ jest on taki sam w całym FreeCAD. W tym folderze umieścisz pliki `.ts` *(pliki tłumaczenia \"źródła\")* i `.qm` *(skompilowane pliki tłumaczenia)*.
-   Należy tłumaczyć tylko tekst, który jest wyświetlany użytkownikowi w interfejsie użytkownika programu FreeCAD. Tekst, wyświetlany w konsoli Python nie powinien być tłumaczony.
-   Tekst, który jest wyświetlany w `FreeCAD.Console`, jest wyświetlany w oknie \"Widok raportu\" i dlatego powinien zostać przetłumaczony. Okno \"Widok raportu\" jest czymś innym niż konsola Python.

### W każdym pliku .py Python 

-   W każdym pliku, w którym trzeba przetłumaczyć tekst, należy zdefiniować funkcję `translate()`. Możesz użyć w pełni kwalifikowanej nazwy z Qt, ale to jest trochę bardziej przejrzyste w użyciu:

:   
    
```python
    import FreeCAD
    translate = FreeCAD.Qt.translate
    
```
    

-   Cały tekst, który musi zostać przetłumaczony, musi zostać przekazany przez funkcję `translate()`:

:   
    
```python
    print("My text")
    
```
    





:   staje się:





:   
    
```python
    print(translate("context", "My text"))
    
```
    





:   Pamiętaj, że `translate()` nie jest zwykłą funkcją: służy również jako \"tag\" dla narzędzia do przetwarzania tekstu `lupdate`, więc musi mieć nazwę dokładnie \"translate\". Program `lupdate` jest prostym procesorem tekstu, nie wykonuje Twojego kodu. Do funkcji `translate()` musisz przekazywać bezpośrednio literały łańcuchowe: nie możesz przekazywać zmiennych, stałych, itp. Na przykład:





:   
    
```python
    # This works:
    FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")

    # This does not, lupdate only sees the word "a_variable", and doesn't know what that is:
    a_variable = "My text"
    FreeCAD.Console.PrintMessage(translate("context", a_variable ) + "\n")

    # But this works -- a_variable will contain the translated string:
    a_variable = translate("context", "My text")
    FreeCAD.Console.PrintMessage(a_variable  + "\n")
    
```
    

Może to być użyte wszędzie: w `print()`, w `FreeCAD.Console.PrintMessage()`, w oknach dialogowych Qt, itd. Funkcje `FreeCAD.Console` nie dodają automatycznie znaku nowej linii *(`\n`)*, więc musi on być dodany na końcu, jeśli jest to pożądane. Ten znak również nie wymaga tłumaczenia, więc może znajdować się poza funkcją tłumaczącą:

:   
    
```python
    FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")
    
```
    

-   Jeśli używasz plików `.ui` wykonanych za pomocą QtDesigner, nie trzeba z nimi robić nic specjalnego.
-   Podczas tworzenia nowych obiektów, nie tłumacz \"Nazwy\" obiektu. Należy raczej tłumaczyć \"Etykietę\" obiektu. Różnica polega na tym, że \"Nazwa\" jest unikalna; pozostaje taka sama przez całe życie obiektu; z drugiej strony, \"Etykieta\" może być zmieniana przez użytkownika wedle życzenia.
-   Kiedy tworzysz właściwości dla swoich obiektów, nie tłumacz nazwy właściwości. Ale umieść opis wewnątrz `QT_TRANSLATE_NOOP`:

:   
    
```python
    obj.addProperty("App::PropertyBool", "MyProperty", "PropertyGroup", QT_TRANSLATE_NOOP("App::Property", "This is what My Property does"))
    
```
    

Nie używaj swojego własnego `"kontekstu"` w tym konkretnym przypadku. Zachowaj `"App::Property"`.

### Wewnątrz InitGui.py 

-   Dodaj następującą linię, na początku pliku:

:   
    
```python
    def QT_TRANSLATE_NOOP(context, text):
        return text
    
```
    

-   Makro `QT_TRANSLATE_NOOP` nie robi nic, ale zaznacza teksty, które później zostaną pobrane przez narzędzie `lupdate`. Ponieważ nie robi ono w zasadzie nic, używamy go tylko w szczególnych przypadkach, gdy FreeCAD sam się wszystkim zajmuje.

-   Aby przetłumaczyć nazwy menu i pasków narzędzi, użyj słowa `"Workbench"` jako kontekstu:

:   
    
```python
    self.appendMenu(QT_TRANSLATE_NOOP("Workbench", "My menu"), [list of commands, ...])
    self.appendToolbar(QT_TRANSLATE_NOOP("Workbench", "My toolbar"), [list of commands, ...])
    
```
    

-   Dodaj ścieżkę do folderu `translations/` w funkcji Initialized:

:   
    
```python
    FreeCADGui.addLanguagePath("/path/to/translations")
    
```
    

Plik `InitGui.py` nie ma atrybutu **plik**, więc nie jest łatwo znaleźć względną lokalizację folderu tłumaczeń. Łatwym sposobem na obejście tego problemu jest zaimportowanie innego pliku z tego samego folderu, a następnie wykonanie w tym pliku polecenia:

:   
    
```python
    FreeCADGui.addLanguagePath(os.path.join(os.path.dirname(__file__), "translations"))
    
```
    

### Wewnątrz każdej klasy poleceń FreeCAD 

-   Dodaj następującą linię, na początku pliku:

:   
    
```python
    def QT_TRANSLATE_NOOP(context, text):
        return text
    
```
    

-   Przetłumacz `'MenuText'` i `'Tooltip'` polecenia w ten sposób:

:   
    
```python
    def GetResources(self):
        return {'Pixmap'  : "path/to/icon.svg"),
                'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
                'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
                'Accel'   : "Shift+A"
        }
    
```
    

gdzie `"CommandName"` jest nazwą polecenia, zdefiniowaną przez:

:   
    
```python
    FreeCADGui.addCommand('CommandName', My_Command_Class())
    
```
    

## Zbierz wszystkie ciągi z twojego modułu 

-   Będziesz potrzebował zainstalowanych w systemie narzędzi `lupdate`, `lconvert`, `lrelease` i `pylupdate`. W dystrybucjach Linuksa są one zwykle dostępne w pakietach o nazwach `pyside-tools` lub `pyside2-tools`. W niektórych systemach `lupdate` nazywa się `lupdate4` lub `lupdate5` lub `lupdate-qt4` lub podobnie. To samo dotyczy innych narzędzi. Możesz użyć wersji Qt4 lub Qt5 według własnego uznania. W Qt6 nie ma oddzielnego systemu tłumaczeń dla plików środowiska Python, `lupdate` jest używany do wyodrębniania łańcuchów ze wszystkich typów plików źródłowych.
-   Jeśli masz pliki `.ui`, musisz najpierw uruchomić `lupdate`:

:   
    
```python
    lupdate *.ui -ts translations/uifiles.ts
    
```
    

To działa rekurencyjnie i znajdzie pliki `.ui` wewnątrz wszystkich twoich katalogów.

-   Jeśli masz pliki `.py`, musisz również uruchomić `pylupdate`:

:   
    
```python
    pylupdate *.py -ts translations/pyfiles.ts
    
```
    

-   Jeśli wykonałeś obie operacje, musisz teraz połączyć te dwa pliki w jeden:

:   
    
```python
    lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
    
```
    

* Sprawdź zawartość trzech plików `.ts`, aby upewnić się, że zawierają one łańcuchy znaków, a następnie możesz usunąć zarówno `pyfiles.ts`, jak i `uifiles.ts`.

-   Możesz to wszystko zrobić w jednym skrypcie bash, tak jak poniżej:

:   
    
```python
    #!/bin/sh
    lupdate *.ui -ts translations/uifiles.ts
    pylupdate *.py -ts translations/pyfiles.ts
    lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
    rm translations/pyfiles.ts
    rm translations/uifiles.ts
    
```
    

## Przesłanie pliku .ts do platformy tłumaczeniowej 

Nadszedł czas, aby zlecić tłumaczenie Twojego pliku `.ts`. Możesz założyć konto na publicznej platformie tłumaczeniowej, takiej jak [Crowdin](https://crowdin.com/) lub [Transifex](https://www.transifex.com/), lub możesz skorzystać z naszego istniejącego [konta FreeCAD-addons na Crowdin](https://crowdin.com/project/freecad-addons), które ma już wielu użytkowników, a zatem jest większa szansa, że Twój plik zostanie przetłumaczony szybko i przez ludzi, którzy znają FreeCAD.

Jeśli chcesz udostępnić swój plik na koncie FreeCAD Crowdin, skontaktuj się z użytkownikiem [Yorik](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68) na forum [FreeCAD](https://forum.freecadweb.org/).


**Uwaga:**

niektóre platformy, takie jak Crowdin, mogą zintegrować się z GitHubem i wykonać wszystkie procesy z punktów 2, 3 i 4 automatycznie. W tym celu nie można korzystać z konta FreeCAD Crowdin. Będziesz musiał założyć własne konto.

## Scalanie tłumaczeń 

Kiedy Twój plik `.ts` został przetłumaczony, choćby częściowo, możesz pobrać tłumaczenia ze strony:

-   Zazwyczaj pobierasz plik `.zip` zawierający jeden plik `.ts` na każdy język.
-   Umieść wszystkie przetłumaczone pliki `.ts`, razem ze swoim podstawowym plikiem `.ts`, w folderze `translations/`.

## Kompilacja tłumaczeń 

Teraz uruchom program `lrelease` dla każdego pliku, który posiadasz:


```python
lrelease "translations/Draft_de.ts"
lrelease "translations/Draft_fr.ts"
lrelease "translations/Draft_pt-BR.ts"
```

Możesz zautomatyzować ten proces:


```python
for f in translations/*_*.ts
do
    lrelease "translations/$f"
done
```

Powinieneś znaleźć jeden plik `.qm` dla każdego przetłumaczonego pliku `.ts`. Pliki `.qm` będą używane przez Qt i FreeCAD w czasie pracy.

To wszystko, czego potrzebujesz. Zauważ, że niektóre części Twojego środowiska pracy nie mogą być tłumaczone w locie, jeśli zdecydujesz się na zmianę języka. Jeśli tak jest, będziesz musiał ponownie uruchomić FreeCAD, aby nowy język został zastosowany.

## Testowanie tłumaczeń 

1.  Przełącz FreeCAD na język, który przetłumaczyłeś *(np. niemiecki)*
2.  Załaduj tłumaczenie do FreeCAD, np. `FreeCADGui.addTranslationPath("/path/to/the/folder/containing/qmfile")`
3.  Przetestuj coś, np. `FreeCAD.Qt.translate("twój kontekst", "jakiś ciąg znaków")`

Wynik: To powinno dać ci niemieckie tłumaczenie. Jeśli to działa dobrze, to znaczy, że podstawowa konfiguracja jest w porządku. Wtedy możemy przyjrzeć się czemuś innemu. Na przykład, nazwy poleceń powinny zawsze używać specjalnego kontekstu, który jest nazwą polecenia zarejestrowanego we FreeCAD.

### Istotne uwagi 

-   Upewnij się, że używasz \*kontekstu\* i \*ciągu znaków\*, które rzeczywiście znajdują się w pliku ts/qm.

## Wygodniejszy skrypt 

Yorik utrzymuje wygodny skrypt dla środowiska pracy BIM, który może zbierać, wysyłać i pobierać pliki ts. Możesz po prostu skopiować i dostosować ten skrypt do swojego środowiska pracy:

<https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Szczegóły techniczne i obsługa zaawansowana 

W powyższych przykładach używane są dwie oddzielne funkcje: `translate()` i `QT_TRANSLATE_NOOP`. Możesz również natknąć się na `tr()` i `QT_TR_NOOP`, które automatycznie podają argument \"kontekst\" na podstawie miejsca wywołania. Te dwie pary funkcji są zasadniczo różne.


`translate()`

i `tr()` wykonują dwa oddzielne zadania: w czasie działania wykonują rzeczywiste tłumaczenie z przekazanego im łańcucha na końcowy przetłumaczony łańcuch. Jest to prawda niezależnie od tego, czy podano im łańcuch literalny, zmienną czy stałą: wyszukiwanie odbywa się dynamicznie i w czasie rzeczywistym podczas wykonywania kodu. Jednakże, zapewniają one dodatkową funkcję nie związaną z czasem rzeczywistym: są rozpoznawane przez narzędzie `pylupdate`. Jeśli (i tylko jeśli) zawierają literał łańcuchowy, to jest on wyodrębniany przez narzędzie. TYLKO literały łańcuchowe są wyodrębniane przez `pylupdate`. \-- jeśli zostanie przekazana zmienna, to jest ona ignorowana przez narzędzie `pylupdate`. Qt będzie próbowało zapewnić tłumaczenie w czasie wykonywania, ale będzie to działać tylko wtedy, gdy jakiś inny fragment kodu wywoła jedną z funkcji tłumaczących z łańcuchem, który ma być przetłumaczony, tak aby `pylupdate` mógł go wydobyć. Zauważ, że kod z łańcuchem literalnym nie musi być w rzeczywistości wykonywany, musi po prostu istnieć jako linia kodu gdzieś w pliku: `pylupdate` nie wykonuje żadnej analizy ani egzekucji kodu, po prostu wykonuje wyszukiwanie i ekstrakcję łańcucha.

W przeciwieństwie do nich, `QT_TRANSLATE_NOOP` i `QT_TR_NOOP` nie robią nic w czasie wykonywania: są dosłownymi \"no-ops\" i są całkowicie ignorowane przez działający kod. Ich jedynym zastosowaniem jest oznaczenie dosłownego łańcucha do ekstrakcji przez `pylupdate`: nigdy nie ma sensu umieszczać zmiennej wewnątrz wywołania jednej z tych funkcji, nie będzie to miało żadnego efektu. Używa się ich w sytuacjach, gdy `translate()` lub `tr()` zostaną wywołane ze zmienną zawierającą tekst do przetłumaczenia. Na przykład, każdy kod, który jest używany do tworzenia poleceń lub właściwości, użyje funkcji typu NOOP wokół tekstu menu poleceń lub etykiety narzędzia, lub docstring właściwości: w czasie działania, gdy FreeCAD wyświetla te elementy użytkownikowi, wywołuje `translate()`: dosłowne ciągi muszą być wyodrębnione przez `pylupdate` w punkcie tworzenia, na przykład:


```python
def GetResources(self):
    return {'Pixmap'  : "path/to/icon.svg",
            'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
            'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
            'Accel'   : "Shift+A"
    }
```

W tym zastosowaniu słownik zwracany przez tę funkcję jest dosłownie w czasie pracy:


```python
{ 
    'Pixmap'  : "path/to/icon.svg",
    'MenuText': "My Command",
    'ToolTip' : "Describes what the command does",
    'Accel'   : "Shift+A"
}
```

Nie ma odniesienia do żadnego typu informacji o tłumaczeniu. Kiedy FreeCAD faktycznie wyświetla te informacje użytkownikowi, pseudokod wygląda następująco:


```python
for command in commands:
    resources = command.GetResources()
    menu_text = translate(resources['MenuText'])
```

W tym przypadku, `lupdate` nie może wydobyć żadnego łańcucha z wywołania `translate()`, ponieważ odwołuje się ono do zmiennej. Zatem `lupdate` ignoruje to wywołanie, ale w czasie wykonywania Qt szuka łańcucha, który został mu przekazany. Tak długo, jak gdzieś w kodzie znajduje się wywołanie jednej z funkcji tłumaczących z pasującym dosłownym łańcuchem (w tym przypadku w funkcji `GetResources()`), to wywołanie tłumaczenia powiedzie się.

Aby sprawdzić, czy wyodrębniane są oczekiwane ciągi znaków, możesz ręcznie uruchomić polecenie `pylupdate`:


```python
pylupdate myfile.py -ts outfile.ts
```

Plik `outfile.ts` będzie zawierał zestaw ciągów znaków, które są przesyłane do CrowdIn w celu przetłumaczenia.

## Ważne odnośniki 

-   Dlaczego warto i jak tłumaczyć funkcje `openCommand()` *([forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=55869))*.

## Powiązane strony 

-   [Zewnętrzne środowiska pracy](External_workbenches/pl.md)
-   [Lokalizacja - tłumaczenie interfejsu i dokumentacji](Localisation/pl.md)
-   Aby uzyskać więcej informacji, złóż zapytanie tutaj [Tłumaczenie zewnętrznych środowisk pracy](https://forum.freecadweb.org/viewtopic.php?f=10&t=36413).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Translating an external workbench/pl
