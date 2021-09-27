# Start up and Configuration/fr
{{TOCright}}

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

La réponse vous permet de connaître les paramètres disponibles :

 Usage: FreeCAD [options] File1 File2 ...
 
 Allowed options:
 
 Generic options:
   -v [ --version ]          Prints version string
   -h [ --help ]             Prints help message
   -c [ --console ]          Starts in console mode
   --response-file arg       Can be specified with '@name', too
   --dump-config             Dumps configuration
   --get-config arg          Prints the value of the requested configuration key
 
 Configuration:
   -l [ --write-log ]        Writes a log file to:
                             /home/username/.FreeCAD/FreeCAD.log
   --log-file arg            Unlike --write-log this allows logging to an 
                             arbitrary file
   -u [ --user-cfg ] arg     User config file to load/save user settings
   -s [ --system-cfg ] arg   System config file to load/save system settings
   -t [ --run-test ] arg     Test case - or 0 for all
   -M [ --module-path ] arg  Additional module paths
   -P [ --python-path ] arg  Additional python paths
   --single-instance         Allow to run a single instance of the application

Dans le tableau suivant, les options sélectionnées sont décrites plus en détail:

+-------------------------------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option longue                             | [Nom de la variable de configuration](#Configuration.md) correspondante | Synopsis                                                                                                                                                                                                                                                                                                                    |
+===========================================+=================================================================================+=============================================================================================================================================================================================================================================================================================================================+
|                            | UserParameter                                                                   | Nom de fichier ou chemin relatif qui se termine par un nom de fichier. La valeur par défaut est `user.cfg`.                                                                                                                                                                                          |
| `--user-cfg <filename>`          |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
|                                        |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
+-------------------------------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                            | Prepends to AdditionalModulePaths                                               | Répertoire qui contient des modules. Cette option peut être donnée à plusieurs reprises pour spécifier plusieurs répertoires.                                                                                                                                                                                               |
| `--module-path <dir>`            |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
|                                        |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
+-------------------------------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                            | la plus part                                                                    | Affiche la valeur demandée dans une boîte de dialogue contextuelle. Quitte après confirmation avec **OK**. Ne peut pas être utilisé à plusieurs reprises. Si un nom de variable inconnu / illégal est utilisé, la réponse est vide. L\'indicateur `--console` n\'est pas respecté. |
| `--get-config <config-var-name>` |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
|                                        |                                                                                 |                                                                                                                                                                                                                                                                                                                             |
+-------------------------------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Les options peuvent être rédigées sous deux formes : `--long-option arg` et `--long-option<nowiki>=</nowiki>arg`.

### Fichiers de configuration et réponse 

Vous pouvez lire certaines options de FreeCAD à partir d\'un fichier de configuration. Ce fichier doit être dans le répertoire {{FileName|/bin}} et doit être nommé {{FileName|FreeCAD.cfg}}. Notez que les options spécifiées en ligne de commande remplacent le fichier de configuration !

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

FreeCAD est généralement compilé avec deux exécutables : un exécutable compatible avec l\'interface graphique, appelé {{FileName|FreeCAD}} ou {{FileName|freecad}}, et un exécutable sans tête, appelé {{FileName|FreeCADCmd}} ou {{FileName|freecadcmd}}. FreeCAD peut être utilisé en mode console en utilisant le commutateur `--console` (qui est le comportement par défaut de {{FileName|FreeCADCmd}}) :

FreeCAD --console

En mode console, aucune interface utilisateur graphique ne sera affichée et vous serez invité à utiliser l\'interpréteur Python : `>>>>`. À partir de cette invite, vous disposez des mêmes fonctionnalités que l\'interpréteur Python qui fonctionne dans l\'interface graphique de FreeCAD, et vous avez accès à tous les modules et plugins de FreeCAD, à l\'exception du module FreeCADGui. Sachez que les modules qui dépendent de FreeCADGui peuvent également être indisponibles.

Pour en savoir plus sur le mode console ou le mode sans tête, consultez [Headless FreeCAD](Headless_FreeCAD/fr.md).

### Exécution de modules, macros et scripts 

+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Type de fichier | Système          | Exemple en lignes de commande                                                                                                      |
+=================+==================+====================================================================================================================================+
| Module          | Windows          |                                                                                                                     |
|                 |                  | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" -M "C:\FreeCAD\Mod\Draft"`                                                    |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux            |                                                                                                                     |
|                 |                  | `FreeCAD_0.19 -M ~/.FreeCAD/Mod/Draft`                                                                                    |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux (AppImage) |                                                                                                                     |
|                 |                  | `path/to/FreeCADXXX.AppImage -M ~/.FreeCAD/Mod/Draft`                                                                     |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 |                  |                                                                                                                                    |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
| .FCMacro or .py | Windows          |                                                                                                                     |
|                 |                  | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"` |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux            |                                                                                                                     |
|                 |                  | `FreeCAD_0.19 ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                                |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux (AppImage) |                                                                                                                     |
|                 |                  | `path/to/FreeCADXXX.AppImage ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                 |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+

Voir [Macro at Startup](Macro_at_Startup/fr.md) pour savoir comment configurer une macro pour qu\'elle s\'exécute automatiquement au démarrage de FreeCAD.

## Variables d\'environnement 

FreeCAD prend en charge les variables d\'environnement suivantes, qui peuvent être utilisées pour configurer les répertoires: {{Version/fr|0.19}}

+------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Variable d\'environnement    | [Nom de la variable de configuration](#Ensemble_de_configuration.md) correspondante | Synopsis                                                                                                                                                                        |
+==============================+=============================================================================================+=================================================================================================================================================================================+
|               | UserHomePath                                                                                | Répertoire \"de base\" de FreeCAD pour conserver les données des utilisateurs locaux.                                                                                           |
| `FREECAD_USER_HOME` |                                                                                             |                                                                                                                                                                                 |
|                           |                                                                                             |                                                                                                                                                                                 |
+------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|               | UserAppData                                                                                 | S\'il n\'est pas défini, la valeur par défaut est `FREECAD_USER_HOME/.FreeCAD` mais uniquement si `FREECAD_USER_HOME` est défini. |
| `FREECAD_USER_DATA` |                                                                                             |                                                                                                                                                                                 |
|                           |                                                                                             |                                                                                                                                                                                 |
+------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|               | AppTempPath                                                                                 | S\'il n\'est pas défini, la valeur par défaut est `FREECAD_USER_HOME/temp` mais uniquement si `FREECAD_USER_HOME` est défini.     |
| `FREECAD_USER_TEMP` |                                                                                             |                                                                                                                                                                                 |
|                           |                                                                                             |                                                                                                                                                                                 |
+------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Si le chemin spécifié n\'existe pas, le paramètre est ignoré!

Les variables d\'environnement ci-dessus sont destinées à être utilisées pour réaliser un environnement FreeCAD *portable*. Pour un exemple d\'utilisation des variables d\'environnement à partir de la ligne de commande sous Linux, reportez-vous aux [notes pour les utilisateurs Linux sur la page de téléchargement](Download/fr#Note_aux_utilisateurs_de_GNU.2FLinux.md).

### `HOME`

FreeCAD utilise [Qt](Third_Party_Libraries/fr#Qt.md), qui respecte la variable d\'environnement `HOME`. Ainsi, le paramètre `HOME` peut être utilisé pour spécifier le répertoire de base des fichiers de configuration liés à Qt (`.config/FreeCAD/FreeCAD.conf`).

FreeCad lui-même ne respecte pas la variable d\'environnement `HOME` (car cela détermine le répertoire personnel de l\'utilisateur à partir d\'une API système de niveau inférieur). Utilisez `FREECAD_USER_HOME` pour cela.

### `TMPDIR` 

Le répertoire temporaire par défaut est {{FileName|/tmp/}}. La variable d\'environnement `TMPDIR` peut être utilisée pour remplacer la valeur par défaut. (*Editeur:priorité?*).

### Bibliothèques

Certaines bibliothèques doivent appeler des variables d\'environnement système. Parfois, lorsqu\'il y a un problème avec une installation de FreeCAD, c\'est parce qu\'une variable d\'environnement est absente ou incorrecte. Par conséquent, certaines variables importantes sont dupliquées dans la configuration et enregistrées dans le fichier de log.

**Python**

-   PYTHONPATH
-   PYTHONHOME
-   TCL\_LIBRARY
-   TCLLIBPATH

**OpenCascade**

-   CSF\_MDTVFontDirectory
-   CSF\_MDTVTexturesDirectory
-   CSF\_UnitsDefinition
-   CSF\_UnitsLexicon
-   CSF\_StandardDefaults
-   CSF\_PluginDefaults
-   CSF\_LANGUAGE
-   CSF\_SHMessage
-   CSF\_XCAFDefaults
-   CSF\_GraphicShr
-   CSF\_IGESDefaults
-   CSF\_STEPDefaults

## Configuration

A chaque démarrage, FreeCAD examine son environnement, ainsi que les paramètres en ligne de commande. Il construit un **ensemble de configuration** qui détient le cœur des informations d\'exécution. Ces informations sont ensuite utilisées pour déterminer l'emplacement où enregistrer les données des utilisateurs ou des fichiers journaux. Il est également très important pour les analyses post-mortem. Par conséquent, il est enregistré dans le fichier journal (log file).

### Informations relatives à l\'utilisateur 

L\'appel se fait de la manière suivante :

path = FreeCAD.ConfigGet("UserAppData")

+-------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Nom de la variable de configuration | Synopsis                                                         | Exemple Windows                                                              | Exemple Linux                                                         |
+=====================================+==================================================================+==============================================================================+=======================================================================+
| UserAppData                         | Chemin où FreeCAD met les données utilisateur de l\'application. |                                                               |                                                        |
|                                     |                                                                  | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD}}              | {{FileName|/home/username/.FreeCAD}}                                  |
|                                     |                                                                  |                                                                           |                                                                    |
|                                     |                                                                  |                                                                    |                                                             |
|                                     |                                                                  | <hr />                                                                       | <hr />                                                                |
|                                     |                                                                  |                                                                           |                                                                    |
|                                     |                                                                  | \'\'Short path : \'\'{{FileName|%APPDATA%\FreeCAD}}            | \'\'Short path : \'\'{{FileName|~/.FreeCAD}}            |
+-------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| UserParameter                       | Chemin où FreeCAD met les fichier utilisateur de l\'application. |                                                               |                                                        |
|                                     |                                                                  | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD\system.cfg}}   | {{FileName|/home/username/.FreeCAD/system.cfg}}                       |
|                                     |                                                                  |                                                                           |                                                                    |
|                                     |                                                                  |                                                                    |                                                             |
|                                     |                                                                  | <hr />                                                                       | <hr />                                                                |
|                                     |                                                                  |                                                                           |                                                                    |
|                                     |                                                                  | \'\'Short path : \'\'{{FileName|%APPDATA%\FreeCAD\system.cfg}} | \'\'Short path : \'\'{{FileName|~/.FreeCAD/system.cfg}} |
+-------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| SystemParameter                     | Fichier où sont les données de l\'application.                   |                                                               |                                                        |
|                                     |                                                                  | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD\system.cfg}}   | {{FileName|/home/username/.FreeCAD/system.cfg}}                       |
|                                     |                                                                  |                                                                           |                                                                    |
|                                     |                                                                  |                                                                    |                                                             |
|                                     |                                                                  | <hr />                                                                       | <hr />                                                                |
|                                     |                                                                  |                                                                           |                                                                    |
|                                     |                                                                  | \'\'Short path : \'\'{{FileName|%APPDATA%\FreeCAD\system.cfg}} | \'\'Short path : \'\'{{FileName|~/.FreeCAD/system.cfg}} |
+-------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| UserHomePath                        | Chemin racine de l\'utilisateur courant.                         |                                                               |                                                        |
|                                     |                                                                  | {{FileName|C:\Documents and Settings\username}}                              | {{FileName|/home/username}}                                           |
|                                     |                                                                  |                                                                           |                                                                    |
|                                     |                                                                  |                                                                    |                                                             |
|                                     |                                                                  | <hr />                                                                       | <hr />                                                                |
|                                     |                                                                  |                                                                           |                                                                    |
|                                     |                                                                  | \'\'Short path : \'\'{{FileName|%USERPROFILE%}}                | \'\'Short path : \'\'{{FileName|~}}                     |
+-------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------+

