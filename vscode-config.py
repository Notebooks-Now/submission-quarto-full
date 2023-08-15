# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'openrefine': {
        'command': ['code-server', '--auth', 'none', '--disable-telemetry', '--port={port}'],
        'port': 3333,
        'timeout': 120,
        'launcher_entry': {
            'enabled': True,
            'icon_path': '/home/jovyan/vscode.svg',
            'title': 'VS Code',
        },
    },
}
