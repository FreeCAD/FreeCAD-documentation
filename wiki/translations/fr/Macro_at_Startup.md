# Macro at Startup/fr
## Introduction


{{TOCright}}

Cette documentation explique comment configurer une macro pour qu\'elle s\'exécute automatiquement au démarrage de FreeCAD.

Avant de commencer, les points suivants doivent être pris en compte:

-   L\'exécution automatique d\'une macro au démarrage peut être considérée comme un risque pour la sécurité. Vous ne devez exécuter que des macros fiables et testées auparavant
-   Vous avez probablement besoin de quelques notions de Python et de codage pour suivre cette procédure
-   Lorsque les dossiers utilisateur (\'Mod\', \'Macro\', \...) sont mentionnés, ils se trouvent dans votre dossier utilisateur FreeCAD. Vous pouvez les localiser au démarrage et à la configuration → [Informations relatives à l\'utilisateur](Start_up_and_Configuration/fr#Informations_correspondant_.C3.A0_l.27utilisateur.md)
-   Cela ne devrait pas être fait pour les macros traitant de la modélisation de pièces. Ceci est plutôt approprié pour les macros qui ajoutent des fonctionnalités en améliorant l\'interface utilisateur, \...

## Comment

### Préparer la macro 

Généralement, il arrivera qu\'une macro ne soit pas directement compatible avec un lancement au démarrage et devra être ajustée

Considérez la macro ci-dessous que vous avez téléchargée quelque part et qui est stockée dans votre dossier \'Macro\' avec le nom \'MySuperMacro.FCMacro\':

    ## Import section ##
    from PySide import QtGui

    ## Definition section (classes, functions, ...)
    class MyMsgBox(QtGui.QMessageBox):

        def __init__(self):
            super(MyMsgBox, self).information(None, "MyTitle", "MyText")

    ## Main instruction section
    MyMsgBox()

Toutes les macros présentent généralement une structure similaire avec une première section d\'importation, puis une section de définition et enfin une section d\'instruction principale. Nous allons nous concentrer sur ce dernier point car les instructions principales (elles sont assez faciles à repérer car elles commencent au début de la ligne) sont en réalité celles qui \"exécutent\" la macro. Pour une étape ultérieure, nous devrons importer la macro avec un programme puis l\'exécuter. Cela ne peut pas être fait avec la structure réelle de la macro. Pour pouvoir le faire, nous devons inclure les instructions principales dans une fonction - par exemple. run() - puis assurez-vous que cette fonction est toujours appelée lorsque la macro est exécutée manuellement par l\'utilisateur. Si vous n\'êtes pas totalement sûr de ce que vous faites, il est conseillé de travailler sur une copie de la macro (ou vous pouvez simplement vouloir conserver la macro d\'origine telle quelle). Le fichier d\'origine doit être modifié comme suit:

    from PySide import QtGui
    ## The 2 below lines shall be added if not already present to ensure FreeCAD modules are imported
    import FreeCAD as App
    import FreeCADGui as Gui

    class MyMsgBox(QtGui.QMessageBox):

        def __init__(self):
            super(MyMsgBox, self).information(None, "MyTitle", "MyText")

    ## Enclose the main instructions in a function
    def run():
        MyMsgBox()

    ## Ensure main instructions are still called in case of manual run
    if __name__ == '__main__':
        run()

Bien sûr, si la fonction \"run()\" existe déjà dans la macro, vous pouvez choisir n\'importe quel autre nom commode. La macro est maintenant prête à être intégrée au démarrage de FreeCAD.

### Intégration au démarrage de FreeCAD 

Commencez par créer un nouveau dossier dans votre dossier utilisateur \"Mod\" de appelé \"MacroStartup\". Copiez la macro modifiée dans ce dossier nouvellement créé et renommez-la avec une extension \".py\" si ce n\'est pas encore le cas (notez que si vous développez la macro vous-même, vous pouvez également la nommer avec l\'extension \".py\" dans le dossier \"Macro\" pour ne pas avoir à le renommer lors de la copie). Enfin, créez dans le même dossier un fichier appelé \"InitGui.py\" qui contient le code suivant:

    def runStartupMacros(name):
        # Do not run when NoneWorkbench is activated because UI isn't yet completely there
        if name != "NoneWorkbench":
            # Run macro only once by disconnecting the signal at first call
            FreeCADGui.getMainWindow().workbenchActivated.disconnect(runStartupMacros)

            # Following 2 lines shall be duplicated for each macro to run
            import MySuperMacro
            MySuperMacro.run()

            # Eg. if a second macro shall be launched at startup
            # import MyWonderfulMacro
            # MyWonderfulMacro.run()

    # The following 2 lines are important because InitGui.py files are passed to the exec() function...
    # ...and the runMacro wouldn't be visible outside. So explicitly add it to __main__
    import __main__
    __main__.runStartupMacros = runStartupMacros

    # Connect the function that runs the macro to the appropriate signal
    FreeCADGui.getMainWindow().workbenchActivated.connect(runStartupMacros)

Notez que cela ne sera fait qu\'une fois. Si vous souhaitez exécuter plus d\'une macro, vous pouvez simplement ajouter les autres macros dans le même fichier (consultez les commentaires sur le code ci-dessus).

Nous avons finis. Votre macro devrait s\'exécuter automatiquement au prochain lancement de FreeCAD.

Notez que si la macro originale a été téléchargée via le gestionnaire d'addon, elle sera écrasée lors de la mise à jour et vous devrez donc à nouveau suivre les étapes décrites ici.

## Remarques générales 

-   Dans l\'exemple de script \'InitGui.py\' ci-dessus, la fonction nommée \'runStartupMacros()\' peut être modifiée, tant que vous modifiez également les quatre autres références à celle-ci, afin qu\'elles correspondent toutes.
-   Ce script sera exécuté avant le chargement automatique de l\'atelier de démarrage de votre choix dans les préférences de FreeCAD, [Préférences générales](Preferences_Editor/fr#Pr.C3.A9f.C3.A9rences_g.C3.A9n.C3.A9rales.md).

### Linux

### MacOS

### Windows

-   Dans l\'exemple ci-dessus, vous pouvez placer le dossier \'MacroStartup\' dans le dossier \'Mod\' de votre répertoire racine FreeCAD (qu\'il s\'agisse de la version installée ou de la version portable), ou vous pouvez créer un dossier \'Mod\' à côté du dossier \'Macro\' dans \'%USERPROFILE%\\AppData\\Roaming\\FreeCAD\\\' et y placer le dossier \'MacroStartup\'.
-   D\'après nos observations, les ateliers trouvés dans l\'un ou l\'autre des dossiers \'Mod\' sont chargés par ordre alphabétique. Ceux qui se trouvent dans le dossier \'Mod\' racine de FreeCAD sont chargés en premier, puis FreeCAD recherche dans le dossier \'%USERPROFILE%\\AppData\\Roaming\\FreeCAD\\Mod\' des ateliers supplémentaires.

## En relation 

[LazyLoader](Extra_python_modules/fr#LazyLoader.md) est un module Python qui permet un chargement différé.


{{Powerdocnavi

}}

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md) [<img src="images/Property.png" style="width:16px"> Macros](Category_Macros.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Macro at Startup/fr
