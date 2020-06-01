def two_fer(name=None):
    template = 'One for %(name)s, one for me.'
    if name:
        return template % {'name': name}
    else:
        return template % {'name': 'you'}
