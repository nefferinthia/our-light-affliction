define _show_hide_transition = Dissolve(0.15)
define fastdissolve = Dissolve(0.15)

layeredimage lucifrid:
    zoom 0.5

    always "lucifrid_base"

    group expressions auto:
        attribute neutral default
        
    group arms auto:
        attribute guardedhips default

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
        attribute small_smile default:
            "emrys/expressions/small_smile.png"
    
    group glasses:
        attribute glasses default:
            "emrys/glasses.png"