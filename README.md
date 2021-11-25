# API-Automation Framework

![languange compliant](https://img.shields.io/badge/language-Python-{green}.svg)

This framework realizes api automation with Python+Requests+Pytest+YAML+Allure.

- **Python + Requests** to send and process api
- **Pytest** as the test executor
- **YAML** to manage test case
- **Allure** To generate a test report.

## Table of Contents

- [API-Automation Framework](#api-automation-framework)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Install](#install)
    - [Install python 3.10.0](#install-python-3100)
    - [Install allure](#install-allure)
    - [Install requirement](#install-requirement)
  - [Usage](#usage)
  - [Test case rule](#test-case-rule)
  - [Example Readmes](#example-readmes)
  - [Related Efforts](#related-efforts)
  - [Maintainers](#maintainers)
  - [Contributing](#contributing)
    - [Contributors](#contributors)
  - [License](#license)

## Background

>This framework started with the issue originally posed by [@Yanyuedavid](https://github.com/Yanyuedavid) about whether or not a framework to api automation would be useful. While working on maintaining other projects, we needed a way to standardize api test. This specification started as a result of that.

## Install

### Install python 3.10.0

This project uses [python](https://www.python.org/) Go check them out if you don't have them locally installed.

### Install allure

 download [allure](https://github.com/allure-framework/allure2/releases) allure-2.15.0.zip

 ```
 copy allure-2.15.0/bin to ENV:path
 ```

### Install requirement

```
 pip install -r ./venv/requirement.txt
```

## Usage

pytest

```
terminal pytest -vs
```

main

```
python main.py
```

## Test case rule

This framework is test case driven, interface encapsulation, and test result assertion, so there are rules for test cases, see for details.
[RULE](https://github.com/xinglun/TestFramwork/blob/master/RULE.md)

## Example Readmes

To see how the specification has been applied, see the [examples](https://github.com/xinglun/TestFramwork/tree/master/testcases).

## Related Efforts

- [pytestDemo](https://github.com/wintests/pytestDemo) 


## Maintainers

 [@Yanyuedavid](https://github.com/Yanyuedavid).

## Contributing

Feel free to dive in! [Open an issue](https://github.com/xinglun/TestFramwork) or submit PRs.

### Contributors

This project exists thanks to all the people who contribute.


## License

MIT
