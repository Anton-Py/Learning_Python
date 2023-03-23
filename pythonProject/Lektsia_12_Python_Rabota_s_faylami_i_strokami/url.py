def get_server_name(string, server_name):
    index_start = string.find(server_name)
    index_end = index_start + len(server_name)
    url = string[index_start:index_end]

    return url


user_string = 'https://SomeServerName/abcd/dfdf.htm?dfdf=dfdf'
user_server_name = 'SomeServerName'

print(get_server_name(user_string, user_server_name))
