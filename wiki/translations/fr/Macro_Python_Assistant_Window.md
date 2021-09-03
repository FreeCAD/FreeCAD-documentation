 {{Macro/fr
|Name=Macro Python Assistant Window
|Description=Cette macro fournit un espace de travail couper/copier/coller pour le code Python. Elle est segmentée afin de pouvoir sélectionner différentes sections et est persistante entre les sessions FreeCAD.
|Author=Piffpoof
|Version=1.0
|Date=2015-01-21
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/4/45/Macro_Python_Assistant_Window.png ToolBar Icon]
}}

L\'un des aspects les plus puissants de Python est la console Python, qui sert à la fois de périphérique de sortie et d\'interpréteur dynamique du code source. La fenêtre de l\'assistant Python (appelée ultérieurement \"PAW\") fournit des fonctionnalités supplémentaires à la console Python. {{Codeextralink|http://pastebin.com/raw/2m0u94Z1}} <img alt="" src=images/PythonAssistantWindowScreenSnapshot.jpg  style="width:500px;">

## Description

En tant qu'environnement de développement moderne, Python présente de nombreux avantages par rapport aux langages plus anciens et à leurs environnements de développement. Un avantage important est la console Python où le code peut être entré de manière interactive et les résultats reçus ([REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)). Ces résultats peuvent ensuite être copiés et utilisés pour construire le code source Python (dans un éditeur de source) ou être recollés dans la console Python sous une forme modifiée pour recevoir une sortie ultérieure. C\'est une méthode très puissante de développement de code.

Aussi puissant que cela puisse paraître, la console Python présente deux inconvénients évidents:

-   la taille de la console est limitée et il est possible que les résultats de votre travail d\'il y a 20 minutes défilent loin de l\'écran. Ils ne sont pas perdus, mais ils sont difficiles à récupérer.
-   la console est effacée chaque fois que vous avez terminé votre session FreeCAD, la console est vide (à part le message de démarrage Python) lors du prochain démarrage de FreeCAD

Le PAW fournit les éléments suivants:

-   il est persistant entre les sessions FreeCAD, les choses ne \"disparaîtront\" pas à moins que l\'utilisateur ne les supprime
-   il a un menu contextuel qui permet ce qui suit:
    -   les opérandes d\'édition standard: Copier/Coller & Tout sélectionner
    -   Copier une sélection dans la console Python
    -   Copiez le contenu complet du PAW dans la console Python
    -   Ajouter le contenu de la console Python au PAW
    -   insérer des marqueurs textuels facilitant la gestion du texte
    -   sélection entre deux marqueurs consécutifs
    -   supprime le préfixe \"\>\>\>\" que la console Python utilise pour indiquer la sortie
    -   réduire plusieurs lignes vides à une seule ligne vide
    -   personnaliser l\'environnement de travail en gérant le PAW (ainsi que la fenêtre principale de FreeCAD) à l\'aide d\'une interface graphique basée sur un curseur

## Installation

Tout le code de pythonAssistantWindow.FCMacro est dans une macro. L\'installation consiste donc à copier le code dans le répertoire Macro approprié et à appeler pythonAssistantWindow à partir du menu Macro, de la console Python ou d\'un bouton de la barre d\'outils (méthode recommandée).

