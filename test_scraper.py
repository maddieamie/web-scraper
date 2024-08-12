import pytest
from playwright.async_api import Page, async_playwright, expect
from scraperlab.scraper import DataHolder


@pytest.mark.asyncio
async def test_example():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://en.wikipedia.org/wiki/Spring-heeled_Jack")

        await expect(page.locator("#mw-content-text")).to_contain_text(
            "The Lord Mayor himself was in two minds about the affair: he thought \"the greatest exaggerations\" had been made, and that it was quite impossible \"that the ghost performs the feats of a devil upon earth\", but on the other hand someone he trusted had told him of a servant girl at Forest Hill who had been scared into fits by a figure in a bear's skin; he was confident the person or persons involved in this \"pantomime display\" would be caught and punished.[9] The police were instructed to search for the individual responsible, and rewards were offered.[citation needed]"
        )
        await expect(page.locator("#mw-content-text")).to_contain_text(
            "Perhaps the best known of the alleged incidents involving Spring-heeled Jack were the attacks on two teenage girls, Lucy Scales and Jane Alsop. The Alsop report was widely covered by the newspapers, including a piece in The Times,[11] while fewer reports appeared in relation to the attack on Scales. The press coverage of these two attacks helped to raise the profile of Spring-heeled Jack.[citation needed]"
        )
        await expect(page.locator("#mw-content-text")).to_contain_text(
            "The Times reported the alleged attack on Jane Alsop on 2 March 1838 under the heading \"The Late Outrage at Old Ford\".[11] This was followed with an account of the trial of one Thomas Millbank, who, immediately after the reported attack on Jane Alsop, had boasted in the Morgan's Arms that he was Spring-heeled Jack. He was arrested and tried at Lambeth Street court. The arresting officer was James Lea, who had earlier arrested William Corder, the Red Barn Murderer. Millbank had been wearing white overalls and a greatcoat, which he dropped outside the house, and the candle he dropped was also found. He escaped conviction only because Jane Alsop insisted her attacker had breathed fire, and Millbank admitted he could do no such thing. Most of the other accounts were written long after the date; contemporary newspapers do not mention them.[citation needed]"
        )
        await expect(page.locator("#mw-content-text")).to_contain_text(
            "But, even as his fame was growing, reports of Spring-heeled Jack's appearances became less frequent if more widespread. In 1843, however, a wave of sightings swept the country again. A report from Northamptonshire described him as \"the very image of the Devil himself, with horns and eyes of flame\", and in East Anglia reports of attacks on drivers of mail coaches became common. In July 1847 \"a Spring-heeled Jack investigation\" in Teignmouth, Devon led to a Captain Finch being convicted of two charges of assault against women during which he is said to have been \"disguised in a skin coat, which had the appearance of bullock's hide, skullcap, horns and mask\".[16] The legend was linked with the phenomenon of the \"Devil's Footprints\" which appeared in Devon in February 1855.[citation needed]"
        )
        await expect(page.locator("#mw-content-text")).to_contain_text(
            "The Marquess was frequently in the news in the late 1830s for drunken brawling, brutal jokes and vandalism, and was said to do anything for a bet; his irregular behaviour and his contempt for women earned him the title \"the Mad Marquis\", and it is also known that he was in the London area by the time the first incidents took place. In 1880 he was named as the perpetrator by E. Cobham Brewer, who said that the Marquess \"used to amuse himself by springing on travellers unawares, to frighten them, and from time to time others have followed his silly example.\"[30][31] In 1842, the Marquess married and settled in Curraghmore House, County Waterford, and reportedly led an exemplary life until he died in a riding accident in 1859.[citation needed]"
        )
        await expect(page.locator("#mw-content-text")).to_contain_text(
            "Fortean authors, particularly Loren Coleman[35] and Jerome Clark,[36] list \"Spring-heeled Jack\" in a category named \"phantom attackers\", with another well-known example being the \"Mad Gasser of Mattoon\". Typical \"phantom attackers\" appear to be human, and may be perceived as prosaic criminals, but may display extraordinary abilities (as in Spring-heeled Jack's jumps, which, it is widely noted, would break the ankles of a human who replicated them) and/or cannot be caught by authorities. Victims commonly experience the \"attack\" in their bedrooms, homes or other seemingly secure enclosures. They may report being pinned or paralysed, or on the other hand describe a \"siege\" in which they fought off a persistent intruder or intruders. Many reports can readily be explained psychologically, most notably as the \"Old Hag\" phenomenon, recorded in folklore and recognised by psychologists as a form of hallucination. In the most problematic cases, an \"attack\" is witnessed by several people and substantiated by some physical evidence, but the attacker cannot be verified to exist.[citation needed]"
        )
        await expect(page.locator(".noprint > i > a").first).to_be_visible()


def test_dataholder_get_citations_needed_count():
    new = DataHolder()
    new_url = 'https://en.wikipedia.org/wiki/Spring-heeled_Jack'

    expected = 7
    actual = new.get_citations_needed_count(new_url)
    assert actual == expected


def test_dataholder_url():
    boo = DataHolder()
    new_url = 'https://en.wikipedia.org/wiki/Spring-heeled_Jack'
    boo.get_citations_needed_count(new_url)

    expected = new_url
    actual = boo.url
    assert actual == expected


