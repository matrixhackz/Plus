# FORK AT YOUR OWN RISK
# Installation

### The Easy Way

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Repo Status
<a href="https://github.com/amitsharma123234/Plus/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/amitsharma123234/Plus?color=orange&style=for-the-badge"></a>

<a href="https://github.com/amitsharma123234/Plus/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/amitsharma123234/Plus?color=orange&style=for-the-badge"></a>

<a href="https://github.com/amitsharma123234/Plus/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/amitsharma123234/Plus?color=orange&style=for-the-badge"></a>

### The Normal Way

Paste this in termux to get string session:
```sh
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python git wget -y
wget https://raw.githubusercontent.com/amitsharma123234/Plus/master/telesetup.py
pip install telethon
python telesetup.py
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Check [Line 111](https://github.com/Total-Noob-69/X-tra-Telegram/blob/master/userbot/uniborgConfig.py#L111) and start adding your vars there.
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
