# Artwork project/it
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Il **Progetto Artwork** è un [progetto](project/it.md) dedicato alla creazione di un nuovo logo, icone e immagini. Da non confondere con la pagina [Opere grafiche](Artwork/it.md) che cattura lo stato dell\'arte attuale;). Vedere anche [Linee guida per le opere grafiche](Artwork_Guidelines/it.md) che descrivono le attuali regole concordate.

This project is more of an experiment, to not be constrained by the current artwork guidelines set in stone many years ago.

## Rationale

Every once in a while a new contributor proposes a new logo or icon. This page is meant to track those proposals and discussions around them.

## Requirements

[Artwork Guidelines](Artwork_Guidelines.md) captures the current guidelines. This section proposes a simplified version of those.

### Size and format 

As there are various screen sizes and contexts, the artwork needs to be scalable. To achieve this scalability all icons must be done in the vector (SVG) format. Splash screens, OTOH are allowed to be raster graphics. At the same time, splash screens should be provided with several resolutions, according to [HiDPI support](HiDPI_support.md) guidelines.

### Color scheme 

As discussed in the section below, colors should be decided separately from the artwork. The artwork format should support an easy re-coloring so that it be consistent with brand colors (when people start proposing color schemes).

As Qt doesn\'t support SVG selectors, a set of icons embedded into FreeCAD distribution should have the colors either hardcoded or replaced in runtime.

## Logo proposals 

![](images/Logo_proposals_2020.png )

A new logo proposal comes up quite often. Even though there\'s a dedicated thread people for proposals, people open a new thread for their own work.

Proposals can be divided into several categories:

-   A variation of traditional design with F and the gear
-   An updated traditional design with F and C stylized as caliper and the gear
-   Geometrical flat figures representing F and C
-   F, C, gear depicted in 3D
-   Abstract ideas, not obviously related to F, C, gear

### Survey

There was a proposal to get quantified feedback. Several solutions were proposed to gather it, from manually gathering votes in the spreadsheet to automated systems.

The simplest way to set up a survey is by using the SurveyMonkey service: <https://www.surveymonkey.com/r/MKFDZQX>

Some contributors forcefully reject the idea of voting, advocating the delegation of the right to decide on Artwork to those who have administrators rights to merge pull requests (mainly yorik and wmayer).

## Artwork

[Artwork](Artwork.md) is proposed less often as there are dozens and hundreds of icons in FreeCAD. Only a few people dared to try this. The traditional artwork is done by a single man years ago. There are currently 2 proposals in progress.

## Color palettes 

Colors are quite an important part of branding. Unique colors are subconsciously associate the product with a brand in the mind of a user. Since artwork proposals are of various color schemes, we need to come up with an easy way to apply a color theme to icons once we establish it.

Currently, there are hundreds of different colors and gradients in the existing artwork. A successful color scheme only needs a dozen: 3-4 main colors, black, white, and shades of each.

### Traditional

  -------------------------------------- -------------------------------------- -------------------------------------- -------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              Use the Yellow tones for tools that create objects; for an example, see [Part](Part_Workbench.md) and [Draft Workbenches](Draft_Workbench.md).
  style=\"background-color:\#729fcf;\|   style=\"background-color:\#3465a4;\|   style=\"background-color:\#204a87;\|   style=\"background-color:\#0b1521;\|   Use the Blue tones for tools that modify objects; for an example, see [Part](Part_Workbench.md) and [Draft Workbenches](Draft_Workbench.md).
  style=\"background-color:\#34e0e2\|    style=\"background-color:\#16d0d2\|    style=\"background-color:\#06989a\|    style=\"background-color:\#042a2a\|    Use the Teal tones for view-related tools; for an example, see the [View Menu](Std_View_Menu.md).
  style=\"background-color:\#ef2929\|    style=\"background-color:\#cc0000\|    style=\"background-color:\#a40000\|    style=\"background-color:\#280000\|    Use the Red tones for Constraint related tools; for an example, see [Sketcher Workbench](Sketcher_Workbench.md).
  -------------------------------------- -------------------------------------- -------------------------------------- -------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

The current color palette is captured in google drive: <https://drive.google.com/file/d/0B_xxY57wUEV-RWNaMHV2OGpoY00/view>

## External links 

### GitHub

-   [Icon themes workbench](https://github.com/triplus/IconThemes)

### Figma

-   [Vanuan\'s FreeCAD project](https://www.figma.com/file/QiSdiUf1vGO6KWdC3dIm6Z/FreeCAD?node-id=5%3A0)
-   [Stephan Bogner\'s Icon theme project](https://www.figma.com/file/DeX9eYTL6y9bvMJYykbXWx/FreeCAD-Icon-Theme?node-id=162%3A0)

### Forum threads 

#### Logo

-   [The main thread about logo proposals](https://forum.freecadweb.org/viewtopic.php?f=34&t=28941)
-   [A new proposed thread to post logo proposals](https://forum.freecadweb.org/viewtopic.php?f=34&t=50640)
-   [A single logo proposal](https://forum.freecadweb.org/viewtopic.php?f=34&t=50885)

#### Icon

-   [Std\_Part](https://forum.freecadweb.org/viewtopic.php?f=34&t=50821)
-   [Std Alignment](https://forum.freecadweb.org/viewtopic.php?f=34&t=50688)

[<img src="images/Property.png" style="width:16px"> Roadmap](Category_Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > Artwork project/it
