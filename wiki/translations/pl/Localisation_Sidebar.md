# Localisation Sidebar/pl
[Lokalizacja](Localisation/pl.md) to proces dostarczania oprogramowania z wielojęzycznym interfejsem użytkownika. Dokumentacja Wiki może być również zlokalizowana, jak opisano w sekcji [Tłumaczenie Wiki FreeCAD](Localisation/pl#Tłumaczenie_dokumentacji_Wiki_dla_FreeCAD.md).

Pasek boczny jest ważnym narzędziem nawigacyjnym w świecie wiki, zobacz [Podręcznik:Interfejs/Sidebar](http://www.mediawiki.org/wiki/Manual:Interface/Sidebar) aby uzyskać więcej informacji.

## Tłumaczenie paska bocznego 

Pasek boczny można teraz przetłumaczyć w pełni za pomocą rozszerzenia [Translation extension](http://www.mediawiki.org/wiki/Help:Extension:Translate), które jest dostępne na wszystkich stronach Wiki.

W Wiki FreeCAD pasek boczny jest implementowany za pomocą szablonów, które zmieniają tekst w zależności od wybranego języka. Szczegóły techniczne jak ta funkcja została zaimplementowana są opisane na forum, w wątku [Wiki navigation/translation](http://forum.freecadweb.org/viewtopic.php?f=21&t=9687&start=10#p80441).

### Wytyczne

Możesz przejść do strony specjalnej [Special:Translate/wiki-sidebar](Special:Translate/wiki-sidebar.md), aby rozpocząć tłumaczenie.

Występuje błąd na stronie pobierania. Nie można przekierować linku do **Download/fr**, lub **Download/de**, itp. Zamiast tego link będzie wskazywał na aktualne tłumaczenie **Download** w Twoim języku. Najlepszym sposobem na poradzenie sobie z tym problemem jest stworzenie nowej strony i przekierowanie jej na właściwą stronę. Więcej na temat przekierowania znajdziesz na stronie [Help:Editing](Help_Editing.md).

### Istotne uwagi 

W większości przypadków na pasku bocznym znajdują się dwa ciągi znaków dla każdej z pozycji.

** {{int:sidebar-faq-target}}|sidebar-faq

Lewy reprezentuje cel łącza, a prawy tekst, który będzie wyświetlany na pasku bocznym.

Możesz zobaczyć różnicę między nimi, patrząc na górną część pola tłumaczenia, gdzie wyświetlana jest nazwa zmiennej. Kiedy nazwa zmiennej kończy się na **-target**, oznacza to, że będziesz tłumaczył link docelowy. Jest on wykonany tak, aby umożliwić tłumaczowi przekierowanie elementów do przetłumaczonych stron, czyli poprzez dodanie kodu językowego na końcu nazwy strony, na przykład **/fr** dla tłumaczenia na język francuski.

Nie dodawaj kodów językowych \"/fr\", \"/de\", \"/es\", \"/ru\", itp., jeśli przetłumaczona strona nie istnieje w tym języku, spowoduje to utracenie linku. W tym przypadku nie należy pisać nic poza nazwą strony, ponieważ w przeciwnym razie przekierowanie zostanie popsute.

![Gdzie patrzeć.](images/Translate-sidebar-instruction.png )



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Wiki](Category_Wiki.md) > Localisation Sidebar/pl
