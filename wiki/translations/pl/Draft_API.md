# Draft API/pl
{{VeryImportantMessage
|''(listopad 2018 r.)'' Informacje te mogą być niekompletne i nieaktualne. Najnowsze API - patrz [https://www.freecadweb.org/api dokumentacja API generowana automatycznie].}}

Funkcje te są częścią Środowiska pracy [Draft](Draft_Workbench.md) i mogą być używane w [makrodefinicjach](macros.md) i z konsoli [Python](Python.md) po zaimportowaniu modułu `Draft`.

Przykład: 
```python
import FreeCAD, Draft

myrect = Draft.makeRectangle(4, 3)
mydistance = FreeCAD.Vector(2, 2, 0)
Draft.move(myrect, mydistance)
```


{{APIFunction|cut|FreeCAD.Object, FreeCAD.Object|Zwraca wycięty obiekt wykonany z różnicy dwóch danych obiektów. Oryginalne obiekty zostają ukryte.|Nowo utworzony obiekt.}}


{{APIFunction|extrude|FreeCAD.Object, Vector|Wyciągnie dany obiekt w kierunku podanym przez wektor. Oryginalny obiekt zostaje ukryty.|Nowo utworzony obiekt.}}


{{APIFunction|formatObject|FreeCAD.Object, [FreeCAD.Object]|Funkcja ta stosuje do danego obiektu docelowego bieżące właściwości ustawione na pasku narzędzi szkicu (kolor linii i szerokość linii) lub kopiuje właściwości drugiego obiektu, jeśli jest podany. Umieszcza również obiekt w grupie konstrukcyjnej, jeśli zostanie naciśnięty przycisk konstrukcyjny.|Nic}}


{{APIFunction|fuse|FreeCAD.Object, FreeCAD.Object|Zwraca obiekt wykonany ze złączenia 2 podanych obiektów. Jeśli obiekty są współpłaszczyznowe, używany jest specjalny ścieżka robocza, w przeciwnym razie obiektem końcowym jest standardowy Part fuse.|Nowo utworzony obiekt.}}


{{APIFunction|getDraftPath|[string]|Zwraca ścieżkę dostępu katalogu użytkownika lub systemu, z którego uruchamiany jest moduł Draft. Jeżeli podano podścieżkę lub nazwę pliku, zwracana jest pełna ścieżka do podścieżki wewnątrz modułu Draft.|Ścieżka dostępu do pliku.}}


{{APIFunction|getGroupContents|list|Skanuje cyklicznie podaną listę grup. Jeśli grupy zostały napotkane, ich zawartość jest dołączana do listy.|Lista obiektów ''FreeCAD Objects''.}}


{{APIFunction|getRealName|string|Odcina numery końcowe z nazwy obiektu.|Nazwa ''(skrócona)'' obiektu.}}


{{APIFunction|getSelection| |Zwraca bieżący wybór z FreeCAD.|Bieżący wybór z FreeCAD.}}


{{APIFunction|makeCircle|radius, [placement], [facemode], [startangle], [endangle]|Tworzy obiekt okręgu o zadanym promieniu. Jeśli podano położenie, to jest ono używane. Jeśli tryb ściany ''(Facemode)'' to False, okrąg jest pokazany jako szkielet druciany, w przeciwnym razie jako ściana. Jeśli podano kąt początkowy i końcowy ''(w stopniach)'', są one używane i obiekt pojawia się jako łuk.|Nowo utworzony obiekt.}}


{{APIFunction|makeDimension|Vector, Vector, [Vector] or FreeCAD.Object, int, int, [Vector]|Tworzy obiekt wymiarowy mierzący odległość pomiędzy pierwszym i drugim wektorem, z oznaczeniem linii wymiarowej przez trzeci wektor, jeśli jest dostępny. Zostanie użyta aktualna szerokość i kolor linii z paska narzędzi Draft. Zamiast 2 wektorów, można również przekazać obiekt FreeCAD i dwie liczby całkowite ''(i opcjonalnie wektor, przez który musi przejść linia wymiarowa)''. W takim przypadku wymiar będzie kojarzony z obiektem i będzie mierzył dwa jego wierzchołki, wskazane przez dwa podane numery indeksów.|Nowo utworzony obiekt.}}


{{APIFunction|makeLine|Vector, Vector|Tworzy linię pomiędzy dwoma danymi wektorami. Zostanie użyta aktualna szerokość i kolor linii z paska narzędzi Draft.|Nowo utworzony obiekt.}}


{{APIFunction|makeRectangle|length, width, [placement], [facemode]|Tworzy obiekt prostokąta o długości w kierunku X i wysokości w kierunku Y. Jeśli podano położenie, jest ono używane. Jeśli tryb Facemode to False, prostokąt jest pokazywany jako szkielet, w przeciwnym razie jako ściana. Zostanie użyta aktualna szerokość i kolor linii z paska narzędzi Draft.|Nowo utworzony obiekt.}}


{{APIFunction|makeText|string or list, [Vector], [screenmode]|Tworzy obiekt tekstowy, w danym punkcie, jeśli podano wektor, zawierający ciąg znaków lub ciągi znaków podane w liście, jeden ciąg na linię. Używany jest aktualny kolor z paska narzędzi Draft oraz wysokość tekstu i czcionka określona w preferencjach. Jeśli tryb ekranu ''(screenmode)'' to True, tekst zawsze jest zwrócony w kierunku widoku, w przeciwnym razie leży na płaszczyźnie XY.|Nowo utworzony obiekt.}}


{{APIFunction|makeWire|list or Part.Wire, [closed], [placement], [facemode]|Tworzy obiekt DWire z podanej listy wektorów lub z podanej ścieżki. Jeśli parametr zamknięty ''(closed)'' to True lub jeśli pierwszy i ostatni punkt są w tym samym położeniu, ścieżka jest zamykana. Jeśli tryb facemode to True ''(i ścieżka jest zamknięta)'', ścieżka zostanie wyświetlana jako wypełniona. Zostanie użyta aktualna szerokość i kolor linii z paska narzędzi Draft.|Nowy obiekt Draft DWire ''(nie mylić z Part Wire)''.}}


{{APIFunction|move|FreeCAD.Object or list, Vector, [copymode]|Przesuwa dany obiekt lub obiekty znajdujące się na liście, w kierunku i na odległość wskazaną przez dany wektor. Jeśli kopymode to True, to aktualne obiekty nie są przesuwane, lecz tworzone są ich kopie.|Obiekt(y) ''(lub ich kopie, jeżeli parametr copymode to True)''.}}


{{APIFunction|precision| |Zwraca wartość dokładności z ustawień użytkownika Draft.|Liczba całkowita.}}


{{APIFunction|rotate|FreeCAD.Object or list, angle, [center], [axis] ,[copymode]|Obraca dany obiekt lub obiekty znajdujące się na danej liście o zadany kąt wokół zadanego punktu środkowego, jeśli podano, z użyciem osi obrotu. Jeśli oś jest pominięta, obrót będzie się odbywał wokół pionowej osi Z. Jeśli parametr copymode to True, aktualne obiekty nie są przesuwane, lecz tworzone są ich kopie.|Obiekty (lub ich kopie).}}


{{APIFunction|scale|FreeCAD.Object or list, vector, [center], [copymode]|Skaluje dany obiekt lub obiekty znajdujące się na podanej liście za pomocą współczynników skali zdefiniowanych przez dany wektor ''(w kierunkach X, Y i Z)'' wokół podanego punktu środka, jeśli jest to możliwe. Jeśli tryb Copymode to True, rzeczywiste obiekty nie są przenoszone, ale zamiast tego tworzone są ich kopie.|Obiekty (lub ich kopie).}}


{{APIFunction|select|FreeCAD.Object|Odznacza wszystko i zaznacza tylko przekazywany obiekt.|Nic.}}


{{APIFunction|shapify|FreeCAD.Object|Przekształca obiekt o kształcie parametrycznym w nieparametryczny.|Nowy obiekt.}}


{{APIFunction|draftify|FreeCAD.Object or list|Zamienia dany obiekt lub każdy obiekt z danej listy w parametryczne ścieżki Draft|Nic.}}


{{APIFunction|getSVG|FreeCAD.Object, [linemodifier], [textmodifier], [(u,v)]|Tworzy reprezentację SVG danego obiektu. Atrybut linemodifier to współczynnik skali ''(w procentach)'' dla szerokości linii i modyfikator tekstu dla rozmiaru tekstu. Możesz także opcjonalnie podać zestaw wektorów w celu zdefiniowania płaszczyzny rzutowania, w przeciwnym razie geometria zostanie rzutowana na płaszczyznę XY.|Łańcuch zawierający reprezentację SVG danego obiektu.}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Draft](Draft_Workbench.md) > Draft API/pl
