# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'openrefine': {
        'command': ['code-server', '--auth', 'none', '--disable-telemetry', '--port={port}'],
        'timeout': 300,
        'launcher_entry': {
            'enabled': True,
            'icon_path': '/home/jovyan/.jupyter/vscode.svg',
            'title': 'VS Code',
        },
    },
}
