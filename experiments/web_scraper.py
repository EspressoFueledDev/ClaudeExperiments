"""
Web Scraper with Claude Analysis

Scrapes web pages and uses Claude to analyze/summarize the content.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import requests
from bs4 import BeautifulSoup
from utils.claude_helper import call_haiku


def scrape_webpage(url):
    """
    Scrape text content from a webpage

    Args:
        url: The webpage URL to scrape

    Returns:
        dict: Contains title, text content, and links
    """
    print(f"Scraping: {url}")

    # Set a user agent to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title
        title = soup.find('title')
        title_text = title.get_text().strip() if title else "No title"

        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()

        # Get text content
        text = soup.get_text()

        # Clean up text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)

        # Extract links
        links = []
        for link in soup.find_all('a', href=True):
            links.append({
                'text': link.get_text().strip(),
                'href': link['href']
            })

        return {
            'url': url,
            'title': title_text,
            'content': text[:5000],  # Limit to first 5000 chars
            'links': links[:10],  # First 10 links
            'success': True
        }

    except requests.RequestException as e:
        return {
            'url': url,
            'error': str(e),
            'success': False
        }


def analyze_with_claude(scraped_data, analysis_type="summarize"):
    """
    Use Claude to analyze scraped content

    Args:
        scraped_data: Dict from scrape_webpage()
        analysis_type: "summarize", "extract_facts", or "sentiment"

    Returns:
        str: Claude's analysis
    """
    if not scraped_data['success']:
        return f"Error: {scraped_data.get('error', 'Unknown error')}"

    content = scraped_data['content']
    title = scraped_data['title']

    prompts = {
        'summarize': f"""Summarize this webpage in 3-5 bullet points:

Title: {title}

Content:
{content}

Provide a concise summary focusing on the main points.""",

        'extract_facts': f"""Extract the key facts and statistics from this webpage:

Title: {title}

Content:
{content}

List the important facts, numbers, and data points.""",

        'sentiment': f"""Analyze the tone and sentiment of this webpage:

Title: {title}

Content:
{content}

Describe the overall tone (professional, casual, promotional, etc.) and sentiment."""
    }

    prompt = prompts.get(analysis_type, prompts['summarize'])

    print(f"\nAnalyzing with Claude ({analysis_type})...")
    result = call_haiku(prompt, max_tokens=2048)

    return result


def scrape_and_analyze(url, analysis_type="summarize"):
    """
    Complete workflow: scrape and analyze

    Args:
        url: Webpage to scrape
        analysis_type: Type of analysis to perform
    """
    print("=" * 80)
    print(f"WEB SCRAPER + CLAUDE ANALYSIS")
    print("=" * 80)

    # Scrape the webpage
    data = scrape_webpage(url)

    if not data['success']:
        print(f"\nError scraping {url}")
        print(f"Error: {data['error']}")
        return

    # Display basic info
    print(f"\nTitle: {data['title']}")
    print(f"Content length: {len(data['content'])} characters")
    print(f"Links found: {len(data['links'])}")

    # Analyze with Claude
    analysis = analyze_with_claude(data, analysis_type)

    print("\n" + "=" * 80)
    print(f"CLAUDE'S ANALYSIS ({analysis_type.upper()})")
    print("=" * 80)
    print(analysis)

    return data, analysis


if __name__ == "__main__":
    # Example usage

    # Example 1: Scrape and summarize a blog post
    url = "https://www.anthropic.com/news"
    scrape_and_analyze(url, analysis_type="summarize")

    # Uncomment to try other examples:

    # Example 2: Extract facts from a Wikipedia article
    # url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    # scrape_and_analyze(url, analysis_type="extract_facts")

    # Example 3: Analyze sentiment of a product page
    # url = "https://news.ycombinator.com"
    # scrape_and_analyze(url, analysis_type="sentiment")
