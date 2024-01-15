---
 GuiCommand:
   Name: Std LinkImport
   Name/fr: Std Importer des liens
   MenuLocation: Aucun
   Workbenches: Tous
   Version: 0.19
   SeeAlso: Std_LinkMake/fr, Std_LinkMakeRelative/fr, Std_LinkImportAll/fr
---

# Std LinkImport/fr

## Description


**[<img src=images/Std_LinkImport.svg style="width:16px"> [Std Importer des liens](Std_LinkImport/fr.md)**

importe la {{PropertyData/fr|Linked Object}} d\'un lien dans le document en cours puis modifie la dépendance à cet objet.

Cette opération est utile lorsque vous travaillez avec des [assemblages](assembly/fr.md) afin d\'organiser des modèles réutilisables qui peuvent se trouver dans d\'autres documents.

Utilisez **[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Std Importer tous les liens](Std_LinkImportAll/fr.md)** pour importer tous les objets liés.



## Utilisation

1.  Assurez-vous que vous avez un document \"source\" avec un objet original, disons, un **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** et une seconde \"cible\" document avec un lien vers cet objet.
2.  Ouvrez le document cible et sélectionnez le lien vers l\'objet. Sa **Linked Object** doit afficher quelque chose comme {{Value|source#Part}}.
3.  Appuyez sur **[<img src=images/Std_LinkImport.svg style="width:16px"> [Std Importer des liens](Std_LinkImport/fr.md)**.

Une copie de l\'original **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** doit maintenant se trouver dans le document \"cible\" actuel. La propriété **Linked Object** du lien doit maintenant afficher {{Value|Part}} indiquant que le lien ne pointe plus vers {{Value|Part}} dans \"source\" mais vers {{Value|Part}} dans le document courant (\"cible\").

![](images/Std_Link_tree_import_1_example.png ) ![](images/Std_Link_tree_import_2_example.png )



*À gauche : un lien pointe vers l'objet dans le document "source".<br />À droite : l'objet d'origine a été importé (copié) dans le document "cible" et le lien existant a été modifié pour pointer vers cette copie, de sorte qu'il ne pointe plus vers l'objet dans "source".*





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkImport/fr
