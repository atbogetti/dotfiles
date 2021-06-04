# Qtile configuration file

# Import statements
import os
import subprocess
from typing import List
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen

# Set variables
mod = "mod4"
terminal = guess_terminal()

# Define keybindings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn("dmenu_run -nf '#fcfcfc' -sf '#fcfcfc' -nb '#232627' -sb '#1793d0' -fn 'DejaVu Sans-11'"), desc="Launch dmenu"),
    Key([mod], "w", lazy.spawn("brave"), desc="Launch Brave"),
    Key([mod, "shift"], "v", lazy.spawn("sudo vpnc lab"), desc="Launch VPN"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Media keys
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Toggle mute"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5"), desc="Increase volume by 5%"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5"), desc="Decrease volume by 5%"),
    
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play or pause music"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Go to next song"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Go to previous song"),

]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layout_theme = {"border_width": 3,
                "margin": 8,
                "border_focus": "1793d0",
                "border_normal": "232627"
               }

layouts = [
    layout.MonadTall(**layout_theme),
    #layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme)
    #layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    #layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [["#232627", "#232627"], # General background
          ["#fcfcfc", "#fcfcfc"], # General foreground
          ["#676e7d", "#676e7d"], # Alternate foreground
          ["#1793d0", "#1793d0"], # General Selection 
          ["#e53935", "#e53935"]] # Urgent Selection 

widget_defaults = dict(
    font='DejaVu Sans Medium',
    fontsize=14,
    padding=2,
    background = colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                         linewidth = 0,
                         padding = 4,
                         foreground = colors[1],
                         background = colors[0]
                          ),
                widget.Image(
                         filename = "~/.config/qtile/icons/python-white.png",
                         scale = "True",
                         margin_y = 3
                            ),
                widget.Sep(
                         linewidth = 0,
                         padding = 2,
                         foreground = colors[1],
                         background = colors[0]
                          ),
                widget.GroupBox(
                         margin_y = 3,
                         margin_x = 3,
                         padding_y = 5,
                         padding_x = 5,
                         borderwidth = 0,
                         active = colors[1],
                         inactive = colors[2],
                         rounded = False,
                         highlight_color = colors[3],
                         highlight_method = "line",
                         foreground = colors[1],
                         background = colors[0],
                         hide_unused = False
                          ),
                widget.WindowName(
                         max_chars = 40,
                         format = '|  {name}'
                                 ),
                widget.GenPollText(
                         update_interval=1, 
                         func=lambda: subprocess.check_output("/home/atb43/.config/i3/blocks/music.sh").decode("utf-8")),
                widget.TextBox(text = ''),
                widget.CPU(
                         format = '{load_percent}%',
                         update_interval = 2
                          ),
                widget.TextBox(text = ' | '),
                widget.TextBox(text = ''),
                widget.Memory(
                         format = '{MemUsed}MB',
                         update_interval = 2
                             ),
                widget.TextBox(text = ' | '),
                widget.TextBox(text = ''),
                widget.ThermalSensor(),
                widget.TextBox(text = ' | '),
                widget.TextBox(text = ''),
                widget.Volume(),
                widget.TextBox(text = ' | '),
                widget.Clock(format='%a %b %d, %H:%M'),
                widget.Sep(
                         linewidth = 0,
                         padding = 1,
                         foreground = colors[1],
                         background = colors[0]
                          ),
                widget.Systray(
                         icon_size = 16,
                         padding = 4
                              ),
                widget.Sep(
                         linewidth = 0,
                         padding = 6,
                         foreground = colors[1],
                         background = colors[0]
                          ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='zoom'),  # gitk
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
