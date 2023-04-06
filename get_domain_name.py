def get_domain_name(url):
    res = url.replace("http://", "").replace("https://","").split('.')
    if res[0] == "www":
        return res[1]
    else:
        return res[0]
