# Macro TemplateHelper
{{Macro
|Name=Macro TemplateHelper
|Description=This macro generates a template to use with the TechDraw workbench and adds a new page with a new template object to the active dokument, ready to place views on it. And it can supply a bill of material (BOM), if wanted.
|Author=FBXL5
|Date=2021-06-25
|Version=00.01
}}

## Description

If you are tired of retyping information whenever you inserted another page into your active FreeCAD file or if you prefer a \"drawn\" bill of material (BOM) over an inserted spread sheet this macro is for you.

This macro generates a TechDraw template on the fly and inserts it into the active document, ready to get new views added.

If you wish, you can fill the space between the title block and the upper border of the drawing area with a BOM. You choose how many lines you need or if you fill the whole space.

 <img alt="" src=images/Macro_TemplateHelper_A3+BOM.png  style="width   *480px;">  
*Page with macro generated template, ISO A3 + bill of material*

## Usage

1.  Open a FreeCAD file or add a new one.
2.  Find the macro file in your macro directory using <img alt="" src=images/Std_DlgMacroExecute.svg  style="width   *16px;"> [Macros\...](Std_DlgMacroExecute.md) and select it.

       *   (The Script section below describes how to put it there.)
3.  Press **Execute** to start the macro.
4.  Select page format.
5.  Select language for the title block.
6.  If you need a BOM change the number of rows.

   *   

       *   You can use the right mouse button to reset to 0 or
       *   to set the maximum number of rows that fit on your chosen page size.

   *   Finally   * Click **OK** to continue.

## Dialogue window 

 <img alt="" src=images/Macro_TemplateHelper_DiaWin.png  style="width   *240px;">  
*Dialogue window on launch*

 <img alt="" src=images/Macro_TemplateHelper_DiaLang.png  style="width   *240px;">  
*Language options*

English is default and just one version, but maybe someone likes to distinguish \'merican and bri\'ish English in the future\...    *-D

 <img alt="" src=images/Macro_TemplateHelper_DiaSize.png  style="width   *240px;">  
*Format options*

 <img alt="" src=images/Macro_TemplateHelper_DiaBOM.png  style="width   *240px;">  
*BOM options*

## Script

The Macro should be found in the macro directory. To put it there, you need to   *

