import check_obs

def_installs = [
    r"C:\Program Files\OBS",
    r"C:\Program Files (x86)\OBS",
    r"C:\Program Files (x86)\OBS\64bit"
]

def main(argv):
    import argparse
    parser = argparse.ArgumentParser(description='obs installation sanity checker')
    parser.add_argument('-i', "--installation", dest='installs', action='append', default=def_installs)
    args = parser.parse_args(argv[1:])

    from check_obs import check_obs
    exc, plugin_dump = check_obs(args.installs)
    from gui import run_gui
    run_gui(exc, plugin_dump)

if __name__ == "__main__":
    import sys
    main(sys.argv)