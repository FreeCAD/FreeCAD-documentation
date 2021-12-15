# Compile on Windows/fr
{{TOCright}}

Cette page explique étape par étape **comment compiler FreeCAD 0.19 ou plus récent sous Windows** en utilisant le compilateur MSVC de Microsoft. Pour des informations sur l\'utilisation de MSYS2/MinGW voir [Compiler sous MinGW](Compile_on_MinGW/fr.md). Pour les autres plateformes, voir [Compiler](Compiling/fr.md).

## Prérequis

La compilation de FreeCAD sous Windows nécessite plusieurs outils et bibliothèques.

### Requis

-   Un compilateur. FreeCAD est testé avec Visual Studio (MSVC). D\'autres compilateurs peuvent fonctionner, mais les instructions d\'utilisation ne sont pas incluses ici. Plus de détails dans [\#Compiler](#Compiler.md), ci-dessous.

-   [Git](http://git-scm.com/) (Il existe également des interfaces GUI disponibles pour Git, voir la section suivante.)

-   [CMake](https://cmake.org/download/) version 3.11.x ou plus récente.  *Astuce :* Choisir l\'option *Ajouter CMake au chemin du système pour tous les utilisateurs* lors de l\'installation de CMake rendra CMake accessible depuis l\'invite de commande Windows, ce qui peut être utile.

-   LibPack (également appelé FreeCADLibs). Il s\'agit d\'un package unique contenant toutes les bibliothèques nécessaires à la compilation de FreeCAD sous Windows. Téléchargez la version du LibPack qui correspond à la version de FreeCAD que vous voulez compiler. Pour compiler FreeCAD 0.19 ou la dernière version en développement 0.20, téléchargez [LibPack for 0.19/0.20](https://github.com/apeltauer/FreeCAD/releases/tag/LibPack_12.5.4) (64-bit seulement). Extrayez le LibPack à un endroit approprié. (Si votre ordinateur ne reconnaît pas l\'extension .7z, vous devez installer le programme [7-zip](https://www.7-zip.org)).  **Remarque** : Il est fortement recommandé de compiler FreeCAD avec la version du compilateur pour laquelle le LibPack est conçu. Par exemple, vous pourriez rencontrer des problèmes pour compiler FreeCAD 0.19 avec MSVC 15 parce que le LibPack pour 0.19 est conçu pour être construit avec MSVC 17.

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

### Compiler

Le compilateur par défaut (recommandé) est MS Visual Studio (MSVC). Bien qu\'il soit possible d\'utiliser d\'autres compilateurs, par exemple gcc via Cygwin ou MinGW, cela n\'est pas testé ni couvert ici.

Vous pouvez obtenir une version gratuite de MSVC (pour un usage individuel) en téléchargeant l \'[édition *Community* de MS Visual Studio](https://visualstudio.microsoft.com/vs/community/).

Pour ceux qui ne veulent pas installer l\'énorme MSVC uniquement pour avoir un compilateur, voir [CompileOnWindows - Réduire l\'espace disque](CompileOnWindows_-_Reducing_Disk_Footprint/fr.md).

**Remarque :** Bien que l\'édition *Community* de MSVC soit gratuite, pour utiliser l\'EDI pendant plus de 30 jours, vous devez créer un compte Microsoft. Si vous ne compilez qu\'en utilisant la ligne de commande, vous n\'avez pas besoin de l\'EDI et donc pas de compte Microsoft.

Comme alternative gratuite et OpenSource IDE, vous pouvez utiliser [KDevelop](https://www.kdevelop.org/download). Vous pouvez utiliser KDevelop pour modifier et écrire du code C ++, mais vous devez utiliser la ligne de commande pour compiler.

### Chemin de Configuration Système optionnel 

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
2.  Si vous y voyez un chemin comme *C:/Program Files/Python38/python.exe*, CMake a reconnu le Python qui est déjà installé sur votre PC, mais cette version n\'est pas compatible avec le LibPack. Étant donné que le LibPack inclut une version compatible de Python, modifiez les paramètres Python suivants dans CMake sur ses chemins (en supposant que le LibPack se trouve dans le dossier *D:\\FreeCAD-build\\FreeCADLibs\_12.5.2\_x64\_VC17*) :

![](images/CMake_Python_settings.png )

S\'il n\'y a pas d\'erreur à propos de Visual Studio ou Python, tout va bien, mais CMake ne connaît pas encore tous les paramètres nécessaires. Donc maintenant :

1.  Recherchez dans CMake la variable **FREECAD\_LIBPACK\_DIR** et spécifiez l\'emplacement du dossier LibPack que vous avez téléchargé précédemment.
2.  Seulement si vous compilez FreeCAD 0.19, cherchez la variable **BUILD\_QT5** et activez cette option.
3.  Cliquez à nouveau sur **Configure**.

Il ne devrait plus y avoir d'erreurs. Si vous continuez à rencontrer des erreurs que vous ne pouvez pas diagnostiquer, allez sur le [Forum Install/Compile](https://forum.freecadweb.org/viewforum.php?f=4) de FreeCAD. Si CMake a procédé correctement, cliquez sur **Generate**. Une fois cela fait, vous pouvez fermer CMake et démarrer la compilation de FreeCAD à l\'aide de Visual Studio. Cependant, pour la première compilation, gardez-le ouvert au cas où vous voudriez ou auriez besoin de changer certaines options pour le processus de construction.

**Remarque :** Lors de la compilation de FreeCAD 0.19, la variable CMake **BUILD\_ENABLE\_CXX\_STD** sera fixée à **C++14** alors que pour FreeCAD 0.20 elle sera fixée à **C++17**. Ceci est dû au fait que FreeCAD 0.20 requiert au moins la version 17 du standard du langage C++. Donc quand vous avez compilé la dernière fois FreeCAD 0.19, il est nécessaire de relancer CMake pour FreeCAD 0.20 pour changer le standard du langage C++.

### Options pour le procédé de compilation 

Le système de compilation CMake vous permet de contrôler certains aspects du processus de compilation. En particulier, vous pouvez activer et désactiver certaines fonctionnalités ou modules à l\'aide des variables CMake.

Voici la description de certaines de ces variables :

  Nom de la variable                       Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Valeur par défaut
  ---------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------
  BUILD\_XXX                               Compile FreeCAD avec le composant XXX. Si vous ne voulez/nécessitez pas compiler par exemple l\'atelier *OpenSCAD*, désactivez la variable *BUILD\_OPENSCAD*. FreeCAD n\'aura alors pas cet atelier. **Remarque:** Certains composants sont nécessaires pour d\'autres composants. Si vous décochez par exemple *BUILD\_ROBOT*, CMake vous informera qu\'alors le composant *Path* ne pourra pas être compilé correctement. Vérifiez donc la sortie de CMake après avoir modifié une option BUILD\_XXX!                                                                                                                                                                                          ca dépend
  BUILD\_ENABLE\_CXX\_STD                  La version du standard du langage C++. **C++14** est la plus élevée possible pour FreeCAD 0.19 alors qu\'au moins **C++17** est nécessaire pour FreeCAC 0.20. Voir aussi la note dans la section [Construire avec Visual Studio 15 (2017) et 16 (2019)](#Version_de_Build.md)                                                                                                                                                                                                                                                                                                                                                                                                            ca dépend
  CMAKE\_INSTALL\_PREFIX                   Le dossier de sortie lors de la construction de la cible *INSTALL*, voir aussi la section [Exécution et installation de FreeCAD](#Ex.C3.A9cution_et_installation_de_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Le dossier d\'installation par défaut du programme de Windows
  FREECAD\_COPY\_DEPEND\_DIRS\_TO\_BUILD   Copie les bibliothèques dépendantes nécessaires à l\'exécution de FreeCAD.exe dans le dossier de construction. Voir aussi la section [Exécution et installation de FreeCAD](#Ex.C3.A9cution_et_installation_de_FreeCAD.md). **Remarque:** les options FREECAD\_COPY\_XXX n\'apparaissent que si les bibliothèques n\'ont pas déjà été copiées. Donc lorsque vous passez à une autre version de LibPack, il est important de supprimer tous les dossiers de votre dossier de construction, à l\'exception du dossier LibPack. Dans CMake, supprimez le cache et démarrez comme si vous compiliez pour la première fois et vous obtiendrez les options FREECAD\_COPY\_XXX.   OFF
  FREECAD\_COPY\_LIBPACK\_BIN\_TO\_BUILD   Copie les binaires LibPack nécessaires à l\'exécution de FreeCAD.exe dans le dossier de compilation. Voir aussi la section [Exécution et installation de FreeCAD](#Ex.C3.A9cution_et_installation_de_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                        OFF
  FREECAD\_COPY\_PLUGINS\_BIN\_TO\_BUILD   Copie les fichiers plugins de Qt nécessaires à l\'exécution de FreeCAD.exe dans le dossier de compilation. Voir aussi la section [Exécution et installation de FreeCAD](#Ex.C3.A9cution_et_installation_de_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                  OFF
  FREECAD\_LIBPACK\_USE                    Active ou désactive l\'utilisation du LibPack de FreeCAD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ON
  FREECAD\_LIBPACK\_DIR                    Répertoire où se trouve le LibPack                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Dossier du code source de FreeCAD
  FREECAD\_RELEASE\_PDB                    Créer des bibliothèques de débogage également pour les builds de version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ON
  FREECAD\_USE\_MP\_COMPILE\_FLAG          Ajoute l\'option /MP (multiprocesseur) aux projets Visual Studio, permettant des accélérations sur les CPU multi-cœurs. Cela peut accélérer considérablement les builds sur les processeurs modernes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            OFF

## Compilation de FreeCAD 

En fonction de votre compilateur, le processus de construction de FreeCAD sera légèrement différent. Dans les sections suivantes, vous décrivez les flux de travail connus. Si vous construisez avec Qt Creator, passez à [Compiler avec Qt Creator](#Compiler_avec_Qt_Creator.md), sinon, procédez directement :


<div class="mw-collapsible mw-collapsed toccolours">

### Build avec Visual Studio 15 (2017), 16 (2019), and 17 (2022) 


<div class="mw-collapsible-content">

#### Version de Build 

1.  Démarrez l\'IDE Visual Studio. Cela peut être effectué en appuyant sur le bouton *Ouvrir un projet* dans l\'interface graphique de CMake ou en double-cliquant sur le fichier *FreeCAD.sln* que vous trouvez dans votre dossier de construction.
2.  Dans la barre d'outils de l'EDI MSVC, assurez-vous que vous utilisez pour la première compilation *Release*.
3.  Il y a une fenêtre appelée *Solution Explorer*. Elle répertorie toutes les cibles de compilation possibles. Pour démarrer une compilation complète, faites un clic droit sur la cible **ALL\_BUILD** puis choisissez **Build**.

Cela va prendre pas mal de temps.

Pour compiler un FreeCAD prêt à l'emploi, compilez la cible *INSTALL*, voir la section [Exécution et installation de FreeCAD](#Exécution_et_installation_de_FreeCAD.md).

Si vous n\'obtenez aucune erreur, vous avez terminé. **Félicitations !** Vous pouvez quitter MSVC ou le garder ouvert.

Remarque : FreeCAD 0.20 nécessite au moins la version 17 du langage standard C++ mais le composant tiers *flann* du LibPack n\'est pas encore prêt pour cela. Par conséquent, vous aurez des erreurs de compilation pour la cible *ReverseEngineering*. Pour résoudre ce problème, faites un clic droit sur cette cible dans l\'explorateur de solutions MSVC et sélectionnez dans le menu contextuel la dernière entrée *Properties*. Dans la boîte de dialogue qui apparaît, changez le *C++ Language Standard* en *ISO C++14*. Enfin, recompilez la cible **ALL\_BUILD**.

#### Build de débogage 

Pour une version de débogage, il est nécessaire d\'utiliser le Python inclus dans le LibPack. Pour assurer cela :

1.  Recherchez \"Python\" dans l\'interface graphique de CMake
2.  Si vous y voyez un chemin comme \'C:/Program Files/Python38/python.exe\'\', CMake a reconnu le Python qui est installé sur votre PC et non celui du LibPack. Dans ce cas, adaptez ces différents paramètres Python dans CMake à cela (en supposant que le LibPack se trouve dans le dossier *D:\\FreeCAD-build\\FreeCADLibs\_12.5.2\_x64\_VC17*) :

![](images/CMake_Python_settings.png )

Maintenant

1.  Démarrez l\'IDE de Visual Studio. Cela peut être fait en appuyant sur le bouton *Open Project* dans l\'interface graphique de CMake ou en double-cliquant sur le fichier «FreeCAD.sln» que vous trouvez dans votre dossier de construction.
2.  Dans la barre d\'outils de MSVC IDE, assurez-vous que vous utilisez pour la première compilation *Debug*.
3.  Il existe une fenêtre appelée *Solution Explorer*. Il répertorie toutes les cibles de compilation possibles. Pour démarrer une compilation complète, faites un clic droit sur la cible **ALL\_BUILD** puis choisissez **Build** dans le menu contextuel.

Cela prendra maintenant beaucoup de temps. S\'il n\'y a pas eu d\'erreurs de compilation, vous pouvez démarrer la compilation de débogage :

1.  Faites un clic droit sur la cible **FreeCADMain** puis choisissez **Set as Startup Project** dans le menu contextuel.
2.  Cliquez enfin dans la barre d\'outils sur le bouton avec le triangle vert nommé **Local Windows Debugger**.

Cela lancera la version de débogage de FreeCAD et vous pourrez utiliser MSVC IDE pour le déboguer.

#### Ressource vidéo 

Tutoriel en anglais qui commence par la configuration dans CMake Gui et continue jusqu\'à la commande \Build\ dans Visual Studio 16 2019 est disponible non répertorié sur YouTube à [Tutorial: Build FreeCAD from source on Windows 10](https://youtu.be/s4pHvlDOSZQ).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Construire avec Qt Creator (obsolète) 


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
3.  Dans l\'explorateur de fichiers de Winddows Shift+Cliquez-droit sur votre dossier de construction et utilisez-le dans le menu contextuel \'\'Invite de commandes ici \'.
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

La méthode 2 est la plus simple, car elle assure automatiquement que toutes les bibliothèques requises pour exécuter FreeCAD.exe se trouvent dans le bon dossier. FreeCAD.exe et les bibliothèques seront sortis dans le dossier que vous avez spécifié dans la variable CMake *CMAKE\_INSTALL\_PREFIX*.

Pour la méthode 1, vous devez placer les bibliothèques dans le dossier *bin* de votre dossier de construction (où se trouve FreeCAD.exe). Cela peut être facilement fait en utilisant les variables CMake en option :

1.  Ouvrez l\'interface graphique de CMake.
2.  Recherchez et cochez la variable *FREECAD\_COPY\_DEPEND\_DIRS\_TO\_BUILD*. S\'il n\'y a pas une telle option, les bibliothèques ont déjà été copiées, voir la [description des options](#Options_pour_le_procédé_de_compilation.md).
3.  Recherchez et cochez la variable *FREECAD\_COPY\_LIBPACK\_BIN\_TO\_BUILD*.
4.  Recherchez et cochez la variable *FREECAD\_COPY\_PLUGINS\_BIN\_TO\_BUILD*.
5.  Cliquez sur **Configurer**. A la fin de la configuration, CMake copiera automatiquement les bibliothèques nécessaires du dossier LibPack.

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

1.  Ouvrez l\'EDI MSVC en double-cliquant sur le fichier *FreeCAD.sln* ou sur le fichier *ALL\_BUILD.vcxproj* dans votre dossier de construction.
2.  Continuer à l\'étape 2 de la section [Construire avec Visual Studio 15 2017](#Construire_avec_Visual_Studio_15_2017.md).

## Outils

Pour rejoindre le développement FreeCAD, vous devez compiler et installer les outils suivants :

### Le plugin Qt Designer 

FreeCAD utilise [Qt](https://fr.wikipedia.org/wiki/Qt) comme boîte à outils pour son interface utilisateur. Toutes les boîtes de dialogue sont configurées dans des fichiers UI qui peuvent être modifiés à l\'aide du programme [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html). Il fait partie de toute installation Qt et également inclus dans le LibPack. FreeCAD a son propre ensemble de widgets Qt pour fournir des fonctionnalités spéciales comme l\'ajout d\'une unité aux champs de saisie et pour définir les propriétés des préférences.

#### Installation

Pour que Qt Designer connaisse les widgets FreeCAD, vous devez

1.  Téléchargez le fichier _.)
2.  Extraire le fichier DLL dans le ZIP et le copier

-   Si vous utilisez le LibPack: dans le dossier *\~\\FreeCADLibs\_12.5.2\_x64\_VC17\\bin\\designer* Puisqu\'il n\'y aura qu\'un dossier *bin* et vous devez d\'abord créer le dossier sous-dossier *designer*.
-   Si vous avez une installation Qt complète: vous pouvez choisir entre le dossier *C:\\Qt\\5.15.2\\msvc2019\_64\\plugins\\designer*ou*C:\\Qt\\5.15.2\\msvc2019\_64\\bin\\designer* (vous devez d\'abord créer le sous-dossier *designer*). (adaptez les chemins à votre installation!).

(Re)démarrez Qt Designer et vérifiez son menu **Help → Plugins**. Si le plugin **FreeCAD\_widgets.dll** est répertorié comme étant chargé, vous pouvez maintenant concevoir et modifier les fichiers .ui de FreeCAD, sinon vous devez [compiler](#Compilation.md) vous-même la DLL.

Si vous préférez utiliser _ vous-même la DLL.

#### Compilation

La DLL ne peut pas être chargée en tant que plug-in si elle a été compilée en utilisant une autre version de Qt que celle sur laquelle est basé Qt Designer/Qt Creator. Dans ce cas, vous devez compiler vous-même la DLL. Cela se fait de la manière suivante :

1.  Accédez au dossier source FreeCAD *\~\\src\\Tools\\plugins\\widget*
2.  Ouvrez une invite de commande MSVC x64 à l\'aide du menu Démarrer de Windows et modifiez-la dans le dossier ci-dessus. Il est important que ce soit la version x64 de l\'invite de commande MSVC !
3.  Exécutez cette commande *D:\\FreeCAD-build\\FreeCADLibs\_12.5.2\_x64\_VC17\\bin\\qmake -t vclib plugin.pro* pour une installation complète de Qt c\'est *C:\\Qt\\5.15.2\\msvc2019\_64\\bin\\qmake -t vclib plugin.pro* (adaptez les chemins à votre installation! )
4.  L\'appel de *qmake* a créé le fichier **FreeCAD\_widgets.vcxproj** dans le dossier *\~\\src\\Tools\\plugins\\widget*. Double-cliquez dessus et l\'IDE MSVC s\'ouvrira.
5.  Dans la barre d\'outils de l\'EDI MSVC, assurez-vous que vous utilisez la cible de compilation *Release*.
6.  Il y a une fenêtre appelée *Solution Explorer*. Faites un clic droit là-bas sur **FreeCAD\_widgets** puis choisissez **Build**.
7.  En conséquence, vous devriez maintenant avoir un **FreeCAD\_widgets.dll** dans le dossier *\~\\src\\Tools\\plugins\\widget\\release* que vous pouvez installer comme plugin comme décrit ci-dessus.

### Fournisseur de vignettes (Thumbnail) 

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
8.  Vous devriez maintenant avoir le fichier **ALL\_BUILD.vcxproj** dans le dossier *\~\\src\\Tools\\thumbs\\ThumbnailProvider*. Double-cliquez dessus et l\'IDE MSVC s\'ouvrira.
9.  Dans la barre d\'outils de l\'EDI MSVC, assurez-vous que vous utilisez la cible de compilation *Release*.
10. Il y a une fenêtre appelée *Solution Explorer*. Faites un clic droit là-bas sur **ALL\_BUILD** puis choisissez **Build**.
11. En conséquence, vous devriez maintenant avoir un **FCStdThumbnail.dll** dans le dossier *\~\\src\\Tools\\thumbs\\ThumbnailProvider\\release* que vous pouvez installer comme décrit ci-dessus.

## Compiler OpenCASCADE 

Libpack standard est livré avec une version d\'OpenCASCADE qui convient à un usage général. Cependant, dans certaines circonstances, vous pouvez souhaiter compiler avec une version alternative d\'OpenCASCADE, comme une de leurs versions officielles, ou un fork patché. Notez qu\'il n\'y a aucune garantie que FreeCAD fonctionnera avec toutes les versions d\'OpenCASCADE, et l\'utilisation d\'une version autre que celle de Libpack est réservée aux utilisateurs avancés. Notez également que si vous utilisez la bibliothèque Netgen, elle utilise OpenCASCADE pour certaines de ses fonctionnalités et doit être compilée avec la même version d\'OpenCASCADE que celle que vous utilisez lors de la compilation de FreeCAD.

Le processus de compilation d\'une version personnalisée d\'OpenCASCADE est similaire à celui de FreeCAD, et peut utiliser le Libpack FreeCAD que vous avez déjà téléchargé pour fournir les dépendances tierces dont il a besoin (Freetype et Tcl/Tk).

Obtenez d\'abord le code source d\'OpenCASCADE, soit directement à partir de la page de publication à [OpenCASCADE.org](https://old.opencascade.com/content/latest-release), via [/occt.git git](https://git.dev.opencascade.org/repos) ou en clonant le fork de quelqu\'un d\'autre, comme [le fork \"blobfish\"](https://gitlab.com/blobfish/occt) maintenu par le membre du forum FreeCAD [tanderson69](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=208).

Ensuite, utilisez CMake pour configurer le système de compilation de la même manière que pour la compilation de FreeCAD. Les principales options de CMake pour OpenCASCADE sont les suivantes :

-   **3RDPARTY\_DIR** - L\'emplacement de vos bibliothèques tierces, généralement dans le répertoire Libpack de FreeCAD
-   **INSTALL\_DIR** - Où installer les bibliothèques terminées. Une bonne pratique consiste à utiliser un répertoire isolé sur votre système, plutôt que d\'installer globalement ou d\'écraser la version du Libpack.

Enfin, ouvrez le projet dans Visual Studio et compilez les cibles ALL\_BUILD puis INSTALLER.

Une fois que vous avez généré les DLL appropriées pour OpenCASCADE (il y en a beaucoup), vous devrez recompiler FreeCAD. Ouvrez CMake et configurez les répertoires source et de compilation d\'une version FreeCAD comme indiqué ci-dessus. C\'est généralement une bonne idée d\'utiliser un nouveau répertoire de compilation pour cette version alternative d\'OpenCASCADE afin qu\'il soit facile de revenir à votre ancienne version de FreeCAD si quelque chose ne va pas, et de mettre en place un répertoire d\'installation afin que vous puissiez vous assurer que les bonnes bibliothèques sont en place. En plus des variables CMake décrites ci-dessus, définissez la variable OpenCASCADE\_DIR à l\'emplacement du dossier cmake contenant vos informations de construction OpenCASCADE. Par exemple:

CMAKE_INSTALL_PREFIX    C:/Users/JaneDoe/Work/FreeCAD_occt751-install/
OpenCASCADE_DIR         C:/Users/JaneDoe/Work/opencascade-7.5.1-install/cmake/

Une fois que vous avez utilisé CMake pour générer les fichiers de compilation pour FreeCAD, ouvrez-le dans Visual Studio, compilez-le, puis exécutez la compilation sur la cible INSTALL.

## Références

Voir aussi

-   [Compilation (accélération)](Compiling_(Speeding_up)/fr.md).







_ _

---
[documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > Compile on Windows/fr
