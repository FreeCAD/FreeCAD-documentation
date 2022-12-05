# Macro FCInfo Alternate Linux/cs
{{Macro/cs
|Name=Macro FCInfo Alternate Linux
|Translate=Macro FCInfo Alternate Linux
|Icon=FCInfo.png
|Description=Vrátí sadu informací o formuláři. (pouze pro PyQt4)
|Author=Mario52
|Version=1.12
|Date=2014-03-05
}}

## Popis

Poskytuje řadu informací o vybraném tvaru a může zobrazovat konverzi délky, svahu (stupeň, radián, sklon, průtok), tvar, povrch, objem a hmotnost tvaru ve zvolené hustotě v různých měrných jednotkách v mezinárodním měřítku a v angličtině-Saxon (pouze pro PyQt4).


{{Codeextralink|https://gist.githubusercontent.com/mario52a/6c6b6131b0c14d800033/raw/ffa3d6857abb0ea207cee1ae13c1cb78edadbcf5/FCInfo_fr_Ver_1-12_No_Docked_Ubuntu.FCMacro}}

Server momentálně nepřijímá více stránek 64 kB a nebylo možné tuto stránku aktualizovat a obnovit.

## Script

Stáhnout soubor zde:

[FCInfo_en_Ver_1-12_No_Docked_Ubuntu.FCMacro.zip](http://forum.freecadweb.org/download/file.php?id=4453)

[Or on the forum](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=48579#p48579)

Rozdíl mezi běžnou verzí a verzí \"Ubuntu\" v jiném typu kódování znaků nad + 128 s postupem
PS: tato verze je odvozena z původní verze, rozdíl je umístěn na úrovni kódovacích znaků **² ³ ° μ**, které mohou v některých konfiguracích způsobit chybu \"ordinal not in range (128)\" na některých konfiguracích ?

Příklad: 
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

Soubory uložené s tímto makrem nejsou kompatibilní se soubory ostatních verzí.

Obě verze mohou pracovat nezávisle na použitém operačním systému.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCInfo Alternate Linux/cs
