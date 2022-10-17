# Macro TreeToAscii/fr
{{Macro
|Name=TreeToAscii
|Description=Cette macro génère une représentation graphique ASCII de l'arbre du ou des objets sélectionnés.
|Author=OpenBrain
|Date=2020-03-23
|Version=0.6
|FCVersion=0.17+
}}

## Description

### Contexte

Cette macro a été écrite dans le but principal de documenter la construction du modèle. Elle génère une représentation graphique ASCII de l\'arbre de construction d\'objet(s) sélectionné(s).

### Utilisation

Sélectionnez simplement le ou les objets dont vous souhaitez imprimer l\'arborescence et exécutez la macro. Il affichera l\'arborescence de chaque objet dans une boîte de dialogue. Tous les objets sélectionnés seront considérés comme étant au même niveau de hiérarchie en haut de l\'arborescence (même s\'ils ne sont pas dans le modèle réel). Une fois la boîte de dialogue ouverte, vous pouvez changer de style et/ou de motif et recréer l\'arborescence ASCII.

![](images/FCTree2Ascii.png )

Plusieurs styles sont fournis, pour l\'instant principalement pour prendre en charge les systèmes qui peuvent rencontrer des problèmes avec le codage Unicode   *

-   ***Modern***    * (par défaut) utilise des caractères Unicode pour afficher les fourches et les branches
-   ***Baroque***    * un autre style Unicode avec une plus grande indentation
-   ***ASCII***    * représentation ASCII pure des fourches et branches

La création de votre propre style ne devrait pas être trop difficile en modifiant la macro et en changeant/ajoutant un style à la variable \'STYLES\'. Le choix du style sélectionné est enregistré dans les paramètres FreeCAD.

Le motif de ligne peut être personnalisé. Il prend en charge différentes métadonnées définies   *

-   ***{LBL}***    * étiquette d\'objet (étiquette affichée)
-   ***{NAM}***    * nom d\'objet (nom interne) par ex. \'Box001\'
-   ***{SNAM}***    * objet ShortName (sans chiffres) par exemple. \'Box001\' sera affiché comme \'Box\'
-   ***{TYP}***    * Type d\'objet par exemple. \'Part   *   *MultiFuse\'
-   ***{BTYP}***    * objet BaseType par exemple. \'Part   *   *MultiFuse\' sera affiché comme \'Part\'
-   ***{STYP}***    * objet ShortType (sans base) par ex. \'Part   *   *MultiFuse\' sera affiché comme \'MultiFuse\'

Le modèle par défaut est \'{LBL} ({SNAM})\', ce qui signifie par exemple. l\'objet \'Box001\' étiqueté \'myCube\' sera affiché comme \'myCube (Box001)\'. Notez que pratiquement tous les caractères sont autorisés. Si vous souhaitez imprimer des accolades, vous devez les doubler. Par exemple. avec le même objet d\'exemple, le modèle \'{LBL} (SNAME) {{{TYP}}} =\>\' affichera \'myCube (Box) {Part   *   *Box} =\>\'. Les métadonnées disponibles sont disponibles dans l\'info-bulle du champ d\'édition de motif, vous n\'avez donc pas besoin de vous en souvenir. Le motif de ligne est enregistré dans les paramètres FreeCAD.

Une fois la boîte de dialogue ouverte, plusieurs actions sont disponibles   *

-   ***Copy to clipboard***    * copie tout l\'arbre dans votre presse-papiers
-   ***Save to file***    * enregistre l\'arborescence entière dans un fichier arbitraire sur votre système
-   ***Embed in text file***    * stocke l\'arborescence entière dans un fichier texte incorporé dans le document (disponible depuis FC 0.18.4)
-   Bien sûr, vous pouvez copier n\'importe quelle partie de l\'arborescence en la sélectionnant et en utilisant les commandes de copie standard

### Installation

