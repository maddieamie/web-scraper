
from playwright.sync_api import sync_playwright


class DataHolder:

    def __init__(self, data_list=[], num_of_citations=0, url=""):
        self.data_list = data_list
        self.num_of_citations = num_of_citations
        self.url = url

    def __repr__(self):
        return f"DataHolder(data_list={self.data_list}, num_of_citations={self.num_of_citations}, url='{self.url}')"

    def __iter__(self):
        return iter(self.data_list)

    def update_url(self, new_url):
        # url is to be updated with instance of class, with each new url.
        self.url = new_url

    def get_citations_needed_count(self, url_string: str) -> int:

        self.update_url(url_string)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, slow_mo=1000)
            page = browser.new_page()
            page.goto(url_string)

        # citation needed span full xpath example
        # //*[@id="mw-content-text"]/div[1]/p[13]/sup[2]/i/a/span
        # //span//ancestor::p is the closest p element
        # more generic inheritance xpath with citation needed text
            citation_needed_spans = page.locator('//p//sup//span[text()="citation needed"]')
            count = citation_needed_spans.count()

        # combination of selectors for citation needed
        # find the parent of the child?

        # for paragraphs that are ancestors of citation_needed_span, get all text contents
        # nth is each instance of citation_needed_span xpath

            for i in range(count):
                paragraph = citation_needed_spans.nth(i).locator('xpath=ancestor::p').text_content()
                self.data_list.append(paragraph)
            self.num_of_citations = len(self.data_list)

            browser.close()
        return len(self.data_list)

    def return_string_formatter(self):
        return_list = []
        counter = 0
        for citation in self.data_list:
            counter += 1
            new_format = f"Citation {counter}, Paragraph parent:{citation}"
            return_list.append(new_format)
        return return_list

    def get_citations_needed_report(self, url_string: str) -> str:
        # the return string should be formatted with each citation listed in the order found.

        if url_string != self.url:
            self.get_citations_needed_count(url_string)
            return_deets = self.return_string_formatter()
        else:
            return_deets = self.return_string_formatter()
        return "\n".join(return_deets)


if __name__ == '__main__':

    new = DataHolder()
    new_url = 'https://en.wikipedia.org/wiki/Spring-heeled_Jack'
    new.get_citations_needed_count(new_url)
    new.get_citations_needed_report(new_url)
