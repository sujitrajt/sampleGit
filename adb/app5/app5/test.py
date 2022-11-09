a = ['rabbit','say']
b = ['noth', '_very_', 'remark', 'alic', 'think', '_very_', 'much', 'way', 'hear', 'rabbit', 'say', '"', 'oh', 'dear']

match = list()
for i in a:
    for j in b:
        if i==j:
            match.append(i)
print(match)
            
