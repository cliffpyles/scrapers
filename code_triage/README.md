# CodeTriage
This is a Scrapy project to scrape repos from codetriage.com.

## Spiders

This project contains one spider and you can list it using the `list`
command:

    $ scrapy list
    code-triage

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl code-triage

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl code-triage -o repos.json
