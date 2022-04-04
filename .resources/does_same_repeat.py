a = ['[[:digit:]]+', ':', '[[:digit:]]+', ':', '[[:digit:]]+', ':', '[[:digit:]]+', ':', '[[:digit:]]+', ':', '[[:digit:]]+']
d={}
for k in zip(a[::2],a[1::2]):
	d[k] = d.get(k,0)+1

print(d)