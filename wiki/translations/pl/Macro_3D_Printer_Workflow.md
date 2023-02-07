# Macro 3D Printer Workflow/pl
<div lang="en" dir="ltr" class="mw-content-ltr">


{{Macro
|Name=Macro 3D Printer Workflow
|Description=Macro that creates an stl file with perfect rounding, i.e. without visible facets, from selected objects. It also allows to launch programs of your choice. For example to automate the FreeCAD → Slicer → printing workflow.<br>
After the creation of the stl file you can, for example, open your slicer with the stl file, switch on your printer, heat the printer bed and, if necessary, trigger additional commands in your home automation.
|Author=2cv001
|Download=[https://wiki.freecadweb.org/images/b/b4/Macro_3D_Printer_Workflow.png ToolBar icon]
|Version=00.02
|Date=2023-01-21
|FCVersion=All
}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Description


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

This macro creates an stl file with perfect rounding, i.e. without visible facets, from selected parts. It also allows to launch programs of your choice. For example to automate the FreeCAD → Slicer → printing workflow.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

After the creation of the stl file you can, for example, open your slicer with the stl file, switch on your printer, heat the printer bed and, if necessary, trigger additional commands in your home automation.


</div>

![](images/Macro_3D_Printer_Workflow_Dialog.png )


<div lang="en" dir="ltr" class="mw-content-ltr">

### Principle of smoothing 


</div>

![](images/Macro_3D_Printer_Workflow_With_Facets.png )


<div lang="en" dir="ltr" class="mw-content-ltr">



*With visible facets*


</div>

![](images/Macro_3D_Printer_Workflow_Without_Facets.png )


<div lang="en" dir="ltr" class="mw-content-ltr">



*Without visible facets*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The macro modifies the deviation property of the solids before creating the stl file and restores the original values afterwards. Next it can launch the stl file which will open for example under Cura, if the stl extension has been associated with that program on your operating system.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Launching other programs or commands 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The macro can launch additional programs or commands that you might enter in a terminal:

-   Turn on the printer and the light (requires a computer controlled socket).
-   Connect Octoprint to the printer.
-   Start preheating the printer bed.
-   Save your FreeCAD and stl file somewhere.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Setup


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Check that the stl extension is associated with your slicer on your operating system. In other words, when you double-click an stl file your slicer should open and load your stl file.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

If you run the macro as it is, it will just create the stl without visible facets, but no others programs will be launched. For that you have to edit the lines of code that come after commands=[ in the section *Parameters that can be changed*. Have a look at the comments in the [Code](#Code.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Usage


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Select one or more solid objects to print.
2.  Start the macro.
3.  The dialog opens:
    ![](images/Macro_3D_Printer_Workflow_Dialog.png )
4.  Check the desired options in the left column.
5.  Enter the **Accuracy (param deviation)**:
    -   0.5 is the default value in FreeCAD.
    -   0.05 allows a stronger smoothing.
    -   0.01 is perfect from a smoothing point of view.
6.  Press the **OK** button.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The lower the deviation, the better the quality, but the larger the size of the stl file. The value must be between 0 and 1


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Links


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [Forum discussion (French)](https://forum.freecadweb.org/viewtopic.php?f=12&t=52138)
-   [Macros recipes](Macros_recipes.md)
-   [How to install macros](How_to_install_macros.md)
-   [How to customize toolbars](Customize_Toolbars.md)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Credits


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Thanks to openBrain for the help on the code. Very good teacher!
Thanks to Mario 52, David69 and Roy_043 for the help on this wiki.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Script


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

ToolBar Icon ![](images/Macro_3D_Printer_Workflow.png )


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Code


</div>

ver 00.02 21/01/2023 by 2cv001 **3D_Printer_Workflow.FCMacro**

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # ==================================================================
    # ==================================================================
    # ==                                                              ==
    # ==  Workflow to print with "stl" file with perfect rounding     ==
    # ==  and launch others programs                                  ==
    # ==                                                              ==
    # ==================================================================
    # ==================================================================
    __author__ = "2cv001"
    __title__   = "Macro_3D_Printer_Workflow"
    __version__ = "v00.02"
    __date__    = "2023/01/21"    #YYYY/MM/DD
    __icon__    = "https://wiki.freecadweb.org/images/b/b4/Macro_3D_Printer_Workflow.png"
    __Wiki__    = "http://www.freecadweb.org/wiki/Macro_3D_Printer_Workflow"
    """
    Macro that creates an "stl" file with perfect rounding
    = without visible facets.
    It also allows to launch programs of your choice
    For example to automate the FreeCAD -> Slicer -> printing workflow

    Principle of smoothing : it modifies the deviation property of the solids before
    generation of the stl and then replace the old values
    At the end, it proposes to launch the stl file which will open for example under
    cura if the stl extension has been associated with cura in your operating system.

    Launching other programs or commands :
    You can ask it to chain any program or command that you might
    type in a terminal.
    To do this, you must change what is in the
    "parameters that can be changed" section.

    Examples of applications:
    - Turn on the printer and the light (requires for example a controlled socket)
    - Connect octoprint to the printer
    - Start the tray preheating
    - Save your FreeCAD and stl file
    ....


    Tested on windows and Linux
    """
    import FreeCAD as App
    import Mesh
    from PySide2 import QtCore, QtWidgets
    import os, sys, subprocess
    import time
    import FreeCADGui as Gui

    #================================
    # Parameters that can be changed
    #================================

    # Smoothing management
    #

    # deviation : default value that will be displayed in the dialog box.
    # 0.5 is the default value in FreeCad, 0.05 allows a stronger smoothing.
    # 0.01 is perfect from a smoothing point of view.
    # The lower the value, the better the quality,
    # but the larger the size of the stl file
    # the value must be between 0 and 1
    deviation=0.01
    doitLancerFichier=True # if True, it will be proposed to launch the stl file.
                                     # otherwise put False

    # Automatic program launch,
    # Automation of the production line
    #

    delaiMax=10 # if the user enters a delay greater than this value,
                       # it will be reduced to delaiMax

    #To launch programs of your choice
        #Typically for example a home automation program, 
        #turn on your printer or/and a light etc.
        #Use the following syntax by adding after the line "# insert your lines here."
    #   a line with this syntax (important: align the [ with the others):
    #  [ ['command to execute', 'param 1', param 2, ] ,'.extention','question to ask', waiting time],
    # Details of the syntax :
    #  'command to execute' : the command you want to execute. 
    #  'param 1, param 2,...' : if your program needs parameters. 
    #    These parameters will be taken into account only if extention=''.
    #
    #  'extention': if not empty then the first parameter will be replaced by the name of 
    #    your FreeCAD file but with this extension.
    #  'question to ask': the question to display in the dialog box
    #  time_wait : optional : nb of seconds to wait after execution
    #    allows for example to wait for the printer to start before asking it to heat the plate

    #  Note the double \ in place of \ (because the special characters
    #    must be preceded by an \ in python). Ditto for the apostrophe for example
    #  the lines in question are to be inserted further down after commands=[...
    #
    # Examples of possible launches:

    """
    To launche a program :
    [ ['calc.exe'                                         ] ,''    ,'Launch the calculator ?'],
    [ ['C:\\WINDOWS\\system32\\mspaint.exe','dessin.jpg'  ] ,''    ,'Launch  Paint ?'          ],
    [ ['C:\\Program Files\\Ultimaker Cura 4.8.0\\Cura.exe'] ,'.stl','Launch  Cura ?'           ],
    [ ['C:\\Program Files\\Mozilla Firefox\\firefox.exe','https://octopi.local'],'','Launch Octoprint ?'],
        On linux:
    [ [   'firefox','https://octopi.local'                ] , ''   ,'Launch Octoprint ?'      ], 
    To launch a web page (here, a php program)
    [ ['curl','http://pidomotique/connecte.php'           ] , ''   ,'Connect the printer ?'],
    Example of printer control via octoprint (if you have it...):
       temperature setting of the plate
    - Replace the XXX after X-Api-Key: by your API key
    (found in the octoprint parameters)
    - Replace http://octopi.local by the url with which you access octoprint
    - Change the value 050 in "M140 S050". S050 indicates that you need to heat to 50°.
         if you want 60°, replace S050 by S060
    - 6 lines to copy after having adapted it:
      [
          [  'curl','-H', 'Content-Type: application/json','-H', 'X-Api-Key: XXXXXXXXXXXXXXXXXXXXX', '-X', 'POST',
                '-d {"command":"M140 S050"}','http://octopi.local/api/printer/command'
          ]
                , '','Warm up the printer plate ?'
      ],

    """


    commandes=[
    # insert your lines here.
    #  [ ['calc.exe'                                         ] ,''    ,'Lancer la calculatrice ?',2],
    #  [ ['C:\\Program Files\\Ultimaker Cura 5.2.1\\Ultimaker-Cura.exe'] ,'.stl','Lancer Cura ?'           ],
    #  [ ['curl','http://pidomotique/connecte.php'              ] , ''   ,'Allumer et connecter l\'imprimante ?',4],
    # 2 jeedom command that I use. Put a # at the begining of the 2 lines.
      [  ['curl', 'https://pijeedom/core/api/jeeApi.php?apikey=xxxxxxxxxxxxxxxxxxxxxxxxxx&type=cmd&id=4042','--insecure' ] , ''   ,'Turn on and connect printer ?',10],
      [  ['curl','https://pijeedom/core/api/jeeApi.php?apikey=xxxxxxxxxxxxxxxxxxxxxxxx&type=cmd&id=4048','--insecure'  ] , ''   ,'Heat the bed ?'],
      [  ['C:\\Program Files\\Mozilla Firefox\\firefox.exe','https://octopi'],'','Launch Octoprint ?'],



               ]


    #===============
    #Initialisations
    #===============
    dictionnaireOrigineDeviation={}
    mw = Gui.getMainWindow()
    indiceCommandeEtParam=0
    indiceExtFileNameParamCommandeALancer=1
    indiceTextAutreCommandeALancer=2
    indiceDelai=3

    # UI Class definitions
    class BoiteDialogueSTLGuiClass(QtWidgets.QDialog):

        def  __init__(self, parent=None):
            super(BoiteDialogueSTLGuiClass, self).__init__(parent)
            self.initUI()

        def initUI(self):
            self.tabCheckboxTextCommandes=[] # table of checkbox commands to run
            self.setGeometry( 250, 250, 400, 150)
            self.setWindowTitle("Export and launch software")
            lay = QtWidgets.QGridLayout(self)

            # checkboxs
            self.checkboxGenererSTL = QtWidgets.QCheckBox("Generate STL ?", self)
            self.checkboxGenererSTL.setCheckState(QtCore.Qt.Checked)
            lay.addWidget(self.checkboxGenererSTL, 0, 0)
            if doitLancerFichier :
                self.checkboxLancerSTL = QtWidgets.QCheckBox("Launch the slicer ?", self)
                self.checkboxLancerSTL.setCheckState(QtCore.Qt.Checked)
                lay.addWidget(self.checkboxLancerSTL, 2, 0)

            for posLigne, cmd in enumerate(commandes, start=3):
               textCommande=cmd[indiceTextAutreCommandeALancer]
               self.checkboxTextCommande = QtWidgets.QCheckBox(textCommande, self)
               # storing this checkbox in a table :
               self.tabCheckboxTextCommandes.append(self.checkboxTextCommande)
               self.checkboxTextCommande.setCheckState(QtCore.Qt.Checked)
               lay.addWidget(self.checkboxTextCommande, posLigne, 0)

            # numeric input field
            self.label2 = QtWidgets.QLabel('Accuracy (param deviation)\nbetween 0.01 and 1\n' +
                '0.01 for high quality', self)
            lay.addWidget(self.label2, 0, 1)

            self.precision = QtWidgets.QDoubleSpinBox(self)
            self.precision.setValue(deviation)
            self.precision.setRange(0.01,1)
            self.precision.setSingleStep(0.01)
            self.precision.setToolTip('The larger the number, the larger the file size\n' +
                'and the better the accuracy.\n' +
                'See the deviation parameter in FreeCAD')
            lay.addWidget(self.precision, 0, 2)

            butBox = QtWidgets.QDialogButtonBox(self)
            butBox.setOrientation(QtCore.Qt.Horizontal)
            butBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
            lay.addWidget(butBox)
            butBox.accepted.connect(self.accept)
            butBox.rejected.connect(self.reject)

            self.setLayout(lay)


    #===============
    #functions
    #===============
    def octopi(api,commande,urlOctopi,apiKey) :
        """
        Function that returns the parameter to pass to subprocess.Popen if you want to run an
        an octopi API. Not used here. But for memory purposes and a future evolution

        Arguments :
            api : the api to run ex: '/api/printer/command'
            commande : the command of the API in question ex: '{"command": "M140 S050"}'
            urlOctoprint : the url of your octopi ex : 'https://octopi.local'
            apiKey : the API key you find in setting/API of octoprint
        Returns :

       Example
           API running a gcode. Here the heating of the printer plate
           subprocess.Popen(
                              octopi(
                                    '/api/printer/command',
                                    '{"command":"M140 S050"}',
                                    'https://octopi.local',
                                    'XXXXKEYXAPIXXXXXXXX'))
                     ,close_fds=True)
        """
        commandeCurl=[
        'curl','-H', 'Content-Type: application/json','-H',
             'X-Api-Key: '+apiKey,
             '-X', 'POST',
            '-d '+commande,urlOctopi+api
        ]
        return commandeCurl


    def nameFileStl(dictionnaireOrigineDeviation,mw=Gui.getMainWindow()):
        """
        Function that determines and returns the file name including path
        where the stl will be saved
        The FreeCAD document containing the dictionary objects must be
        opened and saved

        Arguments :
            dictionaryOrigineDeviation (dictionary) :
                a dictionary whose keys are FreeCAD solids.
                the filename will be obtained from the filename of the
                of the document containing the first object (solid) of this
                dictionary

        Returns :
            '' if the document does not exist,
            otherwise the name of the file where the stl will be saved

        Example
        """

        doc=list(dictionnaireOrigineDeviation.keys())[0].Document
        if doc is None:
            QtWidgets.QMessageBox.information(mw,'Warning',\
                "You do not have a document open")
            return ''
        if doc.FileName=='':
            QtWidgets.QMessageBox.information(mw,
                 'Warning','Save your document before restarting the order')
            return ''
        return(os.path.splitext(doc.FileName)[0]+'.stl')

    def memoriseObjEtDeviation(selection,deviationImpose):
        """
        Memorises the solids that are contained in selection and their
        deviation property and replaces it with the value
        of deviationImpose
        It imposes a subsequent recompute by a touch.
        Recompute() must eventually be run after

        Arguments :
            selection: a selection of objects
    deviationImpose (float): value that we want to impose to deviation.

        Returns:
            a dictionary containing the object in key and the deviation in value
            Returns {} if there is no suitable object in the selection

        Example:
            memoriseObjEtDeviation(Gui.Selection.getSelection(),deviation)
        """
        dicoObjDeviation={}
        for objData in selection :
            if objData.isDerivedFrom('Part::Feature') \
              and not objData.isDerivedFrom('PartDesign::Feature')\
              and not objData.isDerivedFrom('Part::Part2DObject'):
                dicoObjDeviation[objData]=objData.ViewObject.Deviation
                objData.ViewObject.Deviation=deviationImpose
               # pour imposer un recompute même si la déviation est plus petite
               # qu'avant :
                objData.touch()
                for o in objData.ViewObject.claimChildren():
                        o.touch()
        return dicoObjDeviation

    def restitueDeviation(dicoOrigineDeviation):
        """
     Function that replaces the deviation property in the objects
        It imposes a recompute by a touch. recompute() must be
        run after

        Arguments:
            dicoOrigineDeviation a dictionary containing the object in key
            and the value to be imposed in the deviation property of the object
            in value

        Returns: Does not return anything

        Example:
            restitueDeviation(dicoOrigineDeviation)

        """
        for ob2 in dicoOrigineDeviation:
            ob2.ViewObject.Deviation=dicoOrigineDeviation[ob2]
            # to impose a recompute even if the deviation is smaller
            # than before:
            ob2.touch()
            for o in ob2.ViewObject.claimChildren():
                o.touch()

    def openFile(fileName):
        """
     function that launches a file depending on the operating system
        checked for now only under windows

        Arguments:
            fileName (string) the name of the file to run

        Returns
            Does not return anything

        Example:
            openFile(unfichier.stl)
            openFile(calc.exe)
        """
        if sys.platform == "win32":
            os.startfile(fileName)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.Popen([opener, fileName],close_fds=True)

    def recalcul(dicoObjs):
        """
        launches a recompute for each Document of the dico objects
        only if it has not already been done
        Arguments:
            dicoObjs a dictionary containing the object in key

        Returns
            Does not return anything

        Example:
            recalcul(dicoMesObjets)
        """
        docDejaRecalcul=[]
        for obj in dicoObjs:
            if obj.Document not in docDejaRecalcul:
                obj.Document.recompute()
                docDejaRecalcul.append(obj.Document)

    def lanceCommmandes(commandesAlancer,fileStlName,formBoiteDialogueSTL):
        """
        launch the orders
        Arguments:
            commandesAlancer in the form of an array of arrays
            [ ['command to execute', 'param 1', param 2, ] ,'.extention','question to ask',delay ],
              ['command to execute', 'param 1', param 2, ] ,'.extention','question to ask',delay ],
              ...
            ]
             'command to execute' : the command you want to execute.
             For example 'myProgram.exe' if need, put also its path.
             param 1, param2... ' : if your program needs parameters.
                Will only be taken into account if extention=''.
             'extention': if not empty, parameter param 1 will be the name of your
                  FreeCAD file but with your extension :
             question to ask': the question to display in the dialog box
             delay: waiting time in seconds before going to the next command.

        Returns
             Do not return anything

        Example:
            lanceCommmandes(commandes,fileStlName,formBoiteDialogueSTL) # lance les commandes que l'on a décrites dans commandes
        """

        for tbktc in formBoiteDialogueSTL.tabCheckboxTextCommandes :
            if tbktc.isChecked() :
                i= formBoiteDialogueSTL.tabCheckboxTextCommandes.index(tbktc)
                commande=commandesAlancer[i]
                commandeEtParam=commande[indiceCommandeEtParam]
                extFileNameParamCommandeALancer=commande[indiceExtFileNameParamCommandeALancer]
                textAutreCommandeALancer=commande[indiceTextAutreCommandeALancer]
                delai=0
                try :
                   if commande[indiceDelai:indiceDelai+1]!=[] : #si l'utilisateur a rentré un délai
                      delai=commande[indiceDelai]
                except :
                   print ('Délai non pris en compte car valeur numérique non valide'+
                          'pour la commande '+ textAutreCommandeALancer)
                if delai > delaiMax :
                    delai=delaiMax

                if extFileNameParamCommandeALancer!='':
                    if commandeEtParam[2:3]==[]  : # Il n'y a aucun paramètre.
                       # On ajoute un paramètre pour y mettre notre nom de fichier
                       # avec notre extension.
                       commandeEtParam.append('')
                    commandeEtParam[1]=   os.path.splitext(fileStlName)[0]+  extFileNameParamCommandeALancer
                subprocess.Popen(commandeEtParam,close_fds=True)
                print(commandeEtParam)
                time.sleep(delai)# Pause de durée delai secondes


    def run(objs=Gui.Selection.getSelection(), dev=deviation):
        """
        main function
        Arguments:
            doc: the active document
            objs : the objects that have been selected beforehand
            dev : the value of the deviation property which will be
                  imposed before the generation of the stl

        Returns
            Returns nothing

        Example:
            run()
        """

       #check if at least one solid (body and similar) has been selected
        nbBody=0
        for objData in objs :
            if objData.isDerivedFrom('Part::Feature') \
              and not objData.isDerivedFrom('PartDesign::Feature')\
              and not objData.isDerivedFrom('Part::Part2DObject'):
              nbBody=nbBody+1

        if nbBody==0: #  if we haven't found any solids, we have to have an active one
             try:
                objs=[]
                objs.append(Gui.ActiveDocument.ActiveView.getActiveObject('pdbody'))
                response=QtWidgets.QMessageBox.information(mw, 'Warning',\
                '-You did not select a solid. Automatic solid selection : '+objs[0].Label +
                ' by the macro..\n-If not adequate, select one or more solids before running the macro',
                      QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel )
                if response==QtWidgets.QMessageBox.Cancel :
                  return
             except :
                QtWidgets.QMessageBox.information(mw, 'Warning',\
                '--Select one or more solids before running the macro')
                return

    # Dialog box of what we want to do
        formBoiteDialogueSTL=BoiteDialogueSTLGuiClass(mw)
        if not formBoiteDialogueSTL.exec_() :
            return
        dev=formBoiteDialogueSTL.precision.value()
        # we memorize the selected solids and their deviation,
        # we make a touch() of their child to be taken into account in recompute :
        dictionnaireOrigineDeviation=memoriseObjEtDeviation(objs,dev)
        if len(dictionnaireOrigineDeviation)==0: # si on a trouvé aucun solide
            QtWidgets.QMessageBox.information(mw, 'Warning',\
                '-Select one or more solids before running the macro')
            return
        # we get the name of the file where we have to save the stl
        fileStlName=nameFileStl(dictionnaireOrigineDeviation)
        if fileStlName == '' :
            return
        #The solids in dictionaryOriginDeviation are passed as parameters
        if formBoiteDialogueSTL.checkboxGenererSTL.isChecked():
           Mesh.export(list(dictionnaireOrigineDeviation.keys()), fileStlName)
           print('Export done')
        # restitution of the original property deviation for all solids :
        restitueDeviation(dictionnaireOrigineDeviation)
        recalcul(dictionnaireOrigineDeviation)

        if formBoiteDialogueSTL.checkboxLancerSTL.isChecked():
                #runs for example cura if cura has been associated with *.stl files
                openFile(fileStlName)

        lanceCommmandes(commandes,fileStlName,formBoiteDialogueSTL)
                # runs the commands described in commands


    if __name__ == '__main__':
        run()



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro 3D Printer Workflow/pl
