# Macro FCInfo Alternate Linux/it
{{Macro/it
|Name=Macro FCInfo Alternate Linux
|Name/it=Macro FCInfo Alternate Linux
|Translate=Info per Linux
|Icon=FCInfo.png
|Description=Fornisce una serie di informazioni sulla forma.(solo per PyQt4)
|Author=Mario52
|Version=1.12
|Date=2014-03-05
|SeeAlso=[Macro FCInfo](Macro_FCInfo/it.md)
}}

## Description

Fornisce una ampia serie di informazioni sulla forma selezionata quali lunghezza, angoli, superficie, inclinazione, volume e peso secondo la densità della forma selezionata, sia nelle unità del Sistema Internazionale che in quelle del Sistema Anglosassone.(solo per PyQt4)


{{Codeextralink|https   *//gist.githubusercontent.com/mario52a/6c6b6131b0c14d800033/raw/ffa3d6857abb0ea207cee1ae13c1cb78edadbcf5/FCInfo_fr_Ver_1-12_No_Docked_Ubuntu.FCMacro}}

Il server non accetta per il momento delle pagine più grandi di 64 KB e mi era impossibile aggiornare e ripristinare.

## Script

Scaricare il file da qui   *

[FCInfo_en_Ver_1-12_No_Docked_Ubuntu.FCMacro.zip](http   *//forum.freecadweb.org/download/file.php?id=4453)

[oppure nel forum](http   *//forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=48579#p48579)

La differenza tra la versione normale e la versione \"Ubuntu\" consiste in un diverso tipo di di procedura di codifica dei caratteri sopra + 128
Questa versione è derivata dalla versione originale, la differenza si trova al livello di codifica dei caratteri *\'² ³ ° μ*\' che possono causare l\'errore \"ordinal not in range (128)\" in alcune configurazioni.

Esempio   * 
```python
global uniteSs       ; uniteSs       = u"mm²"
global uniteVs       ; uniteVs       = u"mm³"
global uniteAs       ; uniteAs       = u"°"
``` replace to    * 
```python
global uniteSs       ; uniteSs       = "mm"+iso8859(unichr(178))
global uniteVs       ; uniteVs       = "mm"+iso8859(unichr(179))
global uniteAs       ; uniteAs       = iso8859(unichr(176))
```

I file salvati con questa macro sono incompatibili con i file delle altre versioni.

Entrambe le versioni possono funzionare indipendentemente dal sistema operativo utilizzato.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCInfo Alternate Linux/it
