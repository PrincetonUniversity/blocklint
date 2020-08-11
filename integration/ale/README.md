## Integration with ALE
Blocklist can be used with [ALE](https://github.com/dense-analysis/ale) for
vim by adding the following to your vimrc:
```vim
" Inclusive syntax {{{1
augroup BlocklintALE
  autocmd!
  autocmd User ALEWantResults call BlocklintHook(g:ale_want_results_buffer)
augroup END

function! BlocklintHook(buffer) abort
  " Tell ALE we're going to check this buffer.
  call ale#other_source#StartChecking(a:buffer, 'blocklint')
  call ale#command#Run(a:buffer, 'blocklint -e --stdin',
              \ function('BlocklintWorkDone'), {'read_buffer': 1})
endfunction

function! BlocklintWorkDone(buffer, results, metadata) abort
  " Send results to ALE after they have been collected.
  let l:pattern = '\v^[^:]+:(\d+):(\d+):(\d+): (.+)$'
  let l:output = []
  for l:match in ale#util#GetMatches(a:results, l:pattern)
    call add(l:output, {
              \ 'lnum': l:match[1],
              \ 'col': l:match[2],
              \ 'end_col': l:match[3],
              \ 'text': l:match[4],
              \ 'type': 'E'})
  endfor
  call ale#other_source#ShowResults(a:buffer, 'blocklint', l:output)
endfunction
```
