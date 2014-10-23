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
            n = f.lower()
            if path.isfile(pf) and n.endswith('.dll'):
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
                    #pdb files are expected
                    if n.endswith('.pdb'):
                        continue
                    exc.append(dict(
                        exception='non-dll file {0} found in plugins base directory {1}'.format(pf, plugin_path),
                        resolution='verify that this file is needed in the plugins directory',
                        type='Notification'
                    ))

    stop_rule(len(exc))

    return rule, exc

def check_clr_plugins(install_info):
    rule = start_rule('verify clr plugins directory')

    exc = []

    for k, v in install_info.items():
        plugin_path = path.join(k, 'plugins')
        if not path.isfile(path.join(plugin_path, 'CLRHostPlugin.dll')):
            # don't need to check
            continue

        clrhost_path = path.join(plugin_path, 'CLRHostPlugin')
        if not path.isdir(clrhost_path):
            exc.append(dict(
                exception='{0} directory does not exist in plugins base directory {1}'.format(clrhost_path, plugin_path),
                resolution='verify that you installed CLRHostPlugin correctly by extracting the dll AND CLRHostPlugin directory',
                type='Error'
            ))
            continue

        interop_path = path.join(clrhost_path, 'CLRHost.Interop.dll')
        if not path.isfile(interop_path):
            exc.append(dict(
                exception='CLRHost.Interop.dll does not exist in CLRHostPlugin directory {0}'.format(clrhost_path),
                resolution='verify that you installed CLRHostPlugin correctly by extracting the dll AND CLRHostPlugin directory',
                type='Error'
            ))
            continue

        import os
        for f in os.listdir(clrhost_path):
            pf = path.join(clrhost_path, f)
            n = f.lower()
            if path.isfile(pf) and n.endswith('.dll'):
                mt, ass = pe_check.get_pe_machine_type(pf)
                m = pe_check.get_pe_machine_string(mt, ass)
                if not ass:
                    exc.append(dict(
                        exception='{0} expected .NET assembly but was {1} native'.format(pf, m),
                        resolution='reinstall the plugin that contains {0}; Only .NET assemblies should be in {1}'.format(f, clrhost_path),
                        type='Error'
                    ))
            else:
                if not path.isdir(pf):
                    #pdb files are expected
                    if n.endswith('.pdb'):
                        continue
                    exc.append(dict(
                        exception='non-dll file {0} found in clr plugin base directory {1}'.format(pf, clrhost_path),
                        resolution='verify that this file is needed in the clr plugins directory',
                        type='Notification'
                    ))

    stop_rule(len(exc))

    return rule, exc