# Changelog

All notable changes to this project will be documented in this file.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Modified

- Translated the issue templates into English.

## [0.1.0] - 2020-07-20

### Added

- Add Issues and Pull-Request templates.
- Configure repository to perform CI/CD by adding a `nox` configuration file
  and two workflows for GitHub Actions.
- New `pytest`, `pytest-cov` and `isort` config files.
- Change from `pyTelegramBotAPI` to `python-telegram-bot` due to easy built-in
  webhook integration and great documentation.
- Add tests for the `etsiit_bot` module.
- Modify `glitch.json` to match new bot settings.

### Modified

- Moved bot code to it's own module.

## [0.0.1] - 2020-04-27

### Added

- Base code.
- Changelog to keep a changes log.
- Populated README.md with a brief description of the project.
- Added LICENSE.txt file.
- Some initial WIKI pages.
- Added Python gitignore.
- Added new badge to informm about new releases.

[Unreleased]: https://github.com/jorgechp/etsiit_bot/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/jorgechp/etsiit_bot/releases/tag/v0.1.0
[0.0.1]: https://github.com/jorgechp/etsiit_bot/releases/tag/v0.0.1
