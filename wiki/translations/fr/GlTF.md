# GlTF/fr
{{TOCright}}

## Description

Le [GL Transmission Format](https://www.khronos.org/gltf/) (glTF™) est une spécification libre de droits pour la transmission et le chargement efficaces de scènes et de modèles 3D par des applications. Il minimise à la fois la taille des actifs 3D et le traitement d\'exécution nécessaire pour décompresser et utiliser ces actifs.

## Installation

Selon ce [fil de discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=31680&p=450917&#p450658), OCC doit être compilé avec le support RapidJSON afin d\'utiliser les fonctionnalités glTF. Par conséquent, définissez l\'option `USE_RAPIDJSON` dans l\'étape de configuration de CMake. Cela nécessite le package rapidjson-dev.

## Importer

Actuellement non pris en charge dans FreeCAD.

## Exporter

Depuis la version 0.19.23074 de FreeCAD, la commande [Std Exporter](Std_Export/fr.md) peut exporter au format gITF.

### Solutions d\'exportation alternatives 

Pour les versions antérieures, ces solutions de contournement peuvent être utilisées:

1\. Exporter en STEP → Importer dans l\'assistant CAD depuis Opencascade -\> Exporter vers glTF

OU

2\. Utilisez la bibliothèque Python `cqparts` ([website](https://github.com/cqparts/cqparts)): {{code|
import cqparts
cqparts.Assembly.importer('step')('myfile.stp').exporter('gltf')('myfile.gltf')
}}

Source: [fil du forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=31680&p=449977#p449977)

## En relation 

-   [Import Export](Import_Export/fr.md)
-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)




[Category:File\_Formats](Category:File_Formats.md)

---
[documentation index](../README.md) > [File_Formats](Category:File_Formats.md) > GlTF/fr
