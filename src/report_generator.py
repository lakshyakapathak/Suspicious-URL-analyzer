rule_messages={"rule_ip_present":"URL uses a raw IP address instead of a domain name.","rule_at_symbol_present":"URL contains an @ symbol, which can hide the real destination of the URL.",
               "rule_no_https":"URL does not use HTTPS","rule_multiple_hyphens":"The domain contains multiple hyphens, which is uncommon is legitimate URLs."
               ,"rule_suskeyword_count":"URL contains suspicious keywords.","rule_lengthof_url":"URL is unusually long",
               "rule_manydots":"The domain contains an unusually high number of subdomains."}
def report_generator(url,score,level,triggered_rules):
    print("Given URL->",url)
    print("Risk Score",score)
    print("Risk Level",level)
    if triggered_rules:
        print("Reasons for the score:")
        for r_name,points in triggered_rules:
            message=rule_messages[r_name]
            print(message,"-",points)
    else:
        print("No suspicious indicators were detected.")

if __name__ == "__main__":
    report_generator(
        "http://129.186.3.1/login",
        43,
        "HIGH",
        [("rule_ip_present", 25), ("rule_no_https", 15), ("rule_manydots", 2), ("rule_suskeyword_count", 1)]
    )
    report_generator("https://accounts.google.com/v3/signin/challenge/pwd?TL=ADG-GRT34RzbVnCEMsMWmcti7q_b0we-Zm7EXTKnZOsHRxGTYnHbdDxnkP-S9mvf&authuser=0&checkConnection=youtube%3A381&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1OkfqjsHz9OsFc74qx7p5q_Hfs6wp1EVlVQJtYvvT5vM%2Fedit%3Fgid%3D0&dsh=S-1022493391%3A1790431605363507&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1OkfqjsHz9OsFc74qx7p5q_Hfs6wp1EVlVQJtYvvT5vM%2Fedit%3Fgid%3D0&ltmpl=sheets&osid=1&pstMsg=1&service=wise",
        3 ,"LOW",
     [('rule_lengthof_url', 2), ('rule_suskeyword_count', 1)])

