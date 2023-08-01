# Macro Arch Axis System Repartition/fr
{{Macro/fr
|Name=Arch Axis System Repartition
|Icon=Macro_Arch_Axis_System_Repartition.png
|Description=Créer un système d'axes le long d'une ligne.
|Author=rockn
|Version=1.0
|Date=2014-12-22
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/a/a0/Macro_Arch_Axis_System_Repartition.png ToolBar Icon]
}}

<img alt="" src=images/ArchAxisSystemRepartition.png  style="width:480px;"> 
*ArchAxisSystemRepartition*

## Description

Voici une macro qui va vous aider dans la création d\'un système d\'axes de l\'atelier Architecture. Pour rappel, l\'outil Système d\'Axes de l\'atelier Architecture permet de créer une répartition où chaque espacement est paramétrable. On peut ensuite l\'associer à un objet FreeCAD afin de le répartir.

## Utilisation

-   Lancer la macro avec ou sans ligne selectionnée.
-   Une fenêtre s\'ouvre dans l\'onglet tâches.
-   Régler la longueur : si une ligne est sélectionnée, la longueur est définie est forcée par la longueur de la ligne ; si rien n\'est sélectionné la longueur peut être ajustée.
-   Régler la longueur de l\'écartement régulier de la répartition.
-   Ou régler le nombre d\'espacement souhaité ; L\'écartement régulier est automatiquement recalculé.
-   Choisir si vous souhaitez que l\'espace restant soit placé au début ou à la fin de la répartition ou de chaque coté.
-   Cocher la case si vous souhaitez une pièce au début de la répartition et régler un éventuel décalage.
-   Cocher la case si vous souhaitez une pièce à la fin de la répartition et régler un éventuel décalage.
-   Pour valider cliquer sur le bouton Ok.
-   Si une ligne est sélectionnée le système d\'axes aura le même placemeent sinon le système est placé à l\'origine du modèle.
-   Si la Librairie FreeCAD est ouverte le fichier sélectionné sera la base du système structurel créé avec le système d\'axes.

## Script

ToolBar Icon ![](images/Macro_Arch_Axis_System_Repartition.png )

