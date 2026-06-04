
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
image main_menu_background = HBox(
    "images/menu screen.png"
)

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_background"
    style_prefix "mm"

    vbox:
        xpos 120
        yalign 0.5
        spacing 25

        textbutton _("New game") action Start()

        textbutton _("Continue") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

style mm_button_text:
    size 45
    font "fonts/Cheboygan.ttf"
    idle_color '#BBAF9D'
    hover_color '#F12F34'
    selected_color '#96211D'
    insensitive_color '#8888887f'
