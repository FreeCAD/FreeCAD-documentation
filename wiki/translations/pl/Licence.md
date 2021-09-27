# Licence/pl
{{TOCright}}

## Licencje używane w programie FreeCAD 

FreeCAD wykorzystuje dwie różne licencje, jedną dla samej aplikacji, a drugą dla dokumentacji:

**_**. Dla całego kodu źródłowego FreeCAD znajdującego się w [oficjalnym repozytorium Git](https://github.com/FreeCAD/FreeCAD).

**[Creative Commons Attribution 3.0 License *(CC-BY-3.0)*](http://creativecommons.org/licenses/by/3.0/)**. Dla dokumentacji dotyczącej <https://www.freecadweb.org>

Więcej informacji na temat licencji używanych przez różne komponenty open-source używane przez FreeCAD można znaleźć w [pliku z prawami autorskimi debiana](https://github.com/FreeCAD/FreeCAD/blob/master/package/debian/copyright).

## Znaczenie licencji 

Poniżej znajduje się bardziej przyjazne wyjaśnienie, co oznacza dla Ciebie licencja LGPL:

#### Wszyscy użytkownicy 

Każdy może pobrać, używać i redystrybuować FreeCAD bezpłatnie, bez żadnych ograniczeń. Twoja kopia FreeCAD jest naprawdę twoja, podobnie jak pliki, które tworzysz w programie. Nie będziesz zmuszany do aktualizacji FreeCAD po pewnym czasie, ani do zmiany sposobu korzystania z niego. Korzystanie z programu FreeCAD nie wiąże się z żadną umową ani zobowiązaniem. Kod źródłowy FreeCAD jest publiczny i może być sprawdzany, więc możliwe jest sprawdzenie, czy nie robi on rczegoś bez Twojej wiedzy, np. wysyłając gdzieś Twoje prywatne dane.

#### Użytkownicy profesjonalni 

FreeCAD może być swobodnie wykorzystywany do wszelkiego rodzaju celów, prywatnych, komercyjnych lub instytucjonalnych. Każda wersja programu FreeCAD może być wdrożona i zainstalowana gdziekolwiek, dowolną ilość razy. Możesz również modyfikować i dostosowywać FreeCAD do swoich własnych celów bez żadnych ograniczeń. Jednakże, nie możesz uczynić deweloperów FreeCAD odpowiedzialnymi za ewentualne szkody lub straty biznesowe, które mogą wyniknąć z używania programu FreeCAD.

#### Twórcy wolnego oprogramowania (otwarto źródłowego) 

Możesz użyć FreeCAD jako bazy do stworzenia własnej aplikacji, lub po prostu rozszerzyć ją poprzez stworzenie dla niej nowych modułów. Jeśli FreeCAD jest wbudowany we własną aplikację, możesz wybrać albo licencję GPL albo LGPL, lub dowolną inną licencję, która jest kompatybilna z LGPL, aby pozwolić na użycie twojej pracy w prawnie zastrzeżonym oprogramowaniu lub nie. Jeśli rozwijasz moduł, który ma być używany jako rozszerzenie, a nie zawierasz w nim żadnego kodu FreeCAD, możesz wybrać dowolną licencję. Jednakże, jeśli chcesz, by twój moduł był używany w jak największym stopniu, dobrym pomysłem jest użycie tej samej licencji LGPL co w samym FreeCAD, dzięki czemu części twojego kodu mogą być łatwiej ponownie użyte w innych przyszłych modułach lub nawet w samym programie FreeCAD.

#### Twórcy oprogramowania o kodzie źródłowym zamkniętym 

Możesz użyć FreeCAD jako bazy dla własnej aplikacji i nie jesteś zmuszony do uczynienia swojej aplikacji open source. Licencja LGPL wymaga jednak dwóch podstawowych rzeczy: 1) abyś wyraźnie poinformował swoich użytkowników, że twoja aplikacja korzysta z FreeCAD i że FreeCAD posiada licencję LGPL, oraz 2) abyś wyraźnie oddzielił swoją własną aplikację od komponentów FreeCAD. Zazwyczaj odbywa się to poprzez dynamiczne łączenie się z komponentami FreeCAD, dzięki czemu użytkownicy mogą je zmieniać, lub udostępnienie kodu źródłowego FreeCAD wraz z modyfikacjami, które do niego wprowadziłeś. Otrzymasz wsparcie od deweloperów FreeCADa tak długo, jak długo nie jest to droga w jedną stronę.

#### Pliki

Modele i inne pliki wyprodukowane za pomocą FreeCAD nie są objęte żadną z wyżej wymienionych licencji, ani nie są związane żadnymi ograniczeniami czy własnością. Twoje pliki są naprawdę Twoje. Możesz ustawić właściciela pliku i określić własne warunki licencyjne dla produkowanych przez siebie plików w programie FreeCAD, poprzez menu Plik → Informacja o projekcie.

## Oświadczenie głównego dewelopera 

Wiem, że dyskusja na temat „właściwej" licencji na oprogramowanie typu open source zajęła znaczną część przepustowości Internetu, dlatego też tutaj, moim zdaniem, FreeCAD powinien ją mieć.

Wybrałem [LGPL](http://en.wikipedia.org/wiki/LGPL) dla projektu i znam zalety i wady dotyczące **LGPL** i podam kilka powodów tej decyzji.

FreeCAD jest mieszanką Bibliotek i aplikacji, więc GPL byłaby do tego trochę mocna. Zapobiegłaby ona pisaniu komercyjnych modułów dla FreeCAD, ponieważ uniemożliwiałaby łączenie się z bazowymi libs FreeCAD. Możesz zapytać dlaczego w ogóle komercyjne moduły? Dlatego Linux jest dobrym przykładem. Czy Linux byłby tak udany, gdyby Biblioteka GNU C była oparta na licencji GPL i tym samym uniemożliwiała łączenie się z aplikacjami, które nie są oparte na licencji GPL? I chociaż kocham wolność Linuksa, chcę także móc korzystać z bardzo dobrego sterownika graficznego NVIDIA 3D. Rozumiem i akceptuję powód, dla którego NVIDIA nie chce oddać kodu sterownika. Wszyscy pracujemy dla firm i potrzebujemy płatności lub przynajmniej jedzenia. Tak więc dla mnie współistnienie oprogramowania open source i oprogramowania zamkniętego nie jest czymś złym, kiedy przestrzega się zasad LGPL. Chciałbym, żeby ktoś napisał procesor do importu/eksportu Catia dla FreeCAD i rozprowadzał go za darmo lub za jakieś pieniądze. Nie lubię go zmuszać do oddawania więcej niż chce. To nie byłoby dobre ani dla niego, ani dla programu FreeCAD.

Niemniej jednak decyzja ta jest podejmowana tylko w odniesieniu do podstawowego systemu FreeCAD. Każdy twórca modułu może podjąć swoją własną decyzję.


{{Quote|Jürgen Riegel|15 Październik 2006}}





 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Licence/pl
