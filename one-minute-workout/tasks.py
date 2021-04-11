from invoke import task

@task

def test(ctx):
    ctx.run("poetry run pytest src")


