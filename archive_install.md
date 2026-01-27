# [ARCHIVE] Installation Instructions for Diamond Laptops

Note: I recommended visiting this page from the laptop, so you can copy and paste these commands!

## As the sudo user

```
cd ~
git clone https://github.com/SheffieldML/opendaycybersecurity.git
chmod 755 ~/opendaycybersecurity/install
~/opendaycybersecurity/install
```
(choose 'yes' when it asks if non-superusers should be able to capture packets).

## As the `offer_holders` user

```
cd ~
git clone https://github.com/SheffieldML/opendaycybersecurity.git
cd ~/opendaycybersecurity
python3 -m venv venv --system-site-packages
source venv/bin/activate
pip install -e ~/opendaycybersecurity/
cp ~/opendaycybersecurity/materials/LoWireshark.desktop ~/.local/share/applications/
```
Open the launcher and start typing LoWi… then right click and press ‘Pin to Dash’

Open the launcher and start typing Text Editor then right click and press 'Pin to Dash'.

### Firefox Bookmarks

Right click on toolbar, and set bookmark toolbar always visible. Then you can drag these links onto the toolbar.
Add links to the bookmarks toolbar:
- [Challenge 1](http://127.0.0.1:5000/rotate.html)
- [Challenge 2](http://127.0.0.1:5000/move.html)
- [Challenge 3](http://127.0.0.1:5000/email.html)
- [Social Media](https://drive.usercontent.google.com/download?id=1v7-TGm-g1czj2YieQFv8SVL3YLpqlG55)
- [Full Control](http://127.0.0.1:5000/full.html)

## Installing the `com_offer_holder_days` ROS 2 Package

**No longer necessary**: this is installed globally on the laptop (rather than locally to the User's workspace).

The following instructions are copied from [here](https://github.com/tom-howard/com_offer_holder_days/blob/main/README.md).
```
cd ~/ros2_ws/src/
git clone https://github.com/tom-howard/com_offer_holder_days.git
cd ~/ros2_ws/ && colcon build --packages-select com_offer_holder_days
source ~/.bashrc
```
