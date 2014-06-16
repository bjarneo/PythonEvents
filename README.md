PythonEvents
============

Fire events with dictionary attached, and listen to events. Small library.

### Example (see cli.py)
```python
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
# Output:
# {'nick': 'bjarneo', 'options': {'dos': 'my second', 'uno': 'my first'}, 'name': 'Bjarne Oeverli', 'e-mail': 'bjarne.oeverli@gmail.com'}


# Listen to all events
e.listenAll(test)
# Output:
# {'Fire': {'nick': 'bjarneo', 'options': {'dos': 'my second', 'uno': 'my first'}, 'name': 'Bjarne Oeverli', 'e-mail': 'bjarne.oeverli@gmail.com'}}


# Listen to event once, and it gets deleted
e.listenOnce('Fire', test)
# Output:
# {'nick': 'bjarneo', 'options': {'dos': 'my second', 'uno': 'my first'}, 'name': 'Bjarne Oeverli', 'e-mail': 'bjarne.oeverli@gmail.com'}

# Remove event
e.remove('Fire')
```