





{{TOCright}}

## Premier test {#premier_test}

Avant de passer à la douloureuse phase de débogage, utilisez l\'[Atelier test](Testing/fr.md) pour vérifier si les tests standards fonctionnent correctement. Si ce n\'est pas le cas, c\'est peut-être dû a une installation défectueuse.

## Ligne de commande {#ligne_de_commande}

Le débogage de FreeCAD est supporté par quelques mécanismes internes. La version en ligne de commande de FreeCAD fournit des options d\'aide au débogage :

Ce sont les options actuellement reconnues par FreeCAD 0.19 :

Options génériques :

 -v [ --version ]            Affiche la version sous la forme d'une chaîne
 -h [ --help ]               Affiche un message d'aide
 -c [ --console ]            Démarre en mode console
 --response-file arg         Peut également être spécifié avec '@name' 
 --dump-config               Charge la configuration
 --get-config arg            Affiche la valeur de la clé de configuration demandée

Configuration :

 -l [ --write-log ]           Ecrit un fichier journal dans :
                              $HOME/.FreeCAD/FreeCAD.log (Linux)
                              $HOME/Library/Preferences/FreeCAD/FreeCAD.log (macOS)
                              %APPDATA%\FreeCAD\FreeCAD.log (Windows)
 --log-file arg               Contrairement à --write-log cela permet de se connecter à un fichier arbitraire
 -u [ --user-cfg ] arg        Fichier de configuration utilisateur pour charger/enregistrer les paramètres utilisateur
 -s [ --system-cfg ] arg      Fichier de configuration pour charger/enregistrer les paramètres du système
 -t [ --run-test ] arg        Cas de test - ou 0 pour tous 
 -M [ --module-path ] arg     Chemin de module supplémentaire
 -P [ --python-path ] arg     Autres chemins Python
 --single-instance            Autoriser à exécuter une seule instance de l'application

## Générer un Backtrace {#générer_un_backtrace}

Si vous exécutez une version de FreeCAD à partir de l\'extrémité saillante de la courbe de développement, il se peut qu\'il se \"bloque\". Vous pouvez aider à résoudre ces problèmes en fournissant aux développeurs une \"backtrace\". Pour ce faire, vous devez exécuter une \"version de débogage\" du logiciel. \"Debug build\" est un paramètre qui est défini au moment de la compilation, donc vous devrez soit compiler vous-même FreeCAD, soit obtenir une version \"debug\" précompilée.

### For Linux {#for_linux}


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Linux Debugging →


<div class="mw-collapsible-content">

Prérequis :

