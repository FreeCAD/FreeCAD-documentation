# CompileOnWindows - Reducing Disk Footprint/fr
Voici des techniques pour réduire l\'espace disque nécessaire à la création de FreeCAD sous Windows. Ceci peut être utile à ceux qui sont limités par l\'espace disque (par exemple, à cause d\'un SSD) et à ceux qui veulent éviter d\'installer complètement Visual Studio.

Il est recommandé de savoir, en pratique, comment [Compiler sous Windows](Compile_on_Windows/fr.md) avec Qt Creator avant d\'essayer ceci.

## Configurer le compilateur MSVC2013 sans installer Visual Studio 

Conditions requises :

-   un autre ordinateur où Visual Studio complet est/peut être installé (en théorie, cela peut être réalisé en décompressant les installateurs VS, mais il n\'y a pas d\'instructions à ce sujet ici)

### Lancer le compilateur 

0\. Pour obtenir les fichiers du compilateur, allez sur un autre ordinateur et localisez le compilateur utilisé. Exemple de chemin d\'accès au compilateur : drive:\\path\\to\\visual\\studio\\VC\\bin.

1\. Copiez les binaires du compilateur et les bibliothèques standard sur un autre ordinateur. C\'est-à-dire, copiez les dossiers suivants dans C:\\Qt\\msvc12rip :

-   drive:\\path\\to\\visual\\studio\\VC\\**bin**
-   drive:\\path\\to\\visual\\studio\\VC\\**lib**
-   drive:\\path\\to\\visual\\studio\\VC\\**include**

2\. Installez [Windows SDK](https://developer.microsoft.com/fr-fr/windows/downloads/sdk-archive/). Pour ceux qui ne le savent pas, c\'est un ensemble d\'en-têtes, de librairies et d\'outils pour compiler des programmes Windows. Notez l\'endroit où il est installé. Exemple de chemin : C:\\Program Files (x86)\\Windows Kits\\8.1

3\. Installez CMake et Qt creator (juste le creator, c\'est à dire l\'environnement, pas le Qt lui-même, pour gagner de la place).

4\. Configurer un compilateur personnalisé dans Qt Creator. Lisez la suite pour savoir comment.

### Compilateur dans Qt Creator 

#### 32-bit

Configurer le compilateur pour 32 bits est assez simple.

4.1. Configurer le compilateur sous l\'onglet Compilateurs dans les paramètres : Ajouter un compilateur **personnalisé** :

-   Nom = msvcrip (le nom n\'a pas d\'importance, c\'est vous qui décidez)
-   Chemin du compilateur : C:\\Qt\\msvc12rip\\VC\\bin\\cl.exe
-   Chemin d\'accès au programme : C:\\Qt\\msvc12\\V\\C\\bin\\nmake.exe
-   ABI : x86-windows-msvc2013-pe-32bit
-   Chemins d\'en-tête : rien
-   Analyseur d\'erreurs : MSVC

![600px](images/Msvc-no-vs_compiler-setup-32.png)

4.2. Sous l\'onglet kits, j\'ai ajouté un kit et je l\'ai configuré comme ceci :

-   Nom : FreeCAD32 (encore une fois, à vous de choisir)
-   Type de support : Bureau
-   Matériel : PC local
-   Compilateur : msvcrip (ou le nom que vous lui avez donné à l\'étape 1)
-   Environnement : (corrigez les chemins d\'accès à votre configuration)


{{code|code=
INCLUDE=C:\Program Files (x86)\Windows Kits\8.1\Include\um\;C:\Qt\msvc12rip\VC\include\
LIB=C:\Qt\msvc12rip\VC\lib\;C:\Program Files (x86)\Windows Kits\8.1\Lib\winv6.3\um\x86\
LIBPATH=C:\Qt\msvc12rip\VC\lib\;C:\Program Files (x86)\Windows Kits\8.1\Lib\winv6.3\um\x86\
PATH=C:\Qt\msvc12rip\VC\bin\;C:\Program Files (x86)\Windows Kits\8.1\bin\x86\;C:\Qt\git\bin\}}

Notez le chemin vers git.exe dans PATH. Il est facultatif, mais s\'il n\'est pas spécifié, l\'information sur la version sera incomplète dans la rubrique A propos de FreeCAD.

-   Débogueur : (facultatif) défini à 32-bit (x86)
-   Version de Qt : Aucune

![600px](images/Msvc-no-vs_kit-setup-32.png)

C\'est la partie environnement des paramètres qui m\'a donné le plus de mal à configurer.

#### 64-bit 

C\'est un peu plus délicat que le compilateur 32 bits. Le principal problème est qu\'il n\'y a pas d\'exécutable nmake dans C:\\Qt\\msvc12rip\\VC\\bin\\**x86_amd64** et nmake continue à utiliser le compilateur 32 bits. Pour contrer ce problème, créez un dossier spécial \"C:\\Qt\\msvc12rip\\VC\\bin\\**x86_amd64_sa**\", où sont réunis mnake et le compilateur 64 bits. Lisez la suite pour obtenir des instructions étape par étape.

4.1. Dans C:\\Qt\\msvc12rip\\VC\\bin, créez un dossier nommé **x86_amd64_sa**. (sa signifie Stand-Alone, utilisez le nom que vous voulez).

4.2. Copiez le contenu du dossier C:\\Qt\\msvc12rip\\C\\bin dans le dossier x86_amd64_sa (vous avez maintenant un compilateur 32 bits).

4.3. copier le contenu du dossier x86_amd64 dans x86_amd64_sa, en remplaçant les fichiers dans le processus. Maintenant vous avez un compilateur 64bit avec nmake.

4.4. Configurer le compilateur sous l\'onglet Compilateurs dans les paramètres : Ajouter un compilateur **personnalisé** :

-   Nom = msvcrip **64** (le nom n\'a pas d\'importance, c\'est à vous de voir)
-   Chemin du compilateur : C:\\Qt\\msvc12rip\\VC\\bin\\x86_amd64_sa\\cl.exe
-   Chemin du programme : C:\\Qt\\msvc12rip\\VC\\bin\\x86_amd64_sa\\nmake.exe
-   ABI : x86-windows-msvc2013-pe-**64bit**\'.
-   Chemins d\'en-tête : rien
-   Analyseur d\'erreurs : MSVC

4.5. Sous l\'onglet kits, ajoutez un kit et configurez-le comme ceci :

-   Nom : FreeCAD**64**. (encore une fois, à vous de choisir)
-   Type de support : Bureau
-   Matériel : PC local
-   Compilateur : msvcrip**64** (ou ce que vous avez appelé à l\'étape 4.4) (ou le nom que vous lui avez donné à l\'étape 4.4)
-   Environnement : (corrigez les chemins en fonction de votre configuration) (par rapport au 32 bits, amd64/x64 est apparu ou a remplacé x86 à plusieurs endroits)


{{code|code=
INCLUDE=C:\Program Files (x86)\Windows Kits\8.1\include\shared\;C:\Program Files (x86)\Windows Kits\8.1\include\um\;C:\Qt\msvc12rip\VC\include
LIB=C:\Program Files (x86)\Windows Kits\8.1\lib\winv6.3\um\x64\;C:\Qt\msvc12rip\VC\lib\amd64\
LIBPATH=C:\Program Files (x86)\Windows Kits\8.1\References\CommonConfiguration\Neutral\
PATH=C:\Qt\msvc12rip\VC\bin\x86_amd64_sa\;C:\Program Files (x86)\Windows Kits\8.1\bin\x64\;C:\Qt\git\bin\}}

Notez le chemin vers git.exe dans PATH. Il est facultatif, mais s\'il n\'est pas spécifié, l\'information sur la version sera incomplète dans la rubrique A propos de FreeCAD.

-   Débogueur : (facultatif) défini à **64**-bit (x64)
-   Version de Qt : Aucune

Astuce : configurez une autre paire kit+compilateur pour utiliser jom au lieu de nmake, pour permettre la construction multicore. La configuration est identique à celle du 64 bits avec nmake, sauf que Make dans l\'onglet compilateur doit pointer vers jom.exe. Exemple de chemin vers jom : C:\\Qt\\Qt542\\Tools\\QtCreator\\bin\\jom.exe (vous devriez pouvoir trouver jom là où votre Qt creator est installé).

Tout le reste est identique à la façon normale de compiler FreeCAD.

### Tester le compilateur et build de FreeCAD 

Conditions requises :

-   Code source de FreeCAD (voir [Compiler sous Windows](Compile_on_Windows/fr.md))
-   Libpack correct, extrait. (\"correct\" signifie qu\'il doit correspondre au compilateur et au type de bit) (voir [Compiler sous Windows](Compile_on_Windows/fr.md))

Lancez FreeCAD (CMakeLists.txt) avec Qt creator et vous serez inviter à lancer cmake. Lancez-le. **CMake va construire un programme de test, pour voir si le compilateur fonctionne.** Si le compilateur ne fonctionne pas, il affichera une erreur indiquant exactement cela et listant le résultat de la compilation. La sortie de la compilation devrait vous aider à identifier ce qui ne va pas. Voici une petite liste d\'erreurs typiques :

-   *Can\'t open Kernel32.lib* - quelque chose ne va pas avec les variables d\'environnement LIB ou LIBPATH (note : elles sont définies sous l\'onglet kits dans Qt, pas dans Windows !)
-   *Can\'t resolve external symbol* - quelque chose ne va pas avec LIB ou LIBPATH (ils pointent probablement vers des .lib-s des mauvais bits 32, 64).
-   *Manifest-related error* - PATH ne pointe pas vers un emplacement où se trouve un compilateur de ressources (rc.exe) des bons bits 32, 64.
-   *Can\'t locate include* - la liste des emplacements d\'inclusion devrait contenir le chemin vers les en-têtes standard (C:\\Qt\\msvc12rip\\VC\\include sur ma machine).

Pour exécuter FreeCAD construit avec le type \"Debug\", les versions de débogage des bibliothèques redistribuables MSVC2013 (msvcp120d.dll, msvcr120d.dll) doivent être présentes quelque part accessible par PATH (dans tout le système, cette fois).

Vous pouvez obtenir ces dlls depuis l\'autre ordinateur qui possède le Visual Studio dont vous avez récupéré le compilateur. Une autre solution consiste à extraire ces dlls directement de l\'installateur de Visual Studio, ce qui est très facile :

-   Monter l\'image .iso téléchargée sur un disque (lecteur D : sur mon système).
-   Localisez les fichiers :
    -   D:\\packages\\vc_librarycore86\\cab3.cab/F_REDIST_DLL_APPLOCAL\_**msvcp120d_x64** (\<- ou x86, si vous construisez en 32 bits)
    -   D:\\packages\\vc_librarycore86\\cab3.cab/F_REDIST_DLL_APPLOCAL\_**msvcr120d_x64**
-   extrayez les fichiers et nommez-les \"msvcp120d.dll\", \"msvcr120d.dll\"
-   copiez les fichiers dans le dossier libpack, dans bin

## Éviter de copier tout fichier libpack pour lancer FreeCAD 

Conditions requises :

-   Windows Vista et versions ultérieures
-   Système de fichiers NTFS (? Peut-être pas \...)

L\'idée est très simple : au lieu de copier des fichiers, créez des liens. Sous Windows, des liens symboliques sont disponibles à cet effet. Un lien fait apparaître le fichier lié à l\'endroit où se trouve le lien, mais le fichier est en fait stocké ailleurs. Les liens peuvent être créés à l\'aide de la commande batch **\[<https://technet.microsoft.com/en-us/library/cc753194(v=ws.10>).aspx mklink\]**.

Comme il y a beaucoup trop de fichiers pour faire des liens manuellement, un script batch doit être utilisé. Voici un exemple d\'un tel script :

links_libpack.bat:


{{code|code=
@set libpackpath=C:\_vt\dev\PC\Qt\FreeCAD\libpack\active
@set builddir=%1
pushd %libpackpath%\bin
for %%i in (*) do mklink "%builddir%\bin\%%i" "%libpackpath%\bin\%%i"
for /D %%s in (*) do mklink /d "%builddir%\bin\%%s" "%libpackpath%\bin\%%s"
popd
pause
}}

La première boucle for crée des liens vers des fichiers, la seconde boucle - des liens vers des dossiers.
Vous devrez modifier le chemin d\'accès à libpack pour qu\'il corresponde au vôtre. Utilisez des chemins absolus. Ensuite, alimentez le chemin du dossier de build de FreeCAD (chemin complet!) au script comme un argument.

Ce programme doit être exécuté avec des privilèges d\'administrateur (ou, vous pouvez autoriser les utilisateurs à utiliser mklink dans les paramètres de la politique de sécurité locale de Windows). Le batch peut échouer, s\'il y a des espaces dans les chemins (il peut fonctionner, mais ce n\'est pas testé). Astuce : créez un raccourci vers links_libpack.bat, configurez-le pour qu\'il fonctionne en tant qu\'administrateur (dans les propriétés du raccourci), et faites glisser le dossier de construction sur le raccourci.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > CompileOnWindows - Reducing Disk Footprint/fr
