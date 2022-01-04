def parse_argv(argv):
    flags_dict = {}
    argument_list = []
    for i in range(len(argv)):
        if argv[i][0] == '-':
            try:
                if argv[i + 1][0] != '-':
                    flags_dict.update({argv[i]: argv[i + 1]})
                else:
                    flags_dict.update({argv[i]: ''})
            except IndexError:
                flags_dict.update({argv[i]: ''})
        elif argv[i - 1][0] != '-':
            argument_list.append(argv[i])
    return flags_dict, argument_list