-   voir [Comment installer des macros](How_to_install_macros/fr.md) pour des informations sur la façon d\'installer ce code de macro
-   voir [Personnaliser les barres d\'outils](Customize_Toolbars/fr.md) pour plus d\'informations sur l\'installation en tant que bouton dans une barre d\'outils

Remarque: une variable globale dans FreeCAD est utilisée pour coordonner le stockage persistant.

 Remarque: un fichier texte du répertoire \"UserAppData\" est utilisé pour stocker le contenu textuel de PAW entre les sessions FreeCAD.

## Utilisation

Le PAW est mieux utilisé comme un bouton dans une barre d'outils. Il peut être exécuté à partir du menu Macro ou du code collé sur la console Python, mais les deux dernières options nuisent grandement à sa facilité d\'utilisation.

Lorsque FreeCAD est démarré, il n'y a aucun signe de PAW, à part un bouton sur une barre d'outils. Cliquer sur le bouton provoquera:

-   le PAW à ouvrir dans le coin inférieur droit
    -   les paramètres par défaut sont pour environ 1/3 de la largeur de l\'écran à dédier au PAW, le reste étant utilisé par la fenêtre principale de FreeCAD, la hauteur du PAW sera d\'environ 1/3 de la hauteur de la fenêtre.
-   le contenu du fichier PAW lors de sa dernière exécution apparaîtra dans la fenêtre - il ne devrait y avoir aucune différence par rapport à la dernière utilisation.
    -   si le PAW n\'a pas été exécuté avant, le contenu sera vide
-   si le PAW est déjà ouvert mais caché par d\'autres fenêtres, il sera élevé vers le haut pour devenir visible
-   la fermeture du PAW entraînera l\'écriture du contenu dans le fichier et la fenêtre se fermera - il n\'y a pas de boîte de dialogue vous demandant s\'il faut sauvegarder ou non
-   Cependant, une boîte de dialogue vous demande si vous souhaitez enregistrer si FreeCAD est quitté (Menu → Quitter FreeCAD) avec les modifications non enregistrées dans le fichier PAW.

La plupart des fonctionnalités du PAW sont fournies par le menu contextuel. Les options sont les suivantes:

-   Copie
    - fournit la fonction de copie standard
-   Copier la sélection sur la console
    - la sélection actuelle est copiée à la fin de la console Python
-   Copier le contenu sur la console
    - l\'intégralité du contenu du PAW est copié à la fin de la console Python
-   Coller
    - fournit la fonction de collage standard
-   Ajouter le contenu de la console Python à PAW
    - les copies de la console Python sont placées à la fin du fichier PAW - notez que le contenu de la console Python peut être un mélange de code Python, sortie du code Python, erreur texte du message, sortie de n\'importe quelle partie de FreeCAD
-   Sélectionner entre les marqueurs
    - les marqueurs sont utilisés pour diviser le texte du PAW en sections, une fois le contenu en sections, une section peut être sélectionnée individuellement et utilisée (par exemple, Copier, Copier dans la console Python, Supprimer ). L'intention de Markers est de permettre aux séquences d'instruction Python distinctes et non liées d'exister dans le PAW, puis d'être gérées et traitées individuellement.
-   Tout sélectionner
    - fournit la fonction standard Tout sélectionner
-   Clearbr
    - fournit la fonction standard Clear où tout le texte du PAW est supprimé
-   Insérer un marqueur
    - insère un marqueur textuel à l'emplacement actuel du curseur
-   Supprimez \"\>\>\>\"
    - une fois la sortie de la console Python copiée dans PAW, toutes les lignes générées à partir de commandes Python exécutées porteront le préfixe \"\>\>\>\". Cette option supprime ces préfixes afin que la sortie être utilisé comme données sans contexte
-   Réduction de plusieurs lignes vides en une seule ligne vide
    - compacte le texte en supprimant plusieurs lignes vides
-   Modifier les paramètres de l\'interface graphique
    - ouvre une fenêtre modale avec trois contrôles:
-   <img alt="" src=images/_PythonAssistantWindowGui2.jpg  style="width:500px;">
    -   un curseur pour définir le pourcentage de la largeur de l\'écran dédié au PAW (en gardant à l\'esprit qu\'il y a une certaine largeur que la fenêtre principale de FreeCAD ne passera pas en dessous)
    -   un curseur pour définir le pourcentage de la hauteur de l\'écran dédié au PAW
    -   une paire de boutons radio pour indiquer si le PAW doit être placé en haut ou en bas du côté gauche de l\'écran
-   Enregistrer en tant que fichier
    - le contenu de la fenêtre PAW est écrit dans un fichier sélectionné par l\'utilisateur - le contenu de PAW n\'est pas modifié
-   Fermer la fenêtre
    - la fenêtre PAW est fermée et le contenu est enregistré dans le fichier de stockage persistant
     Remarque : il n\'y a pas de boîte de dialogue demandant de sauvegarder, cela se fait automatiquement

## Interface utilisateur 

L'interface utilisateur est un simple éditeur de texte, un bouton permet de démarrer le PAW et un menu contextuel d'options pour afficher le texte dans la fenêtre d'édition. Les options sont décrites dans la section Utilisation.

## Exemples

**Un premier exemple**

En janvier, votre collègue a besoin d\'aide avec du code Python pour mettre à jour un fichier. Vous écrivez et déboguez sur votre ordinateur et lui envoyez le code source. Vous avez proposé 3 façons différentes de faire le travail et vous ne savez pas quelle est la meilleure solution. Vous copiez les 3 versions finies sur le PAW et les séparez par des marqueurs.

Au début du mois de mai, vous travaillez avec plaisir sur le projet de la bouteille avec FreeCAD. Il y a quelques problèmes pour obtenir le code Python exact pour générer ce qui est requis. Vous devez donc le modéliser graphiquement et le code Python équivalent est généré sur la console Python. En utilisant PAW, vous copiez le contenu de la console Python dans PAW. Vous le façonnez en le déplaçant et en l\'exécutant, en copiant les résultats, en les modifiant dans PAW et en les recopiant jusqu\'à ce que vous soyez heureux.

Le lundi suivant, votre patron s\'est précipité pour dire qu\'il y avait une forte demande pour un opérateur de CAO à l\'usine qui rencontre des problèmes avec la séquence de pliage pour la nouvelle chaîne d\'emballage. Vous y allez immédiatement et vous y restez 2 semaines. Vous terminez votre mission et revenez à votre espace de travail habituel.

À votre retour, évidemment les gens utilisent votre espace de travail pour le déjeuner, vous devez donc le nettoyer un peu. Lorsque vous démarrez FreeCAD et que vous cliquez sur le bouton PAW de la barre d'outils, votre dernier projet s'ajoute à celui de la veille. Vous réalisez que la solution à la conception de votre bouteille réside dans le code de fichier que vous avez écrit en janvier et dans ce que vous avez laissé deux semaines plus tôt. Rapidement, vous pouvez sélectionner et copier les segments de code dans la console Python pour les exécuter et les affiner.

Une fois le code stabilisé, vous pouvez l\'enregistrer dans un fichier pour un fichier Python ou un fichier de macro FreeCAD.

**Autre Exemple**

Vous essayez de savoir ce qui ne va pas avec les valeurs de rotation de divers objets dans un assemblage. Sur 27 objets, vous ne pouvez voir aucun motif quant aux objets qui seront affectés. Vous devez donc regrouper quelques lignes de Python pour isoler les objets incorrects, puis les coller dans le PAW. Ensuite, prenez quelques lignes de Python pour obtenir les valeurs Label et Rotation, collez également ce code dans PAW. Copiez le code pour détailler tous les objets que vous avez besoin de voir dans la liste et répétez-le pour chaque objet, le tout dans le PAW. La console Python aura tous ces résultats (y compris les erreurs de frappe et les messages d\'erreurs), mais elle aura fait défiler la partie visible de la fenêtre il y a longtemps. Vous avez maintenant un ensemble concis de lignes Python, vous le copiez à partir de PAW, vous le collez dans la console Python et vous obtenez la liste exacte des objets nécessitant un débogage, ainsi que leurs valeurs spécifiques. Si nécessaire, vous pouvez ensuite coller les résultats de la console Python dans PAW - préfixez-le avec le caractère de commentaire Python (\'\#\') si vous souhaitez l\'enregistrer dans le code Python et le garder exécutable. Enfin, vous pouvez enregistrer cette agglomération dans un fichier du PAW afin qu'elle soit sécurisée sur disque. Prêt pour la prochaine fois que vous devez voler ou adapter la logique du code.

## Options

La seule option pour le PAW est la possibilité de modifier la taille et la forme de son affichage initial en fonction de la taille et de la forme de la fenêtre principale de FreeCAD. Le code Python contient 3 valeurs constantes: la taille initiale et l\'emplacement du fichier PAW.

## Remarques

Il existe une preuve de concept très simple pour un travail de stockage persistant dans ce code. Il peut être utile à quiconque ayant besoin d\'une telle capacité.

## Links

none (so far)

## Script


{{VeryImportantMessage|'''Si la liste de scripts ne se termine pas par les informations de version de FreeCAD et que la dernière ligne de la phrase "termine ainsi la macro ...", le script est sur le Wiki mais vous pouvez le télécharger ou le copier à partir de [[http://pastebin.com/raw.php?i=2m0u94Z1 unabbreviated script on pastebin.com]]'''}}

ToolBar Icon ![](images/Macro_Python_Assistant_Window.png )

**Macro\_Python\_Assistant\_Window.FCMacro**

    #
    #
    #               Python Assistant Window
    #               v 0.1 initial release
    #
    #
    #***********************************************************************************
    #
    # provide a text editing window with functions to aid in coding Python within FreeCAD
    #
    ############ To Do ############
    # - contextual window doesn't fire if cursor is on last position in file
    # - executing "from PySide import QtGui, QtCore" on console seems to close window
    # - is it possible to copy code to console and then select and execute it?
    ##############################
    #***********************************************************************************
    # The next three variables define the width and height and vertical positioning
    # of the Python Assistant Window
    # 'pawWidthPercent' specifies the percentage of the screen width to be assigned to the Python Assistant Window
    # 'pawHeightPercent' specifies the percentage of the screen height to be assigned to the Python Assistant Window
    # 'pawAtBottomFlag' specifies if the Python Assistant Window is at the top or the bottom
    # The Python Assistant Window is automatically placed at the left,
    # so pawWidthPercent = 26, pawHeightPercent = 41, pawAtBottomFlag = False will cause the
    # following:
    # 1) the main FreeCAD window will be placed in the upper left corner of the screen,
    #    it's height will be 100% of the screen height,
    #    it's width will be 74% (=100%-26%) of the screen
    # 2) the Python Assistant Window will be placed in the left side of the screen,
    #    it's height will be 41% of the screen height,
    #    it's width will be 26% of the screen
    #    it will be at the top (leaving empty space below it)
    # The empty space (either above or below the Python Assistant Window),
    # is left for the text editor (for editing the Macros) to be placed in.
    #
    pawWidthPercentInitial      = 37.5 # percent of the screen width
    pawHeightPercentInitial     = 32.0 # percent of the screen height
    pawAtBottomFlagInitial      = True
    #***********************************************************************************
    # import statements
    import sys, operator, os
    from os.path import expanduser
    from PySide import QtGui, QtCore

    # UI Class definitions

    class PythonAssistantWindow(QtGui.QMainWindow):
        """"""
        def __init__(self, pythonTextToEdit):
            self.textIn = pythonTextToEdit
            super(PythonAssistantWindow, self).__init__()
            self.initUI(pythonTextToEdit)
        def initUI(self, pythonTextToEdit):
            """Constructor"""
            # set default return value and pointer to subsequent child window
            self.result         = userCancelled
            self.childWindow    = None
            self.alertWindow    = None
            # set window dimensions for Python Advisor Window from the constants at the top of Macro file
            self.pawWinWidth    = pawWidthPercentInitial/100.0 * availableWidth
            self.pawWinHeight   = pawHeightPercentInitial/100.0 * availableHeight
            self.left           = screenWidth - self.pawWinWidth
            if pawAtBottomFlagInitial:
                self.top        = screenHeight - self.pawWinHeight
            else:
                self.top        = 0     
            self.editorHeight   = self.pawWinHeight
            # set dimensions for main FreeCAD window
            self.mainWinWidth   = availableWidth - (self.pawWinWidth+interWindowGap)
            self.mainWinHeight  = availableHeight
            # define main window
            FreeCADGui.getMainWindow().setGeometry(0, 0, self.mainWinWidth, self.mainWinHeight)
            # now set up this window
            self.setGeometry(self.left, self.top, self.pawWinWidth, self.pawWinHeight)
            self.setWindowTitle("Python Assistant Window")
            #
            centralWidget       =  QtGui.QWidget(self)
            layout              =  QtGui.QGridLayout()
            centralWidget.setLayout(layout)
            # set up text editing widget
            self.text_editor = QtGui.QPlainTextEdit(self)
            self.text_editor.move(0,0)
            self.text_editor.resize(self.pawWinWidth,self.editorHeight)
            self.text_editor.appendPlainText(self.textIn)
            self.text_editor.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
            self.text_editor.textChanged.connect(self.onTextChanged)
            # set up a monospace font for the text editor to match the Python console
            font = QtGui.QFont()
            font.setFamily("Courier")
            font.setStyleHint(QtGui.QFont.Monospace)
            font.setFixedPitch(True)
            font.setPointSize(12)
            self.text_editor.setFont(font)
            #self.text_editor.cursorPositionChanged.connect(self.onCursorPosition)
            self.cursor = self.text_editor.textCursor()
            # populate layout
            layout.addWidget(self.text_editor,0,0)
            self.setCentralWidget(centralWidget)
            # set contextual menu options for text editing widget
            # menu dividers
            mnuDivider1 = QtGui.QAction(self)
            mnuDivider1.setText(menuDividerText)
            mnuDivider1.triggered.connect(self.onMenuDivider)
            mnuDivider2 = QtGui.QAction(self)
            mnuDivider2.setText(menuDividerText)
            mnuDivider2.triggered.connect(self.onMenuDivider)
            mnuDivider3 = QtGui.QAction(self)
            mnuDivider3.setText(menuDividerText)
            mnuDivider3.triggered.connect(self.onMenuDivider)
            mnuDivider4 = QtGui.QAction(self)
            mnuDivider4.setText(menuDividerText)
            mnuDivider4.triggered.connect(self.onMenuDivider)
            # clear text
            mnuClear = QtGui.QAction(self)
            mnuClear.setText("Clear")
            mnuClear.triggered.connect(self.onClear)
            # paste copy/paste buffer
            mnuPaste = QtGui.QAction(self)
            mnuPaste.setText("Paste")
            mnuPaste.triggered.connect(self.onPaste)
            # paste contents of console
            mnuAppendFromConsole = QtGui.QAction(self)
            mnuAppendFromConsole.setText("Append contents of console")
            mnuAppendFromConsole.triggered.connect(self.onAppendFromConsole)
            # select between markers
            mnuSelectMarkers = QtGui.QAction(self)
            mnuSelectMarkers.setText("Select between markers")
            mnuSelectMarkers.triggered.connect(self.onSelectMarkers)
            # select all
            mnuSelectAll = QtGui.QAction(self)
            mnuSelectAll.setText("Select all")
            mnuSelectAll.triggered.connect(self.onSelectAll)
            # insert marker
            mnuInsertMarker = QtGui.QAction(self)
            mnuInsertMarker.setText("Insert marker")
            mnuInsertMarker.triggered.connect(self.onInsertMarker)
            # remove console generated ">>> " character strings
            mnuStripPrefix = QtGui.QAction(self)
            mnuStripPrefix.setText("Remove '>>> '")
            mnuStripPrefix.triggered.connect(self.onStripPrefix)
            # remove blank lines
            mnuReduceBlankLines = QtGui.QAction(self)
            mnuReduceBlankLines.setText("Delete multiple blank lines")
            mnuReduceBlankLines.triggered.connect(self.onReduceBlankLines)
            # copy selection
            mnuCopy = QtGui.QAction(self)
            mnuCopy.setText("Copy")
            mnuCopy.triggered.connect(self.onCopy)
            # copy selection to console
            mnuCopySelectionToConsole = QtGui.QAction(self)
            mnuCopySelectionToConsole.setText("Copy selection to console")
            mnuCopySelectionToConsole.triggered.connect(self.onCopySelectionToConsole)
            # copy to console
            mnuCopyToConsole = QtGui.QAction(self)
            mnuCopyToConsole.setText("Copy contents to console")
            mnuCopyToConsole.triggered.connect(self.onCopyToConsole)
            # save as file
            mnuSaveAsFile = QtGui.QAction(self)
            mnuSaveAsFile.setText("Save contents to file")
            mnuSaveAsFile.triggered.connect(self.onSaveAsFile)
            # close window
            mnuCloseWindow = QtGui.QAction(self)
            mnuCloseWindow.setText("Close window")
            mnuCloseWindow.triggered.connect(self.onCloseWindow)
            # alter GUI settings
            mnuSettings = QtGui.QAction(self)
            mnuSettings.setText("=Alter GUI settings=")
            mnuSettings.triggered.connect(self.onSettings)
            # define menu and add options
            self.text_editor.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
            self.text_editor.addAction(mnuCopy)
            self.text_editor.addAction(mnuCopySelectionToConsole)
            self.text_editor.addAction(mnuCopyToConsole)
            self.text_editor.addAction(mnuDivider1)
            self.text_editor.addAction(mnuPaste)
            self.text_editor.addAction(mnuAppendFromConsole)
            self.text_editor.addAction(mnuSelectMarkers)
            self.text_editor.addAction(mnuSelectAll)
            self.text_editor.addAction(mnuClear)
            self.text_editor.addAction(mnuDivider2)
            self.text_editor.addAction(mnuInsertMarker)
            self.text_editor.addAction(mnuStripPrefix)
            self.text_editor.addAction(mnuReduceBlankLines)
            self.text_editor.addAction(mnuDivider3)
            self.text_editor.addAction(mnuSaveAsFile)
            self.text_editor.addAction(mnuSettings)
            self.text_editor.addAction(mnuCloseWindow)
            #
            self.show()
        #----------------------------------------------------------------------
        def onMenuDivider(self):
            # just a divider in the menu so we don't do anything
            pass
        def onClear(self):
            # clear editing field
            self.text_editor.clear()
        def onPaste(self):
            # paste contents of system copy/paste buffer into QPlainTextEdit field
            self.text_editor.paste()
        def onAppendFromConsole(self):
            # copy text from "Python console"
            mainWindow  = FreeCADGui.getMainWindow()
            pcDW        = mainWindow.findChild(QtGui.QDockWidget, "Python console")
            pcPTE       = pcDW.findChild(QtGui.QPlainTextEdit, "Python console")
            consoleStr  = pcPTE.document().toPlainText()
            self.text_editor.appendPlainText(copyFromConsoleText)
            self.text_editor.appendPlainText("")
            self.text_editor.appendPlainText(consoleStr)
        def onCopy(self):
            # copy selected text to system copy/paste buffer
            self.text_editor.copy()
        def onCopySelectionToConsole(self):
            # copy selected text to "Python console"
            mainWindow  = FreeCADGui.getMainWindow()
            pcDW        = mainWindow.findChild(QtGui.QDockWidget, "Python console")
            pcPTE       = pcDW.findChild(QtGui.QPlainTextEdit, "Python console")
            #
            cursor      = self.text_editor.textCursor()
            cursorText  = self.text_editor.toPlainText()
            textToCopy = cursorText[cursor.selectionStart():cursor.selectionEnd()]
            if len(textToCopy)>0:
                pcPTE.appendPlainText(textToCopy)
        def onCopyToConsole(self):
            # copy text to "Python console"
            mainWindow  = FreeCADGui.getMainWindow()
            pcDW        = mainWindow.findChild(QtGui.QDockWidget, "Python console")
            pcPTE       = pcDW.findChild(QtGui.QPlainTextEdit, "Python console")
            pcPTE.appendPlainText(copyToConsoleText)
            pcPTE.appendPlainText()
        def onInsertMarker(self):
            # insert marker
            self.text_editor.insertPlainText(markerText)
        def onStripPrefix(self):
            # strip out ">>> " from text edit window
            self.text_editor.selectAll()
            if len(self.text_editor.toPlainText())>0:
                self.text_editor.selectAll()
                tmp = self.text_editor.toPlainText()
                self.text_editor.clear()
                self.text_editor.appendPlainText(tmp.replace(">>> ",""))
        def onReduceBlankLines(self):
            # reduce multiple blank lines to single blank lines
            contents = self.text_editor.toPlainText()
            self.text_editor.clear()
            self.text_editor.appendPlainText(os.linesep.join([s for s in contents.splitlines() if s]))
        def onSelectMarkers(self):
            cursor      = self.text_editor.textCursor()
            cursorText  = self.text_editor.toPlainText()
            bNum = cursor.blockNumber(); cNum = cursor.columnNumber()
            pos = cursor.position(); cursorTextLength = len(cursorText)
            occurrences = [i for i in range(len(cursorText)) if cursorText.startswith(markerText, i)]
            if len(occurrences)==0:
                self.alertWindow = QtGui.QMessageBox()
                self.alertWindow.setText("There are no markers...")
                self.alertWindow.show()
            elif len(occurrences)==1:
                hdrStart = occurrences[0]
                hdrEnd = hdrStart + markerTextLength
                if pos<hdrStart:
                    selectStart = 0; selectEnd = hdrStart
                    self.cursor.setPosition(selectStart)
                    self.cursor.setPosition(selectEnd, QtGui.QTextCursor.KeepAnchor)
                    self.text_editor.setTextCursor(self.cursor)
                if pos>hdrEnd:
                    selectStart = hdrEnd; selectEnd = cursorTextLength
                    self.cursor.setPosition(selectStart)
                    self.cursor.setPosition(selectEnd, QtGui.QTextCursor.KeepAnchor)
                    self.text_editor.setTextCursor(self.cursor)
            else:
                startOccurrences = list(); endOccurrences = list(occurrences)
                for i in range(len(occurrences)):
                    startOccurrences.append(occurrences[i] + markerTextLength + 1)
                startOccurrences.insert( 0, 0)
                endOccurrences.insert( len(occurrences), cursorTextLength)
                for i in range(len(occurrences)+1):
                    if startOccurrences[i]<pos<endOccurrences[i]:
                        if i==0:
                            selectStart = startOccurrences[i]
                        else:
                            selectStart = startOccurrences[i]-1
                        selectEnd = endOccurrences[i]
                        self.cursor.setPosition(selectStart)
                        self.cursor.setPosition(selectEnd, QtGui.QTextCursor.KeepAnchor)
                        self.text_editor.setTextCursor(self.cursor)
                        break
        def onSelectAll(self):
            self.text_editor.selectAll()
        def onCloseWindow(self):
            self.close()
        def onSettings(self):
            # get new width (as %), height (as %), vertical flag
            self.childWindow = GetGuiConfigParams(self)
            pass
        def onTextChanged(self):
            FreeCAD.PythonAssistantWindowStatus[1] = True
        def onCursorPosition(self):
            #print ("Line: {} | Column: {}".format(
            #   self.text_editor.textCursor().blockNumber(),
            #   self.text_editor.textCursor().columnNumber()))
            #print self.text_editor.textCursor().position()+self.text_editor.textCursor().columnNumber()
            pass
        def onSaveAsFile(self):
            filePath = QtGui.QFileDialog.getSaveFileName(parent=None,caption="Save contents as",dir=expanduser("~"),filter="*.txt")
            file = open(filePath[0],"w")
            file.write(self.text_editor.toPlainText())
            file.close()
        def closeEvent(self,event):
            # write out contents for next session
            file = open(persistenceFile,"w")
            file.write(self.text_editor.toPlainText())
            file.close()
            # clear global flag
            del FreeCAD.PythonAssistantWindowStatus
            self.close()

    class GetGuiConfigParams(QtGui.QMainWindow):
        """"""
        def __init__(self, parentWindow):
            self.parentWindow = parentWindow
            super(GetGuiConfigParams, self).__init__()
            self.initUI(parentWindow)
        def initUI(self, parentWindow):
            """Constructor"""
            self.result                         = userCancelled
            # grab geometry from our parent so we can tell if user has changed values
            self.initialParentWindowX           = self.parentWindow.geometry().x()
            self.initialParentWindowY           = self.parentWindow.geometry().y()
            self.initialParentWindowH           = self.parentWindow.geometry().height()
            self.initialParentWindowW           = self.parentWindow.geometry().width()
            self.initialHeightSliderSetting     = self.initialParentWindowH/float(availableHeight)*100
            self.initialWidthSliderSetting      = self.initialParentWindowW/float(availableWidth-interWindowGap)*100
            # set some fixed GUI attributes
            width                               = 450
            height                              = 40
            buttonWidth                         = 80
            sliderWidth                         = 100
            self.setWindowTitle("GUI Configuration")
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.resize(width, height)
            self.widthSlider                    = self.initialWidthSliderSetting
            self.heightSlider                   = self.initialHeightSliderSetting
            #
            centralWidget                       =  QtGui.QWidget(self)
            layout                              =  QtGui.QGridLayout()
            centralWidget.setLayout(layout)
            verticalLine                        =  QtGui.QFrame()
            # sliders
            widthSlider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
            widthSlider.setFocusPolicy(QtCore.Qt.NoFocus)
            widthSlider.valueChanged[int].connect(self.widthSliderChangeValue)
            widthSlider.setFixedWidth(sliderWidth)
            widthSlider.setValue(self.initialWidthSliderSetting)
            heightSlider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
            heightSlider.setFocusPolicy(QtCore.Qt.NoFocus)
            heightSlider.valueChanged[int].connect(self.heightSliderChangeValue)
            heightSlider.setFixedWidth(sliderWidth)
            heightSlider.setValue(self.initialHeightSliderSetting)
            # labels
            pawWidthLbl     = QtGui.QLabel("Python Assistant Window width", self)
            pawHeightLbl    = QtGui.QLabel("Python Assistant Window height", self)
            # radio buttons - window top or bottom
            self.rb1 = QtGui.QRadioButton("Window at Top",self)
            self.rb1.clicked.connect(self.onRb1)
            self.rb2 = QtGui.QRadioButton("Window at Bottom",self)
            self.rb2.toggle() # set default value
            self.rb2.clicked.connect(self.onRb2)
            if self.parentWindow.geometry().y()==0:
                self.rb1.toggle()
            # cancel button
            cancelButton = QtGui.QPushButton('Cancel', self)
            cancelButton.clicked.connect(self.onCancel)
            cancelButton.setFixedWidth(buttonWidth)
            # OK button
            okButton = QtGui.QPushButton('OK', self)
            okButton.clicked.connect(self.onOk)
            okButton.setFixedWidth(buttonWidth)
            #
            verticalLine.setFrameStyle(QtGui.QFrame.VLine)
            verticalLine.setSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
            #
            pawWidthLbl.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
            pawHeightLbl.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
            self.rb1.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
            self.rb2.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
            # populate layout
            layout.addWidget(widthSlider,0,0)
            layout.addWidget(pawWidthLbl,0,1)
            layout.addWidget(heightSlider,2,0)
            layout.addWidget(pawHeightLbl,2,1)
            layout.addWidget(verticalLine,0,2,3,1)
            layout.addWidget(self.rb1,0,3)
            layout.addWidget(self.rb2,2,3)
            layout.addWidget(cancelButton,3,1,QtCore.Qt.AlignRight)
            layout.addWidget(okButton,3,3)
            #
            self.setCentralWidget(centralWidget)
            #
            self.show()
        def widthSliderChangeValue(self, value):
            self.widthSliderValue = value
        def heightSliderChangeValue(self, value):
            self.heightSliderValue = value
        def onRb1(self):
            pass
        def onRb2(self):
            pass
        def onCancel(self):
            self.result = userCancelled
            self.close()
        def onOk(self):
            self.result = "OK"
            # the two slider values are the width and height of the Python Assistant Window
            # resize main FreeCAD window
            freeCadMainWidth    = ((1-(self.widthSliderValue/100.0)) * availableWidth)-(3*interWindowGap)
            FreeCADGui.getMainWindow().setGeometry(0, 0, freeCadMainWidth, availableHeight)
            # resize the PAW window
            newPawWidth         = availableWidth-freeCadMainWidth
            newPawHeight        = (self.heightSliderValue/100.0) * availableHeight
            if self.rb1.isChecked():
                newPawTop       = 0
            else:
                newPawTop       = availableHeight - newPawHeight
            self.parentWindow.setGeometry(freeCadMainWidth+interWindowGap, newPawTop, newPawWidth-interWindowGap, newPawHeight)
            self.close()

    #----------------------------------------------------------------------

    # Class definitions
            
    # Function definitions

    def onFreeCADShutdown():
        # this will be invoked when FreeCAD is told to shut down
        #QtGui.QMessageBox.information(None,"","FreeCAD shutting down")
        if FreeCAD.PythonAssistantWindowStatus[1]:
            reply = QtGui.QMessageBox.question(None, "",
                "The Python Assistant Window has changes, do you want to save them?",
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                # write out contents for next session
                file = open(persistenceFile,"w")
                file.write(FreeCAD.PythonAssistantWindowStatus[0].text_editor.toPlainText())
                file.close()
        del FreeCAD.PythonAssistantWindowStatus

    # Constant definitions

    userCancelled       = "Cancelled"
    markerText          = "#=========== marker ===========\n"
    markerTextLength    = len(markerText)
    copyFromConsoleText = "#=========== copy from console ==========="
    copyToConsoleText   = "#============ copy to console ============"
    menuDividerText     = "--------"
    interWindowGap      = 3 # space between 2 windows for appearance sake
    persistenceFile     = App.ConfigGet("UserAppData")+"PythonAssistantWindow.txt"
    # code ***********************************************************************************
    # put down user data saving routine for when FreeCAD exits
    mw=Gui.getMainWindow()
    mw.mainWindowClosed.connect(onFreeCADShutdown)
    # get screen dimensions
    screenWidth         = QtGui.QDesktopWidget().screenGeometry().width()
    screenHeight        = QtGui.QDesktopWidget().screenGeometry().height()
    # get dimensions for available space on screen
    availableWidth      = QtGui.QDesktopWidget().availableGeometry().width()
    availableHeight     = QtGui.QDesktopWidget().availableGeometry().height()

    if not hasattr(FreeCAD,"PythonAssistantWindowStatus"):
        previousContents = ""
        if os.path.isfile(persistenceFile):
            # read contents of last session
            file = open(persistenceFile,"r")
            previousContents = file.read()
            file.close()
        # open window with contents from last session
        form = PythonAssistantWindow(previousContents)
        # save pointer to window so it can be located again and Raised when it becomes obscured
        FreeCAD.PythonAssistantWindowStatus = [None, False]
        FreeCAD.PythonAssistantWindowStatus[0] = form
    else:
        # window is open so Raise it so it is visible
        FreeCAD.PythonAssistantWindowStatus[0].raise_()
        pass
    #
    #OS: Mac OS X
    #Word size: 64-bit
    #Version: 0.14.3703 (Git)
    #Branch: releases/FreeCAD-0-14
    #Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
    #Python version: 2.7.5
    #Qt version: 4.8.6
    #Coin version: 3.1.3
    #SoQt version: 1.5.0
    #OCC version: 6.7.0
    #
    #thus ends the macro...




