## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 600
define config.thumbnail_height = 340

style saves_label_text:
    size 45

screen saves(slot=None):

    tag menu

    use game_menu(_("Saves"))

    default name = "New Save..."
    default name_input = ScreenVariableInputValue("name", default=False)

    fixed:
        if slot:
            image "gui/save slot.png"
            
        hbox:
            null width 500
            frame:
                xsize 350
                vbox:
                    style_prefix "saves"
                    null height 40
                    label "Saves"
                    viewport:
                        style_prefix "file_slots"
                        mousewheel True draggable True pagekeys True
                        scrollbars "vertical" yinitial 0.0

                        vbox:
                            button:
                                key_events True
                                action [SetScreenVariable("name", ""), name_input.Toggle()]

                                input:
                                    value name_input
                                    action [
                                        name_input.Toggle(), 
                                        SetVariable("save_name", name_input.get_text()), 
                                        FileSave(None, confirm=False, page=1, action=ShowMenu("saves"))
                                    ]

                            $ slots = FileUsedSlots(1)

                            for s in slots:
                                if FileLoadable(s, page=1):
                                    if FileSaveName(s, page=1) != '':
                                        if s == slot:
                                            textbutton FileSaveName(s, page=1)
                                        else:
                                            textbutton FileSaveName(s, page=1) action ShowMenu("saves", slot=s)
                                    else:
                                        $ time = FileTime(s, page=1,
                                                    format=_("{#file_time}%Y-%m-%d %H:%M"),
                                                    empty=_("empty slot"))
                                        textbutton time action ShowMenu("saves", slot=s)
            null width 320
            if slot:
                vbox:
                    null height 150
                    add FileScreenshot(slot, page=1) xysize (config.thumbnail_width, config.thumbnail_height)
                    null height 50
                    $ time = FileTime(slot, page=1,
                        format=_("{#file_time}%H:%M"),
                        empty=_("empty slot"))
                    text "Save Time:   " + time xalign 0.5
                    if FileSaveName(slot, page=1) != '':
                        text "Save Name:   " + FileSaveName(slot, page=1) xalign 0.5
                    null height 100
                    hbox:
                        xalign 0.5
                        textbutton "Overwrite" action [SetVariable("save_name", FileSaveName(slot, page=1)), FileSave(slot, confirm=True, page=1, action=ShowMenu("saves", slot=slot))]
                        null width 20
                        textbutton "Load" action  FileLoad(slot, confirm=True, page=1)
                        null width 20
                        textbutton "Delete" action [FileDelete(slot, confirm=True, page=1), ShowMenu("saves")]
                        
screen save(slot=None):

    tag menu

    use file_slots(_("saves"), slot=slot)


screen load(slot=None):

    tag menu

    use file_slots(_("Load"), slot=slot)

screen file_slots(title, slot=None):

    use game_menu(title)

style file_slots_viewport:
    xsize 350
    ysize config.screen_height-200
    yoffset 50

style file_slots_side:
    yfill True

style file_slots_vscrollbar:
    yalign 0.5
    ysize config.screen_height-200
    unscrollable "hide"


