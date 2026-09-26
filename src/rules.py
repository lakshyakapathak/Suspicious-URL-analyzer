def rule_ip_present(features):
    return 25 if features["has_ip"] else 0
def rule_at_symbol_present(features):
    return 20 if features["has_at_symbols"] else 0
def rule_no_https(features):
    return 15 if not features["uses_https"] else 0
def rule_multiple_hyphens(features):
    points_per_hyphen=2
    max_points=10
    score=features["numberof_hyphens"]*points_per_hyphen
    return min(score,max_points)
def rule_suskeyword_count(features):
    point=1
    max_points=5
    score=features["suspicious_keywordcount"]*point
    return min(score,max_points)
def rule_lengthof_url(features):
    return 2 if features["length"]>100 else 0
def rule_manydots(features):
    points=2
    max_points=10
    baseline=2
    x=max(0,features["numberof_dots"]-baseline)
    score=x*points
    return min(score,max_points)

rules=[rule_ip_present,rule_at_symbol_present,rule_lengthof_url,rule_no_https,rule_manydots,rule_suskeyword_count,rule_multiple_hyphens]

if __name__ == "__main__":
    from feature_extractor import feature_extractor
    testurls = ["https://www.google.com/search?q=test","https://shop.royalchallengers.com/merchandise",
        "http://192.168.1.1/login",
        "https://secure-login-verify-account.example.com/update"]
    for u in testurls:
        features = feature_extractor(u)
        print(u)
        for rule in rules:
            print(f"  {rule.__name__}: {rule(features)}")
        print()
    #test cases to decide on risk levels
    TESTCASES = [
    # Category 1: Clearly legitimate, short
    "https://www.google.com",
    "https://github.com/torvalds/linux",
    "https://music.youtube.com/watch?v=CvlWnG1yiyQ",
    "https://raptor.martincarlisle.com/",

    # Category 2: Clearly legitimate, long/complex
    "https://www.simonandschuster.com/books/21-Days-of-Fear/Herve-Commere/9798347119615",
    "https://www.amazon.com/s?k=laptop+stand&ref=nb_sb_noss_2",
    "https://www.myntra.com/sweaters/h%26m/hm-women-ribbed-pullover/45333756/buy",

    # Category 3: Legitimate but with a superficial red flag
    "https://accounts.google.com/signin/v2/identifier",
    "https://www.paypal.com/signin",
    "https://yonobusiness.sbi.bank.in/yonobusinesslogin",

    # Category 4: Classic phishing pattern — IP-based 
    "http://192.168.1.1/login",
    "http://45.33.32.156/verify-account",
    "http://103.45.22.9/sbi-verify-account",

    # Category 5: Classic phishing pattern — @ symbol trick 
    "http://accounts-google.com@evil-site.com/",
    "http://paypal.com@192.168.5.5/secure",

    #Category 6: Classic phishing pattern — keyword + hyphen stuffing
    "https://secure-login-verify-account.example.com/update",
    "http://paypal-secure-update-account.info/verify",
    "http://yono-sbi-secure-login.xyz/update-kyc",

    # Category 7: Ambiguous / borderline
    "https://mybank-secure-portal.com/dashboard",
    "http://user@fake-bank.com/verify",
    "http://sbi.bank.in.verify-account-now.com/login",
    "http://127.0.0.1:52400/signin?nonce=En2c5OlTxCLzJ7fdo30hAQ==",
]
    for p in TESTCASES:
        features = feature_extractor(p)
        print(p)
        for rule in rules:
            print(f"  {rule.__name__}: {rule(features)}")
        print()


