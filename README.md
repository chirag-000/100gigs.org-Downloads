Like most websites with static content, all the files they host are linked somewhere in the source code.

After poking around, I found this [JavaScript file](https://100gigs.org/_nuxt/DuFK2s2m.js) which contains direct links to all their content. The structure is pretty simple - each file has a `relative_path` (showing its filename and folder structure) and a corresponding `download_url`.

All I needed to do was extract these download URLs. You can find them in [download_links.txt](https://github.com/chirag-000/100gigs.org-Downloads/blob/main/download_links.txt) file in this repo.
There are a total of 1386 files!
Just copy and paste any of these URLs into your browser to view/download the content directly. 🎵
