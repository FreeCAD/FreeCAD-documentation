# WebTools Sketchfab/ro
---
- GuiCommand   *   Name   *WebTools Sketchfab   MenuLocation   *WebTools → Sketchfab   |Workbenches   *[[WebTools Workbench   WebTools]]|Shortcut   *   SeeAlso   *---


</div>

## Descriere

Acest instrument vă permite să exportați sau să faceți upload de obiecte pe contul dvs. [SketchFab](http   *//www.sketchfab.com) account. <small>(v0.17)</small> 

![](images/Sketchfab_exporter.jpg )


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Creați-vă un cont în [SketchFab](http   *//www.sketchfab.com)dacă nu aveți încă. Conturile gratuite sunt suficiente, cele plătite au mai multe funcționalități ca de ex. posibilitatea de a avea șabloane private și dimensiune maximală mai mare la upload
2.  Prepare a model you wish to upload
3.  Click on <img alt="" src=images/WebTools_Sketchfab.png  style="width   *32px;"> from the main toolbar in the [WebTools Workbench](WebTools_Workbench.md)
4.  Fill in the fields. Name and API key are mandatory
5.  Click pe butonul \"Upload\"


</div>

1.  Make yourself an account on [SketchFab](http   *//www.sketchfab.com) if you don\'t have one yet. Free accounts are just fine, paid accounts add more features like the possibility to have private models and bigger maximum upload sizes
2.  Prepare a model you wish to upload
3.  Click on <img alt="" src=images/WebTools_Sketchfab.svg  style="width   *32px;"> from the main toolbar in the [WebTools Workbench](WebTools_Workbench.md)
4.  Fill in the fields. Name and API key are mandatory
5.  Click the \"Upload\" button

## Opţiuni

-   Aveți nevoie de o cheie API Sketchfab pentru acest exportator pentru a vă putea conecta la contul sketchfab. Prin apăsarea butonului \"Obtain\", care va fi direcționat către pagina de setări Sketchfab, unde este cheia dvs. unică pentru contul dvs. Copy the key and paste it in the \"API key\" field in the exporter. This value will be stored by FreeCAD so you only need to do it once
-   The name field is mandatory, the others can be left blank.
-   The exporter proposes several different export formats. The best on for you depends on the kind of model and result you wish to obtain, it is recommended to test what works best for you. Generally, OBJ + MTL will give you a better control over materials, while IV (OpenInventor) will give a result that is more similar to what you see in the FreeCAD 3D view.
-   Once your model is uploaded, Sketchfab offers a pretty advanced interface where you can further configure materials, lighting and environment.
-   When you press the \"Upload button\", after the upload finished, if everything went well, the button will turn into a \"View your model online\" button, which, when clicked, will take you directly to the model page on Sketchfab.
-   Unele formate, cum ar fi OBJ, sun interpretat diferit de Sketchfab și FreeCAD. FreeCAD consideră axa Z să fie orientată în sus, în timp ce Sketchfab consideră că aceasta indică persoana care se află în spatele ecranului. To remedy this, after the upload is finished, the exporter will use the Sketchfab API to rotate the model to its correct position. If this operation fails, you will be warned, but your model will still be correctly uploaded. Ysau îl puteți roti în interfața Sketchfab, apăsând pe săgeata dreapta axa \"X\" din tab-ul de orientare a modelului.



---
![](images/Right_arrow.png) [documentation index](../README.md) > WebTools Sketchfab/ro
