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

def list_files(startpath):
    import os
    dump = ''
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        dump += '{}{}/\n'.format(indent, os.path.basename(root))
        sub = ' ' * 4 * (level + 1)
        for f in files:
            import pe_check
            fl = f.lower()
            if fl.endswith('.dll') or fl.endswith('.exe'):
                dump += '{}{}: {}\n'.format(sub, f, pe_check.get_pe_machine(path.join(root, f)))
            else:
                dump += '{}{}\n'.format(sub, f)
    return dump

def get_plugin_dump(install_info):
    plugin_dump = {}
    for k in install_info:
        plugin_path = path.join(k, 'plugins')
        plugin_dump[plugin_path] = list_files(plugin_path)

    return plugin_dump

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

    plugin_dump = get_plugin_dump(install_info)
    return exceptions, plugin_dump