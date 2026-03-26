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
tb3_bringup
```

Close down this window (click "Close Terminal" if asked).

In a new terminal, run:
```
tmux
```
then inside that tmux screen,
```
rmwz
```
Finally: Type `Ctrl-B` + `D` (this detaches the tmux windows, so the students can't see it).

## Running the Web Server
First start another tmux window: 

```
tmux
```

Then, activate the virtual environment:

```
source ~/opendaycybersecurity/venv/bin/activate
```

Launch the activity:

```
activity
```

Finally, detach the tmux window: `Ctrl-B` + `D`. This hides the server from the students.

### Stopping the Web Server

To kill the web server, use:

```
pkill activity
``` 

(from a separate terminal.)

### Using tmux (a very quick guide!):

#### List Sessions

To list all tmux sessions:
```
tmux ls
```
If you followed the steps above, there should be two listed:
```
tmux ls
0: 1 windows (created Day Month Year HH:MM:SS YYYY)
1: 1 windows (created Day Month Year HH:MM:SS YYYY)
```
Session id's are the left most numbers in the above (i.e. `0` and `1`).

#### Attach (return) to an existing session

To attach to a session (e.g. `0` or `1` from above)

```
tmux a -t SESSION_ID
```
e.g. to return to session `0`:
```
tmux a -t 0
```
Or to return to session `1`:
```
tmux a -t 1
```

#### Detach (exit from) a session 

Leave (i.e. "detach from") a tmux session: `Ctrl-B` + `d`.