**Macro_Repartition.FCMacro**


    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    #***************************************************************************
    #*                                                                         *
    #*   Copyright (c) 2014 Jonathan Wiedemann <wood.galaxy@gmail.com          *
    #*                                                                         *
    #*   This program is free software; you can redistribute it and/or modify  *
    #*   it under the terms of the GNU Lesser General Public License (LGPL)    *
    #*   as published by the Free Software Foundation; either version 2 of     *
    #*   the License, or (at your option) any later version.                   *
    #*   for detail see the LICENCE text file.                                 *
    #*                                                                         *
    #*   This program is distributed in the hope that it will be useful,       *
    #*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
    #*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
    #*   GNU Library General Public License for more details.                  *
    #*                                                                         *
    #*   You should have received a copy of the GNU Library General Public     *
    #*   License along with this program; if not, write to the Free Software   *
    #*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
    #*   USA                                                                   *
    #*                                                                         *
    #***************************************************************************

    __title__="Repartition"
    __author__ = "Jonathan Wiedemann"
    __url__ = "http://www.freecad-france.com"

    import FreeCAD, FreeCADGui, DraftGeomUtils, DraftVecUtils
    import Arch
    import Part
    import math
    from PySide import QtCore, QtGui

    class _RepartitionTaskPanel:
        def __init__(self):
            self.title = QtGui.QLabel('Repartition')
            self.grid = QtGui.QGridLayout()
            self.grid.addWidget(self.title, 1, 0)

            self.longueurLabel = QtGui.QLabel('Longueur')

            self.dSBLongueur = QtGui.QDoubleSpinBox()
            self.dSBLongueur.setRange(0., 9999999.)
            self.sel = FreeCADGui.Selection.getSelection()
            if self.sel:
                self.longueur = self.sel[0].Shape.Length
                self.dSBLongueur.setValue(self.longueur)
            else:
                self.dSBLongueur.setValue(5000.)

            self.grid.addWidget(self.longueurLabel, 2, 0)
            self.grid.addWidget(self.dSBLongueur, 2, 1)

            self.ecartementLabel = QtGui.QLabel('Ecartement')
            self.ecartementDSB = QtGui.QDoubleSpinBox()
            self.ecartementDSB.setRange(0., 9999999.)
            self.ecartementDSB.setValue(500.)
            self.grid.addWidget(self.ecartementLabel, 3, 0)
            self.grid.addWidget(self.ecartementDSB, 3, 1)

            self.qteLabel = QtGui.QLabel('Quantite')
            self.qteSB = QtGui.QSpinBox()
            self.qteSB.setRange(0,99999)
            self.grid.addWidget(self.qteLabel, 4, 0)
            self.grid.addWidget(self.qteSB, 4, 1)

            self.infoText = QtGui.QLabel('Espace restant = ')
            self.grid.addWidget(self.infoText, 5, 0)
            self.combobox = QtGui.QComboBox()
            items = ["Debut","Fin","Divise"]
            self.combobox.addItems(items)
            self.combobox.setCurrentIndex(items.index("Fin"))
            self.grid.addWidget(self.combobox, 5, 1)

            self.debutLabel = QtGui.QLabel('Debut')
            self.grid.addWidget(self.debutLabel, 6, 0)

            self.debutRepartitionCB = QtGui.QCheckBox()
            self.debutRepartitionCB.setCheckState(QtCore.Qt.CheckState.Checked)
            self.grid.addWidget(self.debutRepartitionCB, 6, 1)

            self.decalageDebutLabel = QtGui.QLabel('Decalage')
            self.grid.addWidget(self.decalageDebutLabel, 7, 0)

            self.decalageDebutDSB = QtGui.QDoubleSpinBox()
            self.decalageDebutDSB.setRange(0., 9999999.)
            self.grid.addWidget(self.decalageDebutDSB, 7, 1)

            self.finLabel = QtGui.QLabel('Fin')
            self.grid.addWidget(self.finLabel, 8, 0)

            self.finRepartitionCB = QtGui.QCheckBox()
            self.finRepartitionCB.setCheckState(QtCore.Qt.CheckState.Checked)
            self.grid.addWidget(self.finRepartitionCB, 8, 1)

            self.decalageFinLabel = QtGui.QLabel('Decalage')
            self.grid.addWidget(self.decalageFinLabel, 9, 0)

            self.decalageFinDSB = QtGui.QDoubleSpinBox()
            self.decalageFinDSB.setRange(0., 9999999.)
            self.grid.addWidget(self.decalageFinDSB, 9, 1)

            groupBox = QtGui.QGroupBox()
            groupBox.setLayout(self.grid)
            self.form = groupBox

            QtCore.QObject.connect(self.dSBLongueur,QtCore.SIGNAL("valueChanged(double)"),self.changerLongueur)
            QtCore.QObject.connect(self.ecartementDSB,QtCore.SIGNAL("valueChanged(double)"),self.changerEcartement)
            QtCore.QObject.connect(self.qteSB,QtCore.SIGNAL("valueChanged(int)"),self.changerQte)
            QtCore.QObject.connect(self.combobox,QtCore.SIGNAL("currentIndexChanged(int)"),self.afficherResultats)
            self.changerLongueur()

        def recupererDonnees(self):
            self.sel = FreeCADGui.Selection.getSelection()
            if self.sel:
                self.longueur = self.sel[0].Shape.Length
            else:
                self.longueur = self.dSBLongueur.value()
            self.ecartementRegulier = self.ecartementDSB.value()
            self.qteEcartement = self.qteSB.value()

            self.objetDebut =  self.debutRepartitionCB.isChecked()
            self.decalageDebut = self.decalageDebutDSB.value()
            self.plEspaceRestant = self.combobox.currentIndex()
            self.objetFin = self.finRepartitionCB.isChecked()
            self.decalageFin = self.decalageFinDSB.value()

        def changerLongueur(self):
            self.recupererDonnees()
            self.qteEcartement = int(math.ceil(self.longueur/self.ecartementRegulier))
            self.afficherResultats()

        def changerEcartement(self):
            self.recupererDonnees()
            self.qteEcartement = int(math.ceil(self.longueur/self.ecartementRegulier))
            self.afficherResultats()

        def changerQte(self):
            self.recupererDonnees()
            self.ecartementRegulier = self.longueur/self.qteEcartement
            self.afficherResultats()

        def afficherResultats(self):
            self.dSBLongueur.blockSignals(True)
            self.dSBLongueur.setValue(self.longueur)
            self.dSBLongueur.blockSignals(False)

            self.ecartementDSB.blockSignals(True)
            self.ecartementDSB.setValue(self.ecartementRegulier)
            self.ecartementDSB.blockSignals(False)


            self.qteSB.blockSignals(True)
            self.qteSB.setValue(self.qteEcartement)
            self.qteSB.blockSignals(False)

            self.espaceRestant = self.longueur - (self.qteEcartement-1) * self.ecartementRegulier
            if round(self.espaceRestant,2) == round(self.ecartementRegulier,2):
                self.espaceRestant = 0.
            if self.combobox.currentIndex() == 2:
                self.infoText.setText( str('Espace restant = 2 x ') + str(round(self.espaceRestant/2,2)) + str(' mm') )
            else:
                self.infoText.setText( str('Espace restant = ') + str(round(self.espaceRestant,2)) + str(' mm') )

        def accept(self):
            self.recupererDonnees()
            distancesListe = []
            if self.objetDebut:
                distancesListe.append(self.decalageDebut)
            if self.plEspaceRestant == 0:
                distancesListe.append(self.espaceRestant)
            if self.plEspaceRestant == 1:
                distancesListe.append(self.ecartementRegulier-self.decalageDebut)
            if self.plEspaceRestant == 2:
                distancesListe.append(self.espaceRestant/2-self.decalageDebut)
            for i in range(self.qteEcartement-2):
                distancesListe.append(self.ecartementRegulier)
            if self.objetFin:
                if self.plEspaceRestant == 0:
                    distancesListe.append(self.ecartementRegulier-self.decalageFin-self.decalageDebut)
                if self.plEspaceRestant == 1:
                    distancesListe.append(self.espaceRestant-self.decalageFin)
                if self.plEspaceRestant == 2:
                    distancesListe.append(self.ecartementRegulier)
                    distancesListe.append((self.espaceRestant/2)-self.decalageFin)
            repartition = Arch.makeAxis(num=len(distancesListe), name="Repartition")
            repartition.Length = 1000.00
            repartition.Distances= distancesListe

            self.sel = FreeCADGui.Selection.getSelection()
            if self.sel:
                edges = DraftGeomUtils.sortEdges(self.sel[0].Shape.Wires[0].Edges)
                vec1 = edges[0].Vertexes[-1].Point.sub(edges[0].Vertexes[0].Point)
                point1 = edges[0].Vertexes[0].Point
                rot = math.degrees(DraftVecUtils.angle(vec1))*-1
                repartition.Placement = App.Placement(App.Vector(point1),App.Rotation(App.Vector(0.0,0.0,1.0),rot))
                FreeCAD.ActiveDocument.recompute()
            else:
                repartition.Placement = App.Placement(App.Vector(0.0,0.0,0.0),App.Rotation(App.Vector(0.0,0.0,1.0),0))

            m = FreeCADGui.getMainWindow()
            w = m.findChild(QtGui.QDockWidget,"PartsLibrary")
            if w:
                if w.isVisible():
                    index = w.folder_view.selectedIndexes()[0]
                    path = w.dirmodel.filePath(index)
                    if path.lower().endswith(".stp") or path.lower().endswith(".step") or path.lower().endswith(".brep"):
                        objetRepartit = Part.show(Part.read(path))
                    else:
                        objetRepartit = FreeCADGui.ActiveDocument.mergeProject(path)
                    repartitionStructurel = Arch.makeStructuralSystem([FreeCAD.ActiveDocument.Objects[-1],],[repartition,], name="RepartitionStructurelle")
            return True

        def reject(self):
            return True

        def getStandardButtons(self):
            return int(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel)


    panel=_RepartitionTaskPanel()
    FreeCADGui.Control.showDialog(panel)

## Liens

-   Vidéo [Macro en action](https://www.youtube.com/watch?v=jfDTkH9-I5Q)
-   [Macro_PartsLibrary](Macro_PartsLibrary.md) Librairie FreeCAD
-   Github [Macro wood galaxy](https://github.com/wood-galaxy/FreeCAD-scripts)



---
⏵ [documentation index](../README.md) > Macro Arch Axis System Repartition/fr
