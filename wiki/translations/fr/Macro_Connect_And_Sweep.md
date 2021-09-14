# Macro Connect And Sweep/fr

 {{Macro/fr
|Name= Macro Connect And Sweep
|Icon=Macro_Connect_And_Sweep.png
|Description={{ColoredText|#ff0000|#ffffff|Nouvelle version de l'interface graphique modifiée pour le dpi HD (QGridLayout) exécutez uniquement la version FC 0.18 et plus (PySide2 Qt5)}} <br/> <br/> Cette macro crée facilement une connexion entre deux objets. Une fonction discretize permet de créer de point suivant le nombre de coupes du fil ou par dimension déterminée.<br/>Une fonction de discrétisation est disponible pour créer des points marqueurs configurables pour couper des lignes en coupe ou une coupe avec une cote sur le point est créée pour toutes les coordonnées.<br/>Une fonction de face ou de fil dupliquée à utiliser avec l'opération de balayage et de lissage <br/>Opération de balayage et de lissage directement avec la macro.<br/>Centrage de la poutrelle sur les faces
|Author=Mario52
|Version=0.12
|Date=2020-07-05
|FCVersion=0.18 et plus
|Download=[https://www.freecadweb.org/wiki/images/c/c9/Macro_Connect_And_Sweep.png ToolBar Icon]
}}

## Description

Cette macro crée facilement une connexion entre deux objets (le centre des objets sont les points de départ et d\'arrivée du sweep) , un objet et un point ou entre deux points une forme peut être choisie cercle polygone ellipse rectangle paramétrable. Une fonction discretize permet de créer de point suivant le nombre de coupes du fil ou par dimension déterminée.
Fonctionnalité de duplication de face ou de fil pour utiliser avec l\'opération de balayage et de lissage.
Opération de balayage et de lissage directement avec la macro.
Centrage de la poutrelle sur les faces


{{Codeextralink|https://gist.githubusercontent.com/mario52a/3ec67a3711202dab69592ce53b938924/raw/5717e333a7df104d461a495e8e1f5de75ead41b9/Macro_Connect_And_Sweep.FCMacro}}

<img alt="" src=images/Macro_Connect_And_Sweep_00.png  style="width:640px;"> 
*Macro_Connect_And_Sweep*

## Utilisation

lancez la macro sélectionnez vos objets ou points choisissez la forme et réglez les dimensions et cliquez sur le bouton **Create**.

<img alt="" src=images/Macro_Connect_And_Sweep_01.png  style="width:350px;"> 
*Macro_Connect_And_Sweep*

![](images/Macro_Connect_And_Sweep_Discretize.png ) *Discretize* ![](images/Macro_Connect_And_Sweep_Duplicate.png ) *Duplicate* ![](images/Macro_Connect_And_Sweep_Sweep.png ) *Sweep* ![](images/Macro_Connect_And_Sweep_Loft.png ) *Loft* ![](images/Macro_Connect_And_Sweep_Reset.png ) *Reset*

## Images

Ces images doivent être copiées dans votre répertoire de macros.

(Pour télécharger les images faites : Clic sur le bouton droit de la souris sur l\'image et selectionnez \"Sauvez l\'image sous\...\"(version 0.17))

![Center](images/Macro_Connect_And_Sweep_CE.png ) ![Top left](images/Macro_Connect_And_Sweep_TL.png ) ![Top rigth](images/Macro_Connect_And_Sweep_TR.png ) ![Low left](images/Macro_Connect_And_Sweep_LL.png ) ![Low rigth](images/Macro_Connect_And_Sweep_LR.png )

L\'icône pour votre barre d\'outils ![Icon for the button](images/Macro_Connect_And_Sweep.png )

## Script

![icon for the button](images/Macro_Connect_And_Sweep.png )\'\'\'

Macro\_Connect\_And\_Sweep.FCMacro\'\'\'

Téléchargez la macro sur Gits [*\' Macro\_Connect\_And\_Sweep.FCMacro*\'](https://gist.github.com/mario52a/3ec67a3711202dab69592ce53b938924)

## Exemple

Créer un tubage en suivant un chemin avec Macro\_Connect\_And\_Sweep et [Macro\_Repro\_Wire](Macro_Repro_Wire/fr.md) <img alt="" src=images/Macro_ReproWire.png  style="width:32px;">


<center>

<File:Macro> Connect And Sweep 02.png\| The sweep to work


</center>


<center>

<File:Macro> Connect And Sweep 03.png\| Sélectionnez les deux point des extrémités de chaque fil exécutez la macro choisisez la forme et les réglages et cliquez sur le bouton **Create solid**


</center>


<center>

<File:Macro> Connect And Sweep 04.png\| Repeat the operation if needed


</center>


<center>

<File:Macro> Connect And Sweep 05.png\| sélectionnez le bord du cylindre et exécutez la macro [Macro\_Repro\_Wire](Macro_Repro_Wire.md) <img alt="" src=images/Macro_ReproWire.png  style="width:32px;">


</center>


<center>

<File:Macro> Connect And Sweep 06.png\| le cercle est créé activez l\'outil Sweep <img alt="" src=images/Part_Sweep.png  style="width:32px;">


</center>


<center>

<File:Macro> Connect And Sweep 07.png\| Sélectionnez le cercle le chemin et exécuter le sweep


</center>


<center>

<File:Macro> Connect And Sweep 08.png\| Easy ?


</center>

==Exemples animés==


*align=center|
[[File:Macro Connect And Sweep Sweep2.gif]]*

{clear}}


*align=center|
Objet et Objet, connexion boundBox center objet 1 et boundBox center objet 2
[[File:Connect_And_Sweep_01_Object_Object.gif]]*





*align=center|
Object SubObject, connexion boundBox center objet 1 et boundBox center Subobjet 1
[[File:Connect_And_Sweept_02_Object_SubObject.gif]]*





*align=center|
SubObject SubObject, connexion boundBox center Subobject 1 et boundBox center Subobject 2
[[File:Connect_And_Sweep_03_SubObject_SubObject.gif]]*





*align=center|
Connect And Sweep Direction un objet sélectionne ou Subobject selectionné
[[File:Connect And Sweep 4 Direction.gif]]*





*align=center|
Detection Erreur de mode de sélection, si une erreur ou sélection est creée le mode change pour le mode 3 et la ligne du mode 3 est colorée en orange
[[File:Connect_And_Sweep_05_Detect_Error.gif]]*




## Versions

ver 0.12 2020/07/05 : inclusion des icônes dans le code source

ver 00.11b 2020-02-22 : ajout d\'un test \"try: except\" au test FreeCAD version

ver 00.11 2020-02-13 : modifier pour HD dpi QGridLayout exécuter uniquement la version FC 0.18 et plus
Pour la version précédente, voir[Macro\_Connect\_And\_Sweep.FCMacro](https://gist.githubusercontent.com/mario52a/3ec67a3711202dab69592ce53b938924/raw/b3554916e0dce63644a2d4d3f88ef114b5e1e390/Macro_Connect_And_Sweep.FCMacro)

ver 00.10 2020-01-09 : centrage de la poutrelle sur les faces

ver 00.09 2020-01-06 : ajout de Tab Duplicate (comme Macro reproWire), Sweep, Loft.

ver 00.08 2019-12-23 : ajout d\'une fonction de discrétisation permet de créer des points repères suivant le nombre de coupes du fil ou par dimension déterminée.

ver 00.07 2019-06-26 : upgrade et ajout des modes Objet et Objet, Objet et SubObjet, SubObjet et SubObjet sélection d\'une linge et autres petits changements

00.06 18/06/2019 : ajout \"Recompute\" à la section Line

00.05 05/04/2019 : compatible Python 3

00.04 22/02/2017 : mise à jour du système de recherche path macros

00.03 15/09/2016 : Ajout de la création de tubes.

00.02 13/06/2016 : ajout de l\'option de choix du coin du rectangle (et ellipse) pour suivre le chemin du sweep et d\'un bouton pour effacer la dernière forme si le sens ne convient pas

00.01 07/06/2016 : ajout des options solid ou non centrage du rectangle ou non

00.00 05/06/2016 :

## Links

La discussion sur le forum [Scripting point to point tubing](http://forum.freecadweb.org/viewtopic.php?f=22&t=15833)

Cette macro est basée sur le code de microelly2 voir sur le forum [Looking for some helpful GUI-commands](http://forum.freecadweb.org/viewtopic.php?t=7029#p56746)

Autre discussion sur le forum [Macro\_Connect\_And\_Sweep](https://forum.freecadweb.org/viewtopic.php?f=22&t=35432)




