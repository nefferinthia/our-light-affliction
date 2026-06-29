## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the title and navigation.
##
## This screen no longer includes a background, and it no longer transcludes
## its contents. It is intended to be easily removable from any given menu
## screen and thus you are required to do some of the heavy lifting for
## setting up containers for the contents of your menu screens.
##

init python:
    _game_menu_screen = "saves"

screen game_menu(title):

    style_prefix "gm"

    window: 
        if title == _("Saves"):
            background Image("gui/save load screen.png")
        else:
            background Image("gui/history screen.png")
    vbox:
        
        xpos 60 yalign 0.5
        spacing 6

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            # textbutton _("Save") action ShowMenu("save")

        textbutton _("Saves") action ShowMenu("saves")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and
            ## unnecessary on Android and Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

    textbutton _("Return"):
        style "return_button"
        action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style return_button:
    
    xpos 60
    yalign 1.0
    yoffset -45

style return_button_text:
    
    font "fonts/Cheboygan.ttf"
    idle_color '#BBAF9D'
    hover_color '#F12F34'
    selected_color '#96211D'
    insensitive_color '#8888887f'

style game_menu_viewport:
    xsize config.screen_width-620
    ysize config.screen_height-200
    align (1.0, 0.5)

style game_menu_side:
    yfill True
    align (1.0, 0.5)

style game_menu_vscrollbar:
    yalign 0.5
    ysize config.screen_height-200
    unscrollable "hide"

style game_menu_label:
    padding (10, 10)
style game_menu_label_text:
    size 45

style gm_button_text:
    size 45
    font "fonts/Cheboygan.ttf"
    idle_color '#BBAF9D'
    hover_color '#F12F34'
    selected_color '#96211D'
    insensitive_color '#8888887f'
