# FreeCAD development model project
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**

 

This page is toward the transition of the FreeCAD code in a GIT repository and a more capable development model. It follows the rules of the \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\] process. The projects are collected in the [Development roadmap](Development_roadmap.md).

## Purpose and principles 

This project aims to define a new development and governance model for FreeCAD. We come to point where one SVN repository is hard to govern. Working with patches is annoying and complicated for people willing to contribute code. To give everyone write access to the SVN repo dangerous. People can unintentional break something in the base system or force tasty decisions.

So I look at the Linux development process, which is maybe at the moment too big for our shoes, but never the less! Which means Git as distributed version control system (DVCS), mailing lists and submaintainers (lieutenants).

## Outcome

## Brainstorming

### Git

-   Using Git as new version control system
-   Keeping SVN (at least for while)
    -   use it as some kind of release repository to keep the ppa work flows and the nice revision numbers
    -   restrict SVN writes to Werner, Yorik and Jurgen (official tree)
    -   all other things, like development, branches, experiments go into Git!
    -   **Option:** switch completely to Git
        -   would give some collaterals in version numbering and ppa builds\....
-   give write rights (push) to everyone interested in

### Development mailing list 

The forum has its limitation, I would use the one or more mailing lists to manage branches and pull requests. That has advantages:

-   can work off-line
-   use powerful search of the mail client
-   no restrictions in attachments and sizes

### Clarify responsibilities 

We will soon become more and more developers and user will have conflicting feature requests. We have to have structure and responsibilities to filter and decide such requests and incoming code.

#### Step ups 

Adrian Przekwas:

Publicity - G+, Youtube,
Tutorials - [http://freecad-tutorial.blogspot.com](http://freecad-tutorial.blogspot.com)
Translation (unsure) - Polish (Wiki, Crowdin)

Yorik van Havre:

Software: arch module, draft module, artwork
Documentation: general wiki organization and design
Translation: french, dutch, brazilian portuguese
Publicity: articles on [http://yorik.uncreated.net/guestblog.php](http://yorik.uncreated.net/guestblog.php), G+, facebook

## Organizing

Decided rules and information goes to the [FreeCAD development model](FreeCAD_development_model.md) document.

## Next actions 

 

[<img src="images/Property.png" style="width:16px"> Roadmap](Category_Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > FreeCAD development model project
