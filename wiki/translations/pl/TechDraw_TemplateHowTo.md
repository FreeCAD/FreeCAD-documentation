# TechDraw TemplateHowTo/pl
{{TutorialInfo/pl
|Topic= Przygotowanie projektu
|Level= początkujący
|Time= 60 minut
|Author=[http://freecadweb.org/wiki/index.php?title=User:wandererfan wandererfan]
|FCVersion=0.17
}}

## Wprowadzenie

Poradnik ten pokazuje jak stworzyć plik [SVG](SVG/pl.md), który może być użyty jako [szablon](TechDraw_Templates/pl.md) tła dla stron Środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md).

W poradniku tym założono, że znasz umiarkowanie dobrze _, jak również FreeCAD i środowisko pracy [Rysunek techniczny](TechDraw_Workbench/pl.md).

Stworzymy prosty szablon dla papieru w rozmiarze US Letter w orientacji poziomej.

Kopia rezultatu tego poradnika jest dostępna w 
```python
$INSTALL_DIR/Mod/TechDraw/Templates/HowToExample.svg
```

Gdzie `$INSTALL_DIR` jest katalogiem, w którym zainstalowano FreeCAD, na przykład 
```python
/usr/share/freecad/Mod/TechDraw/Templates/HowToExample.svg
```

## Tworzenie dokumentu bazowego 

1\. Otwórz nowy dokument w programie Inkscape.

2\. W Właściwościach dokumentów

-   Wybierz rozmiar strony **US Letter** lub **A4** i orientację **landscape**.
-   Ustaw standardowe jednostki na \"mm\", a rozmiar strony na *279,4* i wysokość *215,9*. Dla strony DIN-A4 należy użyć **210** i **297**.

<img alt="" src=images/InkDocProp.png  style="width:800px;"> 
*align=center|Inkscape: dokument z rozmiarem i orientacją strony* 

3\. Użyj edytora XML, aby dodać klauzulę przestrzeni nazw „freecad" do elementu {{incode | <svg>}}.

:   xmlns:freecad="[http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace](http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace)".

Zauważ, że twoje edytowalne teksty będą \"nie\" działały, jeśli używasz **<https://>\...**, nawet jeśli wiki jest obecnie osiągalne przez https. Ponieważ SVG jest formatem czytelnym dla człowieka, możesz także wpisać powyższą linię do pliku za pomocą edytora tekstu. <img alt="" src=images/InkXMLNameSpace.png  style="width:800px;"> 
*align=center|Inkscape: Edytor XML dodaje klauzulę przestrzeni nazw „freecad” do elementu <svg>* 

## Tworzenie szablonu rysunku 

4\. Narysuj ramkę, numery stref, linie środkowe i inną geometrię.

5\. Narysuj pola i linie dla bloku tytułu.

6\. Dodaj i umieść swój tekst, który ma pozostać niezmienny.

7\. Dodaj i umieść tekst, który będzie można edytować.

8\. Masz teraz gotowe dzieło, które powinno wyglądać mniej więcej tak: <img alt="" src=images/InkFinishedArt.png  style="width:800px;"> 
*align=center|Inkscape: wstępny układ szablonu* 

## Tworzenie pól do edycji 

9\. Użyj edytora XML, aby dodać tag `freecad:editable`} do każdego edytowalnego elementu `<text>}.
* Przypisać sensowną nazwę do każdego pola tekstowego, które można edytować.
_

*align=center|Inkscape: Edytor XML dodający właściwość "freecad:editable" do żądanej pozycji <text>.*
{{clear`

==Dopasowanie wielkości SVG==

10. Użyj edytora XML, aby dopasować atrybut `viewBox` do rozmiaru strony, w milimetrach.
* Są to cztery wartości, w formacie `"0 0 width height"`
_

*align=center|Inkscape: Edytor XML dopasowujący pole widzenia do rozmiaru strony w milimetrach*


