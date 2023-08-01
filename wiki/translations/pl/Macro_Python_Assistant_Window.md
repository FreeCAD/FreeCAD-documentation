# Macro Python Assistant Window/pl
{{Macro
|Name=Macro Python Assistant Window
|Description=This macro provides a cut/copy/paste workspace for Python code, it is segmented so different sections can be selected and it is persistent between FreeCAD sessions.
|Author=Piffpoof
|Version=1.0
|Date=2015-01-21
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/4/45/Macro_Python_Assistant_Window.png ToolBar Icon]
}}

One of Python\'s powerful aspects is the Python Console which serves both as an output device and a dynamic interpreter of source code. The Python Assistant Window (subsequently referred to as \'PAW\') provides additional functionality to the Python Console. {{Codeextralink|http://pastebin.com/raw/2m0u94Z1}} <img alt="" src=images/PythonAssistantWindowScreenSnapshot.jpg  style="width:500px;">

## Description

As a modern development environment, Python has a lot of advantages over older languages and their development environments. One large benefit is the Python Console where code can be interactively entered and the results received ([REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)). Those results can then be copied and used to either build up Python source code (in a source editor) or pasted back into the Python Console in an altered form to receive further output. This is a very powerful method of developing code.

As powerful as it may be, two readily apparent shortcomings with the Python Console are:

-   the console is of limited size and the results of your work from 20 minutes ago may be scrolled far off the screen, they are not lost but they are awkward to retrieve
-   the console is cleared each time you quite your FreeCAD session, the console is empty (aside from the Python startup message) next time you start FreeCAD

The PAW provides the following:

-   it is persistent between FreeCAD sessions, things will not \"disappear\" from it unless the user removes them
-   it has a contextual menu that allows the following:
    -   the standard editing operands: Copy & Paste & Select All
    -   Copy a selection to the Python Console
    -   Copy the complete contents of the PAW to the Python Console
    -   Append the contents of the Python Console to the PAW
    -   insert textual markers that facilitate management of the text
    -   selection between any two consecutive markers
    -   remove the prefix \"\>\>\> \" which the Python Console uses to denote output
    -   reduce multiple blank lines to single blank lines
    -   personalise the working environment by managing the PAW (as well as the main FreeCAD window) by a slider-based GUI

## Installation

All the code for pythonAssistantWindow.FCMacro is in one macro. So installation is comprised of copying the code to the appropriate Macro directory and invoking pythonAssistantWindow from the Macro menu, the Python console or a toolbar button (the preferred method).

-   see [How to install macros](How_to_install_macros.md) for information on how to install this macro code
-   see [Customize Toolbars](Customize_Toolbars.md) for information how to install as a button on a toolbar

Note: A global variable within FreeCAD is used to coordinate the persistent storage.

Note: A text file in the \"UserAppData\" directory is used to store the textual contents of the PAW between FreeCAD sessions.

## Usage

The PAW is best used as a button on a toolbar. It can be run from the Macro Menu or the code pasted onto the Python Console but the latter two options really detract from it\'s ease of use.

When FreeCAD is started there will be no sign of the PAW, other than a button on a toolbar. Clicking the button will cause:

-   the PAW to open in the lower right corner
    -   the default settings are for the about 1/3 of the screen width to be dedicated to the PAW with the remainder being used by the main FreeCAD window, the height of the PAW will be about 1/3 of the window height
-   the contents of the PAW when it last ran will appear in the window - there should be no difference from the last time it was used
    -   if the PAW has not run before then the contents will be empty
-   if the PAW is already open but hidden by other windows then it will be raised to the top so that it becomes visible
-   closing the PAW will cause the contents to be written to file and the window will close - there is no Dialog asking whether to save or not
-   however there is a Dialog asking whether to save if FreeCAD is quit (Menu-\>Quit FreeCAD) with unsaved changes in thePAW

Most of the functionality for the PAW is provided by the contextual menu, the options are:

-   Copy
    - provide the standard Copy function
-   Copy selection to console
    - the current selection is copied to the end of the Python Console
-   Copy contents to console
    - the complete contents of the PAW is copied to the end of the Python Console
-   Paste
    - provide the standard Paste function
-   Append contents of Python Console to PAW
    - the copies of the Python Console are placed at the end of the PAW - note that the contents of the Python Console may be a mixture of Python Code, output from Python Code, error message text, output from any part of FreeCAD
-   Select between Markers
    - markers are used to divide up the text of the PAW into sections, once the contents are in sections then a section can be selected individually and worked with (e.g. Copy, Copy to the Python Console, Delete). The intention of Markers is to allow separate and unrelated sequences of Python statement to exist in the PAW, and then be managed and worked with individually.
