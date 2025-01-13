# Macro Express Placement/fr
{{Macro/fr
|Name=Macro Express Placement
|Description=Affichez et modifiez rapidement les coordonnées de placement d'un objet sélectionné, directement ou par le biais d'expressions.
|Author=screeneroner
|Download=[https://raw.githubusercontent.com/screeneroner/fc-express-placement/master/fc-express-placement.FCMacro Express Placement]
|Version=1.0
|Date=2023-08-01
|FCVersion=Créé et testé en 0.21
|Icon=Std_AxisCross_example.svg
}}

## Description

La macro **Express Placement** est une extension de l\'interface graphique de FreeCAD. Elle permet d\'éditer rapidement les coordonnées de placement X, Y, Z de l\'objet sélectionné.



## Différence et avantages 

![Standard versus Express](images/Standard_vs_express.png )

Un double clic pour modifier l\'emplacement des objets au lieu de quatre clics séquentiels : **vous pouvez travailler 4 fois plus vite** !



### Emplacement standard de FreeCAD (en rouge) 

L\'éditeur intégré standard de FreeCAD nécessite de nombreux clics de souris supplémentaires avant que vous ne commenciez à modifier les paramètres, en particulier lorsque vous utilisez des expressions paramétriques pour positionner votre objet :

1.  Cliquez sur l\'élément Base/Placement dans la vue Propriété pour déployer l\'arbre Placement.
2.  Cliquez sur la branche Position pour déployer les champs de coordonnées X, Y, Z.
3.  Cliquez sur la coordonnée souhaitée pour rendre visible l\'icône d\'édition d\'expression.
4.  Cliquez sur l\'icône d\'édition d\'expression, qui est si petite qu\'il peut être difficile d\'atteindre.
    Vous pouvez également appuyer sur la touche **&#61;** du clavier. Cela peut prendre encore plus de temps que de cliquer sur l\'icône.

Vous devez répéter ces clics lorsque vous sélectionnez un autre objet. Encore et encore\...



### Express Placement (en vert) 

La macro Express Placement crée un panneau spécial pour vous. Vous pouvez placer ce panneau à l\'endroit de votre choix. Il affiche trois lignes avec des coordonnées X, Y et Z. Ces coordonnées contiennent des valeurs et des champs d\'expression. Ces coordonnées contiennent des valeurs et des champs d\'expression. Il suffit d\'un double clic pour les modifier.

## Installation



### Gestionnaire des extensions 

Trouvez [Express Placement](https://wiki.freecad.org/Macro_Express_Placement) dans le gestionnaire des extensions de FreeCAD et installez-la.



### Lancer directement Express Placement 

Vous pouvez télécharger et utiliser l\'extension Express Placement directement dans votre FreeCAD :

1.  Téléchargez le fichier express-placement.FCMacro et placez-le dans le dossier User Macros à l\'intérieur du dossier d\'installation de FreeCAD. \# Exécutez-le directement à partir du menu principal de FreeCAD Macro/Macros/User Macros.



### Installer le bouton de la barre d\'outils Express Placement 

Pour pouvoir passer rapidement au tableau de Express Placement, vous pouvez placer un bouton pour exécuter rapidement cette macro et faire apparaître le tableau de Express Placement :

1.  Téléchargez le fichier Express Placement.FCMacro et placez-le dans le dossier User Macros à l\'intérieur du dossier d\'installation de FreeCAD.
2.  Sélectionnez la macro Express Placement dans le panneau User Macros, lancé à partir du menu principal de FreeCAD Macro/Macros/User Macros.
3.  Appuyez sur le bouton de la barre d\'outil et suivez les indications de fenêtre de dialogue pour placer le bouton Express Placement à l\'endroit souhaité dans les barres d\'outils de FreeCAD.



## Utilisation

Il suffit d\'exécuter la macro Express Placement directement ou via le bouton de la barre d\'outils et vous verrez une nouvelle fenêtre de propriété ancrée dans l\'interface utilisateur de FreeCAD. Vous pouvez la faire glisser à n\'importe quel endroit autorisé de l\'interface utilisateur et la fermer dès que vous n\'en avez plus besoin. La prochaine fois que vous en aurez besoin, exécutez la macro ou appuyez à nouveau sur le bouton de la barre d\'outils pour faire apparaître la fenêtre Express Placement.

Lorsque vous décidez de modifier le placement de l\'objet sélectionné, il vous suffit de double-cliquer sur la cellule souhaitée dans la fenêtre Placement express et de saisir une nouvelle valeur ou de modifier la valeur existante. La nouvelle valeur sera directement inscrite dans votre modèle.

*Si vous trouvez cette extension utile et que vous estimez qu\'elle vaut la peine de m\'offrir deux-trois tasses de café en reconnaissance de mon travail, vous pouvez le faire à tout moment via [☕ Buy me a coffee](https://www.buymeacoffee.com/screeneroner)*

## Script

Cliquez ici pour afficher/masquer le code source de cette extension.


<div class="mw-collapsible mw-collapsed" id="mw-customcollapsible-codeBlock">


{{MacroCode|code=
<nowiki>
# -*- coding: utf-8 -*-
__Name__ = "Express Placement"
__Comment__ = "FreeCAD GUI addon that allow quick editing X,Y,Z coordinates of the selected object"
__Author__ = "screeneroner"
__Version__ = "1.0"
__Date__ = "2023-08-01"
__License__ = "GPL-3.0"
__Web__ = "https://wiki.freecad.org/Macro_Express_Placement"
__Wiki__ = "https://wiki.freecad.org/Macro_Express_Placement"
__Icon__ = "https://wiki.freecad.org/images/8/8f/Std_AxisCross_example.svg"
__Help__ = "Display and quickly edit selected object placement coordinates directly or via expressions"
__Status__ = "Working"
__Requires__ = "FreeCAD >= 0.19"
__Communication__ = "https://forum.freecad.org/memberlist.php?mode=viewprofile&u=60629"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This macro is free software: you can redistribute it and/or modify it under the terms of the  
version 3 GNU General Public License as published by the Free Software Foundation. 
 
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY without even  
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details (https://www.gnu.org/licenses/gpl-3.0.html) 
 
WARNING TO USERS AND MODIFIERS 
 
This script contains "Buy me a coffee" links to honor the author's hard work and dedication in creating 
all the features present in this code. Removing or altering these links not only violates the GPL license 
but also disregards the significant effort put into making this script valuable for the community. 
 
If you find value in this script and would like to show appreciation to the author, 
kindly consider visiting the site below and treating the author to a few cups of coffee: 
                           https://www.buymeacoffee.com/screeneroner 
Your honor and gratitude is greatly appreciated.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''' 


import FreeCADGui as Gui
import FreeCAD as App
from PySide import QtGui, QtCore

# Define a function to create and display a table
def create_table():
    # Function to update the table with the selected object's data
    def update_table_with_selected_object():
        # Clear the table first
        clear_table()

        # Get the selected objects
        selection = Gui.Selection.getSelection()
        # If there's exactly one selected object
        if len(selection) == 1:
            selected_obj = selection[0]
            selected_object = selected_obj
            # Ensure the object isn't a spreadsheet
            if str(selected_obj.TypeId) != "Spreadsheet::Sheet":
                # Populate the table with the object's placement data
                populate_table_with_placement(selected_obj)
                # Store the selected object on the table widget
                table_widget.selected_object = selected_obj

    # Function to populate the table with an object's placement data
    def populate_table_with_placement(selected_obj):
        # Clear the table first
        clear_table()    # Get the object's placement
        placement = selected_obj.Placement
        # Update each row of the table with the object's placement data
        for row in range(3):  # Limit to 3 instead of row_count
            value_widget = QtGui.QTableWidgetItem()
            value_widget.setText(str(getattr(placement.Base, ["x", "y", "z"][row])))
            table_widget.setItem(row, 0, value_widget)    # Get the object's properties
        properties_list = selected_obj.ExpressionEngine
        # If the object has properties
        if properties_list is not None:
            # For each property that involves placement
            for prop in properties_list:
                if prop[0] in [".Placement.Base.x", ".Placement.Base.y", ".Placement.Base.z"]:
                    # Get the attribute's name
                    attribute = prop[0].split(".")[-1]
                    # Set the corresponding cell's value
                    expression_label = QtGui.QTableWidgetItem()
                    expression_label.setText(prop[1])
                    table_widget.setItem(["x", "y", "z"].index(attribute), 1, expression_label)    # Add the new row with the support data
        support_label_widget = QtGui.QLabel(" ")
        support_link_widget = QtGui.QLabel( u'\u2615' + '  <a href="https://www.buymeacoffee.com/screeneroner">Buy me a coffee</a>  ')
        support_link_widget.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        support_link_widget.setTextFormat(QtCore.Qt.RichText)
        support_link_widget.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        support_link_widget.setOpenExternalLinks(True)
                
        table_widget.setCellWidget(3, 0, support_label_widget)
        table_widget.setCellWidget(3, 1, support_link_widget)    # Adjust the height of each row
        header = table_widget.horizontalHeader()
        header.setFixedHeight(24)  
        for row in range(row_count):
            table_widget.setRowHeight(row, 18)



    # Function to clear the table
    def clear_table():
        for row in range(row_count):
            for col in range(column_count):
                table_widget.takeItem(row, col)

    # Function to update the selected object's placement values based on edits to the table
    def update_values(row):
        item = table_widget.item(row, 0)
        if item is not None:
            # Get the edited text
            edited_text = item.text()
            # Get the label of the value that was edited
            value_label = ["x", "y", "z"][row]
            # Get the selected object
            selected_obj = table_widget.selected_object
            # Get the object's placement
            placement = selected_obj.Placement

            # If the edited text is not empty
            if edited_text != "":
                try:
                    # Try to convert the edited text to a float
                    edited_value = float(edited_text)
                    # Update the corresponding placement value
                    if value_label == "x":
                        placement.Base.x = edited_value
                    elif value_label == "y":
                        placement.Base.y = edited_value
                    elif value_label == "z":
                        placement.Base.z = edited_value
                except ValueError:
                    # If the text can't be converted to a float, print an error message
                    print("Invalid value entered. The value must be a valid number.")

                # Update the object's placement
                selected_obj.Placement = placement

                # Recompute the document to reflect the changes
                App.ActiveDocument.recompute()
                # print(f"Updated value: {edited_value} in row {row}, column 0")

                # Reselect the object to refresh the table data
                reselect_object(selected_obj)

    # Function to update the selected object's expression values based on edits to the table
    def update_expression(row):
        item = table_widget.item(row, 1)
        if item is not None:
            # Get the edited text
            edited_text = item.text()
            # Get the label of the expression that was edited
            expression_label = ["x", "y", "z"][row]
            # Get the selected object
            selected_obj = table_widget.selected_object
            # Get the attribute's name
            attribute = f".Placement.Base.{expression_label}"

            # Update the attribute's expression
            selected_obj.setExpression(attribute, edited_text if edited_text != "" else None)

            # Recompute the document to reflect the changes
            App.ActiveDocument.recompute()
            # print(f"Updated expression: {edited_text} in row {row}, column 1")

            # Reselect the object to refresh the table data
            reselect_object(selected_obj)

    # Function to reselect an object
    def reselect_object(selected_obj):
        # Clear the current selection
        Gui.Selection.clearSelection()
        # Add the selected object to the selection
        Gui.Selection.addSelection(selected_obj)

    # Define the table's dimensions
    row_count = 4
    column_count = 2

    # Create the table widget
    table_widget = QtGui.QTableWidget(row_count, column_count)
    table_widget.setHorizontalHeaderLabels(["Value", "Expression"])
    table_widget.setVerticalHeaderLabels(["x", "y", "z", " "])

    # Left align the headers
    header = table_widget.horizontalHeader()
    header.setDefaultAlignment(QtCore.Qt.AlignLeft)

    # Adjust columns to contents
    table_widget.setSizeAdjustPolicy(QtGui.QAbstractScrollArea.AdjustToContents)
    table_widget.resizeColumnsToContents()
    table_widget.resizeRowsToContents()

    table_widget.setShowGrid(False)

    # Assign a delegate to handle cell edits
    delegate = QtGui.QItemDelegate()
    table_widget.setItemDelegate(delegate)

    # Connect signals to handle cell edits
    delegate.commitData.connect(lambda: update_values(table_widget.currentRow()) if table_widget.currentColumn() == 0 else None)
    delegate.closeEditor.connect(
        lambda: update_expression(table_widget.currentRow()) if table_widget.currentColumn() == 1 else None
    )

    # Define a class to observe selection changes
    class SelectionObserver:
        # When an object is selected, update the table
        def addSelection(self, doc, obj, sub, pnt):
            update_table_with_selected_object()

        # When an object is deselected, update the table
        def removeSelection(self, doc, obj, sub):
            update_table_with_selected_object()

    # Create an instance of the observer class
    selection_observer = SelectionObserver()
    # Add the observer to the selection
    Gui.Selection.addObserver(selection_observer)

    # Update the table with the currently selected object's data
    update_table_with_selected_object()

    # Make the last column stretch to fill the remaining space
    table_widget.horizontalHeader().setStretchLastSection(True)

    # Get the main window
    mainWindow = Gui.getMainWindow()

    # Check if the dock widget already exists
    dock_widget = mainWindow.findChild(QtGui.QDockWidget, "ExpressPlacementWidget")

    # If the dock widget does not exist, create it
    if dock_widget is None:
        dock_widget = QtGui.QDockWidget("Express Placement")
        dock_widget.setObjectName("ExpressPlacementWidget")  # Assign an object name to the dock widget
        mainWindow.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock_widget)

    # Set the dock widget's widget to the table
    dock_widget.setWidget(table_widget)
    # Make sure the dock widget is visible
    dock_widget.setVisible(True)

# Create and display the table
create_table()
</nowiki>
}}


</div>



---
⏵ [documentation index](../README.md) > Macro Express Placement/fr
