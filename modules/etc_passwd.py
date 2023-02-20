
from sysinfo_lib import parseCharDelimitedTable, tableToDict

def parser(stdout, stderr):
    columnsNames = ['username', 'password', 'uid', 'gid', 'idInfo', 'homeDir', 'shell']
    output = parseCharDelimitedTable(stdout, ':', columnsNames)
    output = tableToDict(output, 'username')
    outputa=[]
    for k,v in output.items():
        outputa.append(v)
    return {'output': outputa}

def register(main):
    main['etc_passwd'] = {
        'cmd': 'cat /etc/passwd',
        'description': 'Attributes of each user or account on a computer',
        'parser': parser
    }