-   le package logiciel gdb installé
-   une version de débogage de FreeCAD (pour l\'instant uniquement disponible par [compilation à partir des sources](Compile_on_Linux/fr#Pour_une_compilation_de_Debogage.md))
-   un modèle FreeCAD qui provoque un crash.

Étapes : Entrez ce qui suit dans votre fenêtre de terminal :

Trouvez le binaire FreeCAD sur votre système :


```python
$ whereis freecad
freecad: /usr/local/freecad <--- for example

$ cd /usr/local/freecad/bin
$ gdb FreeCAD
```

GNUdebugger affichera des informations d'initialisation. Le (gdb) montre que GNUDebugger est en cours d'exécution dans le terminal, entrez maintenant :


```python
(gdb) handle SIG33 noprint nostop
(gdb) run
```

FreeCAD va maintenant démarrer. Effectuez les étapes qui provoquent le crash ou le blocage de FreeCAD, puis entrez dans la fenêtre du terminal :


```python
(gdb) bt
```

Cela va générer une longue liste de ce que le programme faisait quand il s\'est planté ou gelé. Incluez ceci avec votre rapport de problème.


```python
(gdb) bt full
```

Affiche également les valeurs des variables locales. Ceci peut être combiné avec un nombre pour limiter le nombre d\'images affichées.


</div>


</div>

### Pour macOS {#pour_macos}


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

macOS Debugging →


<div class="mw-collapsible-content">

Prerequis :

-   logiciel lldb installé
-   une version de débogage de FreeCAD
-   un modèle FreeCAD qui provoque un crash

Étapes: Entrez ce qui suit dans la fenêtre de votre terminal :


```python
$ cd FreeCAD/bin
$ lldb FreeCAD
```

LLDB générera des informations d'initialisation. Le (lldb) montre que le débogueur s\'exécute dans le terminal, entrez maintenant :


```python
(lldb) run
```

FreeCAD va maintenant démarrer. Effectuez les étapes qui provoquent le crash ou le blocage de FreeCAD, puis entrez dans la fenêtre du terminal :


```python
(lldb) bt
```

Cela va générer une longue liste de ce que le programme faisait quand il s\'est bloqué ou arrêté. Incluez ceci avec votre rapport de problème.


</div>


</div>

## Liste des bibliothèques chargées par FreeCAD {#liste_des_bibliothèques_chargées_par_freecad}

(Applicable à Linux et macOS)

Parfois, il est utile de comprendre quelles bibliothèques FreeCAD charge, en particulier s\'il y a plusieurs bibliothèques en cours de chargement du même nom mais de versions différentes (collision de versions). Afin de voir quelles bibliothèques sont chargées par FreeCAD lorsqu\'il se bloque, vous devez ouvrir un terminal et l\'exécuter dans le débogueur. Dans une deuxième fenêtre de terminal, découvrez l\'ID du processus de FreeCAD :


`ps -A &#124; grep FreeCAD`

Utilisez l\'ID retourné et transmettez-le à `lsof` :


` lsof -p process_id`

Cela affiche une longue liste de ressources chargées. Ainsi, par exemple, si vous essayez de vérifier si plusieurs versions de la bibliothèque Coin3d sont chargées, faites défiler la liste ou recherchez directement Coin dans la sortie :


`lsof -p process_id &#124; grep Coin`

## Débogage Python {#débogage_python}

Pour une approche plus moderne du débogage de Python, consultez les articles suivants :

-   [Debugging macros with VS 2017](https://forum.freecadweb.org/viewtopic.php?f=22&t=28901)
-   [Python workbenches debugging](https://forum.freecadweb.org/viewtopic.php?f=10&t=35383)
-   [python3.dll, Qt5Windgets.dll, Qt5Gui.dll and Qt5Core.dll not found](https://forum.freecadweb.org/viewtopic.php?f=4&t=40251)

### winpdb


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

winpdb Debugging →


<div class="mw-collapsible-content">

Voici un exemple d\'usage de *Winpdb* dans FreeCAD :

Nous avons besoin du débogueur Python : *Winpdb*. Si vous ne l\'avez pas installé, vous pouvez le faire sous Ubuntu/Debian avec :


```python
sudo apt-get install winpdb
```

Vous pouvez maintenant configurer le débogueur.

1.  Démarrez *Winpdb*.
2.  Définissez le mot de passe du débogueur sur \"test\" : Allez dans le menu \"Fichier\" → \"Mot de passe\" et définissez le mot de passe.

Nous allons maintenant exécuter étape par étape un script de test Python dans FreeCAD.

1.  Lancez winpdb et définissez le mot de passe (par exemple, test)
2.  Créer un fichier Python avec ce contenu


```python
import rpdb2
rpdb2.start_embedded_debugger("test")
import FreeCAD
import Part
import Draft
print "hello"
print "hello"
import Draft
points=[FreeCAD.Vector(-3.0,-1.0,0.0),FreeCAD.Vector(-2.0,0.0,0.0)]
Draft.makeWire(points,closed=False,face=False,support=None)
```

1.  Démarrer FreeCAD et charger le fichier ci-dessus dans FreeCAD
2.  Appuyez sur F6 pour l\'exécuter
3.  Maintenant, FreeCAD ne répondra plus car le débogueur Python attend
4.  Passez à l\'interface graphique de Windpdb et cliquez sur \"Attacher\". Après quelques secondes, un élément \"\" apparaît où vous devez double-cliquer
5.  Maintenant, le script actuellement exécuté apparaît dans Winpdb.
6.  Définir une pause à la dernière ligne et appuyez sur F5
7.  Maintenant, appuyez sur F7 pour entrer dans le code Python de Draft.makeWire


</div>


</div>

### Code Visual Studio (VS Code) {#code_visual_studio_vs_code}


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

VS Code Debugging →


<div class="mw-collapsible-content">

Prerequis :

-   Le paquet ptvsd doit être installé


```python
pip install ptvsd
```

[Page pypi](https://pypi.org/project/ptvsd/)

[Documentation du code Visual Studio pour debugging à distance](https://code.visualstudio.com/docs/python/debugging#_remote-debugging)

Étapes :

-   Ajoutez le code suivant au début de votre script


```python
import ptvsd
print("Waiting for debugger attach")
# 5678 is the default attach port in the VS Code debug configurations
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
ptvsd.wait_for_attach()
```

-   Ajoutez une configuration de débogage dans le Code Visual Studio {{MenuCommand|Debug → Add Configurations…}}. Cela devrait ressembler à ceci :




        "configurations": [
            {
                "name": "Python: Attacher",
                "type": "python",
                "request": "attach",
                "port": 5678,
                "host": "localhost",
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "."
                    }
                ]
            },

-   Dans VS Code, ajoutez un point d\'arrêt n\'importe où.
-   Lancez le script dans FreeCAD. FreeCAD gèle en attente de la pièce jointe.
-   Dans VS Code, lancez le débogage en utilisant la configuration créée. Vous devriez voir des variables dans la zone du débogueur.
-   Lors de la mise en place de points d\'arrêt, VS Code se plaindra de ne pas trouver le fichier .py ouvert dans l\'éditeur VS Code.
    -   Changez \"remoteRoot\" : \".\" en \"remoteRoot\" : \"\"
    -   Par exemple, si le fichier Python se trouve dans */home/FC\_myscripts/myscript.py*
    -   Changez : \"remoteRoot\" : \"/home/FC\_myscripts\"
-   Si votre macro ne trouve pas ptvsd alors que vous l\'avez installé quelque part, faites précéder \'import ptvsd\' par


```python
from sys import path
sys.path.append('/path/to/site-packages')
```

où le chemin est celui du répertoire où ptvsd a été installé.

-   Sur le bord inférieur gauche de VSCode, vous pouvez choisir l\'exécutable Python - il est préférable de choisir la version fournie avec FreeCAD.

Dans le package Mac, c\'est /Applications/FreeCAD.App/Contents/Resources/bin/python.

Vous pouvez le trouver sur votre système en tapant 
```python
import sys
print(sys.executable)
``` dans la console Python de FreeCAD.


</div>


</div>

## Débogage d\'OpenCasCade {#débogage_dopencascade}

Pour les développeurs qui ont besoin d\'approfondir le noyau d\'OpenCasCade, l\'utilisateur \@abdullah a créé un [fil de discussion](https://forum.freecadweb.org/viewtopic.php?f=10&t=47017) qui explique comment le faire.





{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
