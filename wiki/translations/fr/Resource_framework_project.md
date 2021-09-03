


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

C\'est le plan du projet, dans le cadre des ressources de FreeCAD, inscrit dans la feuille de [route de développement](Development_roadmap/fr.md).

## Objets et principes 

Il s\'agit d\'un projet de développement logiciel visant à mettre en œuvre les capacités [Product Data Management (PDM)](http://fr.wikipedia.org/wiki/Système_de_gestion_de_données_techniques) (Système de gestion de données techniques). Il s\'agit de mettre en œuvre les instances nécessaires.

Les étapes de développement sont prévues ici, et suivies dans le système de suivi de problèmes [Mantis](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php) pour obtenir un journal des modifications bien informé : <img alt="" src=images/Mantis_logo_button.gif  style="width:48px;">

## Résultats

-   Contrôle de révision pour les projets de conception de grande taille.
-   Partager le travail avec d\'autres sur Internet / intranet(s) : **Collaboration**.
-   Les catalogues en ligne et hors ligne avec des [pièces standard](http://en.wikipedia.org/wiki/Interchangeable_parts).

## Réflexions

### Ce que font les autres 

Voici quelques liens sur des produits commerciaux comparables :

-   PTC [PDMLink](http://www.ptc.com/product/windchill/pdmlink) - *\"\... lorsque tous les intervenants ont accès à un seul référentiel digne de confiance, les fabricants ont le pouvoir de gérer toutes les formes de données numériques de produits de développement \... PDMLink est la solution idéale. Web-basé, pour faciliter l\'accès aux industries, cette industrie de gestion de données a fait ses preuves, (PDM), supporte des équipes dispersées géographiquement, tout en gérant les processus critiques tels que le changement/gestion de la configuration, et, de la conception détaillée. \"*

-   Aras Corp [Aras PLM Software](http://www.aras.com/) - Ils semblent offrir des solutions Open Source, ce qui peut être intéressant, à étudier plus tard \...

### Cas d\'utilisation 

*Provided by Charles:*

Bien sûr, il y aura différents types de personnes qui utiliseront ce logiciel et pour différentes raisons, ils peuvent peut-être avoir besoin de différentes solutions PDM, mais il serait bon d\'étudier des solutions universelles.
Je vois les méthodes différentes suivantes de développement (il doit aussi y en avoir d\'autres):

-   Les utilisateurs individuels - sont probablement un pourcentage très important de personnes travaillant de cette façon, et, ils peuvent être assez autonome, mais le contrôle de révisions et la ramification sont encore utile. Beaucoup de ces personnes peuvent travailler dans des régions du monde où l\'accès internet est parsemé ou onéreux, de sorte qu\'ils travaillent peut-être déconnectés pendant de longues périodes. Ce serait bien de faire des projets individuels très facilement reproductibles par d\'autres personnes, il s\'agit d\'un bon travail - si la conception peut évoluer dans plusieurs directions à la fois - beaucoup d\'évolutions Darwiniennes explorent des solutions dans le temps

-   De petites équipes de personnes qui travaillent ensemble - peut-être même les établissements d\'enseignement - chaque individu, peut vouloir sa propre liberté d\'exploration sur tous les aspects du projet, plutôt que d\'être affecté radicalement à une partie spécifique du projet. Nous trouvons que cela permet généralement plus d\'options, faciles à explorer, et, donne une plus grande flexibilité.

-   Plus larges conceptions des projets open source - plus de membres, et, géographiquement dispersés. Le miroir de projets de logiciels open-source - où il semble y avoir une tendance générale vers des systèmes distribués (en fait, Python [a déplacé](http://mail.python.org/pipermail/python-dev/2009-March/087931.html) plus d\'un mois de [DVCS](http://en.wikipedia.org/wiki/Data_Validation_and_Certification_Server) dernièrement). Je vois que la conception et l\'ingénierie va dans le même sens, pour les mêmes raisons. Donc, je pense qu\'il y a une raison de plus pour que nous réfléchissions sur la façon, dont un système distribué peut travailler dans la CAO (CAD) - et si nous réglons cela, nous aurons un gros avantage sur les éditeurs de CAO commerciaux ! Je suis convaincu qu\'il existe une solution (si l\'on ne s\'en sort pas, un développeur système de CAO le fera ! )

-   Projet plus hiérarchiquement rigide - il peut y avoir certains projets où les équipes préfèrent cet arrangement, mais je ne vois pas cela comme étant constructif au sein des entreprises.

#### Le site Blendswap 

[Blendswap](http://www.blendswap.com/) - leurs propres mots - sont **\"\... l\'endroit idéal pour trouver et partager des projets avec le monde entier, faites des projets impressionnants, les partager dans le plus grand dépôt Open Source 3D, les effectuer avec la géniale suite Open Source 3D, qu\'est Blender.\"**

La suite open source 3D [Blender](http://www.blender.org/) est un créateur de projets très populaire.

Bien que n\'étant pas un logiciel de CAO, il a de nombreux points qui peuvent être notés et des leçons à tirer sur la façon dont Blender et sa communauté ont fait évoluer les choses.

Blendswap est un excellent exemple de **ligne de conduite**. Je crois que les principales particularités, que nous pouvons apprendre, sont les suivantes :

-   Fournir des images détaillées sur le site. Cela permet aux visiteurs de naviguer librement, et de trouver rapidement un contenu.
-   Les modèles (fichiers blend) ont des licences claires et détaillées (ces informations sont également consultables rapidement en voyant l\'image, via le logo [Creative Commons](http://fr.wikipedia.org/wiki/Creative_Commons)).

### Possibilités de contrôler la version du système 

C\'est seulement un petit pas, que de penser au contrôle de révision, cette méthode est utilisée dans le développement de logiciels modernes. Il y a fondamentalement deux approches différentes de la matière :

-   Structurée, centrée serveur, ([Subversion](http://subversion.tigris.org/) ou [CVS](http://www.nongnu.org/cvs/)).
-   Structurée, distribuée ([Mercurial](http://www.selenic.com/mercurial/wiki/), [Bazaar](http://bazaar-vcs.org/) et [Git](http://git-scm.com/)).

Bien que les cas d\'utilisations d\'un système de demande de révision de contrôle distribué, tous nommés, ont un inconvénient majeur. Si vous clonez un dépôt, toutes les versions précédentes seront reproduites sur votre ordinateur. Qui peut, dans le cas de données de CAO, avoir un nombre conséquent de Mb. En revanche, les systèmes centrés uniquement sur serveur, vérifient la version en premier, et, donc transfèrent une somme relativement compacte de données.

### Licence

Dans un projet distribué par internet, il est nécessaire que chaque document comporte une licence claire. Encore plus important, si vous pensez à les cataloguer. Pièces détachées utilisées pour des projets (libre et non libre), et, il faut donc une licence libre, pour usage clair. Comme il y a plusieurs systèmes d\'octroi de licences, il y en a de différentes sorte, ici un ensemble de licences possibles pour les fichiers CAD :

#### Creative Commons 

Les licences CC sont très populaires pour le matériel créatif, vous pouvez trouver la description ici : [Creative Commons](http://creativecommons.org/).

#### ISO 16016 

fraganaut01 nous donne une fiche à un autre système de licences pour la CAO :

-   Droits d\'auteur par le fournisseur (pas de restrictions).
-   Reportez-vous à la protection notice [ISO16016](http://www.iso.org/iso/fr/home/store/catalogue_tc/catalogue_detail.htm?csnumber=28850) (pas de restriction particulière).
-   Confidentiel, pour usage interne uniquement. Utiliser uniquement avec obligation de confidentialité. Reportez-vous au préavis de protection [ISO16016](http://www.iso.org/iso/fr/home/store/catalogue_tc/catalogue_detail.htm?csnumber=28850).
-   Confidentiel, pour usage interne uniquement. Reportez-vous au préavis de protection [ISO16016](http://www.iso.org/iso/fr/home/store/catalogue_tc/catalogue_detail.htm?csnumber=28850).
-   Toute diffusion, uniquement avec l\'autorisation expresse de l\'auteur.

### Conception

Toutes les données de révision sont contrôlées, les catalogues, les tutoriels et ainsi de suite, ont une certaine forme de représentation dans FreeCAD.
Tout cela peut se résume sous le nom de **Ressources**. Il doit y avoir une **class design** pour contenir ce genre d\'informations sur les ressources, et, de distinguer les différents cas.

### Architecture

Cette cinématique de services est par définition uniquement locale, sur la machine de l\'utilisateur. Le niveau plus haut, se trouve dans le [Cloud Computing](http://en.wikipedia.org/wiki/Cloud_computing), mis en œuvre sur les différents services, sur les différents serveurs.
Il faut distinguer quatre types de serveurs :

-   Serveur bon marché - [LaMp](http://wiki.debian.org/LaMp).
-   Serveur complet - (par exemple serveurs [Ubuntu](http://ubuntu-fr.org/) / [Debian](http://www.debian.org/index.fr.html)).
-   Serveur de téléchargement - par exemple [sf.net](https://sourceforge.net/).
-   [BitTorrent](http://en.wikipedia.org/wiki/BitTorrent_(protocol)) tracker.

Ce qui nous conduit au scénario suivant :

<img alt="" src=images/ResourceFramework.png  style="width:1000px;">

## Organisation

### Recherche

Tout d\'abord, les différentes alternatives des systèmes de contrôle de révision, doivent être testés, pour obtenir des chiffres plus précis sur la façon dont ils se comportent sur les données de CAO.

### Design

Une **class design** pour le Resource framwork.

## Actions suivantes 

-   Construire des référentiels de tests sur le serveur, et deux machines locales.
-   Testez les différents cas d\'utilisation.



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
