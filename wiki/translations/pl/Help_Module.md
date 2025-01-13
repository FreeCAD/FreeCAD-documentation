# Help Module/pl
## Opis

Moduł Pomoc jest odpowiedzialny za obsługę wszystkich żądań dotyczących dokumentacji i wyświetlanie jej w odpowiedni sposób. Do wersji FreeCAD 0.21, moduł Pomoc był dostępny jako [dodatek](Std_AddonMgr/pl.md), po tej wersji jest dołączony do programu FreeCAD. Można bez problemu zostawić dodatek zainstalowany po wersji 0.21.

Moduł Pomoc zapewnia stronę preferencji w **Edycja → Preferencje → Ogólne → Pomoc**, co pozwala na określenie:

-   Źródła dokumentacji: Dokumentacja może być przechwytywana ze źródeł online, takich jak [official FreeCAD wiki](https://wiki.freecad.org) (domyślnie) lub [konwersja Markdown](https://github.com/FreeCAD/FreeCAD-documentation) bądź z lokalizacji offline, takiej jak folder, do którego dokumentacja może być pobrana przy pomocy [Menedżera dodatków](Std_AddonMgr/pl.md).

-   Sposobu wyświetlania dokumentacji: w przeglądarce systemowej, w osobnym dokowalnym oknie dialogowym, które pozwala np. trzymać dokumentację otwartą podczas pracy (przydatne dla tutoriali) lub w nowej zakładce programu FreeCAD. Zauważ, że w wersji 1.0 te dwie ostatnie opcje wymagają komponentów PySide Web. Jeśli ich nie ma, można użyć zamiast tego pierwszej opcji.

-   Alternatywnego pliku css: To jest używane tylko podczas używania źródeł Markdown lub offline opisanych wyżej i pozwala na dostosowanie stylu dokumentacji.



## Tworzenie skryptów 

Moduł Pomoc składa się zasadniczo z [pojedynczego modułu Pythona](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/Help/Help.py). Jego głównym celem jest używanie funkcji {{Incode|show}}. Może przechwycić URL, lokalny plik (Markdown lub html) bądź znaleźć stronę automatycznie z ustawień w **Preferencje → Ogólne → Pomoc**.

Niezależnie od tego co zapewnisz, system rozpozna zawartość HTML lub Markdown i wyświetli ją odpowiednio.

Podstawowe użycie:


```python
import Help
Help.show("Draft Line")
Help.show("Draft_Line")  # works with spaces or underscores
Help.show("https://wiki.freecadweb.org/Draft_Line")
Help.show("https://gitlab.com/freecad/FreeCAD-documentation/-/raw/main/wiki/Draft_Line.md")
Help.show("/home/myUser/.FreeCAD/Documentation/Draft_Line.md")
Help.show("http://myserver.com/myfolder/Draft_Line.html")
```



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [Help](Help_Workbench.md) > Help Module/pl
