# WikiRobots/pl
**Roboty są z natury niebezpieczne, ponieważ mogą automatycznie wyrządzić wiele szkód. Używaj ich z najwyższą ostrożnością!**

## Informacje ogólne 

Powtarzalne zadania mogą być zautomatyzowane za pomocą robotów lub botów, czyli programów komputerowych działających samodzielnie na wiki.

Naturalne i najczęściej używane roboty dla stron wiki są dostarczane przez MediaWiki, pod nazwą pakietu Pywikibot. Zobacz [Manual:Pywikibot](http://www.mediawiki.org/wiki/Manual:Pywikibot), aby uzyskać pełne informacje.

W skrócie, Pywikibot jest zbiorem skryptów Pythona zdolnych do używania natywnego API wiki do działania na stronach wiki. Aby zobaczyć listę API dla FreeCAD wiki, odwiedź <http://www.freecadweb.org/wiki/api.php>.

Aby korzystać z Pywikibota, należy:

1.  zainstaluj pakiet Pywikibot
2.  skonfiguruj Pywikibota do pracy na FreeCAD Wiki
3.  uruchom skrypty potrzebne do wykonania danego zadania

Istnieje wiele informacji o tym jak zainstalować, skonfigurować i używać Pywikibota. Należy jednak pamiętać, że informacje te, choć przydatne, mogą być mylące, ponieważ mieszają instrukcje dotyczące dwóch różnych baz kodu Pywikibota i różnych wersji kolekcji skryptów Pywikibota.

Poniżej znajdziesz podstawowe instrukcje, jak skonfigurować i używać Pywikibota na wiki FreeCAD. Pozwoli Ci to na wykonywanie najczęstszych zadań. W celu uzyskania bardziej zaawansowanych informacji należy zapoznać się z [Manual:Pywikibot](http://www.mediawiki.org/wiki/Manual:Pywikibot) oraz z kodem źródłowym w środowisku Python.

## Instalacja

Wejdź na stronę <http://tools.wmflabs.org/pywikibot/> i pobierz **package/pywikipedia/core.zip** *(projekt jest również na githubie, gerrit, itp., ale jest to prosty sposób, aby uzyskać pełny, samodzielny pakiet)*.

Rozpakuj zawartość w wybranym przez siebie katalogu.

Jeśli nie chcesz zainstalować bibliotek w lokalizacji swoich bibliotek Python, to już po wszystkim *(jeśli nadal chcesz je zainstalować, sprawdź plik **INSTALL** w katalogu bazowym)*.

Pywikibot działa ze środowiskiem Python v2.6 i v2.7 bez żadnych problemów. Python 3  nie był testowany do tej pory z FreeCAD wiki działa równie dobrze.

## Konfiguracja

Musisz zapisać poniższy kod Pythona jako plik o nazwie **user-config.py** w katalogu bazowym, w którym rozpakowałeś **package/pywikipedia/core.zip** *(dla jasności, w tym samym katalogu, w którym znajdziesz już plik o nazwie **user-config.py.sample**)*.


```python
# -*- coding: cp437  -*-
family = 'freecadwiki'
mylang = 'en'
usernames['freecadwiki']['en'] = u'<<yourWikiUserName>>'
#usernames['freecadwiki']['freecadwiki'] = u'<<yourWikiUserName>>'
console_encoding = 'cp437'
```

W powyższym kodzie:

-   zamień *\<\>* na nazwę użytkownika Wiki
-   zastąp *cp437* swoim *console_encoding*. Aby dowiedzieć się, jakie jest kodowanie twojej konsoli, w systemach Windows i Linux uruchom interpreter Pythona, wpisz {{SystemInput|import sys}}, a następnie {{SystemInput|print sys.stdout.encoding}}. Python wyświetli twoje {{SystemOutput|console_encoding}} na ekranie.

Następnie musisz zapisać poniższy kod Pythona jako plik o nazwie **freecadwiki_family.py** w podkatalogu **/pywikibot/families** *(razem z innymi plikami **family_xxx.py**)*.


```python
# -*- coding: utf-8  -*-

__version__ = '$Id: 7f3891c3bbbfbd69c0b005de953514803d783d92 $'

z pywikibot zaimportuj rodzinę


# The MediaWiki family
# user-config.py: usernames['mediawiki']['mediawiki'] = 'User name'
class Family(family.WikimediaFamily):
    def __init__(self):
        super(Family, self).__init__()
        self.name = 'freecadwiki'

        self.langs = {
            'en': 'www.freecadweb.org',
        }

    def scriptpath(self, code):
        return 'wiki'

    def path(self, code):
        return '/index.php' #The path of index.php, look at your wiki address. 
     
    def apipath(self, code):
        return '/api.php' #The path of api.php

    def version(self, code):
        # Replace with the actual version being run on your wiki
        return '1.20.3'

    def protocol(self, code):
        """
        Can be overridden to return 'https'. Other protocols are not supported.
        """
        return 'http'
        #return 'https' # My server uses https
```

## Użycie

Teraz możesz już uruchamiać skrypty Pywikibota. Same skrypty znajdują się w podkatalogu **/scripts**, z którego możesz poznać ich nazwy.

Aby uruchomić skrypty, należy otworzyć konsolę i przejść do katalogu bazowego *(instalacyjnego, NIE podkatalogu **/scripts**)*, a następnie napisać


{{SystemInput|python pwb.py <<scriptname>>.py -<<parameter>>}}

gdzie oczywiście zastępujemy *\<\>* nazwą interesującego nas skryptu, a *\<\>* parametrem*(ami)* wymaganym*(i)* dla danego skryptu.

Aby mieć opis użycia i parametrów dowolnego skryptu, po prostu użyj parametru *-help*. Na przykład, aby uzyskać opis skryptu **replace.py** *(jeden z najbardziej użytecznych)*, wpisz


{{SystemInput|python pwb.py replace.py -help}}

Istnieje jeszcze jeden bardzo użyteczny parametr, ważny dla wszystkich skryptów, o nazwie *-simulate*, który pozwala na testowanie poleceń bez szkody dla Wiki. Warto go użyć przed rozpoczęciem pracy na żywo.

## Przykłady

Ta komenda zaloguje do wiki


{{SystemInput|pwb.py login.py}}

To polecenie wydrukuje listę wszystkich stron zawierających link do SourceForge


{{SystemInput|pwb.py listpages.py -weblink:sourceforge.net}}

To polecenie zastąpi wszystkie linki do starego forum SourceForge linkiem do nowego forum hostowanego przez freecadweb.org


{{SystemInput|pwb.py replace.py -weblink:sourceforge.net/apps/phpbb/free-cad "sourceforge.net/apps/phpbb/free-cad" "forum.freecadweb.org"}}

To polecenie wydrukuje listę wszystkich stron zawierających słowo **PartDesign**, zaczynając od strony zatytułowanej \"2d Drafting Module\" i idąc dalej alfabetycznie


{{SystemInput|pwb.py listpages.py -start:"2d Drafting Module" -grep:PartDesign}}

Ta komenda zastąpi wszystkie bezpieczne linki do starego forum SourceForge linkiem do nowego forum hostowanego przez freecadweb.org na przetłumaczonych stronach


{{SystemInput|pwb.py replace.py -start:Translations:! "https://sourceforge.net/apps/phpbb/free-cad" "http://forum.freecadweb.org"}}

## FreeCAD Wiki Powiązane komendy 

Policz wszystkie strony, na których użyto określonego szablonu wiki


{{SystemInput|python3 pwb.py templatecount -count GuiCommand}}

Lista wszystkich stron, na których użyty jest określony szablon Wiki


{{SystemInput|python3 pwb.py templatecount -list GuiCommand}}

Zamień ciąg we wszystkich stronach wymienionych w kategorii Arch *(a/k/a )*


{{SystemInput|python3 pwb.py replace.py -cat:Arch}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Administration](Category_Administration.md) > [Developer](Category_Developer.md) > WikiRobots/pl
