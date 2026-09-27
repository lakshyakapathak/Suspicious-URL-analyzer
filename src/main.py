from url_validator import url_validator
from feature_extractor import feature_extractor
from risk_analyzer import analyze
from report_generator import report_generator
def main():
    ans="y"
    while ans=="y":

        url= input("Enter a URL to analyze:")
        is_valid,message= url_validator(url)
        if not is_valid:
           print("Error",message)
           ans=input("Do you want to check another URL?:y/n")
           continue
        Features=feature_extractor(url)
        score,level,triggered_rules=analyze(Features)
        report_generator(url,score,level,triggered_rules)
        print()
        ans=input("Do you want to check another URL?:y/n")

if __name__=="__main__":
    main()

