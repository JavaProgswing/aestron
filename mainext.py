import builtins
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
async def publicaexec(code, ctx,client):
    # Make an async function with the code and `exec` it
    env = vars(builtins)
    env['print'] = print
    env['dir'] = dir
    env['locals']=locals
    env['ctx']=ctx
    env['client']=client
    code=f'async def __ex(ctx,client): ' +''.join(f'\n {l}' for l in code.split('\n'))+f"\n return client.loop.create_task(__ex(ctx,client))"
    f = StringIO()
    e = StringIO()
    directout = None
    with redirect_stderr(e):
        with redirect_stdout(f):
            directout = exec(code,env)
    if directout is None:
        directout = ""
    output = f.getvalue()+f" {directout}"
    erroutput = e.getvalue()
    jsonout={
        "output":output,
        "erroutput":erroutput,
    }
    return jsonout

    # Get `__ex` from local variables, call it and return the result
    