11. Twój szablon pojawi się teraz znacznie większy niż oczekiwano.
_

*align=center|Inkscape: wstępny układ szablonów przekraczający rozmiar strony.*


12. Musimy go skurczyć.
* **Edycja → Wybierz wszystko we wszystkich warstwach** lub pole wyboru wybierz i zaznacz wszystkie.
* Dostosuj proporcje pola roboczego **W:** i **H:** do rozmiarów twojego dzieła w milimetrach.
* Ustaw go na rozmiar strony pomniejszony o odpowiednie marginesy, na przykład **W: 250**, i **H: 200**.

13. Użyj opcji '''Wyrównaj i Rozmieść''' lub przycisków **X:** i **Y:**, aby umieścić grafikę w obszarze strony, jeśli to konieczne.

14. Twój szablon powinien teraz wyglądać dokładnie tak, jak na ukończonym obrazku powyżej.

==Usuń przekształcenia z SVG==

15. Upewnij się, że wszystkie edytowalne teksty są ''rozgrupowane'' za pomocą klawiszy **Shift** + **Ctrl** + **g**.

16. Zaznacz wszystko na swojej stronie, używając **Edycja → Wybierz wszystko**, a następnie **Edycja → Kopiuj** **Ctrl** + **C**''.

17. Następnie usuń bieżącą warstwę, **Warstwa → Usuń aktualną warstwę**.
: Uwaga: jeśli usunąłeś już warstwę (w Twoim panelu warstw nie ma żadnej listy warstw), ten krok nie jest wymagany. W tym przypadku należy zaznaczyć wszystko **Ctrl**+**A**, wyciąć zaznaczenie **Ctrl**+**X** i wkleić je przy pomocy polecenia w następnym kroku.

18. Następnie wklej, **Edycja → Wklej tutaj**.
: Uwaga: To polecenie zapobiega zapisywaniu pozycji tekstowych w znacznikach transformacji. <u>Ważne jest, aby nie używać standardowej komendy wklejania.</u>

19. Twój szablon powinien teraz wyglądać właściwie i nie powinien zawierać żadnych niepożądanych przekształceń.

20. Zapisz swój szablon. Jeśli używasz Inkscape, zapisz go najlepiej jako '''Plain SVG''', ponieważ FreeCAD może obsługiwać tylko cechy specyfikacji SVG </br>1.1. Zwykły SVG'' usunie wszystkie znaczniki XML specyficzne dla Inkscape'a.

21. Wypróbuj go w programie FreeCAD i środowisku pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) z opcją [wstaw stronę uzywając szablonu](TechDraw_PageTemplate/pl.md).
_

*align=center|FreeCAD: gotowy szablon z polem tekstowym do edycji*


==Uwagi==
Nie używaj warstw w programie Inkscape, dopóki nie opanowałeś tworzenia szablonów bez nich. Warstwy i grupy mogą automatycznie wstawiać niechciane zmiany do Twojego pliku [SVG](SVG/pl.md).

Ostatnim krokiem przed użyciem nowego szablonu jest usunięcie wszelkich zapisów o przekształceniach z kodu SVG. Ponieważ '''spowodują one problemy'''.

Zobacz dyskusję w portalu Stackoverflow na temat [https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files usuwanie zapisów o przekształceniach w plikach SVG].

Jeśli nie widzisz zielonych pól na swoich tekstach do edycji, może być coś nie tak z Twoją skalą dokumentów. Otwórz ponownie swój plik w programie Inkscape i potwierdź, że wartości viewBox i rozmiary są zgodne. 

Jeśli w FreeCAD teksty są przesunięte, może być konieczne usunięcie atrybutów {{Incode|xml:space<nowiki>=</nowiki>"preserve"}} w pliku SVG. Patrz: https://www.forum.freecadweb.org/viewtopic.php?t=50897.

{{Tutorials navi}} {{TechDraw Tools navi}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateHowTo/pl
