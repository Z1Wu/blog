from ipdb import launch_ipdb_on_exception

with launch_ipdb_on_exception():
    a = {}
    a[0]