
def detect_failed_logins(count):
    if count>3:
        return {"threat":"Brute Force Attack","score":90}
    return {"threat":"Normal","score":0}
