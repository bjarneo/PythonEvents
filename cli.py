import events


e = events.Events()

e.register('Fire', {
    'name': 'Bjarne Oeverli',
    'nick': 'bjarneo',
    'e-mail': 'bjarne.oeverli@gmail.com',
    'options': {
        'uno': 'my first',
        'dos': 'my second'
    }
})

# Callback
def test(item):
    print item

# Listen to event and add callback
e.listen('Fire', test)

# Listen to all events
e.listenAll(test)

# Listen to event once, and it gets deleted
e.listenOnce('Fire', test)

# Remove event
e.remove('Fire')