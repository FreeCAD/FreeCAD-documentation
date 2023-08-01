---
- GuiCommand:
   Name:Std LinkImportAll
   Name/fr:Std Importer tous les liens
   MenuLocation:Aucun
   Workbenches:Tous
   Version:0.19
   SeeAlso:[Std Créer un lien](Std_LinkMake/fr.md), [Std Créer un lien relatif](Std_LinkMakeRelative/fr.md), [Std Importer des liens](Std_LinkImport/fr.md)
---

# Std LinkImportAll/fr

## Description


**[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Std Importer tous les liens](Std_LinkImportAll/fr.md)**

importe toutes les {{PropertyData/fr|Linked Object}} des liens dans le document en cours puis modifie la dépendance pour qu\'elle pointe vers ces objets importés.

Cette commande exécute essentiellement **[<img src=images/Std_LinkImport.svg style="width:16px"> [Std Importer des liens](Std_LinkImport/fr.md)** pour tous les liens d\'un document.

## Utilisation

1.  Assurez-vous d\'avoir un document \"source\" avec les objets originaux et un deuxième document \"cible\" avec des liens vers ces objets.
2.  Ouvrez le document cible et appuyez sur **[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Std Importer tous les liens](Std_LinkImportAll/fr.md)**.

![](images/Std_Link_tree_import_all_1_example.png ) ![](images/Std_Link_tree_import_all_2_example.png )



*À gauche : divers liens qui pointent vers des objets dans le document "source".<br/>À droite : les objets originaux ont été importés (copiés) dans le document "cible" et les liens existants ont été modifiés pour pointer vers ces copies, de sorte qu'ils ne pointent plus vers des objets dans "source".*





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std LinkImportAll/fr
