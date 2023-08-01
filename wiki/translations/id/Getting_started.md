# Getting started/id
## Pendahuluan


<div class="mw-translate-fuzzy">

FreeCAD adalah aplikasi parametrik modeling CAD/CAE. FreeCAD masih dalam tahap awal pengembang, jadi jangan berharap dapat menggunakannya untuk menghasilkan pekerjaan seperti aplikasi CAD yang telah populer.


</div>


<div class="mw-translate-fuzzy">

Tapi, jika kamu ingin tahu seperti FreeCAD itu dan fitur apa saja yang sedang dikembangkan, Anda dipersilakan untuk mengunduhnya dan mencobanya. Pada saat ini, banyak fungsi yang sudah ada, tapi masih banyak antarmuka pengguna yang belum dibuat. Namun jika kamu tahu sedikit tentang Python, kamu akan mampu menghasilkan dan memodifikasi geometri yang kompleks dengan relatif mudah. Jika tidak, mungkin kamu akan menemukan bahwa FreeCAD masih belum sempurna untukmu. Tapi, bersabarlah, hal ini diharapkan segera berubah.


</div>


<div class="mw-translate-fuzzy">

Dan jika setelah mencoba kamu punya saran, ide atau opini, silahkan dibagi dengan kami di [FreeCAD discussion forum](http://forum.freecadweb.org/index.php)!


</div>

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Which workbench should I choose?](Which_workbench_should_I_choose.md)
-   [Tutorials](Tutorials.md)
-   [Video tutorials](Video_tutorials.md)



## Instalasi


<div class="mw-translate-fuzzy">

Pertama (jika belum) unduh dan instal FreeCAD. Lihat halaman [Download](Download.md) untuk informasi tentang versi terbaru dan updatenya. Terdapat paket instalasi siap pakai untuk Windows (.msi), Ubuntu & Debian (.deb), openSUSE (.rpm) dan Mac OSX. See the [Instal](Installing/id.md) page for information about how to install FreeCAD.


</div>




<div class="mw-translate-fuzzy">

## Explorasi FreeCAD 

![The FreeCAD interface when you start it for the first time. See more [screenshots](images/screenshots.md) here.](Freecad09-empty.jpg )

FreeCAD adalah aplikasi 3D modeling untuk semua kebutuhan, difokuskan pada teknik mesin dan bidang terkait, seperti spesialisasi teknik lain atau arsitektur. Hal ini dijadikan dasar sebagai platform untuk mengembangkan berbagai jenis aplikasi 3D, tetapi juga untuk melakukan tugas-tugas yang sangat spesifik. Untuk tujuan itu, antarmuka dibagi menjadi beberapa [Workbenches](Workbenches.md). Workbenches memungkinkan untuk mengubah isi antarmuka untuk menampilkan semua dan hanya alat yang diperlukan untuk tugas tertentu, atau kelompok tugas.

Antarmuka FreeCAD dapat digambarkan sebagai wadah yang sangat sederhana, dengan menu bar, area tampilan 3D, dan beberapa panel samping untuk menampilkan gambaran isi atau properti obyek. Semua isi dari panel ini dapat diubah tergantung pada workbench.

Ketika kamu mulai FreeCAD untuk pertama kalinya, kamu akan disajikan sebuah workbench \"umum\", yang kita sebut \"complete workbench\". Workbench ini hanya menampilkan alat yang paling matang dari workbenches lainnya. Karena FreeCAD cukup muda dan belum digunakan untuk pekerjaan yang sangat khusus, workbench ini sangat berguna untuk menjadikan FreeCAD lebih mudah. Pada dasarnya, semua alat disini sudah cukup baik untuk menghasilkan geometri.


</div>

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Freecad_default.jpg  style="width:600px;">


</div>


**See a full explanation in [Interface](Interface.md).**


:   1\. The [main view area](main_view_area.md), which can contain different tabbed windows, principally the [3D view](3D_view.md).
:   2\. The [3D view](3D_view.md), showing the geometrical objects in the document.
:   3\. The [tree view](tree_view.md) (part of the [combo view](combo_view.md)), showing the hierarchy and construction history of objects in the document; it can also display the [task panel](task_panel.md) for active commands.
:   4\. The [property editor](property_editor.md) (part of the [combo view](combo_view.md)), which allows viewing and modifying properties of the selected objects.
:   5\. The [selection view](selection_view.md), which indicates the objects or sub-elements of objects (vertices, edges, faces) that are selected.
:   6\. The [report view](report_view.md) (or output window), where messages, warnings and errors are shown.
:   7\. The [Python console](Python_console.md), where all the commands executed are printed, and where you can enter [Python](Python.md) code.
:   8\. The [status bar](status_bar.md), where some messages and tooltips appear.
:   9\. The toolbar area, where the toolbars are docked.
:   10\. The [workbench selector](Std_Workbench.md), where you select the active [workbench](workbenches.md).
:   11\. The [standard menu](Standard_Menu.md), which holds basic operations of the program.

