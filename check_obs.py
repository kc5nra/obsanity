from os import path

import check_rules
rules = [
    check_rules.check_install_machine_types,
    check_rules.check_plugins,
    check_rules.check_clr_plugins
]

def check_install(install):
    import pe_check
    return dict(
        machine=str(pe_check.get_pe_machine(path.join(install, "obs.exe")))
    )

def check_obs(obs_installations):
    install_info = {}
    for i in obs_installations:
        if path.isdir(i):
            print('Found installation at {0}'.format(i))
            install_info[i] = check_install(i)
        else:
            print('No installation found at {0}\n'.format(i))

    exceptions = list()
    for r in rules:
        e = r(install_info)
        if len(e):
            exceptions.append(e)

    return exceptions