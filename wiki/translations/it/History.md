# History/it
\_\_FORCETOC\_\_

## Storia

<img alt="Vecchia versione sconosciuta di FreeCAD." src=images/Screenshot_mesh.jpg  style="width:300px;"> <img alt="Versione 0.7 di FreeCAD del 2009." src=images/Part_BooleanOperations.png  style="width:300px;">

### Come tutto è iniziato 

La storia FreeCAD è iniziata nel gennaio 2001 quando [Jürgen Riegel](User_Jriegel.md) ha iniziato a lavorare al progetto Cas.CADE. Cas.CADE era un framework di sviluppo software commerciale che includeva un [kernel di modellazione geometrica](Glossary/it#Geometric_modeling_kernel.md) (o kernel CAD): è stato rilasciato con licenza open source nel 2000 e ribattezzato [OpenCASCADE](OpenCASCADE/it.md). Ciò ha reso possibile la realizzazione di un programma CAD 3D open source, in quanto dover programmare da zero un kernel CAD avrebbe richiesto un enorme mole di lavoro.

Dalle parole di Jürgen:


{{Quote|text=''The FreeCAD project was started by me in January 2001, as a so called GOM (Graphical Object Modeler), with the idea to use Qt, Python and Cas.CADE, an commercial CAD-Kernel that time I used in Daimler's projects. Cas.CADE gone open source shortly before, so the time seemed right to try a move in the, at that time, empty space of open source CAD. I had a two year experience with OpenCascade in a project called QSpect in which, at the end, I was the main software designer. I learned a lot about 3D and CAD programming. I also was influenced by Catia V5 and its very special user and programming interface… In March 17 2002, within the OpenCascade Project, I registered the software as FreeCAD. I couldn't think of a better name, I'm very bad on names… In April 2003, Werner Meyer, one of the colleges in the QSpect project, switched to a company called Imetric. The contact to Imetric resulted very promising since they searched for a new 3D software platform for their 3D sensors. In 2005, Imetric donated most of its Mesh Module to FreeCAD and the Open Source community, and since then they used FreeCAD as basis for their sensor system software. Since that time, Werner Meyer is a very active developer of FreeCAD. In 2005, after one year of struggle, I decided to rip of the OpenCascade document framework and replace it with an own implementation. So, at the end, we only use the CAD kernel of OpenCascade and not the rest of its Framework. 2007 was another interesting milestone. We switched to QT4 and, therefore, to the LGPL. At that time we did much work, mainly Werner''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[http://forum.freecadweb.org/viewtopic.php?f=8&t=295 Who is behind FreeCad?]''}}

Il progetto è stato annunciato al pubblico sul [Forum di OpenCascade](https://dev.opencascade.org/forums) nel 2003.


{{Quote|text=''Hi together, my name is Juergen Riegel and today I want announce an OpenCasCade project, FreeCAD. It is an Open Source CAx RAD based on OpenCasCade, QT and Python. It features some key concepts like Macro Recording, Workbenches, ability to run as a server and as a dynamically loadable applications' extension, and it is designed to be platform independent… Although it is in an early stage and not usable for users nor developers—the first user release is planned for the end of 2003—, I would like to get some feedback on the direction and design of FreeCAD. The GUI is nearly finished and now we, my co-developer Werner Mayer and me, have started adding the first CAD functions. FreeCAD can be seen as a general purpose mechanical CAD system, but its first audience, I think, will be CAx developers which need groundwork for own development''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[https://dev.opencascade.org/content/announcing-freecad-project Announcing FreeCAD Project on Sun, 08/17/2003 - 19:23]''}}

### Werner Mayer 

Werner Mayer si è unito al progetto non appena è stato annunciato come progetto open source (prima dell\'annuncio il progetto era un progetto privato di Jürgen). Vedere questo post sul forum di Werner in tedesco: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>

Con il tempo, il progetto ha guadagnato attenzione, e si sono aggiunti dei nuovi contributori chiave nella comunità.

-   **L\'inizio con Linux**


{{Quote|text=''A fun fact is that he wanted to have an open-source CAD software mainly for Linux because at that time there existed actually nothing for this platform. However, from the beginning on we exclusively developed on Windows for the next 1.5 years. Then a Czech guy made a contribution to make the code of the core build on Linux: https://github.com/berndhahnebach/All_FreeCAD/commit/9fd2e27c95ba3dc84778d92e2564cd094793ce2f#diff-480477e89f9b6ddafb30c4383dcdd705''}}


{{Quote|text=''Half a year later I continued the Linux build: https://github.com/berndhahnebach/All_FreeCAD/commit/35b962d7d751dd80f7c7781df60f93bc9a3da992''}}

**Q:** Potresti condividere come sono andati i primi 1,5 anni? Vi siete incontrati di persona o online?


{{Quote|text=''Well, at that time we were colleagues (until 2005) so we could discuss things face to face. After that time we still had some personal meetings but discussed most things by email or phone.''}}


{{Quote|text=''As third core developer Yorik joined around end of 2007 but it took another 3 or 4 years until the community and number of contributors started to grow significantly.''}}

**Q:** Avete diviso i compiti o avete lavorato su implementazioni concorrenti?


{{Quote|text=''Yes. Jürgen was designing and implementing most of the application and document logic and I was doing the basics of the GUI.''}}


{{Quote|text=''However, this wasn't a gradual process but we have experimented with many things at the beginning. For example, in the initial version we used OCC's document framework OCAF and its viewer but after a year or two we got into a dead end because documentation about OCC was very poor and we couldn't get it to work to extend OCAF with our own feature types. So, we decided to only use OCC's modeling capacities but develop our own application/document framework.''}}

**Q:** All\'epoca pensavate che FreeCAD sarebbe arrivato dov\'è oggi?


{{Quote|text=''We didn't know but we hoped. Of course we couldn't anticipate how exactly FreeCAD will look today.<br>The most important design decisions were to make it available on all major platforms and make the whole SW as accessible as possible, i.e. to impose all important functions to Python so that (power) users are able to extend FreeCAD with own functions. This way we hoped to get a broad audience.''}}

(Vedere questo post sul forum di Werner [Re: FreeCAD History](https://forum.freecadweb.org/viewtopic.php?f=8&t=47703#p411612))

### Yorik si unisce al progetto 

[Yorik van Havre](User_Yorik.md) ha aderito al progetto nel 2008 e avviato i lavori sul [Modulo Draft](Draft_Workbench/it.md). Prima non c\'era modo di creare la geometria 2D attraverso la [GUI](Glossary/it#GUI.md). Questo modulo è stato programmato interamente in Python, anziché in C++ (che era il linguaggio di programmazione di base utilizzato in FreeCAD). Il nuovo ambiente Draft provò che l\'integrazione di Python era stata un successo e ha dimostrato che poteva essere utilizzato per estendere o personalizzare le funzionalità di FreeCAD. Oltre al suo lavoro sul modulo Draft, Yorik ha lavorato sull\'espansione della documentazione di FreeCAD, ed è diventato *de facto* \"Art director\" di FreeCAD, creando molte icone per la GUI e [definendo lo stile](Artwork/it.md) di FreeCAD.

La versione 0.7 di FreeCAD rilasciata nell\'aprile 2009 è stata la prima a includere il modulo Draft. Il modulo Part ha fornito un semplice flusso di lavoro [CSG](Glossary/it#Constructive_Solid_Geometry.md) con la creazione di forme primitive e operazioni booleane accessibili tramite il menu Part. Era possibile anche l\'estrusione di profili 2D e la filettatura.

La versione 0.8 rilasciata a luglio 2009 ha visto ulteriori progressi nel modulo Draft, incluso un nuovo strumento Dimension. Il modulo Parte ha beneficiato di una nuova barra degli strumenti insieme a nuovi strumenti, Rivoluzione e Sezione.

Alla fine del 2009, FreeCAD è stato accettato come pacchetto Debian nei repository Debian. FreeCAD è stato aggiunto ai repository di Ubuntu 10.04 nel 2010.

### Il progetto va avanti 

La versione 0.10 è stata rilasciata nel luglio 2010 ed ha introdotto L\'[Ambiente Sketcher](Sketcher_Workbench/it.md), basato su Sketchsolve, un risolutore basato su vincoli per creare geometrie 2D. La prima versione era limitata alla creazione di rettangoli e linee.

All\'inizio del 2011, cogliendo l\'opportunità offerta dalla piattaforma online [Launchpad](https://launchpad.net), è stato creato il [FreeCAD Maintainers team](https://launchpad.net/~freecad-maintainers) per fornire nuovi rilasci stabili insieme a compilazioni quotidiane dei pacchetti di FreeCAD per gli utenti del sistema operativo Ubuntu.

La versione 0.11 rilasciata a maggio 2011 ha introdotto il nuovo ambiente di lavoro Part Design che includeva strumenti come Pad, Pocket, Fillet e Chamfer. L\'ambiente Draft ha ricevuto miglioramenti e nuovi strumenti, come BSpline. L\'ambiente di lavoro Robot presentava più strumenti GUI.

La versione 0.12 è stata rilasciata nel gennaio 2012 e presentava un ambiente di Sketcher più completo. Comprendeva un risolutore completamente riscritto, FreeGCS. Era il risultato di mesi di lavoro dei principali sviluppatori di FreeCAD insieme ai nuovi arrivati ​​logari81 (che ha programmato il risolutore) e mrlukeparry. Altri strumenti sono stati aggiunti al workbench di PartDesign.

### Allargamento del team di sviluppo principale 

Nell\'aprile 2019 il team di sviluppatori principali è stato ampliato: Jürgen, Werner e Yorik sono stati raggiunti da Abdullah, Bernd, sliptonic e WandererFan

## Post interessanti sul forum 

-   riguardo a PartDesignNext e altre decisioni di progettazione: <https://forum.freecadweb.org/viewtopic.php?f=8&t=34923&start=130#p297074>
-   riguardo alla storia del Forum: <https://forum.freecadweb.org/viewtopic.php?f=8&t=7448&start=200#p287106>
-   riguardo la storia del progetto: <https://forum.freecadweb.org/viewtopic.php?f=8&t=47703>
-   riguardo alla storia del codice: <https://forum.freecadweb.org/viewtopic.php?f=10&t=46733&start=10#p405068> BTW: il controllo iniziale del codice è stato il 18 marzo 2002 (si potrebbe considerare come il compleanno?)
-   riguardo al progetto come OpenSource: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>
-   riguardo alla cronologia dei commit di rilascio: <https://forum.freecadweb.org/viewtopic.php?f=8&t=23695#p184940>
-   riguardo a chi c\'è in FreeCAD: <http://forum.freecadweb.org/viewtopic.php?f=8&t=295>
-   riguardo alla storia di FEM: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48646#p416389>
-   riguardo alla storia del mesher FEM: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48733#p417627>



## Cronologia dei rilasci 

#### Panoramica

  Version   Nome della Release   Data della Release    Note della Release                                       Commit della Release                                                                      Branch della Release
       
  1.1       \-                   in fase di sviluppo   [Release notes 1.1](Release_notes_1.1/it.md)     [head main](https://github.com/FreeCAD/FreeCAD/commits/main)                              
  1.0       BGBSWW               2024-11-18            [Release notes 1.0](Release_notes_1.0/it.md)     [release commit 1.0](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-1-0)     [branch bugfixes 1.0](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-1-0)
  0.21      \-                   2023-08-02            [Release notes 0.21](Release_notes_0.21/it.md)   [release commit 0.21](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-21)   [branch bugfixes 0.21](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-21)
  0.20      \-                   2022-06-14            [Release notes 0.20](Release_notes_0.20/it.md)   [release commit 0.20](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-20)   [branch bugfixes 0.20](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-20)
  0.19      \-                   2021-03-20            [Release notes 0.19](Release_notes_0.19/it.md)   [release commit 0.19](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-19)   [branch bugfixes 0.19](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-19)
  0.18      \-                   2019-03-12            [Release notes 0.18](Release_notes_0.18/it.md)   [release commit 0.18](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-18)   [branch bugfixes 0.18](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-18)
  0.17      Roland               2018-04-06            [Release notes 0.17](Release_notes_0.17/it.md)   [release commit 0.17](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-17)   [branch bugfixes 0.17](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-17)
  0.16      \-                   2016-04-18            [Release notes 0.16](Release_notes_0.16/it.md)   [release commit 0.16](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-16)   [branch bugfixes 0.16](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-16)
  0.15      \-                   2015-04-08            [Release notes 0.15](Release_notes_0.15/it.md)   [release commit 0.15](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-15)   [branch bugfixes 0.15](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-15)
  0.14      \-                   2014-07-01            [Release notes 0.14](Release_notes_0.14/it.md)   [release commit 0.14](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-14)   [branch bugfixes 0.14](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-14)
  0.13      \-                   2013-01-29            [Release notes 0.13](Release_notes_0.13/it.md)   [release commit 0.13](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-13)   [branch bugfixes 0.13](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-13)
  0.12      \-                   2011-12-20            [Release notes 0.12](Release_notes_0.12/it.md)                                                                                             
  0.11      \-                   2011-05-03            [Release notes 0.11](Release_notes_0.11/it.md)                                                                                             
  0.10      \-                   2010-07-24                                                                                                                                                               
  0.9       \-                   2010-01-16                                                                                                                                                               
  0.8       \-                   2009-07-10                                                                                                                                                               
  0.7       \-                   2009-04-24                                                                                                                                                               
  0.6       \-                   2007-02-27                                                                                                                                                               
  0.5       \-                   2006-10-05                                                                                                                                                               
  0.4       \-                   2006-01-15                                                                                                                                                               
  0.3       \-                   2005-10-31                                                                                                                                                               
  0.2       \-                   2005-08-09                                                                                                                                                               
  0.1       \-                   2003-01-27                                                                                                                                                               
  0.0.1     \-                   2002-10-29            Initial Upload of a version                                                                                                                        



#### Legenda

  Colore   Tipo della Versione
   
           Release Futura
           **Ultima versione**
           Vecchia versione
           

## Link Esterni 

-   [Sezione File in SourceForge](http://sourceforge.net/projects/free-cad/files/)
-   [Sezione File vecchi in SourceForge](http://sourceforge.net/projects/free-cad/files/OldFiles/)
-   [Annuncio del progetto FreeCAD](http://www.opencascade.org/org/forum/thread_6572/?forum=11) sul forum di OpenCascade



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > History/it
