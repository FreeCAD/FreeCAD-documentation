# UTF Project/fr
**
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
**


{{TOCright}}

C\'est le plan de projet pour la partie FreeCAD du Guide de la [route de développement](Development_roadmap/fr.md).

## But et principes 

Pour améliorer les capacités multilingues de FreeCAD, mettant en œuvre la prise en charge des caractères [UTF](http://fr.wikipedia.org/wiki/UTF-8) dans l\'interface [Coin3D](https://bitbucket.org/Coin3D/coin/wiki/Home).

Malgré que Coin3D passe maintenant à une plate-forme de développement plus ouverte, il est toujours très difficile de contribuer à ce projet.

(mrlukeparry) J\'ai encore reçu une réponse retour pour la contribution ,et, il semble maintenant plus approprié de le conserver au sein du projet FreeCAD et cela signifierait que nous pouvons permettre aux utilisateurs de faire des tests sans devoir travailler avec les versions de développement de Coin3D. J'aurai pour objectif de parvenir à la version 0,14, en considérant que c\'est une haute priorité pour accroître l\'accessibilité de FreeCAD aux utilisateurs non-anglophoness.

## Organisation

-   Présenter une chaîne UTF de base indépendante des principales bibliothèques STL à l\'exception des fonctionnalités de manipulation.

-   Mettre en place les champs Coin3D, et, les nœuds de texte 3D pour gérer le stockage de nouvelles données UTF.

-   Migrer les modules sur pour utiliser les nouveaux nœuds de textes.

-   tests rigoureux.

## Actions suivantes 

-   Misee en place de la chaîne UTF de classe **(WIP)**.

-   Gestion des polices, et, des glyphes.

-   Mettre en œuvre le champ texte Coin3D, et, les nœuds pour les utiliser dans le projet.

Migrer des modules pour exploiter de nouveaux nœuds à l\'aide de [SoText2](http://doc.coin3d.org/Coin/classSoText2.html) et [SoText3](http://doc.coin3d.org/Coin/classSoText3.html)



[<img src="images/Property.png" style="width:16px"> Roadmap](Category_Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > UTF Project/fr
