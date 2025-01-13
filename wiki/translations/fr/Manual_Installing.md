# Manual:Installing/fr
{{Manual:TOC}}

FreeCAD est sous licence [LGPL](https://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_limit%C3%A9e_GNU), ce qui vous permet de le télécharger, de l\'installer, de le redistribuer et de l\'utiliser à toutes fins, commerciales ou non, sans aucune restriction. Vous conservez l\'entière propriété des fichiers que vous créez.

FreeCAD fonctionne de manière identique sur Windows, macOS et Linux, bien que le processus d\'installation varie en fonction de la plateforme. Pour les utilisateurs de Windows et de Mac, la communauté FreeCAD propose des installateurs précompilés prêts à l\'emploi. Sous Linux, le code source est fourni aux responsables des distributions qui compilent le logiciel pour leurs systèmes spécifiques. En général, les utilisateurs de Linux peuvent installer FreeCAD directement via le gestionnaire de logiciels de leur système.

La page officielle de téléchargement de FreeCAD se trouve à l\'adresse la [FreeCAD page de téléchargement](https://www.freecad.org/downloads.php). Des informations supplémentaires sur le processus d\'installation sont disponibles sur le [wiki de téléchargement](https://wiki.freecad.org/Download/fr) dédié.

**Versions de FreeCAD**

Les versions stables officielles de FreeCAD sont disponibles sur la page de téléchargement référencée et dans le gestionnaire de logiciels de votre distribution. Cependant, le rythme de développement de FreeCAD est soutenu, avec de nouvelles fonctionnalités et des corrections de bogues incorporées presque quotidiennement. En raison des périodes prolongées entre les versions stables, vous pouvez vouloir expérimenter avec des versions plus récentes de FreeCAD. Ces versions de développement, ou pré-versions, peuvent être trouvées sur la même page de téléchargement. Pour les utilisateurs d\'Ubuntu ou de Fedora, la communauté FreeCAD fournit également des \"versions de développement\" sur le [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Personal Package Archives) et le [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/), régulièrement mis à jour.

Si vous envisagez d\'installer FreeCAD sur une machine virtuelle, sachez que ses performances peuvent être considérablement réduites, voire inutilisables, en raison de la prise en charge limitée d\'OpenGL dans de nombreuses machines virtuelles.



### Installation sur Windows 

1.  Téléchargez un programme d\'installation (.exe) à partir de la page de téléchargement. Les programmes d\'installation de FreeCAD devraient fonctionner sur n\'importe quelle version de Windows à partir de Windows 7.
2.  Acceptez les termes de la licence LGPL. C\'est l\'un des rares cas où vous pouvez vraiment cliquer sur le bouton « accepter » sans lire le texte. Pas de clauses cachées : ![](images/LicenseAgreement_0212.jpeg )
3.  Vous pouvez laisser le chemin d\'accès par défaut ici, ou le changer si vous le souhaitez : ![](images/Path0212.jpeg )
4.  Assurez-vous de cocher tous les composants à installer : ![](images/Components0212.jpeg )
5.  C\'est tout. L\'installation est maintenant terminée et vous pouvez commencer à explorer les possibilités de FreeCAD.

**Installation d\'une version de développement**

La livraison de FreeCAD et le développement d\'un programme d\'installation impliquent un investissement considérable en temps et en efforts. C\'est pourquoi les versions de développement (également appelées pré-versions) sont généralement livrées sous la forme d\'archives .zip ou .7z situées sur la [page de téléchargement de FreeCAD](https://www.freecad.org/downloads.php). Il n\'est pas nécessaire de procéder à une installation formelle avec ces fichiers. Il suffit d\'en extraire le contenu et de lancer FreeCAD en double-cliquant sur le fichier FreeCAD.exe qui se trouve à l\'intérieur. Cette approche vous permet également de maintenir la version stable et la version « instable » sur le même ordinateur. C\'est comme si vous aviez dans votre garage une voiture de tous les jours et un jet pack expérimental !



### Installation sur Linux 

Pour les utilisateurs des distributions Linux modernes telles qu\'Ubuntu, Fedora, openSUSE, Debian, Mint et Elementary, l\'installation de FreeCAD est aussi simple qu\'un simple clic. Vous pouvez l\'installer de manière transparente via l\'outil de gestion des logiciels fourni par votre distribution, bien que l\'apparence de ces outils puisse différer des images d\'illustration puisque chaque distribution utilise sa propre application.

1.  Ouvrez le gestionnaire de logiciels et recherchez \"freecad\" :
2.  Cliquez sur le bouton \"installer\" et c\'est tout, FreeCAD s'installe. N\'oubliez pas de noter ensuite!
    <img alt="" src=images/linuxInstallation.png  style="width:800px;">

**Modes alternatifs**

Un des gros avantages de l\'utilisation sous Linux ce sont les nombreuses possibilités d\'adapter votre logiciel, alors ne vous retenez pas. Pour les utilisateurs d\'Ubuntu et de ses dérivés, FreeCAD peut être installé à partir d\'un [PPA](https://launchpad.net/~freecad-maintainers) maintenue par la communauté FreeCAD, qui comprend à la fois des versions stables et des versions de développement. Sur Fedora, vous pouvez accéder aux dernières versions de développement de FreeCAD via [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/). De plus, comme FreeCAD est un logiciel libre, vous avez la liberté de [compiler FreeCAD vous-même](Compiling/fr.md).



### Installation sur Mac OS 

L\'installation de FreeCAD sur Mac OSX est aujourd\'hui aussi simple que sur d\'autres plates-formes. Cependant, étant donné qu\'il y a moins de gens dans la communauté qui possèdent un Mac, les paquets disponibles sont souvent en retard de quelques versions derrière les autres plates-formes.

1.  Téléchargez un package compressé correspondant à votre version.
2.  Ouvrez le dossier Téléchargements et développez le fichier zip téléchargé: ![](images/Freecad-mac-01.jpg )
3.  Faites glisser l\'application FreeCAD de l\'intérieur du zip vers le dossier Applications : ![](images/Freecad-mac-02.jpg )
4.  Ça y est, FreeCAD est installé ! ![](images/Freecad-mac-03.jpg )
5.  Si le système empêche FreeCAD de se lancer, en raison des autorisations restreintes pour les applications ne provenant pas de l\'App Store, vous devrez l\'activer dans les paramètres du système : ![](images/Freecad-mac-04.jpg )



### Désinstallation

Idéalement, vous ne voudrez jamais vous séparer de FreeCAD, mais si vous devez le désinstaller, sachez que la procédure est simple.

-   Sous Windows, utilisez l\'option familière « supprimer un logiciel » du panneau de configuration.
-   Pour les utilisateurs de Linux, désinstallez le logiciel à l\'aide du gestionnaire de logiciels que vous avez utilisé pour l\'installer.
-   Les utilisateurs de Mac ont la tâche la plus facile : il suffit de faire glisser FreeCAD du dossier Applications vers la corbeille.



### Définir les préférences de base 

Après avoir installé FreeCAD, vous souhaiterez probablement le personnaliser en ajustant certains paramètres. Vous pouvez trouver les paramètres de préférences dans FreeCAD en faisant *Édition → Préférences*. Vous trouverez ci-dessous quelques paramètres de base que vous pourriez envisager de modifier immédiatement, mais n\'hésitez pas à explorer les différentes pages de préférences pour adapter le logiciel à vos besoins.



#### Catégorie générale, onglet Général 

![](images/FreeCAD_022_GeneralGen.png )

1.  **Langue** : par défaut, FreeCAD sélectionnera la langue de votre système d\'exploitation, mais vous avez la possibilité de la changer. Grâce à la contribution de nombreux contributeurs, FreeCAD est disponible dans un large éventail de langues.
2.  *\'Unités*: ce paramètre vous permet de choisir le système d\'unités par défaut pour vos projets.



#### Catégorie Général, onglet Document 

![](images/FreeCAD_022_GeneralDoc.png )

1.  **Créer un nouveau document au démarrage** : FreeCAD ouvrira automatiquement un nouveau document à chaque démarrage du programme.
2.  **Stockage** : configurez ici les paramètres pour vous aider à récupérer votre travail en cas de crash.
3.  **Création et licence** : dans cette zone, vous pouvez déterminer les paramètres pour les nouveaux fichiers. Pour faciliter le partage, vous pouvez commencer par une licence plus permissive, avec une licence copyleft telle que la Creative Commons.



#### Catégorie Affichage, onglet Navigation 

![](images/FreeCAD_022_DisplayNav.png )

1.  **Zoomer sur le curseur** : lorsque cette option est activée, les actions de zoom sont centrées sur le curseur de la souris. Si elle est désactivée, le zoom se concentre sur le centre de la vue.
2.  **Inverser le zoom** : cette option inverse la direction du zoom par rapport au mouvement de la souris.



#### Onglet Ateliers 

![](images/FreeCAD_022_WBMenu.png )

Bien que FreeCAD s\'ouvre généralement sur la page d\'accueil, ce paramètre vous permet de l\'ignorer. Vous pouvez démarrer directement dans l\'atelier de votre choix. En outre, vous pouvez personnaliser les postes de travail affichés dans le menu de sélection.



#### Onglet Importer/Exporter 

![](images/FreeCAD_022_ImportExport.png )

Cette section permet de définir les paramètres de base pour l\'importation et l\'exportation dans différents formats.



### Installation de contenu supplémentaire 

Au fur et à mesure que la communauté FreeCAD s\'agrandit et que la facilité de personnalisation augmente, de nombreuses contributions externes et des projets secondaires réalisés par des membres de la communauté commencent à apparaître. Beaucoup de ces projets prennent la forme d\'ateliers ou de macros, et vous pouvez facilement les ajouter à votre boîte à outils via le [gestionnaire des extensions](Std_AddonMgr/fr.md), accessible depuis le menu Outils. Le gestionnaire des extensions vous ouvre un monde de possibilités, vous permettant d\'installer divers composants intéressants, tels que : ![](images/FreeCAD_022_AddonsMenu.png )

<img alt="" src=images/FreeCAD_022_AddonsMenu.png  style="width:600px;">

1.  Une [bibliothèque de pièces](https://github.com/FreeCAD/FreeCAD-library). Cette bibliothèque est un trésor de modèles utiles ou de fragments de modèles créés par les utilisateurs de FreeCAD. Tous les éléments de cette bibliothèque sont disponibles gratuitement pour être utilisés dans vos projets et sont accessibles directement dans votre configuration FreeCAD.
2.  Des [ateliers en plus](https://github.com/FreeCAD/FreeCAD-addons). Il s\'agit d\'extensions spécialisées qui améliorent les fonctionnalités de FreeCAD pour des tâches spécifiques. Les exemples d\'applications comprennent l\'animation de pièces de modèles ou la gestion de processus de construction spécifiques tels que le pliage de tôles ou la modélisation des données du bâtiment (BIM). Des informations détaillées sur chaque atelier, y compris une vue d\'ensemble des outils qu\'il contient, sont fournies sur la page de chaque extension, accessible par le lien correspondant dans le gestionnaire des extensions.
3.  Une large gamme de [macros](https://github.com/FreeCAD/FreeCAD-macros) est également disponible au téléchargement. Celles-ci peuvent considérablement rationaliser votre flux de travail, et une documentation détaillée sur la façon de les utiliser peut être trouvée sur le [wiki de FreeCAD](Macros_recipes/fr.md).

À partir de FreeCAD v0.17.9940, la méthode d\'installation recommandée pour tous les outils ci-dessus est le gestionnaire des extensions intégré. Cependant, si pour une raison quelconque cette option n\'est pas disponible, une installation manuelle est toujours possible. Pour plus d\'informations, consultez la [FreeCAD page des extensions](https://github.com/FreeCAD/FreeCAD-addons).

**Lire plus d\'informations**

-   [Plus d\'options de téléchargement](Download/fr.md)
-   [Dépôt FreeCAD pour Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [Dépôt des extensions de FreeCAD pour Ubuntu](https://launchpad.net/freecad-extras)
-   [Compilez FreeCAD vous-même](Compiling/fr.md)
-   [Traductions FreeCAD](https://crowdin.com/project/freecad)
-   [Page du github FreeCAD](https://github.com/FreeCAD)
-   [Gestionnaire des extensions de Freecad](Std_AddonMgr/fr.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/fr
