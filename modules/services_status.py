
import re
from sysinfo_lib import parseTable, tableToDict

def parser_services(stdout, stderr):
    output = parseTable(stdout)
    output = tableToDict(output, 'unit')
    outputa=[]
    for k,v in output.items():
        outputa.append(v)
    return {'output': outputa}

def parser_services_params(stdout, stderr):
    output = []
    entry = {}
    service = None
    if stdout:
        for line in stdout.splitlines():
            serviceSearch = re.search(r'^>>>\s*Service:\s*(.*)$', line)
            if serviceSearch:
                service = serviceSearch.group(1).strip()
                if entry:
                    output.append(entry)
                entry = {}

            if service:
                keyValueSearch = re.search(r'^([^=]+)=(.*)$', line)
                if keyValueSearch:
                    entry[keyValueSearch.group(1)] = keyValueSearch.group(2).strip()

    return {'output': output}

def register(main):
    main['services_list'] = {
        'cmd': """systemctl -l --type service --all --plain | grep -i -e ".service\|description" | sed 's/^\s*//g' """,
        'description': 'Displays services with status',
        'parser': parser_services
    }

    main['services_params'] = {
        'cmd': """systemctl -l --type service --all --plain | sed -E 's/^\s*(\\S+.service).*$/\\1/g' | grep -i -e ".service" | xargs -I '{}' sh -c "echo '>>> Service: {}'; systemctl show {} --no-page" """,
        'description': 'Displays services with status',
        'parser': parser_services_params
    }

