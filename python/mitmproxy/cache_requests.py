from mitmproxy import http, ctx
from cachetools import TTLCache
import re
import os

# Cache with a maximum of 1000 entries, each with a TTL of 1 hour
cache = TTLCache(maxsize=1000, ttl=3600)

# script_dir = os.path.dirname(os.path.abspath(__file__))
# json_path = os.path.join(script_dir, "paths.json")

# with open(json_path, "r") as f:
#     paths = json.load(f)

patterns = os.getenv("MYTILS_PROXY_CACHE_PATTERNS")

if patterns:
    paths = patterns.split(";")
else:
    paths = [".*"]

# Define URL patterns to cache (can be modified to suit your needs)
URL_PATTERNS_TO_CACHE = [re.compile(path) for path in paths]

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url in cache:
        ctx.log.info(f"Cache hit for {flow.request.pretty_url}")
        flow.response = cache[flow.request.pretty_url].copy()
        flow.response.headers["X-Cache-Status"] = "HIT"

def response(flow: http.HTTPFlow) -> None:
    # Modify CORS headers
    flow.response.headers["Access-Control-Allow-Origin"] = "*"
    flow.response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    flow.response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    # Cache responses matching patterns
    for pattern in URL_PATTERNS_TO_CACHE:
        if pattern.match(flow.request.pretty_url) and flow.response.status_code == 200:
            cache[flow.request.pretty_url] = flow.response.copy()
            flow.response.headers["X-Cache-Status"] = "MISS"