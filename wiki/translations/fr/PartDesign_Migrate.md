---
- GuiCommand:
   Name: PartDesign Migrate
   Name/fr: PartDesign Migrer
   MenuLocation: Part Design -> Migrer
   Workbenches: PartDesign_Workbench/fr
   Version: 0.17
---

# PartDesign Migrate/fr

## Description

L\'atelier PartDesign dans FreeCAD V0.17 introduit de nouveaux outils et éléments qui ne sont pas reconnus par les anciennes versions FreeCAD (0.16 et plus anciennes). Les documents FreeCAD créés dans des versions plus anciennes peuvent toujours être ouverts et modifiés. Pour bénéficier des nouvelles fonctionnalités, vous devez les migrer via le menu PartDesign → Migrer.


{{Version/fr|0.17}}

## Utilisation

1.  Ouvrez un document FreeCAD créé avec FreeCAD {{VersionMinus/fr|0.16}}.
2.  Basculez vers l\'atelier **<img src="images/Workbench_PartDesign.svg" width=16px> [PartDesign](PartDesign_Workbench/fr.md)**.
3.  Aller au menu **Part Design** → **Migrer**.
4.  Si la migration fonctionne, un <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Part Conteneur](Std_Part/fr.md) sera créé. Il contiendra un ou plusieurs <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps](PartDesign_Body/fr.md), chacun hébergeant une chaîne de fonctionnalités.

## Limitations

-   Avant de commencer le processus de migration, vérifier si le modèle a été construit avec les options d\'affinage automatique activées (**Édition → Préférences → Part Design → Général**) et définir vos préférences en conséquence. Cela peut être facilement déterminé en basculant successivement la visibilité des entités dans l\'arborescence du modèle. Si aucun bord résiduel n\'est laissé entre les fonctions telles que des protrusions et des cavités, les options d\'affinage automatique ont été désactivées.
-   Si un document à migrer ne contient que des esquisses et des fonctions PartDesign, le processus de migration peut réussir. Certaines fonctionnalités telles que les chanfreins et les filets peuvent nécessiter une reconstruction.
-   Si le document à migrer a un flux mixte de production Part/Part Design/Draft, la conversion échouera très probablement ou au mieux produira des résultats inattendus et devra être migrée manuellement.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Migrate/fr
