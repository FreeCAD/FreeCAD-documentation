# Macro FCInfo Alternate Linux/de

 {{Macro/de
|Name=Macro FCInfo Alternate Linux
|Translate=Macro FCInfo Alternate Linux
|Icon=FCInfo.png
|Description=Gibt eine Reihe von Informationen im Formular aus (nur für PQt4).
|Author=Mario52
|Version=1.12
|Date=2014-03-05
}}

## Beschreibung

Gibt eine Reihe von Informationen über die ausgewählte Form und kann eine Umwandlung von Länge, Neigung (Grad, Bogenmaß, Neigung, Fließvermögen), Form, Oberfläche, Volumen und Gewicht der Form in der ausgewählten Dichte in verschiedenen Mengeneinheiten international und englisch anzeigen -Saxon (nur für PyQt4).


{{Codeextralink|https://gist.githubusercontent.com/mario52a/6c6b6131b0c14d800033/raw/ffa3d6857abb0ea207cee1ae13c1cb78edadbcf5/FCInfo_fr_Ver_1-12_No_Docked_Ubuntu.FCMacro}}

Der Server akzeptiert für den Moment keine weiteren Seiten von 64 KB und es war nicht möglich, diese Seite für mich zu aktualisieren und wiederherzustellen.

## Skript

Laden Sie die Datei hier herunter:

[FCInfo\_en\_Ver\_1-12\_No\_Docked\_Ubuntu.FCMacro.zip](http://forum.freecadweb.org/download/file.php?id=4453)

[Oder im Forum](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=48579#p48579)

Der Unterschied zwischen der regulären Version und der Version \"Ubuntu\" besteht in einer anderen Art der Kodierung der Zeichen über + 128 mit der Prozedur
PS: Diese Version ist von der Originalversion abgeleitet, der Unterschied liegt auf der Ebene der Kodierung **² ³ ° µ** Zeichen, die bei einigen Konfigurationen den Fehler \"ordinal nicht im Bereich (128)\" verursachen können.

Beispiel: 
```python
global uniteSs       ; uniteSs       = u"mm²"
global uniteVs       ; uniteVs       = u"mm³"
global uniteAs       ; uniteAs       = u"°"
``` replace to : 
```python
global uniteSs       ; uniteSs       = "mm"+iso8859(unichr(178))
global uniteVs       ; uniteVs       = "mm"+iso8859(unichr(179))
global uniteAs       ; uniteAs       = iso8859(unichr(176))
```

Mit diesem Makro gespeicherte Dateien sind nicht kompatibel mit den Dateien der anderen Versionen.

Beide Versionen können unabhängig vom verwendeten Betriebssystem ausgeführt werden.




