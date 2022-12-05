# Macro FCInfo Alternate Linux
{{Macro
|Name=Macro FCInfo Alternate Linux
|Icon=FCInfo.png
|Description=Gives a series of information on the form. (only for PyQt4)
|Author=Mario52
|Version=1.12
|Date=2014-03-05
|SeeAlso=[[Macro_FCInfo]]
}}

## Description

Gives a series of informations about the selected shape and can display a conversion of length, inclination (degrees, radians, grades, pourcent) shape, surface, volume and the weight of the form in the density selected in different units of quantities international and Anglo-Saxon (only for PyQt4).

 

The server does not accept for the moment of the more pages of 64 KB and it was impossible to update and restore this page to me.

## Script

Download the file here :

[FCInfo_en_Ver_1-12_No_Docked_Ubuntu.FCMacro.zip](http://forum.freecadweb.org/download/file.php?id=4453)

[Or on the forum](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=48579#p48579)

The difference between the regular version and the version \"Ubuntu\" in another type of encoding of the characters above + 128 with the procedure
PS: this version is derived from the original version, the difference is located at the level of encoding **² ³ ° µ** characters that can cause the error \"ordinal not in range (128)\" on some configurations ?

Example :  
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

Files saved with this macro are incompatible with the files of the other versions.

Both versions can operate independently of the OS used.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCInfo Alternate Linux
