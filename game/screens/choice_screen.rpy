
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

init python:
    hovered_choice = -1

screen choice(items):
    style_prefix "choice"

    vbox:
        for idx, an_action in enumerate(items):
            $ choice_text, tooltip_text = an_action[0].split("#")

            button:
                action [Hide("full_choice", dissolve), an_action.action]
                style "choice{}".format(idx+1)
                hovered Show("full_choice", dissolve, idx, tooltip_text)
                unhovered Hide("full_choice", dissolve)
                text choice_text
            
screen full_choice(i, t):
    window:
        background Frame("gui/choice button {}.png".format(i+1), 20, 20, 50, 20)
        padding (20, 20, 100, 20)
        xsize 600
        xalign 0.5
        yalign 0.7
        text t

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 33

style choice1:
    idle_background Frame("gui/choice button 1.png", 5, 5, 30, 5)
    hover_background Frame("gui/choice button 1 hover.png", 5, 5, 30, 5)
    xsize 1355
    padding (30, 30)

style choice2:
    idle_background Frame("gui/choice button 2.png", 5, 5, 30, 5)
    hover_background Frame("gui/choice button 2 hover.png", 5, 5, 30, 5)
    xsize 1355
    padding (30, 30)

style choice3:
    idle_background Frame("gui/choice button 3.png", 5, 5, 30, 5)
    hover_background Frame("gui/choice button 3 hover.png", 5, 5, 30, 5)
    xsize 1355
    padding (30, 30)

style choice_button_text:
    yalign 0.5

style choice_button_text:
    is default # This means it doesn't use the usual button text styling
    xalign 0.5 yalign 0.5
    idle_color "#ccc"
    hover_color "#fff"
    insensitive_color "#444"
