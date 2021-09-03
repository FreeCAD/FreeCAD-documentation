


{{TutorialInfo/fr
|Topic=Analyse par Éléménts Finis
|Level=Intermédiaire
|Time=30 minutes
|Author=[http://www.freecadweb.org/wiki/index.php?title=User:Berndhahnebach Bernd]
|FCVersion=0.18.15985 ou plus récente
}}

## Introduction

Ce tutoriel est destiné à montrer comment une simple analyse par éléments finis (**FEA**) dans L\'<img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [Atelier FEM](FEM_Workbench/fr.md) est conçu à l\'aide de Python. Le modèle du tutoriel [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D/fr.md) sera utilisé pour cet exemple.

<img alt="" src=images/FEM_example01_pic00.jpg  style="width:700px;">

### Requis

-   La version compatible de FreeCAD comme indiqué dans l\'aperçu du tutoriel.

    :   Utilisez la {{MenuCommand|Aide → À propos de FreeCAD}} pour voir la version de FreeCAD installée.
-   **Remarque importante:** En raison du développement continu de l\'<img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [Atelier FEM](FEM_Workbench/fr.md), il est recommandé d\'utiliser la dernière version de FreeCAD, spécialement pour les analyses FEM écrites en Python.
-   Un atelier FEM fonctionnel. Exécutez l\'analyse [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D/fr.md) pour vérifier cela.

## Commençons

### Nouveau document et la partie à analyser {#nouveau_document_et_la_partie_à_analyser}


```python
# new document
doc = App.newDocument("Scripted_CalculiX_Cantilever3D")

# part
import Part
box_obj = doc.addObject('Part::Box', 'Box')
box_obj.Height = box_obj.Width = 1000
box_obj.Length = 8000

# see how our part looks like
import FreeCADGui
FreeCADGui.ActiveDocument.activeView().viewAxonometric()
FreeCADGui.SendMsgToActiveView("ViewFit")

#
```

### Analysis et l\'analyse des objets {#analysis_et_lanalyse_des_objets}


```python
# let us create some objects

# import to create objects
import ObjectsFem

# analysis
analysis_object = ObjectsFem.makeAnalysis(doc, "Analysis")

# solver (we gone use the well tested CcxTools solver object)
solver_object = ObjectsFem.makeSolverCalculixCcxTools(doc, "CalculiX")
solver_object.GeometricalNonlinearity = 'linear'
solver_object.ThermoMechSteadyState = True
solver_object.MatrixSolverType = 'default'
solver_object.IterationsControlParameterTimeUse = False
analysis_object.addObject(solver_object)

# material
material_object = ObjectsFem.makeMaterialSolid(doc, "SolidMaterial")
mat = material_object.Material
mat['Name'] = "Steel-Generic"
mat['YoungsModulus'] = "210000 MPa"
mat['PoissonRatio'] = "0.30"
mat['Density'] = "7900 kg/m^3"
material_object.Material = mat
analysis_object.addObject(material_object)

# fixed_constraint
fixed_constraint = ObjectsFem.makeConstraintFixed(doc, "FemConstraintFixed")
fixed_constraint.References = [(doc.Box, "Face1")]
analysis_object.addObject(fixed_constraint)

# force_constraint
force_constraint = ObjectsFem.makeConstraintForce(doc, "FemConstraintForce")
force_constraint.References = [(doc.Box, "Face2")]
force_constraint.Force = 9000000.0
force_constraint.Direction = (doc.Box, ["Edge5"])
force_constraint.Reversed = True
analysis_object.addObject(force_constraint)

```


<div class="mw-collapsible mw-collapsed toccolours" style="width:750px ">

### Maillage MEF (manuel) {#maillage_mef_manuel}

Cette section contient le code de maillage MEF. Veuillez l\'agrandir pour afficher le contenu.

**Remarque:** Consultez la section [Information supplémentaire](#Information_Suppl.C3.A9mentaire.md) ci-dessous pour savoir comment créer un script de génération de maillage avec GMSH ou objet maillé Netgen.


<div class="mw-collapsible-content">


```python
# mesh
import Fem
femmesh = Fem.FemMesh()

# nodes
femmesh.addNode(8000.0, 1000.0, 0.0, 1)
femmesh.addNode(8000.0, 1000.0, 1000.0, 2)
femmesh.addNode(8000.0, 0.0, 0.0, 3)
femmesh.addNode(8000.0, 0.0, 1000.0, 4)
femmesh.addNode(0.0, 1000.0, 0.0, 5)
femmesh.addNode(0.0, 1000.0, 1000.0, 6)
femmesh.addNode(0.0, 0.0, 0.0, 7)
femmesh.addNode(0.0, 0.0, 1000.0, 8)
femmesh.addNode(728.0, 1000.0, 1000.0, 9)
femmesh.addNode(1456.0, 1000.0, 1000.0, 10)
femmesh.addNode(2184.0, 1000.0, 1000.0, 11)
femmesh.addNode(2912.0, 1000.0, 1000.0, 12)
femmesh.addNode(3640.0, 1000.0, 1000.0, 13)
femmesh.addNode(4368.0, 1000.0, 1000.0, 14)
femmesh.addNode(5096.0, 1000.0, 1000.0, 15)
femmesh.addNode(5824.0, 1000.0, 1000.0, 16)
femmesh.addNode(6552.0, 1000.0, 1000.0, 17)
femmesh.addNode(7280.0, 1000.0, 1000.0, 18)
femmesh.addNode(728.0, 0.0, 1000.0, 19)
femmesh.addNode(1456.0, 0.0, 1000.0, 20)
femmesh.addNode(2184.0, 0.0, 1000.0, 21)
femmesh.addNode(2912.0, 0.0, 1000.0, 22)
femmesh.addNode(3640.0, 0.0, 1000.0, 23)
femmesh.addNode(4368.0, 0.0, 1000.0, 24)
femmesh.addNode(5096.0, 0.0, 1000.0, 25)
femmesh.addNode(5824.0, 0.0, 1000.0, 26)
femmesh.addNode(6552.0, 0.0, 1000.0, 27)
femmesh.addNode(7280.0, 0.0, 1000.0, 28)
femmesh.addNode(728.0, 1000.0, 0.0, 29)
femmesh.addNode(1456.0, 1000.0, 0.0, 30)
femmesh.addNode(2184.0, 1000.0, 0.0, 31)
femmesh.addNode(2912.0, 1000.0, 0.0, 32)
femmesh.addNode(3640.0, 1000.0, 0.0, 33)
femmesh.addNode(4368.0, 1000.0, 0.0, 34)
femmesh.addNode(5096.0, 1000.0, 0.0, 35)
femmesh.addNode(5824.0, 1000.0, 0.0, 36)
femmesh.addNode(6552.0, 1000.0, 0.0, 37)
femmesh.addNode(7280.0, 1000.0, 0.0, 38)
femmesh.addNode(728.0, 0.0, 0.0, 39)
femmesh.addNode(1456.0, 0.0, 0.0, 40)
femmesh.addNode(2184.0, 0.0, 0.0, 41)
femmesh.addNode(2912.0, 0.0, 0.0, 42)
femmesh.addNode(3640.0, 0.0, 0.0, 43)
femmesh.addNode(4368.0, 0.0, 0.0, 44)
femmesh.addNode(5096.0, 0.0, 0.0, 45)
femmesh.addNode(5824.0, 0.0, 0.0, 46)
femmesh.addNode(6552.0, 0.0, 0.0, 47)
femmesh.addNode(7280.0, 0.0, 0.0, 48)
femmesh.addNode(8000.0, 500.0, 500.0, 49)
femmesh.addNode(0.0, 500.0, 500.0, 50)
femmesh.addNode(4731.99999977, 500.000001086, 499.999998599, 51)
femmesh.addNode(0.0, 500.0, 1000.0, 52)
femmesh.addNode(364.0, 1000.0, 1000.0, 53)
femmesh.addNode(1092.0, 1000.0, 1000.0, 54)
femmesh.addNode(1820.0, 1000.0, 1000.0, 55)
femmesh.addNode(2548.0, 1000.0, 1000.0, 56)
femmesh.addNode(3276.0, 1000.0, 1000.0, 57)
femmesh.addNode(4004.0, 1000.0, 1000.0, 58)
femmesh.addNode(4732.0, 1000.0, 1000.0, 59)
femmesh.addNode(5460.0, 1000.0, 1000.0, 60)
femmesh.addNode(6188.0, 1000.0, 1000.0, 61)
femmesh.addNode(6916.0, 1000.0, 1000.0, 62)
femmesh.addNode(7640.0, 1000.0, 1000.0, 63)
femmesh.addNode(8000.0, 500.0, 1000.0, 64)
femmesh.addNode(364.0, 0.0, 1000.0, 65)
femmesh.addNode(1092.0, 0.0, 1000.0, 66)
femmesh.addNode(1820.0, 0.0, 1000.0, 67)
femmesh.addNode(2548.0, 0.0, 1000.0, 68)
femmesh.addNode(3276.0, 0.0, 1000.0, 69)
femmesh.addNode(4004.0, 0.0, 1000.0, 70)
femmesh.addNode(4732.0, 0.0, 1000.0, 71)
femmesh.addNode(5460.0, 0.0, 1000.0, 72)
femmesh.addNode(6188.0, 0.0, 1000.0, 73)
femmesh.addNode(6916.0, 0.0, 1000.0, 74)
femmesh.addNode(7640.0, 0.0, 1000.0, 75)
femmesh.addNode(0.0, 500.0, 0.0, 76)
femmesh.addNode(364.0, 1000.0, 0.0, 77)
femmesh.addNode(1092.0, 1000.0, 0.0, 78)
femmesh.addNode(1820.0, 1000.0, 0.0, 79)
femmesh.addNode(2548.0, 1000.0, 0.0, 80)
femmesh.addNode(3276.0, 1000.0, 0.0, 81)
femmesh.addNode(4004.0, 1000.0, 0.0, 82)
femmesh.addNode(4732.0, 1000.0, 0.0, 83)
femmesh.addNode(5460.0, 1000.0, 0.0, 84)
femmesh.addNode(6188.0, 1000.0, 0.0, 85)
femmesh.addNode(6916.0, 1000.0, 0.0, 86)
femmesh.addNode(7640.0, 1000.0, 0.0, 87)
femmesh.addNode(8000.0, 500.0, 0.0, 88)
femmesh.addNode(364.0, 0.0, 0.0, 89)
femmesh.addNode(1092.0, 0.0, 0.0, 90)
femmesh.addNode(1820.0, 0.0, 0.0, 91)
femmesh.addNode(2548.0, 0.0, 0.0, 92)
femmesh.addNode(3276.0, 0.0, 0.0, 93)
femmesh.addNode(4004.0, 0.0, 0.0, 94)
femmesh.addNode(4732.0, 0.0, 0.0, 95)
femmesh.addNode(5460.0, 0.0, 0.0, 96)
femmesh.addNode(6188.0, 0.0, 0.0, 97)
femmesh.addNode(6916.0, 0.0, 0.0, 98)
femmesh.addNode(7640.0, 0.0, 0.0, 99)
femmesh.addNode(8000.0, 1000.0, 500.0, 100)
femmesh.addNode(0.0, 1000.0, 500.0, 101)
femmesh.addNode(8000.0, 0.0, 500.0, 102)
femmesh.addNode(0.0, 0.0, 500.0, 103)
femmesh.addNode(364.0, 500.0, 1000.0, 104)
femmesh.addNode(728.0, 500.0, 1000.0, 105)
femmesh.addNode(1092.0, 500.0, 1000.0, 106)
femmesh.addNode(1456.0, 500.0, 1000.0, 107)
femmesh.addNode(1820.0, 500.0, 1000.0, 108)
femmesh.addNode(2184.0, 500.0, 1000.0, 109)
femmesh.addNode(2548.0, 500.0, 1000.0, 110)
femmesh.addNode(3276.0, 500.0, 1000.0, 111)
femmesh.addNode(3640.0, 500.0, 1000.0, 112)
femmesh.addNode(4004.0, 500.0, 1000.0, 113)
femmesh.addNode(4368.0, 500.0, 1000.0, 114)
femmesh.addNode(4732.0, 500.0, 1000.0, 115)
femmesh.addNode(5096.0, 500.0, 1000.0, 116)
femmesh.addNode(5460.0, 500.0, 1000.0, 117)
femmesh.addNode(5824.0, 500.0, 1000.0, 118)
femmesh.addNode(6188.0, 500.0, 1000.0, 119)
femmesh.addNode(6552.0, 500.0, 1000.0, 120)
femmesh.addNode(6916.0, 500.0, 1000.0, 121)
femmesh.addNode(7640.0, 500.0, 1000.0, 122)
femmesh.addNode(2912.0, 500.0, 1000.0, 123)
femmesh.addNode(7280.0, 500.0, 1000.0, 124)
femmesh.addNode(364.0, 500.0, 0.0, 125)
femmesh.addNode(1092.0, 500.0, 0.0, 126)
femmesh.addNode(728.0, 500.0, 0.0, 127)
femmesh.addNode(1820.0, 500.0, 0.0, 128)
femmesh.addNode(1456.0, 500.0, 0.0, 129)
femmesh.addNode(2548.0, 500.0, 0.0, 130)
femmesh.addNode(2184.0, 500.0, 0.0, 131)
femmesh.addNode(3640.0, 500.0, 0.0, 132)
femmesh.addNode(3276.0, 500.0, 0.0, 133)
femmesh.addNode(4004.0, 500.0, 0.0, 134)
femmesh.addNode(5096.0, 500.0, 0.0, 135)
femmesh.addNode(4732.0, 500.0, 0.0, 136)
femmesh.addNode(5460.0, 500.0, 0.0, 137)
femmesh.addNode(6188.0, 500.0, 0.0, 138)
femmesh.addNode(5824.0, 500.0, 0.0, 139)
femmesh.addNode(6916.0, 500.0, 0.0, 140)
femmesh.addNode(6552.0, 500.0, 0.0, 141)
femmesh.addNode(7640.0, 500.0, 0.0, 142)
femmesh.addNode(2912.0, 500.0, 0.0, 143)
femmesh.addNode(4368.0, 500.0, 0.0, 144)
femmesh.addNode(7280.0, 500.0, 0.0, 145)
femmesh.addNode(364.0, 1000.0, 500.0, 146)
femmesh.addNode(728.0, 1000.0, 500.0, 147)
femmesh.addNode(1092.0, 1000.0, 500.0, 148)
femmesh.addNode(1456.0, 1000.0, 500.0, 149)
femmesh.addNode(1820.0, 1000.0, 500.0, 150)
femmesh.addNode(2184.0, 1000.0, 500.0, 151)
femmesh.addNode(2548.0, 1000.0, 500.0, 152)
femmesh.addNode(3276.0, 1000.0, 500.0, 153)
femmesh.addNode(3640.0, 1000.0, 500.0, 154)
femmesh.addNode(4004.0, 1000.0, 500.0, 155)
femmesh.addNode(4368.0, 1000.0, 500.0, 156)
femmesh.addNode(4732.0, 1000.0, 500.0, 157)
femmesh.addNode(5096.0, 1000.0, 500.0, 158)
femmesh.addNode(5460.0, 1000.0, 500.0, 159)
femmesh.addNode(5824.0, 1000.0, 500.0, 160)
femmesh.addNode(6188.0, 1000.0, 500.0, 161)
femmesh.addNode(6552.0, 1000.0, 500.0, 162)
femmesh.addNode(6916.0, 1000.0, 500.0, 163)
femmesh.addNode(7640.0, 1000.0, 500.0, 164)
femmesh.addNode(2912.0, 1000.0, 500.0, 165)
femmesh.addNode(7280.0, 1000.0, 500.0, 166)
femmesh.addNode(364.0, 0.0, 500.0, 167)
femmesh.addNode(1092.0, 0.0, 500.0, 168)
femmesh.addNode(728.0, 0.0, 500.0, 169)
femmesh.addNode(1820.0, 0.0, 500.0, 170)
femmesh.addNode(1456.0, 0.0, 500.0, 171)
femmesh.addNode(2548.0, 0.0, 500.0, 172)
femmesh.addNode(2184.0, 0.0, 500.0, 173)
femmesh.addNode(3640.0, 0.0, 500.0, 174)
femmesh.addNode(3276.0, 0.0, 500.0, 175)
femmesh.addNode(4004.0, 0.0, 500.0, 176)
femmesh.addNode(5096.0, 0.0, 500.0, 177)
femmesh.addNode(4732.0, 0.0, 500.0, 178)
femmesh.addNode(5460.0, 0.0, 500.0, 179)
femmesh.addNode(6188.0, 0.0, 500.0, 180)
femmesh.addNode(5824.0, 0.0, 500.0, 181)
femmesh.addNode(6916.0, 0.0, 500.0, 182)
femmesh.addNode(6552.0, 0.0, 500.0, 183)
femmesh.addNode(7640.0, 0.0, 500.0, 184)
femmesh.addNode(2912.0, 0.0, 500.0, 185)
femmesh.addNode(4368.0, 0.0, 500.0, 186)
femmesh.addNode(7280.0, 0.0, 500.0, 187)
femmesh.addNode(8000.0, 250.0, 250.0, 188)
femmesh.addNode(8000.0, 250.0, 750.0, 189)
femmesh.addNode(8000.0, 750.0, 750.0, 190)
femmesh.addNode(8000.0, 750.0, 250.0, 191)
femmesh.addNode(0.0, 250.0, 750.0, 192)
femmesh.addNode(0.0, 250.0, 250.0, 193)
femmesh.addNode(0.0, 750.0, 250.0, 194)
femmesh.addNode(0.0, 750.0, 750.0, 195)
femmesh.addNode(1456.0, 500.0, 500.0, 196)
femmesh.addNode(6552.0, 500.0, 500.0, 197)
femmesh.addNode(6916.0, 500.0, 500.0, 198)
femmesh.addNode(2184.0, 500.0, 500.0, 199)
femmesh.addNode(2548.0, 500.0, 500.0, 200)
femmesh.addNode(2912.0, 500.0, 500.0, 201)
femmesh.addNode(1820.0, 500.0, 500.0, 202)
femmesh.addNode(7640.0, 750.0, 250.0, 203)
femmesh.addNode(7640.0, 750.0, 750.0, 204)
femmesh.addNode(7280.0, 500.0, 500.0, 205)
femmesh.addNode(7640.0, 250.0, 250.0, 206)
femmesh.addNode(5460.0, 500.0, 500.0, 207)
femmesh.addNode(5096.0, 500.0, 500.0, 208)
femmesh.addNode(6188.0, 500.0, 500.0, 209)
femmesh.addNode(5824.0, 500.0, 500.0, 210)
femmesh.addNode(364.0, 750.0, 250.0, 211)
femmesh.addNode(364.0, 750.0, 750.0, 212)
femmesh.addNode(364.0, 250.0, 250.0, 213)
femmesh.addNode(1092.0, 500.0, 500.0, 214)
femmesh.addNode(728.0, 500.0, 500.0, 215)
femmesh.addNode(364.0, 250.0, 750.0, 216)
femmesh.addNode(4549.99999989, 250.000000543, 249.9999993, 217)
femmesh.addNode(4549.99999989, 750.000000543, 249.9999993, 218)
femmesh.addNode(4549.99999989, 750.000000543, 749.9999993, 219)
femmesh.addNode(4368.0, 500.0, 500.0, 220)
femmesh.addNode(4549.99999989, 250.000000543, 749.9999993, 221)
femmesh.addNode(4913.99999989, 250.000000543, 749.9999993, 222)
femmesh.addNode(4913.99999989, 750.000000543, 749.9999993, 223)
femmesh.addNode(3276.0, 500.0, 500.0, 224)
femmesh.addNode(3640.0, 500.0, 500.0, 225)
femmesh.addNode(4004.0, 500.0, 500.0, 226)
femmesh.addNode(4913.99999989, 750.000000543, 249.9999993, 227)
femmesh.addNode(4913.99999989, 250.000000543, 249.9999993, 228)

# elements
femmesh.addVolume([40, 19, 10, 20, 168, 106, 196, 171, 66, 107], 149)
femmesh.addVolume([10, 31, 30, 40, 150, 79, 149, 196, 128, 129], 150)
femmesh.addVolume([38, 17, 18, 47, 163, 62, 166, 140, 197, 198], 151)
femmesh.addVolume([32, 41, 11, 12, 130, 199, 152, 165, 200, 56], 152)
femmesh.addVolume([12, 32, 41, 42, 165, 130, 200, 201, 143, 92], 153)
femmesh.addVolume([42, 21, 12, 22, 172, 110, 201, 185, 68, 123], 154)
femmesh.addVolume([10, 31, 40, 11, 150, 128, 196, 55, 151, 202], 155)
femmesh.addVolume([11, 12, 41, 21, 56, 200, 199, 109, 110, 173], 156)
femmesh.addVolume([20, 41, 11, 40, 170, 199, 108, 171, 91, 202], 157)
femmesh.addVolume([20, 41, 21, 11, 170, 173, 67, 108, 199, 109], 158)
femmesh.addVolume([32, 11, 41, 31, 152, 199, 130, 80, 151, 131], 159)
femmesh.addVolume([11, 10, 20, 40, 55, 107, 108, 202, 196, 171], 160)
femmesh.addVolume([38, 17, 47, 37, 163, 197, 140, 86, 162, 141], 161)
femmesh.addVolume([38, 18, 49, 48, 166, 204, 203, 145, 205, 206], 162)
femmesh.addVolume([46, 15, 45, 36, 207, 208, 96, 139, 159, 137], 163)
femmesh.addVolume([47, 16, 46, 37, 209, 210, 97, 141, 161, 138], 164)
femmesh.addVolume([18, 4, 2, 49, 122, 64, 63, 204, 189, 190], 165)
femmesh.addVolume([18, 17, 27, 47, 62, 120, 121, 198, 197, 183], 166)
femmesh.addVolume([38, 18, 48, 47, 166, 205, 145, 140, 198, 98], 167)
femmesh.addVolume([12, 23, 42, 22, 111, 175, 201, 123, 69, 185], 168)
femmesh.addVolume([26, 47, 27, 17, 180, 183, 73, 119, 197, 120], 169)
femmesh.addVolume([50, 29, 9, 6, 211, 147, 212, 195, 146, 53], 170)
femmesh.addVolume([27, 48, 18, 47, 182, 205, 121, 183, 98, 198], 171)
femmesh.addVolume([8, 7, 39, 50, 103, 89, 167, 192, 193, 213], 172)
femmesh.addVolume([40, 9, 39, 30, 214, 215, 90, 129, 148, 126], 173)
femmesh.addVolume([42, 21, 41, 12, 172, 173, 92, 201, 110, 200], 174)
femmesh.addVolume([50, 9, 29, 39, 212, 147, 211, 213, 215, 127], 175)
femmesh.addVolume([29, 7, 50, 39, 125, 193, 211, 127, 89, 213], 176)
femmesh.addVolume([31, 11, 41, 40, 151, 199, 131, 128, 202, 91], 177)
femmesh.addVolume([47, 16, 37, 17, 209, 161, 141, 197, 61, 162], 178)
femmesh.addVolume([40, 9, 30, 10, 214, 148, 129, 196, 54, 149], 179)
femmesh.addVolume([2, 38, 49, 1, 164, 203, 190, 100, 87, 191], 180)
femmesh.addVolume([2, 38, 18, 49, 164, 166, 63, 190, 203, 204], 181)
femmesh.addVolume([48, 49, 38, 3, 206, 203, 145, 99, 188, 142], 182)
femmesh.addVolume([38, 49, 1, 3, 203, 191, 87, 142, 188, 88], 183)
femmesh.addVolume([49, 4, 3, 48, 189, 102, 188, 206, 184, 99], 184)
femmesh.addVolume([28, 48, 4, 18, 187, 184, 75, 124, 205, 122], 185)
femmesh.addVolume([49, 18, 4, 48, 204, 122, 189, 206, 205, 184], 186)
femmesh.addVolume([7, 50, 5, 29, 193, 194, 76, 125, 211, 77], 187)
femmesh.addVolume([50, 6, 5, 29, 195, 101, 194, 211, 146, 77], 188)
femmesh.addVolume([50, 9, 19, 6, 212, 105, 216, 195, 53, 104], 189)
femmesh.addVolume([50, 19, 9, 39, 216, 105, 212, 213, 169, 215], 190)
femmesh.addVolume([50, 19, 8, 6, 216, 65, 192, 195, 104, 52], 191)
femmesh.addVolume([40, 9, 10, 19, 214, 54, 196, 168, 105, 106], 192)
femmesh.addVolume([51, 44, 34, 14, 217, 144, 218, 219, 220, 156], 193)
femmesh.addVolume([51, 24, 44, 14, 221, 186, 217, 219, 114, 220], 194)
femmesh.addVolume([25, 15, 24, 51, 116, 115, 71, 222, 223, 221], 195)
femmesh.addVolume([43, 12, 32, 13, 224, 165, 133, 225, 57, 153], 196)
femmesh.addVolume([43, 12, 23, 42, 224, 111, 174, 93, 201, 175], 197)
femmesh.addVolume([43, 12, 13, 23, 224, 57, 225, 174, 111, 112], 198)
femmesh.addVolume([43, 12, 42, 32, 224, 201, 93, 133, 165, 143], 199)
femmesh.addVolume([34, 13, 14, 44, 155, 58, 156, 144, 226, 220], 200)
femmesh.addVolume([14, 24, 15, 51, 114, 115, 59, 219, 221, 223], 201)
femmesh.addVolume([23, 24, 14, 44, 70, 114, 113, 176, 186, 220], 202)
femmesh.addVolume([33, 32, 13, 43, 81, 153, 154, 132, 133, 225], 203)
femmesh.addVolume([34, 33, 13, 43, 82, 154, 155, 134, 132, 225], 204)
femmesh.addVolume([35, 14, 15, 51, 157, 59, 158, 227, 219, 223], 205)
femmesh.addVolume([25, 45, 15, 51, 177, 208, 116, 222, 228, 223], 206)
femmesh.addVolume([44, 43, 13, 23, 94, 225, 226, 176, 174, 112], 207)
femmesh.addVolume([35, 34, 14, 51, 83, 156, 157, 227, 218, 219], 208)
femmesh.addVolume([46, 15, 36, 16, 207, 159, 139, 210, 60, 160], 209)
femmesh.addVolume([36, 35, 15, 45, 84, 158, 159, 137, 135, 208], 210)
femmesh.addVolume([37, 36, 16, 46, 85, 160, 161, 138, 139, 210], 211)
femmesh.addVolume([25, 26, 16, 46, 72, 118, 117, 179, 181, 210], 212)
femmesh.addVolume([47, 16, 17, 26, 209, 61, 197, 180, 118, 119], 213)
femmesh.addVolume([47, 16, 26, 46, 209, 118, 180, 97, 210, 181], 214)
femmesh.addVolume([27, 28, 18, 48, 74, 124, 121, 182, 187, 205], 215)
femmesh.addVolume([35, 34, 51, 45, 83, 218, 227, 135, 136, 228], 216)
femmesh.addVolume([13, 14, 44, 23, 58, 220, 226, 112, 113, 176], 217)
femmesh.addVolume([44, 25, 24, 51, 178, 71, 186, 217, 222, 221], 218)
femmesh.addVolume([44, 45, 25, 51, 95, 177, 178, 217, 228, 222], 219)
femmesh.addVolume([46, 15, 16, 25, 207, 60, 210, 179, 116, 117], 220)
femmesh.addVolume([46, 15, 25, 45, 207, 116, 179, 96, 208, 177], 221)
femmesh.addVolume([50, 8, 19, 39, 192, 65, 216, 213, 167, 169], 222)
femmesh.addVolume([35, 51, 15, 45, 227, 223, 158, 135, 228, 208], 223)
femmesh.addVolume([34, 44, 43, 13, 144, 94, 134, 155, 226, 225], 224)
femmesh.addVolume([51, 44, 45, 34, 217, 95, 228, 218, 144, 136], 225)
femmesh.addVolume([9, 29, 39, 30, 147, 127, 215, 148, 78, 126], 226)
femmesh.addVolume([40, 9, 19, 39, 214, 105, 168, 90, 215, 169], 227)


# add it to the analysis
femmesh_obj = doc.addObject('Fem::FemMeshObject', 'Box_Mesh')
femmesh_obj.FemMesh = femmesh
analysis_object.addObject(femmesh_obj)

```


</div>


</div>

### Maillage MEF (gmsh) {#maillage_mef_gmsh}


```python
femmesh_obj = ObjectsFem.makeMeshGmsh(doc, box_obj.Name + "_Mesh")
femmesh_obj.Part = doc.Box

doc.recompute()

from femmesh.gmshtools import GmshTools as gt
gmsh_mesh = gt(femmesh_obj)
error = gmsh_mesh.create_mesh()
print(error)

analysis_object.addObject(femmesh_obj)
```

### Maillage MEF (netgen) {#maillage_mef_netgen}


```python
mesh = doc.addObject('Fem::FemMeshShapeNetgenObject', 'FEMMeshNetgen')
mesh.Shape = doc.Box
mesh.MaxSize = 1000
mesh.Fineness = "Moderate"
mesh.Optimize = True
mesh.SecondOrder = True
doc.recompute()

analysis_object.addObject(mesh)
```

### Recalculer


```python
# recompute
doc.recompute()

###
```

## Lancement de l\'analyse {#lancement_de_lanalyse}

Pour exécuter l\'analyse à l\'aide de Python, une instance de la `ccxtools` classe de module `FemToolsCcx` doit être créée, nous avons deux choix lors de l\'exécution de l\'analyse:

1.  Exécutez tous les processus en même temps (voir la section [\"Tout en un\"](#Tout_en_une_fois.md) ci-dessous)
2.  Exécuter les processus les uns après les autres (voir la section [\"Pas à pas\"](#Pas_.C3.A0_pas.md) ci-dessous)

S\'il n\'y a qu\'une seule analyse dans le document et un seul solveur dans l\'analyse, aucun objet ne doit être transmis à `fea init`. La méthode `init` de la classe `fea` activera l\'analyse **si l\'interface graphique est active**.

L\'activation d\'une analyse à l\'aide de Python fonctionne comme suit:


```python
# activating analysis
import FemGui
FemGui.setActiveAnalysis(doc.Analysis)

###
```

#### Tout en une fois {#tout_en_une_fois}


```python
# run the analysis all in one
from femtools import ccxtools
fea = ccxtools.FemToolsCcx()
fea.purge_results()
fea.run()

###
```

#### Pas à pas {#pas_à_pas}


```python
# run the analysis step by step
from femtools import ccxtools
fea = ccxtools.FemToolsCcx()
fea.update_objects()
fea.setup_working_dir()
fea.setup_ccx()
message = fea.check_prerequisites()
if not message:
    fea.purge_results()
    fea.write_inp_file()
    # on error at inp file writing, the inp file path "" was returned (even if the file was written)
    # if we would write the inp file anyway, we need to again set it manually
    # fea.inp_file_name = '/tmp/FEMWB/FEMMeshGmsh.inp'
    fea.ccx_run()
    fea.load_results()
else:
    FreeCAD.Console.PrintError("Houston, we have a problem! {}\n".format(message))  # in report view
    print("Houston, we have a problem! {}\n".format(message))  # in python console

###
```

## Montrer les résultats {#montrer_les_résultats}


```python
# show some results
for m in analysis_object.Group:
    if m.isDerivedFrom('Fem::FemResultObject'):
        result_object = m
        break

femmesh_obj.ViewObject.setNodeDisplacementByVectors(result_object.NodeNumbers, result_object.DisplacementVectors)
femmesh_obj.ViewObject.applyDisplacement(10)

###
```

### Informations supplémentaires {#informations_supplémentaires}

#### Script des objets de maillage MEF {#script_des_objets_de_maillage_mef}

##### Netgen

Le scriptage de l\'objet maillé Netgen a été tenté dans le [\"Etude MEF paramétré\"](http://forum.freecadweb.org/viewtopic.php?f=18&t=16944#p134519) (fil du sous-forum FreeCAD FEM) mais a certaines limites.

##### GMSH

Au contraire, l\'objet maillé GMSH prend entièrement en charge les scripts Python. Voir les messages de forum suivants:

-   <https://forum.freecadweb.org/viewtopic.php?f=22&t=42922#p365042>
-   sujet du forum <http://forum.freecadweb.org/viewtopic.php?f=18&t=20087>

#### Script d\'analyses multiple {#script_danalyses_multiple}

Voir la publication du forum: <http://forum.freecadweb.org/viewtopic.php?f=18&t=19549#p151385>

#### Script de résultats {#script_de_résultats}

###### Objet de résultat standard de FreeCAD {#objet_de_résultat_standard_de_freecad}

Voir les publications du forum :

-   <https://forum.freecadweb.org/viewtopic.php?f=18&t=34048&p=289519#p289519> → facteur d\'échelle dans l\'objet résultat standard
-   <http://forum.freecadweb.org/viewtopic.php?f=18&t=4677&start=20#p148982>
-   <http://forum.freecadweb.org/viewtopic.php?f=18&t=4677&start=30#> p149043
-   <http://forum.freecadweb.org/viewtopic.php?t=18415#p144028>
-   <https://forum.freecadweb.org/viewtopic.php?f=18&t=31123&p=258761#p258761> → colorier un seul élément
-   <https://forum.freecadweb.org/viewtopic.php?f=18&t=41951&p=357687#p357685> → réinitialiser tout le maillage des résultats, afficher l\'amplitude de déplacement colorée

##### Objet de résultat Vtk {#objet_de_résultat_vtk}

Voir les messages du forum:

-   <https://forum.freecadweb.org/viewtopic.php?f=18&t=47227#p405406>

#### Mode console {#mode_console}

L\'écriture du fichier d\'entrée en mode console FreeCAD (sans interface graphique) peut être effectuée en mode test. Voir ce [post du forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=25852&p=208897#p208897) pertinent pour plus de détails et d\'expérimentation.

## Appendice

Amusez-vous! Aussi, si vous avez des commentaires ou des améliorations, n\'hésitez pas à participer sur le [sous-forum FreeCAD FEM](https://forum.freecadweb.org/viewforum.php?f=18).


{{Tutorials navi

}} {{FEM Tools navi}}  

[Category:Python Code{{\#translation:}}](Category:Python_Code.md)
