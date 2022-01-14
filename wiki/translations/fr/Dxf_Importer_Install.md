# Dxf Importer Install/fr
{{TutorialInfo/fr
|Topic=SampleClass
|Level=Moyen
|Time=15 minutes
|Author=[Mario52](User_Mario52.md)
|FCVersion=Toutes
}}

## Description

Cette page explique étape par étape la marche à suivre pour installer l\'ensemble des fichiers Draft-dxf-import yorikvanhavre pour pouvoir importer des fichiers au format DXF et DWG dans FreeCAD à l\'aide de l\'utilitaire de teighafileconverter. Cet exemple d\'installation a été fait dans l\'environnement Windows Vista, mais le principe de l'installation de ce système est la même pour Linux.

## Première étape: 

Identifier le dossier des macros FreeCAD

**1 :** ouvrez FreeCAD


<div class = "mw-collapsible mw-collapsed toccolours">

Si vous avez une version 0,15, vous pouvez utiliser le package de mise à jour automatique DXF (dérouler pour voir)


<div class="mw-collapsible-content">

<img alt="Installation automatique du module DXF " src=images/Dxf_Importer_Install_01b.png  style="width:640px;"> 


</div>


</div>

**2 :** cliquez **Menu \> Macro \> Macros** ou cliquez sur le bouton <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Ouvre une boîte de dialogue pour exécuter une macro enregistrée\".

![ouverture de FreeCAD](images/Dxf_Importer_Install_01.png ) 

**3 :** la boîte de dialogue s\'ouvre

**4 :** copiez l\'adresse de \"Destination de la macro\" (ici **C:\\Users\\d\\AppData\\Roaming\\FreeCAD\\**) dans Ubuntu, normalement **/home/your\_user\_name/.FreeCAD**

![Ouvre une boîte de dialogue pour exécuter une macro enregistrée](images/Dxf_Importer_Install_02.png ) 

**5 :** collez l\'adresse dans votre explorateur et confirmez

