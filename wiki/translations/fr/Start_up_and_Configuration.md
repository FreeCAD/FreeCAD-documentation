# Start up and Configuration/fr
**Dans la version 0.20 de FreeCAD, l'emplacement par défaut des fichiers de configuration, de données et de cache du programme a été modifié pour Linux.<br>
Voir les [Notes de version 0.20](Release_notes_0.20/fr#Noyau.md) pour plus d'informations. Cette page n'a pas encore été mise à jour en conséquence.**






## Présentation

Cette page montre les différentes façons de lancer FreeCAD et ses éléments de configuration les plus importants.



## Démarrer FreeCAD en ligne de commande 

FreeCAD peut être lancé normalement en double-cliquant sur son icône qui est sur le bureau, ou en le sélectionnant dans le menu de démarrage, mais il peut également être lancé directement à partir de la ligne de commande. Cela vous permet de changer les options de démarrage par défaut.



### Utilisation des options en ligne de commande sans utiliser le shell 

-   Sur Ubuntu, vous pouvez créer une icône de bureau et modifier leurs propriétés. Ajoutez les options de ligne de commande séparées par des espaces derrière le nom du programme dans le champ \"Commande\".
-   Sous Windows, créez un raccourci et modifiez ses propriétés. Ajoutez les options de ligne de commande séparées par des espaces dans le champ \"Cible\".



### Options disponibles en ligne de commande 

Les options en ligne de commande sont l\'objet de fréquents changements. Il est donc sage de vérifier les options de votre version courante en tapant :

FreeCAD --help

La réponse vous permet de connaître les paramètres disponibles. Pour FreeCAD version 1.0, ce sont les suivants :

 Usage: FreeCAD [options] File1 File2 ...
 
 Allowed options:
 
 Generic options:
   -v [ --version ]          Prints version string
   --verbose                 Prints verbose version string
   -h [ --help ]             Prints help message
   -c [ --console ]          Starts in console mode
   --response-file arg       Can be specified with '@name', too
   --dump-config             Dumps configuration
   --get-config arg          Prints the value of the requested configuration key
   --set-config arg          Sets the value of a configuration key
   --keep-deprecated-paths   If set then config files are kept on the old 
                             location
 
 Configuration:
   -l [ --write-log ]        Writes FreeCAD.log to the user directory.
   --log-file arg            Unlike --write-log this allows logging to an 
                             arbitrary file
   -u [ --user-cfg ] arg     User config file to load/save user settings
   -s [ --system-cfg ] arg   System config file to load/save system settings
   -t [ --run-test ] arg     Run a given test case (use 0 (zero) to run all 
                             tests). If no argument is provided then return list
                             of all available tests.
   -r [ --run-open ] arg     Run a given test case (use 0 (zero) to run all 
                             tests). If no argument is provided then return list
                             of all available tests.  Keeps UI open after 
                             test(s) complete.
   -M [ --module-path ] arg  Additional module paths
   -P [ --python-path ] arg  Additional python paths
   --single-instance         Allow to run a single instance of the application
   --safe-mode               Force enable safe mode
   --pass arg                Ignores the following arguments and pass them 
                             through to be used by a script

Dans le tableau suivant, les options sélectionnées sont décrites plus en détail :

++++
| Option longue                             | [Nom de la variable de configuration](#Configuration.md) correspondante | Synopsis                                                                                                                                                                                                                                                                                                                    |
+===========================================+=================================================================================+=============================================================================================================================================================================================================================================================================================================================+
|                            | UserParameter                                                                   | Nom de fichier ou chemin relatif qui se termine par un nom de fichier. La valeur par défaut est `user.cfg`.                                                                                                                                                                                          |
| `--user-cfg <filename>`          |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
|                                        |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
++++
|                            | Préfèrée à AdditionalModulePaths                                                | Répertoire qui contient des modules. Cette option peut être donnée à plusieurs reprises pour spécifier plusieurs répertoires.                                                                                                                                                                                               |
| `--module-path <dir>`            |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
|                                        |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
++++
|                            | La plus part                                                                    | Affiche la valeur demandée dans une fenêtre de dialogue contextuelle. Quitte après confirmation avec **OK**. Ne peut pas être utilisé à plusieurs reprises. Si un nom de variable inconnu/illégal est utilisé, la réponse est vide. L\'indicateur `--console` n\'est pas respecté. |
| `--get-config <config-var-name>` |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
|                                        |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
++++

Les options peuvent être rédigées sous deux formes : `--long-option arg` et `--long-option<nowiki>=</nowiki>arg`.



### Fichiers de configuration et réponse 

Vous pouvez lire certaines options de FreeCAD à partir d\'un fichier de configuration. Ce fichier doit être dans le répertoire **/bin** et doit être nommé **FreeCAD.cfg**. Notez que les options spécifiées en ligne de commande remplacent le fichier de configuration !

Certains systèmes d\'exploitation ne permettent qu\'un nombre de caractères assez limité en ligne de commande. La façon courante de contourner cette limitation, est l\'utilisation des fichiers *response*. Un fichier *response* n\'est qu\'un fichier de configuration, qui utilise la même syntaxe qu\'en ligne de commande. Si la ligne de commande spécifie un nom de fichier *response* à utiliser, il est chargé, analysé et ajouté à la ligne de commande :

    FreeCAD @ResponseFile.txt 

ou :

    FreeCAD --response-file=ResponseFile.txt

ou :

    FreeCAD --response-file ResponseFile.txt



### Options cachées 

Il y a des options qui sont invisibles à l\'utilisateur. Ces options sont, par exemple, les paramètres X-Window analysés par le système Windows :

-   **-display display**, définit l\'affichage X (valeur par défaut est \$DISPLAY).
-   **-geometry geometry**, la géométrie fixe de la première fenêtre client qui est affichée.
-   **-fn or -font font**, définit la police de l\'application. La police doit être spécifié en utilisant la description de police logique X.
-   **-bg or -background color**, définit la couleur de fond par défaut et une palette d\'application (tons clairs et foncés sont calculés).
-   **-fg or -foreground color**, définit la couleur de premier plan par défaut.
-   **-btn or -button color**, définit la couleur des boutons par défaut.
-   **-name name**, définit le nom de l\'application.
-   **-title title**, définit le titre de l\'application.
-   **-visual TrueColor**, force l\'application à utiliser un visuel TrueColor sur un affichage 8-bits.
-   **-ncols count**, limite le nombre de couleurs allouées dans le cube de couleur sur un écran 8-bits, si l\'application utilise la spécification de couleur QApplication::ManyColor. Si le nombre est 216, un cube 6x6x6 couleurs est utilisé (soit 6 niveaux de rouge, 6 de vert, et 6 de bleu); pour d\'autres valeurs un cube à peu près proportionnel à un cube 2x3x1 couleurs est utilisé.
-   **-cmap**, provoque l\'installation d\'une carte de couleurs réservée à l\'application, sur un affichage 8-bits.



### Executer FreeCAD sans interface graphique utilisateur 

FreeCAD est généralement compilé avec deux exécutables : un exécutable compatible avec l\'interface graphique, appelé **FreeCAD** ou **freecad**, et un exécutable sans tête, appelé **FreeCADCmd** ou **freecadcmd**. FreeCAD peut être utilisé en mode console en utilisant le commutateur `--console` (qui est le comportement par défaut de **FreeCADCmd**) :

FreeCAD --console

En mode console, aucune interface utilisateur graphique ne sera affichée et vous serez invité à utiliser l\'interpréteur Python : `>>>>`. À partir de cette invite, vous disposez des mêmes fonctionnalités que l\'interpréteur Python qui fonctionne dans l\'interface graphique de FreeCAD, et vous avez accès à tous les modules et plugins de FreeCAD, à l\'exception du module FreeCADGui. Sachez que les modules qui dépendent de FreeCADGui peuvent également être indisponibles.

Pour en savoir plus sur le mode console ou le mode sans tête, consultez [FreeCAD sans GUI](Headless_FreeCAD/fr.md).



### Exécution de modules, macros et scripts 

++++
| Type de fichier | Système          | Exemple en lignes de commande                                                                                                      |
+=================+==================+====================================================================================================================================+
| Module          | Windows          |                                                                                                                     |
|                 |                  | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" -M "C:\FreeCAD\Mod\Draft"`                                                    |
|                 |                  |                                                                                                                                 |
++++
|                 | Linux            |                                                                                                                     |
|                 |                  | `FreeCAD_0.19 -M ~/.FreeCAD/Mod/Draft`                                                                                    |
|                 |                  |                                                                                                                                 |
++++
|                 | Linux (AppImage) |                                                                                                                     |
|                 |                  | `path/to/FreeCADXXX.AppImage -M ~/.FreeCAD/Mod/Draft`                                                                     |
|                 |                  |                                                                                                                                 |
++++
|                 |                  |                                                                                                                                    |
++++
| .FCMacro or .py | Windows          |                                                                                                                     |
|                 |                  | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"` |
|                 |                  |                                                                                                                                 |
++++
|                 | Linux            |                                                                                                                     |
|                 |                  | `FreeCAD_0.19 ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                                |
|                 |                  |                                                                                                                                 |
++++
|                 | Linux (AppImage) |                                                                                                                     |
|                 |                  | `path/to/FreeCADXXX.AppImage ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                 |
|                 |                  |                                                                                                                                 |
++++

Voir [Macro at Startup](Macro_at_Startup/fr.md) pour savoir comment configurer une macro pour qu\'elle s\'exécute automatiquement au démarrage de FreeCAD.



## Variables d\'environnement 

FreeCAD prend en charge les variables d\'environnement suivantes, qui peuvent être utilisées pour configurer les répertoires: {{Version/fr|0.19}}

++++
| Variable d\'environnement    | [Nom de la variable de configuration](#Ensemble_de_configuration.md) correspondante | Synopsis                                                                                                                                                                        |
+==============================+=============================================================================================+=================================================================================================================================================================================+
|               | UserHomePath                                                                                | Répertoire \"de base\" de FreeCAD pour conserver les données des utilisateurs locaux.                                                                                           |
| `FREECAD_USER_HOME` |                                                                                             |                                                                                                                                                                                 |
|                           |                                                                                             |                                                                                                                                                                                 |
++++
|               | UserAppData                                                                                 | S\'il n\'est pas défini, la valeur par défaut est `FREECAD_USER_HOME/.FreeCAD` mais uniquement si `FREECAD_USER_HOME` est défini. |
| `FREECAD_USER_DATA` |                                                                                             |                                                                                                                                                                                 |
|                           |                                                                                             |                                                                                                                                                                                 |
++++
|               | AppTempPath                                                                                 | S\'il n\'est pas défini, la valeur par défaut est `FREECAD_USER_HOME/temp` mais uniquement si `FREECAD_USER_HOME` est défini.     |
| `FREECAD_USER_TEMP` |                                                                                             |                                                                                                                                                                                 |
|                           |                                                                                             |                                                                                                                                                                                 |
++++

Si le chemin spécifié n\'existe pas, le paramètre est ignoré!

Les variables d\'environnement ci-dessus sont destinées à être utilisées pour réaliser un environnement FreeCAD *portable*. Pour un exemple d\'utilisation des variables d\'environnement à partir de la ligne de commande sous Linux, reportez-vous aux [notes pour les utilisateurs Linux sur la page de téléchargement](Download/fr#Note_aux_utilisateurs_de_GNU.2FLinux.md).

### `HOME`

FreeCAD utilise [Qt](Third_Party_Libraries/fr#Qt.md), qui respecte la variable d\'environnement `HOME`. Ainsi, le paramètre `HOME` peut être utilisé pour spécifier le répertoire de base des fichiers de configuration liés à Qt (`.config/FreeCAD/FreeCAD.conf`).

FreeCad lui-même ne respecte pas la variable d\'environnement `HOME` (car cela détermine le répertoire personnel de l\'utilisateur à partir d\'une API système de niveau inférieur). Utilisez `FREECAD_USER_HOME` pour cela.

### `TMPDIR` 

Le répertoire temporaire par défaut est **/tmp/**. La variable d\'environnement `TMPDIR` peut être utilisée pour remplacer la valeur par défaut. (*Editeur:priorité?*).



### Bibliothèques

Certaines bibliothèques doivent appeler des variables d\'environnement système. Parfois, lorsqu\'il y a un problème avec une installation de FreeCAD, c\'est parce qu\'une variable d\'environnement est absente ou incorrecte. Par conséquent, certaines variables importantes sont dupliquées dans la configuration et enregistrées dans le fichier de log.

**Python**

-   PYTHONPATH
-   PYTHONHOME
-   TCL_LIBRARY
-   TCLLIBPATH

**OpenCascade**

-   CSF_MDTVFontDirectory
-   CSF_MDTVTexturesDirectory
-   CSF_UnitsDefinition
-   CSF_UnitsLexicon
-   CSF_StandardDefaults
-   CSF_PluginDefaults
-   CSF_LANGUAGE
-   CSF_SHMessage
-   CSF_XCAFDefaults
-   CSF_GraphicShr
-   CSF_IGESDefaults
-   CSF_STEPDefaults



## Configuration

A chaque démarrage, FreeCAD examine son environnement, ainsi que les paramètres en ligne de commande. Il construit un **ensemble de configuration** qui détient le cœur des informations d\'exécution. Ces informations sont ensuite utilisées pour déterminer l'emplacement où enregistrer les données des utilisateurs ou des fichiers journaux. Il est également très important pour les analyses post-mortem. Par conséquent, il est enregistré dans le fichier des logs.



### Informations relatives à l\'utilisateur 

L\'appel se fait de la manière suivante :

path = FreeCAD.ConfigGet("UserAppData")

+++++
| Nom de la variable de configuration | Synopsis                                                         | Exemple Windows                                                            | Exemple Linux                                                                                                                      |
+=====================================+==================================================================+============================================================================+====================================================================================================================================+
| UserAppData                         | Chemin où FreeCAD met les données utilisateur de l\'application. |                                                             |                                                                                                                     |
|                                     |                                                                  | **C:\Documents and Settings\username\AppData\FreeCAD**            | **/home/username/.FreeCAD**                                                                                               |
|                                     |                                                                  |                                                                         |                                                                                                                                 |
|                                     |                                                                  |                                                                  |                                                                                                                          |
|                                     |                                                                  | <hr />                                                                     | <hr />                                                                                                                             |
|                                     |                                                                  |                                                                         |                                                                                                                                 |
|                                     |                                                                  | *Chemin court :***%APPDATA%\FreeCAD**               | *Chemin court :***~/.FreeCAD**                                                                              |
+++++
| UserParameter                       | Chemin où FreeCAD met les fichier utilisateur de l\'application. |                                                             |                                                                                                                     |
|                                     |                                                                  | **C:\Documents and Settings\username\AppData\FreeCAD\user.cfg**   | **/home/username/.config/FreeCAD/user.cfg**                                                                               |
|                                     |                                                                  |                                                                         |                                                                                                                                 |
|                                     |                                                                  |                                                                  |                                                                                                                          |
|                                     |                                                                  | <hr />                                                                     | <hr />                                                                                                                             |
|                                     |                                                                  |                                                                         |                                                                                                                                 |
|                                     |                                                                  | *Chemin court :***%APPDATA%\FreeCAD\user.cfg**      | *Chemin court :***~/.config/FreeCAD/user.cfg** or **$HOME/.config/FreeCAD/user.cfg** |
+++++
| SystemParameter                     | Fichier où sont les données de l\'application.                   |                                                             |                                                                                                                     |
|                                     |                                                                  | **C:\Documents and Settings\username\AppData\FreeCAD\system.cfg** | **/home/username/.config/FreeCAD/system.cfg**                                                                             |
|                                     |                                                                  |                                                                         |                                                                                                                                 |
|                                     |                                                                  |                                                                  |                                                                                                                          |
|                                     |                                                                  | <hr />                                                                     | <hr />                                                                                                                             |
|                                     |                                                                  |                                                                         |                                                                                                                                 |
|                                     |                                                                  | *Chemin court :***%APPDATA%\FreeCAD\system.cfg**    | *Chemin court :***~/.FreeCAD/system.cfg** or **$HOME/.FreeCAD/system.cfg**           |
+++++
| UserHomePath                        | Chemin racine de l\'utilisateur courant.                         |                                                             |                                                                                                                     |
|                                     |                                                                  | **C:\Documents and Settings\username**                            | **/home/username**                                                                                                        |
|                                     |                                                                  |                                                                         |                                                                                                                                 |
|                                     |                                                                  |                                                                  |                                                                                                                          |
|                                     |                                                                  | <hr />                                                                     | <hr />                                                                                                                             |
|                                     |                                                                  |                                                                         |                                                                                                                                 |
|                                     |                                                                  | *Chemin court :***%USERPROFILE%**                   | *Chemin court :***~**                                                                                       |
+++++

Remarque: pour les distributions Linux, un fichier de configuration supplémentaire lié à [Qt](Third_Party_Libraries/fr#Qt.md) peut exister au chemin **/home/username/.config/FreeCAD/FreeCAD.conf**.



### Paramètres en ligne de commande 

++++
| Nom de la variable de configuration | Synopsis                                                                                                                                                                                                                                                                                                                               | Exemple                                                                     |
+=====================================+========================================================================================================================================================================================================================================================================================================================================+=============================================================================+
| LoggingFile                         | 1 si l\'enregistrement est activé                                                                                                                                                                                                                                                                                                      | 1                                                                           |
++++
| LoggingFileName                     | Nom du fichier ou le joural est placé                                                                                                                                                                                                                                                                                                  |                                                              |
|                                     |                                                                                                                                                                                                                                                                                                                                        | **C:\Documents and Settings\username\AppData\FreeCAD\FreeCAD.log** |
|                                     |                                                                                                                                                                                                                                                                                                                                        |                                                                          |
++++
| RunMode                             | Cela indique comment la boucle principale travaillera. **\"Script\"** signifie que le script donné est appelé puis quitté. **\"Cmd\"** est destiné à l'interpréteur en ligne de commande. **\"Internal\"** exécute un script interne. **\"Gui\"** entre dans la boucle d\'évènement Gui. **\"Module\"** charge un module Python donné. | \"Cmd\"                                                                     |
++++
| FileName                            | Dépend du RunMode                                                                                                                                                                                                                                                                                                                      |                                                                             |
++++
| ScriptFileName                      | Dépend du RunMode                                                                                                                                                                                                                                                                                                                      |                                                                             |
++++
| Verbose                             | Niveau de verbosité de FreeCAD                                                                                                                                                                                                                                                                                                         | \"\" or \"strict\"                                                          |
++++
| OpenFileCount                       | Donne le nombre de dossiers ouverts par les arguments en ligne de commande                                                                                                                                                                                                                                                             | \"12\"                                                                      |
++++
| AdditionalModulePaths               | Contient les chemins des modules supplémentaires donnés dans la ligne de commande                                                                                                                                                                                                                                                      | \"extraModules/\"                                                           |
++++



### Relatif au système 

+++++
| Nom de la variable de configuration | Synopsis                                                                                                                                                                                                                                                                                                                      | Exemple Windows                           | Exemple Linux            |
+=====================================+===============================================================================================================================================================================================================================================================================================================================+===========================================+==========================+
| AppHomePath                         | Chemin où est installé FreeCAD                                                                                                                                                                                                                                                                                                |                            | /user/local/FreeCAD_0.19 |
|                                     |                                                                                                                                                                                                                                                                                                                               | **c:/Progam Files/FreeCAD_0.19** |                          |
|                                     |                                                                                                                                                                                                                                                                                                                               |                                        |                          |
+++++
| PythonSearchPath                    | Donne une liste de chemins que les modules Python recherchent. S\'effectue au démarrage, et peut changer en cours d\'exécution                                                                                                                                                                                                |                                           |                          |
+++++
| AppTempPath                         | Chemin du répertoire temporaire.                                                                                                                                                                                                                                                                                              |                                           |           |
|                                     | Peut être donné avec la variable d\'environnement `TMPDIR` ou avec l\'<img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [éditeur des paramètres](Std_DlgParameter/fr.md): **Outils → Editer paramètres ... → BaseApp → Préférences → Général → TempPath** |                                           | **/tmp/**       |
|                                     |                                                                                                                                                                                                                                                                                                                               |                                           |                       |
|                                     |                                                                                                                                                                                                                                                                                                                               |                                           | (par défaut)             |
+++++



### Informations relatives à la version 

Le tableau ci-dessous montre les informations générées par la version disponible. La plupart proviennent du dépôt de sous-version. Cette astuce est nécessaire pour reconstruire exactement une version !

  Nom de la variable de configuration   Synopsis                                                                                                       Exemple
    
  BuildVersionMajor                     Numéro de version majeure de la construction. Définie dans **src/Build/Version.h.in**   0
  BuildVersionMinor                     Numéro de version mineure de la construction. Définie dans **src/Build/Version.h.in**   7
  BuildRevision                         Numéro de révision du référentiel SVN du src de construction. Généré par SVN                                   356
  BuildRevisionRange                    Gamme de différents changements                                                                                123-356
  BuildRepositoryURL                    URL de référence                                                                                               <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk/src>
  BuildRevisionDate                     Date de la révision ci-dessus                                                                                  2007/02/03 22:21:18
  BuildScrClean                         Indique si la source a été modifiée après la dernière construction                                             Source modifiée
  BuildScrMixed                                                                                                                                        Source non mixée



### Identité liée à la marque 

Ces entrées de configuration sont liées au dispositif d\'identification à la marque FreeCAD. Voir [Branding](Branding/fr.md) pour plus de renseignements.

++++
| Nom de la variable de configuration | Synopsis                                                                                                                                         | Exemple                  |
+=====================================+==================================================================================================================================================+==========================+
| ExeName                             | Nom du fichier exécutable de compilation. Ce nom peut être différent de FreeCAD si un **main.cpp** différent est utilisé. |           |
|                                     |                                                                                                                                                  | **FreeCAD.exe** |
|                                     |                                                                                                                                                  |                       |
++++
| ExeVersion                          | La version présente au moment de la compilation                                                                                                  | V0.19                    |
++++
| AppIcon                             | L\'icône qui est utilisé pour l\'exécutable, affichée dans la fenêtre principale d\'application                                                  | \"FCIcon\"               |
++++
| ConsoleBanner                       | Bannière du prompt en mode console                                                                                                               |                          |
++++
| SplashPicture                       | Nom de l\'icône utilisée pour l\'écran de démarrage                                                                                              | \"FreeCADSplasher\"      |
++++
| SplashAlignment                     | Alignement du texte dans la fenêtre de dialogue Splash                                                                                           | \"Bottom\" ou \"Left\"   |
++++
| SplashTextColor                     | Couleur du texte splashé                                                                                                                         | \"#000000\"              |
++++
| StartWorkbench                      | Nom de l\'atelier lancé automatiquement après le démarrage                                                                                       | \"PartDesign\"           |
++++
| HiddenDockWindow                    | Liste des dockwindows (séparés par un point-virgule) qui seront désactivés                                                                       | \"Property editor\"      |
++++



### Interrogation de la configuration 

**Depuis la console Python de FreeCAD**

Les entrées de la configuration peuvent être interrogées avec le **nom de la variable de configuration** (voir les tableaux ci-dessus) depuis la [console Python](Python_console/fr.md). Par exemple :

 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'

Si le nom n\'est pas trouvé, une chaîne vide est renvoyée.

**En ligne de commande**

Utilisez l\'option `--get-config <config-var-name>` pour interroger un seul nom. Tous les noms ne sont pas pris en charge. Par exemple :

 FreeCAD --get-config ExeVersion

Utilisez l\'option `--dump-config` pour obtenir une liste de noms et leurs valeurs. Tous les noms ne sont pas pris en charge.

**Depuis la console FreeCAD**

Démarrez FreeCAD en mode console avec `--console` et interrogez avec du code Python. Par exemple :

 $ FreeCAD --console
 [FreeCAD Console mode <Use Ctrl-D (i.e. EOF) to exit.>]
 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'
 >>> exit()

Pour Linux (shell bash), vous pouvez modifier la ligne de commande suivante en fonction de vos besoins :

 $ FreeCAD --console <<EOF
 print( "FREECAD_USER_HOME: " + ( "not set" if ( os.environ.get('FREECAD_USER_HOME') is None ) else os.environ.get('FREECAD_USER_HOME') ) )
 print( "UserHomePath: " + FreeCAD.ConfigGet("UserHomePath") )
 exit()
 EOF



## Démarrage de FreeCAD à partir du bureau 



### Linux : création d\'une option de démarrage supplémentaire 

Ce qui suit suppose que votre bureau est configuré de telle sorte que vous puissiez lancer FreeCAD à partir de celui-ci. En fonction de votre distribution Linux et de votre environnement de bureau, vous devrez peut-être adapter les étapes suivantes :

1.  Copiez le fichier d\'entrée freedesktop pour FreeCAD de **/usr/share/applications/freecad.desktop** vers **~/.local/share/applications**.
2.  Changez le nom de **freecad.desktop** en autre chose (par exemple **MyFreeCADConfig.desktop**).
3.  Ouvrez le fichier avec un éditeur de texte et changez la façon dont FreeCAD est appelé en modifiant la ligne commençant par `Exec`.
4.  Pour résultat, une entrée supplémentaire dans votre menu Démarrer/lanceur d\'application est disponible. De cette façon, vous pouvez avoir plusieurs entrées FreeCAD avec différentes options de lancement.



## Démarrage de FreeCAD à partir d\'un medium USB 

**Windows**

Placez l\'exécutable FreeCAD, **FreeCAD.exe**, sur le support USB. Créez un fichier batch, **FreeCAD.bat** et placez-le dans le même répertoire que **FreeCAD.exe**. Dans le fichier batch, écrivez :


```python
set CURRENTDIR=%cd%
set FREECAD_USER_HOME=%CURRENTDIR%
start FreeCAD.exe -u FreeCAD/user.cfg -s FreeCAD/system.cfg --write-log 
```

Or with `FREECAD_USER_DATA` ([see](https://forum.freecadweb.org/viewtopic.php?f=12&t=54784&start=60#p474759)):


```python
set CURRENTDIR="%cd%"
set FREECAD_USER_DATA=%CURRENTDIR%/..
start FreeCAD.exe -u %FREECAD_USER_DATA%/user.cfg -s %FREECAD_USER_DATA%/system.cfg```

Avec le batch dans la racine du support USB :


```python
set CURRENTDIR=%cd%
set FREECAD_USER_DATA=%CURRENTDIR%FreeCAD\
start %cd%FreeCAD\bin\FreeCAD.exe -u %FREECAD_USER_DATA%user.cfg -s %FREECAD_USER_DATA%system.cfg
```

Maintenant, double-cliquez sur le fichier de commandes pour démarrer FreeCAD. ([voir ce fil](https://forum.freecadweb.org/viewtopic.php?f=4&t=49028))



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Start](Start_Workbench.md) > Start up and Configuration/fr
