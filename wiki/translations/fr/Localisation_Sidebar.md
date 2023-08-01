# Localisation Sidebar/fr
La [localisation](Localisation/fr.md) est le processus consistant à fournir au logiciel une interface utilisateur multilingue. La documentation wiki peut également être localisé, comme décrit dans la section [Traduire le wiki](Localisation/fr#Traduire_le_wiki_FreeCAD.md).

La barre latérale est un outil de navigation important dans le monde wiki, voir [Manuel: Interface/Barre latérale](http://www.mediawiki.org/wiki/Manual:Interface/Sidebar/fr) pour plus d\'informations.

## Traduire la barre latérale 

La barre latérale est maintenant entièrement traduisible avec [l\'extension Traduction](http://www.mediawiki.org/wiki/Help:Extension:Translate), qui est disponible dans toutes les pages du wiki.

Dans le wiki FreeCAD, la barre latérale est implémentée à l\'aide de modèles, qui changent le texte en fonction de la langue sélectionnée. Les détails techniques sur la façon dont cette fonctionnalité a été mise en œuvre sont décrits dans le sujet du forum [Wiki navigation / translation](http://forum.freecadweb.org/viewtopic.php?f=21&t=9687&start=10#p80441).

### Instructions

Vous pouvez aller à la page [Special:Translate/wiki-sidebar](Special:Translate/wiki-sidebar.md) pour commencer la traduction.

Il y a un bug avec la page de téléchargement. Vous ne pouvez pas rediriger le lien vers \"Download/fr\", ou \"Download/de\", etc. Au lieu de cela, le lien pointe vers la traduction de \"Download\" dans votre propre langue. La meilleure façon de traiter ce point est de créer cette nouvelle page et de rediriger celle-ci vers la bonne page. Plus d\'information à propos des redirections sur [Help:Editing](Help_Editing.md).

## Remarques importantes 

La plupart du temps, il y aura deux chaînes de caractères pour chaque item de la barre latérale.

** {{int:sidebar-faq-cible}}|sidebar-faq

Le groupe de gauche représente la cible du lien, tandis que celui de droite représente le texte qui sera affiché dans la barre latérale.

Vous pouvez voir la différence entre les deux en regardant en haut de la zone de traduction où le nom de la variable est affiché. Lorsque le nom de la variable se termine par \"-cible\", cela signifie que vous allez traduire un lien cible. Cela est prévu pour permettre au traducteur de rediriger les items vers les pages traduites, c\'est-à-dire en ajoutant un code de langue à la fin du nom de page, par exemple, \"/fr\" pour une traduction française.

N\'ajoutez pas les codes de langue \"/fr\", \"/de\", \"/es\", \"/ru\", etc. Si la page traduite n\'existe pas dans cette langue, le lien sera rompu. Dans ce cas, n\'écrivez rien d\'autre que le nom de la page, sinon vous briserez le lien.

![Ou regarder](images/Translate-sidebar-instruction.png )



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Wiki](Category_Wiki.md) > Localisation Sidebar/fr
