#Email to Google Calendar

The main purpose of this app is to parse the events from subscription emails and automatically upload them in the user's google calendar.

The whole app was divided into four distinct parts:
* [Scrape the specified emails using an IMAP connection to the mail client.](#email)
* [Crawl the saved emails to get only the necessary data in them.](#scrapy)
* [Place the scraped data inside a database.](#scrapy)
* [Call those scraped data from the database to serve as input to Google Calendar API.](#database and api)
* [Schedule to call all these weekly for the calendar to be updated.](#bashscript and crontab)

## How to use
#### Dependendies Required that are normally not included in the initial python setup:
#####On connecting using IMAP4 Protocol:
* getpass

#####On crawling the html files and using the database:
* scrapy
* SQLAlchemy
* psycopg2

#####On calling the Google Calendar api:
* httplib2
* apiclient
* oath2client

<a id="email"></a>

####Scrape the mail account
Upon running the app in the "Email Scraping" folder, Google will notify the user through email that an unsecured app is trying to access the account. This is due to the fact that I still havent created the oath2 which Google recommends to have for every app that accesses its services. The user can simply change the setting of his account to allow the access of 'less secure apps' just for this. The subject emails will then be saved to the local directory, [out_dir](https://github.com/SiliconValleyInsight/svi-training-a/tree/master/code-samples/week4/SVI%20Email%20to%20Calendar/Email%20Scraping/out_dir).

To run this, simply place the following command in the terminal:

    python email_scraper.py

#####reference links:
*   [How can I get an email message's text content using python?](How can I get an email message's text content using python?)
*   [18.1.1. email.message: Representing an email message](https://docs.python.org/2/library/email.message.html)
*   [What is Multipart sending and why should I do this](https://www.interspire.com/support/kb/questions/563/What+is+multipart+sending+and+why+should+I+do+this%3F)
*   [How to get attachments from emails and save it locally](http://stackoverflow.com/questions/18497397/how-to-get-csv-attachment-from-email-and-save-it)
*   [IMAP4 Library](http://pymotw.com/2/imaplib/)
*   [Less Secure Apps](https://www.google.com/settings/security/lesssecureapps)
*   [Fetching all messages since last check with Python + Imap](https://blog.jtlebi.fr/2013/04/12/fetching-all-messages-since-last-check-with-python-imap/)
*   [Gmail blocks less secure apps](http://www.ghacks.net/2014/07/21/gmail-starts-block-less-secure-apps-enable-access/)

<a id="scrapy"></a>

####Scrape data out of the Email
Once the html part of the email has been saved, we can now get the contents of the email using Scrapy in folder [my_scraper](https://github.com/SiliconValleyInsight/svi-training-a/tree/master/code-samples/week4/SVI%20Email%20to%20Calendar/my_scraper) folder.

To start this, go inside the my_scraper folder and run the command:

    scrapy crawl crunchbaseevents_spider
    scrapy crawl crunchbaseevents_others_spider
    scrapy crawl crunchbaseevents_accelerator_spider

Scrapy is the the name of the scraping framework we use. Crawl is the command for the spider to start crawling the website. The last entry is the name of the spider specified in the spider app. Running the command will place all the scraped data inside the database.

For a more detailed instructions, please go to the link below:

[Introduction to Web Scraping using Scrapy and Postgres](http://newcoder.io/scrape/intro/)

For further reference:
*   [python scrapy on offline local data](http://stackoverflow.com/questions/19385837/python-scrapy-on-offline-local-data)

<a id="database and api"></a>
####Query from the database, edit the result, then use that to post events through the google calendar api.
On querying the database, we use this app named, [database_query.py](https://github.com/SiliconValleyInsight/svi-training-a/blob/master/code-samples/week4/SVI%20Email%20to%20Calendar/SVI%20Calendar/database_query.py) inside folder [SVI Calendar](https://github.com/SiliconValleyInsight/svi-training-a/tree/master/code-samples/week4/SVI%20Email%20to%20Calendar/SVI%20Calendar). It obtains, upon running, all the info inside the database used by Scrapy then formats it in a way that can be read by the google calendar api.

The dates are edited to fit the api by calling the script named [stringtodate.py](https://github.com/SiliconValleyInsight/svi-training-a/blob/master/code-samples/week4/SVI%20Email%20to%20Calendar/SVI%20Calendar/stringtodate.py)

The final data is then used by the script [upcoming.py](https://github.com/SiliconValleyInsight/svi-training-a/blob/master/code-samples/week4/SVI%20Email%20to%20Calendar/SVI%20Calendar/upcoming.py) which accesses the api of google. The other scripts named [client_secret.json](https://github.com/SiliconValleyInsight/svi-training-a/blob/master/code-samples/week4/SVI%20Email%20to%20Calendar/SVI%20Calendar/client_secret.json) and [credentials.dat](https://github.com/SiliconValleyInsight/svi-training-a/blob/master/code-samples/week4/SVI%20Email%20to%20Calendar/SVI%20Calendar/credentials.dat) are used by the api for its oath2 authentication method and can be obtained by following the instructions on the google developer site.

To run this, simply call:

    python upcoming.py
        
Reference links:
*   [How to install and use postgresql](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04)
*   [Postgresql Tutorial](http://zetcode.com/db/postgresqlpythontutorial/)
*   [Simple SQLAlchemy Tutorial](http://www.blog.pythonlibrary.org/2012/07/01/a-simple-sqlalchemy-0-7-0-8-tutorial/)
*   [sqlalchemy or psycopg2](http://stackoverflow.com/questions/8588126/sqlalchemy-or-psycopg2)
*   [is it possible to check or change postgresql-user-password](http://stackoverflow.com/questions/12720967/is-possible-to-check-or-change-postgresql-user-password)
*   [SQLAlchemy 0.9 Documentation Object Relational Tutorial](http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html)
*   [Introduction to the Google Calendar API (HOWTO)](http://www.oeey.com/2014/10/google-calendar-api.html)
*   [Oath2.0 Google APIs Client Library for Python](https://developers.google.com/api-client-library/python/guide/aaa_oauth#flow_from_clientsecrets)
*   [Google Calendar API Insert Events](https://developers.google.com/google-apps/calendar/v3/reference/events/insert)
*   [Using Google Calendar API v 3 with Python](http://stackoverflow.com/questions/14058964/using-google-calendar-api-v-3-with-python)

<a id="bashscript and crontab"></a>
###Bash Scripts and CronTab
Instead of running all these separate apps by yourself, we can create a bash script and place that inside the crontab. I still havent done this for the whole app and i've only written one for the spider just to see if it works. To run it, get inside the my_scraper folder and run the following command:

    source scrape.sh
The specific command should be source and not sh because we will be working in a virtualenv and the script would not work if the latter was used.

Reference links:
*   [Beginners guide to shell scripting](http://www.howtogeek.com/67469/the-beginners-guide-to-shell-scripting-the-basics/)
*   [HowTo: Run the .sh File Shell Script In Linux / UNIX](http://www.cyberciti.biz/faq/run-execute-sh-shell-script/)
*   [Linux and Unix crontab command](http://www.computerhope.com/unix/ucrontab.htm)
*   [What are cron and crontab, and how do I use them?](https://kb.iu.edu/d/afiz)
*   [Activating a virtualenv using a shell script doesnt seem to work.](http://stackoverflow.com/questions/7369145/activating-a-virtualenv-using-a-shell-script-doesnt-seem-to-work)

##To Do list
* <s>Add links to the docs.</s> 03/19/2015
* <s>Fix format of other two spiders.</s> 04/05/2015
* Create a function that would check if the email have already been scraped or not.
* Create another spider that can also get the details of smaller events.
* Create a script that could call a database function to remove duplicate entries.
* Create a bash script to run all these automatically
* Place an oath2 on the IMAP4 script
* Check whether it would be better if we just use the Gmail API instead of the IMAP4 Script.
