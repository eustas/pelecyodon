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
 - download [pelecyodon.py](https://raw.githubusercontent.com/eustas/pelecyodon/master/pelecyodon.py) (once)
 - open terminal
 - type `python ~/Downloads/pelecyodon.py YourFavoriteGame 0.2` and press enter
 - run the game
 - enjoy
 - switch to terminal window
 - press Control-C
 - close terminal window

Second parameter for script is `ratio` - how much CPU should be allowed to be
used by the target application. `0.15` is enough for "Darkest Dungeon",
`0.2` works well for "Diablo 2" and "Knights of the Old Republic"
on my MacBookPro 2018.
