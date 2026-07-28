import requests
import urllib.parse
from typing import Dict, Any

class WebSearchExtension:
    """Extension to perform web search via DuckDuckGo Instant Answer API."""

    def __init__(self):
        self.api_url = "https://api.duckduckgo.com/"
        self.query_template = "https://api.duckduckgo.com/?q={query}&format=json&no_html=1&no_redirect=1"

    def parse(self, data: Dict[str, Any]) -> str:
        """Parse DuckDuckGo JSON response into readable output."""
        if not data.get("AbstractText"):
            return "No results found."
        response = []
        response.append("🔍 **Web Search:**")
        response.append(f"✅ **Result:** {data['AbstractText']}")
        if data.get("AbstractURL"):
            response.append(f"🌐 **Source:** [Link]({data['AbstractURL']})\n")
        else:
            response.append("No source link provided.\n")
        return "\n".join(response.strip())

    def search(self, query: str) -> str:
        try:
            encoded_query = urllib.parse.quote(query)
            search_url = self.query_template.format(query=encoded_query)
            response = requests.get(search_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return self.parse(data)
        except Exception as e:
            return f"❌ Search failed: {e}"

def handle_query(query: str) -> str:
    """Main entry point for the extension."""
    ext = WebSearchExtension()
    return ext.search(query)