Remarque: pour les distributions Linux, un fichier de configuration supplémentaire lié à [Qt](Third_Party_Libraries/fr#Qt.md) peut exister au chemin {{FileName|/home/username/.config/FreeCAD/FreeCAD.conf}}.

### Paramètres en ligne de commande 

+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Nom de la variable de configuration | Synopsis                                                                                                                                                                                                                                                                                                                               | Exemple                                                                     |
+=====================================+========================================================================================================================================================================================================================================================================================================================================+=============================================================================+
| LoggingFile                         | 1 si l\'enregistrement est activé                                                                                                                                                                                                                                                                                                      | 1                                                                           |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| LoggingFileName                     | Nom du fichier ou le joural est placé                                                                                                                                                                                                                                                                                                  |                                                              |
|                                     |                                                                                                                                                                                                                                                                                                                                        | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD\FreeCAD.log}} |
|                                     |                                                                                                                                                                                                                                                                                                                                        |                                                                          |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| RunMode                             | Cela indique comment la boucle principale travaillera. **\"Script\"** signifie que le script donné est appelé puis quitté. **\"Cmd\"** est destiné à l'interpréteur en ligne de commande. **\"Internal\"** exécute un script interne. **\"Gui\"** entre dans la boucle d\'évènement Gui. **\"Module\"** charge un module Python donné. | \"Cmd\"                                                                     |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| FileName                            | Dépend du RunMode                                                                                                                                                                                                                                                                                                                      |                                                                             |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| ScriptFileName                      | Dépend du RunMode                                                                                                                                                                                                                                                                                                                      |                                                                             |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Verbose                             | Niveau de verbosité de FreeCAD                                                                                                                                                                                                                                                                                                         | \"\" or \"strict\"                                                          |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| OpenFileCount                       | Donne le nombre de dossiers ouverts par les arguments en ligne de commande                                                                                                                                                                                                                                                             | \"12\"                                                                      |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| AdditionalModulePaths               | Contient les chemins des modules supplémentaires donnés dans la ligne de commande                                                                                                                                                                                                                                                      | \"extraModules/\"                                                           |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

