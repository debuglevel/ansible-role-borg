# ansible-role-borg

Installs `borg` and `borgmatic` and configures a scheduled `borgmatic`.

There are options to use a `pipx` or `docker` deployment.

## Requirements

<!-- Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required. -->

## Role Variables

<!-- A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well. -->

## Dependencies

<!-- A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles. -->

## Example Playbook

<!-- Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 } -->

```yaml
- name: Ensure borgmatic backups
  hosts: root_server
  become: true
  roles:
    - debuglevel.borg
  # tags:
  #   - base
  #   - base:users
```

## Usage

Add this in your `requirements.yaml`:

```
roles:
  - name: debuglevel.template
    src: https://github.com/debuglevel/ansible-role-template
    version: <commit hash>

  - name: debuglevel.template
    src: git@gitlab.mycorp.internal:ansible/roles/ansible-role-template.git
    scm: git
    version: <commit hash>
```

## Linting and Testing

Install Ansible with `pip3 install --requirement requirements.txt`.

Lint YAML files with `yamllint`:
1. Install via `pip3 install yamllint`.
2. Lint using `yamllint .`.
3. It is configured in `.yamllint`, in case you want to modify it.

Lint Ansible with `ansible-lint`:
1. Install via `pip3 install ansible-lint`.
2. Run `ansible-lint` to check for common issues or bad practices.
3. Reformat it with `ansible-lint --write`.

Test the role with `molecule`:
1. (Maybe install collections first using `ansible-galaxy install --role-file requirements.yaml`; maybe use `--force`)
2. `molecule test --all`
