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
    print (correct('whiel selled'))

Add more patterns
-----
You can either create your own dictionary or just append to the default dictionary::

    from regextypofix import correct, create_dictionary

    # Build default dictionary
    default_dictionary = create_dictionary()

    # User defined dictionary
    user_dictionary = create_dictionary('./path_to_text_files')

    # Complete dictionary
    dictionary = default_dictionary + user_dictionary

    # Now pass dictionary to `correct`

    correct('whiel selled', dictionary=dictionary)

