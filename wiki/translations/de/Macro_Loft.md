# Macro Loft/de
{{Macro/de
|Name=Macro Loft
|Icon=FCCreaLoft.png
|Description=Erzeugt ein Loft mit ausgewählten Drähten.
|Author=Mario52
|Version=00.04
|Date=2019-07-03
|Download=[https://www.freecadweb.org/wiki/images/2/29/FCCreaLoft.png ToolBar Icon]
|SeeAlso= [32px|FCTexture](File:FCTexture.png.md) [Macro Texture](Macro_Texture/de.md)
|FCVersion=All
}}

## Beschreibung

Speziell für einfaches Lofting mit Linien geschrieben, die von [Macro Texture](Macro_Texture/de.md) erzeugt wurden (kann aber für gewöhnliche Lofts geeignet sein und verwendet werden)
{{Codeextralink|https://gist.githubusercontent.com/mario52a/c477f892233d6abe02df5e97af828ff4/raw/d633193c577e8257ef458b8c1824d1047c3c6613/Macro_FCCreaLoft.FCMacro}}

<img alt="" src=images/Texture_001_Logo.png  style="width:480px;"> 
*Texture_001_Logo*

## Anwendung

Kopieren Sie das Makro und das Symbol in Ihr Makroverzeichnis.

-   ****Sort****: Sortiert die Dateneinträge.
-   ****Reverse****: Die Reihenfolge der Daten wird umgekehrt.
-   ****Reset** / **Upgrade****: Diese Schaltfläche hat so viele Funktionen:
-   \# Wenn eine Auswahl in 3Dview angezeigt wird, wird diese Schaltfläche {{KEY | Upgrade}} angezeigt.
    Wählen Sie Ihr Objekt in der 3D-Ansicht oder in der Kombinationsansicht aus und klicken Sie auf diese Schaltfläche, um die Daten im Makro zu aktualisieren. Die Schaltfläche ändert sich {{KEY | Reset}}.
-   \# Wenn vor dem Laufmakro ein oder mehrere Objekte ausgewählt werden, wird diese Schaltfläche **Reset** angezeigt.
    Alle ausgewählten Objekte werden im Makrofenster angezeigt.
    Nach **Sort** oder **Reverse** die angezeigten Daten, wird diese Schaltfläche **Reset** verwendet, um zur ursprünglichen Reihenfolge zurückzukehren.
    Wenn Sie in das 3DView klicken oder alle Objekte deaktivieren, werden diese Objekte deaktiviert Die Schaltfläche wird zum Zurücksetzen auf Makro verwendet.
    Wenn Sie ein oder mehrere Objekte in die Liste aufnehmen, wird diese Schaltfläche verwendet.
-   ****Select all****: Alle Objekte im Dokument auswählen.
-   **SpinBox**: Inkrementieren Sie den Sprung x Elemente (Standardeinstellung 1 alle Objekte werden verwendet).
-   ****Quit****: Beenden Sie das Makro.
-   **CheckBox** Wenn die CheckBox markiert ist, wird der Arbeitsfortschritt angezeigt, wenn nicht nur ProgressBar funktioniert (diese Methode ist schneller) (standardmäßig aktiviert).
-   ****Launch the Lofting****: Lofting starten und Makro zurücksetzen. Die Nummer der Auswahl wird angezeigt und die tatsächliche Zahl wird erhöht, wenn die SpinBox \"jump\" verwendet wird

### Die Schnittstelle 

<img alt="FCCreaLoft002" src=images/Macro_FCCreaLoft_01.png  style="width:400px;"> 

## Skript

Die Symbole für Ihre Werkzeugleiste <img alt="" src=images/FCCreaLoft.png  style="width:64px;">

Laden Sie das Makro in herunter Gist [**Macro\_FCCreaLoft.FCMacro**](https://gist.github.com/mario52a/c477f892233d6abe02df5e97af828ff4)

## Links

Die Forumsdiskussion [Texture](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893&start=10)

Das [Macro Texture](Macro_Texture/de.md)

## Version

ver 00.00 : 06/02/2016

ver 00.02 : 09/02/2016 : Add button \"Select all\" and little option displayed in the button Launch (number selections) and (real number loft)

ver 00.03 : 09/02/2016 : minor (display on button)

ver 00.04 : 03/07/2019 : adapt to Python 3



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Loft/de
