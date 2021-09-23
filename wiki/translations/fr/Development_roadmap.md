# Development roadmap/fr
 **Important : nombre de ces feuilles de route ne sont pas à jour ou sont peut-être abandonnées. Cette page et les pages vers lesquelles elle renvoie contiennent très probablement des informations obsolètes. Une feuille de route "souple" se trouve sur le [http://www.freecadweb.org/tracker/roadmap_page.php bugtracker] mais il n'y a pas de feuille de route "dure" pour le moment. De nombreux efforts sont déployés simultanément.**

FreeCAD - bien qu\'utilisable dans de nombreuses applications - FreeCAD n\'est qu\'au début d\'un long voyage dans la [CAO](http://fr.wikipedia.org/wiki/Conception_assistée_par_ordinateur). Il y a encore beaucoup de travail à faire pour atteindre un stade où nous pourrons rivaliser avec les logiciels commerciaux.

Cette section donne un aperçu de ce qui est prévu et vous donne la possibilité de participer ou de donner votre avis. Comme nous sommes des volontaires pour développer FreeCAD, nous n\'avons que notre temps libre pour le développer.
Si vous êtes intéressés à l\'un des sujets et prêts à nous aider, vous n\'avez juste qu\'a nous le faire savoir sur le [forum](http://forum.freecadweb.org/) ou, pour la section française à [Yorikvanhavre](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)!
Nous utilisons le style [Getting Things Done (GTD)](http://fr.wikipedia.org/wiki/Getting_Things_Done) pour le document de projet.
Voici le modèle [de projet](Project_template/fr.md) ([en](Project_template.md)).

-   L\'[organigramme](http://www.freecadweb.org/wiki/index.php?title=Organization_chart) montre qui fait quoi dans l\'univers de FreeCAD.
-   Vous pouvez suivre les questions et sujets qui sont actuellement travaillés via le bugtracker ici : ![](images/Mantis_logo_button.gif )

## Projets

  Projet                                                                                          La description                                                                                                                                              Catégorie                                                                 Statut
  ----------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------- ---------
  **[Projet STEP](STEP_project/fr.md)**                                                   sur l\'amélioration et l\'avancement du support STEP dans FreeCAD                                                                                           Modélisation, formats de fichiers                                         Courant
  **[Projet Nommage](Naming_project/fr.md)**                                              consiste à implémenter un cadre robuste de référencement de forme.                                                                                          Modélisation                                                              Courant
  **[Projet Modèle de développement FreeCAD](FreeCAD_development_model_project/fr.md)**   déplacer FreeCAD vers un modèle de développement plus performant                                                                                            Processus de développement                                                Courant
  **[Projet Sketcher](Sketcher_project/fr.md)**                                           est la mise en œuvre en cours de la contrainte / esquisse paramétrique                                                                                      Modélisation, contraintes 2D                                              Courant
  **[Projet PartDesign](PartDesign_project/fr.md)**                                       est l\'effort vers une conception de pièce de travail dans FreeCAD                                                                                          Modélisation                                                              Courant
  **[Projet d\'assemblage](Assembly_project/fr.md)**                                      crée un module d\'assemblage qui gère la création de produits, les listes de pièces et certaines cinématiques.                                              Modélisation, contraintes 3D                                              Courant
  **[Projet d\'architecture](Arch_Concept/fr.md)**                                        jettera les bases d\'un environnement de modélisation architectural moderne et paramétrique.                                                                Modélisation, BIM                                                         Courant
  **[Projet Unités](Units_project/fr.md)**                                                enfin, faites en sorte que FreeCAD reconnaisse différentes unités et systèmes d\'unités.                                                                    Modélisation, documentation de fabrication, dimensions et référencement   Courant
  **[Projet Structure des ressources](Resource_framework_project/fr.md)**                 aborder la collaboration des utilisateurs, [PDM](http://en.wikipedia.org/wiki/Product_Data_Management) catalogue / matériel de pièce standard               Cloud, bases de données, nomenclature                                     Courant
  **[Projet Qualité](Quality_project/fr.md)**                                             vise à masquer les fonctionnalités inachevées et à améliorer la documentation.                                                                              Processus de développement                                                Courant
  **[Projet Raytracing](Raytracing_project/fr.md)**                                       fournir une nouvelle interface générique pour les moteurs de rendu externes pour la visualisation                                                           Visualisation 3D                                                          Courant
  **[Projet UTF](UTF_Project/fr.md)**                                                     vise à mettre à jour l\'interface Coin3D de FreeCAD pour utiliser les chaînes UTF pour une meilleure expérience multilingue avec des caractères non ASCII   Internationalisation                                                      Courant
  **[Projet FEM](FEM_project/fr.md)**                                                     fournit un module [FEM](http://en.wikipedia.org/wiki/Finite_element_method) dans FreeCAD.                                                                   Modélisation, analyse                                                     Courant
  **[Modèle des données sur les matériaux](Material_data_model/fr.md)**                   Effort pour décrire un modèle de données de matériau dans FreeCAD                                                                                           Modélisation                                                              Courant
  **[Python 3](Python_3/fr.md)**                                                          Portage de FreeCAD vers Python 3.                                                                                                                           Outils de développement                                                   Courant
  **[Prise en charge HiDPI](HiDPI_support/fr.md)**                                        Prise en charge de l\'évolutivité sur les écrans 4K.                                                                                                        GUI                                                                       Courant
  **[Tolérancement](Tolerancing/fr.md)**                                                  La prise en charge des tolérances de modélisation, en utilisant les normes internationales (ISO 1101 / ASME Y14.5, ISO 16792 / ASME Y14.41)                 Modélisation, documentation de fabrication, dimensions et référencement   Courant
  **[Atelier de l\'arpenteur-géomètre](Land_Survey_Workbench_Blueprint/fr.md)**                                                                                                                                                                                                                                                 Futur
  **[Projet Robot](Robot_project/fr.md)**                                                 Un atelier de simulation de robot                                                                                                                           Modélisation, contraintes 3D                                              Fini
  **[Projet d\'illustration](Artwork_project/fr.md)**                                     Un projet de mise à jour du logo et des icônes                                                                                                              GUI                                                                       Courant
                                                                                                                                                                                                                                                                                                                                        

## Calendrier de publications 

Comme dans les plupart des projets [FLOSS](http://fr.wikipedia.org/wiki/Free/Libre_Open_Source_Software) le calendrier de diffusion est très sommaire. Il n\'y a aucune date fixe et **\"Ce sera disponible quand ce sera prêt !\"**

-   La page [Release process](Release_process.md) rassemble des idées pour un flux de publication plus efficace.




[Category:Roadmap](Category:Roadmap.md)
