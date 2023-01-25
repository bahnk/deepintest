Search
======

.. module:: deepintest.search

The `search` subpackage is used to clean strings and search for a specific term.

Characters
----------

The `characters` module is used to manipule characters for a given encoding.

.. autoclass:: deepintest.search.characters.CharacterRange

  .. automethod:: deepintest.search.characters.CharacterRange.__init__

  .. automethod:: deepintest.search.characters.CharacterRange.get_characters

.. autoclass:: deepintest.search.characters.CharacterSet

  .. automethod:: deepintest.search.characters.CharacterSet.__init__

  .. automethod:: deepintest.search.characters.CharacterSet.get_characters

  .. automethod:: deepintest.search.characters.CharacterSet.add_character

Cleaner
-------

The `cleaner` module is used to remove unwanted characters from a string.

.. autoclass:: deepintest.search.cleaner.Cleaner

  .. automethod:: deepintest.search.cleaner.Cleaner.__init__

  .. automethod:: deepintest.search.cleaner.Cleaner.clean_line

Matcher
-------

The `matcher` module is used to search for a term in a string.

.. autoclass:: deepintest.search.matcher.Matcher

  .. automethod:: deepintest.search.matcher.Matcher.__init__

  .. automethod:: deepintest.search.matcher.Matcher.match

