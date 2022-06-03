# WikiRobots/fr
**Les robots sont intrinsèquement dangereux car ils peuvent automatiquement faire beaucoup de dégâts. Utilisez-les avec une extrême prudence!**

## Présentation

Les tâches répétitives peuvent être automatisées à l\'aide de robots ou de bots, c\'est-à-dire de programmes logiciels fonctionnant seuls sur le wiki.

Les robots classiques et les plus utilisés pour les sites wiki sont fournis par MediaWiki, sous le nom de paquet Pywikibot. Voir [Manuel   *Pywikibot](https   *//www.mediawiki.org/wiki/Manual   *Pywikibot/fr) pour des informations complètes.

En un mot, Pywikibot est une collection de scripts Python capables d\'utiliser l\'API wiki native pour agir sur les sites wiki. Pour voir la liste des API pour le wiki de FreeCAD, visitez <http   *//www.freecadweb.org/wiki/api.php>.

Pour utiliser Pywikibot, vous devez    *

1.  installer le package Pywikibot
2.  configurez Pywikibot pour qu\'il fonctionne sur le Wiki FreeCAD.
3.  lancez les scripts dont vous avez besoin pour la tâche à accomplir.

Il existe une multitude d\'informations sur la façon d\'installer, de configurer et d\'utiliser Pywikibot. Cependant, soyez conscient que ces informations, bien qu\'utiles, peuvent être trompeuses, car elles mélangent des instructions relatives à deux bases de code Pywikibot différentes et différentes versions de la collection de scripts Pywikibot.

Dans ce qui suit, vous trouverez les instructions de base pour configurer et utiliser Pywikibot sur le wiki FreeCAD. Cela vous permettra d\'effectuer les tâches les plus courantes. Pour une utilisation avancée, référez-vous au [Manuel   *Pywikibot](https   *//www.mediawiki.org/wiki/Manual   *Pywikibot/fr) et au code source Python.

## Installation

Allez sur <http   *//tools.wmflabs.org/pywikibot/> et téléchargez **package/pywikipedia/core.zip**. (le projet est aussi sous github, gerrit, etc\... mais c\'est un moyen simple d\'obtenir un paquet complet et autonome).

Décompressez le contenu dans le répertoire de votre choix.

À moins que vous ne vouliez installer les bibliothèques dans vos librairies Python, vous avez terminé (si vous voulez toujours les installer, vérifiez le fichier **INSTALL** dans le répertoire de base).

Pywikibot fonctionne avec Python 2.6 et 2.7 sans problème. Python 3 n\'a pas été testé jusqu\'à présent avec FreeCAD wiki fonctionne également.

## Configuration

Vous devez enregistrer le code Python suivant dans un fichier portant le nom **user-config.py** dans le répertoire de base où vous avez décompressé **package/pywikipedia/core.zip**. (pour être clair, dans le même répertoire où vous trouvez déjà un fichier appelé **user-config.py.sample**).


```python
# -*- coding   * cp437  -*-
family = 'freecadwiki'
mylang = 'en'
usernames['freecadwiki']['en'] = u'<<yourWikiUserName>>'
#usernames['freecadwiki']['freecadwiki'] = u'<<yourWikiUserName>>'
console_encoding = 'cp437'
```

Dans le code ci-dessus    *

-   remplacez *\<\>* par votre nom d\'utilisateur Wiki
-   remplacer *cp437* par votre *console\_encoding*. Pour connaître l\'encodage de votre console, pour Windows et Linux, lancez l\'interpréteur Python, entrez {{SystemInput|import sys}} suivi de {{SystemInput|print sys.stdout.encoding}}. Python écrira votre {{SystemOutput|console_encoding}} à l\'écran.

Vous devez ensuite enregistrer le code Python suivant dans un fichier portant le nom **freecadwiki_family.py** dans le sous-répertoire **/pywikibot/families**. (avec les autres fichiers **family_xxx.py**).


```python
# -*- coding   * utf-8  -*-

__version__ = '$Id   * 7f3891c3bbbfbd69c0b005de953514803d783d92 $'

from pywikibot import family


# The MediaWiki family
# user-config.py   * usernames['mediawiki']['mediawiki'] = 'User name'
class Family(family.WikimediaFamily)   *
    def __init__(self)   *
        super(Family, self).__init__()
        self.name = 'freecadwiki'

        self.langs = {
            'en'   * 'www.freecadweb.org',
        }

    def scriptpath(self, code)   *
        return 'wiki'

    def path(self, code)   *
        return '/index.php' #The path of index.php, look at your wiki address. 
     
    def apipath(self, code)   *
        return '/api.php' #The path of api.php

    def version(self, code)   *
        # Replace with the actual version being run on your wiki
        return '1.20.3'

    def protocol(self, code)   *
        """
        Can be overridden to return 'https'. Other protocols are not supported.
        """
        return 'http'
        #return 'https' # My server uses https
```

## Utilisation

Vous êtes maintenant prêt à lancer les scripts de Pywikibot. Les scripts eux-mêmes sont contenus dans le sous-répertoire **/scripts**, dont vous pouvez connaître les noms.

Pour lancer les scripts, ouvrez un terminal et allez dans le répertoire de base (celui de l\'installation, PAS le sous-répertoire **/scripts**), et écrivez


{{SystemInput|python pwb.py <<scriptname>>.py -<<parameter>>}}

où bien sûr vous remplacez *\<\>* par le nom du script qui vous intéresse, et *\<\>* par le ou les paramètres requis pour le script donné.

Pour obtenir une description de l\'utilisation et des paramètres d\'un script, il suffit d\'utiliser le paramètre *-help*. Par exemple, pour obtenir une description du script **replace.py** (l\'un des plus utiles), tapez


{{SystemInput|python pwb.py replace.py -help}}

Il existe un autre paramètre très utile, valable pour tous les scripts, appelé *-simulate*, qui vous permet de tester les commandes sans endommager le Wiki. Utilisez-le avant de passer en mode \'live\'.

## Exemples

Cette commande permet de se connecter au wiki


{{SystemInput|pwb.py login.py}}

Cette commande imprimera une liste de toutes les pages contenant un lien vers SourceForge


{{SystemInput|pwb.py listpages.py -weblink   *sourceforge.net}}

Cette commande remplacera tous les liens vers l\'ancien forum SourceForge par un lien vers le nouveau forum hébergé par freecadweb.org.


{{SystemInput|pwb.py replace.py -weblink   *sourceforge.net/apps/phpbb/free-cad "sourceforge.net/apps/phpbb/free-cad" "forum.freecadweb.org"}}

Cette commande imprimera une liste de toutes les pages contenant le mot \'PartDesign\', en commençant par la page intitulée \"2d Drafting Module\" et en poursuivant par ordre alphabétique.


{{SystemInput|pwb.py listpages.py -start   *"2d Drafting Module" -grep   *PartDesign}}

Cette commande remplacera tous les liens sécurisés vers l\'ancien forum SourceForge par un lien vers le nouveau forum hébergé par freecadweb.org dans les pages traduites.


{{SystemInput|pwb.py replace.py -start   *Translations   *! "https   *//sourceforge.net/apps/phpbb/free-cad" "http   *//forum.freecadweb.org"}}

## Commandes liées au Wiki FreeCAD 

Compter toutes les pages dans lesquelles un modèle wiki spécifique est utilisé


{{SystemInput|python3 pwb.py templatecount -count GuiCommand}}

Liste de toutes les pages dans lesquelles un modèle wiki spécifique est utilisé.


{{SystemInput|python3 pwb.py templatecount -list GuiCommand}}

Remplacer une chaîne dans toutes les pages listées dans la catégorie Arch (connu comme )


{{SystemInput|python3 pwb.py replace.py -cat   *Arch}}

[Category   *Arch](Category_Arch.md) [Category   *Administration](Category_Administration.md) [Category   *Developer](Category_Developer.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Administration](Category_Administration.md) > [Developer](Category_Developer.md) > WikiRobots/fr
