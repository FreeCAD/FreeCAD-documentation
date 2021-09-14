# Part/it



## Introduzione


{{TOCright}}


<div class="mw-translate-fuzzy">

In FreeCAD il termine \"[Parte](Part/it.md)\" è in genere usato per riferirsi ad una [Parte](Std_Part/it.md) (classe `App::Part`), un tipo di oggetto contenitore che è definito dal sistema base. Questa Parte è usata per gestire la posizione di forme tridimensionali allo scopo di creare assemblaggi meccanici.


</div>


<div class="mw-translate-fuzzy">

Si veda [Parte](Std_Part/it.md) per maggiori informazioni riguardo questo tipo d\'oggetto.


</div>

## Utilizzo

Lo strumento Parte non è definito da un particolare ambiente di lavoro, ma dal sistema base; di conseguenza lo si ritrova nella **barra degli strumenti struttura**, che è disponibile in tutti gli [ambienti di lavoro](Workbenches/it.md).

1.  Premere il pulsante **<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)**. Una Parte vuota viene creata e diventa automaticamente *[attiva](Std_Part/it#Stato_attivo.md)*.

## Note

Nell\'uso informale, una \"Parte\" può essere qualunque figura geometrica che sia visibile nella [Vista 3D](3D_view/it.md), e dunque il suo concetto può essere confuso con quello di \"[Corpo](Body/it.md)\" o \"[Assemblaggio](Assembly/it.md)\".

Tuttavia, quando è richiesta maggiore precisione, vanno fatte le dovute distinzioni.

-   Un \"[Corpo](Body/it.md)\" è usato per singoli elementi contigui, di solito creati con gli ambienti di lavoro [Parte](Part_Workbench/it.md) o [Part Design](PartDesign_Workbench/it.md).
    -   Un \"Corpo\" ha una \"[Forma](Shape/it.md)\".
-   Una \"Parte\" è usata per raggruppare un singolo \"Corpo\", o diversi, per formare un \"Assemblaggio\".
    -   Una \"Parte\" ha una collezione di \"[Forme](Shape/it.md)\", ma non ha essa stessa una \"Forma\".
-   Un \"Assemblaggio\" è una collezione di \"Parti\" organizzate in una qualche maniera, manualmente, o usando un ambiente di assemblaggio.


{{Std Base navi

}} {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)
