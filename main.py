import requests, feedparser,pypandoc
from readability import Document
from fetched import fetched_links

def get_links_from_rss(rss_page):
    feed = feedparser.parse(rss_page)
    links = [entry.link for entry in feed.entries]
    
    return links

def get_webpage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        # soup = BeautifulSoup(response.content, 'html.parser')        
        return response.content
    else:
        # If the request was unsuccessful, print an error message
        print(f"Failed to retrieve webpage: {response.status_code} , {url}")
        return None

sources = [
    {
        "link": "https://theverge.com/rss/index.xml",
        "name": "The Verge"
    },
    {
        "link": "https://prod-qt-images.s3.amazonaws.com/production/prothomalo-bangla/feed.xml",
        "name": "Prothom Alo"
    }
]


for source in sources:
    rss_page = get_webpage(source["link"])
    source_name = source["name"]
    links = get_links_from_rss(rss_page)

    epub_content=""

    for link in links:
        if link not in fetched_links:
            test_page = get_webpage(link)
            if test_page:
                doc = Document(test_page)
            
                if source_name == "The Verge":
                    title = doc.title().replace(" - The Verge","")
                else: 
                    title = doc.title()
                # output = pypandoc.convert_text(doc.summary() ,to="markdown_strict", outputfile=f"/home/joy/Synced/Notes/ReadLater/Articles/Verge/{title}.md", format="html", extra_args=["--wrap=none"])
                #  epub
                epub_content += f"""
                <h1>{title}</h1>
                {doc.summary()}
                """
                
                fetched_links.append(link)


    output_epub = pypandoc.convert_text(epub_content ,to="epub", outputfile=f"/home/joy/Synced/Books/{source_name}.epub", format="html", extra_args=["--wrap=none"])    

    # with open(f"/home/joy/Dev/apps/automation/verge-rss/fetched_{source_name}.py", "w") as output_file:
        # output_file.write(f"fetched_links={fetched_links}")

