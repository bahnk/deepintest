Input/Output
============

.. module:: deepintest.io

The `io` subpackage is used to read files and output results.

Reader
------

The `reader` module is used to read files.

.. autoclass:: deepintest.io.reader.TextFileReader

  .. automethod:: deepintest.io.reader.TextFileReader.__init__

  .. automethod:: deepintest.io.reader.TextFileReader.read

Formatter
---------

The `formatter` module is used to format output.

.. autoclass:: deepintest.io.formatter.Formatter

  .. automethod:: deepintest.io.formatter.Formatter.__init__

  .. automethod:: deepintest.io.formatter.Formatter.format_line

  .. automethod:: deepintest.io.formatter.Formatter.format_lines

