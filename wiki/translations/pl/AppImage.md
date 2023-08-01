# AppImage/pl
**Od 7 lipca 2019 roku społeczność FreeCAD obserwuje, że pobieranie AppImages z Github wydaje się powodować przekroczenie czasu przed zakończeniem. Nie jesteśmy pewni, dlaczego tak się dzieje. Jeśli tak się dzieje u Ciebie proszę spróbuj pobrać ponownie. Może to zająć kilka prób. Zalecaną praktyką jest użycie [https://www.freecadweb.org/wiki/Appimage#Automatic_updating funkcji autoaktualizacji], AppImage która przywróci pobieranie z miejsca, w którym się nie powiodło.**






## Czym jest AppImage? 

![](images/AppImage-logo.png ) **Wystarczy raz przygotować pakiet, by móc go uruchomić wszędzie. Pozwala dotrzeć do użytkowników wszystkich głównych dystrybucji Linuksa.**

AppImage to \"uniwersalny pakiet binarny\" przeznaczony do dystrybucji aplikacji do dowolnej dystrybucji Linuksa. Więcej o nim można przeczytać na stronie [domowej Appimage](https://appimage.org) i [Wikipedii](https://en.wikipedia.org/wiki/AppImage).

Aby go uruchomić, najpierw uczyń go wykonywalnym, a następnie wpisz względną lub pełną ścieżkę.


```python
chmod +x FreeCAD_xxx-x86_64.AppImage
./FreeCAD_xxx-x86_64.AppImage
```

Inne wersje instalacyjne znajdziesz na stronie [pobierania](Download/pl.md).



## AppImages dla FreeCAD 

  Stable                                                                                                                Development
   
  ![](images/AppImage-logo.png ) [v0.20.2](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/0.20.2)   ![](images/AppImage-logo.png ) [Weekly build](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds)

  : style=\"text-align: center; font-size: 150%; \| Available FreeCAD AppImages \|+

**Ważne uwagi:**

-   Rozwój postępuje codziennie i dynamicznie.
-   Wielu użytkowników na forum korzysta z wersji rozwojowej.
-   Może być uruchomiona na tym samym systemie równolegle z inną wersją FreeCAD.
-   Użytkownicy używają wersji rozwojowej, aby skorzystać z najnowszych funkcji i poprawek błędów *(ponieważ FreeCAD ma długi cykl wydawniczy)*. Używają jej również do testowania i znajdowania błędów, aby stymulować rozwój i ulepszanie FreeCAD.



#### Obowiązkowe słowo przestrogi 

W przeważającej części wersja rozwojowa jest stabilna, ale oczywiście należy dodać obowiązkowe stwierdzenie, aby używać jej na własne ryzyko. Chociaż większość ludzi, którzy wykorzystują kopie zapasowe i \"często zapisują\" radzi sobie całkiem dobrze.



## Automatyczne aktualizacje 

AppImage ma inteligentny i ekonomiczny sposób aktualizacji. Oblicza różnicę między nowym AppImage a starym i pobiera tylko zmiany między ich wersjami. Teoretycznie użytkownik za każdym razem pobiera około 15% zamiast zupełnie nowego AppImage.

Automatyczna aktualizacja odbywa się za pomocą kilku opcjonalnych metod. Obecnie istnieją cztery metody, dwie przez interfejs graficzny *(GUI)* i dwie przez interfejs wiersza poleceń / terminala *(CLI)*.



### Eksperymentalna aktualizacja w aplikacji 

Dzięki wysiłkom kilku kluczowych deweloperów, istnieje dyskusja [bieżące wysiłki](https://forum.freecadweb.org/viewtopic.php?f=8&t=44324), aby zintegrować funkcję, która pozwala na **samoaktualizację AppImage w programie FreeCAD**. Począwszy od FC 0.19.21514 istnieje teraz sekcja AppImage dostępna poprzez menu **Edycja → Preferencje → AppImage**. Proszę przetestować tę możliwość i zgłosić swoje doświadczenia na [forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=44324).



### GUI, metoda 1 *(oficjalna)* 

To jest oficjalna aplikacja AppImageUpdate GUI.

1.  Pobierz [AppImageUpdate-x86_64.AppImage](https://github.com/AppImage/AppImageUpdate/releases/download/continuous/AppImageUpdate-x86_64.AppImage).
2.  Uczyń plik wykonywalnym klikając prawym przyciskiem myszy na nim, wchodząc do właściwości i \"Uruchom jako wykonywalny\".
3.  Kliknij dwukrotnie na ikonę AppImage, pojawi się okno dialogowe i zostaniesz poproszony o określenie, jaki AppImage chcesz zaktualizować.
4.  Określ ścieżkę do istniejącego AppImage.
5.  Po aktualizacji AppImage, naciśnij przycisk **Run updated AppImage**.



### GUI, metoda 2 *(nieoficjalna)* 

To jest bardziej elegancka, niezależna, nieoficjalna wersja AppImageUpdate o nazwie: **AppImageUpdater**. Jest jeszcze w fazie rozwoju *(w czasie tej edycji wiki)*, ale mimo to, całkiem przyjemna w użyciu.

1.  Pobierz [AppImageUpdater-\*-x86_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous)
2.  Nadaj mu atrybut wykonywalności: 
```pythonchmod +x AppImageUpdater*-x86_64.AppImage```
3.  Uruchom go: 
```pythonsource AppImageUpdater*-x86_64.AppImage```
4.  Znajdź swój aktualny obraz FreeCAD AppImage i przeciągnij go na AppImageUpdater

Wynik: Postępuj zgodnie z podpowiedziami AppImageUpdater



### CLI, metoda 1 *(oficjalna)* 

Uruchom w terminalu następujące instrukcje


```python
wget https://github.com/AppImage/AppImageUpdate/releases/download/continuous/appimageupdatetool-x86_64.AppImage
chmod +x ./appimageupdatetool-x86_64.AppImage
./appimageupdatetool.AppImage path/to/old/FreeCAD.AppImage
chmod +x path/to/updated/FreeCAD.AppImage
./path/to/updated/FreeCAD.AppImage
```

Uwagi:

-   Nazwy plików będą unikalne z powodu informacji o wersji, która jest w nich osadzona. Powyższe instrukcje są uproszczone dla wygody.
-   Uruchom polecenie `./appimageupdatetool-x86_64.AppImage --help`, aby dowiedzieć się o funkcjach takich jak `--remove-old`, `--overwrite` i `--self-update`.
-   Istnieje również wersja i386; zobacz stronę [wydania AppImageUpdate](https://github.com/AppImage/AppImageUpdate/releases).

Zadanie: udostępnić skrypt, który można dodać jako alias lub zadanie [cron](https://en.wikipedia.org/wiki/Cron).



### CLI, metoda 2 *(nieoficjalna)* 

Podobnie jak w przypadku metod graficznych mających oficjalne i nieoficjalne podejście do pobierania AppImages, to samo dotyczy wiersza poleceń. Jest to elegancka opcja dotycząca wiersza poleceń pochodząca od innych osób, aby pobrać AppImages.

1.  Pobierz [appimageupdater-\*-x86_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous-cli)
2.  Uczyń go wykonywalnym: 
```pythonchmod +x appimageupdater*-x86_64.AppImage```
3.  Uruchom go: 
```pythonsource appimageupdater*-x86_64.AppImage /path/to/old/FreeCAD-AppImage.AppImage```

**Wynik**: Aktualizuje wskazany plik AppImage, jeśli aktualizacja jest dostępna.



# Eksperymentalne



## Naprawianie zsync dla AppImage 

Może się zdarzyć, że AppImage nie będzie aktualizowany, ponieważ jego plik docelowy zmienił się w jakiś sposób. Zamiast pobierać cały nowy AppImage, można przepisać plik zsync, który jest używany przez AppImage do pobrania zmiany. Więcej informacji można znaleźć na stronie <https://github.com/antony-jr/appimage-update-info-writer>.

Ta część wymaga więcej szczegółów.



## Pobieranie przez Bittorrent 

Eksperymentalną funkcją, którą bada zespół pakujący FreeCAD *(dzięki pracy Antony-jr)* jest możliwość pobrania pliku appimage delta FreeCAD przez bittorrent. Zagadnienie repozytorium znajduje się pod adresem <https://github.com/FreeCAD/FreeCAD-Bundle/issues/49>.



# Sekcja Deweloperów 


**Uwaga:**

poniższe sekcje są przeznaczone dla programistów.



## Rozpakowanie AppImages 

Bardzo wygodnym aspektem FreeCAD jest to, że większość z nich jest zbudowana w środowisku [Python](Python/pl.md), które nie musi być samodzielnie kompilowane jak C++. Zasadniczo, plik Pythona może zostać zmodyfikowany, a po ponownym uruchomieniu programu FreeCAD zmiany te zostaną zintegrowane z aplikacją. Programista może szybko pracować nad najnowszym wydaniem FreeCAD używając tej techniki i AppImage. Co więcej, użycie AppImage nie modyfikuje w żaden sposób środowiska Twojego systemu, to znaczy, że nic nie jest instalowane i żadne zmienne środowiskowe nie są modyfikowane.



### Modyfikacja AppImages 

AppImage osadza w sobie system plików ze wszystkim, co jest wymagane do uruchomienia aplikacji. Aby go zmodyfikować, system plików musi zostać wyodrębniony.


```python
./FreeCAD_xxx.AppImage --appimage-extract
cd squashfs-root/
```

Teraz otwórz wymagane pliki źródłowe Pythona w preferowanym edytorze kodu, zmodyfikuj je i zapisz. Następnie uruchom aplikację.


```python
./AppRun
```



### Przepakowanie AppImages 

Jeśli zmodyfikowałeś kod, a teraz chcesz ponownie spakować AppImage z najnowszymi zmianami, użyj narzędzia [appimagetool-x86_64](https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage) na wyodrębnionym systemie plików.


```python
cd ..
wget "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
chmod +x appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage squashfs-root
```



## Personalizowanie AppImages 

Dzięki pracy **realthunder**, autora [App Link](App_Link/pl.md) i środowiska pracy [Assembly3](Assembly3_Workbench/pl.md), możliwe jest budowanie niestandardowych AppImages przy użyciu zestawu skryptów.

Dzięki temu bardzo wygodnie jest wydawać obrazy dla konkretnej gałęzi kodu źródłowego, aby inni mogli je testować. Chociaż AppImages działają tylko na Linuksie, skrypty realthundera umożliwiają generowanie AppImages także na Windows i MacOS.

Repozytorium dla tych skryptów znajduje się pod adresem [realthunder/FreeCADMakeImage](https://github.com/realthunder/FreeCADMakeImage). Proszę przeczytać informacje z pliku [Readme.md](https://github.com/realthunder/FreeCADMakeImage/blob/master/Readme.md), aby uzyskać więcej szczegółów.



## Powiązane

-   pakiety [Snap](Ubuntu_Snap/pl.md).
-   pakiety [Flatpak](Flatpak/pl.md).



---
⏵ [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > AppImage/pl