### Relatif au système 

+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+---------------------------+
| Nom de la variable de configuration | Synopsis                                                                                                                                                                                                                                                                                                                                                           | Exemple Windows                           | Exemple Linux             |
+=====================================+====================================================================================================================================================================================================================================================================================================================================================================+===========================================+===========================+
| AppHomePath                         | Chemin où est installé FreeCAD                                                                                                                                                                                                                                                                                                                                     |                            | /user/local/FreeCAD\_0.19 |
|                                     |                                                                                                                                                                                                                                                                                                                                                                    | {{FileName|c:/Progam Files/FreeCAD_0.19}} |                           |
|                                     |                                                                                                                                                                                                                                                                                                                                                                    |                                        |                           |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+---------------------------+
| PythonSearchPath                    | Donne une liste de chemins que les modules Python recherchent. S\'effectue au démarrage, et peut changer en cours d\'exécution                                                                                                                                                                                                                                     |                                           |                           |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+---------------------------+
| AppTempPath                         | Chemin du répertoire temporaire. Peut être donné avec la variable d\'environnement `TMPDIR` ou avec l\'<img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Editeur des paramètres](Std_DlgParameter/fr.md): **Outils → Editer paramètres ... → BaseApp → Préférences → Général → TempPath** |                                           |            |
|                                     |                                                                                                                                                                                                                                                                                                                                                                    |                                           | {{FileName|/tmp/}}        |
|                                     |                                                                                                                                                                                                                                                                                                                                                                    |                                           |                        |
|                                     |                                                                                                                                                                                                                                                                                                                                                                    |                                           | (par défaut)              |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+---------------------------+