1.  Select the macro below (from **\#! pyth\...** to **\...main()**).
2.  Copy the selection.
3.  Create a new macro file using <img alt="" src=images/Std_DlgMacroExecute.svg  style="width   *16px;"> [Macros\...](Std_DlgMacroExecute.md) and select **Create**.
4.  Type in the name (TemplateHelper) and select **OK**. (*.FCMacro* is added automatically.)
5.  Paste the clipboard content into the Editor window.
6.  Press <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width   *16px;"> [Execute macro](Std_DlgMacroExecuteDirect.md) to start the macro.




<div class="mw-collapsible mw-collapsed toccolours">

**TemplateHelper.FCMacro**


<div class="mw-collapsible-content">


{{MacroCode|code=
#! python
# -*- coding   * utf-8 -*-
# (c) 2021 <FBXL5>, LGPL
# Thanks to WRS for some very helpful suggestions.
"""
This script generates or overwrites a TechDraw Template file (MyTemplate.svg)
and then adds it to the active FreeCAD document.

GUI section   *
1. It reads the Language parameter from the preferences to customise the
   user interface (DE and EN are finished and I tried my best with IT and FR)
2. It checks if you have assigned a template directory in your TechDraw preferences yet!
3. It checks if a FreeCAD file is opened.
   If either is False nothing will be generated.
4. You can choose a language for the title block labelling (fix texts).
   (DE, EN, IT, FR available)
5. You can choose one from several drawing formats.
   (ISO is finished but ANSI and Arch formats need tweaking)
6. If you need a bill of material you can enter the needed number of rows (lines).
   Right mouse action lets you reset the value to (default) 0 or to the maximum
   of rows which was set when the format was chosen.
7. You can choose to cancel or to execute the creation.

Template creation   *
8. A template file (MyTemplate.svg) will be generated and
   saved into your template directory. (You can use it like any other template
   or save it for later reuse until it is overwritten by the next macro run)

Insertion sction   *
9.  It adds new page object and a new temlate object to the active FreeCAD file.
10. "MyTemplate.svg" is loaded into the templated object.
11. Some editable texts are altered depending on allready existing pages   *
    On all first page   *
    - author's name
    - date of creation (current date)
    - format
    On any but the first page these are copied from the first page to the current   *
    - Owner's details
    - Copyright info
    - Title and part number
    - CAD version
    and the total number of sheets is updated on all Pages
In contrast to manually inserted pages and templates these pages and templates
are numbered with only 2 digits and afterwards their labels are changed
from page to Blatt/Sheet/Feuille/Pagina + the two digit number.

Some entries could be handled by follow-up macros now.

!!! It is strongly recommended to save,close and reopen
    the active document before adding another page,
    especially with another format.
    The previously generated editable texts will slip to the
!!! current positions of the newly generated ones

I have tried to follow this naming rule   *
 class names   *    CamelCase
 function names   * mixedCase
 constant names   * ALL_CAPITAL + underscore
 variable names   * lower_case + underscore
"""

__Name__= "Template Helper"
__Comment__ = "Template generator, Page adder, BOM provider"
__Author__ = "FBXL5"
__Version__ = "00.01.00"
__Date__    = "2021-06-20"
__License__ = "LGPL-2.0-or-later as FreeCAD"
__Web__ = ""
__Wiki__ = "http   *//www.freecadweb.org/wiki/index.php?title=Macro_TemplateHelper"
__Icon__  = ""
__IconW__  = ""
__Help__ = "Start the macro and see what happens"
__Status__ = "Alpha"
__Requires__ = "FreeCAD >= 0.19 + Python3 "
__Communication__ = "http   *//www.freecadweb.org/wiki/index.php?title=User   * FBXL5"
__Files__ = ""

# imports and constants
import time, os     # built-in modules
from PySide2.QtWidgets import (QDialog, QPushButton, QLabel, QComboBox,
                               QLineEdit, QAction, QDoubleSpinBox)

# - SVG creation -

class ToteBag   *
    pass
# This class is empty to act as a container for several variables

borders = ToteBag()      #- one bag for drawing border offsets
sheet_format = ToteBag() #- one bag for page dimensions
title_block = ToteBag()  #- one bag for title block static texts
bom_list = ToteBag()     #- one bag for bill of material
owner_data = ToteBag()   #- one bag for owner's data and copyright info

class InputWindow(QDialog)   *
    """
    docstring for InputWindow.
    """
    def __init__(self)   *
        super(InputWindow, self).__init__()
        self.initUI()

    def initUI(self)   *
        # set some defaut values
        #- Get the path to the template folder that is set in the FreeCAD parameters
        parameter_path = FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/Mod/TechDraw/Files")
        template_path = parameter_path.GetString("TemplateDir")
        template_name = "MyTemplate.svg"
        #- Link template_path and template_name for any OS
        self.template_file = os.path.join(template_path, template_name)

        parameter_path = FreeCAD.ParamGet("User parameter   *BaseApp/Preferences/General")
        app_language = parameter_path.GetString("Language")
        self.setWindowTexts(app_language)

        self.result = "Cancelled" # Default return status
        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(350)
        self.setWindowTitle(self.text_window)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        if template_path == ""   *
            # create some labels
            self.text_template_directory = ("" +
            "You haven't assigned a template directory \n" +
            "in your TechDraw preferences yet! \n\n" +
            "Have a look at   * \n Preferenes \n - TechDraw \n - " +
            "General \n - Template Directory")
            self.label_format = QLabel(self.text_template_directory, self)
            self.label_format.setStyleSheet("""
                background-color   * #f0ddbb;
                font-size   * 14px;
                """)
            #- OK button
            self.ok_button = QPushButton(self.text_ok, self)
            self.ok_button.clicked.connect(self.onCancel)
            self.ok_button.move(200, 300)

        elif FreeCAD.activeDocument() == None   *
            # create some labels
            self.text_template_directory = ("" +
            "No active FreeCAD file found! \n\n" +
            "Open a FreeCAD file before \n" +
            "launching this macro. \n")
            self.label_format = QLabel(self.text_template_directory, self)
            self.label_format.setStyleSheet("""
                background-color   * #f0ddbb;
                font-size   * 22px;
                """)
            #- OK button
            self.ok_button = QPushButton(self.text_ok, self)
            self.ok_button.clicked.connect(self.onCancel)
            self.ok_button.move(200, 300)

        else   *
            # create some labels
            self.label_format = QLabel(self.text_format, self)
            self.label_format.move(20, 90)
            self.label_language = QLabel(self.text_language, self)
            self.label_language.move(20, 20)
            self.label_BOM_rows = QLabel(self.text_bom, self)
            self.label_BOM_rows.move(20, 160)
            self.label_warning = QLabel(self.text_warning, self)
            self.label_warning.move(20, 260)
            # set up lists for pop-ups
            self.format_list = ("ISO A0","ISO A1","ISO A2","ISO A3","ISO A4",\
                "ANSI A","ANSI B","ANSI C","ANSI D","ANSI E",\
                "Arch A","Arch B","Arch C","Arch D","Arch E","Arch E1")
            self.language_list = ("DE","FR","IT","UK","US")
            # create some result containers and set default values
            self.result_format   = "ISO A4"
            self.result_language = "UK"
            # create some input elements
            #- set up pop-up menu - ComboBox - Format
            self.popup_format = QComboBox(self)
            self.popup_format.setToolTip(self.tooltip_format)
            self.popup_format.move(200, 100)
            self.popup_format.addItems(self.format_list)
            self.popup_format.setCurrentIndex(self.format_list.index("ISO A4"))
            self.popup_format.activated[str].connect(self.onPopupFormat)
            #- set up pop-up menu - ComboBox - Language
            self.popup_language = QComboBox(self)
            self.popup_language.setToolTip(self.tooltip_language)
            self.popup_language.move(200, 20)
            self.popup_language.addItems(self.language_list)
            self.popup_language.setCurrentIndex(self.language_list.index("UK"))
            self.popup_language.activated[str].connect(self.onPopupLanguage)
            # set up text input field - Number of BOM rows
            self.input_BOM_rows = QDoubleSpinBox(self)
            self.input_BOM_rows.setToolTip(self.tooltip_bom)
            self.input_BOM_rows.setMinimum(0)
            self.input_BOM_rows.setMaximum(34) # default value for ISO A4
            self.input_BOM_rows.setDecimals(0) # no decimals
            self.input_BOM_rows.setValue(0)    # no BOM as default
            self.input_BOM_rows.move(200, 180)
            self.input_BOM_rows.setFixedWidth(60)
            # set contextual menu options for text editing widget
            # reset text field to default
            self.BOM_action1 = QAction(self)
            self.BOM_action1.setText(self.text_none)
            self.BOM_action1.triggered.connect(self.onBOMAction1)
            # set tex maximum
            self.BOM_action2 = QAction(self)
            self.BOM_action2.setText(self.text_maximum)
            self.BOM_action2.triggered.connect(self.onBOMAction2)
            # define RMB-menu and add options
            self.input_BOM_rows.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
            self.input_BOM_rows.addAction(self.BOM_action1)
            self.input_BOM_rows.addAction(self.BOM_action2)

            #- cancel button
            self.cancel_button = QPushButton(self.text_cancel, self)
            self.cancel_button.clicked.connect(self.onCancel)
            self.cancel_button.setAutoDefault(False) # no AutoDefault with okButton!
            self.cancel_button.move(80, 300)
            #- OK button
            self.ok_button = QPushButton(self.text_ok, self)
            self.ok_button.clicked.connect(self.onOk)
            self.ok_button.move(200, 300)

        # now make the window visible
        self.show()

    def setWindowTexts(self, lang)   *
        if lang == "German"   *
            self.text_format   = "Gewünschtes Blattformat \nauswählen"
            self.text_language = "Sprache für Schriftfeld \nund Stückliste auswählen"
            self.text_bom      = ("Bei Bedarf \nAnzahl erforderlicher"+
            " \nStücklistenzeilen eingeben")
            self.text_window   = "Dialogfenster"
            self.text_cancel   = "Abbrechen"
            self.text_ok       = "OK"
            self.text_none     = "Keine"
            self.text_maximum  = "Maximal"
            self.text_warning  = ("Nicht vergessen, die Datei zu \nSpeichern, Schließen " +
            "und wieder zu Öffnen!")
            self.tooltip_format   = ("Die Auswahl eines Blattformats \nsetzt "+
            "die Anzahl der Stücklistenzeilen \nauf 0 zurück")
            self.tooltip_language = "Sprache des Schriftfeldes auswählen"
            self.tooltip_bom      = ("Die Anzahl der \nStücklistenzeilen"+
            " \neingeben oder  mit \nder rechten Maustaste \n\"Keine\" oder \n\"Maximal\" auswählen")
        elif lang == "French"   *
            self.text_format   = "Sélectionnez le format \nde page de votre choix"
            self.text_language = "Sélectionnez language de le \ncartouche et la liste des pièces"
            self.text_bom      = "Entrer nombre de lignes \npour la liste des pièces, \nau besoin"
            self.text_window   = "Fenêtre de dialogue"
            self.text_cancel   = "Annuler"
            self.text_ok       = "OK"
            self.text_none     = "Aucun"
            self.text_maximum  = "Maximum"
            self.text_warning  = "Don't forget to Save, Close \nand Reopen the file!"
            self.tooltip_format   = ("Selecting a sheet format \n"+
            "resets the number \nof BOM rows to 0")
            self.tooltip_language = "Select language of the title block"
            self.tooltip_bom      = ("Enter the number \nof BOM rows or use \n"+
            "right mouse buton \nto select \"Aucun\" or \n\"Maximum\"")
        elif lang == "Italian"   *
            self.text_format   = "Selezionare il formato \ndesiderato"
            self.text_language = "Selezionare lingua del \ncartiglio e la lista dei pezzi"
            self.text_bom      = "Inserire numero delle linee \nper la lista dei pezzi, \nall'occorrenza"
            self.text_window   = "Finestra di dialogo"
            self.text_cancel   = "Annulla"
            self.text_ok       = "OK"
            self.text_none     = "Nessuno"
            self.text_maximum  = "Massimo"
            self.text_warning  = "Don't forget to Save, Close \nand Reopen the file!"
            self.tooltip_format   = ("Selecting a sheet format \n"+
            "resets the number \nof BOM rows to 0")
            self.tooltip_language = "Select language of the title block"
            self.tooltip_bom      = ("Enter the number \nof BOM rows or use \n"+
            "right mouse buton \nto select \"Nessuno\" or \n\"Massimo\"")
        else   *
            self.text_format   = "Select desired \nsheet format"
            self.text_language = "Select language for \nthe title block and BOM"
            self.text_bom      = "Enter number of rows \nfor a BOM, if required"
            self.text_window   = "Dialogue window"
            self.text_cancel   = "Cancel"
            self.text_ok       = "OK"
            self.text_none     = "None"
            self.text_maximum  = "Maximum"
            self.text_warning  = "Don't forget to Save, Close \nand Reopen the file!"
            self.tooltip_format   = ("Selecting a sheet format \n"+
            "resets the number \nof BOM rows to 0")
            self.tooltip_language = "Select language of the title block"
            self.tooltip_bom      = ("Enter the number \nof BOM rows or use \n"+
            "right mouse buton \nto select \"None\" or \n\"Maximum\"")

    def onPopupFormat(self, selected_text)   *
        self.result_format = selected_text
        # WRS suggestion   *
        max_row = 0
        #print("Format   * ", selected_text)
        if selected_text == "ISO A4"   *
            max_row = 34
        elif selected_text =="ISO A3"   *
            max_row = 34
        elif selected_text =="ISO A2"   *
            max_row = 54
        elif selected_text =="ISO A1"   *
            max_row = 83
        elif selected_text =="ISO A0"   *
            max_row = 125

        elif selected_text =="ANSI A"   *
            max_row = 31
        elif selected_text =="ANSI B"   *
            max_row = 31
        elif selected_text =="ANSI C"   *
            max_row = 56
        elif selected_text =="ANSI D"   *
            max_row = 78
        elif selected_text =="ANSI E"   *
            max_row = 128

        elif selected_text =="Arch A"   *
            max_row = 35
        elif selected_text =="Arch B"   *
            max_row = 35
        elif selected_text =="Arch C"   *
            max_row = 61
        elif selected_text =="Arch D"   *
            max_row = 86
        elif selected_text =="Arch E"   *
            max_row = 137
        elif selected_text =="Arch E1"   *
            max_row = 111
        else   *
            max_row = 0

        self.input_BOM_rows.setMaximum(max_row) # max. value for selectd format
        self.input_BOM_rows.setValue(0)         # reset default value

    def onPopupLanguage(self, selected_text)   *
        self.result_language = selected_text

    def onBOMAction1(self)   *
        # no bill of material
        self.input_BOM_rows.setValue(0)
    def onBOMAction2(self)   *
        # max. rows for selected format
        self.input_BOM_rows.setValue(self.input_BOM_rows.maximum())

    def onCancel(self)   *
        self.result = "Cancelled"
        self.close()
    def onOk(self)   *
        self.result = "OK"
        self.close()

#- set values according to ISO, ANSI, Arch
def setBorderValues(format)   *
    # customise values if needed
    # I assume ANSI and Arch need different values but as long as I'm not sure
    # these settings are quite redundant but are not removed
    if format[0   *3] == "ANS"   *
        borders.drawing_area_top    = 10 # distance from page boundary
        borders.drawing_area_bottom = 10
        borders.drawing_area_left   = 20
        borders.drawing_area_right  = 10
        borders.sheet_frame_top     = 5  # distance from drawing area border
        borders.sheet_frame_bottom  = 5
        borders.sheet_frame_left    = 5
        borders.sheet_frame_right   = 5
    elif format[0   *3] == "Arc"   *
        borders.drawing_area_top    = 10 # distance from page boundary
        borders.drawing_area_bottom = 10
        borders.drawing_area_left   = 20
        borders.drawing_area_right  = 10
        borders.sheet_frame_top     = 5  # distance from drawing area border
        borders.sheet_frame_bottom  = 5
        borders.sheet_frame_left    = 5
        borders.sheet_frame_right   = 5
    else   *
        borders.drawing_area_top    = 10 # distance from page boundary
        borders.drawing_area_bottom = 10
        borders.drawing_area_left   = 20
        borders.drawing_area_right  = 10
        borders.sheet_frame_top     = 5  # distance from drawing area border
        borders.sheet_frame_bottom  = 5
        borders.sheet_frame_left    = 5
        borders.sheet_frame_right   = 5

def setSheetDimensions(format)   *
    if format[0   *3] == "ANS"   *
        if format[-1   *] == "A"   *
            sheet_format.width  = "216"
            sheet_format.height = "279"
        elif format[-1   *] == "B"   *
            sheet_format.width  = "432"
            sheet_format.height = "279"
        elif format[-1   *] == "C"   *
            sheet_format.width  = "559"
            sheet_format.height = "432"
        elif format[-1   *] == "D"   *
            sheet_format.width  = "864"
            sheet_format.height = "559"
        else   * # E
            sheet_format.width  = "1118"
            sheet_format.height = "864"
    elif format[0   *3] == "Arc"   *
        if format[-1   *] == "A"   *
            sheet_format.width  = "229"
            sheet_format.height = "305"
        elif format[-1   *] == "B"   *
            sheet_format.width  = "457"
            sheet_format.height = "305"
        elif format[-1   *] == "C"   *
            sheet_format.width  = "610"
            sheet_format.height = "457"
        elif format[-1   *] == "D"   *
            sheet_format.width  = "914"
            sheet_format.height = "610"
        elif format[-1   *] == "E"   *
            sheet_format.width  = "1219"
            sheet_format.height = "914"
        else   * # E1
            sheet_format.width  = "1067"
            sheet_format.height = "762"
    else   * # ISO
        if format[-1   *] == "4"   *
            sheet_format.width  = "210"
            sheet_format.height = "297"
        elif format[-1   *] == "3"   *
            sheet_format.width  = "420"
            sheet_format.height = "297"
        elif format[-1   *] == "2"   *
            sheet_format.width  = "594"
            sheet_format.height = "420"
        elif format[-1   *] == "1"   *
            sheet_format.width  = "841"
            sheet_format.height = "594"
        else   * # A0
            sheet_format.width  = "1189"
            sheet_format.height = "841"
    print(format, sheet_format.width, sheet_format.height)

def setTitleBlockStaticTexts(language)   *
    # Labels for the text entry fields in chosen language
    if language == "DE"   *
        title_block.author_name      = "Ersteller   *"
        title_block.date_of_creation = "Datum   *"
        title_block.supervisor_name  = "Prüfer   *"
        title_block.date_of_approval = "Datum   *"
        title_block.sheet_format     = "Format   *"
        title_block.sheet_scale      = "Maßstab   *"
        title_block.weight           = "Gewicht   *"
        title_block.owner            = "Eigentümer   *"
        title_block.version          = "Version   *"
        title_block.sheet_count      = "Blatt   *"
    elif language == "FR"   *
        title_block.author_name      = "Dessinateur   *"
        title_block.date_of_creation = "Date   *"
        title_block.supervisor_name  = "Validé par   *"
        title_block.date_of_approval = "Date   *"
        title_block.sheet_format     = "Format   *"
        title_block.sheet_scale      = "Échelle   *"
        title_block.weight           = "Poids   *"
        title_block.owner            = "Société   *"
        title_block.version          = "Version   *"
        title_block.sheet_count      = "Feuille   *"
    elif language == "IT"   *
        title_block.author_name      = "Nome Progettista   *"
        title_block.date_of_creation = "Data   *"
        title_block.supervisor_name  = "Supervisore   *"
        title_block.date_of_approval = "Data   *"
        title_block.sheet_format     = "Formato   *"
        title_block.sheet_scale      = "Scala   *"
        title_block.weight           = "Peso   *"
        title_block.owner            = "Ditta   *"
        title_block.version          = "Numero di Versione   *"
        title_block.sheet_count      = "Pagina   *"
    else   *
        title_block.author_name      = "Author Name   *"
        title_block.date_of_creation = "Date   *"
        title_block.supervisor_name  = "Supervisor Name   *"
        title_block.date_of_approval = "Date   *"
        title_block.sheet_format     = "Format   *"
        title_block.sheet_scale      = "Scale   *"
        title_block.weight           = "Weight   *"
        title_block.owner            = "Owner   *"
        title_block.version          = "Version   *"
        title_block.sheet_count      = "Sheet   *"

def setBillOfMaterialTexts(language)   *
    # Labels for the BOM bottom line in chosen language
    if language == "DE"   *
        bom_list.position = "Pos."
        bom_list.amount   = "Menge"
        bom_list.unit     = "Einheit"
        bom_list.title    = "Benennung"
        bom_list.number   = "Sachnummer"
        bom_list.material = "Werkstoff"
        bom_list.mass     = "Masse"
        bom_list.remark   = "Bemerkung"
    else   *
        bom_list.position = "Pos."
        bom_list.amount   = "Amount"
        bom_list.unit     = "Unit"
        bom_list.title    = "Title"
        bom_list.number   = "Part number"
        bom_list.material = "Material"
        bom_list.mass     = "Mass"
        bom_list.remark   = "Remark"

#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y)   *
    svg_line=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svg_line

#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2)   *
    if x2=="v" or x2=="V" or x2=="h" or x2=="H"   *
        svg_line=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else   *
        svg_line=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svg_line

#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue)   *
    svg_line=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svg_line

#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue)   *
    svg_line=("<text freecad   *editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svg_line

#- Create a file and insert a header line
def createSvgFile(file_path)   *
    t=open(file_path,"w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def startSvg(file_path)   *
    t=open(file_path,"a") # a = append, new lines are added at the end of an existing file
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http   *//www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns   *freecad=\"http   *//www.freecadweb.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def createSheet(file_path)   *
    #- set sheet dimensions
    sWidth  = sheet_format.width
    sHeight = sheet_format.height
    t=open(file_path,"a")
    t.write("  width =\""+sWidth+"mm\"\n")
    t.write("  height=\""+sHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+sWidth+" "+sHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def endSvg(file_path)   *
    t=open(file_path,"a")
    t.write("</svg>")
    t.close

#- Frame creation
def createFrame(file_path)   *
    t=open(file_path,"a")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill   *none;stroke   *#000000;stroke-width   *0.5;\
stroke-linecap   *round\">\n")
    #- set sheet dimensions
    sWidth  = sheet_format.width
    sHeight = sheet_format.height
    #- set frame offsets
    dAT = borders.drawing_area_top
    dAB = borders.drawing_area_bottom
    dAL = borders.drawing_area_left
    dAR = borders.drawing_area_right
    sFT = borders.sheet_frame_top
    sFB = borders.sheet_frame_bottom
    sFL = borders.sheet_frame_left
    sFR = borders.sheet_frame_right
    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(dAL)
    drawingY=str(dAT)
    #- lower right corner
    drawingWidth=str(int(sWidth)-dAR)
    drawingHeight=str(int(sHeight)-dAB)
    t.write("      \n")
    #- frame dimensions
    drawingWidth=str(int(sWidth)-dAL-dAR)
    drawingHeight=str(int(sHeight)-dAT-dAB)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(dAL-sFL)
    drawingY=str(dAT-sFT)
    #- lower right corner
    drawingWidth=str(int(sWidth)-dAR+sFR)
    drawingHeight=str(int(sHeight)-dAB+sFB)
    t.write("      \n")
    #- frame dimensions
    drawingWidth=str(int(sWidth)-dAL-dAR+sFL+sFR)
    drawingHeight=str(int(sHeight)-dAT-dAB+sFT+sFB)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close

#- Indexes and folding marks creation
def createDecoration(file_path)   *
    t = open(file_path,"a")
    t.write("    <g id=\"index-separators\"\n")
    t.write("      style=\"fill   *none;stroke   *#000000;stroke-width   *0.25;\
stroke-linecap   *round\">\n")
    #- set sheet dimensions
    sWidth  = sheet_format.width
    sHeight = sheet_format.height
    #- set frame offsets
    dAT = borders.drawing_area_top
    dAB = borders.drawing_area_bottom
    dAL = borders.drawing_area_left
    dAR = borders.drawing_area_right
    sFT = borders.sheet_frame_top
    sFB = borders.sheet_frame_bottom
    sFL = borders.sheet_frame_left
    sFR = borders.sheet_frame_right

    drawingX=str(dAL)
    drawingY=str(dAT)
    drawingWidth=str(int(sWidth)-dAL-dAR)
    drawingHeight=str(int(sHeight)-dAT-dAB)

    #- starting point values of center lines
    indexCenter=str(int(drawingWidth)/2+dAL)
    indexMiddle=str(int(drawingHeight)/2+dAT)
    indexLeft=str(dAL+5)
    indexRight=str(int(drawingWidth)+dAL-5)
    indexUpper=str(dAT+5)
    indexLower=str(int(drawingHeight)+dAT-5)

    #- centre and middle markings of drawing area
    if sWidth=="210"   * # format=="DIN-A4"   *
        indexLeft=str(dAL)
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-15")+"\n")
    elif sWidth=="420"   * # format=="DIN-A3"   *
        indexLeft=str(dAL+5)
        t.write("        "+svgpath(indexCenter,indexUpper,"v","-10")+"\n")
        t.write("        "+svgpath(indexCenter,indexLower,"v"," 10")+"\n")
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-20")+"\n")
        t.write("        "+svgpath(indexRight,indexMiddle,"h"," 10")+"\n")
    else    *
        t.write("        "+svgpath(indexCenter,indexUpper,"v","-10")+"\n")
        t.write("        "+svgpath(indexCenter,indexLower,"v"," 10")+"\n")
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-10")+"\n")
        t.write("        "+svgpath(indexRight,indexMiddle,"h"," 10")+"\n")

    #- starting point values of separator lines
    indexLeft =str(dAL)
    indexRight=str(int(drawingWidth)+dAL)
    indexUpper=str(dAT)
    indexLower=str(int(drawingHeight)+dAT)

    #- set number of horizontal and vertical indexes
    # this needs to be extended for American formats
    if sWidth=="420"   * # format=="DIN-A3"   *
        indexCountX=8
        indexCountY=6
    elif sWidth=="594"   * # format=="DIN-A2"   *
        indexCountX=12
        indexCountY=8
    elif sWidth=="841"   * # format=="DIN-A1"   *
        indexCountX=16
        indexCountY=12
    elif sWidth=="1189"   * # format=="DIN-A0"   *
        indexCountX=24
        indexCountY=16
    else    *
        indexCountX=0
        indexCountY=0

    #- indexCenter and indexMiddle contain strings but floating point
    #   numbers are needed to calculate
    floatCenter=int(drawingWidth)/2+dAL
    floatMiddle=int(drawingHeight)/2+dAT

    #- horizontal index separators
    max=int(indexCountX/2-1)
    for value in range(0,max)   *
        indexX=str(floatCenter+(value+1)*50)
        t.write("        "+svgpath(indexX,indexUpper,"v"," -5")+"\n")
        t.write("        "+svgpath(indexX,indexLower,"v","  5")+"\n")
        indexX=str(floatCenter-(value+1)*50)
        t.write("        "+svgpath(indexX,indexUpper,"v"," -5")+"\n")
        t.write("        "+svgpath(indexX,indexLower,"v","  5")+"\n")

    #- vertical index separators
    max=int(indexCountY/2-1)
    for value in range(0,max)   *
        indexY=str(floatMiddle+(value+1)*50)
        t.write("        "+svgpath(indexLeft, indexY,"h"," -5")+"\n")
        t.write("        "+svgpath(indexRight,indexY,"h","  5")+"\n")
        indexY=str(floatMiddle-(value+1)*50)
        t.write("        "+svgpath(indexLeft, indexY,"h"," -5")+"\n")
        t.write("        "+svgpath(indexRight,indexY,"h","  5")+"\n")

    t.write("    </g>\n")

    t.write("    <g id=\"indexes\"\n")
    t.write("      style=\"font-size   *3.5;text-anchor   *middle;fill   *#000000;\
    font-family   *osifont\">\n")

    #- position point values of indexes
    indexLeft=str(dAL-sFL/2)
    indexRight=str(int(drawingWidth)+dAL+sFR/2)
    indexUpper=str(dAT-1)
    indexLower=str(int(drawingHeight)+dAT+sFB-1)

    #- horizontal indexes, numbers
    max=int(indexCountX/2)
    for value in range(0,max)   *
        indexX=str(floatCenter+value*50+25)
        t.write("        "+svgtext(indexX,indexUpper,str(int(indexCountX/2+value+1)))+"\n")
        t.write("        "+svgtext(indexX,indexLower,str(int(indexCountX/2+value+1)))+"\n")
        indexX=str(floatCenter-value*50-25)
        t.write("        "+svgtext(indexX,indexUpper,str(int(indexCountX/2-value)))+"\n")
        t.write("        "+svgtext(indexX,indexLower,str(int(indexCountX/2-value)))+"\n")

    #- vertical indexes, letters
    max=int(indexCountY/2)
    for value in range(0,max)   *
        indexY=str(floatMiddle+value*50+25)
        if int(indexCountY/2+value+1)>9    *  # to avoid the letter J
            t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2+value+2)))+"\n")
            t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2+value+2)))+"\n")
        else    *
            t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2+value+1)))+"\n")
            t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2+value+1)))+"\n")
        indexY=str(floatMiddle-value*50-25)
        t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2-value)))+"\n")
        t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2-value)))+"\n")

    t.write("    </g>\n\n")

    #- puncher mark
    t.write("    <g id=\"puncher mark\"\n")
    t.write("      style=\"fill   *none;stroke   *#b0b0b0;stroke-width   *0.25;\
    stroke-linecap   *miter;stroke-miterlimit   *4\">\n")
    if sWidth in["1189", "841", "594"]    * # A3 and A4 have extended middle markings
        t.write("        "+svgpath(str(dAL-sFL),str(int(sHeight)-(297/2)),"h","-10")+"\n")
    t.write("    </g>\n\n")

    #- folding marks
    t.write("    <g id=\"folding marks\"\n")
    t.write("      style=\"fill   *none;stroke   *#b0b0b0;stroke-width   *0.25;\
    stroke-linecap   *miter;stroke-miterlimit   *4\">\n")
    if sWidth=="420"   * # DIN-A3
        t.write("        "+svgpath("125",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("125",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("230",str(dAT-sFT),"v","-5")+"\n")
        t.write("        "+svgpath("230",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
    elif sWidth=="594"   * # DIN-A2
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("402",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("402",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","123","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(sWidth)-dAR+sFR),"123","h","  5")+"\n")
    elif sWidth=="841"   * # DIN-A1
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("400",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("400",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("651",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("651",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","297","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(sWidth)-dAR+sFR),"297","h","  5")+"\n")
    elif sWidth=="1189"   * # DIN-A0
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("400",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("400",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("590",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("590",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("780",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("780",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("999",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("999",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","247","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(sWidth)-dAR+sFR),"247","h","  5")+"\n")
        t.write("        "+svgpath("  5","544","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(sWidth)-dAR+sFR),"544","h","  5")+"\n")

    t.write("    </g>\n\n")
    t.close

#- Title block movable
def createTitleBlock(file_path)   *
    #- set sheet dimensions
    sWidth  = sheet_format.width
    sHeight = sheet_format.height
    #- set frame offsets
    dAB = borders.drawing_area_bottom
    dAR = borders.drawing_area_right
    #- set static texts
    tb_author     = title_block.author_name
    tb_created    = title_block.date_of_creation
    tb_supervisor = title_block.supervisor_name
    tb_approved   = title_block.date_of_approval
    tb_format     = title_block.sheet_format
    tb_scale      = title_block.sheet_scale
    tb_weight     = title_block.weight
    tb_owner      = title_block.owner
    tb_version    = title_block.version
    tb_sheet      = title_block.sheet_count

    #- lower left corner
    tbX=str(int(sWidth)-dAR-180) # 180 according to DIN EN ISO 7200
    tbY=str(int(sHeight)-dAB)
    #- group to move allelements in one step
    t=open(file_path,"a")
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate("+tbX+","+tbY+")\">\n")
    t.write("      \n\n")
    #- title block
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill   *none;stroke   *#000000;stroke-width   *0.35;\
stroke-linecap   *miter;stroke-miterlimit   *4\">\n")
    t.write("        "+svgpath("  0","  0","  0","-63")+"\n")
    t.write("        "+svgpath("  0","-63","180","  0")+"\n")
    t.write("        "+svgpath("  0"," -4","h","155")+"\n")
    t.write("        "+svgpath("  0","-16","h","155")+"\n")
    t.write("        "+svgpath("  0","-30","h","155")+"\n")
    t.write("        "+svgpath("  0","-46.5","h"," 50")+"\n")
    t.write("        "+svgpath(" 25"," -4","v","-26")+"\n")
    t.write("        "+svgpath(" 50"," -4","v","-59")+"\n")
    t.write("        "+svgpath("140"," -4","v","-12")+"\n")
    t.write("        "+svgpath("155","  0","v","-63")+"\n")
    t.write("        "+svgpath("160","  0","v","-63")+"\n")
    t.write("        "+svgpath("155"," -7","h"," 25")+"\n")
    t.write("        "+svgpath("155","-14","h"," 25")+"\n")
    t.write("        "+svgpath("155","-21","h"," 25")+"\n")
    t.write("        "+svgpath("155","-28","h"," 25")+"\n")
    t.write("        "+svgpath("155","-35","h"," 25")+"\n")
    t.write("        "+svgpath("155","-42","h"," 25")+"\n")
    t.write("        "+svgpath("155","-49","h"," 25")+"\n")
    t.write("        "+svgpath("155","-56","h"," 25")+"\n")
    t.write("      </g>\n")
    #- small texts, left-aligned
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size   *2.5;text-anchor   *start;fill   *#000000;\
font-family   *osifont\">\n")
    t.write("        "+svgtext("  1.5","-60  ", tb_author)+"\n")
    t.write("        "+svgtext("  1.5","-52  ", tb_created)+"\n")
    t.write("        "+svgtext("  1.5","-43.5 ", tb_supervisor)+"\n")
    t.write("        "+svgtext("  1.5","-35.5 ", tb_approved)+"\n")
    t.write("        "+svgtext("  1.5","-27  ", tb_format)+"\n")
    t.write("        "+svgtext("  1.5","-13  ", tb_scale)+"\n")
    t.write("        "+svgtext(" 26.5","-13  ", tb_weight)+"\n")
    t.write("        "+svgtext(" 51.5","-27  ", tb_owner)+"\n")
    t.write("        "+svgtext(" 51.5","-13  ", tb_version)+"\n")
    t.write("        "+svgtext("141.5","-13  ", tb_sheet)+"\n")
    t.write("      </g>\n")
    #- revision indexes, centered
    t.write("      <g id=\"titleblock-revision-indexes\"\n")
    t.write("        style=\"font-size   *5.0;text-anchor   *middle;fill   *#000000;\
font-family   *osifont\">\n")
    t.write("        "+svgtext("157.5"," -1.5  ","A")+"\n")
    t.write("        "+svgtext("157.5"," -8.5  ","B")+"\n")
    t.write("        "+svgtext("157.5","-15.5  ","C")+"\n")
    t.write("        "+svgtext("157.5","-22.5  ","D")+"\n")
    t.write("        "+svgtext("157.5","-29.5  ","E")+"\n")
    t.write("        "+svgtext("157.5","-36.5  ","F")+"\n")
    t.write("        "+svgtext("157.5","-43.5  ","G")+"\n")
    t.write("        "+svgtext("157.5","-50.5  ","H")+"\n")
    t.write("        "+svgtext("157.5","-57.5  ","I")+"\n")
    t.write("      </g>\n")

    t.write("    </g>\n\n")
    t.close

#- Title block editable texts
def createEditableText(file_path)   *
    #- set sheet dimensions
    sWidth  = sheet_format.width
    sHeight = sheet_format.height
    #- set frame offsets
    dAB = borders.drawing_area_bottom
    dAR = borders.drawing_area_right

    #- offsets for editable texts
    edX=int(sWidth)-dAR-180 # 180 according to DIN EN ISO 7200
    edY=int(sHeight)-dAB

    t=open(file_path,"a")
    t.write("    <g id=\"titleblock-editable-owner\"\n")
    t.write("      style=\"font-size   *3.5;text-anchor   *start;fill   *#0000d0;\
font-family   *osifont\">\n")

    t.write("      "+FCeditext("Owner",str(edX+65),str(edY-27.0),"Owner")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-address\"\n")
    t.write("      style=\"font-size   *2.5;text-anchor   *start;fill   *#0000d0;\
font-family   *osifont\">\n")
    t.write("      "+FCeditext("Address-1",str(edX+65),str(edY-23.5),"Address1")+"\n")
    t.write("      "+FCeditext("Address-2",str(edX+65),str(edY-20.0),"Address2")+"\n")
    t.write("      "+FCeditext("MailTo",   str(edX+65),str(edY-16.5),"MailTo")+"\n")
    t.write("      "+FCeditext("Copyright",str(edX+2), str(edY-1.0), "Copyright")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-medium\"\n")
    t.write("      style=\"font-size   *5;text-anchor   *start;fill   *#0000d0;\
font-family   *osifont\">\n")
    t.write("      "+FCeditext("Author",    str(edX+2),  str(edY-55.0),"Author")+"\n")
    t.write("      "+FCeditext("AuDate",    str(edX+7),  str(edY-47.5),"YYYY/MM/DD")+"\n")
    t.write("      "+FCeditext("Supervisor",str(edX+2),  str(edY-38.5),"Supervisor")+"\n")
    t.write("      "+FCeditext("SvDate",    str(edX+7),  str(edY-31.0),"YYYY/MM/DD")+"\n")
    t.write("      "+FCeditext("SubTitle",  str(edX+64), str(edY-42.0),"Sub-title")+"\n")
    t.write("      "+FCeditext("Version",   str(edX+60), str(edY-8.0), "Version")+"\n")
    t.write("      "+FCeditext("Revision-A",str(edX+162),str(edY-1.5), "______")+"\n")
    t.write("      "+FCeditext("Revision-B",str(edX+162),str(edY-8.5), "______")+"\n")
    t.write("      "+FCeditext("Revision-C",str(edX+162),str(edY-15.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-D",str(edX+162),str(edY-22.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-E",str(edX+162),str(edY-29.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-F",str(edX+162),str(edY-36.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-G",str(edX+162),str(edY-43.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-H",str(edX+162),str(edY-50.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-I",str(edX+162),str(edY-57.5),"______")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-centered\"\n")
    t.write("      style=\"font-size   *5;text-anchor   *middle;fill   *#0000d0;\
font-family   *osifont\">\n")
    t.write("      "+FCeditext("Format", str(edX+12), str(edY-21),"A3")+"\n")
    t.write("      "+FCeditext("Sheets", str(edX+148),str(edY-8), "1 / 1")+"\n")
    t.write("      "+FCeditext("Scale",  str(edX+12), str(edY-8), "1    * 1")+"\n")
    t.write("      "+FCeditext("Weight", str(edX+35), str(edY-8), "___ kg")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-Large\"\n")
    t.write("      style=\"font-size   *7;text-anchor   *start;fill   *#0000d0;\
font-family   *osifont\">\n")
    t.write("      "+FCeditext("Title",   str(edX+62),str(edY-50),"Drawing Title")+"\n")
    t.write("      "+FCeditext("PtNumber",str(edX+62),str(edY-32),"Part Number")+"\n")
    t.write("    </g>\n\n")
    t.close

#- Title block Freecad logo
def createFreecadLogo(file_path)   *
    #- set sheet dimensions
    sWidth  = sheet_format.width
    sHeight = sheet_format.height
    #- set frame offsets
    dAB = borders.drawing_area_bottom
    dAR = borders.drawing_area_right

    t=open(file_path,"a")
    t.write("    <g id=\"freecad-logo-F\"\n")
    t.write("      style=\"display   *inline\"\n")
    t.write("      stroke=\"#000000\"\n")
    t.write("      stroke-width=\"0.25\"\n")
    t.write("      fill=\"rgb(255, 50, 50)\"\n")
    t.write("      fill-rule=\"evenodd\"\n")
    stX=int(sWidth)  - dAR - 128
    stY=int(sHeight) - dAB -  12
    t.write("      transform=\"translate("+str(stX)+","+str(stY)+") scale(0.6)\">\n")
    t.write("      <path d=\"m0.1524,0.15254 v8.8549 h1.9744 v-3.4652 h1.396 \
v-1.3661 h-1.396 v-1.4745 h3.4391 v-2.5441 l-5.4135 -0.005z\"/>\n")
    t.write("    </g>\n")

    t.write("    <g id=\"freecad-logo-Cog\"\n")
    t.write("      style=\"display   *inline\"\n")
    t.write("      stroke=\"#000000\"\n")
    t.write("      stroke-width=\"0.25\"\n")
    t.write("      fill=\"rgb(50, 50, 255)\"\n")
    t.write("      fill-rule=\"evenodd\"\n")
    stX=int(sWidth)  - dAR - 128
    stY=int(sHeight) - dAB -  12
    t.write("      transform=\"translate("+str(stX)+","+str(stY)+") scale(0.6)\">\n")
    t.write("      <path d=\"m7.7927,3.4504 -0.50715,-0.176 -0.48387 -1.2366 \
-0.76115 0.04 -0.34718 1.2787 -0.4859 0.23269 -1.2119 -0.53015 -0.51188 0.56882 \
0.65892 1.1485 -0.18006 0.50567 -1.2366 0.48387 0.044064 0.76263 1.2787 0.34718 \
0.23269 0.4859 -0.53421 1.2104 0.56882 0.51188 1.1485 -0.65891 0.50973 0.18155 \
0.4798 1.2351 0.7667 -0.04258 0.34311 -1.2802 0.4859 -0.23269 1.2145 0.5357 \
0.51188 -0.56882 -0.65891 -1.1485 0.17748 -0.51122 1.2351 -0.4798 -0.03851 -0.76521 \
-1.2802 -0.34311 -0.23269 -0.4859 0.53163 -1.216 -0.56881 -0.51184z \
m-0.5715 1.2244 0.23576 0.13679 0.20426 0.18519 0.16353 0.22101 0.11763 0.24572 \
0.06916 0.26489 0.01146 0.27146 -0.03921 0.27139 -0.08948 0.25764 -0.14234 0.23834 \
-0.17964 0.2016 -0.22101 0.16353 -0.24572 0.11763 -0.26489 0.06916 -0.27295 0.01553 \
-0.2719 -0.04 -0.2576 -0.089 -0.2383 -0.143 -0.2002 -0.183 -0.165 -0.217 \
-0.1177 -0.246 -0.0676 -0.269 -0.0156 -0.273 0.039206 -0.2714 0.089484 -0.25764 \
0.14085 -0.23427 0.18113 -0.20574 0.22101 -0.16352 0.24572 -0.11763 0.26895 -0.06768 \
0.27147-0.01146 0.27139 0.03921 0.25764 0.08948z\"/>\n")
    t.write("    </g>\n\n")
    t.close

#- Symbol for first angle projection
def createProjectionSymbol(file_path)   *
    #- set sheet dimensions
    sWidth  = sheet_format.width
    sHeight = sheet_format.height
    #- set frame offsets
    dAB = borders.drawing_area_bottom
    dAR = borders.drawing_area_right
    # order top and side symbols
    if projectionGroupAngle() == 1   *
        # Third angle projection
        top_offset  = "-3.5"
        side_offset =  "3.5"
    else   *
        # First angle projection
        top_offset  =  "3.5"
        side_offset = "-3.5"

    t=open(file_path,"a")
    t.write("    <g id=\"Projection-symbol\"\n")
    t.write("      stroke=\"#000000\"\n")
    t.write("      stroke-width=\"0.18\"\n")
    t.write("      stroke-linecap=\"round\"\n")
    t.write("      stroke-linejoin=\"round\"\n")
    t.write("      fill=\"none\"\n")
    stX=int(sWidth) - dAR - 142
    stY=int(sHeight)- dAB - 23
    t.write("      transform=\"translate("+str(stX)+","+str(stY)+")\">\n")
    t.write("      <g id=\"Top\"\n")
    t.write("        transform=\"translate("+top_offset+","+"0.0"+")\">\n")
    t.write("        <circle cx=\"0.0\" cy=\"0.0\" r=\"1.0\"\n")
    t.write("          stroke=\"#0000d0\" stroke-width=\"0.35\"/>\n")
    t.write("        <circle cx=\"0.0\" cy=\"0.0\" r=\"2.0\"\n")
    t.write("          stroke=\"#0000d0\" stroke-width=\"0.35\"/>\n")
    t.write("        "+svgpath(" -2.5 "," 0   ","h"," 1")+"\n")
    t.write("        "+svgpath(" -1.15"," 0   ","h"," 0.3")+"\n")
    t.write("        "+svgpath(" -0.5 "," 0   ","h"," 1")+"\n")
    t.write("        "+svgpath("  0.85"," 0   ","h"," 0.3")+"\n")
    t.write("        "+svgpath("  1.5 "," 0   ","h"," 1")+"\n")
    t.write("        "+svgpath("  0   ","-2.5 ","v"," 1")+"\n")
    t.write("        "+svgpath("  0   ","-1.15","v"," 0.3")+"\n")
    t.write("        "+svgpath("  0   ","-0.5 ","v"," 1")+"\n")
    t.write("        "+svgpath("  0   "," 0.85","v"," 0.3")+"\n")
    t.write("        "+svgpath("  0   "," 1.5 ","v"," 1")+"\n")
    t.write("      </g>\n")
    t.write("      <g id=\"Side\"\n")
    t.write("        transform=\"translate("+side_offset+","+"0.0"+")\">\n")
    t.write("        <path d=\"m -2.5 1.0 v -2.0 l 5.0 -1.0 v 4.0 z \"\n")
    t.write("          stroke=\"#0000d0\" stroke-width=\"0.35\"/>\n")
    t.write("        "+svgpath(" -3.0 "," 0   ","h"," 1")+"\n")
    t.write("        "+svgpath(" -0.5 "," 0   ","h"," 1")+"\n")
    t.write("        "+svgpath("  2.0 "," 0   ","h"," 1")+"\n")
    t.write("        "+svgpath(" -1.4 "," 0   ","h"," 0.3")+"\n")
    t.write("        "+svgpath("  1.1 "," 0   ","h"," 0.3")+"\n")
    t.write("      </g>\n")
    t.write("    </g>\n\n")
    t.close

def createBOMLines(file_path,bom_rows)   *
    #- set sheet dimensions
    sWidth  = sheet_format.width
    sHeight = sheet_format.height
    #- set frame offsets
    dAB = borders.drawing_area_bottom
    dAR = borders.drawing_area_right

    if bom_rows == 0   *
        return
    else   *
        max_rows = (int(bom_rows)+1)

    stX=int(sWidth)-dAR-180
    stY=int(sHeight)-dAB-63

    t=open(file_path,"a")
    t.write("    <g id=\"bill-of-material\">\n")
    # BOM base line
    t.write("      <g style=\"stroke   *#000000;stroke-width   *0.35;stroke-linecap   *round\">\n")
    if sWidth=="210"   * # format=="DIN-A4"   *
        t.write("        "+svgpath(str(stX),str(stY-8)," 180","  0 ")+"\n")
    else    *
        t.write("        "+svgpath(str(stX),str(stY-8)," 180","  0 ")+"\n")
        t.write("        "+svgpath(str(stX),str(stY)  ,"   0"," -8 ")+"\n")
    t.write("      </g>\n")
    # Field separators
    t.write("      <g style=\"stroke   *#000000;stroke-width   *0.18;stroke-linecap   *round\">\n")
    t.write("        "+svgpath(str(stX+ 10),str(stY),"v","  -8")+"\n")
    t.write("        "+svgpath(str(stX+ 20),str(stY),"v","  -8")+"\n")
    t.write("        "+svgpath(str(stX+ 30),str(stY),"v","  -8")+"\n")
    t.write("        "+svgpath(str(stX+ 60),str(stY),"v","  -8")+"\n")
    t.write("        "+svgpath(str(stX+120),str(stY),"v","  -8")+"\n")
    t.write("        "+svgpath(str(stX+140),str(stY),"v","  -8")+"\n")
    t.write("        "+svgpath(str(stX+160),str(stY),"v","  -8")+"\n")
    t.write("      </g>\n")
    # Non-editable Texts
    t.write("      <g id=\"BOM-h35-non-editable\"\n")
    t.write("        style=\"font-family   *osifont;font-size   *3.5;text-anchor   *middle;fill   *#000000\">\n")
    t.write("        "+svgtext(str(stX+  5),str(stY-4),bom_list.position)+"\n")
    t.write("        "+svgtext(str(stX+ 15),str(stY-4),bom_list.amount)+"\n")
    t.write("        "+svgtext(str(stX+ 25),str(stY-4),bom_list.unit)+"\n")
    t.write("        "+svgtext(str(stX+ 45),str(stY-4),bom_list.title)+"\n")
    t.write("        "+svgtext(str(stX+ 90),str(stY-4),bom_list.number)+"\n")
    t.write("        "+svgtext(str(stX+130),str(stY-4),bom_list.material)+"\n")
    t.write("        "+svgtext(str(stX+150),str(stY-4),bom_list.mass)+"\n")
    t.write("        "+svgtext(str(stX+170),str(stY-4),bom_list.remark)+"\n")
    t.write("      </g>\n")
    # Editable Lines
    t.write("      <g id=\"BOM-Line\">\n")
    #stX=int(sWidth)-dAR-180
    #stY=int(sHeight)-dAB-72
    stY -= 8

    for value in range(1,max_rows)   *
        t.write("        <g style=\"stroke   *#000000;stroke-width   *0.35;stroke-linecap   *round\">\n")
        if sWidth=="210"   * # format=="DIN-A4"   *
            t.write("          "+svgpath(str(stX),str(stY-6)," 180","  0 ")+"\n")
        else    *
            t.write("          "+svgpath(str(stX),str(stY-6)," 180","  0 ")+"\n")
            t.write("          "+svgpath(str(stX),str(stY)  ,"   0"," -6 ")+"\n")
        t.write("        </g>\n")
        t.write("        <g style=\"stroke   *#000000;stroke-width   *0.18;stroke-linecap   *round\">\n")
        t.write("          "+svgpath(str(stX+ 10),str(stY),"v","  -6")+"\n")
        t.write("          "+svgpath(str(stX+ 20),str(stY),"v","  -6")+"\n")
        t.write("          "+svgpath(str(stX+ 30),str(stY),"v","  -6")+"\n")
        t.write("          "+svgpath(str(stX+ 60),str(stY),"v","  -6")+"\n")
        t.write("          "+svgpath(str(stX+120),str(stY),"v","  -6")+"\n")
        t.write("          "+svgpath(str(stX+140),str(stY),"v","  -6")+"\n")
        t.write("          "+svgpath(str(stX+160),str(stY),"v","  -6")+"\n")
        t.write("        </g>\n")
        # Editable Texts
        t.write("        <g id=\"BOM-editable-left-aligned\"\n")
        t.write("          style=\"font-family   *osifont;font-size   *3.5;text-anchor   *start;fill   *#0000d0\">\n")
        t.write("          "+FCeditext("Partname"+str(value),str(stX+32),str(stY-2),"-")+"\n")
        t.write("          "+FCeditext("PartNumber"+str(value),str(stX+62),str(stY-2),"-")+"\n")
        t.write("          "+FCeditext("Material"+str(value),str(stX+122),str(stY-2),"-")+"\n")
        t.write("          "+FCeditext("Remark"+str(value),str(stX+162),str(stY-2),"-")+"\n")
        t.write("        </g>\n")
        t.write("        <g id=\"BOM-editable-right-aligned\"\n")
        t.write("          style=\"font-family   *osifont;font-size   *3.5;text-anchor   *end;fill   *#0000d0\">\n")
        t.write("          "+FCeditext("Position"+str(value),str(stX+9),str(stY-2),str(value))+"\n")
        t.write("          "+FCeditext("Amount"+str(value),str(stX+19),str(stY-2),"-")+"\n")
        t.write("          "+FCeditext("Mass"+str(value),str(stX+159),str(stY-2),"-")+"\n")
        t.write("        </g>\n")
        t.write("        <g id=\"BOM-editable-centered\"\n")
        t.write("          style=\"font-family   *osifont;font-size   *3.5;text-anchor   *middle;fill   *#0000d0\">\n")
        t.write("          "+FCeditext("Unit"+str(value),str(stX+25),str(stY-2),"-")+"\n")
        t.write("        </g>\n")
        stY=stY-6

    t.write("      </g>\n")
    t.write("    </g>\n\n")
    t.close

def existingPages(document)   *
    # this counts existing pages in the active document
    number_of_pages=0
    for entry in document.Objects   *
        if entry.Name[   *4] == "Page"   *
            number_of_pages += 1
    return number_of_pages

def updateSheetTotal(total_pages, document)   *
    # update the number of sheets on earlier sheets
    count_down = total_pages
    while count_down > 1   *
        count_down -= 1
        if count_down < 10   *
            # insert leading zero
            current_page = ("Page"+ "0"+ str(count_down))
        else   *
            current_page = ("Page"+ str(count_down))

        editable_texts = document.getObject(current_page).Template.EditableTexts
        editable_texts["Sheets"]     = (str(count_down) + "/" + str(total_pages))
        document.getObject(current_page).Template.EditableTexts = editable_texts

def setOwnerData()   *
    owner_data.company   = "Owner / Company"
    owner_data.address1  = "Address-1"
    owner_data.address2  = "Address-1"
    owner_data.mailTo    = "Info@theCompany.com"
    owner_data.copyright = "All rights reserved"

def getAuthor()   *
    # Reads the user name from the preferences settings
    parameter_path = App.ParamGet("User parameter   *BaseApp/Preferences/Document")
    author_name = parameter_path.GetString("prefAuthor")
    if author_name == ""   *
        author_name = "not set yet"
    return author_name

def projectionGroupAngle()   *
    # Reads the projection convention from the preferences settings
    parameter_path = App.ParamGet("User parameter   *BaseApp/Preferences/Mod/TechDraw/General")
    projection_angle = parameter_path.GetInt("ProjectionAngle")
    return projection_angle

def main()   *
    # Gui to select some presets
    form = InputWindow()
    form.exec_()
    if form.result == "Cancelled"   *
        pass
    else   *
        template_file = form.template_file
        setBorderValues(form.result_format)
        setSheetDimensions(form.result_format)
        setTitleBlockStaticTexts(form.result_language)
        setBillOfMaterialTexts(form.result_language)

        createSvgFile(template_file) # overwrites existing File
        startSvg(template_file)  # adds Start tag and namespaces
        createSheet(template_file)
        createFrame(template_file)
        createDecoration(template_file)
        createTitleBlock(template_file)
        createEditableText(template_file)
        createFreecadLogo(template_file)
        createProjectionSymbol(template_file)
        createBOMLines(template_file, form.input_BOM_rows.value())
        endSvg(template_file)
        # At this point a new SVG-file is generated and saved
        # and shall be attached to the active document

        # -- Add a page and a template to the active document --

        active_doc = App.activeDocument()
        # add a page to the active document
        #- count existing pages
        how_many = existingPages(active_doc)
        how_many += 1 # for the following new page
        #- Define the new page's name (with only 2 trailing digits)
        if how_many < 10   *
            # insert leading zero
            new_page = ("Page"+ "0"+ str(how_many))
        else   *
            new_page = ("Page"+ str(how_many))

        # set template number according to page number
        new_template = ('Template' + new_page[4   *])
        # add a page object to the active document
        active_doc.addObject('TechDraw   *   *DrawPage',new_page)
        # add a template object to the active document
        active_doc.addObject('TechDraw   *   *DrawSVGTemplate',new_template)
        # load the svg template into the template object
        active_doc.getObject(new_template).Template = template_file
        # add the template object to the page's object list
        active_doc.getObject(new_page).Template = active_doc.getObject(new_template)
        #create entries on first page or copy from first page
        #- check for arch formats
        if form.result_format[   *4] == "Arch"   *
            sheet_format = form.result_format
        else   *
            sheet_format = form.result_format[-2   *]

        if how_many == 1   *
            setOwnerData()
            # update entries on first sheet
            editable_texts = active_doc.getObject(new_page).Template.EditableTexts
            #- EditableTexts is a dictionary automatically created when the Template is inserted
            # Listed are all keys      and (default) values - as created with the template above
            editable_texts["Owner"]      = owner_data.company
            editable_texts["Address-1"]  = owner_data.address1
            editable_texts["Address-2"]  = owner_data.address2
            editable_texts["MailTo"]     = owner_data.mailTo
            editable_texts["Copyright"]  = owner_data.copyright
            editable_texts["Author"]     = getAuthor()
            editable_texts["AuDate"]     = time.strftime("%y/%m/%d")
            #editable_texts["Supervisor"] = "Supervisor"
            #editable_texts["SvDate"]     = "YYYY/MM/DD"
            #editable_texts["SubTitle"]   = "Sub-title"
            editable_texts["Version"]    = "FreeCAD 0.19"
            #editable_texts["Revision-A"] = "______"
            #editable_texts["Revision-B"] = "______"
            #editable_texts["Revision-C"] = "______"
            #editable_texts["Revision-D"] = "______"
            #editable_texts["Revision-E"] = "______"
            #editable_texts["Revision-F"] = "______"
            #editable_texts["Revision-G"] = "______"
            #editable_texts["Revision-H"] = "______"
            #editable_texts["Revision-I"] = "______"
            editable_texts["Format"]     = sheet_format
            #editable_texts["Sheets"]     = "1 / 1"
            #editable_texts["Scale"]      = "1    * 1"
            #editable_texts["Weight"]     = "Weight"
            #editable_texts["Title"]      = "Title"
            #editable_texts["PtNumber"]   = "Part number"
            active_doc.getObject(new_page).Template.EditableTexts = editable_texts
        else   *
            # copy some entries from first sheet that are identical on all sheets
            existing_texts = active_doc.Page01.Template.EditableTexts
            editable_texts = active_doc.getObject(new_page).Template.EditableTexts

            editable_texts["Owner"]      = existing_texts["Owner"]
            editable_texts["Address-1"]  = existing_texts["Address-1"]
            editable_texts["Address-2"]  = existing_texts["Address-2"]
            editable_texts["MailTo"]     = existing_texts["MailTo"]
            editable_texts["Copyright"]  = existing_texts["Copyright"]
            editable_texts["Author"]     = getAuthor()
            editable_texts["AuDate"]     = time.strftime("%y/%m/%d")
            #editable_texts["Supervisor"] = existing_texts["Supervisor"]
            #editable_texts["SvDate"]     = existing_texts["SvDate"]
            editable_texts["SubTitle"]   = existing_texts["SubTitle"]
            editable_texts["Version"]    =  "FreeCAD 0.19" #existing_texts["Version"]
            #editable_texts["Revision-A"] = existing_texts["______"]
            #editable_texts["Revision-B"] = existing_texts["______"]
            #editable_texts["Revision-C"] = existing_texts["______"]
            #editable_texts["Revision-D"] = existing_texts["______"]
            #editable_texts["Revision-E"] = existing_texts["______"]
            #editable_texts["Revision-F"] = existing_texts["______"]
            #editable_texts["Revision-G"] = existing_texts["______"]
            #editable_texts["Revision-H"] = existing_texts["______"]
            #editable_texts["Revision-I"] = existing_texts["______"]
            editable_texts["Format"]     = sheet_format
            editable_texts["Sheets"]     = (str(how_many) + "/" + str(how_many))
            #editable_texts["Scale"]      = existing_texts["Scale"]
            editable_texts["Weight"]     = existing_texts["Weight"]
            editable_texts["Title"]      = existing_texts["Title"]
            editable_texts["PtNumber"]   = existing_texts["PtNumber"]
            active_doc.getObject(new_page).Template.EditableTexts = editable_texts
            # update the number of sheets on earlier sheets
            updateSheetTotal(how_many, active_doc)

        # rename 'Page' according to the title block label
        active_doc.getObject(new_page).Label = (title_block.sheet_count[   *-1] + " " + new_page[4   *])
        # open the page object for editing
        active_doc.getObject(new_page).ViewObject.doubleClicked()


main()
}}


</div>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro TemplateHelper
