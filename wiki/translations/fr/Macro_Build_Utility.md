# Macro Build Utility/fr
{{Macro/fr
|Name=Macro Build Utility
|Description=Cette macro fournit un utilitaire de compilation permettant d'assembler plusieurs fichiers projets en un seul.
|Author=Piffpoof
|Version=1.0
|Date=2015-01-21
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/8/87/Macro_Build_Utility.png ToolBar Icon]
}}

## Description

Cette macro est destinée à des projets volumineux, impliquant des centaines d\'objets. Son utilisation sur un petit projet avec un fichier unique serait inutile. Toutefois, dans le cas d'un projet volumineux comportant de nombreux objets et de nombreux fichiers à fusionner, cela fera gagner du temps, et évitera à l'utilisateur d'être impliqué dans des actions répétitives et supprimera les erreurs humaines.

## Installation

Tout le code pour buildUtility.FCMacro est dans une macro. L\'installation consiste donc à copier le code dans le répertoire Macro approprié et à appeler l\'utilitaire de génération à partir du menu Macro, de la console Python ou d\'un bouton de la barre d\'outils (méthode recommandée).

-   voir [Comment installer des macros](How_to_install_macros/fr.md) pour des informations sur la façon d\'installer ce code de macro
-   voir [Personnaliser les barres d\'outils](Customize_Toolbars/fr.md) pour plus d\'informations sur l\'installation en tant que bouton dans une barre d\'outils

## Usage

L\'utilitaire de construction fonctionne sur les mêmes principes que les fichiers de construction utilisés pour assembler des systèmes logiciels volumineux (comme FreeCAD). Un éditeur de texte est utilisé pour créer un fichier texte qui respecte les formats requis par l\'utilitaire de génération. L\'utilitaire de construction lit ensuite chaque ligne du fichier texte et exécute les actions spécifiées par ce fichier texte.

La macro demande à l\'utilisateur un \"fichier de construction\". Il analyse ensuite le fichier de construction, il existe 3 types de lignes:

-   lignes commençant par le caractère de commentaire \"#\", qui sont ignorées en tant que commentaires ou remarques
-   lignes commençant par le caractère de sous-fichier \"@\" qui sont ignorées
     Remarque : le caractère \"@\" est destiné à une amélioration future lorsque les fichiers de construction inférieurs seront gérés.
-   toutes les autres lignes pouvant être un fichier de projet ou un sous-répertoire

L\'extension de fichier pour le fichier Build Utility est \".FCBld\". Ceci afin que les fichiers ne soient pas mélangés avec d\'autres utilisations et applications.

Tout fichier spécifié dans le fichier de construction est supposé avoir l\'extension \".FCStd\" Si la ligne commence par un répertoire, le fichier de projet est lu à partir de ce sous-dossier. Sinon, on suppose que la ligne spécifie un fichier de projet. Les répertoires au sein des répertoires sont pris en charge, ce qui permet d\'imbriquer des profondeurs arbitraires. Le format de spécification de fichier est le style \"Unix\" avec différents niveaux séparés par la barre oblique \"/\".

Tout fichier manquant est imprimé sur la vue Rapport. Tout répertoire manquant est imprimé sur la vue Rapport.

Un nouveau document est créé et chaque projet est un \"Projet fusionné\" dans ce nouveau document vide. Une fois terminé le document n\'est pas enregistré, libre à l\'utilisateur de le sauvegarder s\'il le souhaite. Si le fichier n\'existe pas, le nom du fichier est Imprimé dans la vue Rapport.

## Interface utilisateur 

Il n\'y a pas vraiment d\'interface graphique pour cette macro. La macro lit un fichier texte qui a été préparé avec un éditeur de texte et génère un modèle dans un document de sortie. En dehors du fait de cliquer sur le bouton de la barre d'outils pour lancer le processus, il n'y a pas d'interaction de la part de l'utilisateur.

## Options

Il n\'y a pas d\'interface graphique, donc il n\'y a pas d\'options. Les seules alternatives qui existent consistent à utiliser les 3 types de lignes du fichier texte, comme décrit ci-dessus.

## Remarques

Pour réitérer ce qui a été dit au début, cette macro n'est pas utile sur un fichier unique. Mais pour les personnes qui modélisent un avion, une locomotive, un navire, un bâtiment, une installation physique ou un circuit complexe, il existe un avantage et un avantage définitifs. En choisissant l\'extension de fichier \".FCBld\", on espère pouvoir définir une norme de tri pour les fichiers de construction dans FreeCAD. En réservant le caractère de préfixe \"@\" dans la définition du fichier de commande, on espère pouvoir en tenir compte pour une utilisation future et (si nécessaire) pour la croissance.

## Liens

none (so far)

## Script

ToolBar Icon ![](images/Macro_Build_Utility.png )

**Macro_Build_Utility.FCMacro**


{{MacroCode|code=
#
#                       Build Utility
#                       v 0.0 - build from files and files in sub-folders
#
#***********************************************************************************
# routine to read in a build file and merge all specified projects
"""
This function asks the user for a "build file". It then parses that build file, there
are 3 legal line types:
- lines starting with the comment character "#" which are ignored
- lines starting with the subfile character "@" which are ignored
    Note:   the "@" character is for future enhancement when sub-build files 
            will be handled
- all other lines which may be a project file or a subfolder (sub-directory)
If the line is a subfolder then the project file is read from that subfolder.
Otherwise it is assumed the line specifies a project file.
A new document is created and each project is "Project Merged" into that new and empty document.
The document is not saved at the end, this is left for the user if desired.
If the file does not exist then the file name is Printed to the Report view
"""
"""
Example file:
#this is a sample build file
#==============================
@sub-build-files - not presently inplemented
# first the top-level file
metal
# now some misc files
./black/black
./blue/blue
# file does not exist
zebra 
# folder does not exist
/bear/bear
# multiple files in one sub-folder
./engineering/green
./engineering/grey
#multiple files in hierarchical folders
./externalModules/white
./externalModules/red/red
#./externalModules/red/stackerAssembly - commented out as not currently loading
./externalModules/red/orange
./externalModules/red/level3/yellow
"""
# import statements
import FreeCAD
import os.path
from PySide import QtGui

# UI Class definitions

# Class definitions

# Function definitionss

# Constant definitions
buildTargetDocument = "build_target"
commentTag = "#"
subfileTag = "@"
lineFeed = "\n"
subfolder = "./"
carriageReturn = "\r"
fileSeparator = "/"
fcFileExtension      = ".FCStd"
fcFileExtensionUC  = ".FCSTD"
fcFileExtensionLen = -6

# code ***********************************************************************************
buildFilePathName=QtGui.QFileDialog.getOpenFileName()[0]
if len(buildFilePathName) > 0:
    # set up a new empty "build_target" document
    FreeCAD.newDocument(buildTargetDocument)
    FreeCAD.setActiveDocument(buildTargetDocument)
    FreeCAD.ActiveDocument=FreeCAD.getDocument(buildTargetDocument)
    guiDoc=FreeCADGui.ActiveDocument
    #
    lastFileSeparator = buildFilePathName.rindex(fileSeparator)
    buildFilePath = buildFilePathName[: lastFileSeparator]
    buildFileName = buildFilePathName[lastFileSeparator +1:]
    #
    buildFileContents = open(buildFilePathName,"r")
    buildFileLines = buildFileContents.readlines()
    buildFileContents.close()
    #
    for line in buildFileLines:
        if line[0] == commentTag:
            # line of internal comment
            pass
        elif line[0] == subfileTag:
            # line of sub-build-file (not presently implemented)
            pass
        else:
            # a line which should specify a FreeCAD project file
            # - may be preceded by a sub-directory e.g. "./subdir309/"
            # - project file may be missing file extension
            #
            # if line break at end of file spec then remove
            if line[-1:] == lineFeed:
                line = line[:-1]
            if line[-1:] == carriageReturn:
                line = line[:-1]
            # if no FreeCAD project file extension supplied then append one
            # make an uppercase comparison in case of mixed case
            tempLine = fcFileExtension + line.upper()
            if fcFileExtensionUC != tempLine[fcFileExtensionLen:]:
                line = line + fcFileExtension
            # if there is a leading subdirectory then remove "./" from beginning
            if subfolder[0:2] == line[0:2]:
                line = line[2:]
            projectFileSpec = str(buildFilePath) + str("/") + str(line)
            if os.path.exists(projectFileSpec):
                guiDoc.mergeProject(projectFileSpec)
            else:
                FreeCAD.Console.PrintMessage('project file "' + projectFileSpec + '" not found' + "\n")

    # set view back to "build_target", it is up to user to save it (if they want)
    FreeCAD.setActiveDocument(buildTargetDocument)
    FreeCAD.ActiveDocument=FreeCAD.getDocument(buildTargetDocument)
    FreeCADGui.ActiveDocument=FreeCADGui.getDocument(buildTargetDocument)
    FreeCADGui.SendMsgToActiveView("ViewFit")
    FreeCADGui.activeDocument().activeView().viewAxometric()
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
}}

## Exemple

Vous travaillez avec d\'autres services de votre entreprise pour utiliser FreeCAD afin de générer un grand modèle de CAO pour un client externe. Pour préparer la présentation à venir, vous devez intégrer les modèles représentés dans les sous-systèmes \"noir\" et \"bleu\". Le service d\'ingénierie est responsable des sous-systèmes \"vert\" et \"gris\" et vous disposez vous-même du sous-système \"métal\" sur votre ordinateur. Le client utilise également FreeCAD et votre conception doit intégrer leurs sous-systèmes \"rouge\" et \"jaune\". Le client externe vous a dit que l'empileur n'est pas prêt à être utilisé. Vous devez donc le commenter dans votre fichier de construction.

Il y a beaucoup de chemins de dossiers à taper afin que vous puissiez entrer les commandes dans le fichier texte de Build Utility, ce qui signifie que vous pouvez l\'exécuter en un simple clic sur un bouton de la barre d\'outils.

<img alt="" src=images/MacroBuildUtilityTreeDiagram.jpg  style="width:500px;">

Le contenu du fichier de construction \"buildFile.FCBld\" présenté ci-dessous montre la structure de fichier du projet décrit ci-dessus.


```python
#this is the build file for the complete assembly
#==============================
@sub-build-files - not presently implemented
# first the top-level file
metal
# now some misc files
./black/black
./blue/blue
# file does not exist
zebra 
# folder does not exist
/bear/bear
# multiple files in one sub-folder
./engineering/green
./engineering/grey
#multiple files in hierarchical folders
./externalModules/white
./externalModules/red/red
#./externalModules/red/stackerAssembly - commented out as not currently loading
./externalModules/red/orange
./externalModules/red/level3/yellow
```

Un résumé du fichier et de la façon dont il est traité est:

-   les deux premières lignes sont traitées comme des commentaires et tout ce qui suit le caractère initial du signe dièse est ignoré


```python
#this is the build file for the complete assembly
#==============================
```

-   la troisième ligne est également ignorée car son premier caractère est le caractère esperluette qui est réservé pour une utilisation future, où les fichiers de commande peuvent appeler d\'autres fichiers de recommandation.


```python
@sub-build-files - not presently implemented
```

-   la cinquième ligne est la première spécification de fichier, le fichier est dans le même répertoire que le fichier de construction, pas dans un sous-répertoire


```python
metal```

-   les septième et huitième lignes sont les deux spécifications de fichier où le fichier est dans un sous-répertoire, notez que le sous-répertoire est de la forme \"./black/\" où \"noir\" est le nom du répertoire, donc un fichier appelé \"sheetFold.FCstd\" dans le répertoire \"outsourcing\" apparaîtrait \"./outsourcing/sheetFold\"


```python
./black/black
./blue/blue```

-   la dix-neuvième ligne montre une spécification de fichier qui existe mais qui n\'est pas incluse dans cette opération de construction


```python
#./externalModules/red/stackerAssembly - commented out as not currently loading```

-   les deux dernières lignes montrent les spécifications du fichier et où le fichier se trouve dans plus d\'un niveau de sous-répertoire


```python
./externalModules/red/orange
./externalModules/red/level3/yellow
```



---
⏵ [documentation index](../README.md) > Macro Build Utility/fr
