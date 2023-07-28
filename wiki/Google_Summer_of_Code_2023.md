# Google Summer of Code 2023
FreeCAD started participating to the Google student coding program (GSoC) in 2016. We participated through a combined effort of many CAx projects, under the BRL-CAD umbrella. Beginning in 2023, we are applying as our own organization.

-   Main page of the program: <https://summerofcode.withgoogle.com/>
-   FreeCAD in GSoC: <https://summerofcode.withgoogle.com/programs/2023/organizations/freecad>

## How it works 

-   The student writes a project proposal for FreeCAD.
    -   Sometimes their project idea caters to something that the open source organization suggests and sometimes it\'s an idea entirely of the student\'s conception.
-   Proposals are reviewed, evaluated, and ranked by the open source organization\'s mentors.
-   Google allocates a certain number of slots to each participating organization
    -   That, in turn, determines how many student developers work with that organization.

If you want to get involved have a look at the [GSoC Checklist](GSoC_Checklist.md). Whether you\'re applying or accepted, we\'ve itemized everything you need to do in this list. We\'re here to help you become new open source developers, so don\'t be shy if you have any questions.

We are proposing a number of project ideas here. But you are in no way forced to follow our ideas. You can propose anything you would like to work on, that you thing would be an interesting project.

## The Selection Process 

GSoC is about getting people involved and contributing to open source over the long-term. As such, we heavily weight our application selection process towards students that are interested in remaining involved in FreeCAD and open source software development long after GSoC has ended. GSoC is not a job. If you think this is just a summer job, then GSoC is probably not for you. It\'s only like a job in terms of planning your time commitment over the summer.

Additionally, submissions are graded based on perception of the submitter\'s abilities to complete the task within the program timeframe, general consensus on the technical approach being proposed, and overall interest in having such modifications made to FreeCAD. Particular notice is made of students that are responsive to questions and readily interactive in the IRC channel or on the forum. Communication is a great thing.

Just about every GSoC organization receives considerably more project proposals than can be accepted. Every application gets read multiple times and reviewed in detail. Of those applications, only a small subset are selected so keep in mind that the selection process is rather competitive and difficult.

Whether or not you are accepted, contributing to open source outside of GSoC is one of the main goals of the program and is the best way to be noticed and get your proposal accepted. Keep that in mind. Thanks for your interest and we look forward to working with new FreeCAD developers!

## Possible Mentors 

