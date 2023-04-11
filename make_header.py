def make_header(str, h=1):
    return f"<h{h}>{str}</h{h}>"

print(make_header("Today"))
print(make_header("Read more", 2))
