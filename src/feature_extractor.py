from urllib.parse import urlparse
suspicious_keywords=["login","verify","password","update","secure","account"]
def is_ip(Netloc):
        host= Netloc.split(":")[0]
        parts= host.split(".")
        if len(parts)!=4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            if not (0<=int(part)<=255):
                 return False
        return True
def sus_keywords_count(path):
     path=path.lower()
     count=0
     for keyword in suspicious_keywords:
          if keyword in path:
               count+=1
     return count            
def feature_extractor(url):
    parsed=urlparse(url)
    features={}
    features["length"]=len(url)
    features["numberof_dots"]= parsed.netloc.count('.')
    features["uses_https"]= parsed.scheme=="https"
    features["has_at_symbols"]= "@" in url 
    features["numberof_hyphens"]= parsed.netloc.count("-")
    features["has_ip"]= is_ip(parsed.netloc)
    features["suspicious_keywordcount"]=sus_keywords_count(parsed.path+parsed.netloc)
    return features 


if __name__ == "__main__":
     urls_fortest = ["https://www.google.com/search?q=test",
                 "http://192.168.1.1/login","https://secure-login-verify-account.example.com/update",
                 "http://user@fake-bank.com/verify","https://www.simonandschuster.com/books/21-Days-of-Fear/Herve-Commere/9798347119615"]
     for u in urls_fortest:
            print(u)
            print(feature_extractor(u))
            print()
         
        