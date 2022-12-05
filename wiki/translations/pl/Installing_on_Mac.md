# Installing on Mac/pl
FreeCAD można zainstalować na systemie MacOS jako pakiet .dmg, który może zostać przeciągnięty do folderu Aplikacje:


{{DownloadMacStable}}

kompilacja weekly może być pobrana z

<img alt="" src=images/Nightly.png  style="width:30px;">[Weekly](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)

Jednakże, w celu aktualizacji oprogramowania, wysoce zalecane jest użycie menedżera pakietów, takiego jak **HomeBrew**. Instrukcje instalacji HomeBrew można zobaczyć [tutaj](https://brew.sh/). Kiedy HomeBrew jest zainstalowany, możesz po prostu zainstalować FreeCAD 0.18.4 poprzez swój terminal bash z


```python
brew install --cask freecad
```

i aby użyć najnowszej dostępnej wersji na HomeBrew, możesz uruchomić


```python
brew install freecad
```

W przypadku wystąpienia jakichkolwiek problemów dotyczących HomeBrew Cask lub Formula można to zgłosić [tutaj](https://github.com/FreeCAD/homebrew-freecad).

Ta strona opisuje użycie i funkcje instalatora FreeCAD. Zawiera również instrukcje dezinstalacji. Po zainstalowaniu, możesz przejść do podręcznika [Jak zacząć](Getting_started/pl.md)!

## Łatwa instalacja 

Instalator FreeCAD jest dostarczany jako pakiet aplikacji (.app), umieszczony w pliku obrazu dysku.

Najnowszy instalator można pobrać ze strony [Download](Download/pl.md). Po pobraniu pliku wystarczy zamontować obraz dysku, a następnie przeciągnąć go do wybranego folderu dla tej aplikacji.

![](images/mac_installer_1.png )

To wszystko.
Teraz wystarczy kliknąć na ikone aplikacji, aby uruchomić FreeCAD. Jeśli ukaże się informacja \"FreeCAD nie może być otwarty, ponieważ pochodzi od niezidentyfikowanego wydawcy.\" otwórz folder aplikacji i kliknij prawym przyciskiem myszki na ikonie aplikacji, kolejnie otwórz i zaakceptuj otwieranie aplikacji.

## De-instalacja 

Obecnie nie ma dezinstalatora dla FreeCAD zainstalowanego z pakietem dmg. Aby całkowicie usunąć FreeCAD i wszystkie zainstalowane komponenty, przeciągnij następujące pliki i foldery do kosza:

-   Folder /Applications:
    -   FreeCAD

Jeśli zainstalowałeś FreeCAD z homebrajskim, po prostu użyj polecenia `brew uninstall freecad`. To jest to.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Mac/pl
