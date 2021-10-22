# Raytracing Workbench/ro
**The Raytracing workbench is essentially obsolete. New development is happening in the [https://github.com/FreeCAD/FreeCAD-render Render Workbench], which is intended as its replacement. This workbench is fully programmed in Python so it is much easier to extend.

Nevertheless, the information in this page is generally useful for the new workbench, as both modules work basically in the same way.
**

<img alt="Raytracing workbench icon" src=images/Workbench_Raytracing.svg  style="width:128px;">

## Introducere

Atelierul de Randare [Raytracing Workbench](Raytracing_Workbench.md)

este folosit pentru a genera imagini fotorealiste ale modelelor dvs., făcându-le  o randare exterioară.


{{TOCright}}

The <img alt="" src=images/Workbench_Raytracing.svg  style="width:24px;"> [Raytracing Workbench](Raytracing_Workbench.md) is used to generate photorealistic images of your models by processing them with an external renderer.

Atelierul de Randare funcționează împreună cu modulele [templates](Raytracing_templates.md), care sunt fișiere de proiect care definesc o scenă pentru modelul dvs. 3D. Puteți localiza luminile și geometria, cum ar fi avioanele de la sol și conține, de asemenea, suporturi pentru poziția camerei și pentru informațiile materiale ale obiectelor din scenă. Proiectul poate fi apoi exportat într-un fișier gata de redare sau poate fi redat direct în cadrul FreeCAD.

În mod obișnuit, sunt susținute două tipuri de randare: [povray](http://en.wikipedia.org/wiki/POV-Ray) și [luxrender](http://en.wikipedia.org/wiki/LuxRender). Pentru a putea randa direct din FreeCAD, cel puțin unul dintre aceste programe trebuiesc instalate pe sistemul dvs., iar calea trebuie să fie configurată în preferințele FreeCAD Raytracing. Totuși dacă nici un program de randare nu este instalat, veți putea să exportați un fișier scenă care poate fi folosit ulterior.

În prezent, există un nou Atelier Renderer în dezvoltare pentru a sprijini multiple back-end-uri precum Lux Renderer și Yafaray. Informațiile pentru utilizarea versiunii în dezvoltare pot fi vizualizate la[Render\_project](Render_project.md). Pentru a afla starea de dezvoltare a modulului Render căutați în proiectul [Raytracing project](Raytracing_project.md)..

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

## Flux de lucru tipic 

1.  Creați sau deschideți un proiect FreeCAD, adăugați unele obiecte [ Part-based](Part_Workbench.md) (mesh-urile nu sunt acceptate în prezent)
2.  Creați un proiect Raytracing (cu luxrender sau povray)
3.  Selectați obiectele pe care doriți să le adăugați la proiectul raytracing și adăugați-le la proiect cu instrumentul \"Inserați o piesă\"
4.  Exportați sau afișați direct


</div>

<img alt="" src=images/Raytracing_Workbench_workflow.svg  style="width:600px;">



*Workflow of the Raytracing Workbench; atelierul de lucru pregătește un fișier de proiect dintr-un șablon dat și apoi apelează un program extern pentru a produce randarea reală a scenei. Programul de randare extern poate fi folosit independent de FreeCAD.*

## Instrumente

### Instrumente de Proiect 

Acestea sunt instrumentele principale pentru exportul lucrării dvs. 3D la programe de randare externe.

-   <img alt="" src=images/Raytracing_New.png  style="width:32px;"> [New PovRay project](Raytracing_New.md): Inserează un nou proiect PovRay project în document
-   <img alt="" src=images/Raytracing_Lux.png  style="width:32px;"> [New LuxRender project](Raytracing_Lux.md): Inserează un nou proiect LuxRender în document
-   <img alt="" src=images/Raytracing_InsertPart.png  style="width:32px;"> [Insert part](Raytracing_InsertPart.md): Introduceți o imagine a unei părți într-un proiect de proiectare
-   <img alt="" src=images/Raytracing_ResetCamera.png  style="width:32px;"> [Reset camera](Raytracing_ResetCamera.md): Potrivește poziția camerei unui proiect de proiectare la vizualizarea curentă
-   <img alt="" src=images/Raytracing_ExportProject.png  style="width:32px;"> [Export project](Raytracing_ExportProject.md): Exportă un proiect raytracing unui fișier de scenă pentru randarea într-un renderer extern
-   <img alt="" src=images/Raytracing_Render.png  style="width:32px;"> [Render](Raytracing_Render.md): Proiectarea unui proiect de raytracing cu un renderer extern

### Utilități

Acestea sunt instrumente de ajutor pentru a efectua sarcini specifice în mod manual.

-   <img alt="" src=images/Raytracing_Export.png  style="width:32px;"> [Export view to povray](Raytracing_Export.md): Scrieți vizualizarea 3D activă cu camera și tot conținutul acesteia într-un fișier povray
-   <img alt="" src=images/Raytracing_Camera.png  style="width:32px;"> [Export camera to povray](Raytracing_Camera.md): Exportați poziția aparatului foto în vizualizarea 3D activă în format POV-Ray într-un fișier
-   <img alt="" src=images/Raytracing_Part.png  style="width:32px;"> [Export part to povray](Raytracing_Part.md): Scrieți Partea (obiect) selectată ca fișier povray

## Preferințe

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Preferences](Raytracing_Preferences.md): Preferințele disponibile pentru instrumentele Raytracing.

## Tutorials

-   [Basic Raytracing tutorial](Raytracing_tutorial.md)
-   [Intermediate Raytracing tutorial](Tutorial_FreeCAD_POV_ray.md)

### Crearea manuală a unui fișier povray 

Instrumentele utilitare descrise mai sus vă permit să exportați vizualizarea 3D curentă și întregul conținut al acestuia într-un fișier [Povray](http://www.povray.org/). În primul rând, trebuie să încărcați sau să creați datele CAD și să poziționați orientarea 3D în orientarea dorită. Apoi alegeți \"Utilities-\> Export View \...\" din meniul raytracing.

![](images/FreeCAD_Raytracing.jpg )

Vi se va solicita o locație pentru salvarea fișierului \* .pov rezultat. După asta, poți să o deschizi [Povray](http://www.povray.org/) and render: ![](images/Povray.jpg )

Ca de obicei, prin randare poți face poze mari și frumoase: <img alt="" src=images/Scharniergreifer_render.jpg  style="width:800px;">

## Script-Programare 

A se vedea [Raytracing API example](Raytracing_API_example.md) pentru informații asupra scrierii programelor de scene.

## Legături

### POVRay

-   <http://www.spiritone.com/~english/cyclopedia/>
-   <http://www.povray.org/>
-   <http://en.wikipedia.org/wiki/POV-Ray>

### Luxrender

-   <http://www.luxrender.net/>

### Viitoare posibile randări de implementat 

-   <http://www.yafaray.org/>
-   <http://www.mitsuba-renderer.org/>
-   <http://www.kerkythea.net/>
-   <http://www.artofillusion.org/>

## Export către Kerkythea 

Deși exportul direct către fișierul Kerkythea XML-File-Format nu este încă acceptat, puteți să exportați Obiectele ca Fișiere Mesh (.obj) și apoi să le importați în Kerkythea.

-   dacă folosiți Kerkythea pentru Linux, nu uitați să instalați pachetul WINE (necesar pentru Kerkythea pentru Linux)
-   puteți să vă transformați modelele cu ajutorul Atelierul Plase în plase și apoi să le exportați ca fișiere .obj
-   Dacă plasa dvs. la exportare a dus la erori (modificări de normale, găuri \...), vă puteți încerca norocul cu [studio netfabb studio](http://www.netfabb.com/downloadcenter.php?basic=1)

:   Gratuit pentru uz personal, disponibil pentru Windows, Linux și Mac OSX.
:   Dispune de instrumente de reparații standard care vă vor repara modelul în majoritatea cazurilor.

-   un alt program bun pentru analiza / repararea ochiului este [Meshlab](http://sourceforge.net/projects/meshlab/)

:   Open Source, disponibil pentru Windows, Linux și Mac OSX.
:   Dispune de instrumente de reparații standard care vă vor repara modelul în majoritatea cazurilor (găuri de umplere, re-orientare de normale etc.)

-   puteți utiliza \"make compound\" și apoi \"face o singură copie\" sau puteți fuziona solide pentru a le grupa înainte de a converti în plase cu ochiuri
-   nu uitați să setați în Kerkythea un factor de import de 0.001 pentru obj-modeler, deoarece Kerkythea se așteaptă ca fișierul obj să fie în m (dar unitățile standard-scheme în FreeCAD sunt mm)

:   În cadrul ferestrelor Windows 7 Kerkythea pe 64 de biți nu pare să poată salva aceste setări.
:   Așa că nu uitați să faceți acest lucru de fiecare dată când porniți Kerkythea

-   dacă importați mai multe obiecte în Kerkythea, puteți folosi comanda \"File\>Merge\" în Kerkythea

## Sugestii de legături 

-   [Render project](Render_project.md)
-   [Raytracing tutorial](Raytracing_tutorial.md)

These pages refer to the new workbench, programmed in Python, meant to replace the current Raytracing Workbench.

-   [Render Workbench](https://github.com/FreeCAD/FreeCAD-render)
-   [Render Workbench](https://forum.freecadweb.org/viewtopic.php?f=9&t=25933) (announcement only, no discussion)
-   [FreeCAD Renderer Workbench improvements](https://forum.freecadweb.org/viewtopic.php?t=39168)

**Outdated**

These pages refer to a replacement workbench, programmed in C++, proposed around 2012, which was never completed.

-   [Raytracing project](Raytracing_project.md)
-   [Render project](Render_project.md)





{{Raytracing Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Raytracing Workbench/ro
