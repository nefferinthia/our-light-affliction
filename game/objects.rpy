define _scene_show_hide_transition = Dissolve(0.15)
define fastdissolve = Dissolve(0.15)

transform closeup:
    zoom 2.0
    yalign 0.15
    xalign 0.5

transform halfcloseup:
    zoom 1.5
    yalign 0.15
    xalign 0.5

transform halfcloseupl:
    zoom 1.5
    yalign 0.15
    xpos 0.35

transform normal:
    zoom 1.0
    yalign 1.0

layeredimage lucifrid:
    zoom 0.5

    always "lucifrid_base"

    group expressions auto:
        attribute neutral default
        
    group arms auto:
        attribute guardedhips default

layeredimage side edelweiss:
    zoom 0.5

    always "edelweiss_base"

    group blush auto

    group expressions auto:
        attribute neutral default

layeredimage edelweiss:

    group blush:
        attribute slightblush default null
        attribute deepblush null
        attribute none null

    group expressions:
        attribute angry null
        attribute awkward null
        attribute conflicted null
        attribute determined null
        attribute laugh null
        attribute neutral null
        attribute panic null
        attribute pout null
        attribute rueful null
        attribute smile null
        attribute smug null
        attribute tearful null
        attribute unamused null

layeredimage ilya:
    zoom 0.5

    group base auto:
        attribute polite default:
            "ilya/polite.png"
        attribute stiff:
            "ilya/stiff.png"

    group expressions:
        attribute annoyed_smile:
            "ilya/expressions/annoyed_smile.png"
        attribute baffled:
            "ilya/expressions/baffled.png"
        attribute calm default:
            "ilya/expressions/calm.png"
        attribute calm_smile:
            "ilya/expressions/calm_smile.png"
        attribute cold:
            "ilya/expressions/cold.png"
        attribute cold_smile:
            "ilya/expressions/cold_smile.png"
        attribute determined:
            "ilya/expressions/determined.png"
        attribute frown:
            "ilya/expressions/frown.png"
        attribute gentle:
            "ilya/expressions/gentle.png"
        attribute pity:
            "ilya/expressions/pity.png"
        attribute sigh:
            "ilya/expressions/sigh.png"

layeredimage emrys:
    zoom 0.5

    group base auto:
        attribute casual default:
            "emrys/casual.png"
        attribute alert:
            "emrys/alert.png"

    group blush:
        attribute none default:
            "emrys/none.png"
        attribute blush:
            "emrys/blush.png"


    group expressions:
        attribute big_smile:
            "emrys/expressions/big_smile.png"
        attribute confused:
            "emrys/expressions/confused.png"
        attribute determined:
            "emrys/expressions/determined.png"
        attribute frowning:
            "emrys/expressions/frowning.png"
        attribute hurt:
            "emrys/expressions/hurt.png"
        attribute neutral default:
            "emrys/expressions/neutral.png"
        attribute small_smile:
            "emrys/expressions/small_smile.png"
    
    group glasses:
        attribute glasses default:
            "emrys/glasses.png"