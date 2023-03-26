def get_server_name(url_address):
    server_name = 'SomeServerName'

    start_index = url_address.find(server_name)
    end_index = start_index + len(server_name)

    return url_address[start_index:end_index]


user_url_address = 'https://SomeServerName/abcd/dfdf.htm?dfdf=dfdf'

print(get_server_name(user_url_address))
