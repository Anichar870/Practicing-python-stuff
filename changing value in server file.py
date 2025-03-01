def update_server_config(file_path, key, value):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    with open(file_path, 'w') as f:
        for line in lines:
            if line.strip().startswith(key + "="):
                f.write(key + "=" + value + "\n")
            else:
                f.write(line)

server_config_file = 'server.conf'
key_to_update = 'MAX_CONNECTIONS'
new_value = '900'

update_server_config(server_config_file, key_to_update, new_value)