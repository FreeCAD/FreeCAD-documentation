# LGTM/pl
## Informacje ogólne 




[LGTM](https://www.lgtm.com) to narzędzie do analizy kodu, które może być zintegrowane z wieloma systemami kontroli wersji oprogramowania online i obsługuje kilka różnych języków. Jest to doskonałe narzędzie do sprawdzania jakości kodu, identyfikujące problemy z kodem, które często są pomijane przez inne narzędzia do sprawdzania kodu i lintery.

LGTM doskonale nadaje się jako narzędzie do analizy kodu do opracowywania środowisk pracy FreeCAD Python i innych małych i średnich projektów. Ta strona zawiera przegląd tego, jak rozpocząć korzystanie z LGTM w środowisku pracy FreeCAD przygotowanym w Python.



## Rozpoczęcie pracy 

Rozpoczęcie pracy z LGTM zależy od używanej platformy kontroli wersji online. Dokumentacja LGTM dla [automatycznego przeglądu kodu](https://lgtm.com/help/lgtm/about-automated-code-review) zawiera dobry przegląd tego, jak zintegrować LGTM z projektem dla kilku platform.

Ponadto możliwe jest przeprowadzenie szerokiego zakresu dogłębnych analiz kodu w LGTM, co wykracza poza zakres tego samouczka. Więcej informacji na ten temat można znaleźć w dokumentacji LGTM na stronie [konfigurowanie analizy kodu](https://lgtm.com/help/lgtm/configuring-lgtm-analysis-project).



## Uzyskiwanie rezultatów 

Po skonfigurowaniu LGTM i zapewnieniu dostępu do repozytoriów kodu, analizy są zwykle wykonywane codziennie w repozytorium. Tak więc wypchnięte zmiany nie przyniosą natychmiastowych wyników. Możliwe jest, aby LGTM analizował pull requesty po ich przesłaniu, jak opisano w dokumentacji LGTM.

Przeglądanie wyników wymaga po prostu zalogowania się do pulpitu nawigacyjnego LGTM i wybrania żądanego projektu. Z tego miejsca analizy kodu dostarczą listę problemów *(takich jak błędy, złe praktyki kodowania, bezużyteczny / nieistotny / niewykorzystany kod itp.)* Ponadto LGTM zapewnia ogólne \"oceny\" kodu *(A, B, C, D)* w zależności od liczby problemów w porównaniu z ogólnym rozmiarem projektu.

Prawdopodobnie najbardziej użytecznym, natychmiastowym sposobem zarządzania wynikami analizy kodu jest po prostu odfiltrowanie plików w projekcie, których nie chcesz analizować. Załóżmy, że rozwijasz nowy kod, który jest niekompletny, przechowujesz starszy kod, który jest nieużywany lub masz dużo kodu testowego, który nie wymaga analizy. LGTM zapewnia [klasyfikację plików](https://lgtm.com/help/lgtm/file-classification), łatwy sposób filtrowania tych plików, aby nie zanieczyszczały wyników analizy.

## Tworzenie pliku .lgtm.yml 

Aby włączyć klasyfikację plików, należy najpierw utworzyć plik o nazwie \".lgtm.yml\" w najwyższym katalogu projektu. Następnie w tym pliku dodaj kilka klasyfikacji.

Poniżej znajduje się przykład ze środowiska pracy FreeCAD Trails zakodowanego w Python:


```python
path_classifiers:
  template:
    - freecad/trails/resources
    - freecad/trails/project/commands/command_template.py
    - freecad/trails/init_gui.py
 
  test:
    - freecad/trails/project/commands/spiral_test.py
    - freecad/trails/TestFPO.py
 
  legacy:
    - freecad/trails/corridor/loft
    - freecad/trails/alignment/VerticalAlignment.py
    - freecad/trails/alignment/VerticalCurve.py
    - freecad/trails/alignment/GenerateVerticalAlignment.py
    - freecad/trails/alignment/ImportVerticalCurve.py
    - freecad/trails/corridor/template/TemplateLibrary.py
```

Należy pamiętać, że poziomy wcięć są ważne w LGTM. Nieprawidłowe wcięcie spowoduje nieudaną klasyfikację pliku.

Ponadto niektóre klasyfikacje *(takie jak \"szablon\" i \"test\")* są używane przez LGTM do zapytań i innych komponentów analitycznych. Można również zdefiniować własne tagi, które będą filtrować kod i dostarczać dodatkowych wyników zapytań.



## Istotne odnośniki internetowe 

-   [Ciągła integracja](Continuous_Integration/pl.md)
-   LGTM [FreeCAD wątek dyskusyjny na forum](https://www.forum.freecadweb.org/viewtopic.php?f=10&t=40228)
-   FreeCAD .lgtm.yml file on [GitHub](https://github.com/FreeCAD/FreeCAD/blob/master/lgtm.yml)
-   freecad.trails .lgtm.yml on [GitHub](https://github.com/joelgraff/freecad.trails/blob/dev/.lgtm.yml)



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Testing](Category_Testing.md) > LGTM/pl
