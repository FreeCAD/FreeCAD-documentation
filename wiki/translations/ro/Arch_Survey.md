---
- GuiCommand:/ro
   Name:Arch Survey
   Name/ro:Arch Survey
   MenuLocation:Arch → Survey
   Workbenches:[Arch](Arch_Workbench/ro.md)
   SeeAlso:[FCInfo (macro)](Macro_FCInfo/ro.md)
---

# Arch Survey/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul survey introduce un mod special de supraveghere, care vă permite să luați rapid măsuri și informații dintr-un model și să transferați aceste informații către alte aplicații. Odată ce vă aflați în modul Survey, faceți clic pe subelementele diferite ale obiectelor 3D, și funcție de selecția dvs, următoarele informații sunt colectate:


</div>

-   Dacă faceți clic pe o margine, obțineți lungimea sa
-   If you click on a vertex, you get its height (coordinate on the Z axis)
-   If you click on a face, you get its area
-   If you double-click anything, therefore select the whole object, you get its volume

Când se colectează o astfel de informație, se întâmplă mai multe lucruri:

-   O etichetă este plasată pe elementul pe care ați făcut clic, care afișează valoarea (cu \"a\" pentru zonă, \"l\" pentru lungime, \"z\" pentru înălțime sau \"v\" pentru volum)
-   The numeric value is copied to the clipboard, so you can paste it in another application
-   A line is printed on the FreeCAD output window. After you exit the survey mode, those lines can be copied and pasted in another application (the values are comma-separated, making it easy to convert to spreadsheet data)
-   The total length or area of the elements you clicked so far is also printed in the output window
-   Each length or area is also recorded in the task dialog

<img alt="" src=images/Arch_Survey_example.jpg  style="width:640px;">

*Imaginea de mai sus arată ce se întâmplă atunci când rulați modul survey.*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/Arch_Survey.png" width=16px> [[Arch Survey]]
**
2.  Click on vertices, edges, faces or double-click to select whole objects
3.  Click outside any geometry (on the background of the 3D view) to remove existing labels, print a total line in the Task dialog, and restart counting lengths and areas from zero
4.  Press **ESC** or the **'''Close'''** button to exit survey mode and remove all the labels.


</div>

## Opţiuni

-   Puteți adăuga o etichetă personalizată la orice linie din caseta de dialog Activare făcând clic pe acea linie, apoi adăugând un text în câmpul de descriere, apoi apăsați pe butonul**set description**.
-   Once you are done, before closing, you can export the contents of the Task dialog by pressing the \"export CSV\" button. The resulting CSV file can then be opened in any spreadsheet application such as Excel or LibreOffice Calc. The values and units will be separated in the resulting CSV file, and the totals are written as SUM() functions.

<img alt="" src=images/Arch_Survey_spreadsheet.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

## Script


</div>


<div class="mw-translate-fuzzy">

Modul Survey nu poate fi folosit direct de la scripturile Python, dar culegerea acelorași informații din oricare dintre obiectele Part selectate [Partși](Part_Workbench.md) este ușor reproductibil cu următorul script:


</div>


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
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Survey/ro
