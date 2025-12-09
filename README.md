# opendaycybersecurity
Activity for open day

# Install Instructions

As the sudo account:
```
cd ~
git clone https://github.com/SheffieldML/opendaycybersecurity.git
chmod 755 ~/opendaycybersecurity/install
~/opendaycybersecurity/install
```

As the student account:
```
cd ~
git clone https://github.com/SheffieldML/opendaycybersecurity.git
cd ~/opendaycybersecurity
python3 -m venv venv --system-site-packages
source venv/bin/activate
pip install -e ~/opendaycybersecurity/
cp ~/opendaycybersecurity/materials/lowireshark.desktop Desktop
cp ~/opendaycybersecurity/materials/lowireshark.desktop ~/.local/share/applications/
```
Then on the desktop find the wireshark icon. Right click and select Allow Launching
After a reboot! Open the launcher and start typing LoWi… then right click and press ‘Pin to Dash’

The following instructions are copied from [here](https://github.com/tom-howard/com_offer_holder_days/blob/main/README.md).
```
cd ~/ros2_ws/src/
git clone https://github.com/tom-howard/com_offer_holder_days.git
cd ~/ros2_ws/ && colcon build --packages-select com_offer_holder_days
source ~/.bashrc
```

# On The Day

## Running the Waffle

The following instructions are copied from [here](https://tom-howard.github.io/ros2/waffles/launching-ros).
```
waffle X pair
```
(where X is the waffle we are using)

Type in the password

Then later, in the same terminal:
```
waffle X term
```
Then:
```
ros2 launch tuos_tb3_tools ros.launch.py
```
In a new terminal, run:
```
ros2 run rmw_zenoh_cpp rmw_zenohd
```

## Running the Web Server

Activate the virtual environment:

```
source ~/opendaycybersecurity/venv/bin/activate
```

Launch the activity:

```
activity
```

### Stopping the Web Server

To kill the web server, use:

```
pkill activity
``` 

(from a separate terminal.)