 [Localisation](Localisation.md) is the process of providing software with a multiple language user interface. The documentation wiki can also be localized, as described in section [Translate the FreeCAD wiki](Localisation#Translate_the_FreeCAD_wiki.md).

The sidebar is an important navigation tool in the wiki world, see [Manual:Interface/Sidebar](http://www.mediawiki.org/wiki/Manual:Interface/Sidebar) for more information.

## Translate the sidebar 

The sidebar is now fully translatable with the [Translation extension](http://www.mediawiki.org/wiki/Help:Extension:Translate), which is available in all pages of the wiki.

In the FreeCAD wiki, the sidebar is implemented using templates, which change the text depending on the selected language. Technical details on how this feature was implemented are described in the forum thread [Wiki navigation / translation](http://forum.freecadweb.org/viewtopic.php?f=21&t=9687&start=10#p80441).

### Инструкции

You can go to the special page [Special:Translate/wiki-sidebar](Special:Translate/wiki-sidebar.md) to begin translation.

There is a bug with the Download page. You can\'t redirect the link to \"Download/fr\", or \"Download/de\", etc. Instead, the link will point to the actual translation of \"Download\" in your language. The best way to deal with it is to create this new page and do a redirection to the right page. More about redirection on [Help:Editing](Help:Editing.md).

## Важные замечания 

Most of the time there will be two strings for each item in the sidebar.

** {{int:sidebar-faq-target}}|sidebar-faq

The left one represents the target of the link, and the right one represent the text that will be displayed in the sidebar.

You can see the difference between the two by looking at the top of the translate box where the name of the variable is displayed. When the variable name ends with \"-target\", it means that you will be translating a target link. It\'s made to allow the translator to redirect the items to the translated pages, that is, by adding a language code at the end of the page name, for example, \"/fr\" for a French translation.

Do not add the language codes \"/fr\", \"/de\", \"/es\", \"/ru\", etc., if the translated page doesn\'t exists in that language, it will break the link. In this case, do not write anything else than the name of the page, or it will break the link.

![Where to look](images/Translate-sidebar-instruction.png )



[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Wiki{{\#translation:}}](Category:Wiki.md)
