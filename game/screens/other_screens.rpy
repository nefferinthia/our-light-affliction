
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
Writing, sprite art, background art, CG art, GUI design and scripting by {a=https://nefferinthia.itch.io/}nefferinthia{/a}. Additional writing, proofreading, additional CG rendering by {a=https://tenshistudios.itch.io/}tenshideve{/a}. GUI programming by {a=https://actualpanda.itch.io/}ActualPanda{/a}. Music composed by {a=https://selenn.itch.io/}Selenn{/a}.

Third party tools used include {a=https://cuteshadow.itch.io/layeredimage-visual-editor-v3}Layered Image Visual Editor in Ren'Py{/a} by CuteShadow, {a=https://makevisualnovels.itch.io/mvn-renpy-transition-kit}Make Visual Novels RenPy Transition Kit{/a} by Stella @ MakeVisualNovels, Blur shader by lauwurence and {a=https://wattson.itch.io/renpy-wave-shader}Ren'py Wave Shader{/a} by Wattson

SFX sourced from {a=http://www.kurage-kosho.info/}Kurage Kosho{/a}, Filmcow, {a=http://www.vita-chi.net/sozai1.htm}Vita-chi Sozaikan{/a}, {a=http://yamicafe.nekonikoban.org/index.html}Yami Cafe{/a}, {a=https://otologic.jp/}OtoLogic{/a}, {a=https://osabisi.sakura.ne.jp/m2/material3.html}osabisi{/a}, {a=https://maou.audio/}Maou Tamashii{/a}, {a=https://taira-komori.net/freesound.html}Taira Komori{/a} and {a=http://freesound.org/}Freesound{/a} (including users {a=http://www.jshaw.co.uk/}InspectorJ{/a}, {a=https://freesound.org/s/188606/}TimPryor{/a}, {a=https://freesound.org/s/167074/}DrMinky{/a} and {a=https://freesound.org/s/270478/}LittleRobotSoundFactory{/a}).

Silhouette sprites by {a=https://izayou.blog.shinobi.jp/}Rurichou{/a}. Battle cut-in CGs by {a=https://arimia.itch.io/}Arimia{/a}.

EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


screen about():

    tag menu

    use game_menu(_("About"))

    hbox:
        null width 500

        viewport:
            style_prefix 'game_menu'
            mousewheel True draggable True pagekeys True
            scrollbars "vertical"

            has vbox
            style_prefix "about"

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _(
            "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label_text:
    size 36


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"))

    hbox:
        null width 500
        
        viewport:
            style_prefix 'game_menu'
            mousewheel True draggable True pagekeys True
            scrollbars "vertical"

            has vbox
            style_prefix "help"
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button:
    xmargin 12

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    xalign 1.0
    textalign 1.0
