import sys
import os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from url_validator import url_validator
from feature_extractor import feature_extractor,is_ip
from risk_analyzer import analyze

def test_valid_https():
    is_valid,message=url_validator("https://vityarthi.com/student-dashboard")
    assert is_valid==True
def test_invalid_scheme():
    is_valid,message=url_validator("ftp://files.example.com")
    assert is_valid==False
def test_ip_detection_true():
    assert is_ip("192.168.1.1")==True

def test_keyword_count():
    features = feature_extractor("https://secure-login-verify-account.example.com/update")
    assert features["suspicious_keywordcount"]==5

def test_high_risk_ip_url():
    features = feature_extractor("http://192.168.1.1/login")
    score, level, triggered_rules = analyze(features)
    assert level=="HIGH"
    assert score==43