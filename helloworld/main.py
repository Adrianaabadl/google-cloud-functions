def hello_world(request):
    request_args = request.args
    if request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return f'Hello {name}'


# if you have already have a process bound to the default port (8000)
# `sudo lsof -i:8080`
# `kill $PID`
