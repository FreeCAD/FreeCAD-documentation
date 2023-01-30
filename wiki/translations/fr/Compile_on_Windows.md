# Compile on Windows/fr
{{TOCright}}

Cette page explique étape par étape **comment compiler FreeCAD 0.19 ou plus récent sous Windows** en utilisant le compilateur MSVC de Microsoft. Pour des informations sur l\'utilisation de MSYS2/MinGW voir [Compiler sous MinGW](Compile_on_MinGW/fr.md). Pour les autres plateformes, voir [Compiler](Compiling/fr.md).



## Prérequis

La compilation de FreeCAD sous Windows nécessite plusieurs outils et bibliothèques.



### Requis

-   Un compilateur. FreeCAD est testé avec Visual Studio (MSVC)-d\'autres compilateurs peuvent fonctionner, mais les instructions d\'utilisation ne sont pas incluses ici. Pour plus de détails, voir la section [Compilateur](#Compilateur.md) ci-dessous.

-   [Git](http://git-scm.com/) (Il existe également des interfaces GUI disponibles pour Git, voir la section suivante.)

-   [CMake](https://cmake.org/download/) version 3.11.x ou plus récente.  *Astuce :* Choisir l\'option *Ajouter CMake au chemin du système pour tous les utilisateurs* lors de l\'installation de CMake rendra CMake accessible depuis l\'invite de commande Windows, ce qui peut être utile.

-   [LibPack](https://github.com/FreeCAD/FreeCAD-LibPack). Il s\'agit d\'un paquetage unique contenant toutes les bibliothèques nécessaires à la compilation de FreeCAD sous Windows. Téléchargez la version du LibPack qui correspond à la version de FreeCAD que vous voulez compiler. Pour compiler FreeCAD 0.20 téléchargez [LibPack version 2.6](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/2.6), pour FreeCAD 0.19 téléchargez [LibPack version 1.0](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/1.0). Extrayez LibPack à un endroit approprié. (Si votre ordinateur ne reconnaît pas l\'extension .7z, vous devez installer le programme [7-zip](https://www.7-zip.org)). **Remarque** : il est fortement recommandé de compiler FreeCAD avec la version du compilateur pour laquelle le LibPack est conçu. Par exemple, vous pourriez rencontrer des problèmes en compilant FreeCAD 0.20 avec MSVC 2017 parce que le LibPack est conçu pour être construit avec MSVC 2019 ou plus récent.Pour mettre à jour votre LibPack ultérieurement, consultez la section [Mise à jour de LibPack](#Mise_.C3.A0_jour_de_LibPack.md).



### Programmes optionnels 

-   Une interface graphique pour Git. Plusieurs interfaces sont disponibles, voir [cette liste](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs). L\'avantage principal d\'une interface est qu\'il n\'est pas nécessaire d\'apprendre les commandes Git pour obtenir le code source de FreeCAD ou pour envoyer des correctifs au référentiel GitHub de FreeCAD.

Nous décrivons ci-après la gestion du code source à l\'aide de l\'interface [TortoiseGit](https://tortoisegit.org/). Cette interface s\'intègre directement dans l\'explorateur de fichiers Windows et dispose d\'une large communauté d\'utilisateurs pour obtenir de l\'aide en cas de problème.

-   [NSIS](http://sourceforge.net/projects/nsis/) est utilisé pour générer le programme d\'installation de FreeCAD Windows.



### Code source 

Vous pouvez maintenant obtenir le code source de FreeCAD :



#### Utiliser une interface 

Lorsque vous utilisez le [Git frontend](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit :

1.  Créez un nouveau dossier dans lequel le code source sera téléchargé.
2.  Cliquez avec le bouton droit de la souris sur ce dossier dans l\'explorateur de fichiers Windows et sélectionnez **Git Clone** dans le menu contextuel.
3.  Une boîte de dialogue apparaîtra. Dans celui-ci, entrez l\'URL du dépôt FreeCAD Git

*<https://github.com/FreeCAD/FreeCAD.git>*

et cliquez sur **OK**.

Le dernier code source sera téléchargé à partir du dépôt FreeCAD Git et le dossier sera suivi par Git.



#### Utiliser la ligne de commande 

Pour créer une branche locale et télécharger le code source, vous devez ouvrir un terminal (invite de commande) et entrez dans le répertoire ou vous désirez placer le code source, puis tapez :


```python
git clone https://github.com/FreeCAD/FreeCAD.git
```



### Compilateur

Le compilateur par défaut (recommandé) est MS Visual Studio (MSVC). Bien qu\'il soit possible d\'utiliser d\'autres compilateurs, par exemple gcc via Cygwin ou MinGW, cela n\'est pas testé ni couvert ici.

Vous pouvez obtenir une version gratuite de MSVC (pour un usage individuel) en téléchargeant l \'[édition *Community* de MS Visual Studio](https://visualstudio.microsoft.com/vs/community/).

Pour ceux qui ne veulent pas installer l\'énorme MSVC uniquement pour avoir un compilateur, voir [CompileOnWindows - Réduire l\'espace disque](CompileOnWindows_-_Reducing_Disk_Footprint/fr.md).

**Remarque :** Bien que l\'édition *Community* de MSVC soit gratuite, pour utiliser l\'EDI pendant plus de 30 jours, vous devez créer un compte Microsoft. Si vous ne compilez qu\'en utilisant la ligne de commande, vous n\'avez pas besoin de l\'EDI et donc pas de compte Microsoft.

Comme alternative gratuite et OpenSource IDE, vous pouvez utiliser [KDevelop](https://www.kdevelop.org/download). Vous pouvez utiliser KDevelop pour modifier et écrire du code C ++, mais vous devez utiliser la ligne de commande pour compiler.



### Configuration optionnelle du chemin d\'accès au système 

Vous pouvez éventuellement inclure les chemins d\'accès à certains dossiers de la variable système PATH. Ceci est utile si vous souhaitez accéder aux programmes de ces dossiers à partir de la ligne de commande/powershell ou si vous souhaitez que des programmes spéciaux soient trouvés par le compilateur ou CMake. En outre, l'ajout de dossiers à PATH peut s'avérer nécessaire si vous n'utilisez pas les options correspondantes lors de l'installation du programme.

-   Vous pouvez inclure le dossier de votre LibPack dans votre variable système PATH. Ceci est utile si vous envisagez de créer plusieurs configurations/versions de FreeCAD.
-   Si vous n\'avez pas utilisé l\'option permettant d\'ajouter CMake à PATH lors de son installation, ajoutez son dossier d\'installation

*C:\\Program Files\\CMake\\bin* à PATH.

-   Si vous n\'avez pas utilisé l\'option permettant d\'ajouter TortoiseGit à PATH lors de son installation, ajoutez son dossier d\'installation

*C:\\Program Files\\TortoiseGit\\bin* à PATH.

Pour ajouter à votre chemin au système :

1.  Dans le menu Démarrer de Windows, cliquez avec le bouton droit de la souris sur *Ordinateur* et choisissez *Propriétés*.
2.  Dans la boîte de dialogue qui apparaît, cliquez sur *Paramètres système avancés*.
3.  Une autre boîte de dialogue s\'ouvrira. Cliquez sur l\'onglet *Avancé* sur **Variables d\'environnement**.
4.  Encore une autre boîte de dialogue s\'ouvrira. Sélectionnez ensuite la variable *Path* et cliquez sur **Editer**.
5.  Une autre boîte de dialogue s\'ouvrira. Cliquez ici sur **Nouveau** et ajoutez le chemin d\'accès au dossier de Git ou du LibPack.
6.  Enfin, appuyez sur **OK** et fermez toutes les boîtes de dialogue en appuyant sur **OK**.

## Configuration

Une fois que vous avez tous les outils, bibliothèques et code source FreeCAD nécessaires, vous êtes prêt à commencer le processus de configuration et de compilation. Ce processus se déroulera en cinq étapes :

1.  Exécutez CMake une fois pour examiner votre système et commencer la progression de la configuration (cela signalera qu\'il a échoué).
2.  Ajustez les paramètres CMake nécessaires pour définir les emplacements du LibPack et activer Qt5.
3.  Relancez CMake pour finaliser la configuration (cette fois, cela devrait réussir).
4.  Utilisez CMake pour générer le système de build Visual Studio.
5.  Utilisez Visual Studio pour créer FreeCAD.

### CMake

Tout d\'abord, configurez l\'environnement de construction à l\'aide de CMake :

1.  Ouvrez l\'interface graphique de CMake
2.  Spécifiez le dossier source de FreeCAD.
3.  Spécifiez un dossier de compilation (n\'utilisez pas le dossier source - CMake créera ce dossier s\'il n\'existe pas).
4.  Cliquez sur **Configure**.
5.  Dans la boîte de dialogue qui apparaît, spécifiez le générateur que vous souhaitez utiliser: dans la plupart des cas, vous utiliserez les valeurs par défaut de cette boîte de dialogue. Pour le MS Visual Studio standard, utilisez *Visual Studio xx 2yyy* où xx est la version du compilateur et 2yyy l\'année de sa sortie. Il est recommandé d\'utiliser l\'option par défaut *Use default native compilers*.

**Remarque:** Il est important de spécifier la variante de bit correcte. Si vous avez la variante 64 bits de LibPack, vous devez également utiliser le compilateur x64.

Cela commencera la configuration et *échouera* à cause de paramètres manquants. C\'est normal, vous n\'avez pas encore spécifié l\'emplacement du LibPack. Cependant, d\'autres problèmes peuvent survenir et nécessiter une action supplémentaire de votre part.

S\'il échoue avec le message \"Visual Studio est introuvable\", la prise en charge de CMake dans MSVC n\'est pas encore installée. Pour l\'installer :

1.  Ouvrez l\'EDI MSVC
2.  Utilisez le menu Outils → Obtenir les outils et fonctionnalités
3.  Dans l\'onglet *Workloads*, activez *Développement de bureau avec C++*
4.  Sur le côté droit, vous devriez maintenant voir que le composant *Outils Visual C++ pour CMake* sera installé.
5.  Installez-le.

Si cela échoue avec un message sur la mauvaise version de Python ou Python manquant, alors :

1.  Utilisez la case \"Search:\" dans CMake pour rechercher la chaîne \"Python\"
2.  Si vous y voyez un chemin comme *C:/Program Files/Python38/python.exe*, CMake a reconnu le Python qui est déjà installé sur votre PC, mais cette version n\'est pas compatible avec le LibPack. Étant donné que le LibPack inclut une version compatible de Python, modifiez les paramètres Python suivants dans CMake sur ses chemins (en supposant que le LibPack se trouve dans le dossier *D:\\FreeCAD-build\\FreeCADLibs_12.5.2_x64_VC17*) :

![](images/CMake_Python_settings.png )

S\'il n\'y a pas d\'erreur à propos de Visual Studio ou Python, tout va bien, mais CMake ne connaît pas encore tous les paramètres nécessaires. Donc maintenant :

1.  Recherchez dans CMake la variable **FREECAD_LIBPACK_DIR** et spécifiez l\'emplacement du dossier LibPack que vous avez téléchargé précédemment.
2.  Seulement si vous compilez FreeCAD 0.19, cherchez la variable **BUILD_QT5** et activez cette option.
3.  Cliquez à nouveau sur **Configure**.

Il ne devrait plus y avoir d'erreurs. Si vous continuez à rencontrer des erreurs que vous ne pouvez pas diagnostiquer, allez sur le [Forum Install/Compile](https://forum.freecadweb.org/viewforum.php?f=4) de FreeCAD. Si CMake a procédé correctement, cliquez sur **Generate**. Une fois cela fait, vous pouvez fermer CMake et démarrer la compilation de FreeCAD à l\'aide de Visual Studio. Cependant, pour la première compilation, gardez-le ouvert au cas où vous voudriez ou auriez besoin de changer certaines options pour le processus de construction.

**Remarque :** Lors de la compilation de FreeCAD 0.19, la variable CMake **BUILD_ENABLE_CXX_STD** sera fixée à **C++14** alors que pour FreeCAD 0.20 elle sera fixée à **C++17**. Ceci est dû au fait que FreeCAD 0.20 requiert au moins la version 17 du standard du langage C++. Donc quand vous avez compilé la dernière fois FreeCAD 0.19, il est nécessaire de relancer CMake pour FreeCAD 0.20 pour changer le standard du langage C++.



### Options pour le procédé de compilation 

Le système de compilation CMake vous permet de contrôler certains aspects du processus de compilation. En particulier, vous pouvez activer et désactiver certaines fonctionnalités ou modules à l\'aide des variables CMake.

Voici la description de certaines de ces variables :

  Nom de la variable                  Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Valeur par défaut
    
  BUILD_XXX                           Compile FreeCAD avec le composant XXX. Si vous ne voulez/nécessitez pas compiler par exemple l\'atelier *OpenSCAD*, désactivez la variable *BUILD_OPENSCAD*. FreeCAD n\'aura alors pas cet atelier. **Remarque:** Certains composants sont nécessaires pour d\'autres composants. Si vous décochez par exemple *BUILD_ROBOT*, CMake vous informera qu\'alors le composant *Path* ne pourra pas être compilé correctement. Vérifiez donc la sortie de CMake après avoir modifié une option BUILD_XXX!                                                                                                                                                                                                                                                                                                             ca dépend
  BUILD_ENABLE_CXX_STD                La version du standard du langage C++. **C++14** est la plus élevée possible pour FreeCAD 0.19 alors qu\'au moins **C++17** est nécessaire pour FreeCAD 0.20. Voir aussi la note dans la section [Construire avec Visual Studio 15 (2017) et 16 (2019)](#Version_de_Build.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ca dépend
  BUILD_DESIGNER_PLUGIN               Pour construire le plugin Qt Designer, voir [cette section ci-dessous](Compile_on_Windows/fr#Le_plugin_Qt_Designer.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   OFF
  BUILD_FLAT_MESH                     Nécessaire pour avoir une version qui inclut la fonction [Développer un objet maillé](MeshPart_CreateFlatMesh/fr.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    OFF
  CMAKE_INSTALL_PREFIX                Le dossier de sortie lors de la construction de la cible *INSTALL*, voir aussi la section [Exécution et installation de FreeCAD](#Ex.C3.A9cution_et_installation_de_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Le dossier d\'installation par défaut de Windows
  FREECAD_COPY_DEPEND_DIRS_TO_BUILD   Copie les bibliothèques dépendantes nécessaires à l\'exécution de FreeCAD.exe dans le dossier de build. Voir aussi la section [Exécution et installation de FreeCAD](#Ex.C3.A9cution_et_installation_de_FreeCAD.md). **Remarque :** les options FREECAD_COPY_XXX n\'apparaissent que si les bibliothèques n\'ont pas déjà été copiées. Si vous avez seulement besoin de mettre à jour/changer pour une autre version du LibPack, voir la section [Mise à jour de LibPack](#Mise_.C3.A0_jour_de_LibPack.md). Si vous voulez ramener les options pour une raison quelconque, vous devez supprimer tous les dossiers de votre dossier de construction, à l\'exception du dossier LibPack. Dans CMake, supprimez le cache et démarrez comme si vous compiliez pour la première fois.   OFF
  FREECAD_COPY_LIBPACK_BIN_TO_BUILD   Copie les binaires LibPack nécessaires à l\'exécution de FreeCAD.exe dans le dossier de compilation. Voir aussi la section [Exécution et installation de FreeCAD](#Ex.C3.A9cution_et_installation_de_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        OFF
  FREECAD_COPY_PLUGINS_BIN_TO_BUILD   Copie les fichiers plugins de Qt nécessaires à l\'exécution de FreeCAD.exe dans le dossier de compilation. Voir aussi la section [Exécution et installation de FreeCAD](#Ex.C3.A9cution_et_installation_de_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  OFF
  FREECAD_LIBPACK_USE                 Active ou désactive l\'utilisation du LibPack de FreeCAD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ON
  FREECAD_LIBPACK_DIR                 Répertoire où se trouve le LibPack                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Dossier du code source de FreeCAD
  FREECAD_RELEASE_PDB                 Créer des bibliothèques de débogage (\*.pdb) également pour les compilations de version. Cela n\'affecte pas la vitesse (comme le ferait une vraie compilation de débogage) et peut être très utile pour localiser les crashs dans le code de FreeCAD. En cas de crash de FreeCAD, un fichier *crash.dmp* sera créé et pourra être chargé avec MSVC et si vous avez les fichiers PDB correspondants ainsi que le code source de cette version, vous pourrez déboguer le code. Sans les fichiers PDB, il n\'est pas possible de déboguer le code et tout ce que le débogueur montre est le nom de la DLL où le crash s\'est produit.                                                                                                                                                                              ON
  FREECAD_USE_MP_COMPILE_FLAG         Ajoute l\'option /MP (multiprocesseur) aux projets Visual Studio, permettant des accélérations sur les CPU multi-cœurs. Cela peut accélérer considérablement les builds sur les processeurs modernes. **Remarque :** Si vous désactivez **FREECAD_USE_PCH**, la compilation peut rapidement surcharger votre espace de tas, même si vous avez 16 Go de RAM.                                                                                                                                                                                                                                                                                                                                                                                                                                        ON
  FREECAD_USE_PCH                     [Précompilation des en-têtes](https://en.wikipedia.org/wiki/Precompiled_header) afin de gagner du temps de compilation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ON
  FREECAD_USE_PYBIND11                Inclut la bibliothèque [PyBind11](https://github.com/pybind/pybind11). Nécessaire pour avoir un build qui inclut la fonction [Développer un objet maillé](MeshPart_CreateFlatMesh/fr.md).**Remarque :** après l\'avoir allumé, vous pourriez obtenir une erreur de configuration. Il suffit de configurer à nouveau et le problème devrait disparaître.                                                                                                                                                                                                                                                                                                                                                                                                                                    OFF



## Compilation de FreeCAD 

En fonction de votre compilateur, le processus de compilation de FreeCAD sera légèrement différent. Dans les sections suivantes, les processus connus sont décrits. Si vous compilez avec Qt Creator, passez à [Compilation avec Qt Creator (obsolète)](#Compilation_avec_Qt_Creator_.28obsol.C3.A8te.29.md), sinon procédez directement :


<div class="mw-collapsible mw-collapsed toccolours">



### Compilation avec Visual Studio 15 (2017) ou plus récent 


<div class="mw-collapsible-content">



#### Version de compilation 

1.  Démarrez l\'IDE Visual Studio. Cela peut être effectué en appuyant sur le bouton *Ouvrir un projet* dans l\'interface graphique de CMake ou en double-cliquant sur le fichier *FreeCAD.sln* que vous trouvez dans votre dossier de construction.
2.  Dans la barre d'outils de l'EDI MSVC, assurez-vous que vous utilisez pour la première compilation *Release*.
3.  Il y a une fenêtre appelée *Solution Explorer*. Elle répertorie toutes les cibles de compilation possibles. Pour démarrer une compilation complète, faites un clic droit sur la cible **ALL_BUILD** puis choisissez **Build**.

Cela va prendre pas mal de temps.

Pour compiler un FreeCAD prêt à l'emploi, compilez la cible *INSTALL*, voir la section [Exécution et installation de FreeCAD](#Ex.C3.A9cution_et_installation_de_FreeCAD.md).

Si vous n\'obtenez aucune erreur, vous avez terminé. **Félicitations !** Vous pouvez quitter MSVC ou le garder ouvert.

Remarque : FreeCAD 0.20 nécessite au moins la version 17 du langage standard C++ mais le composant tiers *flann* du LibPack n\'est pas encore prêt pour cela. Par conséquent, vous aurez des erreurs de compilation pour la cible *ReverseEngineering*. Pour résoudre ce problème, faites un clic droit sur cette cible dans l\'explorateur de solutions MSVC et sélectionnez dans le menu contextuel la dernière entrée *Properties*. Dans la boîte de dialogue qui apparaît, changez le *C++ Language Standard* en *ISO C++14*. Enfin, recompilez la cible **ALL_BUILD**.



#### Compilation de débogage 

Pour une version de débogage, il est nécessaire d\'utiliser le Python inclus dans le LibPack. Pour assurer cela :

1.  Recherchez \"Python\" dans l\'interface graphique de CMake
2.  Si vous y voyez un chemin comme \'C:/Program Files/Python38/python.exe*, CMake a reconnu le Python qui est installé sur votre PC et non celui du LibPack. Dans ce cas, adaptez ces différents paramètres Python dans CMake à cela (en supposant que le LibPack se trouve dans le dossier*D:\\FreeCAD-build\\FreeCADLibs_12.5.2_x64_VC17\'\') :

![](images/CMake_Python_settings.png )

Comme pré-requis pour la compilation debug, vous devez faire ceci :

1.  Copier le contenu du dossier LibPack *bind* dans le dossier *bin* du dossier de la compilation de FreeCAD (écraser les fichiers existants).
2.  Copier le contenu du dossier LibPack *libd* dans le dossier *lib* du dossier de la compilation de FreeCAD.

Maintenant vous pouvez compiler :

1.  Démarrez l\'IDE de Visual Studio. Cela peut être fait en appuyant sur le bouton *Open Project* dans l\'interface graphique de CMake ou en double-cliquant sur le fichier «FreeCAD.sln» que vous trouvez dans votre dossier de construction.
2.  Dans la barre d\'outils de MSVC IDE, assurez-vous que vous utilisez pour la première compilation *Debug*.
3.  Il existe une fenêtre appelée *Solution Explorer*. Il répertorie toutes les cibles de compilation possibles. Pour démarrer une compilation complète, faites un clic droit sur la cible **ALL_BUILD** puis choisissez **Build** dans le menu contextuel.

Cela prendra maintenant beaucoup de temps. S\'il n\'y a pas eu d\'erreurs de compilation, vous pouvez démarrer la compilation de débogage :

1.  Faites un clic droit sur la cible **FreeCADMain** puis choisissez **Set as Startup Project** dans le menu contextuel.
2.  Cliquez enfin dans la barre d\'outils sur le bouton avec le triangle vert nommé **Local Windows Debugger**.

Cela lancera la version de débogage de FreeCAD et vous pourrez utiliser MSVC IDE pour le déboguer.

#### Ressource vidéo 

Tutoriel en anglais qui commence par la configuration dans CMake Gui et continue jusqu\'à la commande \Build\ dans Visual Studio 16 2019 est disponible non répertorié sur YouTube à [Tutorial: Build FreeCAD from source on Windows 10](https://youtu.be/s4pHvlDOSZQ).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Compilation avec Qt Creator (obsolète) 


<div class="mw-collapsible-content">



#### Installation et configuration de Qt Creator 

-   Téléchargez et installez [Qt Creator](https://www.qt.io/offline-installers)
-   Outils → Options → Editeur Texte → Behavior tab:
    -   File Encodings → Default Encodings:
    -   Set to: **ISO-8859-1 /\...csISOLatin1** (Certain caracteres créent une errors/warnings avec Qt Creator if left set to UTF-8. Cela semble pour corrigé.)
-   Tools → Options → Build & Run:
    -   CMake tab
        -   Fill Executable box with path to cmake.exe
    -   Kits tab
        -   Name: MSVC 2008
        -   Compiler: Microsoft Visual C++ Compiler 9.0 (x86)
        -   Debugger: Détection automatique \...
        -   Qt version: None
    -   General tab
        -   Uncheck: Toujours compiler et déployer le projet
        -   Uncheck: Toujours déployer le projet avant de l\'exécuter



#### Importer un projet et compiler 

-   File → Open File or Project
-   Open **CMakeLists.txt** qui est dans le plus haut niveau de la source
-   Ceci démarre CMake
-   Choisissez créer le répertoire et cliquez sur suivant
-   Ensemble de générateurs de **NMake Generator (MSVC 2008)**
-   Cliquez sur Démarrer CMake. Suivez les instructions décrites ci-dessus pour configurer CMake à votre convenance.

Maintenant FreeCAD est construit

-   Build → Build All
-   Ceci peut prendre du temps\...

Une fois terminé, il peut être exécuté: Il y a 2 triangles verts en bas à gauche. Un est pour la mise au point. L\'autre est pour l\'exécution. Faites votre choix.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Compilation en ligne de commande 


<div class="mw-collapsible-content">

Les étapes pour compiler à partir de la ligne de commande dépendent du compilateur. Pour MSVC 2017, les étapes sont les suivantes:

1.  Dans le menu Démarrer de Windows, accédez à **Visual Studio 2017 → Outils Visual Studio** et choisissez **Invite de commande du développeur pour VS 2017**.
2.  Allez dans votre dossier de construction.
3.  Exécute la commande


```pythonmsbuild ALL_BUILD.vcxproj /p:Configuration=Release```

ou


```pythonmsbuild INSTALL.vcxproj /p:Configuration=Release```

Ces étapes peuvent également être automatisées. Voici par exemple une solution pour MSVC 2017 :

1.  Téléchargez le script [compile-FC.txt](https://forum.freecadweb.org/download/file.php?id=92135).
2.  Le renommer en *compile-FC.bat*
3.  Dans l\'explorateur de fichiers de Windows, faites Shift+Cliquez-droit sur votre dossier de construction et utilisez-le dans le menu contextuel *Invite de commandes ici*.
4.  Exécute la commande


```pythoncompile-FC install```

Au lieu d\'appeler **compile-FC** avec l\'option *installer*, vous pouvez aussi utiliser *déboguer* ou *release* :

*déboguer*   - compiler FreeCAD dans la configuration de débogage

*release* - compiler FreeCAD dans la configuration de release

*install*   - compiler FreeCAD dans la configuration de la version et créer une installation


</div>


</div>



## Exécution et installation de FreeCAD 

Il existe 2 méthodes pour exécuter la compilation de FreeCAD :

*Method 1* : Vous exécutez FreeCAD.exe que vous trouvez dans votre dossier de construction qui se trouve dans le sous-dossier *bin*

*Method 2* : Vous construisez la cible *INSTALL*

La méthode 2 est la plus simple, car elle assure automatiquement que toutes les bibliothèques requises pour exécuter FreeCAD.exe se trouvent dans le bon dossier. FreeCAD.exe et les bibliothèques seront sortis dans le dossier que vous avez spécifié dans la variable CMake *CMAKE_INSTALL_PREFIX*.

Pour la méthode 1, vous devez placer les bibliothèques dans le dossier *bin* de votre dossier de construction (où se trouve FreeCAD.exe). Cela peut être facilement fait en utilisant les variables CMake en option :

1.  Ouvrez l\'interface graphique de CMake.
2.  Recherchez et cochez la variable *FREECAD_COPY_DEPEND_DIRS_TO_BUILD*. S\'il n\'y a pas une telle option, les bibliothèques ont déjà été copiées, voir la [description des options](#Options_pour_le_procédé_de_compilation.md).
3.  Recherchez et cochez la variable *FREECAD_COPY_LIBPACK_BIN_TO_BUILD*.
4.  Recherchez et cochez la variable *FREECAD_COPY_PLUGINS_BIN_TO_BUILD*.
5.  Cliquez sur **Configurer**. A la fin de la configuration, CMake copiera automatiquement les bibliothèques nécessaires du dossier LibPack.



### Dépannage

Lors de l\'exécution de FreeCAD, vous pouvez rencontrer des DLLs manquantes lors de l\'utilisation de certains ateliers ou fonctionnalités d\'ateliers. Le message d\'erreur dans la console de FreeCAD ne vous dira pas quelle DLL est manquante. Pour le savoir, vous devez utiliser un outil externe :

-   Téléchargez la dernière version du programme **Dependencies** : [(choisissez le fichier *Dependencies_x64_Release.zip*)](https://github.com/lucasg/Dependencies/releases)
-   Dans la [Console Python](Python_console/fr.md) de FreeCAD, exécutez ces commandes :

import os
os.system(r"~DependenciesGui.exe")

**Note** : Au lieu du \~, vous devez spécifier le chemin complet du *DependenciesGui.exe* sur votre système.

-   Faites maintenant glisser le fichier \*.pyd de l\'atelier avec lequel vous obtenez des DLLs manquantes signalées.



## Mise à jour de la compilation 

FreeCAD est très activement développé. Par conséquent, son code source change presque quotidiennement. De nouvelles fonctionnalités sont ajoutées et des bugs corrigés. Pour bénéficier de ces modifications du code source, vous devez reconstruire votre FreeCAD. Cette reconstruction se fait en deux étapes:

1.  Mise à jour du code source
2.  Recompilation



### Mise à jour du code source 



#### Utiliser une interface 

Lorsque vous utilisez le [Git frontend](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit :

1.  Dans l\'explorateur de fichiers Windows faites clic droit sur le dossier de code source FreeCAD et sélectionnez dans le menu contextuel **Pull**.
2.  Une boîte de dialogue apparaîtra. Sélectionnez la branche de développement que vous souhaitez obtenir. **master** est la branche principale. Par conséquent, utilisez la sauf si vous voulez compiler une nouvelle fonctionnalité spéciale à partir d\'une branche qui n\'a pas encore été fusionnée avec **maître**. (Pour plus d\'informations sur les branches Git, consultez [Processus de développement Git](Source_code_management/fr#Processus_de_développement_Git.md)).

Cliquez enfin sur **OK**.



#### Utiliser la ligne de commande 

Ouvrez un terminal (invite de commande) et accédez au répertoire source. Puis tapez :


```python
git pull https://github.com/FreeCAD/FreeCAD.git master
```

où *master* est le nom de la branche principale du développement. Si vous voulez obtenir le code d'une autre branche, utilisez son nom au lieu de *master*.

### Recompilation

1.  Ouvrez l\'EDI MSVC en double-cliquant sur le fichier *FreeCAD.sln* ou sur le fichier *ALL_BUILD.vcxproj* dans votre dossier de compilation.
2.  Continuer à l\'étape 2 de la section [Compilation avec Visual Studio 15 (2017) ou plus récent](#Compilation_avec_Visual_Studio_15_.282017.29_ou_plus_r.C3.A9cent.md).



## Mise à jour de LibPack 

Si une nouvelle version majeure d\'une dépendance tierce comme Open Cascade est publiée, ou si une dépendance tierce a des corrections de bogues importantes, un nouveau LibPack est publié. Vous pouvez trouver la dernière version [ici](https://github.com/FreeCAD/FreeCAD-LibPack/releases/).

Pour mettre à jour votre LibPack, la recette suivante est la meilleure pratique :

1.  Supprimez le dossier *bin* de votre dossier de compilation.
2.  Passez à votre dossier LibPack local et supprimez tout ce qui s\'y trouve.
3.  Extrayez le contenu du nouveau fichier ZIP LibPack dans le dossier LibPack local existant, mais maintenant vide.
4.  Ouvrez CMake et appuyez sur le bouton **Configure** et ensuite sur le bouton **Generate**. Cela recrée le dossier *bin* que vous venez de supprimer et y copie également les nouveaux fichiers LibPack.
5.  Dans CMake, cliquez sur le bouton **Open Project** et l\'IDE MSVC s\'ouvrira.
6.  Dans l\'IDE MSVC, construisez la cible *INSTALL*.



## Outils

Pour rejoindre le développement FreeCAD, vous devez compiler et installer les outils suivants :



### Le plugin Qt Designer 

FreeCAD utilise [Qt](https://fr.wikipedia.org/wiki/Qt) comme boîte à outils pour son interface utilisateur. Toutes les boîtes de dialogue sont configurées dans des fichiers UI qui peuvent être modifiés à l\'aide du programme [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html). Il fait partie de toute installation Qt et également inclus dans le LibPack. FreeCAD a son propre ensemble de widgets Qt pour fournir des fonctionnalités spéciales comme l\'ajout d\'une unité aux champs de saisie et pour définir les propriétés des préférences.

#### Compilation

Le plugin ne peut pas être chargé par le Qt Designer s\'il a été compilé en utilisant une autre version de Qt que celle sur laquelle votre Qt Designer/Qt Creator est basé. Par conséquent, le plugin doit être compilé en même temps que FreeCAD :

-   Dans les options CMake (voir [cette section ci-dessus](Compile_on_Windows/fr#Options_pour_le_proc.C3.A9d.C3.A9_de_compilation.md)) activez l\'option BUILD_DESIGNER_PLUGIN et reconfigurez.
-   Ouvrez MSVC et construisez la cible **FreeCAD_widgets**.

Le résultat est le fichier du plugin **FreeCAD_widgets.dll** dans le dossier*\~src\\Tools\\plugins\\widget\\Release*



#### Installation

Pour installer le plugin, copiez-le dans l\'un des deux endroits suivants :

-   Si vous utilisez le LibPack : dans le dossier*\~\\FreeCADLibs_12.5.4_x64_VC17\\bin\\designer*Puisqu\'il n\'y aura qu\'un dossier *bin* et que vous devez d\'abord créer le sous-dossier *designer*.
-   Si vous avez une installation complète de Qt : vous pouvez choisir entre le dossier*C:\\Qt\\5.15.2\\msvc2019_64\\plugins\\designer*ou*C:\\Qt\\5.15.2\\msvc2019_64\\bin\\designer* (vous devez d\'abord créer le sous-dossier *designer*.)(adaptez les chemins à votre installation !).

Enfin, (re)lancez Qt Designer et vérifiez son menu **Help → Plugins**. Si le plugin **FreeCAD_widgets.dll** est répertorié comme étant chargé, vous pouvez maintenant concevoir et modifier les fichiers .ui de FreeCAD, sinon vous devez [compiler](#Compilation.md) vous-même la DLL.

Si vous préférez utiliser [Qt Creator](https://fr.wikipedia.org/wiki/Qt_Creator) au lieu de Qt Designer, le fichier du plugin doit être placé dans ce dossier : *C:\\Qt\\Qt5.15.2\\Tools\\QtCreator\\bin\\plugins\\designer* Puis (re)lancez Qt Creator Qt Creator, passez en mode **Design** puis vérifiez le menu **Tools → Form Editor → About Qt Designer Plugins**. Si le plugin **FreeCAD_widgets.dll** est répertorié comme étant chargé, vous pouvez maintenant concevoir et modifier les fichiers .ui de FreeCAD. Sinon, vous devez [compiler](#Compilation.md) vous-même la DLL.



### Fournisseur de vignettes 

FreeCAD a la fonctionnalité de fournir des vignettes d\'aperçu pour les fichiers \*.FCStd. Cela signifie que dans l\'explorateur de fichiers Windows, les fichiers \*.FCStd sont affichés avec une capture d\'écran du modèle qu\'il contient. Pour fournir cette fonctionnalité, FreeCAD doit avoir le fichier **FCStdThumbnail.dll** installé sur Windows.



#### Installation 

La DLL est installée de cette façon :

1.  Téléchargez [ce fichier ZIP](https://forum.freecadweb.org/download/file.php?id=13404) et extrayez-le.
2.  Ouvrez une invite de commande Windows avec des privilèges d\'administrateur (ces privilèges sont obligatoires).
3.  Accédez au dossier où se trouve la DLL.
4.  Exécutez cette commande 
```pythonregsvr32 FCStdThumbnail.dll```

Vérifiez donc si cela fonctionne, assurez-vous que dans FreeCAD, l\'option de préférences **[Enregistrer la miniature dans le fichier de projet lors de l\'enregistrement du document](Preferences_Editor/fr#Document.md)** est activée et enregistre un modèle. Affichez ensuite dans l\'Explorateur Windows le dossier du modèle enregistré à l\'aide d\'une vue de symboles. Vous devriez maintenant voir une capture d\'écran du modèle dans la vue des dossiers.

#### Compilation 

Pour compiler le FCStdThumbnail.dll

1.  Accédez au dossier source FreeCAD *\~\\src\\Tools\\thumbs\\ThumbnailProvider*
2.  Ouvrez l\'interface graphique de CMake
3.  Spécifiez là comme dossier source celui dans lequel vous vous trouvez actuellement.
4.  Utilisez le même dossier que le dossier de construction.
5.  Cliquez sur **Configure**
6.  Dans la boîte de dialogue qui apparaît, spécifiez le générateur en fonction de celui que vous souhaitez utiliser. Pour le MS Visual Studio standard, utilisez *Visual Studio xx 2yyy* où xx est la version du compilateur et 2yyy l\'année de sa sortie. Il est recommandé d\'utiliser l\'option par défaut *Use default native compilers*.**Remarque:** Il est important de spécifier la variante de bit correcte. Si vous avez la variante 64 bits de LibPack, vous devez également utiliser le compilateur x64.
7.  Cliquez sur **Generate**.
8.  Vous devriez maintenant avoir le fichier **ALL_BUILD.vcxproj** dans le dossier *\~\\src\\Tools\\thumbs\\ThumbnailProvider*. Double-cliquez dessus et l\'IDE MSVC s\'ouvrira.
9.  Dans la barre d\'outils de l\'EDI MSVC, assurez-vous que vous utilisez la cible de compilation *Release*.
10. Il y a une fenêtre appelée *Solution Explorer*. Faites un clic droit là-bas sur **ALL_BUILD** puis choisissez **Build**.
11. En conséquence, vous devriez maintenant avoir un **FCStdThumbnail.dll** dans le dossier *\~\\src\\Tools\\thumbs\\ThumbnailProvider\\release* que vous pouvez installer comme décrit ci-dessus.



## Compilation d\'Open Cascade 

LibPack est livré avec une version d\'[Open Cascade](https://en.wikipedia.org/wiki/Open_Cascade) qui convient à une utilisation générale. Cependant, dans certaines circonstances, vous pouvez souhaiter compiler avec une autre version d\'Open Cascade, comme l\'une de leurs versions officielles, ou un fork patché.

Lorsque vous compilez Open Cascade pour FreeCAD, notez qu\'il n\'y a aucune garantie que FreeCAD fonctionnera avec toutes les versions d\'Open Cascade. Notez également que lorsque vous utilisez la bibliothèque Netgen, vous devez utiliser la version NetGen approuvée pour la compilation avec la version d\'Open Cascade que vous souhaitez compiler.

Pour compiler :

-   Procurez-vous d\'abord le code source d\'Open Cascade, soit directement depuis [le dépôt git d\'Open Cascade](https://github.com/Open-Cascade-SAS/OCCT), soit en clonant le fork de quelqu\'un d\'autre, comme [le fork \"blobfish\"](https://gitlab.com/blobfish/occt) maintenu par un membre du forum FreeCAD [tanderson69](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=208).

-   Ensuite, ouvrez l\'interface graphique de CMake pour configurer le système de compilation d\'une manière similaire à la compilation de FreeCAD. Ces options CMake doivent être définies (ou ne pas être définies explicitement) :

  Nom de la variable                 Description                                                                                                                                                                                                                                                                                                                                                  Valeur par défaut
    
  3RDPARTY_DIR                       Le chemin vers les composants tiers. Il est recommandé d\'utiliser en entrée le dossier où se trouve votre LibPack utilisé. Laissez explicitement ce champ vide.                                                                                                                                                                                             vide
  3RDPARTY_DOXYGEN_EXECUTABLE        Le chemin vers l\'exécutable du composant tiers [Doxygen](https://fr.wikipedia.org/wiki/Doxygen). Il est recommandé d\'installer Doxygen. CMake le trouvera alors automatiquement.                                                                                                                                                                           vide
  3RDPARTY_FREETYPE_DIR              Le chemin vers le composant tiers nécessaire [Freetype](https://fr.wikipedia.org/wiki/FreeType). Il est recommandé d\'utiliser comme entrée le dossier où se trouve votre LibPack utilisé.                                                                                                                                                                   vide
  3RDPARTY_RAPIDJSON_DIR             Uniquement disponible si **USE_RAPIDJSON** est utilisé. Le chemin vers le composant tiers [RapidJSON](https://rapidjson.org/). Il est recommandé de NE PAS utiliser un dossier LibPack existant comme entrée. Vous pouvez utiliser le dossier RapidJSOn d\'un LibPack, mais copiez-le dans un nouveau dossier et utilisez ce nouveau dossier comme entrée.   vide
  3RDPARTY_TCL_DIR                   Le chemin vers le composant tiers nécessaire [TCL](https://fr.wikipedia.org/wiki/Tool_Command_Language). Il est recommandé de ne PAS utiliser un dossier LibPack existant comme entrée. Prenez par exemple une des [ces versions](https://github.com/teclab-at/tcltk/releases), extrayez-la et prenez-la comme dossier d\'entrée pour CMake.                 vide
  3RDPARTY_TK_DIR                    Le chemin vers le composant tiers nécessaire [TK](https://fr.wikipedia.org/wiki/Tk_(informatique)). Il est recommandé de ne PAS utiliser un dossier LibPack existant comme entrée. Prenez par exemple une des [ces versions](https://github.com/teclab-at/tcltk/releases), extrayez-la et prenez-la comme dossier d\'entrée pour CMake.                      vide
  3RDPARTY_VTK_DIR                   Uniquement disponible si **USE_VTK** est utilisé. Le chemin vers le composant tiers nécessaire [VTK](https://fr.wikipedia.org/wiki/VTK). Il est recommandé d\'utiliser le dossier en entrée où se trouve votre LibPack utilisé. Si vous utilisez un autre dossier, assurez-vous que vous n\'utilisez pas VTK 9.x ou plus récent.                             Vide
  BUILD_RELEASE_DISABLE_EXCEPTIONS   Désactive la gestion des exceptions pour les builds de version. Pour FreeCAD vous devez le régler sur **OFF**.                                                                                                                                                                                                                                               ON
  INSTALL_DIR                        Le dossier de sortie lors de la construction de la cible *INSTALL*. Si la construction a réussi, prenez les fichiers de ce dossier pour mettre à jour votre LibPack.                                                                                                                                                                                         Dossier d\'installation du programme par défaut de Windows
  INSTALL_DIR_BIN                    Le sous-dossier de sortie pour la DLL lors de la construction de la cible *INSTALL*. Vous devez le remplacer par **bin**.                                                                                                                                                                                                                                    win64/vc14/bin
  INSTALL_DIR_LIB                    Le sous-dossier de sortie pour les fichiers .lib lors de la construction de la cible *INSTALL*. Vous devez le remplacer par **lib**.                                                                                                                                                                                                                         win64/vc14/lib
  USE_RAPIDJSON                      Pour compiler Open Cascade avec le support de RapidJSON. L\'activation de cette option est obligatoire pour obtenir le support du format de fichier [glTF](https://fr.wikipedia.org/wiki/GlTF).                                                                                                                                                              OFF
  USE_VTK                            Pour compiler Open Cascade avec le support de VTK. L\'activation de cette option est optimale. Vous pouvez l\'utiliser pour construire le pont VTK d\'Open Cascade.                                                                                                                                                                                          OFF

-   Ouvrez le projet dans Visual Studio et construisez d\'abord les cibles ALL_BUILD puis INSTALL en mode *Release*.
-   Répétez la construction des deux cibles en mode *Debug*.

Pour compiler FreeCAD en utilisant Open Cascade auto-compilé, vous devez effectuer les opérations suivantes :

-   Copiez tous les dossiers de INSTALL_DIR dans votre dossier LibPack (écrasez les fichiers existants).
-   Passez au dossier LibPack et allez dans le sous-dossier *cmake*.
-   Ouvrez-y le fichier *OpenCASCADEDrawTargets.cmake* avec un éditeur de texte.
-   Cherchez-y les chemins absolus vers votre dossier LibPack et supprimez-les. Ainsi, par exemple, le chemin absolu*D:/FreeCADLibs_12.5.4_x64_VC17/lib/freetype.lib*devient simplement *freetype.lib*
-   Faites de même pour le fichier *OpenCASCADEVisualizationTargets.cmake*



## Compilation de Netgen 

LibPack est livré avec une version de [Netgen](https://ngsolve.org) qui a été testée pour être construite avec la version Open Cascade du LibPack. Le problème est que chaque nouvelle version de Netgen modifie l\'API. De même, chaque nouvelle version d\'Open Cascade fait de même. Par conséquent, on ne peut pas changer facilement la version de Netgen.

Cependant, vous pouvez tout de même construire Netgen. C\'est une tâche facile :

-   Tout d\'abord, procurez-vous le code source de Netgen, soit directement à partir de [Dépôt git de Netgen](https://github.com/NGSolve/netgen).
-   Ensuite, ouvrez l\'interface graphique CMake pour configurer le système de compilation de manière similaire à la construction de FreeCAD. Les options CMake suivantes doivent être définies :

  Nom de la variable     Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Valeur par défaut
    
  CMAKE_INSTALL_PREFIX   Le dossier de sortie lors de la compilation de la cible *INSTALL*. Si la compilation a réussi, prenez les fichiers de ce dossier pour mettre à jour votre LibPack.                                                                                                                                                                                                                                                                                                                                                                                                                                                            C:/netgen
  OpenCasCade_DIR        Le chemin vers les fichiers CMake d\'Open Cascade. Si vous avez compilé Open Cascade comme décrit dans la section [Compilation d\'Open Cascade](#Compilation_d.27Open_Cascade.md), vous pouvez utiliser le sous-dossier *cmake* du dossier que vous avez utilisé comme INSTALL_DIR. Sinon, utilisez le sous-dossier *cmake* de votre LibPack. Notez que le LibPack doit alors déjà contenir une compilation correcte d\'Open Cascade. Indépendamment du dossier que vous utilisez, vous devez maintenant y créer un sous-dossier *lib* et y copier les fichiers *freetype.lib* et *freetyped.lib* de votre LibPack.   vide
  USE_GUI                Mettez-le sur **OFF**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ON
  USE_NATIVE_ARCH        Mettez la valeur **OFF** ; ceci n\'est nécessaire et important que pour supporter les anciens processeurs qui n\'ont pas le jeu d\'instructions [AVX2](https://fr.wikipedia.org/wiki/Advanced_Vector_Extensions).                                                                                                                                                                                                                                                                                                                                                                                                             ON
  USE_OCC                Mettez-le sur **ON**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         OFF
  USE_PYTHON             Mettez-le sur **OFF**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ON
  USE_SUPERBUILD         Mettez-le sur **OFF**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ON
  ZLIB_INCLUDE_DIR       Le chemin vers le composant tiers nécessaire [zlib](https://fr.wikipedia.org/wiki/Zlib). Il est recommandé d\'utiliser en entrée le dossier où se trouve votre LibPack utilisé.                                                                                                                                                                                                                                                                                                                                                                                                                                               vide
  ZLIB_LIBRARY_DEBUG     Le chemin vers le fichier ZLib *zlibd.lib*. Il est situé dans le sous-dossier *lib* de votre dossier LibPack.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 vide
  ZLIB_LIBRARY_RELEASE   Le chemin vers le fichier ZLib *zlib.lib*. Il est situé dans le sous-dossier *lib* de votre dossier LibPack.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  vide

-   De plus, vous devez ajouter une nouvelle entrée CMake :

nom : *CMAKE_DEBUG_POSTFIX*, type : *string*, contenu : **\_d**Cela garantit que les noms de fichiers des bibliothèques de débogage ont un autre nom que les bibliothèques de publication et ne peuvent pas être échangés accidentellement par la suite.

-   Appuyez sur le bouton *Configure* dans CMake pour générer les fichiers \*.cmake.
-   Seulement nécessaire si des CPU plus anciens doivent être supportés qui n\'ont pas le jeu d\'instructions AVX2 :
    -   Recherchez dans votre dossier de construction Netgen le fichier *netgen-targets.cmake* et ouvrez-le avec un éditeur de texte. Supprimez le paramètre *;/arch:AVX2* dans l\'option INTERFACE_COMPILE_OPTIONS.
    -   Appuyez à nouveau sur le bouton *Configure* dans CMake.
-   Appuyez sur le bouton *Generate* dans CMake.
-   Ouvrez le projet dans Visual Studio et construisez d\'abord les cibles ALL_BUILD et ensuite INSTALL en mode *Release*.
-   Répétez la construction des deux cibles en mode *Debug*.

Pour compiler FreeCAD en utilisant l\'auto-compilation de Netgen, vous devez faire ce qui suit :

-   Copiez tous les dossiers de CMAKE_INSTALL_PREFIX dans votre dossier LibPack (écrasez les fichiers existants).



## Références

Voir aussi

-   [Compilation (accélération)](Compiling_(Speeding_up)/fr.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Windows/fr
