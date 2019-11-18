# pelecyodon
> Pelecyodon is an extinct genus of ground sloths from the Early Miocene.

MacBook burns your belly, fans run at max speed? How would that happen with
games that run perfectly on old Pentium?

Explanation is simple - "busy loop". Game uses all the resources of CPU core
producing numerous screen updates whereas only 60 are shown.

`pelecyodon` is a tiny script that fixes the problem.
Just run `python pelecyodon.py YourFavoriteGame` before the game itself, and it
will throttle the game.

No installation is required. `Python` is already part of OSX distribution.
Just download script and run it in terminal.

> The Terminal app is in the Utilities folder in Applications.
> To open it press Command-Spacebar (launch Spotlight) and
> type "Terminal" then double-click the search result.

Step-by-step how-to:
 - download pelecyodon.py (once)
 - open terminal
 - type `python pelecyodon.py YourFavoriteGame 0.2` and press enter
 - run the game
 - enjoy
 - switch to terminal window
 - press Control-Spacebar
 - close terminal window
