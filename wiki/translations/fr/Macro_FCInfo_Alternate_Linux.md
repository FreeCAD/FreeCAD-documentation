# Macro FCInfo Alternate Linux/fr
 {{Macro/fr
|Name=Macro FCInfo Alternate
|Icon=FCInfo.png
|Description=Donne une série de renseignements sur la forme.(pour PyQt4)
|Author=Mario52
|Version=1.12
|Date=2014-03-05
|SeeAlso=[Macro_FCInfo](Macro_FCInfo/fr.md)
}}

## Description

Donne une série de renseignements sur la forme sélectionnée et peut afficher une conversion de la longueur, de l\'inclinaison de la forme (degrés, radian, grade, pourcent), de la surface, du volume et du poids de la forme dans la densité sélectionnée dans différentes unités de grandeurs internationales et anglo-saxonnes. (seulement pour PyQt4).


{{Codeextralink|https://gist.githubusercontent.com/mario52a/6c6b6131b0c14d800033/raw/ffa3d6857abb0ea207cee1ae13c1cb78edadbcf5/FCInfo_fr_Ver_1-12_No_Docked_Ubuntu.FCMacro}}

Pour le moment le serveur n\'accepte plus les pages de plus que 64 Ko et il était impossible de mettre à jour et de restaurer cette page.

## Script

Téléchargez le fichier:

[FCInfo\_en\_Ver\_1-12\_No\_Docked\_Ubuntu.FCMacro.zip](http://forum.freecadweb.org/download/file.php?id=4453)

[Or on the forum](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=48579#p48579)

Les versions de FCInfo sont les mêmes la seule différence ici le code est modifié (à cause de l\'erreur d\'affichage des caractères : ² ³ ° µ\" ordinal not in range (128)\") qui posaient problèmes dans certaines configurations toutes les fonctions sont les mêmes

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

les fichiers sauvés avec cette version sont incompatibles avec les autres versions.

Les deux versions peuvent fonctionner indépendamment du système d\'exploitation utilisé.




