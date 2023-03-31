def get_server_name(url):
    first_symbols_set = '://'
    second_symbol_set = "/"

    start_index = url.find(first_symbols_set) + 3
    end_index = url.find(second_symbol_set, start_index)

    if end_index == -1:
        return url[start_index:]

    return url[start_index:end_index]


user_url = 'https://SomeServerName/abcd/dfdf.htm?dfdf=dfdf'
# user_url = 'https://SomeServerName'

print(get_server_name(user_url))