### Informations relatives à la version 

Le tableau ci-dessous montre les informations générées par la version disponible. La plupart proviennent du dépôt de sous-version. Cette astuce est nécessaire pour reconstruire exactement une version !

  Nom de la variable de configuration   Synopsis                                                                                                       Exemple
  ------------------------------------- -------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------
  BuildVersionMajor                     Numéro de version majeure de la construction. Définie dans {{FileName|src/Build/Version.h.in}}   0
  BuildVersionMinor                     Numéro de version mineure de la construction. Définie dans {{FileName|src/Build/Version.h.in}}   7
  BuildRevision                         Numéro de révision du référentiel SVN du src de construction. Généré par SVN                                   356
  BuildRevisionRange                    Gamme de différents changements                                                                                123-356
  BuildRepositoryURL                    URL de référence                                                                                               <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk/src>
  BuildRevisionDate                     Date de la révision ci-dessus                                                                                  2007/02/03 22:21:18
  BuildScrClean                         Indique si la source a été modifiée après la dernière construction                                             Src modifié
  BuildScrMixed                                                                                                                                        Src non mixé

### Identité liée à la marque 

Ces entrées de configuration sont liées au dispositif d\'identification à la marque FreeCAD. Voir [Branding](Branding/fr.md) pour plus de renseignements.

+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Nom de la variable de configuration | Synopsis                                                                                                                                         | Exemple                  |
+=====================================+==================================================================================================================================================+==========================+
| ExeName                             | Nom du fichier exécutable de compilation. Ce nom peut être différent de FreeCAD si un {{FileName|main.cpp}} différent est utilisé. |           |
|                                     |                                                                                                                                                  | {{FileName|FreeCAD.exe}} |
|                                     |                                                                                                                                                  |                       |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| ExeVersion                          | La version présente au moment de la compilation                                                                                                  | V0.19                    |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| AppIcon                             | L\'icône qui est utilisé pour l\'exécutable, affichée dans la fenêtre principale d\'application                                                  | \"FCIcon\"               |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| ConsoleBanner                       | Bannière du prompt en mode console                                                                                                               |                          |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| SplashPicture                       | Nom de l\'icône utilisée pour l\'écran de démarrage                                                                                              | \"FreeCADSplasher\"      |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| SplashAlignment                     | Alignement du texte dans la boîte de dialogue Splash                                                                                             | \"Bottom\" ou \"Left\"   |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| SplashTextColor                     | Couleur du texte splashé                                                                                                                         | \"\#000000\"             |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| StartWorkbench                      | Nom de l\'atelier lancé automatiquement après le démarrage                                                                                       | \"Part design\"          |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| HiddenDockWindow                    | Liste des dockwindows (séparés par un point-virgule) qui seront désactivés                                                                       | \"Property editor\"      |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+

