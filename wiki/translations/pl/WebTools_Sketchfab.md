---
 GuiCommand:
   Name: WebTools Sketchfab
   Name/pl: Web: Sketchfab
   MenuLocation: WebTools , Sketchfab
|
   Workbenches: WebTools_Workbench/pl
---

# WebTools Sketchfab/pl

## Opis

Narzędzie to umożliwia eksportowanie i przesyłanie obiektów na konto w serwisie [SketchFab](http://www.sketchfab.com). {{Version/pl|0.17}}

![](images/Sketchfab_exporter.jpg )

## Użycie

1.  Załóż konto w serwisie [SketchFab](http://www.sketchfab.com), jeśli jeszcze go nie masz. Darmowe konta są w porządku, płatne konta dodają więcej funkcji, takich jak możliwość posiadania prywatnych modeli i większe maksymalne rozmiary transferu.
2.  Przygotuj model, który chcesz załadować
3.  Kliknij na przycisk <img alt="" src=images/WebTools_Sketchfab.png  style="width:32px;"> z głównego paska narzędzi w Środowisku pracy [Narzędzia Web](WebTools_Workbench/pl.md).
4.  Wypełnij pola. Nazwa i klucz API są obowiązkowe.
5.  Kliknij przycisk **Prześlij**.

## Opcje

-   Potrzebujesz klucza Sketchfab API, aby ten eksporter mógł się połączyć z Twoim kontem Sketchfab. Po naciśnięciu przycisku \"Uzyskaj\" zostaniesz przekierowany na stronę ustawień programu Sketchfab, gdzie podany jest klucz API (który jest unikalny dla Twojego konta). Skopiuj klucz i wklej go w pole \"API key\" eksportera. Wartość ta będzie przechowywana przez FreeCAD, więc musisz to zrobić tylko raz.
-   Pole z nazwą jest obowiązkowe, pozostałe można pozostawić puste.
-   Eksporter proponuje kilka różnych formatów eksportu. To, co najlepsze dla Ciebie, zależy od rodzaju modelu i wyniku, który chcesz uzyskać. Zaleca się przetestowanie, który z nich jest dla Ciebie najlepszy. Ogólnie rzecz biorąc, OBJ + MTL da Ci lepszą kontrolę nad materiałami, podczas gdy IV *(OpenInventor)* da wynik, który jest bardziej podobny do tego, co widzisz w widoku 3D FreeCAD.
-   Po załadowaniu modelu, Sketchfab oferuje dość zaawansowany interfejs, w którym można dalej konfigurować materiały, oświetlenie i środowisko.
-   Po naciśnięciu przycisku **Prześlij**, gdy przesyłanie się zakończy, jeśli wszystko pójdzie dobrze, przycisk zmieni swój opis na **Przeglądaj swój model online**. Po kliknięciu zostaniesz przeniesiony bezpośrednio na stronę modelu w programie Sketchfab.
-   Niektóre formaty, jak OBJ, są różnie interpretowane przez Sketchfab i FreeCAD. FreeCAD uważa, że oś Z jest skierowana ku górze, podczas gdy Sketchfab uważa, że wskazuje osobę znajdującą się za ekranem. Aby temu zaradzić, po zakończeniu ładowania, eksporter użyje API Sketchfab, aby obrócić model do właściwego położenia. Jeśli ta operacja się nie powiedzie, zostaniesz ostrzeżony, ale Twój model nadal będzie poprawnie załadowany. Możesz obrócić go ręcznie w interfejsie Sketchfab, naciskając strzałkę w prawo obok osi **X** w zakładce orientacji modelu.



---
⏵ [documentation index](../README.md) > WebTools Sketchfab/pl
