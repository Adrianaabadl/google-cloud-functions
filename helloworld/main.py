def hello_world(request):
    request_args = request.args
    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
    else:
        name = 'World'
        lastname = ''
    return f'Hello {name} {lastname}'


# if you have already have a process bound to the default port (8000)
# `sudo lsof -i:8080`
# `kill $PID`
