# Bug Triage/de






{{TOCright}}

## Why


{{ColoredParagraph|Triageː

1a :  the sorting of and allocation of treatment to patients and especially battle and disaster victims according to a system of priorities designed to maximize the number of survivors

1b :  the sorting of patients (as in an emergency room) according to the urgency of their need for care

2:  the assigning of priority order to projects on the basis of where funds and other resources can be best used, are most needed, or are most likely to achieve success
}}

Bug triage is important to organize and prioritize bugs/features/patches in respect to the FreeCAD [Bug Tracker](Tracker.md). If this task is neglected a project can suffer from what is called \'Bugtracker Bloat\' which is essentially neglected tickets accumulating and rotting. Triage also helps to identify duplicate tickets that have a tendency to accumulate especially if there is a long standing unresolved issue that the FC team is well aware of but doesn\'t have the resources for whatever reason to fix at the time.

## How to Triage 

### Ticket Status 

#### New

Per MantisBT docsː {{ColoredText|This is the landing status for new issues. Issues stay in this status until they areː assigned, acknowledged, confirmed or resolved. }}

In other words, **NEW** status indicates several thingsː

1.  Ticket hasn\'t been confirmed.
2.  Ticket is still in process, i.e. Triage/Devs still evaluating/clarifying details of ticket from OP.
3.  FreeCAD team hasn\'t decided what to do with this ticket yet.

All current [open FreeCAD tickets with **NEW** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=10&hide_status=80).

#### Acknowledged

#### Feedback

Tickets get designated this status when OP is being requested to provide more information.

The ticket is pending based on the participation of OP. For exampleː the ticket is missing FC version info; or perhaps a certain 3rd party library name or version is required etc\... Devs need to set this status whenever replying to OP in order to indicate that the ticket is pending. This is important due to the possibilit that OP neglects to respond which has a high probability for the ticket to \'rot\' in the tracker.

When OP responds the ticket status changes back to **New** automatically. Then ticket needs to be re-examined to decide what is needed.

Further discussion on this topic in the [FreeCAD forum](https://forum.freecadweb.org/viewtopic.php?f=10&t=23005).

All current [open FreeCAD tickets with **FEEDBACK** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=20&hide_status=80) in the FC bugtracker.

#### Confirmed

When a ticket is confirmed it has been eitherː

-   a bug that has been reproduced
-   a feature that has been greenlit to be considered valid.

It is now ready to be assigned to or by a dev.

All current [open FreeCAD tickets with **CONFIRMED** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=40&hide_status=80) in the FC tracker.

#### Assigned

Self-explanatory, these tickets that have been assigned to a specific developer.

All current [open FreeCAD tickets with **ASSIGNED** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=50&hide_status=80) in the FC tracker.

#### Resolved

These tickets have been resolved but not closed yet, most likely because they need confirmation that the ticket has been fixed.

------------------------------------------------------------------------

### Ticket Resolutioɲ 

#### Open

Self-explanatory, all tickets remain as \'open\' if they are still relevant at the discretion of the FC team.

#### Fixed

Tickets that have been fixed.

#### Unable to reproduce 

Tickets deemed un-reproducible

#### Duplicate

Tickets that are or have a duplicate ticket.

#### No change required 

Tickets were it has been ascertained that no modifications are necessary.

#### Won\'t fix 

FC team has rejected the ticket request for whatever reason stated.

#### Not fixable 

#### Reopened

Tickets that have been closed me then re-opened for a relevant reason. Most likely that the issue has resurfaced or wasn\'t totally fixed.

#### Suspended

### Ticket Priority 

#### Immediatə

#### Urgent

#### High

#### Normal

#### Low

#### None

### Ticket Severity 

#### Block

#### Crash

#### Major

#### Minor

#### Tweak

#### Text

#### Trivial

#### Feature

## Tagging Tickets 

An important methodology to track tickets by a certain subject/theme/category. It\'s important that **Existing Tags** be used to tag issues **before** new tags are created. If duplicate or superfluous tags are created the bug tracker admin is responsible to remove them and if possible retag said tickets.

## Related

[Bugtracker](Tracker.md)







[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Administration](Category:Administration.md)
