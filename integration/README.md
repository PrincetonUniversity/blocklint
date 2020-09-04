## General

Blocklint works similar to common linters and should work out of the box
with your favorite editor.  Below are some examples, please submit a PR or
issue if you don't see your favorite or have a better implementation.

### Nano
The `~/.nanorc` can expand syntaxes to specify a linter for a given filetype.
For each filetype you would like to lint with blocklint, add
```
extendsyntax <SYNTAX> linter blocklint
```
where <SYNTAX> is the filetype, e.g. python or c.
