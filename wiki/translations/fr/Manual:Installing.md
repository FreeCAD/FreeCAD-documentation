





{{Manual:TOC/fr}}

FreeCAD utilise la licence [LGPL](https://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_limit%C3%A9e_GNU), ce qui vous permet de télécharger, installer, redistribuer et utiliser FreeCAD comme vous le souhaitez, quel que soit le type de travail que vous allez faire avec (commercial ou non commercial). Vous n\'êtes lié à aucune clause ou restriction, et les fichiers que vous produirez avec sont entièrement à vous. La seule chose que la licence interdit, en réalité, est de prétendre que vous avez programmé FreeCAD vous-même !

FreeCAD fonctionne sans aucune différence sur Windows, Mac OS et Linux. Cependant, les méthodes d\'installation diffèrent légèrement selon votre plate-forme. Sur Windows et Mac, la communauté FreeCAD fournit des paquets précompilés (installeurs) prêts à télécharger, alors que sous Linux, le code source est mis à la disposition des responsables de distribution de Linux, qui sont responsables de packaging de FreeCAD pour leur distribution spécifique. Par conséquent, sur Linux, vous pouvez généralement installer FreeCAD directement à partir de l\'application du gestionnaire de logiciels.

La page de téléchargement officielle de FreeCAD pour Windows et Mac OS est <https://github.com/FreeCAD/FreeCAD/releases>

**Versions de FreeCAD**

Les versions officielles de FreeCAD, que vous pouvez trouver sur la page ci-dessus et dans le gestionnaire de logiciels de votre distribution, sont des versions stables. Cependant, le développement de FreeCAD est rapide! De nouvelles fonctionnalités et des corrections de bogues sont ajoutées presque tous les jours. Puisque cela peut parfois prendre beaucoup de temps entre deux versions stables, vous pourriez être intéressé par essayer une version en cours de développement de FreeCAD. Ces versions, ou pré-versions, sont mises à disposition régulièrement sur la page de téléchargement mentionnée ci-dessus ( [download page](https://github.com/FreeCAD/FreeCAD/releases) ) ou, si vous utilisez Ubuntu, la communauté FreeCAD gère également [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Personal Package Archives) ou «daily builds (états d\'avancement quotidiens)» régulièrement mis à jour avec les changements les plus récents.

Si vous installez FreeCAD dans une machine virtuelle, sachez que la performance peut être ralentie ou, dans certains cas, inutilisable en raison des limites du support [OpenGL](https://fr.wikipedia.org/wiki/OpenGL) de la plupart des machines virtuelles.

### Installation sur Windows 

1.  Téléchargez un package d\'installation (.exe) correspondant à votre version de Windows (32 bits ou 64 bits) à partir de la page de téléchargement ([download page](https://github.com/FreeCAD/FreeCAD/releases)). Les installeurs FreeCAD devraient fonctionner sur n\'importe quelle version à partir de Windows 7.
2.  Double-cliquez sur le programme d\'installation téléchargé.
3.  Acceptez les termes de la licence LGPL (ce sera l\'un des rares cas où vous pouvez vraiment cliquer sur le bouton \"accepter\" sans lire le texte. Pas de clauses cachées) : ![](images/Freecad-windows-install-01.jpg )
4.  Vous pouvez laisser ici le chemin par défaut ou le modifier si vous le souhaitez: ![](images/Freecad-windows-install-02.jpg )
5.  Il n\'est pas nécessaire de définir la variable PYTHONPATH, sauf si vous prévoyez faire des améliorations en programmation Python, dans ce cas, vous savez probablement déjà pourquoi : ![](images/Freecad-windows-install-03.jpg )
6.  Pendant l\'installation, un certain nombre de composants supplémentaires, qui sont regroupés à l\'intérieur de l'installeur, sera installé aussi : ![](images/Freecad-windows-install-04.jpg )
7.  Ça y est, FreeCAD est installé. Vous le trouverez dans votre menu de démarrage. ![](images/Freecad-windows-install-05.jpg )

**Installation d\'une version de développement**

La réalisation du package FreeCAD et la création d\'un installeur prend du temps et du dévouement, de sorte que les versions de développement (également appelées pré-versions) sont fournies sous forme d\'archives .zip (ou .7z). Celles-ci n\'ont pas besoin d\'être installées, il suffit de les décompresser et de lancer FreeCAD en double-cliquant sur le fichier FreeCAD.exe que vous trouverez à l\'intérieur. Cela vous permet également de conserver à la fois les versions stable et \"instable\" sur le même ordinateur.

### Installation sur Linux 

Sur la plupart des distributions Linux modernes (Ubuntu, Fedora, openSUSE, Debian, Mint, Elementary, etc.), FreeCAD peut être installé en un bouton, directement à partir de l\'application de gestion de logiciels fournie par votre distribution (l\'aspect peut différer des images ci-dessous, chaque distribution utilise son propre outil).

1.  Ouvrez le gestionnaire de logiciels et recherchez \"freecad\":
    <img alt="" src=images/Freecad-linux-install-01.jpg  style="width:800px;">
2.  Cliquez sur le bouton \"installer\" et c\'est tout, FreeCAD s'installe. N\'oubliez pas de noter ensuite! <img alt="" src=images/Freecad-linux-install-02.jpg  style="width:800px;">

**Modes alternatifs**

Un des gros avantages de l\'utilisation sous Linux ce sont les nombreuses possibilités d\'adapter votre logiciel. Ne vous en privez donc pas. Sous Ubuntu et ses dérivés, FreeCAD peut également être installé à partir d\'un [PPA](https://launchpad.net/~freecad-maintainers) maintenu par la communauté FreeCAD (il contient à la fois les versions stables et de développement). Sous Fedora, les versions récentes de développement peuvent être installées à partir de [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/), et comme il s\'agit de logiciels open-source, vous pouvez également compiler FreeCAD vous-même ( [ Compiler](Compiling/fr.md)).

### Installation sur Mac OS 

L\'installation de FreeCAD sur Mac OSX est aujourd\'hui aussi simple que sur d\'autres plates-formes. Cependant, étant donné qu\'il y a moins de gens dans la communauté qui possèdent un Mac, les paquets disponibles sont souvent en retard de quelques versions derrière les autres plates-formes.

1.  Téléchargez un package compressé correspondant à votre version à partir de la page de téléchargement ( [download page](https://github.com/FreeCAD/FreeCAD/releases)).
2.  Ouvrez le dossier Téléchargements et développez le fichier zip téléchargé: ![](images/Freecad-mac-01.jpg )
3.  Faites glisser l\'application FreeCAD de l\'intérieur du zip vers le dossier Applications : ![](images/Freecad-mac-02.jpg )
4.  Ça y est, FreeCAD est installé ! ![](images/Freecad-mac-03.jpg )
5.  Si le système empêche FreeCAD de se lancer, en raison des autorisations restreintes pour les applications ne provenant pas de l\'App Store, vous devrez l\'activer dans les paramètres du système : ![](images/Freecad-mac-04.jpg )

### Désinstallation

Espérons que vous ne voudrez pas désinstaller FreeCAD néanmoins il est bon de savoir comment faire. Sur Windows et Linux, la désinstallation de FreeCAD est très simple. Sur Windows, utilisez l\'option classique \"supprimer logiciel\" qui se trouve dans le panneau de contrôle. Sur Linux, supprimez-le avec le même gestionnaire de logiciels que vous avez utilisé pour l\'installer. Sur Mac, tout ce que vous devez faire est de l\'enlever du dossier Applications.

### Définir les préférences de base 

Une fois que FreeCAD est installé, vous voudrez peut-être l\'ouvrir et définir quelques préférences. Les paramètres de préférences dans FreeCAD se trouvent sous menu **Edit → Preferences**. Sont listées un certain nombre de préférences de base que vous pourriez aimer changer. Vous avez la possibilité de parcourir les différentes pages pour voir s\'il y a autre chose que vous voudriez changer.

1.  **Langue** : (onglet *General*, catégorie *General*) FreeCAD choisira automatiquement la langue de votre système d\'exploitation, mais vous pourriez vouloir changer cela. FreeCAD est presque entièrement traduit en 5 ou 6 langues, plus beaucoup d\'autres qui ne sont actuellement traduites que partiellement. Vous pouvez facilement [aider à traduire FreeCAD](https://crowdin.com/project/freecad). ![](images/Freecad-basic-options01.jpg )
2.  **Module de chargement automatique** : (onglet *General*, catégorie *Démarrage*) Normalement, FreeCAD commencera en vous montrant la page centrale de démarrage. Vous pouvez la sauter et commencer une session FreeCAD directement dans l\'atelier de votre choix, listé à la ligne \"Charger automatiquement le module après le démarrage\". Les [ateliers](Workbenches/fr.md) seront expliqués en détail dans le [chapitre suivant](Manual:The_FreeCAD_Interface/fr.md).
3.  **Créer un document au démarrage** : (onglet *Document*, catégorie *General*) combiné à la précédente option \"Module de chargement automatique\", si cette case est cochée alors FreeCAD est prêt à fonctionner. ![](images/Freecad-basic-options02.jpg )
4.  **Options de stockage** : (onglet *Document*, catégorie *Stockage*) en tant qu\'application complexe, FreeCAD peut s\'interrompre du fait de bugs. Ici, vous pouvez configurer quelques options qui vous aideront à récupérer votre travail en cas de crash.
5.  **Autorisation et licence** : (onglet *Document*, catégorie *Création et Licence*) ici vous pouvez définir les paramètres par défaut qui seront utilisés pour vos nouveaux fichiers. Pensez à rendre vos fichiers partageables dès leur création, en utilisant une licence copyleft comme [copyleft](https://fr.wikipedia.org/wiki/Copyleft) licence like [Creative Commons](https://creativecommons.org/).
6.  **Rediriger les messages internes Python** vers la sortie : (onglet *Fenêtre de sortie*, catégorie *Interpréteur python*) ces deux options sont toujours bonnes à cocher, car elles vous permettront de voir ce qui ne va pas dans [La vue rapport](Manual:The_FreeCAD_Interface#Report_view/fr.md) quand il y a un problème avec l\'exécution d\'un script python particulier. ![](images/Freecad-basic-options03.jpg )
7.  **Unités** : (onglet *Unités*) ici, vous pouvez définir le système d\'unités par défaut que vous souhaitez utiliser. ![](images/Freecad-basic-options04.jpg )
8.  **Zoom au curseur**: (catégorie \'\' Affichage \'\', onglet \'\' Vue 3D \'\') Si cette option est définie, les opérations de zoom se feront sur le pointeur de la souris. Si l\'option n\'est pas défini, le centre de la vue en cours est la mise au point du zoom.
9.  **Inverser le zoom**: (catégorie \'\' Affichage \'\', onglet \'\' Vue 3D \'\') Inverse le sens du zoom par rapport au mouvement de la souris. ![](images/_FreeCAD-v0-18-Preferences-Display.png )

### Installation de contenu supplémentaire 

À mesure que le projet FreeCAD et sa communauté augmentent rapidement, et aussi parce qu\'il est facile de l\'améliorer, les contributions externes et les projets parallèles réalisés par les membres de la communauté et les autres amateurs commencent à apparaître partout sur Internet. La plupart des projets externes sont des ateliers ou des macros et peuvent facilement s\'intaller depuis FreeCAD via le [Gestionnaire d\'extensions](AddonManager/fr.md) situé sous le menu **Outils**. Le gestionnaire des addons vous permettra d\'installer de nombreuses options telles que:

1.  Une [bibliothèque de pièces](https://github.com/FreeCAD/FreeCAD-library) qui contient toutes sortes de modèles utiles ou des modèles créés par des utilisateurs FreeCAD et qui peuvent être utilisés librement dans vos projets. La bibliothèque peut être utilisée et accessible directement depuis votre installation FreeCAD.
2.  Une [collection de greffons](https://github.com/FreeCAD/FreeCAD-addons) (addons) qui étend les fonctionnalités de la plupart des ateliers supplémentaires de FreeCAD pour certaines tâches. Les instructions d\'installation sont fournies pour chaque atelier lorsque vous venez à cliquer sur le lien du greffon correspondant.
3.  Une [collection de macros](https://github.com/FreeCAD/FreeCAD-macros) également disponible sur le [wiki FreeCAD ](Macros_recipes/fr.md) ainsi que des informations sur la façon de les utiliser.

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">

Si vous utilisez Ubuntu, certains des greffons cités au-dessus sont disponibles dans les packages [FreeCAD addons PPA](https://launchpad.net/freecad-extras).

**Lire plus d\'informations**

-   [Plus d\'options de téléchargement](Download/fr.md)
-   [Dépôt FreeCAD pour Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [Dépôt de greffons FreeCAD pour Ubuntu](https://launchpad.net/freecad-extras)
-   [Compilez FreeCAD vous-même](Compiling/fr.md)
-   [Traductions FreeCAD](https://crowdin.com/project/freecad)
-   [Page du github FreeCAD](https://github.com/FreeCAD)




[Category:Poweruser Documentation{{\#translation:}}](Category:Poweruser_Documentation.md) [Category:Tutorials{{\#translation:}}](Category:Tutorials.md)
