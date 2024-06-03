<!--
SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
SPDX-License-Identifier: MPL-2.0
-->

# OS2mo-rollekatalog

OS2mo integration for [OS2Rollekatalog](https://www.os2.eu/os2rollekatalog).

Rollekatalog API documentation: https://htk.rollekatalog.dk/download/api.html.


## Usage

```
docker-compose up -d
```

Configuration is done through environment variables. Available options can be
seen in [os2mo_rollekatalog/config.py]. Complex variables such as dict or lists
can be given as JSON strings, as specified by Pydantic's settings parser.


## Versioning
This project uses [Semantic Versioning](https://semver.org/) with the following
strategy:
- MAJOR: Incompatible API changes.
- MINOR: Backwards-compatible updates and functionality.
- PATCH: Backwards-compatible bug fixes.


## Authors
Magenta ApS <https://magenta.dk>


## License

- This project: [MPL-2.0](LICENSES/MPL-2.0.txt)

This project uses [REUSE](https://reuse.software) for licensing. All licenses can be found in the [LICENSES folder](LICENSES/) of the project.
