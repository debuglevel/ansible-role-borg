"""Role testing files using testinfra."""

def test_directories(host):
    """Validate service directories exists."""
    directories = [
        "/etc/borgmatic",
        "/tmp/sshkey",
        "/tmp/instance",  # initialized borg repository
    ]

    for directory in directories:
        d = host.file(directory)

        assert d.exists
        assert d.is_directory

def test_files(host):
    """Validate files existing"""

    files_names = [
        "/etc/borgmatic/config.yaml",

        "/tmp/sshkey/id_ed25519",
        "/tmp/sshkey/id_ed25519.pub",

        #"/root/.local/bin/borgmatic",  # pip installation

        "/etc/systemd/system/borgmatic.service",
        "/etc/systemd/system/borgmatic.timer",
    ]

    for file_name in files_names:
        file = host.file(file_name)

        assert file.exists
        assert file.is_file

# TODO: Does not seem to work on molecule.
# def test_service(host):
#     """Validate service is valid."""
#     service = host.service("borgmatic")
#
#     assert service.is_valid

def test_commands(host):
    """Validate commands exists."""
    commands = [
        "borg",
        "borgmatic",
    ]

    for command in commands:
        print(f"Searching for command {command}...")
        c = host.find_command(command)

# def test_executables(host):
#     """Validate service executables exists."""
#     executables = [
#         "/tmp/test.sh",
#     ]
#
#     for executable in executables:
#         e = host.file(executable)
#
#         assert e.exists
#         assert e.is_file
#         assert e.is_executable
