# rasptemp-monitor
Monitors Raspberry Pi temperature and shutdowns automatically if it reaches the limit

## Pushover notifications
Add your user and API keys for pushover notification before shutting down

## Autorun
To run on startup execute the following steps

  1. Add command to a file to be run on startup

```
cat "python3 /path/to/rastemp.py &" >> /home/pi/startup.sh
sudo chmod +x ~/startup.sh
```

  2. Add this line to ```/etc/rc.local```  before the ```exit 0``` line

```/home/pi/startup.sh || exit 1```
