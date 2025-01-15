# Console API/pl
**''(Październik 2019)'' Nie edytuj tych stron. Informacje są niekompletne i nieaktualne. Najnowsze API można znaleźć w [https://www.freecadweb.org/api automatycznie generowana dokumentacja API], lub wygenerować dokumentację samodzielnie, śledząc dokument [Dokumentacja źródłowa](Source_documentation/pl.md).**

Ten moduł jest zawarty wewnątrz modułu FreeCAD i zawiera metody do wysyłania tekstu do konsoli wyjściowej i paska stanu programu FreeCAD. Wiadomości będą miały różny kolor, w zależności od tego czy będą to komunikaty, ostrzeżenia czy błędy.

Przykład: 
```python
import FreeCAD
FreeCAD.Console.PrintMessage("Hello World!\n")
```


{{APIFunction|GetStatus|"Log" lub "Msg" lub "Wrn" lub "Err"|Uzyskaj status Log, Msg, Wrn lub Error dla obserwatora|ciąg komunikatu stanu}}


{{APIFunction|PrintError|string|Wyświetla na wyjściu komunikat o błędzie| }}


{{APIFunction|PrintLog|string|Wyświetla na wyjściu komunikat dziennika| }}


{{APIFunction|PrintMessage|string|Wyświetla na wyjściu komunikat| }}


{{APIFunction|PrintWarning|string|Wyświetla na wyjściu ostrzeżenie| }}


{{APIFunction|SetStatus|string|Ustaw statystyki Log, Msg, Wrn lub Error dla obserwatora| }}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > Console API/pl
