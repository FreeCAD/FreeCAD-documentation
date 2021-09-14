# Advanced TechDraw Tutorial/fr







{{TutorialInfo
|Topic=Modélisation
|Level=Utilisateur expérimenté
|Author=NormandC
|FCVersion=≥ 0.19.23300
}}

## L\'objectif en bref 

Créez des points, des lignes, des cercles, des arcs, etc\... dans des vues TechDraw et/ou des dessins \"cosmétiques\" entiers avec une précision absolue, adaptée aux outils de cotation dont l\'établi est équipé, pour générer des dessins techniques conformes et détaillés.

## Introduction

Ce tutoriel présente à l\'utilisateur expérimenté une utilisation avancée d\'outils et de techniques existants dans d\'autres ateliers pour étendre les fonctionnalités manquantes dans l\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;">. [atelier TechDraw](TechDraw_Workbench/fr.md). Ce tutoriel n\'est pas un guide complet et exhaustif de l\'atelier TechDraw et de nombreux outils et fonctionnalités ne sont pas couverts. Il devrait contribuer à surmonter les difficultés rencontrées pour citer et enrichir le dessin technique à l\'aide de TechDraw. Ce tutoriel conduira les utilisateurs avancés à travers les étapes nécessaires pour produire des dessins techniques exigeants de la pièce à partir du [Tutoriel d\'introduction PartDesign](Basic_Part_Design_Tutorial/fr.md) en utilisant les outils de dessin de l\'atelier TechDraw.


<div class="mw-translate-fuzzy">

1.  L\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md) (lignes, polylignes, circonférences, arcs, splines, béziers, etc.), en particulier les accrochages, pour créer sur l\'objet des \"points cosmétiques\" réellement précis qui pourront ensuite être utilisés pour le dimensionnement dans TechDraw.
2.  Il est également possible d\'utiliser l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [atelier Sketcher](Sketcher_Workbench/fr.md) comme
    -   générateur de \"base-sketchTD\" (bases de croquis pour TechDraw) en 2D (par exemple, schéma de système, plans d\'étage, élévations, vues de pièces mécaniques ou d\'ensemble etc\...) ou en
    -   utilisant directement les croquis qui ont généré les modèles 3D, ou en
    -   convertissant en esquisse le \"facebinder\" généré avec l\'ébauche obtenue à partir des faces et/ou des sections des modèles 3D.
3.  Pour obtenir des sections particulières (coupes sur différents plans ou axes) à présenter sur la page dans TechDraw (il est conseillé d\'utiliser une copie de l\'objet 3D original), ensuite par la création de plans (même sur différents axes) en utilisant le <img alt="" src=images/Workfeature_workbench_icon.svg  style="width:24px;"> WorkFeatureDev, il est possible de sectionner la copie de l\'objet 3D <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> (***Séparer/exploser*** fonctionnalité dans l\'atelier **Part**) pour obtenir les faces à convertir en esquisse <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:24px;"> (***Draft vers Esquisse*** fonctionnalité dans l\'atelier **Draft**) et ensuite, à travers l\'atelier *\'Sketcher*, les éditer pour les adapter au dessin technique que l\'on souhaite générer dans TechDraw. L\'atelier *WorkFeatureDev* (et la macro **workfeature**) sont pleins de fonctions supplémentaires pratiques qui nous permettent de créer facilement des plans (théoriquement infinis en extension et en quantité) en sélectionnant trois points (sommets) *(rappelez-vous que pour trois points passant, un et un seul plan passe par trois points non alignés un et un seul plan passe par trois points non alignés*) est un axiome géométrique, qui confirme sans aucune ambiguïté (!) la validité et l\'importance de l\'outil WorkFeatureDev pour créer des plans précis très facilement.

(\**Ceci est tout à fait comparable à la commande Slice d\'AutoCAD [1](https://knowledge.autodesk.com/support/autocad/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/AutoCAD-Core/files/GUID-27593C5E-4B89-41F2-872B-927D69517CBF-htm.html) qui est basée sur cet axiome. Sans pré-construction d\'un nouveau plan, un plan de coupe utilisant trois points est défini.*)


</div>

*Note: These planes can be joined together by overlapping/ coinciding of two edges using the Boolean feature of <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> [Part Union](Part_Fuse.md).* The planes thus formed and suitably positioned (according to our provisions) will be used as **cutting blades** <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part SliceApart](Part_SliceApart.md), cutting our 3D object into several parts according to the chosen planar confirmation.\'\'

## Before You Begin 

The Workbenches that are used to produce the drawings of the attached examples are:
\* <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md)

-   <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md)
-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md)
-   <img alt="" src=images/Workfeature_workbench_icon.svg  style="width:24px;"> [Workfeature Workbench](Workfeature_Workbench.md)
-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md)

## The Task 

Stages of the procedure:

