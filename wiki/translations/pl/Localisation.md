# Localisation/pl
## Informacje ogólne 

**Lokalizacja** oznacza zasadniczo proces dostarczania oprogramowania z wielojęzycznym interfejsem użytkownika. W FreeCAD możesz ustawić język interfejsu użytkownika w **Edycja → Preferencje → Ogólnie**. FreeCAD używa [Qt](wikipedia:Qt_(toolkit).md), aby umożliwić obsługę wielu języków. W systemach Unix/Linux, FreeCAD domyślnie korzysta z bieżących ustawień lokalnych systemu.



## Pomoc w tłumaczeniu programu FreeCAD 

Jedną z bardzo ważnych rzeczy, które użytkownicy mogą wnieść do FreeCAD *(jeśli na przykład nie posiadają umiejętności programowania)* jest pomoc w tłumaczeniu jego różnych elementów *(kod źródłowy, Wiki, strona internetowa, dokumentacja itp\...)* na inny język. Są dostępne następujące sposoby, aby tego dokonać.



## Przetłumacz kod źródłowy FreeCAD 

FreeCAD korzysta z zewnętrznego systemu tłumaczeń on-line, zwanego [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

Jest to oprogramowanie własnościowe, ale wolne dla projektów [FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software). Poniżej znajdują się instrukcje jak go używać:

-   Udaj się na stronę [Crowdin tłumaczenia projektu FreeCAD](http://crowdin.net/project/freecad);
-   Zaloguj się tworząc nowy profil lub używając innego konta (GitHub, GitLab, GMail itp\...)
-   Kliknij na język nad którym chcesz pracować;
-   Rozpocznij tłumaczenie przez kliknięcie przycisku **Translate** przy jednym z plików. Na przykład **FreeCAD.ts**\' zawiera ciągi tekstu z głównego interfejsu graficznego FreeCAD.
-   Możesz głosować na istniejące tłumaczenia lub dodawać własne.

{{Message|Jeśli aktywnie bierzesz udział w tłumaczeniu FreeCAD i chcesz być informowany przed premierą kolejnego wydania, aby mieć czas na zapoznanie się z treścią tłumaczenia, zapisz się do jednego z zespołów tłumaczy Crowdin FreeCAD.}}


**Note:**

Szczegóły dotyczące używania programu Crowdin można znaleźć na stronie [Administracja Crowdin](Crowdin_Administration/pl.md).



## Tłumaczenie interfejsu zewnętrznych Środowisk pracy 

Odwiedź stronę [Tłumaczenie interfejsu Środowisk zewnętrznych](Translating_an_external_workbench.md).



## Preferencje FreeCAD dla tłumaczy 

Począwszy od FreeCAD w wersji 0.20, następujące zmienne mogą być ręcznie dodane do sekcji BaseApp/Preferences/General pliku **user.cfg**, aby pomóc w rozwoju nowych tłumaczeń:

**AdditionalLanguageDomainEntries** - aby dodać zupełnie nowe języki do programu FreeCAD, które nie są obecnie obsługiwane przez kod źródłowy, możesz użyć tej preferencji użytkownika, aby dodać je do listy dostępnych języków. Format języków to \"Nazwa języka\"=\"kod\"; na przykład:

    <FCText Name="AdditionalLanguageDomainEntries">"Esperanto"="eo";"French"="fr";</FCText>

**AdditionalTranslationsDirectory** - dodaj dodatkowy katalog, w którym FreeCAD będzie szukał plików \*.qm. Ta lokalizacja będzie miała pierwszeństwo przed \$resourceDir/translations *(dla Linux OS)* oraz \$userAppDataDir/translations *(dla Windows)*. Na przykład:

    <FCText Name="AdditionalTranslationsDirectory">C:/Users/FreeCADUser/TestTranslations</FCText>



## Tłumaczenie dokumentacji Wiki dla FreeCAD 

Wiki zawiera wiele treści, z których większość tworzy podręcznik. Możesz przeglądać dokumentację zaczynając od [Strony głównej](Main_Page/pl.md), lub zajrzeć do podręcznika użytkownika [Spis treści pomocy online](Online_Help_Toc/pl.md).

Aby móc tłumaczyć wiki, musisz mieć uprawnienia do edycji wiki; zobacz [Jak mogę uzyskać uprawnienia do edycji na wiki?](Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki?.md).

Powinieneś również posiadać znajomość znaczników Wiki i stosować się do ogólnych wytycznych dotyczących stylizacji opisanych na [witrynie Wiki](WikiPages/pl.md).



### Rozszerzenie do tłumaczenia Mediawiki 

Kiedy Wiki została odłączona od SourceForge, [Yorik](User_Yorik.md) zainstalował [MediaWiki\'s Translation extension](http://www.mediawiki.org/wiki/Help:Extension:Translate), które ułatwia tłumaczenie stron. Zaletą rozszerzenia tłumaczeń jest to, że tytuł strony może być teraz przetłumaczony, śledzi tłumaczenia, powiadamia, czy oryginalna strona została zaktualizowana, oraz utrzymuje tłumaczenia w synchronizacji z oryginalną stroną angielską.

Narzędzie jest udokumentowane w [Pomoc:Rozszerzenia:Tłumaczenie](http://www.mediawiki.org/wiki/Help:Extension:Translate) i jest częścią [MediaWiki Pakietu rozszerzeń językowych](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

Aby szybko rozpocząć przygotowywanie strony do tłumaczenia, proszę przeczytać przykład [Tłumaczenie strony](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example). Para znaczników musi zawierać całą stronę aby system tłumaczenia został aktywowany:

    &lt;translate&gt; ... &lt;/translate&gt;

Strona musi być również oznaczona do tłumaczenia.

Aby zobaczyć przykładowy sposób działania narzędzia do tłumaczenia, odwiedź stronę [Strona główna](Main_Page.md). Na górze pojawi się automatycznie wygenerowany pasek językowy. Kliknij na [polski](Main_Page/pl.md). *(polski)*, doprowadzi cię do [Main_Page/pl](Main_Page/pl.md). Tuż pod tytułem, możesz przeczytać , **XX** jest bieżącą wartością procentową postępu tłumaczenia. Kliknij na **Przetłumacz** u góry strony, aby uruchomić narzędzie do aktualizacji, korekty i przeglądania istniejącego tłumaczenia.

Jeśli przejdziesz do [Strony głównej](Main_Page/pl.md), zauważysz, że nie możesz już edytować strony bezpośrednio, przez kliknięcie znacznika \[Edit\], a górny link **Edit** został zastąpiony linkiem **Translate**, który otwiera narzędzie do tłumaczenia.

Przy dodawaniu nowych treści należy najpierw utworzyć stronę w języku angielskim, a następnie przetłumaczyć ją na inny język. Jeśli ktoś chce zmienić lub dodać treść na stronie, najpierw należy zmodyfikować stronę w języku angielskim.

Jeśli nie jesteś pewien, jak postępować z tłumaczeniami, nie wahaj się poprosić o pomoc w [Development → Wiki subforum](https://forum.freecadweb.org/viewforum.php?f=21) lub w [podforum konkretnego języka](https://forum.freecadweb.org/viewforum.php?f=11) na [forum FreeCAD](http://forum.freecadweb.org).



### Istotne uwagi 

Każdy użytkownik wiki posiadający uprawnienia **Edytora** jest w stanie uruchomić narzędzie do tłumaczenia oraz tworzyć, zapisywać i przeglądać tłumaczenia.

Jednak tylko użytkownicy z uprawnieniami **Administrator** mogą oznaczać strony do tłumaczenia. Strona, która nie jest oznaczona do tłumaczenia, nie będzie korzystać z rozszerzenia tłumaczenia i nie będzie prawidłowo zsynchronizowana z informacjami w języku angielskim.

Lewy pasek boczny jest również przetłumaczalny, ale tylko Administratorzy mogą modyfikować ten element strony. Proszę postępować zgodnie z dedykowanymi instrukcjami na stronie [Tłumaczenie paska Sidebar](Localisation_Sidebar.md).

Przy pierwszym przełączeniu strony do nowego systemu tłumaczeń, traci ona wszystkie swoje stare \"ręczne\" tłumaczenia. Aby odzyskać tłumaczenie, należy zapisać kopię starego tekstu w trybie offline przed przełączeniem. Następnie możesz użyć tego starego przetłumaczonego tekstu do wypełnienia jednostek tłumaczeń w nowym systemie. Możesz również otworzyć wcześniejszą wersję z historii i w ten sposób odzyskać stary tekst. Musi to być zrobione dla każdego języka, który miał przetłumaczoną stronę.



### Tłumaczenie dokumentacji FreeCAD 

Zgodnie z ogólnym konsensusem, strona referencyjna w Wiki jest stroną angielską, która powinna być utworzona jako pierwsza. Jeśli chcesz zmienić lub dodać treść do strony, powinieneś zrobić to najpierw na angielskiej stronie, a dopiero po zakończeniu aktualizacji przenieść modyfikację na przetłumaczoną stronę.



### Stare instrukcje tłumaczenia 

++
| Instrukcje te dotyczą wyłącznie tła historycznego. Tłumaczenia powinny używać nowego systemu z [#Mediawiki Translation Extension](#Mediawiki_Translation_Extension.md) opisanego powyżej.                                                                                                                                                                                                                                                                                                                                                         |
++
| Więc pierwszym krokiem jest **sprawdzenie czy tłumaczenie ręczne zostało już rozpoczęte dla Twojego języka** *(spójrz na lewy pasek boczny, pod \"manual\")*.                                                                                                                                                                                                                                                                                                                                                                                             |
| Jeśli nie, udaj się na [forum](http://forum.freecadweb.org/) i powiedz, że chcesz rozpocząć nowe tłumaczenie, stworzymy podstawowe ustawienia dla języka, nad którym chcesz pracować.                                                                                                                                                                                                                                                                                                                                                                     |
| Musisz wtedy [uzyskać uprawnienia do edycji wiki](Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki.3F.md).                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Jeśli Twój język jest już wymieniony, zobacz, których stron nadal brakuje w tłumaczeniu (będą one wymienione na czerwono). Technika jest prosta: **wejdź na czerwoną stronę, skopiuj/wklej zawartość odpowiedniej angielskiej strony i zacznij tłumaczyć**.                                                                                                                                                                                                                                                                                               |
| Nie zapomnij dołączyć wszystkich tagów i szablonów z oryginalnej angielskiej strony. Niektóre z tych szablonów będą miały swój odpowiednik w Twoim języku (na przykład, istnieje francuski szablon Docnav zwany Docnav/fr). W prawie wszystkich linkach powinieneś używać **ukośnika i kodu języka**. Spójrz na inne już przetłumaczone strony, aby zobaczyć, jak to zrobiono.                                                                                                                                                                            |
| Dodaj ukośnik i kod języka w kategoriach, takich jak \[\[Category:Developer Documentation/fr\]\]                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| A jeśli nie jesteś pewien, udaj się na forum i poproś ludzi, aby sprawdzili, co zrobiłeś i powiedzieli ci, czy jest to słuszne czy nie.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Cztery szablony są powszechnie używane na stronach manualnych. Te 4 szablony mają zlokalizowane wersje *(Template:Docnav/fr, Template:fr, itd.)*.                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -   [Template:GuiCommand](Template_GuiCommand.md) : to blok informacyjny Gui Command w prawym górnym rogu dokumentacji poleceń.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -   [Template:Docnav](Template_Docnav.md) : jest to pasek nawigacji na dole strony, pokazujący poprzednie i następne strony.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -   [Template:Userdocnavi](Template_Userdocnavi.md) : daje bezpośrednie linki do głównych stron bazowych                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Strona dotycząca porozumienia w sprawie nadawania nazw \'\"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Zwróć uwagę, że ze względu na ograniczenia w implementacji silnika MediaWiki w Sourceforge, wymagamy, aby wszystkie Twoje strony zachowały swoją oryginalną angielską nazwę, dołączając ukośnik i kod języka. Na przykład, przetłumaczona strona dla About FreeCAD powinna być About Freecad/es dla hiszpańskiego, About FreeCAD/pl dla polskiego, itp. Powód jest prosty: jeśli tłumacze odejdą, administratorzy wiki, którzy nie znają wszystkich języków, będą wiedzieć do czego służą te strony. Ułatwi to utrzymanie i pozwoli uniknąć utraty stron. |
| Jeśli chcesz, aby szablon Docnav pokazywał strony z linkami w Twoim języku, możesz użyć**przekierowania stron*\'. Są to w zasadzie skrócone linki do rzeczywistej strony. Oto przykład z francuską stroną dla About FreeCAD.                                                                                                                                                                                                                                                                                                                              |
| \* Strona*O FreeCAD/fr\'\' jest stroną z treścią                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -   Strona *À propos de* FreeCAD zawiera ten kod:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| #REDIRECT [[About_FreeCAD/fr]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -   Na stronie *O FreeCAD/fr*, kod Docnav będzie wyglądał tak:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| {{docnav/fr|[Bienvenue dans l'aide en ligne de FreeCAD](Online_Help_Startpage/fr.md)|[Fonctionnalités](Feature_list/fr.md)}}                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Strona *Bienvenue dans l\'aide en ligne de FreeCAD* przekierowuje do Online_Help_Startpage/fr, a strona *Fonctionnalités* przekierowuje do Feature_list/fr.                                                                                                                                                                                                                                                                                                                                                                                               |
++



## Tłumaczenie strony internetowej FreeCAD 

Tłumaczenie strony internetowej FreeCAD odbywa się teraz poprzez [Crowdin](https://crowdin.com/translate/freecad/561/en-en). Plik nazywa się **homepage.po**.



## Programowanie - jak dodać lokalizację 

Ta sekcja jest przeznaczona dla programistów, którzy chcą dodać lokalizację do swojego kodu.



### Przygotowanie modułów FreeCAD/master do tłumaczenia 

Są to części wykorzystywane w procesie tłumaczenia FreeCAD:

-   Wyodrębnij ciągi tekstu z kodu źródłowego do plików \*.ts,
-   załaduj pliki \*.ts do [FreeCAD Crowdin](http://crowdin.net/project/freecad),
-   tłumaczenie ciągów znaków w Crowdin,
-   wypakuj zmodyfikowane / nowe \* .ts pliki z Crowdin,
-   konwertuj pliki \* .ts na pliki \* .qm i aktualizuj plik \* .qrc każdego modułu,
-   aktualizacja FreeCAD Master.

Wszystkie powyższe kroki są wykonywane przez \"skrypty do tłumaczeń\", które są okresowo uruchamiane przez administratora.

Przygotowanie modułu do tłumaczenia jest dość proste. Po pierwsze, musisz upewnić się, że posiadasz katalog nazwany **translations** w **myModule/Gui/Resources**. Następnie otwórz okno terminala *(lub odpowiednik Windows/OSX)* w katalogu \"**translations** i wpisz poniższe polecenie: 
```pythonlupdate -ts myModule.ts```

W ten sposób powstaje pusty plik z tłumaczeniem. Po zakończeniu tego procesu należy upewnić się, że skrypty do tłumaczenia są aktualizowane tak, jak w tym przypadku [pull request](https://github.com/FreeCAD/FreeCAD/pull/810).

Następnie wszystko odbywa się automatycznie, jeśli chodzi o dewelopera. Administrator wyodrębni ciągi tekstowe, tłumacze je przetłumaczą, następnie administrator wyciąga tłumaczenia i aktualizuje FreeCAD/master.



### Przygotowywanie modułu zewnętrznego lub makra do tłumaczenia 

Moduły lub makra osób trzecich są tłumaczone w podobny sposób, z tym że część pracy musisz wykonać samodzielnie. Ta [dyskusja na forum](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) opisuje szczegóły.

***Aktualizacja***: zobacz [Tłumaczenie zewnętrznych środowisk pracy](Translating_an_external_workbench.md)



## Automatyzacja aktualizacji tłumaczeń Crowdin 

Obecnie opiekunowie FreeCAD używają API Crowdin poprzez [skrypty Crowdin](Crowdin_Scripts/pl.md) do wciągania i przesuwania tłumaczeń do Crowdina i z powrotem do Github repo. API Crowdin daje opiekunom FreeCAD możliwość automatyzacji procesów tłumaczenia w projekcie, więcej informacji można znaleźć w dokumentacji [Crowdin API](https://support.crowdin.com/api/api-integration-setup/).



## Powiązane strony 

-   [Administracja Crowdin](Crowdin_Administration/pl.md)
-   [Skrypty Crowdin](Crowdin_Scripts/pl.md)



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby uzyskać słownik z językami obsługiwanymi przez interfejs FreeCAD, użyj metody `supportedLocales` modułu `FreeCADGui`.


```python
locales = FreeCADGui.supportedLocales()
```

Po wykonaniu, `locales` będzie zawierał:


```python
{'English': 'en', 'Afrikaans': 'af', 'Arabic': 'ar', 'Basque': 'eu', 'Catalan': 'ca', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Dutch': 'nl', 'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'German': 'de', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kabyle': 'kab', 'Korean': 'ko', 'Lithuanian': 'lt', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Portuguese, Brazilian': 'pt-BR', 'Romanian': 'ro', 'Russian': 'ru', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es-ES', 'Swedish': 'sv-SE', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Valencian': 'val-ES', 'Vietnamese': 'vi'}
```

Aby uzyskać aktualny język interfejsu użyj metody `getLocale` z tego samego modułu:


```python
locale = FreeCADGui.getLocale()
```

Jeśli aktualnym językiem jest angielski, `locale` będzie zawierać:


```python
'English'
```

Aby uzyskać odpowiedni [kod języka](https://support.crowdin.com/api/language-codes/) można użyć:


```python
locale = FreeCADGui.supportedLocales()[Gui.getLocale()]
```

Jeśli aktualnym językiem jest angielski, wynik będzie następujący:


```python
'en'
```

Aby ustawić aktualny język interfejsu należy użyć metody `setLocale` tego samego modułu. Możesz podać język lub kod języka:


```python
FreeCADGui.setLocale('Russian')
FreeCADGui.setLocale('ru')
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Wiki](Category_Wiki.md) > Localisation/pl
