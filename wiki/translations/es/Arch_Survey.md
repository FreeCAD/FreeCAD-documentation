# Arch Survey/es
---
- GuiCommand:   Name: Arch Survey   Workbenches: Arch_Workbench/es   Arch---


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta de encuesta ingresa en un modo de topografía especial, que le permite tomar rápidamente medidas e información de un modelo y transferir esa información a otras aplicaciones. Una vez que esté en modo Encuesta, al hacer clic en diferentes subelementos de objetos 3D, se recopila la siguiente información, en función de lo que haga clic en:


</div>

-   Si haces clic en un borde, obtienes su longitud
-   Si hace clic en un vértice, obtiene su altura (coordenada en el eje Z)
-   Si haces clic en una cara, obtienes su área.
-   Si hace doble clic en cualquier cosa, por lo tanto, selecciona todo el objeto, obtiene su volumen

Cuando se recopila una información de este tipo, suceden varias cosas:

-   A label is placed on top of the element you clicked, that displays the value (with \"a\" for area, \"l\" for length, \"z\" for height, or \"v\" for volume)
-   The numeric value is copied to the clipboard, so you can paste it in another application
-   A line is printed on the FreeCAD output window. After you exit the survey mode, those lines can be copied and pasted in another application (the values are comma-separated, making it easy to convert to spreadsheet data)
-   The total length or area of the elements you clicked so far is also printed in the output window
-   Each length or area is also recorded in the task dialog

<img alt="" src=images/Arch_Survey_example.jpg  style="width:640px;">

*The above image shows what happens when running the survey mode.*

## Usage

1.  Press the **<img src="images/Arch_Survey.svg" width=16px> [Arch Survey](Arch_Survey.md)** button.
2.  Click on vertices, edges, faces or double-click to select whole objects.
3.  Click outside any geometry (on the background of the 3D view) to remove existing labels, print a total line in the Task dialog, and restart counting lengths and areas from zero.
4.  Press **Esc** or the **Close** button to exit survey mode and remove all the labels.

## Options

-   You can add a custom label to any line in the Task dialog by clicking that line, then adding a text in the description field, then press the **set description** button.
-   Once you are done, before closing, you can export the contents of the Task dialog by pressing the \"export CSV\" button. The resulting CSV file can then be opened in any spreadsheet application such as Excel or LibreOffice Calc. The values and units will be separated in the resulting CSV file, and the totals are written as SUM() functions.

<img alt="" src=images/Arch_Survey_spreadsheet.jpg  style="width:640px;">

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Survey tool doesn\'t have a programming interface, but gathering the same information from any selected [Part](Part_Workbench.md)-based object is reproduced with the following script:


```python
import FreeCADGui

selection = FreeCADGui.Selection.getSelectionEx()

for obj in selection:
    for element in obj.SubObjects:
        print("Area: %f", element.Area)
        print("Length: %f", element.Length)
        print("Volume: %f", element.Volume)
        print("Center of Mass: %f", element.CenterOfMass)
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Survey/es
