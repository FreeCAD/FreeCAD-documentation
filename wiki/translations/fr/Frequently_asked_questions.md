# Frequently asked questions/fr
Cette page tente de répondre aux questions les plus fréquemment posées sur les forums FreeCAD.

Si vous avez un problème ou une question concernant FreeCAD, vérifiez ci dessous avant tout. Puis, si vous ne trouvez pas de réponse à votre question, allez voir et au besoin poster sur le [forum de FreeCAD](http://forum.freecadweb.org/viewforum.php?f=3) !

## Installation

### Quel est le moyen le plus facile, pour installer FreeCAD sur mon système ? 

Si vous êtes sous Windows ou macOS, le moyen le plus simple est de vous rendre sur la page [Téléchargements](Download/fr.md), où vous trouverez plusieurs packages prêts à installer. Si vous êtes sur Debian, Fedora ou Ubuntu et d\'autres distributions, FreeCAD est déjà inclus dans les référentiels de logiciels standard et vous pouvez simplement l\'installer avec le gestionnaire de logiciels. Sur Ubuntu, l\'équipe FreeCAD maintient également ses propres [dépôts PPA](Installing_on_Linux/fr#PPA_stable.md). Pour plus de détails sur l\'installation, reportez-vous à la page d\'installation de votre système d\'exploitation ([Windows](Installing_on_Windows/fr.md), [Linux](Installing_on_Linux/fr.md) ou [Mac](Installing_on_Mac/fr.md)).

### Quelles sont les conditions requises pour l\'exécution de FreeCAD ? 

Contrairement à la plupart des logiciels de CAO 3D, FreeCAD peut fonctionner correctement sur les ordinateurs les plus modestes - il est connu pour fonctionner sur les processeurs Pentium IV et Intel Core2 Solo. Si votre ordinateur exécute un système d\'exploitation récent, il y a de fortes chances que FreeCAD s\'exécute. La seule condition préalable est que votre carte graphique ou chipset prenne en charge [OpenGL](https://fr.wikipedia.org/wiki/OpenGL), de préférence pas plus ancien que v2.0. En cas de problème, reportez-vous à la section [Dépannage](Frequently_asked_questions/fr#D.C3.A9pannage.md) de cette FAQ.

#### Multithreading

Le noyau de modélisation géométrique sous-jacent de FreeCAD, la bibliothèque tierce [Technologie OpenCASCADE](https://fr.wikipedia.org/wiki/Open_CASCADE_Technology) (OCCT), [ne prend en charge que partiellement le multithreading pour le moment](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501&p=173095&hilit=Multithread#p173095). Voir la page [multithreading](Multithreading/fr.md) pour plus de détails.

#### Pour les utilisateurs Mac 

Seulement l\'architecture MacIntel est prise en charge. Il n\'y a aucune version disponible pour l\'architecture PowerPC.

### Que faire si je veux compiler FreeCAD moi-même ? 

Le code source de FreeCAD est toujours disponible dans le répertoire du code source du projet. Compiler vous-même avec FreeCAD vous permet d'utiliser les dernières fonctionnalités en cours de développement mais nécessite quelques connaissances informatiques, bien que la procédure soit relativement simple. L\'accès au code source est expliqué [ici](Compile_on_Linux/fr#Obtenir_le_code_source.md) et ici des instructions détaillées pour la compilation sur [Windows](Compile_on_Windows/fr.md), [Linux](Compile_on_Linux/fr.md) et [macOS](Compile_on_MacOS/fr.md).

### FreeCAD me signale que certains modules ou applications sont manquants 

FreeCAD dépend de beaucoup de choses pour offrir toutes ses fonctionnalités. Tous les principaux composants requis sont généralement regroupés dans votre installation FreeCAD ou fournis par votre gestionnaire de packages, donc normalement vous n\'avez pas à vous inquiéter. Cependant, si vous avez installé FreeCAD à partir de sources non officielles ou compilé FreeCAD vous-même, une partie peut manquer, ce qui n\'est pas critique pour FreeCAD lui-même, mais peut entraîner l\'indisponibilité de certaines fonctionnalités. Certains formats de fichiers spécifiques tels que Collada ou DWG nécessitent également des composants supplémentaires, qui ne peuvent pas être regroupés dans FreeCAD, et doivent être installés par vous-même séparément.

Tous ces composants et la manière appropriée de les installer sont listés sur la page [Modules Python supplémentaires](Extra_python_modules/fr.md).

## Dépannage

### FreeCAD ne démarre pas du tout 

Il peut y avoir de nombreuses raisons à cela, la plus probable est que certaines bibliothèques sont manquantes. Essayez de démarrer FreeCAD à partir d\'un terminal (saisir {{SystemInput|freecad}} après le prompt, {{SystemInput|FreeCAD}} sur certains systèmes) pour voir si un message d\'erreur apparaît. Lisez aussi le reste de cette FAQ car cela peut vous donner divers indices pour détecter la cause du problème. Si rien n\'y fait, parlez en sur le [forum](http://forum.freecadweb.org/), il y aura sûrement quelqu\'un qui pourra vous aider.

Sur certains systèmes Windows XP plus anciens, vous pouvez recevoir un message d\'erreur comme celui-ci: **L'application ne peut pas démarrer, car la configuration côte à côte est incorrecte. La réinstallation de l'application peut résoudre le problème.** La raison de ce problème est que sur votre système, soit les bibliothèques d\'exécution CRT sont manquantes, soit la version installée est trop ancienne car FreeCAD était lié à une version plus récente. Dans ce cas, vous devez installer le **Microsoft Visual C++ Redistributable Package** que vous trouverez chez Microsoft. Voir aussi le [message de forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=1298&p=9961) correspondant.

### FreeCAD démarre normalement, mais toutes les icônes ne sont pas affichées, certaines d\'entre elles sont remplacées par un \'X\' noir 

Certaines parties de FreeCAD dépendent d\'un module Python externe appelé Pivy. Sous Windows, pivy est inclus dans l\'installation de FreeCAD. Sur les systèmes Debian/Ubuntu, le paquet python-pivy fait partie des dépôts de logiciels standard. Sur d\'autres systèmes, pour le moment, vous devrez peut-être compiler vous-même. Notez que bien que certains outils ne soient pas disponibles sans pivy, le reste de FreeCAD fonctionne normalement.

### J\'ai des problèmes d\'affichage, la vue 3D ne se comporte pas correctement, il y a des résidus, trainées quand je bouge/fait pivoter la vue, etc. 

FreeCAD dépend d\'OpenGL pour afficher le contenu 3D et nécessite donc un environnement OpenGL fonctionnel. Sur certains systèmes, OpenGL n\'est pas activé par défaut et vous devrez peut-être installer ou mettre à niveau vos pilotes graphiques. Ces problèmes surviennent le plus souvent sur les systèmes Linux ou sur les systèmes virtuels. Si vous utilisez un système Linux, essayez les étapes suivantes:

-   vérifiez que votre ordinateur dispose d\'une carte graphique compatible 3D
-   tapez {{SystemInput|glxinfo}} dans une fenêtre de terminal, et vérifiez dans la sortie que Direct Rendering est réglé sur \"yes\" et que le fournisseur/moteur de rendu/version d\'OpenGL correspond à votre carte graphique.
-   installez un autre logiciel basé sur OpenGL ([Blender](http://www.blender.org), par exemple) et vérifiez s\'il fonctionne et s\'affiche correctement.

### FreeCAD plante au démarrage 

Un plantage peut indiquer un bogue plus grave ou un problème dans votre configuration. La plupart des plantages au démarrage se produisent pour l\'une des deux raisons suivantes :

#### Les pilotes OpenGL ne sont pas installés, ou ne fonctionnent pas correctement 

C\'est une cause très courante du problème. Les symptômes sont simplement que FreeCAD se bloque au démarrage, ou chaque fois que vous ouvrez une vue 3D (par exemple en créant un nouveau document). Essayez de découvrir quelle est votre puce graphique, puis découvrez si elle prend en charge [OpenGL](https://fr.wikipedia.org/wiki/OpenGL) (les puces les plus récentes le font), puis trouvez le pilote approprié et installez-le. Un bon moyen de vérifier si OpenGL est disponible est d\'essayer d\'exécuter une autre application OpenGL telle que [blender](http://www.blender.org).

Et comme astuce générale pour obtenir plus d\'informations sur les plantages avec FreeCAD, vous pouvez le démarrer avec le paramètre de programme {{SystemInput|--write-log}}. Cela créera le fichier **FreeCAD.log** dans **$XDG_CONFIG_HOME/FreeCAD** (<small>(v0.20)</small> ) ou **$HOME/.FreeCAD** ({{VersionMinus/fr|0.19}}) sur Linux, ou **$HOME/Library/Preferences/FreeCAD** sur macOS, ou **%APPDATA%/FreeCAD** sur les systèmes Windows.

Dans certains cas rares, vous pouvez avoir un pilote graphique installé qui ne correspond pas à votre carte graphique. Nous avons eu un cas où l\'ordinateur portable de l\'utilisateur avait un graphique Intel intégré, mais certains pilotes ATI ont été installés. [1](http://forum.freecadweb.org/viewtopic.php?f=13&t=5160&start=10#p41042) Après avoir supprimé les fichiers et réinstallé le pilote correct, FreeCAD a commencé à fonctionner.

#### Certaines bibliothèques nécessaires à FreeCAD, ne sont pas présentes sur votre système, ou n\'ont pas été trouvées par FreeCAD 

Il peut y avoir deux possibilités à ce problème: soit une bibliothèque manque simplement, donc FreeCAD refusera de démarrer, soit la bibliothèque est là, mais il s\'agit d\'une version plus ancienne que celle attendue par FreeCAD, donc un crash se produira lorsque FreeCAD tente de utiliser une fonctionnalité manquante de cette bibliothèque. Un exemple courant est que lorsque Qt3 et Qt4 sont installés sur votre système, FreeCAD peut détecter Qt4 mais si votre installation Qt n\'est pas correctement configurée, certains morceaux de Qt3 peuvent encore être utilisés, provoquant des plantages.

Veuillez revoir la procédure d\'installation ([Windows](Installing_on_Windows/fr.md), [Linux](Installing_on_Linux/fr.md) ou [Mac](Installing_on_Mac/fr.md)), assurez-vous d\'avoir installé toutes les bibliothèques requises (sur la plupart des systèmes Linux, cela se fait automatiquement), et vérifiez quel est le numéro de version minimum pour chacun des composants.

Si tout semble correct, décrivez le problème sur le [forum](http://forum.freecadweb.org/) ou [soumettre un bogue](Tracker/fr.md). Si vous êtes sur un système Linux, il est facile de faire un backtrace de débogage, qui fournit des informations très utiles sur le crash aux développeurs:

-   dans un terminal, tapez: {{SystemInput|gdb freecad}} (en supposant que le package gdb est installé)
-   dans gdb, tapez {{SystemInput|run}}
-   après le plantage, tapez {{SystemInput|bt}} pour obtenir le backtrace, que vous pouvez inclure dans votre rapport de bogue.

### FreeCAD se bloque après le démarrage 

Au démarrage de FreeCAD, l\'interface graphique apparaît presque immédiatement mais l\'interface graphique est figée et le processeur est à environ 99%. Cela peut se produire sur le bureau KDE lors de l\'utilisation du thème Oxygen. C\'est un bogue dans le thème Oxygen et le choix d\'un autre thème devrait résoudre ce problème.

### Plantage de FreeCAD à la création d\'un nouveau document ou à l\'ouverture d\'un fichier 

Si FreeCAD plante lors de la création d\'une nouvelle vue 3D, essayez de lancer FreeCAD à partir d\'un terminal. Si un message d\'erreur apparaît lors de la panne, mentionnant {{SystemOutput|Assertion Failed}} et un nom de composant commençant par \"So\" ({{SystemOutput|SoBase}}, {{SystemOutput|SoFieldContainer}}, etc.), les chances sont très élevées, surtout si vous êtes sous Linux, que FreeCAD essaie d\'utiliser deux versions différentes de la bibliothèque Coin, ce qui provoque le crash. Pour vérifier si tel est bien le problème, essayez ce qui suit:

-   Localisez l\'exécutable FreeCAD (généralement dans **/usr/lib/FreeCAD/bin**)
-   Exécutez la commande {{SystemInput|ldd FreeCAD}} depuis un terminal
-   Notez la version de la bibliothèque **libCoin.so** utilisée par FreeCAD (par exemple **libCoin.so.60**)
-   Localisez la bibliothèque **libSoQt.so** (généralement dans **/usr/lib**)
-   exécutez {{SystemInput|ldd libSoQt.so}} et vérifiez s\'il est lié à la même version de Coin que FreeCAD

S\'il y a une différence, FreeCAD ou SoQt doivent être recompilés (mieux vaut recompiler celui qui utilise la version la plus ancienne de Coin). Le comportement normal est d\'essayer de contacter les personnes responsables de l\'empaquetage de SoQt ou de FreeCAD et de leur demander de bien vouloir envisager la recompilation. Si vous souhaitez entreprendre cette étape pour vous-même, et qu\'il n\'est pas possible de recompiler SoQt car il casse d\'autres applications sur votre système, vous pouvez forcer FreeCAD à compiler avec la version Coin requise avec {{SystemInput|<nowiki>./configure --with-coin=DIR</nowiki>}}. Mais vous devez vous assurer que le package de développement correct de cette version Coin est installé.

### FreeCAD se bloque après Édition → Alignement 

Une erreur de segmentation se produit à {{SystemOutput|vbo_save_playback_vertex_list()}}. Cela signifie que l\'implémentation de VBO dans le pilote graphique est mauvaise. Afin d\'éviter la mise en cache des appels OpenGL, vous pouvez essayer de définir la variable d\'environnement {{SystemInput|<nowiki>IV_SEPARATOR_MAX_CACHES=0</nowiki>}} et redémarrer FreeCAD.

### J\'ai des problèmes en cours d\'exécution de FreeCAD sur macOS 

La plate-forme Mac est moins facile à prendre en charge que Windows ou Linux, car aucun des principaux développeurs n\'en possède une. Les packages macOS sont compilés par des utilisateurs FreeCAD volontaires, et ils peuvent parfois ne pas fonctionner correctement sur votre machine, en fonction de votre système. Votre meilleure chance est probablement de vous rendre sur les forums, de rechercher des fils liés à macOS et de discuter de votre problème là-bas ou de voir si quelqu\'un d\'autre a trouvé une solution.

### Je ne peux pas modifier les valeurs numériques dans les panneaux de propriétés de FreeCAD 

<img alt="language options" src=images/Jj62l.png  style="width:480px;">

Vous avez probablement une mauvaise configuration des paramètres régionaux de Windows. Veuillez vérifier si vous avez le même symbole pour le séparateur décimal et le symbole de regroupement de chiffres dans vos paramètres régionaux. Si vous le faites, [adaptez vos paramètres système](http://forum.freecadweb.org/viewtopic.php?f=4&t=2655&p=20046#p20041) pour utiliser des caractères différents pour le symbole de regroupement de chiffres et le séparateur décimal. Notez qu\'il n\'est pas obligatoire d\'avoir un point comme séparateur décimal. Il est obligatoire d\'utiliser des symboles différents dans ces deux paramètres. 

### FreeCAD fonctionnait normalement, et tout à coup, il ne fonctionne plus 

Cela peut également se produire si vous aviez une ancienne version de FreeCAD installée et que vous êtes passé à une version plus récente. Dans ce processus, les fichiers de configuration de FreeCAD ont peut-être été corrompus pour une raison quelconque, et maintenant FreeCAD ne peut plus les lire et ne parvient pas à démarrer. La solution consiste simplement à supprimer ces fichiers de configuration, afin que FreeCAD les recrée lors de la première exécution.

-   sur Windows : Ouvrez le gestionnaire de fichiers et saisir **%APPDATA%\FreeCAD** dans le chemin de fichiers. Ensuite supprimer les fichiers **user.cfg** et **system.cfg**.
-   sur Linux : Naviguez jusqu\'à **/home/USERNAME/.local/share/FreeCAD** ({{VersionPlus/fr|0.20}}) ou **/home/USERNAME/.FreeCAD** ({{VersionMinus/fr|0.19}}) et supprimer les fichiers **user.cfg** et **system.cfg**.
-   sur Mac : Naviguez jusqu\'à **/Users/USERNAME/Library/Preferences/FreeCAD**et supprimer les fichiers **user.cfg** et **system.cfg**.

FreeCAD devrait maintenant redémarrer normalement avec tous ses paramètres réinitialisés.

Une [Macro findConfigFiles](Macro_findConfigFiles/fr.md) est disponible pour vous aider à localiser vos fichiers de configuration. Elle peut être installée en utilisant le Gestionnaire des extensions dans le menu **Outils → Gestionnaire des extensions → Macros → findConfigFiles**. La macro trouvera votre dossier de fichier de configuration, le copiera dans le presse-papiers et ouvrira (si possible) cet emplacement avec votre navigateur de fichiers par défaut. Elle n\'effectue aucun changement sur vos fichiers ou paramètres.

## Utiliser FreeCAD 

### FreeCAD est-il vraiment gratuit? Même pour un usage commercial? 

FreeCAD est un [logiciel open-source](https://fr.wikipedia.org/wiki/Open_source), gratuit non seulement pour votre utilisation personnelle ou pour tout travail commercial, mais aussi pour le distribuer, le modifier, ou même l\'utiliser dans une application à code source propriétaire. Pour résumer, vous êtes libre de faire (presque) tout ce que vous voulez avec lui. Lisez la page de la [licence](Licence/fr.md) pour plus de renseignements.

### Comment puis-je faire pivoter la vue 3D ? 


<center>

Image:Style_of_navigation.png\|À partir du **bouton droit** de la souris Image:Style of navigation menu.png\|À partir du menu **Édition → Préférences →**


</center>




FreeCAD a différents [styles de navigation](Mouse_navigation/fr.md) disponibles qui peuvent être réglés dans les préférences ou en faisant un clic droit dans la vue 3D. Pour plus de détails lisez la page [Navigation par la souris](Mouse_navigation/fr.md).

### Que puis-je faire avec FreeCAD ? Où dois-je commencer ? 

Dirigez-vous vers la page [Démarrer avec FreeCAD](Getting_started/fr.md) pour une description rapide des outils que vous pouvez utiliser. Il y a aussi une nouvelle section de [tutoriels](Tutorials/fr.md) contenant quelques ressources. La page [Documentation pour utilisateurs](User_hub/fr.md) contient des informations plus détaillées sur les différents ateliers de FreeCAD. Notez que FreeCAD est relativement jeune, et que son interface utilisateur est encore un peu dépouillée, et ne comporte pas de nombreux outils. Mais beaucoup de fonctionnalités avancées sont déjà à votre disposition à partir des [scripts Python](Power_users_hub/fr.md).

### Y-a-il une documentation pour les nouveaux arrivants ? Comment puis-je apprendre à utiliser FreeCAD ? 

Il y a beaucoup de documentation répartie à différents endroits, à la fois sur et en dehors du site Web de FreeCAD. Vous souhaiterez peut-être commencer par la page [Démarrer avec FreeCAD](Getting_started/fr.md). La section [Tutoriels](Tutorials/fr.md) contient de nombreuses pages de tutoriels spécialisés pour vous aider à démarrer avec les différents ateliers. Le [Manuel : Introduction](Manual:Introduction/fr.md) est un guide utilisateur général et complet de FreeCAD. La section [Documentation pour utilisateurs](User_hub/fr.md) de ce wiki répertorie toutes les pages destinées aux utilisateurs finaux. Sur des sites externes comme [Youtube](https://www.youtube.com/results?search_query=freecad), vous trouverez également une foule de tutoriels vidéo créés par les utilisateurs. Et, last but not least, le [forum](https://forum.freecadweb.org) contient de nombreuses réponses aux questions posées par d\'autres nouveaux venus.

### Je veux importer/exporter des données au format XYZ de/vers FreeCAD. Comment faire ? 

Référez vous à la page [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md). Peut-être que vos questions y trouveront une réponse.

### Où puis-je trouver des solutions de contournement pour les fonctionnalités que FreeCAD ne supporte pas actuellement ? 

Veuillez vous reporter à la page [Solutions de contournement](Workarounds/fr.md).

## Travailler avec la géométrie de Part 

### Comment puis-je extruder des formes dans des solides ? Je n\'ai pas le résultat attendu 

La théorie est simple : Les lignes (ou les polylignes), lorsqu\'elles sont extrudées, forment des faces. Les faces, lorsqu\'elles sont extrudées, forment des solides. Si vous extrudez quelque chose et que le résultat n\'est pas un solide, alors ce quelque chose n\'était pas une face. Si vous avez des lignes et que vous voulez extruder un solide à partir de celles-ci, vous devez d\'abord sélectionner des lignes qui forment un périmètre fermé (sélectionnez plusieurs objets en appuyant sur **Ctrl**), les joindre en une polyligne (outil [Draft Agréger](Draft_Upgrade/fr.md)), puis faire une face à partir de cette polyligne (outil <img alt="" src=images/Draft_Upgrade.svg  style="width:16px;"> [Draft Agréger](Draft_Upgrade/fr.md) à nouveau). Et voilà, si tout s\'est bien passé, vous pouvez maintenant l\'extruder en un solide.

Maintenant, il peut y avoir de nombreux petits détails qui feront obtenir un mauvais résultat. La meilleure façon de faire, est de vérifier que tout ce qu\'il y a dans votre forme peut être extrudé. Le contenu des objets peut être facilement exploré grâce à des procédures en Python. En supposant par exemple que vous ayez un objet appelé \"Wire\", vous pouvez taper ceci dans la console Python:


{{code|code=
obj = FreeCAD.ActiveDocument.Wire
shp = obj.Shape
print shp.Faces
print shp.Wires
if shp.Wires:
    for w in shp.Wires:
        print w.isClosed()
}}

Le code ci-dessus récupère la forme d\'un objet, montre les faces et les fils de votre objet (le cas échéant) et, s\'il y a des fils, imprime si ces fils sont fermés. Si vous n\'avez pas de faces, vous n\'obtiendrez pas de solide. S\'il n\'y a pas de fil fermé, il ne deviendra pas une face. Si vous êtes intéressé, vous trouverez plus d\'informations sur ce que vous pouvez vérifier avec Python sur la page [Scripts pour création topologique](Topological_data_scripting/fr.md). Si vous ne pouvez pas joindre plusieurs lignes dans un fil, la cause la plus probable est que leurs extrémités ne se rencontrent pas, il doit y avoir de petits espaces entre (certains d\'entre eux). Là, j\'ai peur, mon expérience me dit que le moyen le plus rapide serait de redessiner un fil par-dessus.

### Mes opérations booléennes échouent, ou donnent des résultats bizarres 

Le noyau de modélisation géométrique [Open CASCADE](https://fr.wikipedia.org/wiki/Open_CASCADE_Technology) utilisé dans FreeCAD pour la géométrie Part, bien que probablement le meilleur noyau de géométrie open-source disponible, a ses défauts et ses limites. En effet les opérations booléennes (fusion, soustraction, intersection) ne sont pas ses meilleures caractéristiques et donnent souvent des résultats étranges. Il s\'agit d\'une limitation actuelle que nous n\'avons aucun moyen de résoudre à la fois, donc votre meilleur moyen est d\'essayer d\'obtenir le résultat souhaité en modélisant d\'une autre manière. Par exemple, les problèmes avec les primitives telles que le cylindre peuvent souvent être résolus en utilisant un cercle extrudé à la place. Les surfaces coplanaires entre les pièces peuvent causer des problèmes, ainsi que la tangence de surface. En règle générale, si une forme ne fonctionne pas, essayez de la remodeler d\'une manière différente. Dans 99% des cas, vous réussirez à obtenir le résultat souhaité.

### Quand j\'exporte (ou visualise) mon modèle, les trous sont remplis 

Ne pas utiliser **Crtl** + **A** (Tout sélectionner) pour exporter toute l\'arborescence. Si le modèle n\'est qu\'un seul élément, essayez de ne sélectionner que l\'élément le plus récent (généralement le dernier) dans l\'arborescence.

Lors de la création d\'un modèle dans l\'[atelier Part Design](PartDesign_Workbench/fr.md), chaque fonction prend la forme de la dernière et ajoute ou supprime quelque chose, en créant des dépendances linéaires de la fonction à l\'élément créé. Ainsi, une fonction \"Soustraction\" est non seulement le trou découpé, mais toute la partie avec la coupe. C\'est pourquoi l\'utilisateur ne voit que l\'élément le plus récent (de la fonction utilisée) dans l\'arborescence du modèle, les autres sont cachées, sinon toutes les phases du modèle se superposent l\'une sur l\'autre, et les trous sont remplis par les caractéristiques du composant précédent.

Pour activer ou désactiver la visibilité d\'un objet, sélectionnez-le dans l\'arborescence et appuyez sur la barre **Espace**. Habituellement tout les objets sauf le dernier élément de l\'arborescence seront grisés et donc non visibles dans la vue 3D.

### Mes objets paramétriques se cassent lorsque je modifie leurs esquisses de base 

Vous avez rencontré l\'(in)fameux problème de toponymie. Il s\'agit actuellement d\'un problème majeur dans FreeCAD pour les nouveaux arrivants. Il est présent partout dans FreeCAD, mais est plus important lors de l\'utilisation d\'[esquisses](Sketcher_Workbench/fr.md). L\'explication est simple: lors du recalcul d\'une esquisse, les entités géométriques (arêtes, faces \...) sont reconstruites dans un ordre différent, en fonction de la priorité des contraintes. Ils reçoivent alors un nom différent (Edge1, Edge2, Face1, Face2 \...). La plupart des opérations ultérieures dépendent de ces noms pour identifier le sous-composant sur lequel elles travaillent. Par conséquent, lorsque l\'esquisse est reconstruite, les fonctions basées sur de tels sous-composants peuvent soudainement changer leur géométrie de base et donner un résultat erroné.

C\'est un problème très difficile à surmonter (le [Projet de dénomination topologique](Topological_Naming_Project/fr.md) vise à le résoudre). Cependant, il existe de nombreuses solutions de contournement disponibles pour atténuer le problème et les utilisateurs plus avancés parviennent généralement à l\'éviter complètement. Quelques stratégies sont:

-   Sachez que les esquisses sont très sensibles au problème. Faire référence à une arête spécifique d\'une esquisse, ou à une face d\'un objet construit sur une esquisse, comme une [PartDesign Protrusion](PartDesign_Pad/fr.md), est dangereux, à moins que vous ne soyez assez sûr que ces esquisses ne changeront pas avec le temps ou que l\'esquisse est très simple. Une Protrusion construite sur une simple esquisse rectangulaire, par exemple, sera probablement sûr car elle ne générera qu\'une seule face, donc il n\'y a pas de problème d\'ordre.
-   Préférez d\'autres types d\'objets tels que [Part](Part_Workbench/fr.md) ou [Draft](Draft_Workbench/fr.md) lorsque cela est possible. Ces objets sont toujours construits de la même manière et, par conséquent, leurs composants géométriques suivent généralement le même ordre chaque fois qu\'ils sont reconstruits. Ils sont beaucoup moins sensibles aux problèmes de toponaming.
-   Pour attacher d\'autres objets sur les faces d\'une géométrie basée sur une esquisse, préférez utiliser [Plan de référence](PartDesign_Plane/fr.md). Ces \"objets d\'aide\" invisibles ne dépendent pas de la géométrie de l\'esquisse et restent donc stables dans le temps.

## Contribuer à FreeCAD 

### FreeCAD est un excellent programme! Comment puis-je participer ? 

Il existe de nombreuses façons d\'aider, même si vous n\'êtes pas programmeur. Voici quelques actions que vous pouvez effectuer:

-   Donner des commentaires aux développeurs FreeCAD: il est toujours utile de savoir ce que les gens pensent, ce qu\'ils ont trouvé bon, ce qu\'ils manquent, etc. Déposez une note sur le [forum](https://forum.freecadweb.org/) donnant votre opinion ou faites une demande sur notre [issue tracker](https://tracker.freecadweb.org/main_page.php)!
-   Aider à la rédaction de la documentation: la documentation que nous avons ici sur ce site est parfois très limitée. Si vous avez découvert quelque chose qui n\'est pas bien documenté, ajoutez-y vos connaissances!
-   Aider les autres nouveaux arrivants: traînez sur le forum et aidez de nouvelles personnes à résoudre des questions de base, comme comment installer, comment ajouter un cube, etc.
-   [Traduire la documentation](Help_FreeCAD/fr#Traduire_la_documentation.md) dans votre propre langue
-   [Traduire FreeCAD](Help_FreeCAD/fr#Traduire_FreeCAD.md) dans votre propre langue
-   Écrire des [Tutoriels](Tutorials/fr.md) ou enregistrer des tutoriels vidéo: les tutoriels sont un moyen très simple pour les nouveaux arrivants d\'apprendre un nouveau logiciel. Si vous avez fait de belles choses, pourquoi ne pas montrer aux autres comment faire?
-   Contribuez avec des ressources et des exemples: il nous manque encore de bons exemples de fichiers dans FreeCAD. Si vous avez créé quelque chose de bien, partagez-le avec nous!
-   [Soumettre les bogues](Tracker/fr.md): il est très important de corriger tous les bogues possibles. Si vous en trouvez un, signalez-le aussi clairement que possible, afin que nous puissions comprendre exactement ce qui se passe.
-   Essayer de faire du codage en Python: vous n\'avez jamais programmé auparavant mais vous voulez essayer? Python est facile. Lisez notre [introduction à Python](Introduction_to_Python/fr.md), mais attention, vous risquez de devenir rapidement accro!
-   Voir la page [Contribuer à FreeCAD](Help_FreeCAD/fr.md) pour plus de détails sur la manière de contribuer.

### Comment puis-je obtenir les droits pour modifier le wiki ? 

Voir le paragraphe [Travailler sur la documentation](Help_FreeCAD/fr#Travailler_sur_la_documentation.md) pour plus de détails sur la manière de contribuer.

### FreeCAD participe t\'il au Google Summer of Code ? 

Oui. Depuis 2016 FreeCAD participe au Google Summer of Code. Lisez [Google Summer of Code 2020](Google_Summer_of_Code_2020.md) pour des informations sur la dernière édition, et [Google Summer Of Code 2016](http://forum.freecadweb.org/viewtopic.php?f=8&t=13838) pour l\'annonce originale sur le forum.

### Je veux commencer à traduire le wiki dans ma propre langue. Que dois-je faire ? 

Ce wiki héberge pas mal de contenu. Les informations les plus intéressantes et les plus à jour sont rassemblées dans le [manuel](Online_Help_Toc/fr.md).

Voir le paragraphe de la page [Traduction de la documentation](Help_FreeCAD/fr#Traduire_la_documentation.md) pour plus de détails sur la façon de traduire le wiki.

### Je peux acheter des goodies ? 

FreeCAD ne propose pas de goodies que vous pouvez commander pour soutenir le projet. Mais vous pouvez créer le vôtre. Voir notre page [Goodies](Swag/fr.md) pour les instructions.

## Licence, copie et réutilisation 

### Dois-je payer quelque chose pour utiliser FreeCAD ? 

Non. FreeCAD est totalement gratuit à utiliser, à télécharger, à redistribuer ou à modifier. Il s\'agit du [logiciel open-source](https://en.wikipedia.org/wiki/Open_source), publié sous les termes de la [Licence publique générale limitée GNU 2.1](https://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_limit%C3%A9e_GNU), qui vous garantit ces libertés et, plus important encore, vous garantit que ces libertés ne vous seront jamais enlevées.

### Puis-je réutiliser une partie de l\'artwork de FreeCAD ou des éléments du site web ? 

Bien sûr. Toutes les œuvres (icônes, bannières, etc ..) de FreeCAD sont sous licence LGPL, de même que le code source de FreeCAD. Aidez vous à partir de la [page Graphisme](Artwork/fr.md). Le site est un site standard MediaWiki, tous les éléments graphiques peuvent être librement réutilisés, et si vous êtes curieux de savoir comment modifier le logiciel MediaWiki comme nous l\'avons fait, regardez les pages spéciales Common **css et js**.

### Puis-je réutiliser des morceaux de FreeCAD dans une autre application ? 

Oui, vous pouvez utiliser les composants essentiels de FreeCAD dans d'autres applications, dans la mesure où vous vous conformez aux conditions de la LGPL. Les bibliothèques tierces, [ateliers externe](External_workbenches/fr.md) et [macros](Macros/fr.md) peuvent être soumises à leurs propres conditions de licence, merci de consulter leurs auteurs. Plus de détails sur la page [licence](Licence/fr.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Documentation](Category_Documentation.md) > Frequently asked questions/fr
