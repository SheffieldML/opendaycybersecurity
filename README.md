# opendaycybersecurity
Activiy for open day

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
cd ~/ros2_ws/src/
git clone https://github.com/tom-howard/com_offer_holder_days.git
cd ~/ros2_ws/ && colcon build --packages-select com_offer_holder_days
source ~/.bashrc

```

Then on the desktop find the wireshark icon. Right click and select Allow Launching
Then open the launcher and start typing LoWi… then right click and press ‘Pin to Dash’

There are three components that need to run:

1) 
