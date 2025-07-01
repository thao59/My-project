Github: thao59
edX: Mabel59(Thao Nguyen Phuong Dinh)

URL link: https://www.youtube.com/watch?v=7h_UcvwwGYw


My project is called AnimeSearch.

There are two folders, static and templates, under my final-project anime directory.

The static folder stores my footer image and CSS stylesheet, which contains all of the site’s styling rules. I use CSS to set the page background colour; text colours for body text, headings, links, placeholders, and button labels; and the background and border colours for the search bar—including its focus state and the button’s active state. To improve usability, I display a pointer cursor when users hover over interactive elements (such as the submit button, the “Anime” heading that redirects to the home page, or the anime titles that link to the detailed information page). The titles themselves use a distinct colour from the rest of the anime details to enhance readability.

I primarily use Flexbox to layout my search results in search.html and anime-info.html, providing a clean, flexible structure that adapts well to different screen sizes. Throughout my CSS, I incorporate percentage-based dimensions over fixed rem or px units so that element sizes adapt responsively to various viewports. I also apply !important on elements where Chrome’s default user-agent styles would otherwise override my rules.

layout.html defines the overall page structure. It begins with a <meta name="viewport" content="width=device-width, initial-scale=1"> tag to ensure elements scale proportionately across devices. I import the Google font “Noto Sans JP” because its aesthetic complements the site’s design. The header is preset here so it appears on every page. For the footer, I only want it to appear on the main page (index.html), so I use {% if %} block to render it as desired. 

index.html is the landing page where users search for anime titles. I incorporate JavaScript to disable the submit button when the input field is empty. As soon as the user begins typing, the button is enabled; if the field is cleared, the button is disabled again.

search.html displays the top ten results returned by the API. Each anime title is wrapped in an <a> tag that points to anime-info.html, passing the anime’s unique ID and title via URL parameters. When users click a title, they are taken to the detailed view for that specific anime.

not_found.html is rendered when the search() function returns None—for example, if the API request fails or returns no data.

anime-info.html presents more comprehensive information about the selected anime, including its genres, status, a link to its MyAnimeList page, and the synopsis. All of these details come from the API response.

app.py defines all of my Flask routes. I use the @app.after_request to prevent caching in development, ensuring that I always see the latest changes to my code and the most updated API data without manually clearing the browser cache. This also benefits end users by making sure they always receive the most up-to-date anime information. I drew heavily on knowledge from Week 9 and Problem Set 9 (Finance) to create this website. I incorporated my understanding of Python dictionaries to manipulate the data returned by search(). I created a dict, search_anime = {}, to store search results manually. The reason for this is that many anime titles are in Japanese. When users input an English title, the matching anime often appears with its Japanese name. For example, when I search “Your Name,” which is a very popular anime, ten results come back and the top one is “Kimi no Na wa.” which is the anime I'm looking for but in Japanese. However, when I click that title to read more, not_found.html is rendered, meaning search() returned None. What happened is that in my original @app.route("/anime") definition of anime(), I tried to retrieve the displayed title from search.html using url_for('anime', title=item['title']). This title=item['title'] passed the Japanese title “Kimi no Na wa.” instead of “Your Name,” so calling search() with the Japanese name returned ten results none of which matched “Kimi no Na wa.,” prompting not_found.html to render. To fix this, I created a dict to cache all previous searches so that in def anime() I can simply look up the needed information, which is far more consistent and reliable. I also chose to use IDs rather than titles. IDs are unique to each anime, whereas titles can be unreliable—especially when they mix Japanese and English.

In functions.py, I set up my API calls, similar to Problem Set 9 (Finance). I initially used the Basic plan, which only allows 100 requests per day, but during development I exceeded that limit and my access was suspended. To continue doing the project without interruption, I upgraded to the Ultra monthly subscription for $8, which provides a higher daily quota.