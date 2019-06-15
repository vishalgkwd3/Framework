from configparser import ConfigParser


class IOBase():

    def get_section_data_from_ini_file(self, file_name, section_name):
        cp = ConfigParser()
        cp.read('./test_data/'+file_name)

        list_data = cp.items(section_name)
        kv = {}
        for tt in list_data:
            key = tt[0]
            value = tt[1]
            kv[key] = value

        return kv