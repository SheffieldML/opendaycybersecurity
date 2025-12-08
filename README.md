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
python3 -m venv venv/
source venv/bin/activate
cd ~
git clone https://github.com/SheffieldML/opendaycybersecurity.git
pip install -e opendaycybersecurity/
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
The following instructions are copied from [here](https://tom-howard.github.io/com2009/waffles/launching-ros).
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
tb3_bringup
```
In a new terminal, run:
```
waffle X bridge
```