La macro est disponible via le [gestionnaire d\'extensions](Std_AddonMgr/fr.md). Le code est fourni sur cette page pour plus de commodité au cas où votre système n\'ait pas git-python. Bien qu\'elle devrait être à jour, la dernière version de la macro est toujours disponible sur [FreeCAD-macro repository](https   *//github.com/FreeCAD/FreeCAD-macros/blob/master/Information/TreeToAscii.FCMacro)

Pour des explications plus détaillées, consultez la page [Comment installer les macros](How_to_install_macros/fr.md).

## Script

### Discussion du forum 

Pour tout commentaire (bug, demande de fonctionnalité, commentaires\...), merci d\'utiliser ce fil de discussion   * <https   *//forum.freecadweb.org/viewtopic.php?f=22&t=43504>

### Code

**Macro_FCTree2Ascii.FCMacro**


{{MacroCode|code=
<nowiki>
#!/usr/bin/python
#####################################
# Copyright (c) openBrain 2020
# Licensed under LGPL v2
#
# This FreeCAD macro prints the Tree of selected object(s) as ASCII art.
# Several styles are available. Tree branch pattern is customizable.
# It can export to clipboard, file or embedded text document.
# This mainly aims at documenting the model.
#
# Version history    *
# *0.6    * introduce last fork string definition, add new style
# *0.5    * beta release
#
#####################################

# -*- coding   * utf-8 -*-

__Name__ = 'TreeToAscii'
__Comment__ = 'Prints the Tree of selected object(s) as ASCII art'
__Author__ = 'openBrain'
__Version__ = '0.6'
__Date__ = '2020-03-23'
__License__ = 'LGPL v2'
__Web__ = 'https   *//www.freecadweb.org/wiki/Macro_TreeToAscii'
__Wiki__ = 'https   *//www.freecadweb.org/wiki/Macro_TreeToAscii'
__Icon__ = ''
__Help__ = 'Select object(s) you want to print the tree then run'
__Status__ = 'Beta'
__Requires__ = 'FreeCAD >= 0.17'
__Communication__ = 'https   *//forum.freecadweb.org/viewtopic.php?f=22&t=43504'

import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtGui, QtCore  # Special FreeCAD's PySide, which may be PySide2!

PREF_PATH = 'User parameter   *BaseApp/Preferences/Mod/TreeToAscii'
PREF_PATTERN = 'TreePattern'
PREF_STYLE = 'TreeStyle'
STYLES = {  # defines styles as NAME    * [ branch str, fork str, opt   *last fork str]
    'Modern'    * [' │ ', ' ├ ', ' └ '],  # Unicode U+251C, Unicode U+2502
    'Baroque'    * [' │  ', ' ├─ ',  ' └─ '],
    'ASCII'    * [' | ', ' \\_']
    }
DEF_PATTERN = '{LBL} ({SNAM})'
DEF_STYLE = list(STYLES.keys())[0]

g_ascii_tree=""

def printChildren(objs=None, level=0, baseline='')   *
    """Build ASCII tree by recursive call"""
    global g_ascii_tree
    for cnt, obj in enumerate(objs,1)   *
        data = {
            "LBL"    * obj.Label,
            "NAM"    * obj.Name,
            "SNAM"    * "".join(filter(str.isalpha, obj.Name)),
            "TYP"    * obj.TypeId,
            "BTYP"    * obj.TypeId.partition('   *   *')[0],
            "STYP"    * obj.TypeId.rpartition('   *   *')[-1]
        }
        branch_str = STYLES[gen_style.currentText()][0]
        fork_str = STYLES[gen_style.currentText()][1]
        last_fork_str = STYLES[gen_style.currentText()][-1]
        if cnt == len(objs)   *
            g_ascii_tree += baseline + last_fork_str
        else   *
            g_ascii_tree += baseline + fork_str
        try   *
            g_ascii_tree += gen_pattern.text().format(**data)
        except (ValueError, IndexError, KeyError)   *
            g_ascii_tree = 'Error in generating pattern'
            return
        g_ascii_tree += '\n'
        if cnt == len(objs)   *
            baselinechi = baseline + ' '*len(branch_str)
        else   *
            baselinechi = baseline + branch_str
        printChildren(obj.ViewObject.claimChildren(), level + 1, baselinechi)

def copyToClip()   *
    """Copies ASCII tree to clipboard"""
    tree_view.selectAll()
    tree_view.copy()
    tree_view.setPlainText("Copied to clipboard")
    QtCore.QTimer.singleShot(3000, lambda   *tree_view.setPlainText(g_ascii_tree))

def saveToFile()   *
    """Saves ASCII tree to user system file"""
    _path = QtGui.QFileDialog.getSaveFileName()
    if _path[0]   *
        save_file = QtCore.QFile(_path[0])
        if save_file.open(QtCore.QFile.ReadWrite)   *
            save_fileContent = QtCore.QTextStream(save_file)
            save_fileContent << g_ascii_tree
            save_file.flush()
            save_file.close()
            tree_view.setPlainText("Saved to file    * " + _path[0])
        else   *
            tree_view.setPlainText("ERROR    * Can't open file    * " + _path[0])
        QtCore.QTimer.singleShot(3000, lambda   *tree_view.setPlainText(g_ascii_tree))

def embedToText()   *
    """Stores ASCII tree into an embedded document"""
    text_doc = None
    try   *
        text_doc = App.ActiveDocument.addObject("App   *   *TextDocument","ModelTree")
    except   *
        tree_view.setPlainText("ERROR    * can't create Text document. Maybe your version is too old")
    if text_doc   *
        text_doc.Text = g_ascii_tree
        tree_view.setPlainText("Embedded to text document    * " + text_doc.Label)
    QtCore.QTimer.singleShot(3000, lambda   *tree_view.setPlainText(g_ascii_tree))

def updateTxt()   *
    """Updates ASCII tree"""
    global g_ascii_tree
    g_ascii_tree=""
    printChildren(Gui.Selection.getSelection())
    tree_view.setPlainText(g_ascii_tree)


def onGenerate()   *
    """Called when updating ASCII tree"""
    p.SetString(PREF_PATTERN, gen_pattern.text())
    p.SetString(PREF_STYLE, gen_style.currentText())
    updateTxt()

# Get saved parameters or use defaults.
p = App.ParamGet(PREF_PATH)
g_name_pattern = p.GetString(PREF_PATTERN, DEF_PATTERN)
g_tree_style = p.GetString(PREF_STYLE, DEF_STYLE)
if g_tree_style not in STYLES   *
    g_tree_style = DEF_STYLE

# Build UI and show
dlg = QtGui.QDialog(Gui.getMainWindow(), QtCore.Qt.Tool)
dlg_layout = QtGui.QVBoxLayout(dlg)
gen_layout = QtGui.QHBoxLayout()
gen_pattern = QtGui.QLineEdit(g_name_pattern, dlg)
gen_pattern.setToolTip("""Defined variables are    *
    {LBL}    * object Label
    {NAM}    * object Name
    {SNAM}    * object ShortName (without digits)
    {TYP}    * object Type
    {BTYP}    * object BaseType
    {STYP}    * object ShortType (without base)
If you need to print curly braces, they have to be doubled""")
gen_run = QtGui.QPushButton("Generate",dlg)
gen_run.clicked.connect(onGenerate)
gen_style = QtGui.QComboBox(dlg)
gen_style.addItems(list(STYLES.keys()))
gen_style.setCurrentIndex(list(STYLES.keys()).index(g_tree_style))
gen_layout.addWidget(QtGui.QLabel("Generating pattern   * "))
gen_layout.addWidget(gen_pattern)
gen_layout.addWidget(QtGui.QLabel("Style    * "))
gen_layout.addWidget(gen_style)
gen_layout.addWidget(gen_run)
tree_view = QtGui.QPlainTextEdit(g_ascii_tree)
tree_view.setReadOnly(True)
tree_view.setMinimumWidth(Gui.getMainWindow().width()/2)
tree_view.setMinimumHeight(Gui.getMainWindow().height()/2)
tree_view.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
button_box = QtGui.QDialogButtonBox()
copy_clip_but = QtGui.QPushButton("Copy to clipboard", button_box)
button_box.addButton(copy_clip_but, QtGui.QDialogButtonBox.ActionRole)
copy_clip_but.clicked.connect(copyToClip)
_but = QtGui.QPushButton("Save to file", button_box)
button_box.addButton(_but, QtGui.QDialogButtonBox.ActionRole)
_but.clicked.connect(saveToFile)
store_embed_but = QtGui.QPushButton("Embed in a text file", button_box)
button_box.addButton(store_embed_but, QtGui.QDialogButtonBox.ActionRole)
store_embed_but.clicked.connect(embedToText)
close_dlg_but = QtGui.QPushButton("Close", button_box)
button_box.addButton(close_dlg_but, QtGui.QDialogButtonBox.RejectRole)
button_box.rejected.connect(dlg.reject)
dlg_layout.insertLayout(0,gen_layout)
dlg_layout.addWidget(tree_view)
dlg_layout.addWidget(button_box)
updateTxt()
dlg.exec_()
</nowiki>
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro TreeToAscii/fr