The main concept behind the FreeCAD interface is that it is separated into [workbenches](workbenches.md). A workbench is a collection of tools suited for a specific task, such as working with [meshes](Mesh_Workbench.md), or drawing [2D objects](Draft_Workbench.md), or [constrained sketches](Sketcher_Workbench.md). You can switch the current workbench with the [workbench selector](Std_Workbench.md). You can [customize](Interface_Customization.md) the tools included in each workbench, add tools from other workbenches or even self-created tools, that we call [macros](macros.md). Widely used starting points are the [PartDesign Workbench](PartDesign_Workbench.md) and [Part Workbench](Part_Workbench.md).

When you start FreeCAD for the first time, you are presented with the Start page. Here is what it looks like for version 0.19:

<img alt="" src=images/Start_center_0.19_screenshot.png  style="width:600px;">

The Start page allows you to quickly jump to one of the most common workbenches, open one of the recent files, or see the latest news from the FreeCAD world. You can change the default workbench in the [preferences](Preferences_Editor.md).



### Navigasi di Area 3D 


<div class="mw-translate-fuzzy">

FreeCAD memiliki tiga [mode navigasi](Mouse_Model/id.md) berbeda yang tersedia, yang dapat diatur dalam dialog pengaturan preferensi atau diubah dengan mengklik kanan dalam tampilan 3D. Untuk informasi lengkap tentang mode, lihat [Mouse Model](Mouse_Model/id.md) page. Untuk mode default (\"CAD Navigation\"), perintah adalah sebagai berikut,


</div>


<div class="mw-translate-fuzzy">

Anda juga memiliki beberapa pandangan(view) yang tersedia (tampak atas, tampak depan, dll) yang tersedia di menu View dan pada toolbar View, dan dengan cara jalan pintas numerik ({{KEY | 1}}, {{KEY | 2}}, dll. .)


</div>

## First steps with FreeCAD 

FreeCAD\'s focus is to allow you to make high-precision 3D models, to keep tight control over those models (being able to go back into modelling history and change parameters), and eventually to build those models (via 3D printing, CNC machining or even construction worksite). It is therefore very different from some other 3D applications made for other purposes, such as animation film or gaming. Its learning curve can be steep, especially if this is your first contact with 3D modeling. If you are stuck at some point, don\'t forget that the friendly community of users on the [FreeCAD forum](http://forum.freecadweb.org/index.php) might be able to get you out in no time.

The workbench you will start using in FreeCAD depends on the type of job you need to do: If you are going to work on mechanical models, or more generally any small-scale objects, you\'ll probably want to try the [PartDesign Workbench](PartDesign_Workbench.md). If you will work in 2D, then switch to the [Draft Workbench](Draft_Workbench.md), or the [Sketcher Workbench](Sketcher_Workbench.md) if you need constraints. If you want to do BIM, launch the [Arch Workbench](Arch_Workbench.md). And if you come from the OpenSCAD world, try the [OpenSCAD Workbench](OpenSCAD_Workbench.md). There are also many community-developed [external workbenches](External_workbenches.md) available.

You can switch workbenches at any time, and also [customize](Interface_Customization.md) your favorite workbench to add tools from other workbenches.

## Working with the PartDesign and Sketcher workbenches 

The [PartDesign Workbench](PartDesign_Workbench.md) is made to build complex objects, starting from simple shapes, and adding or removing pieces (called \"features\"), until you get to your final object. All the features you applied during the modelling process are stored in a separate view called the [tree view](Document_structure.md), which also contains the other objects in your document. You can think of a PartDesign object as a succession of operations, each one applied to the result of the preceding one, forming one big chain. In the tree view, you see your final object, but you can expand it and retrieve all preceding states, and change any of their parameter, which automatically updates the final object.

The PartDesign workbench makes heavy use of another workbench, the [Sketcher Workbench](Sketcher_Workbench.md). The sketcher allows you to draw 2D shapes, which are defined by applying Constraints to the 2D shape. For example, you might draw a rectangle and set the size of a side by applying a length constraint to one of the sides. That side then cannot be resized anymore (unless the constraint is changed).

Those 2D shapes made with the sketcher are used a lot in the PartDesign workbench, for example to create 3D volumes, or to draw areas on the faces of your object that will then be hollowed from its main volume. This is a typical PartDesign workflow:

1.  Create a new sketch
2.  Draw a closed shape (make sure all points are joined)
3.  Close the sketch
4.  Expand the sketch into a 3D solid by using the pad tool
5.  Select one face of the solid
6.  Create a second sketch (this time it will be drawn on the selected face)
7.  Draw a closed shape
8.  Close the sketch
9.  Create a pocket from the second sketch, on the first object

Which gives you an object like this:

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

At any moment, you can select the original sketches and modify them, or change the extrusion parameters of the pad or pocket operations, which will update the final object.

## Working with the Draft and Arch workbenches 

The [Draft Workbench](Draft_Workbench.md) and [Arch Workbench](Arch_Workbench.md) behave a bit differently than the other workbenches above, although they follow the same rules, which are common to all of FreeCAD. In short, while the Sketcher and PartDesign are made primarily to design single pieces, Draft and Arch are made to ease your work when working with several, simpler objects.

The [Draft Workbench](Draft_Workbench.md) offers you 2D tools somewhat similar to what you can find in traditional 2D CAD applications such as [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). However, 2D drafting being far away from the scope of FreeCAD, don\'t expect to find there the full array of tools that these dedicated applications offer. Most of the Draft tools work not only in a 2D plane but also in the full 3D space, and benefit from special helper systems such as [Work planes](Draft_SelectPlane.md) and [object snapping](Draft_Snap.md).

The [Arch Workbench](Arch_Workbench.md) adds [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) tools to FreeCAD, allowing you to build architectural models with parametric objects. The Arch workbench relies extensively on other modules such as Draft and Sketcher. All the Draft tools are also present in the Arch workbench, and most Arch tools make use of the Draft helper systems.

A typical workflow with Arch and Draft workbenches might be:

1.  Draw a couple of lines with the Draft Line tool
2.  Select each line and press the Wall tool to build a wall on each of them
3.  Join the walls by selecting them and pressing the Arch Add tool
4.  Create a floor object, and move your walls in it from the Tree view
5.  Create a building object, and move your floor in it from the Tree view
6.  Create a window by clicking the Window tool, select a preset in its panel, then click on a face of a wall
7.  Add dimensions by first setting the working plane if necessary, then using the Draft Dimension tool

Which will give you this:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">

More on the [Tutorials](Tutorials.md) page.




<div class="mw-translate-fuzzy">

## [Scripting](Scripting.md)

Dan terakhir, satu dari banyak fitur yang paling handal di FreeCAD adalah [scripting](Scripting/id.md) . Dari integrasi konsol python (atau dari eksternal skrip python yang lain), kamu dapat mengakses ke hampir semua bagian dari FreeCAD, membuat atau modifikasi geometri, memodifikasi representasi dari objek - objek dalam tampilan 3D atau akses dan memodifikasi antarmuka FreeCAD. Python scripting juga dapat digunakan dalam [macro](Macros/id.md), yang menyediakan metode yang mudah untuk membuat perintah sesuai keinginkan kita.


</div>

FreeCAD, as an open source software, offers the possibility to supplement its workbenches with addons.

The [Addon](Addon.md) principle is based on the development of a workbench complement. Any user can develop a function that he or she deems to be missing for her/his own needs or, ultimately, for the community. With the forum, the user can request an opinion, help on the forum. It can share, or not, the object of its development according to copyright rules to define. Free to her/him. To develop, the user has available [scripting](scripting.md) functions.

There are two types of addons:

1.  [Macros](Macros.md): short snippets of Python code that provide a new tool or functionality. Macros usually start as a way to simplify or automate the task of drawing or editing a particular object. If many of these macros are collected inside a directory, the entire directory may be distributed as a new workbench.
2.  [External workbenches](External_workbenches.md): collections of tools programmed in Python or C++ that extend FreeCAD in an important way. If a workbench is sufficiently developed and is well documented, it may be included as one of the base workbenches in FreeCAD. Under [External workbenches](External_workbenches.md), you\'ll find the principle and a list of existing library.

## Scripting 

And finally, one of the most powerful features of FreeCAD is the [scripting](scripting.md) environment. From the integrated python console (or from any other external Python script), you can gain access to almost any part of FreeCAD, create or modify geometry, modify the representation of those objects in the 3D scene or access and modify the FreeCAD interface. Python scripting can also be used in [macros](macros.md), which provide an easy method to create custom commands.




<div class="mw-translate-fuzzy">

## Apa yang baru 


</div>


<div class="mw-translate-fuzzy">

-   [Version 0.17 Release notes](Release_notes_0.17.md) : Lihat apa yang baru di rilis 0.17
-   [Version 0.16 Release notes](Release_notes_0.16.md) : Lihat apa yang baru di rilis 0.16
-   [Version 0.15 Release notes](Release_notes_0.15.md) : Lihat apa yang baru di rilis 0.15
-   [Version 0.14 Release notes](Release_notes_0.14.md) : Lihat apa yang baru di rilis 0.14
-   [Version 0.13 Release notes](Release_notes_0.13.md) : Lihat apa yang baru di rilis 0.13
-   [Version 0.12 Release notes](Release_notes_0.12.md) : Lihat apa yang baru di rilis 0.12
-   [Version 0.11 Release notes](Release_notes_0.11.md) : Lihat apa yang baru di rilis 0.11


</div>


<div class="mw-translate-fuzzy">


{{docnav/id|Install on Mac/id|Mouse Model/id}}


</div>



---
⏵ [documentation index](../README.md) > Getting started/id
