:soccer: __C H A M P G A F F E R__ :soccer:
===========================================
_Web-based football manager application // Python, Django and JavaScript_
------------------------------------------------------------------

_I N T R O_
-----------

__CHAMPGAFFER__ is a football (soccer) manager simulation game where the user is given the task of guiding their team out of the second-tier _Sub League_ (based on the English Championship) and onto glory in the _Super League_ (based on the English Premier League).

The premise is built loosely around the early [Championship Manager][] games - with a fun, retro spin - using fictional teams and players with nods to the real world. The interface utilises [Bootstrap][] to enhance browser compatibilty and ensure a modern user-experience, but also offers hints of nostalgia with arcade fonts, Windows 98 inspired 'email', fixture lists and [Teletext][] matchday action, results and league standings.

The application uses a mixture of pre-determined and randomised elements to generate player/squad attributes and simulate results. Users can purchase players to improve their squad, increase the likelihood of winning matches, and work their way up the rankings.


_H T M L ,  C S S   &   L A Y O U T_
------------------------------------

Excluding the Teletext-inspired match simulation pages, each __CHAMPGAFFER__ extends [layout.html][]. The head of [layout.html][] contains links to global components of the app: 

+   [Bootstrap][] stylesheet for basic styling
+   The custom [main.css][] stylesheet imports:
    - [98.css][]: for Windows '98 styling
    - [teletext.css][]: for teletext styling
    - [styles.css][]: _CSS_ fine tuning
+   [jQuery][], [popper.js][] and [Bootstrap]'s _JavaScript_
+   [font awesome][] icons

[layout.html][] also handles the global navigation bar, alerts and acknowledgements in the footer. Here also lives the simple loading page, which appends an animated loader icon to a pre-loaded page and removes it once all elements have loaded to the DOM. A [setTimeout()][] fallback is included in the event of a page item failing to load after 5 seconds:

[layout.html][]
```javascript
$(window).on('load', function(){
    removeLoader(); //wait for page load
});
window.setTimeout(removeLoader, 5000); // fallback if some content fails to load
```

Layout and content alignment for all non-Teletext pages is handled by _Bootstrap_'s [grid system][], ensuring responsiveness and flexibilty in the page layouts.


[Championship Manager]: https://en.wikipedia.org/wiki/Championship_Manager      "Championship Manager Wikipedia page"
[Bootstrap]: https://getbootstrap.com/      "Bootstrap site"
[Teletext]: https://en.wikipedia.org/wiki/Teletext      "Teletext Wikipedia page"

[layout.html]:  main/templates/main/layout.html       "HTML file for common page layout"
[main.css]: main/static/main/css/main.css       "main.css stylesheet"
[98.css]: https://jdan.github.io/98.css/    "Adapted for the 'Windowfied' elements of the app"
[teletext.css]: main/static/main/css/teletext.css     "CSS for Teletext pages"
[styles.css]: main/static/main/css/styles.css     "Stylesheet for general customisations"
[jQuery]: https://jquery.com/       "jQuery site"
[setTimeout()]: https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout       "JavaScript setTimeout() Mozilla docs"
[popper.js]: https://popper.js.org/     "popper.js (tooltip and popover positioning) site"

