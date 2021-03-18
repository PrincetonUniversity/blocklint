if !exists('g:blocklint_command')
    " get blocklint main file relative to this file
    let s:path = expand('<sfile>:p:h:h:h:h') . '/blocklint/main.py'

    let g:blocklint_command = system('which blocklint')
    if len(g:blocklint_command) == 0
        let g:blocklint_command = 'python ' . s:path
    else  " strip trailing whitespace
        let g:blocklint_command = substitute(g:blocklint_command, '\%x00$', '', '')
    endif
endif

if !exists('g:blocklint_options')
    let g:blocklint_options = ''
endif

augroup BlocklintALE
    autocmd!
    autocmd User ALEWantResults call blocklint#Hook(g:ale_want_results_buffer)
augroup END
