d={'name':'mahmood khali','coures':'python','fees':200000}
del d['name']
print(d)
for n in d.keys():
    print(n)
    for v in d.values():
        print(v)
        for n,v in d.items():
            print(n,v)