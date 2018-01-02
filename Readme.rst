RegEx Typo Fix
====

Regex spellchecker based on Wikipedia's `RegExTypoFix` project

.. _RegExTypoFix: https://en.wikipedia.org/wiki/Wikipedia:AutoWikiBrowser/Typos

The dictionary prepared by wikipedia contains most common incorrectly spelled words.

Usage
-----

The easiest way to install it is using pip::

    pip install regextypofix

    from regextypofix import correct
    print (correct('whiel sold'))
