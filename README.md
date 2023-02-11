oclif-hello-world
=================

oclif example Hello World CLI

[![oclif](https://img.shields.io/badge/cli-oclif-brightgreen.svg)](https://oclif.io)
[![Version](https://img.shields.io/npm/v/oclif-hello-world.svg)](https://npmjs.org/package/oclif-hello-world)
[![CircleCI](https://circleci.com/gh/oclif/hello-world/tree/main.svg?style=shield)](https://circleci.com/gh/oclif/hello-world/tree/main)
[![Downloads/week](https://img.shields.io/npm/dw/oclif-hello-world.svg)](https://npmjs.org/package/oclif-hello-world)
[![License](https://img.shields.io/npm/l/oclif-hello-world.svg)](https://github.com/oclif/hello-world/blob/main/package.json)

<!-- toc -->
* [Usage](#usage)
* [Commands](#commands)
<!-- tocstop -->
# Usage
<!-- usage -->
```sh-session
$ npm install -g symbol-soup
$ symbol-soup COMMAND
running command...
$ symbol-soup (--version)
symbol-soup/0.0.0 linux-x64 node-v16.18.0
$ symbol-soup --help [COMMAND]
USAGE
  $ symbol-soup COMMAND
...
```
<!-- usagestop -->
# Commands
<!-- commands -->
* [`symbol-soup hello PERSON`](#symbol-soup-hello-person)
* [`symbol-soup hello world`](#symbol-soup-hello-world)
* [`symbol-soup help [COMMANDS]`](#symbol-soup-help-commands)
* [`symbol-soup plugins`](#symbol-soup-plugins)
* [`symbol-soup plugins:install PLUGIN...`](#symbol-soup-pluginsinstall-plugin)
* [`symbol-soup plugins:inspect PLUGIN...`](#symbol-soup-pluginsinspect-plugin)
* [`symbol-soup plugins:install PLUGIN...`](#symbol-soup-pluginsinstall-plugin-1)
* [`symbol-soup plugins:link PLUGIN`](#symbol-soup-pluginslink-plugin)
* [`symbol-soup plugins:uninstall PLUGIN...`](#symbol-soup-pluginsuninstall-plugin)
* [`symbol-soup plugins:uninstall PLUGIN...`](#symbol-soup-pluginsuninstall-plugin-1)
* [`symbol-soup plugins:uninstall PLUGIN...`](#symbol-soup-pluginsuninstall-plugin-2)
* [`symbol-soup plugins update`](#symbol-soup-plugins-update)

## `symbol-soup hello PERSON`

Say hello

```
USAGE
  $ symbol-soup hello [PERSON] -f <value>

ARGUMENTS
  PERSON  Person to say hello to

FLAGS
  -f, --from=<value>  (required) Who is saying hello

DESCRIPTION
  Say hello

EXAMPLES
  $ oex hello friend --from oclif
  hello friend from oclif! (./src/commands/hello/index.ts)
```

_See code: [dist/commands/hello/index.ts](https://github.com/dcoon/symbol-soup/blob/v0.0.0/dist/commands/hello/index.ts)_

## `symbol-soup hello world`

Say hello world

```
USAGE
  $ symbol-soup hello world

DESCRIPTION
  Say hello world

EXAMPLES
  $ symbol-soup hello world
  hello world! (./src/commands/hello/world.ts)
```

## `symbol-soup help [COMMANDS]`

Display help for symbol-soup.

```
USAGE
  $ symbol-soup help [COMMANDS] [-n]

ARGUMENTS
  COMMANDS  Command to show help for.

FLAGS
  -n, --nested-commands  Include all nested commands in the output.

DESCRIPTION
  Display help for symbol-soup.
```

_See code: [@oclif/plugin-help](https://github.com/oclif/plugin-help/blob/v5.2.4/src/commands/help.ts)_

## `symbol-soup plugins`

List installed plugins.

```
USAGE
  $ symbol-soup plugins [--core]

FLAGS
  --core  Show core plugins.

DESCRIPTION
  List installed plugins.

EXAMPLES
  $ symbol-soup plugins
```

_See code: [@oclif/plugin-plugins](https://github.com/oclif/plugin-plugins/blob/v2.3.0/src/commands/plugins/index.ts)_

## `symbol-soup plugins:install PLUGIN...`

Installs a plugin into the CLI.

```
USAGE
  $ symbol-soup plugins:install PLUGIN...

ARGUMENTS
  PLUGIN  Plugin to install.

FLAGS
  -f, --force    Run yarn install with force flag.
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Installs a plugin into the CLI.
  Can be installed from npm or a git url.

  Installation of a user-installed plugin will override a core plugin.

  e.g. If you have a core plugin that has a 'hello' command, installing a user-installed plugin with a 'hello' command
  will override the core plugin implementation. This is useful if a user needs to update core plugin functionality in
  the CLI without the need to patch and update the whole CLI.


ALIASES
  $ symbol-soup plugins add

EXAMPLES
  $ symbol-soup plugins:install myplugin 

  $ symbol-soup plugins:install https://github.com/someuser/someplugin

  $ symbol-soup plugins:install someuser/someplugin
```

## `symbol-soup plugins:inspect PLUGIN...`

Displays installation properties of a plugin.

```
USAGE
  $ symbol-soup plugins:inspect PLUGIN...

ARGUMENTS
  PLUGIN  [default: .] Plugin to inspect.

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Displays installation properties of a plugin.

EXAMPLES
  $ symbol-soup plugins:inspect myplugin
```

## `symbol-soup plugins:install PLUGIN...`

Installs a plugin into the CLI.

```
USAGE
  $ symbol-soup plugins:install PLUGIN...

ARGUMENTS
  PLUGIN  Plugin to install.

FLAGS
  -f, --force    Run yarn install with force flag.
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Installs a plugin into the CLI.
  Can be installed from npm or a git url.

  Installation of a user-installed plugin will override a core plugin.

  e.g. If you have a core plugin that has a 'hello' command, installing a user-installed plugin with a 'hello' command
  will override the core plugin implementation. This is useful if a user needs to update core plugin functionality in
  the CLI without the need to patch and update the whole CLI.


ALIASES
  $ symbol-soup plugins add

EXAMPLES
  $ symbol-soup plugins:install myplugin 

  $ symbol-soup plugins:install https://github.com/someuser/someplugin

  $ symbol-soup plugins:install someuser/someplugin
```

## `symbol-soup plugins:link PLUGIN`

Links a plugin into the CLI for development.

```
USAGE
  $ symbol-soup plugins:link PLUGIN

ARGUMENTS
  PATH  [default: .] path to plugin

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Links a plugin into the CLI for development.
  Installation of a linked plugin will override a user-installed or core plugin.

  e.g. If you have a user-installed or core plugin that has a 'hello' command, installing a linked plugin with a 'hello'
  command will override the user-installed or core plugin implementation. This is useful for development work.


EXAMPLES
  $ symbol-soup plugins:link myplugin
```

## `symbol-soup plugins:uninstall PLUGIN...`

Removes a plugin from the CLI.

```
USAGE
  $ symbol-soup plugins:uninstall PLUGIN...

ARGUMENTS
  PLUGIN  plugin to uninstall

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Removes a plugin from the CLI.

ALIASES
  $ symbol-soup plugins unlink
  $ symbol-soup plugins remove
```

## `symbol-soup plugins:uninstall PLUGIN...`

Removes a plugin from the CLI.

```
USAGE
  $ symbol-soup plugins:uninstall PLUGIN...

ARGUMENTS
  PLUGIN  plugin to uninstall

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Removes a plugin from the CLI.

ALIASES
  $ symbol-soup plugins unlink
  $ symbol-soup plugins remove
```

## `symbol-soup plugins:uninstall PLUGIN...`

Removes a plugin from the CLI.

```
USAGE
  $ symbol-soup plugins:uninstall PLUGIN...

ARGUMENTS
  PLUGIN  plugin to uninstall

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Removes a plugin from the CLI.

ALIASES
  $ symbol-soup plugins unlink
  $ symbol-soup plugins remove
```

## `symbol-soup plugins update`

Update installed plugins.

```
USAGE
  $ symbol-soup plugins update [-h] [-v]

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Update installed plugins.
```
<!-- commandsstop -->
