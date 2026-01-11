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
uv run konsoltheme --dark_profile "Dark" --light_profile "Light"
```


## Systemd Auto-start

You can use the provided systemd unit file to automatically start the background process when you log in.

1. Create the systemd user directory if it doesn't exist:
   ```bash
   mkdir -p ~/.config/systemd/user/
   ```

2. Copy or link the service file:
   ```bash
   # Adjust path to where you cloned the repo
   ln -s $(pwd)/systemd/user/konsole-daynight.service ~/.config/systemd/user/
   ```

3. Reload systemd and enable the service:
   ```bash
   systemctl --user daemon-reload
   systemctl --user enable --now konsole-daynight.service
   ```

4. Check the status:
   ```bash
   systemctl --user status konsole-daynight.service
   ```

> [!NOTE]
> The service file assumes you are using `uv` and the project is located at `~/Documents/src/konsole_daynight`. If your setup is different, you may need to edit the `ExecStart` line in the service file.