### Interrogation de la configuration 

**Depuis la console Python de FreeCAD**

Les entrées de la configuration peuvent être interrogées avec le **config var name** (voir les tableaux ci-dessus) depuis la [Console Python](Python_console/fr.md). Par exemple:

 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'

Si le nom n\'est pas trouvé, une chaîne vide est renvoyée.

**En ligne de commande**

Utilisez l\'option `--get-config <config-var-name>` pour interroger un seul nom. Tous les noms ne sont pas pris en charge. Par exemple:

 FreeCAD_0.19 --get-config ExeVersion

Utilisez l\'option `--dump-config` pour obtenir une liste de noms et leurs valeurs. Tous les noms ne sont pas pris en charge.

**Depuis la console FreeCAD**

Démarrez FreeCAD en mode console avec `--console` et interrogez avec du code Python. Par exemple:

 $ FreeCAD_0.19 --console
 [FreeCAD Console mode <Use Ctrl-D (i.e. EOF) to exit.>]
 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'
 >>> exit()

Pour Linux (shell bash), vous pouvez modifier la ligne de commande suivante en fonction de vos besoins:

 $ FreeCAD_0.19 --console <<EOF
 print( "FREECAD_USER_HOME: " + ( "not set" if ( os.environ.get('FREECAD_USER_HOME') is None ) else os.environ.get('FREECAD_USER_HOME') ) )
 print( "UserHomePath: " + FreeCAD.ConfigGet("UserHomePath") )
 exit()
 EOF

## Démarrage de FreeCAD à partir du bureau 

### Linux: création d\'une option de démarrage supplémentaire 

Ce qui suit suppose que votre bureau est configuré de telle sorte que vous puissiez lancer FreeCAD à partir de celui-ci. En fonction de votre distribution Linux et de votre environnement de bureau, vous devrez peut-être adapter les étapes suivantes:

1.  Copiez le fichier d\'entrée freedesktop pour FreeCAD de {{FileName|/usr/share/applications/freecad.desktop}} vers {{FileName|~/.local/share/applications}}.
2.  Changez le nom de {{FileName|freecad.desktop}} en autre chose (par exemple {{FileName|MyFreeCADConfig.desktop}}).
3.  Ouvrez le fichier avec un éditeur de texte et changez la façon dont FreeCAD est appelé en modifiant la ligne commençant par `Exec`.
4.  Pour résultat, une entrée supplémentaire dans votre menu Démarrer/lanceur d\'application est disponible. De cette façon, vous pouvez avoir plusieurs entrées FreeCAD avec différentes options de lancement.

## Démarrage de FreeCAD à partir d\'un medium USB 


{{Version/fr|0.19}}

**Windows**

Placez l\'exécutable FreeCAD, {{FileName|FreeCAD.exe}}, sur le support USB. Créez un fichier de commandes, {{FileName|FreeCAD.bat}}, et placez-le dans le même répertoire que {{FileName|FreeCAD.exe}}. Dans le fichier de commandes, écrivez:


```python
set CURRENTDIR=%cd%
set FREECAD_USER_HOME=%CURRENTDIR%
start FreeCAD.exe -u FreeCAD/user.cfg -s FreeCAD/system.cfg --write-log 
```

[or](https://forum.freecadweb.org/viewtopic.php?f=12&t=54784&start=60#p474759) with `FREECAD_USER_DATA`


```python
set CURRENTDIR="%cd%"
set FREECAD_USER_DATA=%CURRENTDIR%/..
start FreeCAD.exe -u %FREECAD_USER_DATA%/user.cfg -s %FREECAD_USER_DATA%/system.cfg```

Maintenant, double-cliquez sur le fichier de commandes pour démarrer FreeCAD. ([voir ce fil](https://forum.freecadweb.org/viewtopic.php?f=4&t=49028))





 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Start](Start_Workbench.md) > Start up and Configuration/fr
