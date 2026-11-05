"""Tells IndexNow engines (Bing, Yandex, Seznam...) that the site's URLs changed. Run it after the GitHub Pages
deploy has finished (the key file must already be online): python3 indexnow.py"""
import json, os, re, urllib.request

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sites", "web")
key = next(f[:-4] for f in os.listdir(OUT) if re.fullmatch(r"[0-9a-f]{32}\.txt", f))
urls = re.findall(r"<loc>([^<]+)</loc>", open(os.path.join(OUT, "sitemap.xml"), encoding="utf-8").read())
host = urls[0].split("/")[2]
body = json.dumps({"host": host, "key": key, "keyLocation": f"https://{host}/{key}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req) as r:
    print(r.status, f"{len(urls)} URLs submitted")  # 200 or 202 = accepted
