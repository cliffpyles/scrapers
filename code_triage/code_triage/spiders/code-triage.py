# -*- coding: utf-8 -*-
import scrapy


class CodeTriageSpider(scrapy.Spider):
    name = "code-triage"
    start_urls = [
        "https://www.codetriage.com/",
    ]

    def parse(self, response):
        for repo in response.css(".repo-list-with-pagination li.repo-item"):
            yield {
                "title": repo.css("h3.repo-item-title::text").extract_first(),
                "description": repo.css(
                    "p.repo-item-description::text"
                ).extract_first(),
                "issue_count": repo.css("span.repo-item-issues::text")
                .extract_first()
                .replace(" Issues", ""),
                "full_name": repo.css("span.repo-item-full-name::text").extract_first(),
                "details_page": repo.css("a::attr(href)").extract_first(),
                "language": repo.attrib["data-language"],
            }

        next_page_url = response.css("a.next_page::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
