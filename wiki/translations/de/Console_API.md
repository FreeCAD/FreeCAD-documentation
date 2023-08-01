# Console API/de
**(Oktober 2019) Bearbeite diese Seiten nicht. Die Informationen sind unvollständig und veraltet. Die neueste API findest Du in der [https://www.freecadweb.org/api autogenerierten API-Dokumentation] oder generiere die Dokumentation selbst, siehe [Quelldokumentation](Source_documentation/de.md).**

Diese Modul ist im FreeCAD-Module integriert und enthält Methoden, um Text auf der FreeCAD-Ausgabe-Konsole und Statuszeile auszugeben. Die Ausgaben haben eine unterschiedliche Farbe, abhängig von Meldung, Warnung oder Fehler.

Beispiel: 
```python
import FreeCAD
FreeCAD.Console.PrintMessage("Hello World!\n")
```


{{APIFunction|GetStatus|"Log" or "Msg" or "Wrn" or "Err"|Get the status for either Log, Msg, Wrn or Error for an observer|a status string.}}


{{APIFunction|PrintError|string|Prints an error message to the output|nothing}}


{{APIFunction|PrintLog|string|Prints a log message to the output|nothing}}


{{APIFunction|PrintMessage|string|Prints a message to the output|nothing}}


{{APIFunction|PrintWarning|string|Prints a warning to the output|nothing}}


{{APIFunction|SetStatus|string|Set the stats for either Log, Msg, Wrn or Error for an observer| }}



---
![](images/Button_right.svg) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Console API/de
