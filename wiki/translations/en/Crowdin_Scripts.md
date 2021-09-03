 {{TOCright}}

## Managing Translations for FreeCAD {#managing_translations_for_freecad}

FreeCAD uses a 3rd party translation service called [Crowdin](https://crowdin.com/project/freecad) to manage translations.

There are 3 scripts in FreeCAD/src/Tools that are used to manage translation files:

1.  updatets.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatets.py)
2.  updatecrowdin.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatecrowdin.py)
3.  updatefromcrowdin.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatefromcrowdin.py)

### Notes

-   These scripts are run from the root of the FreeCAD/ directory.
-   In order for these scripts to work one needs to have the valid FreeCAD Crowdin API key placed in their ~/.crowdin-freecad file. (For security reasons, only available to people with admin rights on the crowdin FreeCAD project)
-   Currently these tools are Python2 compatible.

### updatets.py

The updatets.py script will create the .ts files in your local FreeCAD/ directory. It generates .ts files (Qt Translation Source File).

It is invoked with: python2 updatets.py

### updatecrowdin.py

The updatecrowdin.py script pushes changes to Crowdin (3rd party translation crowdsource translation service) from your local FreeCAD/ directory. The script currently supports 4 arguments:

-   updatecrowdin.py status prints a status of the translations
-   updatecrowdin.py update updates crowdin the current version of .ts files found in the source code
-   updatecrowdin.py build builds a new downloadable package on crowdin with all translated strings
-   updatecrowdin.py download downloads the latest build

### updatefromcrowdin.py

The updatefromcrowdin.py script pulls changes from crowdin to your local FreeCAD/ directory.

## To send latest strings to crowdin {#to_send_latest_strings_to_crowdin}

-   Only tested on linux
-   You need a .credentials file in your /home/YourUser directory. That file is a simple text file containing only one line, which is the API key that you get on <https://crowdin.com/project/freecad/settings#api> (only for admins)
-   Make sure your repository is clean (git pull, git stash if needed)
-   cd /path/to/freecad-source-code/src/Tools
-   python updatets.py (will fill all the .ts files found in the source with the lastest strings)
-   python updatecrowdin.py update (will send the ts files to crowdin. Crowdin will only update strings that are new)
-   cd ../.. (go back to the source code root folder)
-   git checkout . (undo all the changes to the .ts files, no reason to commit them right now as they are still untranslated)

## To merge latest translations from crowdin {#to_merge_latest_translations_from_crowdin}

-   Only tested on linux
-   You need a .credentials file in your /home/YourUser directory. That file is a simple text file containing only one line, which is the API key that you get on <https://crowdin.com/project/freecad/settings#api> (only for admins)
-   Make sure your repository is clean (git pull, git stash if needed)
-   cd /path/to/freecad-source-code/src/Tools
-   python updatecrowdin.py build (will create a zip on crowdin side with all the files, can take a while.. This step can also be done on the crowdin website)
-   python updatecrowdin.py download (will download a freecad.zip file in this directory)
-   mv freecad.zip \~ move the zip file to your home dir, to avoid accidentally committing it later)
-   (optional) edit updatefromcrowdin.py script and check that the default\_languages contain all the ones you want (basically all that are at more than 50%)
-   python updatefromcrowdin.py -z /home/YourUser/freecad.zip
-   cd ../.. (go back to the source code root folder)
-   if something went wrong or you are unsure, clean everything with git checkout .
-   if everything looks ok (git status), commit with git add . && git commit
-   Create a PR on FreeCAD

## To generate a translation file from the website {#to_generate_a_translation_file_from_the_website}

-   Clone the homepage repository
-   cd /path/to/FreeCAD-homepage
-   xgettext \--from-code=UTF-8 -o lang/homepage.pot \*.php
-   Update the \"homepage.po\" on crowdin website manually, using the lang/homepage.pot file

## To update the translations of the website {#to_update_the_translations_of_the_website}

-   Get the freecad.zip file either by downloading it from the crowdin website or following instructions above (python updatecrowdin.py download)
-   cd /path/to/FreeCAD-homepage
-   Make sure your repository is clean (git pull, git stash if needed)
-   python updatefromcrowdin.py -z /path/to/freecad.zip
-   if something went wrong or you are unsure, clean everything with git checkout .
-   if everything looks ok (git status), commit with git add . && git commit
-   Create a PR on FreeCAD-Homepage
-   After the PR is merged, one of the admins will ftp push to the webhost

## Related

-   [Localisation](Localisation.md)
-   [Crowdin Administration](Crowdin_Administration.md)
-   [Release process](Release_process.md)




[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Administration{{\#translation:}}](Category:Administration.md)
