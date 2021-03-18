function! blocklint#Hook(buffer) abort
    " Change job type to prevent early stopping
    call setbufvar(a:buffer, 'ale_job_type', 'other')
    " Tell ALE we're going to check this buffer.
    call ale#other_source#StartChecking(a:buffer, 'blocklint')
    " Start async job to perform blocklint, will call WorkDone
    call ale#command#Run(a:buffer,
                \ g:blocklint_command . ' -e --stdin ' . g:blocklint_options,
                \ function('blocklint#WorkDone'), {'read_buffer': 1})
endfunction

function! blocklint#WorkDone(buffer, results, metadata) abort
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
