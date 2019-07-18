import itertools
from collections import defaultdict

lst = [
    ['2.2.5', '/usr/local/share/dotnet/shared/Microsoft.AspNetCore.All'],
    ['2.2.6', '/usr/local/share/dotnet/shared/Microsoft.AspNetCore.All'],
    ['2.2.5', '/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App'],
    ['2.2.6', '/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App'],
    ['2.2.5', '/usr/local/share/dotnet/shared/Microsoft.NETCore.App'],
    ['2.2.6', '/usr/local/share/dotnet/shared/Microsoft.NETCore.App']
]

{
    "2.2.5": ['/usr/local/share/dotnet/shared/Microsoft.AspNetCore.All/2.2.5',
              '/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App/2.2.5',
              '/usr/local/share/dotnet/shared/Microsoft.NETCore.App/2.2.5'],
    "2.2.6": ['/usr/local/share/dotnet/shared/Microsoft.AspNetCore.All/2.2.6',
              '/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App/2.2.6',
              '/usr/local/share/dotnet/shared/Microsoft.NETCore.App/2.2.6']
}

# d = {}
#
# for a in k:
#     d[a[0]] = [a[1]]

# d = dict(itertools.zip_longest(*iter(k), fillvalue=""))
print(dict(lst))

to_dict = {key[0]: [value[1] + '/' + value[0] for value in lst] for key in lst}

from collections import defaultdict

out = {}
for n, v in lst:
    out.setdefault(n, []).append(v + '/' + n)

dct = dict((a[0], [b[1]+'/'+a[0] for b in lst if b[0] == a[0]]) for a in lst)


from pprint import pprint
pprint(dct)
pprint(out)

