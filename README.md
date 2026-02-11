# opendaycybersecurity
Activity for open day

# Install Instructions

As of Jan 2026, all necessary tools / packages are pre-installed on the Diamond Laptops, so there are NO installation steps to carry out. Nonetheless, [the installation steps are documented here for future reference](./archive_install.md).

# On The Day

Log in to the `offer_holders` user account on the Diamond Laptop.

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
tmux
```
then inside that tmux screen,
```
ros2 run rmw_zenoh_cpp rmw_zenohd
```
Finally: Type Ctrl-B D (this detaches the tmux windows, so the students can't see it).

## Running the Web Server
First start another tmux window, type: `tmux`.
Then:

Activate the virtual environment:

```
source ~/opendaycybersecurity/venv/bin/activate
```

Launch the activity:

```
activity
```

Finally detach the tmux window: `Ctrl-B D`. This hides the server from the students.

### Stopping the Web Server

To kill the web server, use:

```
pkill activity
``` 

(from a separate terminal.)

### Using tmux:

```
tmux ls
tmux a -t 0
Ctrl-B d
```
