from urllib.parse import urlparse 
def url_validator(url):
    url=url.strip()
    if not url:
        return False,"Invalid URL"
    else:
        parsed=urlparse(url)
        Scheme=parsed.scheme 
        Netloc=parsed.netloc
        if Scheme not in("http","https"):
            return False,"Unsupported Scheme"
        if not Netloc:
            return False, "Host is missing"
        return True, "Valid URL"
    
if __name__ == "__main__":
    urls_for_test = [ "https://www.google.com",
        "http://example.com/page","https://mail.google.com/mail/u/0/#inbox",
        "ftp://files.example.com",
        "not a url at all",
        "",
        "   https://spaced.com   "]
    for i in urls_for_test:
        print(i, "->", url_validator(i))