-   Select all
    - provide the standard Select All function
-   Clearbr
    - provide the standard Clear function where all the text in the PAW is deleted
-   Insert marker
    - insert a textual Marker at the current cursor location
-   Remove \"\>\>\> \"
    - after Python Console output is copied to the PAW, any lines which were output from executed Python commands will be prefixed with \"\>\>\> \", this option removed those prefixes so the output can be used as context free data
-   Reduce multiple blank lines to single blank lines
    - compacts the text by removing multiple blank lines
-   Alter GUI settings
    - brings up a modal window with three controls:
-   <img alt="" src=images/PythonAssistantWindowGui2.jpg  style="width:500px;">
    -   a slider to set the percentage of the screen width dedicated to the PAW (remembering that there is a certain width which the FreeCAD main window will not go below)
    -   a slider to set the percentage of the height of the screen dedicated to the PAW
    -   a pair of radio buttons to indicate whether the PAW should be placed at the top or bottom of the left hand side of the screen
-   Save as file
    - the contents of the PAW window are written out to a user selected file - the contents of the PAW are not altered
-   Close window
    - the PAW window is closed and the contents written out to the persistent storage file
    Note: there is no Dialog asking about saving, it is done automatically

## User Interface 

The user interface is a simple text editing window, there is one button to start the PAW and a contextual menu of options to perform on the text in the text editing window. The options are described in the Usage section.

## Examples

**A First Example**

In January your co-worker needs some help with the Python code to update a file. You write and debug it on your computer and send him the source code. You have come up with 3 different ways to do the job and are not sure which is the best to keep. You copy all 3 finished versions to the PAW and separate them by Markers.

As the month of May starts, you are happily working on the bottle project using FreeCAD. There is some problem getting the exact Python code to generate what is required so you model this graphically and the equivalent Python code is generated on the Python Console. Using PAW you copy the contents of the Python Console to the PAW. You shape it by moving it back and running, copying the results, modifying them in PAW and copying them back until you are happy.

The next Monday your boss rushed over to say that there is a big requirement for a CAD operator at the plant where they are having problems with the folding sequence for the new packaging stream. You will fly there the same day and be there for 2 weeks. You complete your assignment and return to your normal office space.

When you get back it is obvious that people have been using your area for a lunch area so you have to clean up a bit. Upon starting FreeCAD and clicking the PAW button on the toolbar, your work from before is sitting there as if it is from the day before. You realise that the solution to your bottle design lies in the file code you wrote back in January along with what you left 2 weeks earlier. Quickly you can select and copy the code segments to the Python Console to execute and fine tune them.

Once the code is stable then you can save it to a file for either e Python file or a FreeCAD macro file.

**Another Example**

You are trying to find out what is going wrong with the Rotation values of various objects in an Assembly. Out of 27 objects you can\'t see any pattern as to which objects will be affected. So you put a few lines of Python together to isolate the incorrect objects, paste it into the PAW. Then take a couple of lines of Python to get the Label and Rotation values, paste that code to the PAW as well. Copy the code to detail all the objects you need to see listed and repeat it for each object - all in the PAW. The Python Console will have all these results (including any typing errors and error messages) but it will have scrolled off the visible portion of the window long ago. So now you have a concise set of Python lines, you copy it from the PAW, paste it into the Python Console and there is the exact list of the objects which need debugging - along with their specific values. If needed you could then paste the results from the Python Console back into the PAW - prefix it with the Python comment character (\'#\') if you want to save it in the Python code and keep it executable. Finally you can save this conglomeration to a file from the PAW so it is secure on disk. Ready for the next time you need to steal or adapt the logic in the code.

## Options

About the only option for the PAW is the ability to alter it\'s initial display size and shape in accordance with the size and shape fo the main FreeCAD window. There are 3 constant values in the Python code which initial size and placement of the PAW.

## Remarks

There is a very simple proof of concept for a persistent storage work in this code. It may be of use to anyone else requiring such a capacity.

## Links

none (so far)

## Script


**'''If the script listing does not end with FreeCAD version information and a last line of "thus ends the macro..." then the Wiki has eaten the script again and you will have to download or copy it from [[http://pastebin.com/raw.php?i=2m0u94Z1 unabbreviated script on pastebin.com]]'''**

ToolBar Icon ![](images/Macro_Python_Assistant_Window.png )

**Macro_Python_Assistant_Window.FCMacro**

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
        #
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

    #

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
    menuDividerText     = ""
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



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Python Assistant Window/pl