![collez l\'adresse dans votre explorateur et confirmez](images/Dxf_Importer_Install_03.png ) 

**6 :** laissez votre explorateur ouvert

![laissez votre explorateur ouvert](images/Dxf_Importer_Install_04.png ) 

**7 :** fermez FreeCAD

## Seconde étape: 

Télécharger les fichiers

**8 :** téléchargez les fichiers sur la page <https://github.com/yorikvanhavre/Draft-dxf-importer>

**9 :** et cliquez sur le bouton **Download ZIP** pour la version courante (ou choisissez une autre version pour votre version de FreeCAD plus bas dans la page).


<div class="mw-collapsible mw-collapsed toccolours">

(ou choix pour votre version de développement voir en bas de la page) (dérouler pour voir)


<div class="mw-collapsible-content">

![ 640px \| center \| installation automatique DXF ](images/Dxf_Importer_Install_05b.png ) 


</div>


</div>

![download des fichiers](images/Dxf_Importer_Install_05.png ) 

**10 :** vous devez extraire les fichiers dans un répertoire temporaire (ici **C:\\tmp**)

![extraction des fichiers](images/Dxf_Importer_Install_06.png ) 

**11 :** le décompresseur crée un nouveau répertoire nommé \"**Draft-dxf-import-master**\"

![décompresseur crée un nouveau répertoire](images/Dxf_Importer_Install_07.png ) 

**12 :** les fichiers se trouvent dans ce répertoire, sélectionnez tous les fichiers et faites \"Couper\"

![sélectionnez tous les fichiers et faites \"Couper\"](images/Dxf_Importer_Install_08.png ) 

**13 :** revenez dans l\'explorateur laissé ouvert (étape 6) et collez les fichiers dans le répertoire (**C:\\Users\\d\\AppData\\Roaming\\FreeCAD\\**)

Dans Ubuntu, normalement ce doit être **/home/your\_user\_name/.FreeCAD**

![Collez les fichiers](images/Dxf_Importer_Install_09.png ) 

**14 :** Ouvrez FreeCAD et cliquez sur le bouton <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> , les fichiers nécessaires pour importer les fichiers de format DXF sont présents, fermez la fenêtre \"Lancez la macro\"

![ouvrez FreeCAD](images/Dxf_Importer_Install_15.png ) 

**15 :** chargez votre fichier .DXF

![ouvrez votre fichier DXF](images/Dxf_Importer_Install_10.png ) 

**16 :** le fichier DXF est bien ouvert dans FreeCAD

![le fichier DXF est bien ouvert dans FreeCAD](images/Dxf_Importer_Install_11.png ) 

**VERSIONS**

Ce dépôt contient plusieurs versions d\'importateur DXF. La version par défaut, que vous téléchargez lorsque vous appuyez sur le bouton **download ZIP** ci-dessus, est la version requise par la version stable actuelle de FreeCAD.

Si vous utilisez une autre version de FreeCAD, par exemple une version de développement ou une ancienne version, vous pouvez avoir besoin d\'une autre version de cette bibliothèque DXF.

Vous pouvez connaître la version de la bibliothèque DXF installée dans votre installation, en entrant le code suivant dans la console Python de FreeCAD : 
```python
import importDXF
print importDXF.CURRENTDXFLIB
```

## Troisième étape : 

Téléchargez et installez Teigha converter pour utiliser les fichiers au format **.DWG**

**17 :** teighafileconverter est téléchargeable à cette adresse [teighafileconverter](http://www.opendesign.com/guestfiles/teighafileconverter)

![téléchargez TeighaConverter](images/Dxf_Importer_Install_12.png ) 

**18 :** choisissez votre version d\'après votre Qt et OS

![choisissez votre version](images/Dxf_Importer_Install_13.png ) 

**19 :** et installez le dans votre système

![Installez le dans votre système](images/Dxf_Importer_Install_14.png ) 

**20 :** ouvrez FreeCAD et cliquez sur le bouton <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Ouvre une boîte de dialogue pour exécuter une macro enregistrée\"

**21 :** Fermez la fenêtre des macros

**22 :** et activez \'\'\'Atelier Planche à Dessin \'\'\'

![activez atelier Planche à Dessin](images/Dxf_Importer_Install_16.png ) 

**23 :** maintenant allez dans la page des options DXF/DWG cliquez \"Menu \> Édition \> Préférences\"

![Menu \> Préférences](images/Dxf_Importer_Install_17.png ) 

**24 :** sélectionnez \"Draft \> DXF/DWG options\"

**25 :** dans la section Option du format DWG, cliquez sur les 3 points **\...** ![Draft \> DXF/DWG options](images/Dxf_Importer_Install_18.png ) 

**26 :** donnez le chemin où se trouve Teigha converter pour que FreeCAD puisse utiliser le convertisseur de DWG vers DXF

**27 :** entrez le chemin ici dans Window \"**C:/Program Files/ODA/Teigha File Converter 4.00.1/**\" puis sélectionnez TeighaFileConverter.exe et confirmez

![Options du format DWG](images/Dxf_Importer_Install_19.png ) 

**28 :** l\'opération est terminée cliquez sur le bouton **OK** et tester un fichier DWG.

![Chemin Teigha File Converter 4.00.1](images/Dxf_Importer_Install_20.png ) 

## Quatrième étape: 

Utilisation de Teigha. Teigha est une application complète et vous pouvez l\'utiliser indépendamment de FreeCAD.

![Emplacement Teigha File Converter 4.00.1](images/Dxf_Importer_Install_21.png ) 

**1 :** Entrez le chemin du dossier : chemin du dossier ou sont les fichiers DXF ou DWG à convertir.

**2 :** Output folder : chemin de destination des fichiers convertis

**3 :** Recurse folder:

**4 :** Audit:

**5 :** Input files filter: filtre des fichiers à DXF, DWG ou DXF et DWG

**6 :** Sortie: le fichier sera converti au format et à la version sélectionnée

**7 :** Start: lance la procédure

### Liens

Tutoriel Vidéo [FreeCAD Tutorial 24 - DXF/DWG Import](https://www.youtube.com/watch?v=wHxTWuDhc3M) (en Allemand 17:16 minutes)

---
[documentation index](../README.md) > Dxf Importer Install/fr
