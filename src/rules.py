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
