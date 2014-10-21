import struct

IMAGE_FILE_MACHINE_I386=332
IMAGE_FILE_MACHINE_IA64=512
IMAGE_FILE_MACHINE_AMD64=34404

def get_pe_machine(pe_file):
    m, ass = get_pe_machine_type(pe_file)
    return get_pe_machine_string(m, ass)

def get_pe_machine_type(pe_file):
    with open(pe_file, 'rb') as f:
        s = f.read(2)
        if s != 'MZ':
            raise Exception('{0} has invalid pe header'.format(pe_file))
        else:
            f.seek(60)
            s = f.read(4)
            header_offset=struct.unpack("<L", s)[0]
            f.seek(header_offset+4)
            s = f.read(2)
            m = struct.unpack("<H", s)[0]

            if m == IMAGE_FILE_MACHINE_I386:
                opt_size = 208
            elif m == IMAGE_FILE_MACHINE_AMD64:
                opt_size = 224
            else:
                return m, False

            f.seek(header_offset+4+20+opt_size)
            s = f.read(4)
            com_addr = struct.unpack("<i", s)[0]
            return m, com_addr != 0

def get_pe_machine_string(pe_machine, assembly):
    if assembly:
        ass = ' (.NET)'
    else:
        ass = ''

    if pe_machine == IMAGE_FILE_MACHINE_I386:
        return '32-bit'+ass
    elif pe_machine == IMAGE_FILE_MACHINE_IA64:
        return "IA-64 (Itanium)"+ass
    elif pe_machine == IMAGE_FILE_MACHINE_AMD64:
        return "64-bit"+ass
    else:
        return "Unknown architecture"+ass