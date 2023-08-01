# Macro FCInfo Alternate Linux/fr
{{Macro/fr
|Name=Macro FCInfo Alternate Linux
|Icon=FCInfo.png
|Description=Donne une série de renseignements sur la forme. (seulement pour PyQt4)
|Author=Mario52
|Version=1.12
|Date=2014-03-05
|SeeAlso=[Macro_FCInfo](Macro_FCInfo/fr.md)
}}

## Description

Donne une série de renseignements sur la forme sélectionnée et peut afficher une conversion de la longueur, de l\'inclinaison de la forme (degrés, radian, grade, pourcent), de la surface, du volume et du poids de la forme dans la densité sélectionnée dans différentes unités de grandeurs internationales et anglo-saxonnes. (seulement pour PyQt4).


{{Codeextralink|https://gist.githubusercontent.com/mario52a/6c6b6131b0c14d800033/raw/ffa3d6857abb0ea207cee1ae13c1cb78edadbcf5/FCInfo_fr_Ver_1-12_No_Docked_Ubuntu.FCMacro}}

Le serveur n\'accepte pas pour le moment des pages plus de 64 KB et il était impossible de mettre à jour et de restaurer cette page pour moi.

## Script

Téléchargez le fichier:

[FCInfo_en_Ver_1-12_No_Docked_Ubuntu.FCMacro.zip](http://forum.freecadweb.org/download/file.php?id=4453)

[Ou sur le forum](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=48579#p48579)

La différence entre la version normale et la version \"Ubuntu\" dans un autre type d\'encodage des caractères supérieurs à + 128 avec la procédure
PS : cette version est dérivée de la version originale, la différence se situe au niveau de l\'encodage des caractères **² ³ ° µ** qui peut provoquer l\'erreur \"ordinal not in range (128)\" sur certaines configurations ?

Exemple : 
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

Les fichiers enregistrés avec cette macro sont incompatibles avec les fichiers des autres versions.

Les deux versions peuvent fonctionner indépendamment du système d\'exploitation utilisé.



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro FCInfo Alternate Linux/fr
