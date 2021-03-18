## Integration with ALE
Blocklist can be used with [ALE](https://github.com/dense-analysis/ale) for
higlighting errors on all filetypes.  To install, add the following
plugin, for [vim-plug](https://github.com/junegunn/vim-plug):
```
Plug 'PrincetonUniversity/blocklint', {'rtp': 'integration/vim/'}
```

Assign `g:blocklint_command` to change how blocklint is invoked.
Default is `which blocklint` or (failing that) `python blocklint/main.py`.

Assign `g:blocklint_options` to modify options.
Will always append `-e --stdin`.
Configuration files will also be utilized if available.
