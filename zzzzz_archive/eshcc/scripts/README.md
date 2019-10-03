% README for the web scraping code examples
% Jasper Op de Coul & Peter van Huisstede
% [Time-stamp: <2018-02-23 11:27:31 (peter)>]

### Intro

We decided to explain both code examples (steam\_scrape.py and
not\_just\_a\_label.py), because they are quite similar, together in
this file.

### Structure of the Python files
 
The structure of both files is the same (from top to bottom):

- import of Python libraries (sys, csv, os, time, requests, and
  BeautifulSoup) we use
- the base URL(s) of the websites we are working with defined as a
  variable (URL and DETAIL_URL) we can use throughout our program
  (saves a lot of typing and typo's)
- functions we need to do the actual scraping. For the Steam website:
  fetch\_reviews and extract\_content. For the Notjustalabel website:
  fetch\_listing\_page and fetch\_detail\_page. These functions return
  results when "called" with the appropriate arguments or variables:
  - Steam function 'fetch\_reviews' expects a 'page\_number' and returns
    something called 'response.content'
  - Steam function 'extract\_content' expects 'reviews\_data' and
    returns 'contents'
  - Notjustalabel function 'fetch\_listing\_page' expects a
  'page\_number' and returns 'designer_urls'
  - Notjustalabel function 'fetch\_detail\_page' expects a 'page_id'
    and returns a so-called dictionary containing 4 key: value pairs:
    id, name, city, and country.
- The whole circus is set in motion with the part that comes last and
  that starts with the somewhat cryptic sentence "if __name__ ==
  '__main__':". This is a Python convention that states that when run,
  this is where the program starts.

We already noted during the workshop that the programs were not
written top down. And hence the best way to read a program is to start
at the bottom with the main function and follow it's logic.

### The process

The logic of both programs is a little bit different, but that is
because the websites are different. Remember that we spend quite some
time in the browser using the "developer tools" to catch the places
where the content is kept that we are interested in.

This step not only provided us with the data for the URL and
DETAIL\_URL variables we declare at the top of the program files. But
also with the parameters we have to use to get at all the pages we
need visit to extract information. In the case of Notjustalabel we
needed two pieces of information:

  - we needed to extract the so-called 'designer\_urls' from the
  overview pages using 'page\_number';
  - then we use this information, stored in the file on disk called
    'designers.txt' to get to the page per designer to extract the
    information from these pages.

We have annotated the Python source file 'not\_just\_a\_label.py'
(the logic of the Steam example is similar, but with different data)
for you to follow the logic.








