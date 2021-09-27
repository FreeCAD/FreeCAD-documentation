# Units project/fr
**
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
**


{{TOCright}}

Ce projet cherche à mettre en œuvre un système décent d\'unités dans FreeCAD. Il suit les règles de la \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\]. Les projets sont collectées dans la feuille de [route](Development_roadmap/fr.md).

## But et principes 

Il s\'agit d\'un projet de développement logiciel visant à mettre en œuvre un [système unitaire](units/fr.md) dans FreeCAD.

Les étapes de développement sont ici rabotées (actions suivantes) et suivies dans \"Issue tracking system\" pour obtenir un journal de modifications bien documenté : [Issue tracker](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php) <img alt="" src=images/Mantis_logo_button.gif  style="width:64px;">.

## Résultats

Permettra à FreeCAD de gérer les systèmes de mesure, comme le [Système Impérial](http://fr.wikipedia.org/wiki/Unités_de_mesure_anglo-saxonnes) et du [Système International](http://fr.wikipedia.org/wiki/Système_international_d'unités) SI.

Également, gérer les formats d\'import/export qui sont les mesure d\'unités de portage (tels que STEP). Et de permettre une valorisation, qui repose sur des conversions, **(mm → m, m → in)**. \[ modificateur \]

## Réflexions

Beaucoup de travail a été réalisé : [voir le topic ici](http://forum.freecadweb.org/viewtopic.php?f=10&t=1616).

Et vous trouverez beaucoup d\'informations dans l\'article dédié aux [Unités](Units/fr.md).

## Organisation

### Mise à jour de l\'analyse des unités 

Mise à jour de l\'analyseur, pour gérer, et, générer des **signatures** comme nous l\'expliquons dans l\'article **[Unités](Units/fr.md)**.

### Propriétés

Modification des propriétés, former des propriétés de Grandeur, par exemple pour **PropertyUntit** avec une signature par unité.

Finalement, créer un éditeur de propriétés pour **PropertyUntit** gérable par l\'utilisateur.

### Établi (boîte à outils) 

-   Mise à jour de la boîte à outils pour l\'utiliser dans le cadre des unités. Je voudrais commencer par, **[Sketcher](Sketcher_Workbench/fr.md)** et **[PartDesign](PartDesign_project/fr.md)** et aller ensuite plus loin \...
-   Documenter le processus de mise à jour, pour que les autres développeurs puissent faire de même avec d\'autres ateliers - _ 13:13, 28 Novembre 2011 (UTC)

## Actions suivantes 

-   Mise à niveau des analyseurs d\'unités ([jriegel](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=67)).



_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > Units project/fr
