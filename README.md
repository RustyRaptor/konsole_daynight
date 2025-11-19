# Konsole Day/Night
A daemon to auto set your konsole profile when you change from dark and light mode in KDE

## Setup
- Use uv to install dependencies and run.
```bash
uv venv
uv sync
```

## Config
- By default looks for profiles named `Light` and `Dark`
- Can configure with `--dark_profile` and `--light_profile`

## Usage

```bash
uv run
uv run konsoltheme --dark_profile "Dark" --light_profile "Light"
```