[Bernd](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=2069), [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68), [Amritpal](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=9146), [Ickby](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686), [Kkremitzki](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=7997), [Kunda1](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=12229), [WandererFan](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=1375), [Sliptonic](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=708) and others. The best way to contact us is through the [FreeCAD GSoC 2023 discussion thread](https://forum.freecad.org/viewtopic.php?t=75828).

## Implementation Ideas 

There are several sources for project ideas. The table below lists existing project ideas already documented on our wiki. FreeCAD also previously participated in an umbrella organization for GSoC, and there are [FreeCAD project ideas available in their GSoC repo](https://github.com/opencax/GSoC/issues?q=is%3Aissue+is%3Aopen+FreeCAD). Additionally, there is a [forum thread](https://forum.freecad.org/viewtopic.php?t=75828) calling for additional ideas which may be the basis of a project.

The ideas listed here or in the OpenCAx repo have a high chance of being accepted as project proposal. Note that for students with an established involvement in FreeCAD who have already contributed code, ideas in their own line of work are also welcome. Feel free to contact us on IRC, the forum or the mailing list for further discussions about the listed projects.

The topic\'s priority shows you how important the work on the ideas is for the mentors, and hence choosing a high priority topic will give you an advantage if there are more applications than slots for FreeCAD. The size column shows the estimated time frame to complete the project, but you are of course free to suggest otherwise if you see arguments for it.

  Topic                                                                                                                                                                                                                                           Language         Size   Difficulty    Priority   Contact
       
  [FreeCAD-BRLCAD integration](https://github.com/FreeCAD/FreeCAD/issues/8557): Allow to open, edit and save BRL-CAD models in FreeCAD                                                                                                            C++              350h   High          Medium     [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68), [Daniel Rossberg](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=23847)
  [Upgrade the documentation system](https://github.com/FreeCAD/FreeCAD/issues/8558): Rework the documentation system so it supports multiple languages, and allows to switch between offline and online versions                                 C++, Python      175h   Medium        Medium     [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [GSoC FEM Solver Z88](https://github.com/FreeCAD/FreeCAD/issues/8559): Extend the capabilities of FEM solver Z88OS in FreeCAD FEM workbench.                                                                                                    Python           175h   Easy-Medium   Low        [Bernd](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686)
  [Advanced FreeCAD test system](https://github.com/FreeCAD/FreeCAD/issues/8560): Create a framework for result file based comparisons and workbench specific comparators. Also creation of test cases should be simplified by a GUI or wizard.   Python/C++       175h   Medium        Low        [Ickby](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686)
  [Unified Measurement Facility](https://github.com/FreeCAD/FreeCAD/issues/8561): Create a generalized measurement tool that combines functionality from workbench-specific ones                                                                  Python/C++       175h   Medium        Low        [Kkremitzki](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=7997)
  [Improve Hidden Line Removal](https://github.com/opencax/GSoC/issues/69): Develop new code for projecting shapes and creating the geometry for technical drawings                                                                               C++              350h   Hard          Low        [WandererFan](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=1375)
  [Improving Headless mode](https://github.com/opencax/GSoC/issues/68): Exposing more FreeCAD functionality to the console that can run with and without the GUI available                                                                        C++              175h   Medium        Low        [Kunda1](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=12229)
  [UI tool for fetching online content](https://github.com/opencax/GSoC/issues/39): Design a library tool that fetches the content online, without the need to download the whole library                                                         Python           175h   Medium        Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [Command-line preferences manipulation](https://github.com/opencax/GSoC/issues/38): Design a command-line tool that allows to create, modify or delete FreeCAD preference parameters                                                            C++              175h   Medium        Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [Better materials structure](https://github.com/opencax/GSoC/issues/37): Invent a handier way to classify, store and select materials and implement that system FreeCAD-wide                                                                    C++ and Python   175h   Medium        Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [Improve the API documentation](https://github.com/opencax/GSoC/issues/36): Work on the FreeCAD doxygen-generated documentation: Propose a better plan, document the modules better, make it clearer to read, etc.                              C++ and Python   175h   Medium        Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [Cabinet tool](https://github.com/opencax/GSoC/issues/35): Design a tool for the Arch workbench that allows a user to easily create several kinds of cabinets                                                                                   Python           350h   Medium        Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [Direct Modeling tools](https://github.com/opencax/GSoC/issues/17): Study and implement direct modeling tools in FreeCAD                                                                                                                        Python/C++       350h   Hard          Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [On-Machine Inspection](https://github.com/opencax/GSoC/issues/8588): Problem: The Path Workbench lacks capability for On-machine inspection                                                                                                    Python/C++       175h   Medium        Low        [Sliptonic](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=708)

Note also that any issue open on the \[FreeCAD issues tracker <https://github.com/FreeCAD/FreeCAD/issues>\] could become a good GSoC proposal. Don\'t hesitate to browse the issues, the ones [marked as \"Feature\"](https://github.com/FreeCAD/FreeCAD/issues?q=is%3Aissue+is%3Aopen+label%3AFeature) are feature requests and might be especially interesting to you. If any of them picks your brain, feel free to discuss it, either directly on the issue itself, or on the [forum thread](https://forum.freecad.org/viewtopic.php?t=75828).

## Schedule

-   January 23 - 18:00 UTC: Mentoring organizations can begin submitting applications to Google
-   February 7 - 18:00 UTC: Mentoring organization application deadline
-   February 7 - 21: Google program administrators review organization applications
-   February 22 - 18:00 UTC: List of accepted mentoring organizations published
-   February 22 - March 19: Potential GSoC contributors discuss application ideas with mentoring organizations
-   March 20 - 18:00 UTC: GSoC contributor application period begins
-   April 4 - 18:00 UTC: GSoC contributor application deadline
-   April 27 - 18:00 UTC: GSoC contributor proposal rankings due from Org Admins
-   May 4 - 18:00 UTC: Accepted GSoC contributor projects announced
-   May 4 - 28: Community Bonding Period \| GSoC contributors get to know mentors, read documentation, get up to speed to begin working on their projects
-   May 29: Coding officially begins!
-   July 10 - 18:00 UTC: Mentors and GSoC contributors can begin submitting midterm evaluations
-   July 14 - 18:00 UTC: Midterm evaluation deadline (standard coding period)
-   July 14 - August 21: Work Period \| GSoC contributors work on their project with guidance from Mentors
-   August 21 - 28 - 18:00 UTC: Final week: GSoC contributors submit their final work product and their final mentor evaluation (standard coding period)
-   August 28 - September 4 - 18:00 UTC: Mentors submit final GSoC contributor evaluations (standard coding period)
-   September 5: Initial results of Google Summer of Code 2023 announced
-   September 4 - November 6: GSoC contributors with extended timelines continue coding
-   November 6 - 18:00 UTC: Final date for all GSoC contributors to submit their final work product and final evaluation
-   November 13 - 18:00 UTC: Final date for mentors to submit evaluations for GSoC contributor projects with extended deadlines

## Previous GSOCs 

-   [Google Summer of Code 2022](Google_Summer_of_Code_2022.md)
-   [Google Summer of Code 2020](Google_Summer_of_Code_2020.md)
-   [Google Summer of Code 2019](Google_Summer_of_Code_2019.md)
-   [Google Summer of Code 2018](Google_Summer_of_Code_2018.md)
-   [Google Summer of Code 2017](Google_Summer_of_Code_2017.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Google Summer of Code 2023