1.  Creation of the 3D object(s) according to the canons of traditional modeling;
2.  Possible creation of independent or simple copies, eg. to be used for the creation of specific continuous sections positioned on multiple planes or axes, and which then through the use of the \"facebinder\", \"Draft to Sketch\", Shape 2D View, etc. functions. it will allow us to produce perfect "Sketches", then edit them to make them (by creating ad hoc "cosmetic points or lines") usable in TechDraw; to these sketches I gave the name of \"base-sketchTD\";
3.  insertion / creation of \"base-sketchTD\" in the layers of belonging (also with \"drag and drop\");
4.  creation of the drawing page with its template;
5.  creation of the view with TechDraw: select the layer or the grouping folder (which contains the "base-sketchTD") from the structure, then click on the "insert view" button; TechDraw will insert the contents of the layer or grouping folder into the view. For a correct creation \"base-sketchTD\" must be perpendicular to the monitor / display view; I point out that whatever we add later in the layer or in the grouping-folder, or modifications of the "base-sketchTD", will be updated in realtime in the TechDraw view. Keep in mind that updates and / or modifications may affect the dimensions already introduced or cosmetic lines created with the specific tool of TechDraw in the view.
6.  once the "base-sketchTD" has been defined in the view, we can move on to dimensioning with the appropriate TechDraw tools;

It is possible to insert the \"base-sketchTD\" also in the projection group views:

-   select the projection view -\> properties tab -\> Data -\> "Projection" record section -\> Source click on the button with the three dots and directly add the "base-sketchTD" or the layer that contains it.

:   It should be noted that the \"base-sketchTD\" must be positioned on the highest face of the model / object, otherwise it will be hidden and will be invisible in TechDraw.

The sections obtained from the views do not seem to have this possibility. Whenever it is necessary to create precise cosmetic points suitable for dimensioning (e.g. tangency points), they can be generated:

-   in \"Sketcher\" through construction lines and inserting circles with infinitesimal diameter / radius (0.00001) in the ends, these will be seen by TechDraw as points / vertices suitable for dimensioning;
-   in Draft with the same method to be inserted in the relevant layer or folder-grouping;

:   once the \"base-sketchTD\" has been modified or the Draft object added in the layer or grouping folder, TechDraw will automatically update the view, if this does not happen, update manually with the appropriate command.

To insert section fills or patterns:
pay attention to the lines created on the faces that intersect two or more edges, they are seen by TechDraw as separating elements of the face that affect the creation of the fills or patterns. This occurs e.g. when creating the outer lines that define the thread of a hole, this line will prevent the fill or pattern from extending further preventing it from arriving on the one that defines the pre-drill hole. In this case it is better to create cosmetic points through construction lines by inserting circles of infinitesimal radius in the vertices that will be seen by TechDraw as cosmetic points and then join them in TechDraw with create cosmetic line by two points.
All lines and / or paths (including cosmetic ones) that are displayed in the views can be edited in the formatting through TechDraw\'s "Change Apparence of selected Lines" command.
To create specific continuous sections on different axes or planes, I used the "WorkFeatureDev" workbench which allows you to create "solid" planes, with a thickness of "0", by selecting three vertices. These planes can be joined through a common or overlapping edge using the Boolean functions of the "Part" workbench and subsequently used for slicing / sectioning the solid model through the "Slice apart" command of the same workbench. The faces of the cut objects can be suitably exploited for the creation, with the "Facebinder" function, the "base-sketchTD"s to produce specific section views in TechDraw and therefore to be able to dimension and detail them.
I believe I have made public every \"trick\" (or rather system) experimented to be able to use more specific tools (not provided for TechDraw) and create high quality professional technical drawings without any limits, making the TechDraw workbench more efficient and adaptable to any need , in all likelihood on par (if not more flexible and powerful) than commercial peers.
It should be said, which is not negligible, that with this system it is possible to create entire 2D files and quote them with TechDraw in the same way as \"LibreCad\" or \"Autocad LT\" or other two-dimensional cads.
I hope I was clear enough (translation permitting) in explaining the procedure (\"trick / system\") that I believe to be \"easier to do than to say\", as it is all about being able to enter 2D drawings into the views of TDs created with \"Draft\" and / or with \"Sketcher\" simply by selecting them from the structure and creating a view in TD with the appropriate command \"create a view\"; but I thought of doing something pleasant and more technical by describing the procedure, certainly, in a \"simplified\" way to create a minimum of organized workflow.
It is up to each of us, with imagination and inventiveness, to optimize it to the maximum to obtain the best result.
I am attaching the files of some workflow examples of technical drawings (not feasible with TechDraw only) from which the images shown below were taken.
In the hope of having been useful, good work and good experimentation!

## Notes

## Future Outlook 

However, the described path could represent the starting point (or the idea) to write additional code to automate the system and integrate it directly into TechDraw with appropriate button / command functions.

## Links

-   [Macro WorkFeatures](https://wiki.freecadweb.org/Macro_WorkFeatures) Wiki page to macro
-   [FreeCAD WorkFeature Workbench](https://github.com/Rentlau/WorkFeature-WB) Repository to source code
-   [TechDraw without limits = Layout autocad](https://forum.freecadweb.org/viewtopic.php?t=54499) Forum Thread
-   [TechDraw: -- come utilizzare gli strumenti Draft/Snaps per creare " vertici/punti cosmetici"](https://forum.freecadweb.org/viewtopic.php?f=28&t=53329) Forum Thread in Italian language


{{Tutorials navi

}} {{TechDraw Tools navi}} 
