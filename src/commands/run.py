import click
import os
from flask.cli import CertParamType, _validate_key, SeparatedPathType, show_server_banner, DispatchingApp, ScriptInfo, FlaskGroup
from flask.helpers import get_env, get_debug_flag

from src.request_handler import RequestHandler

cli = FlaskGroup(add_default_commands=False, )

pass_script_info = click.make_pass_decorator(ScriptInfo, ensure=True)


@cli.command("run", short_help="Run a development server.")
@click.option("--host", "-h", default="127.0.0.1", help="The interface to bind to.")
@click.option("--port", "-p", default=5000, help="The port to bind to.")
@click.option(
    "--cert",
    type=CertParamType(),
    help="Specify a certificate file to use HTTPS.",
    is_eager=True,
)
@click.option(
    "--key",
    type=click.Path(exists=True, dir_okay=False, resolve_path=True),
    callback=_validate_key,
    expose_value=False,
    help="The key file to use when specifying a certificate.",
)
@click.option(
    "--reload/--no-reload",
    default=None,
    help="Enable or disable the reloader. By default the reloader "
    "is active if debug is enabled.",
)
@click.option(
    "--debugger/--no-debugger",
    default=None,
    help="Enable or disable the debugger. By default the debugger "
    "is active if debug is enabled.",
)
@click.option(
    "--eager-loading/--lazy-loading",
    default=None,
    help="Enable or disable eager loading. By default eager "
    "loading is enabled if the reloader is disabled.",
)
@click.option(
    "--with-threads/--without-threads",
    default=True,
    help="Enable or disable multithreading.",
)
@click.option(
    "--extra-files",
    default=None,
    type=SeparatedPathType(),
    help=(
        "Extra files that trigger a reload on change. Multiple paths"
        f" are separated by {os.path.pathsep!r}."
    ),
)
@click.option(
    "--exclude-patterns",
    default=None,
    type=SeparatedPathType(),
    help=(
        "Files matching these fnmatch patterns will not trigger a reload"
        " on change. Multiple patterns are separated by"
        f" {os.path.pathsep!r}."
    ),
)
@pass_script_info
def run_command(
    info,
    host,
    port,
    reload,
    debugger,
    eager_loading,
    with_threads,
    cert,
    extra_files,
    exclude_patterns,
):
    """Run a local development server.
    This server is for development purposes only. It does not provide
    the stability, security, or performance of production WSGI servers.
    The reloader and debugger are enabled by default if
    FLASK_ENV=development or FLASK_DEBUG=1.
    """
    print("OAISJDOIASJDOIASJDIOAJS")
    debug = get_debug_flag()

    if reload is None:
        reload = debug

    if debugger is None:
        debugger = debug

    show_server_banner(get_env(), debug, info.app_import_path, eager_loading)
    app = DispatchingApp(info.load_app, use_eager_loading=eager_loading)

    from werkzeug.serving import run_simple

    run_simple(
        host,
        port,
        app,
        use_reloader=reload,
        use_debugger=debugger,
        threaded=with_threads,
        ssl_context=cert,
        extra_files=extra_files,
        exclude_patterns=exclude_patterns,
        request_handler=RequestHandler,
    )