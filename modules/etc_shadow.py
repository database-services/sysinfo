
from sysinfo_lib import parseCharDelimitedTable, tableToDict

def parser(stdout, stderr):
    columnsNames = ['username', 'password', 'lastPasswordChange', 'minimum', 'maximum', 'warn', 'inactive', 'expire']
    output = parseCharDelimitedTable(stdout, ':', columnsNames)
    output = tableToDict(output, 'username')
    outputa=[]
    for k,v in output.items():
        outputa.append(v)
    return {'output': outputa}

def register(main):
    main['etc_shadow'] = {
        'cmd': 'cat /etc/shadow',
        'description': 'Shadow database of the passwd file',
        'parser': parser
    }
