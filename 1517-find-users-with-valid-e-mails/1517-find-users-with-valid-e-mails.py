import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    v_mail=users[users['mail'].str.match('^[a-zA-Z][A-Za-z0-9._-]*@leetcode\.com$')]
    return v_mail