# About
Globally repalces all imports, and paths. Specially useful when working with boilerplates.

Ex:

    python3 replace.py @@ test

Changes:

    from @@.foo import bar

To:

    from test.foo import bar


# Usage
    python3 replacer.py *target* *replacement*

