from sys import stdout
from os import path
import pe_check

def start_rule(r):
    stdout.write('Rule: {0}...'.format(r))
    return r

def stop_rule(n):
    stdout.write('Done ({0} exceptions).\n'.format(n))

def check_install_machine_types(install_info):
    rule = start_rule("verify installation machine types")

    dupe_exc_message = 'multiple installations of machine type {0} found: {1}'
    dupe_res_message = 'remove/uninstall unnecessary installation'
    exc = []
    installed_machines = {}
    for k, v in install_info.items():
        m = v['machine']
        if m in installed_machines:
            installed_machines[m]['candidates'].append(k)
            installed_machines[m]['dupe'] = True
        else:
            installed_machines[m] = dict(
                candidates=[k],
                dupe=False
            )

    for k, v in installed_machines.items():
        if v['dupe']:
            exc.append(dict(
                exception=dupe_exc_message.format(k, v['candidates']),
                resolution=dupe_res_message,
                type='Warning'
            ))

    stop_rule(len(exc))

    return rule, exc

def check_plugins(install_info):
    rule = start_rule('verify plugins directory')

    exc = []

    for k, v in install_info.items():
        plugin_path = path.join(k, 'plugins')
        if not path.isdir(plugin_path):
            exc.append(dict(
                exception='''missing plugin directory in {0}'''.format(k),
                resolution='reinstall OBS to {0}'.format(k),
                type='Fatal'
            ))

        import os
        for f in os.listdir(plugin_path):
            pf = path.join(plugin_path, f)
            if path.isfile(pf) and f.lower().endswith('.dll'):
                mt, ass = pe_check.get_pe_machine_type(pf)
                m = pe_check.get_pe_machine_string(mt, ass)
                if (ass):
                    exc.append(dict(
                        exception='plugin file {0} expected {1} but was {2}'.format(pf, v['machine'], m),
                        resolution='remove {0} and reinstall the plugin that contains this file'.format(f),
                        type='Error'
                    ))
                elif m != v['machine']:
                    exc.append(dict(
                        exception='plugin file {0} expected {1} but was {2}'.format(pf, v['machine'], m),
                        resolution='reinstall {0} version of plugin {1}'.format(v['machine'], f),
                        type='Error'
                    ))
            else:
                if not path.isdir(pf):
                    exc.append(dict(
                        exception='non-dll file {0} found in plugins base directory {1}'.format(pf, plugin_path),
                        resolution='verify that this file is needed in the plugins directory',
                        type='Notification'
                    ))

    stop_rule(len(exc))

    return rule, exc
