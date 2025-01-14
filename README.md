# Kasa Smartbulb Fun

Fun with Kasa smart bulbs!

TP-link's Kasa and Tapo apps don't support cycling through colors so let's do it ourselves.

## Install

Runs on python 3.9 or above. Maybe it runs on older versions of python 3 as well.

```sh
pip install -r requirements.txt
```

## Run

Before running the script, make sure you've lists your bulbs' IP addresses in your `.env`. Refer to `.env.example`.

```sh
python main.py
```

## Docker

If you don't want to keep a terminal opened just to run this script, you can let it run in a Docker container and forget about it.

```sh
docker-compose up -d
```
