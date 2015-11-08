==============
PM Transcripts
==============

Last week, while preparing for the Humanities in Public lesson on APIs, 
I stumbled across the `Department of Prime Minister and Cabinet`_'s 
`Transcripts from the Prime Ministers of Australia`_ - because it has 
an "API"_. I was looking for all the speeches given by Malcolm Fraser
in order to give some contextual richness to another site we are
building on Fraser's speech.

After reading the page three times trying to understand how the API 
worked, I realised that it only **just** made the grade as an API. A 
lot of work would be required to get it functional.

What **is** available? There is a `single xml file` which lists a link 
to each transcript's data in xml format, which it became apparent 
(later) is also the basis for each transcript's actual web page.

As an example, see Whitlam's 
`Sales tax on oral contraceptives website`_ vs the 
`Sales tax on oral contraceptives xml`_

There is no easy way to comprehensively get the data programmatically
(which is *my* definition of an API). In particualar, I couldn't just 
get all the speeches by Malcolm Fraser - meta data and content.

So I decided to fix this problem as an example of how an API does work,
but also how one **can** work.











.. _Department of Prime Minister and Cabinet: http://www.dpmc.gov.au
.. _Transcripts from the Prime Ministers of Australia: http://pmtranscripts.dpmc.gov.au/
.. _"API": http://pmtranscripts.dpmc.gov.au/developers
.. _single xml file: http://pmtranscripts.dpmc.gov.au/transcripts.xml
.. _Sales tax on oral contraceptives xml: http://pmtranscripts.dpmc.gov.au/release/transcript-2737
.. _Sales tax on oral contraceptives website: http://pmtranscripts.dpmc.gov.au/query?transcript=2737
