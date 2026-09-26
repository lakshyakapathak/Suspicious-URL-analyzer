from rules import rules 
def analyze(features):
    total_score=0
    triggered_rules=[]
    for r in rules:
       points=r(features)
       if points>0:

        total_score+=points
        triggered_rules.append((r.__name__,points))
    if total_score>=35:
       
       level="HIGH"
    elif total_score>=15:
        level="MEDIUM"
    else:
        level="LOW"

    return total_score,level,triggered_rules

if __name__ == "__main__":
    from feature_extractor import feature_extractor

    urlsfortest = [
        "https://www.google.com",
        "http://192.168.1.1/login",
        "https://secure-login-verify-account.example.com/update",
        "https://accounts.google.com/v3/signin/challenge/pwd?TL=ADG-GRT34RzbVnCEMsMWmcti7q_b0we-Zm7EXTKnZOsHRxGTYnHbdDxnkP-S9mvf&authuser=0&checkConnection=youtube%3A381&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1OkfqjsHz9OsFc74qx7p5q_Hfs6wp1EVlVQJtYvvT5vM%2Fedit%3Fgid%3D0&dsh=S-1022493391%3A1790431605363507&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1OkfqjsHz9OsFc74qx7p5q_Hfs6wp1EVlVQJtYvvT5vM%2Fedit%3Fgid%3D0&ltmpl=sheets&osid=1&pstMsg=1&service=wise",
    ]
    for u in urlsfortest:
        features = feature_extractor(u)
        score, level, triggered = analyze(features)
        print(u)
        print(f"  Score: {score}  Level: {level}")
        print(f"  Triggered: {triggered}")
        print()

