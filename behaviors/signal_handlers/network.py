def process_host_query_request(component, signal, args):
    hosts = "TODO"
    args['host'].send('host_query_response', {'hosts': hosts})
