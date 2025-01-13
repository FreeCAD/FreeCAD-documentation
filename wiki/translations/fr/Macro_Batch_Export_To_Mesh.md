# Macro Batch Export To Mesh/fr
{{Macro/fr
|Name=Batch Export To Mesh
|Description=Cette macro permet de convertir par lots en maillage et d'exporter des fichiers STL et OBJ.
|Author=Pablo Gil Fernández
|Version=2.16
|Date=2024-10-11
}}

## Description

Cette macro permet de convertir par lots en maillage et d\'exporter des fichiers STL et OBJ. Elle ajoute une interface graphique pour accélérer la conversion et l\'enregistrement des objets sélectionnés.

<img alt="general" src=images/Screenshot1.png  style="width:560px;">
<img alt="presets" src=images/Screenshot2.png  style="width:560px;">



## Fonctions

-   Option de maillage *standard* de FreeCAD
-   Noms personnalisés (objet, projet ou personnalisé)
-   Conversion/exportation d\'un ou plusieurs objets à la fois
-   Conversion d\'objets dans le projet FreeCAD actif ou dans un fichier STL ou OBJ
-   Exportation des objets vers des fichiers STL ou OBJ
-   Les chemins d\'accès absolus ou relatifs sont autorisés
-   Sélection des coordonnées locales ou globales (utile pour la conception d\'une impression 3D)
-   Crée des dossiers si nécessaire
-   Ouvre le dossier dans l\'explorateur de fichiers
-   Chargement/sauvegarde des préréglages
-   Mémorise le dernier préréglage utilisé

## Script


{{MacroCode|code=
<nowiki>
__Title__   = "Batch export to mesh"
__Author__  = "Pablo Gil Fernández"
__Version__ = "2.16"
__Date__    = "2024-10-11"
__Comment__ = "This macro helps batch converting to mesh and exporting STL and OBJ files"
__Web__ = "https://github.com/pgilfernandez/FreeCAD_Macro_Batch_Export_To_Mesh"
__Wiki__ = "https://wiki.freecad.org/Macro_Batch_Export_To_Mesh"
__Icon__  = "/usr/lib/freecad/Mod/Mesh/Resources/icons/MeshWorkbench.svg"
# __IconW__  = "C:/Documents and Settings/YourUserName/Application Data/FreeCAD"
__Help__ = "https://forum.freecadweb.org/viewtopic.php?f=22&t=41219"
__Status__ = "stable"
__Requires__ = "FreeCAD 0.17"
__Communication__ = "https://github.com/pgilfernandez/FreeCAD_Macro_Batch_Export_To_Mesh"

import FreeCAD, FreeCADGui, Draft, Part, PartGui, math, PartDesignGui, Mesh, MeshPart, Import, os
from FreeCAD import Base
from PySide import QtGui, QtCore
from math import cos, radians
from pivy import coin
import sys
import subprocess
import Mesh

App = FreeCAD
Gui = FreeCADGui

# If developer mode is True it will show important messages on the Report panel:
dev_mode = False

class SavePresetDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(SavePresetDialog, self).__init__(parent)
        self.setWindowTitle("Save Preset")
        self.layout = QtGui.QVBoxLayout()

        self.label = QtGui.QLabel("Enter new preset name:")
        self.layout.addWidget(self.label)

        self.nameEdit = QtGui.QLineEdit()
        self.layout.addWidget(self.nameEdit)

        self.buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        self.saveButton = QtGui.QPushButton("Save")
        self.cancelButton = QtGui.QPushButton("Cancel")
        self.buttonBox.addButton(self.saveButton, QtGui.QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(self.cancelButton, QtGui.QDialogButtonBox.RejectRole)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)

        self.saveButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

    def getName(self):
        return self.nameEdit.text().strip()

class BatchExportToMesh(QtGui.QDockWidget):
    def __init__(self):
        if dev_mode:
            self.clear_console()

        existing_instance = Gui.getMainWindow().findChild(QtGui.QWidget, "BatchETM")
        if existing_instance:
            if dev_mode:
                self.message("Old instance closed!")
            existing_instance.close()  # close instance

        super(BatchExportToMesh, self).__init__()
        self.setWindowTitle("Batch export to mesh")
        self.setObjectName("BatchETM")
        self.setWindowIcon(QtGui.QIcon(":/icons/Mesh_SplitComponents.svg"))
        self.resize(420, 500)
        self.paramGet = App.ParamGet("User parameter:BaseApp/BatchETM")
        self.initParameters()
        self.initGui()
        # self.loadConfigurations()
        # self.updateConfigDropdown()
        self.loadActiveConfiguration()  # Cargar la configuración activa al iniciar
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        Gui.getMainWindow().addDockWidget(QtCore.Qt.RightDockWidgetArea, self)
        self.setFloating(True)
        self.topLevelChanged.connect(self.on_topLevelChanged) # resize window to defaults when undocking
        self.setFocusOnInput()

    def setFocusOnInput(self):
        self.configDropdown.setFocus()
        
    def initParameters(self):
        self.paramGet = App.ParamGet("User parameter:BaseApp/BatchETM")
        configsGroup = self.paramGet.GetGroup("Configurations")
        groupNames = configsGroup.GetGroups()  # groupNames es una lista de nombres de grupos (cadenas)
        if not groupNames:
            if dev_mode:
                self.message("Creando configuración por defecto")
            # Crear configuración por defecto
            self.createDefaultConfiguration()

        # Cargar configuraciones
        self.loadConfigurations()

    def loadConfigurations(self):
        self.configurations = []
        configsGroup = self.paramGet.GetGroup("Configurations")
        if configsGroup is None:
            # Crear el grupo 'Configurations' si no existe
            configsGroup = self.paramGet.GetGroup("Configurations")
            if dev_mode:
                self.message("Creado el grupo 'Configurations'")
        groupNames = configsGroup.GetGroups()  # Ahora groupNames es una lista de nombres de grupos (cadenas)

        if not groupNames:
            # Si no existen configuraciones, crear una configuración por defecto
            self.createDefaultConfiguration()
        else:
            for groupName in groupNames:
                configGroup = configsGroup.GetGroup(groupName)
                configName = configGroup.GetString("ConfigName")
                if not configName:
                    configName = configGroup.GetString("Name")
                self.configurations.append((groupName, configName))

            if dev_mode:
                self.message("Configuraciones cargadas: " + str(self.configurations))

    def createDefaultConfiguration(self):
        configsGroup = self.paramGet.GetGroup("Configurations")
        defaultConfig = configsGroup.GetGroup("config_1")
        defaultConfig.SetString("ConfigName", "Default")
        defaultConfig.SetString("Name", "Default")
        defaultConfig.SetFloat("SurfaceDeviation", 0.10)
        defaultConfig.SetBool("Relative", False)
        defaultConfig.SetFloat("AngularDeviation", 5.0)
        defaultConfig.SetString("FileNameOption", "Label")
        defaultConfig.SetBool("LocalCoordinates", True)
        defaultConfig.SetString("FileFormat", "Stereolithography (.STL)")
        defaultConfig.SetString("FileSavingDirectory", "./")
        # Establecer ActiveConfig solo al crear la configuración por defecto por primera vez
        self.paramGet.SetInt("ActiveConfig", 1)
        # self.configurations.append(("config_1", "Default"))
        if dev_mode:
            self.message("Creada configuración por defecto")

    def on_topLevelChanged(self, floating):
        if floating:
            self.resize(420, 500)

    def initGui(self):
        infoIcon = [
            "16 16 3 1",
            "   c None",
            "+  c #444444",
            ".  c #e6e6e6",
            "      ....      ",
            "    ........    ",
            "   .....++...   ",
            "  ......++....  ",
            " .............. ",
            " ....+++++..... ",
            " ...+++++...... ",
            ".......++.......",
            ".......++.......",
            " ......+....... ",
            " .....++....... ",
            " .....++.+..... ",
            "  ....++++....  ",
            "   ....++....   ",
            "    ........    ",
            "      ....      "
        ]

        folderIcon = [
            "16 16 3 1",
            "   c None",
            "+  c #444444",
            ".  c #e6e6e6",
            "                ",
            " .....          ",
            ".......         ",
            "........        ",
            "..............  ",
            "..............  ",
            "...             ",
            "...             ",
            "..  ............",
            "..  ............",
            ".  ............ ",
            ".  ............ ",
            "  ............  ",
            "  ............  ",
            " ............   ",
            "                "
        ]
        
        deleteIcon = [
            "16 16 3 1",
            "   c None",
            "+  c #444444",
            ".  c #e6e6e6",
            "                ",
            "                ",
            "                ",
            "                ",
            "                ",
            "                ",
            "                ",
            "  ............  ",
            "  ............  ",
            "                ",
            "                ",
            "                ",
            "                ",
            "                ",
            "                ",
            "                "
        ]
        
        addIcon = [
            "16 16 3 1",
            "   c None",
            "+  c #444444",
            ".  c #e6e6e6",
            "                ",
            "                ",
            "       ..       ",
            "       ..       ",
            "       ..       ",
            "       ..       ",
            "       ..       ",
            "  ............  ",
            "  ............  ",
            "       ..       ",
            "       ..       ",
            "       ..       ",
            "       ..       ",
            "       ..       ",
            "                ",
            "                "
        ]

        # Hide/show "to column" label and spinbox based on mode type
        def disableWidget():
            if self.d7c.isChecked():
                self.d7c.setText("Custom:")
                self.d4.show()
                self.d4.setEnabled(True)
                if len(Gui.Selection.getSelection()) == 0:
                    self.d4.setText("mesh001")
                else:
                    self.d4.setText(Gui.Selection.getSelection()[0].Label)
            else:
                self.d7c.setText("Custom")
                self.d4.setEnabled(False)
                self.d4.setText("")
                self.d4.hide()

        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.dockWidgetContents.setObjectName("dockWidgetContents")

        self.grid = QtGui.QGridLayout(self.dockWidgetContents)
        self.grid.setSpacing(10)

        iN1 = QtGui.QLabel("Surface deviation")
        iN1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.d1 = QtGui.QDoubleSpinBox()
        self.d1.setValue(0.10)
        self.d1.setSingleStep(0.01)
        self.d1.setToolTip("Maximal linear deflection of a mesh section from the surface of the object")
        self.d1.setSuffix(" mm")

        iN2 = QtGui.QLabel("Angular deviation")
        iN2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.d2 = QtGui.QDoubleSpinBox()
        self.d2.setValue(5.0)
        self.d2.setSingleStep(1.0)
        self.d2.setToolTip("Maximal angular deflection of a mesh section to the next section")
        self.d2.setSuffix(" º")

        iN3 = QtGui.QLabel("Relative")
        iN3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.d3 = QtGui.QCheckBox()
        self.d3.setToolTip("The maximal linear deviation of a mesh segment will be specified\nSurface deviation multiplied by the length of the current mesh segment (edge)")

        self.d4 = QtGui.QLineEdit()
        self.d4.setText("")  # Default value
        self.d4.setToolTip("Name without extension. For batch export multiple objects it is recommended to add '001' to the name so that the rest of files are numbered correctly.")
        self.d4.setEnabled(False)  # set initial state as disabled
        self.d4.hide()

        iN5 = QtGui.QLabel("File format")
        iN5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.d5 = QtGui.QComboBox()
        self.d5.addItem("Stereolithography (.STL)")
        self.d5.addItem("Alias mesh (.OBJ)")
        self.d5.setToolTip("File format to export")
        self.d5.setCurrentIndex(0)  # sets default option

        iN6 = QtGui.QLabel("File Saving Directory")
        iN6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.d6 = QtGui.QLineEdit()
        self.d6.setText("./")  # Default value
        self.d6.setToolTip("Use any absolute path you want or use relative ones taking in count that:\n  - start with './' for relative paths from your project directory.\n  - use '../' to exit a folder.")

        iN7 = QtGui.QLabel("File name:")
        iN7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.d7a = QtGui.QRadioButton("Label")
        self.d7a.setChecked(True)
        self.d7a.setToolTip("if selected, the .STL file will be named with the user defined name")
        self.d7a.toggled.connect(disableWidget)

        self.d7b = QtGui.QRadioButton("Project")
        self.d7b.setChecked(False)
        self.d7b.setToolTip("if selected, the .STL file will be named with the project name, that is, the FreeCAD file name")
        self.d7b.toggled.connect(disableWidget)

        self.d7c = QtGui.QRadioButton("Custom")
        self.d7c.setChecked(False)
        self.d7c.setToolTip("if selected, the .STL file will be named with a custom name set in the next field")
        self.d7c.toggled.connect(disableWidget)

        # Agrupar los botones de radio
        self.radio_group = QtGui.QButtonGroup()
        self.radio_group.addButton(self.d7a)
        self.radio_group.addButton(self.d7b)
        self.radio_group.addButton(self.d7c)

        iN8 = QtGui.QLabel("Use local coordinates")
        iN8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.d8 = QtGui.QCheckBox()
        self.d8.setChecked(True)
        self.d8.setToolTip("if TRUE the .STL origin will match with the part one. It's a very useful option when you design multipart files or assemblies")

        # Presets
        iN9 = QtGui.QLabel("Preset:")
        iN9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.configDropdown = QtGui.QComboBox()
        self.configDropdown.setToolTip("Select a saved preset to change all the macro parameters. You can save them as new presets whenever you want with the button to the left.")
        self.updateConfigDropdown()
        self.configDropdown.currentIndexChanged.connect(self.onConfigSelected)

        self.deleteConfigButton = QtGui.QPushButton() # "Delete" button
        deleteSVG = QtGui.QIcon(':/icons/list-remove.svg')
        if not deleteSVG.isNull():
            self.deleteConfigButton.setIcon(deleteSVG)
        else:
            self.deleteConfigButton.setIcon(QtGui.QIcon(QtGui.QPixmap(deleteIcon)))
        self.deleteConfigButton.setToolTip("Delete active preset.")
        self.deleteConfigButton.clicked.connect(self.onDeleteConfig)
        
        self.savePresetButton = QtGui.QPushButton() # "New..." button
        addSVG = QtGui.QIcon(':/icons/list-add.svg')
        if not addSVG.isNull():
            self.savePresetButton.setIcon(addSVG)
        else:
            self.savePresetButton.setIcon(QtGui.QIcon(QtGui.QPixmap(addIcon)))
        self.savePresetButton.setToolTip("Save parameters into a new preset.")
        self.savePresetButton.clicked.connect(self.openSavePresetDialog)

        self.SavePath = QtGui.QPushButton()
        folderSVG = QtGui.QIcon(':/icons/folder.svg')
        if not folderSVG.isNull():
            self.SavePath.setIcon(folderSVG)
        else:
            self.SavePath.setIcon(QtGui.QIcon(QtGui.QPixmap(folderIcon)))
        self.SavePath.setObjectName("save_path")
        self.SavePath.setToolTip("Sets a directory to save the converted files. By default it saves the files in the same directory as the FreeCAD project is placed")
        self.SavePath.clicked.connect(self.onSavePath)

        self.openPath = QtGui.QPushButton()
        self.openPath.setText("Open folder")
        self.openPath.setMinimumHeight(40)
        self.openPath.setObjectName("open_path")
        self.openPath.setToolTip("Opens the directory written to the left. By default it opens the folder where the FreeCAD project is placed")
        self.openPath.clicked.connect(self.onOpenPath)

        self.convertStlButton = QtGui.QPushButton()
        self.convertStlButton.setText("Convert")
        self.convertStlButton.setMinimumHeight(40)
        self.convertStlButton.setObjectName("create")
        self.convertStlButton.setToolTip("Create a new mesh from selected objects inside the FreeCAD project.")
        self.convertStlButton.clicked.connect(self.onConvertStl)

        self.saveStl = QtGui.QPushButton()
        self.saveStl.setText("Save to file")
        self.saveStl.setMinimumHeight(40)
        self.saveStl.setObjectName("save")
        self.saveStl.setToolTip("Export selected objects into a mesh file (STL or OBJ).")
        self.saveStl.clicked.connect(self.onSaveMesh)

        self.help = QtGui.QPushButton()
        infoSVG = QtGui.QIcon(':/icons/info.svg')
        if not infoSVG.isNull():
            self.help.setIcon(infoSVG)
        else:
            self.help.setIcon(QtGui.QIcon(QtGui.QPixmap(infoIcon)))
        self.help.setFixedWidth(40)
        self.help.setObjectName("help")
        self.help.setToolTip("More information aboout the macro.")
        self.help.clicked.connect(self.onInfo)

        self.noSelection = QtGui.QPushButton()
        self.noSelection.setText("No selection")
        self.noSelection.setObjectName("noSelection")
        self.noSelection.clicked.connect(self.onError)
        
        self.infoLabel = QtGui.QLabel("")
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        spacer1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        spacer2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        spacer3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)

        line_separator1 = QtGui.QFrame()
        line_separator1.setObjectName("separator")
        line_separator1.setFrameShape(QtGui.QFrame.HLine)
        line_separator1.setFrameShadow(QtGui.QFrame.Sunken)
        line_separator1.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);border: 1px solid transparent;border-bottom-color: rgba(255, 255, 255, 0.2);")
        
        line_separator2 = QtGui.QFrame()
        line_separator2.setObjectName("separator")
        line_separator2.setFrameShape(QtGui.QFrame.HLine)
        line_separator2.setFrameShadow(QtGui.QFrame.Sunken)
        line_separator2.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);border: 1px solid transparent;border-bottom-color: rgba(255, 255, 255, 0.2);")

        info = QtGui.QLabel("v" + __Version__)
        info.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        # info.setStyleSheet("color:#2e2d2d; font-style:italic;")

        line = QtGui.QLabel("")

        # addWidget(*Widget, row, column, rowspan, colspan)
        # Presets management
        self.grid.addWidget(iN9,                        1, 0, 1, 1)
        self.grid.addWidget(self.configDropdown,        1, 1, 1, 9)
        self.grid.addWidget(self.deleteConfigButton,    1, 10, 1, 1)
        self.grid.addWidget(self.savePresetButton,      1, 11, 1, 1)
        
        self.grid.addItem(spacer1,                      2, 0, 1, 12)
        self.grid.addWidget(line_separator1,            3, 0, 1, 12)
        
        # Convert
        self.grid.addWidget(iN1,                        4, 0, 1, 3)
        self.grid.addWidget(self.d1,                    4, 3, 1, 6)
        self.grid.addWidget(iN3,                        4, 9, 1, 2)
        self.grid.addWidget(self.d3,                    4, 11, 1, 1)
        self.grid.addWidget(iN2,                        5, 0, 1, 3)
        self.grid.addWidget(self.d2,                    5, 3, 1, 6)
        self.grid.addWidget(iN7,                        6, 0, 1, 3)
        self.grid.addWidget(self.d7a,                   6, 3, 1, 3)
        self.grid.addWidget(self.d7b,                   7, 3, 1, 3)
        self.grid.addWidget(self.d7c,                   8, 3, 1, 3)
        self.grid.addWidget(self.d4,                    8, 6, 1, 6)
        self.grid.addWidget(iN8,                        9, 0, 1, 3)
        self.grid.addWidget(self.d8,                    9, 3, 1, 1)
        self.grid.addWidget(self.convertStlButton,      10, 0, 1, 12)
        
        self.grid.addItem(spacer2,                      11, 0, 1, 12)
        self.grid.addWidget(line_separator2,            12, 0, 1, 12)
        
        # Save to file
        self.grid.addWidget(iN5,                        13, 0, 1, 3)
        self.grid.addWidget(self.d5,                    13, 3, 1, 9)
        self.grid.addWidget(iN6,                        14, 0, 1, 3)
        self.grid.addWidget(self.d6,                    14, 3, 1, 8)
        self.grid.addWidget(self.SavePath,              14, 11, 1, 1)
        self.grid.addWidget(self.saveStl,               15, 0, 1, 8)
        self.grid.addWidget(self.openPath,              15, 8, 1, 4)
        
        self.grid.addItem(spacer3,                      16, 0, 1, 12)
        
        # Info footer
        self.grid.addWidget(self.help,                  17, 0, 1, 1)
        self.grid.addWidget(self.infoLabel,             17, 1, 1, 10)
        self.grid.addWidget(info,                       17, 11, 1, 1)

        # Fixed label widths
        iN1.setFixedWidth(140)

        self.setWidget(self.dockWidgetContents)
        self.dockWidgetContents.setContentsMargins(0, 0, 0, 0)

        # Load the active configuration
        self.loadActiveConfiguration()

    def updateConfigDropdown(self):
        self.configDropdown.clear()
        if dev_mode:
            print("")
            print("UPDATE START")
        for groupName, configName in self.configurations:
            self.configDropdown.addItem(configName)
        # Establecer el índice seleccionado según la configuración activa
        activeConfigIndex = self.paramGet.GetInt("ActiveConfig")
        if dev_mode:
            if dev_mode:
                print("    UPDATE - ActiveConfig loaded: " + str(activeConfigIndex))
        # print("len(self.configurations): " + str(len(self.configurations)))
        if 1 <= activeConfigIndex <= len(self.configurations):
            if dev_mode:
                print("    UPDATE - Update ActiveConfig: " + str(activeConfigIndex))
            self.configDropdown.setCurrentIndex(activeConfigIndex)
        else:
            if dev_mode:
                print("    UPDATE - Reset ActiveConfig to defaults (1)")
            self.configDropdown.setCurrentIndex(1)
        
        if dev_mode:
            print("UPDATE END")


    def onConfigSelected(self, index):
        if index >= 0 and index < len(self.configurations):
            groupName, configName = self.configurations[index]  
            self.paramGet.SetInt("ActiveConfig", index + 1)  # Actualiza ActiveConfig
            self.loadConfiguration(groupName)
            if dev_mode:
                print("")
                print("SAVE CONFIG - ActiveConfig: " + str(index + 1))


    def loadActiveConfiguration(self):
        activeConfigIndex = self.paramGet.GetInt("ActiveConfig")
        if 1 <= activeConfigIndex <= len(self.configurations):
            if dev_mode:
                print("")
                print ("LOAD ACTIVE - ActiveConfig: " + str(activeConfigIndex))
            # Bloquear señales para evitar llamadas redundantes a onConfigSelected
            self.configDropdown.blockSignals(True)
            self.configDropdown.setCurrentIndex(activeConfigIndex -1)
            self.configDropdown.blockSignals(False)
            # Cargar la configuración correspondiente
            groupName, configName = self.configurations[activeConfigIndex - 1]
            self.loadConfiguration(groupName)
        else:
            # Si el índice no es válido, cargar la configuración por defecto
            self.configDropdown.blockSignals(True)
            self.configDropdown.setCurrentIndex(0)
            self.configDropdown.blockSignals(False)
            groupName, configName = self.configurations[0]
            self.loadConfiguration(groupName)



    def loadConfiguration(self, groupName):
        configsGroup = self.paramGet.GetGroup("Configurations")
        configGroup = configsGroup.GetGroup(groupName)
        # Set the parameters
        self.d1.setValue(configGroup.GetFloat("SurfaceDeviation", 0.10))
        self.d2.setValue(configGroup.GetFloat("AngularDeviation", 5.0))
        self.d3.setChecked(configGroup.GetBool("Relative", False))
        fileNameOption = configGroup.GetString("FileNameOption", "Label")
        if fileNameOption == "Label":
            self.d7a.setChecked(True)
        elif fileNameOption == "Project":
            self.d7b.setChecked(True)
        else:
            self.d7c.setChecked(True)
        self.d8.setChecked(configGroup.GetBool("LocalCoordinates", True))
        fileFormat = configGroup.GetString("FileFormat", "Stereolithography (.STL)")
        index = self.d5.findText(fileFormat)
        if index != -1:
            self.d5.setCurrentIndex(index)
        self.d6.setText(configGroup.GetString("FileSavingDirectory", "./"))

    def onSaveConfig(self, configName):
        if not configName:
            self.onError("<h2>Empty Preset Name</h2><p style='font-weight:normal;'>Please enter a name for the preset.</p>")
            return
        # Determine the next available configuration number
        configsGroup = self.paramGet.GetGroup("Configurations")
        existingConfigs = configsGroup.GetGroups()  # existingConfigs is a list of group names (strings)
        nextConfigNumber = 1
        while "config_" + str(nextConfigNumber) in existingConfigs:
            nextConfigNumber += 1
        # Save the current parameters into the new configuration
        newConfigGroup = configsGroup.GetGroup("config_" + str(nextConfigNumber))
        newConfigGroup.SetString("ConfigName", configName)
        newConfigGroup.SetString("Name", configName)
        newConfigGroup.SetFloat("SurfaceDeviation", self.d1.value())
        newConfigGroup.SetFloat("AngularDeviation", self.d2.value())
        newConfigGroup.SetBool("Relative", self.d3.isChecked())
        if self.d7a.isChecked():
            newConfigGroup.SetString("FileNameOption", "Label")
        elif self.d7b.isChecked():
            newConfigGroup.SetString("FileNameOption", "Project")
        else:
            newConfigGroup.SetString("FileNameOption", "Custom")
        newConfigGroup.SetBool("LocalCoordinates", self.d8.isChecked())
        newConfigGroup.SetString("FileFormat", self.d5.currentText())
        newConfigGroup.SetString("FileSavingDirectory", self.d6.text())
        # Update the list of configurations
        self.loadConfigurations()
        self.updateConfigDropdown()
        # Set the new configuration as active
        self.paramGet.SetInt("ActiveConfig", len(self.configurations))
        self.configDropdown.blockSignals(True)
        self.configDropdown.setCurrentIndex(len(self.configurations) - 1)
        self.configDropdown.blockSignals(False)
        groupName, configName = self.configurations[len(self.configurations) - 1]
        self.loadConfiguration(groupName)


    def onDeleteConfig(self):
        index = self.configDropdown.currentIndex()
        if index >= 0 and index < len(self.configurations):
            groupName, configName = self.configurations[index]
            if groupName == "config_1":
                self.onError("<h2>Default preset can't be deleted</h2><p style='font-weight:normal;'>Select any other preset to be deleted.</p>")
                return
            # Confirmar eliminación
            reply = QtGui.QMessageBox.question(None, 'Confirm preset removal', "<p style='font-weight:normal;'>Are you sure do you want to delete <span style='font-weight:bold'>" + str(configName) + "</span>?</p>", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                # Eliminar la configuración
                configsGroup = self.paramGet.GetGroup("Configurations")
                configsGroup.RemGroup(groupName)
                # Actualizar la lista de configuraciones
                self.loadConfigurations()
                self.updateConfigDropdown()
                # Establecer la configuración por defecto como activa
                self.paramGet.SetInt("ActiveConfig", 1)
                self.configDropdown.blockSignals(True)
                self.configDropdown.setCurrentIndex(0)
                self.configDropdown.blockSignals(False)
                groupName, configName = self.configurations[0]
                self.loadConfiguration(groupName)
            self.infoMessages("Preset removed!","positive")

    def openSavePresetDialog(self):
        dialog = SavePresetDialog(self)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            presetName = dialog.getName()
            if presetName:
                self.onSaveConfig(presetName)
                self.infoMessages("Preset saved!","positive")
            else:
                self.onError("<h2>Empty Configuration Name</h2><p style='font-weight:normal;'>Please enter a name for the configuration.</p>")

    def onInfo(self):
        msg="""<h2>Batch export to mesh</h2><p style='font-weight:normal;font-style:italic;'>version """ + __Version__ + """</p><p style='font-weight:normal;'>This macro helps Bath converting to mesh and exporting STL and OBJ files. It adds a GUI for speeding up the conversion and file saving of the selected objects</p><p>Features</p><ul><li style='font-weight:normal;'>FreeCAD "standard" meshing option</li><li style='font-weight:normal;'>custom names</li><li style='font-weight:normal;'>Converts/exports one or several objects at once</li><li style='font-weight:normal;'>Convert objects into the active FreeCAD project, a user selected folder or</li><li style='font-weight:normal;'>Export objects to .STL or .OBJ files</li><li style='font-weight:normal;'>Absolute or relative paths allowed</li><li style='font-weight:normal;'>Select local or global coordinates</li><li style='font-weight:normal;'>Creates folders if needed</li><li style='font-weight:normal;'>Opens folder in file explorer</li><li style='font-weight:normal;'>Presets loading/saving</li></ul><hr><h2>Licence</h2><p style='font-weight:normal;'>Copyright 2024 Pablo Gil Fernández</p><p style='font-weight:normal;'>This work is licensed under GNU Lesser General Public License (LGPL). To view a copy of this license, visit:</p><p style='font-weight:normal;'><a href='https://www.gnu.org/licenses/lgpl-3.0.html'>https://www.gnu.org/licenses/lgpl-3.0.html</a></p>"""
        # Create a message box
        res = QtGui.QMessageBox()
        res.setWindowTitle("Information")
        res.setText(msg)
        
        infoSVG = QtGui.QPixmap(":/icons/info.svg")
        if not infoSVG.isNull():
            res.setIconPixmap(infoSVG)
        else:
            res.setIcon(QtGui.QMessageBox.Information)  # Set a predefined icon: NoIcon, Information, Warning, Critical, Question

        # Show the message box
        res.exec_()

    # ERROR
    def onError(self, msg):
        res = QtGui.QMessageBox.warning(None,"Error",msg,QtGui.QMessageBox.Ok)

    # GET SAVING PATH
    def onSavePath(self):
        folder_path = QtGui.QFileDialog.getExistingDirectory()
        if folder_path:
            if dev_mode:
                self.message(folder_path)
            self.d6.setText(folder_path)

    # OPEN PATH IN FILE BROWSER
    def onOpenPath(self):
        if dev_mode:
            print("\nOpen directory\n===================")
        project_filename_path = FreeCAD.ActiveDocument.FileName
        project_path = os.path.dirname(project_filename_path)
        length_project_path = len(project_path)
        final_folder_path = ""
        user_path = self.d6.text()
        length_user_path = len(user_path)
        if dev_mode:
            print("\nproject_path = " + project_path)
            print("\nlength_project_path = " + str(length_project_path))
            print("\nuser_path = " + user_path)
            print("\nlength_user_path = " + str(length_user_path))
        if length_project_path == 0:
            FreeCAD.Console.PrintError("\nProject not saved!\nIt is not possible to open the file browser. Try again after saving your project somewhere.")
            self.onError("<h2>Project not saved!</h2><p style='font-weight:normal;'>It is not possible to open the file browser. Try again after saving your project somewhere.</p>")
        else:
            if length_user_path == 0:
                if dev_mode:
                    self.message("\n-- Absolute mode (user path) --")
                final_folder_path = project_path
            else:
                project_filename_path = FreeCAD.ActiveDocument.FileName
                project_path = os.path.dirname(project_filename_path)
                length_user_path = len(user_path)
                if length_user_path == 0:
                    if dev_mode:
                        self.message("\n-- Absolute mode (project path) --")
                    final_folder_path = project_path
                else:
                    if dev_mode:
                        self.message("\n-- Relative mode --")
                    joined_path = os.path.join(project_path, user_path)
                    final_folder_path = os.path.abspath(joined_path)

            if os.path.exists(final_folder_path):
                if dev_mode:
                    self.message("\nThe path exists")
                    self.message("\nfinal_folder_path: " + final_folder_path)

                    if dev_mode:
                        print("\nOpening...")
                        FreeCAD.Console.PrintMessage("\nOpening...")

                operating_system = sys.platform
                if operating_system == "darwin":
                    if dev_mode:
                        print("\nOpening macOS Finder...")
                    subprocess.run(["open", final_folder_path])

                elif operating_system == "win32":
                    if dev_mode:
                        print("\nOpening File Explorer...")
                    subprocess.run(["explorer", final_folder_path], shell=True)

                elif operating_system == "linux":
                    if dev_mode:
                        print("\nOpening Linux file explorer...")
                    subprocess.run(["xdg-open", final_folder_path])

                else:
                    FreeCAD.Console.PrintError("\nUnsupported operating system")
                    self.onError("<h2>Unsupported operating system</h2><p style='font-weight:normal;'>It is not possible to open your OS file browser.</p>")

            else:
                FreeCAD.Console.PrintError("\nThe path doesn't exist, please create it")
                self.onError("<h2>The path doesn't exist</h2><p style='font-weight:normal;'>Please create it manually.</p>")

    # CONVERT STL INTO ACTIVE FREECAD PROJECT
    def onConvertStl(self):
        if dev_mode:
            self.clear_console()
            self.message("\n****** START (convert) ********")

        # Variables
        selection = Gui.Selection.getSelection()
        surface = self.d1.value()
        angular = self.d2.value() * math.pi / 180
        if self.d3.isChecked():
            relative = True
        else:
            relative = False
        name = self.d4.text()

        if len(selection) == 0:
            if dev_mode:
                self.message("\n-- No selection --")
            FreeCAD.Console.PrintError("Export STL error: nothing selected, please, select one or several objects")
            self.onError("<h2>Nothing selected</h2><p style='font-weight:normal;'>You must select at least one object to convert or export.</p>")

        elif len(selection) == 1:
            if dev_mode:
                self.message("\n-- 1 object selected --")
            # Generate Mesh
            mesh = App.ActiveDocument.addObject("Mesh::Feature","Mesh")
            part = Gui.Selection.getSelection()[0]
            shape = part.Shape.copy(False)

            # Set part coordinates (local or global)
            if self.d8.isChecked():
                shape.Placement = App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
            else:
                shape.Placement = part.getGlobalPlacement()

            # Create mesh
            mesh.Mesh = MeshPart.meshFromShape(Shape=shape, LinearDeflection=surface, AngularDeflection=angular, Relative=relative)

            # Name mesh
            if self.d7a.isChecked():
                final_name = Gui.Selection.getSelection()[0].Label
            elif self.d7b.isChecked():
                final_name = App.ActiveDocument.Name
            else:
                final_name = name

            mesh.Label = final_name

            part.Visibility = False
            Gui.activeDocument().activeObject().DisplayMode=u"Flat Lines"
            if dev_mode:
                self.message("\n-- 1 object converted to mesh --")
            del mesh, part, shape
            
            self.infoMessages("1 object converted to mesh","positive")

        else:
            quantity = len(selection)
            if dev_mode:
                self.message("\n-- " + str(quantity) + " objects selected --")
            i = 0
            while i < quantity:
                mesh = App.ActiveDocument.addObject("Mesh::Feature","Mesh")
                part = Gui.Selection.getSelection()[i]
                shape = part.Shape.copy(False)

                # Set part coordinates (local or global)
                if self.d8.isChecked():
                    shape.Placement = App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
                else:
                    shape.Placement = part.getGlobalPlacement()

                # Create mesh
                mesh.Mesh = MeshPart.meshFromShape(Shape=shape, LinearDeflection=surface, AngularDeflection=angular, Relative=relative)

                # Name mesh
                if self.d7a.isChecked():
                    mesh.Label = Gui.Selection.getSelection()[i].Label
                elif self.d7b.isChecked():
                    mesh.Label = App.ActiveDocument.Name + "_" + str(i+1)
                else:
                    mesh.Label = name + "_" + str(i+1)

                part.Visibility = False
                Gui.activeDocument().activeObject().DisplayMode=u"Flat Lines"
                del mesh, part, shape
                i += 1
            if dev_mode:
                self.message("\n-- " + str(quantity) + " objects converted to mesh --")
            
            self.infoMessages(str(quantity) + " objects converted to mesh","positive")
            
        App.ActiveDocument.recompute()
        if dev_mode:
            self.message("\n********* END *********")
            FreeCAD.Console.PrintMessage("\nConversion done")


    # SAVE TO .STL OR .OBJ FILE
    def onSaveMesh(self):
        if dev_mode:
            self.clear_console()
            self.message("\n****** START (save) ********")

        # Variables
        selection = Gui.Selection.getSelection()
        surface = self.d1.value()
        angular = self.d2.value() * math.pi / 180
        if self.d3.isChecked():
            relative = True
        else:
            relative = False
        name = self.d4.text()
        savePath = self.d6.text()
        docPath = FreeCAD.ActiveDocument.FileName

        if docPath == "":
            if savePath[0] == ".":
                if dev_mode:
                    self.message("\n-- The project is not saved or the path doesn't correspond to an absolute one --")
                    FreeCAD.Console.PrintError("Error exporting: The project is not saved or the path doesn't correspond to an absolute one, please, save your project somewhere or add a valid absolute path under '<i>File saving directory</i>' field.")
                self.onError("<h2>Error exporting</h2><p style='font-weight:normal;'>The project is not saved or the path doesn't correspond to an absolute one, please, save your project somewhere or add a valid absolute path under '<i>File saving directory</i>' field.</p>")
                return
            if os.path.exists(savePath) and os.path.isdir(savePath):
                if dev_mode:
                    self.message("\nsavePath is valid, continuing... ")
            else:
                if dev_mode:
                    self.message("\n-- The project is not saved or the path doesn't correspond to an absolute one --")
                    FreeCAD.Console.PrintError("Error exporting: The project is not saved or the path doesn't correspond to an absolute one, please, save your project somewhere or add a valid absolute path under '<i>File saving directory</i>' field.")
                self.onError("<h2>Error exporting</h2><p style='font-weight:normal;'>The project is not saved or the path doesn't correspond to an absolute one, please, save your project somewhere or add a valid absolute path under '<i>File saving directory</i>' field.</p>")
                return

        if savePath[0] == ".":
            if dev_mode:
                self.message("\n-- Relative mode: --")
            absolutePath = os.path.dirname(docPath)
            relativePath = savePath.replace(".","",1)
            relativePath = relativePath.replace("\\","",1)
            relativePath = relativePath.replace("/","",1)
            savePath = os.path.join(absolutePath, relativePath)

        if len(selection) == 0:
            if dev_mode:
                self.message("\n-- No selection --")
                FreeCAD.Console.PrintError("Export STL error: nothing selected, please, select one or several objects")
            self.onError("<h2>Nothing selected</h2><p style='font-weight:normal;'>You must select at least one object to convert or export.</p>")
            return

        elif len(selection) == 1:
            if dev_mode:
                self.message("\n-- 1 object selected --")
            # Generate STL
            obj=[]
            part = Gui.Selection.getSelection()[0]
            shape = part.Shape.copy(False)

            # Set part coordinates (local or global)
            if self.d8.isChecked():
                shape.Placement = App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
            else:
                shape.Placement = part.getGlobalPlacement()

            # Create mesh
            mesh = MeshPart.meshFromShape(Shape=shape, LinearDeflection=surface, AngularDeflection=angular, Relative=relative)

            # Name mesh
            if self.d7a.isChecked():
                final_name = Gui.Selection.getSelection()[0].Label
            elif self.d7b.isChecked():
                final_name = App.ActiveDocument.Name
            else:
                final_name = name

            # Check if the path exists:
            if not os.path.exists(savePath):
                if dev_mode:
                    FreeCAD.Console.PrintWarning("\nThe path doesn't exist, creating it...")
                os.makedirs(savePath, exist_ok=True)
            else:
                if dev_mode:
                    print("\nThe path exist, continuing...")

            if self.d5.currentText() == "Stereolithography (.STL)":
                # export mesh to STL
                filename = os.path.join(savePath, final_name + ".stl")
                mesh.write(filename)
            if self.d5.currentText() == "Alias mesh (.OBJ)":
                # export mesh to OBJ
                filename = os.path.join(savePath, final_name + ".obj")
                obj = []
                obj.append(part)
                Mesh.export(obj, filename)

            if dev_mode:
                self.message("\n-- 1 mesh exported to file at: " + filename + " --")
            del mesh, obj, part, shape

            if dev_mode:
                FreeCAD.Console.PrintMessage("\nSaved")
        
            self.infoMessages("1 object exported to file","positive")

        else:
            quantity = len(selection)
            if dev_mode:
                self.message("\n-- " + str(quantity) + " objects selected --")
            i = 0
            namesArray = []
            labelsArray = []
            while i < quantity:
                obj=[]
                part = Gui.Selection.getSelection()[i]
                shape = part.Shape.copy(False)

                # Set part coordinates (local or global)
                if self.d8.isChecked():
                    shape.Placement = App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
                else:
                    shape.Placement = part.getGlobalPlacement()

                # Create mesh
                mesh = MeshPart.meshFromShape(Shape=shape, LinearDeflection=surface, AngularDeflection=angular, Relative=relative)

                # Name mesh
                if self.d7a.isChecked():
                    final_name = Gui.Selection.getSelection()[i].Label
                elif self.d7b.isChecked():
                    final_name = App.ActiveDocument.Name + "_" + str(i+1)
                else:
                    final_name = name + "_" + str(i+1)

                labelsArray.append(final_name)

                # Check if the path exists:
                if not os.path.exists(savePath):
                    FreeCAD.Console.PrintWarning("\nThe path doesn't exist, creating it...")
                    os.makedirs(savePath, exist_ok=True)
                else:
                    if dev_mode:
                        print("\nThe path exist, continuing...")

                if self.d5.currentText() == "Stereolithography (.STL)":
                    # export mesh to STL
                    filename = os.path.join(savePath, labelsArray[i] + ".stl")
                    mesh.write(filename)
                if self.d5.currentText() == "Alias mesh (.OBJ)":
                    # export mesh to OBJ
                    filename = os.path.join(savePath, labelsArray[i] + ".obj")
                    obj = []
                    obj.append(part)
                    Mesh.export(obj, filename)

                if dev_mode:
                    self.message("\n-- 1 mesh exported to file at: " + filename + " --")
                del mesh, obj, part, shape
                i += 1

            i = 0
            while i < quantity:
                if dev_mode:
                    self.message("\n-- " + str(labelsArray[i]) + " exported --")
                i += 1

            if dev_mode:
                FreeCAD.Console.PrintMessage("\nSaved")
            
            self.infoMessages(str(quantity) + " objects exported to file","positive")

        App.ActiveDocument.recompute()
        if dev_mode:
            self.message("\n********* END *********")

    def clear_console(self):
        #clearing previous messages
        mw=FreeCADGui.getMainWindow()
        r=mw.findChild(QtGui.QTextEdit, "Report view")
        r.clear()

    def message(self,msg):
        FreeCAD.Console.PrintMessage("BatchETM: " + str(msg) + "\n")

    def message_warning(self,msg):
        FreeCAD.Console.PrintWarning("BatchETM: " + str(msg) + "\n")

    def message_error(self,msg):
        FreeCAD.Console.PrintError("BatchETM: " + str(msg) + "\n")
        
    def infoMessages(self,msg,type):
        if type == "positive":
            self.infoLabel.setStyleSheet("color: rgb(19, 27, 2);background-color: rgba(183, 192, 165, 0.5);border-radius: 8px;") # positive
        elif type == "negative":
            self.infoLabel.setStyleSheet("color: rgb(20, 0, 0);background-color: rgba(172, 40, 40, 0.5);border-radius: 8px;") # negative
        elif type == "reset":
            self.infoLabel.setStyleSheet("color: black;background-color: rgba(0, 0, 0, 0);border-radius: 8px;") # reset
        else:
            self.infoLabel.setStyleSheet("color: rgb(0, 0, 255);background-color: rgba(183, 192, 165, 0.5);border-radius: 8px;")
        self.infoLabel.setText(str(msg))

BatchETM = BatchExportToMesh()
BatchETM.show()
BatchETM.destroyed.connect(lambda: FreeCADGui.getMainWindow().findChild(QtGui.QWidget, "BatchETM").deleteLater())
</nowiki>
}}



## Licence

Copyright 2024 Pablo Gil Fernández Ce travail est sous licence GNU Lesser General Public License (LGPL). Pour voir une copie de cette licence, visitez :
<https://www.gnu.org/licenses/lgpl-3.0.html>



---
⏵ [documentation index](../README.md) > Macro Batch Export To Mesh/fr
