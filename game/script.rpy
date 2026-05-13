# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Edelweiss", image="edelweiss")
define em = Character("Emrys", image="emrys")
define l = Character("Lucifrid", image="lucifrid")
define i = Character("Ilya", image="ilya")
define n = Character(None, kind=nvl)

#HOLD UP YOU CAN CHANGE EXPRESSIONS MID-LINE
#lines longer than 1 laptop screen should be split in 2

label start:
    
    default positive_arc = 0
    default negative_arc = 0
    default lucy_yan = 0
    default ilya_respect = 0
    default ilya_affection = 0
    default lucy_distrust = False

    default momconvodiviner = 0
    default momconvolucy = 0
    default momconvoilya = 0

    default true_ending = 0
    default lucy_ending = 0
    default ilya_ending = 0
    default bad_ending = 0

    scene black

    n "To those of us who can see {i}them{/i}...{w} there are two paths available."
    n "One is to work towards peace in equilibrium with the realm beyond as diviners,"
    n "the other to stand firm in protecting humans by eradicating dangerous apparitions as exorcists."
    n "But inscribed upon the gate to both these paths stands a warning that all must heed:"
    n "To intertwine the mortal realm with the realm beyond can lead to naught but misfortune."

    nvl clear
    scene classroom day

    "Out of the corner of my eye I see something crawling. It's {i}them{/i} again."
    "I don’t know what happened to this school. We’ve been having a serious spider plague."

    show edelweiss determined

    e "Look, they're back! The spiders! There’s a whole bunch of them right there in the corner."
    "Emrys looks to where I point but merely shoots me a confused glance."

    show emrys casual confused

    em "Edelweiss, are you getting enough sleep? I’m starting to worry about you."

    show edelweiss awkward

    e "Oh, um... Never... mind?{nw=1}"
    
    show edelweiss smile
    extend " I-it was just a joke! Don't look into it too much!"
    em "If you say so. Just take care of yourself, alright?"

    hide emrys

    "Oops, that was awkward. I guess I should’ve gotten the hint when I brought up our school’s newest denizens and no one seemed to have a clue what I was on about."
    "They must be apparitions."

    #cut in image of spiders? opt.

    "But it’s strange, even for someone with diviner blood, simple creatures often escape notice. They’re just spiders, there doesn’t appear to be anything too noteworthy about them."
    "Pitch-black with red eyes... They’re creepy. I wish I couldn’t see them."
    "At the desk beside me Emrys is continuing diligently with our homework, but I can’t seem to focus."
    "Ah, who cares about schoolwork! The only reason I’m attending this place is because the barrier between our world and the spirit realm is thin here."
    "One day I’ll be the head of our family, a top class diviner! No mathematics are going to help me with that."

    show emrys small_smile

    em "You’re distracted."
    "His voice drops to a whisper."

    show emrys determined

    em "{size=-8}Don’t tell me... the spiders are from the beyond?{/size}"
    "Emrys has been in the employ of my family since we were children. He doesn’t have the ancient blood required to see apparitions properly, but he can sense stronger ones by virtue of his training."
    "Practical abilities aside, growing up as a diviner can be rather lonely. Having him around as a friend who understands, who I don't need to hide anything from, has been a blessing."

    show edelweiss neutral

    e "Most likely. But something is off. Why do I see them without even focussing on it? They're just bugs, spiritual power nigh zero."
    "Suddenly the spiders all seem to stand on high alert and rush out of the classroom."
    "I can’t help myself—I need to find out what’s going on."
    "It’s my duty to keep the balance between the realms. This is way more important than homework!"
    "I get up casually to follow the spiders down the hallway."
    "Emrys rises from his desk."
    em "Where do you think you’re going?"

    show edelweiss determined

    e "It’s important! The spiders are up to something!"

    show emrys alert

    em "Then I’m coming with you."

    show edelweiss smug

    e "Fine... Do as you wish, just don’t draw too much attention."

    show emrys confused alert

    "He shoots me an incredulous glance."
    "Okay fine, if anyone’s going to draw too much attention it’s probably me."
    "But I have my secret technique. If you act like you know what you’re doing, no one will think you’re not supposed to be doing it."

    scene hallway day
    with MVNStainedGlass10

    "As we leave the classroom, the last few arachnids scurry up the steps and out of our sight."

    show edelweiss neutral

    e "They’re going upstairs? I’ve never been to the fourth floor..."

    show emrys small_smile casual

    em "Well, it's officially off-limits."
    em "You're not about to let that stop you, I presume."
    "He doesn't sound judgmental, just matter-of-fact. A mischievous smile finds its way onto my face as I nod."

    scene black
    with fade
    scene hallway day
    with MVNStainedGlass10

    #sfx creak
    "As we climb the staircase, the lights grow dimmer. Wooden floorboards creak underneath my loafers and the dust in the air makes my throat go dry."
    "Only a few steps later I feel an uncomfortable shiver creep across my back."
    "Did I imagine it?"
    "No, I really feel something!"

    show edelweiss panic slightblush

    e "{size=+8}Eeeek!!{/size}"
    "I flail around in panic and a spider drops to the floor."

    show edelweiss angry

    e "No! Bad spider! My back is not your hiding place!"
    "The spider shrinks away into a corner as if it understood my scolding."
    "Oh no, I feel a little bad now..."
    "I turn around again and look ahead into the dark hallway, so dark that I can’t even tell where it ends."
    "Wait, where's Emrys? My eyes trail to where he was standing, but not a trace of him remains."
    "Oh, this is bad. He came to keep an eye on me and now I’m the one who put him in danger!"
    "?!"
    "What was that sound? I rush to where it seemed to be coming from."
    #sfx creak
    "A classroom door slings slightly ajar with a creak, and hundreds of shining, scarlet eyes peer at me ominously from the other side."
    "I swallow hard. Okay, calm down, you've got this. For Emrys."

    #door sfx
    #scary ominous Lucifrid cg??, camera pans to emrys

    scene hideout placeholder
    with MVNStainedGlass10

    "There he is—hanging in a large web against the wall. Surrounding him are numerous of the spiders we followed here and some of their larger brethren."
    "A boy about our age stands facing him. Four eyes, four arms and a wide, fanged grin betray his inhuman nature. If I had to guess, he's the one controlling the spider troops."
    "I can’t let my guard down here, apparitions don’t usually meddle in human affairs."
    "If I can only figure out what he wants, we should be able to resolve this."

    show edelweiss determined

    e "L-let Emrys go! He’s my assistant!"
    "I stumble over my words despite myself. So much for intimidation."

    show lucifrid invitinghips grin

    l "Oh, you came! I’ve been looking for you."
    "His grin is almost innocent."

    show lucifrid evilsmile invitinghips

    l "Don’t worry about him, he’s safe up there, you know. The poison’s only knocked him out. {i}Hehe.{/i}"

    show lucifrid evilsmile invitinghips at closeup

    "The boy apparition is upon me in a flash, his movements sudden. {i}Inhuman{/i}. I back away instinctively—his face is too close."
    e "You’ve been looking for me? What business do you have with me?"
    "I try to stay calm, but I’m at an undeniable disadvantage. I can't falter here, I just have to bluff my way through."
    "If I have something he wants then I can leverage it. Apparitions may not follow human rules but they’re not complete savages."

    show lucifrid guardedopen neutral at closeup

    l "Well, first things first, I believe an introduction is in order."
    #sfx finger snap
    "At the snap of his fingers, the door behind me shuts and his familiars fall into a practiced formation."
    "He bows to me as he says his next line."

    show lucifrid guardedopen evilsmile at closeup

    l "My name is Lucifrid, prince of spiders and one of the deities on the dark side of the barrier of this school."
    l "And you... are the strongest human specimen this school has to offer."
    l "It seems my plan to lure you here worked out in my favour."
    "Tch... Seems I've been dancing to his tune the whole time."
    "I keep my voice firm."
    e "I'm Edelweiss, though I suppose I don't have to inform you. That boy you’ve so rudely accosted is Emrys."

    show lucifrid threateninghips neutral

    "He clasps two of his arms behind his back in a solemn pose, using the other two to pull at Emrys’ uniform in a part-curious, part-disgusted manner."
    l "Now what are you doing spending your time with a halfwit such as this?"
    "Right, apparitions only respect spiritual power. I just have to go along with his view."

    show edelweiss neutral

    e "He’s my assistant. I delegate any work not fit for my hands to him."

    show lucifrid innocent

    l "Hmmmm, is that so?"

    show lucifrid evilsmile

    l "It seems like he’s causing you more trouble than he’s getting you out of."

    show lucifrid ominous

    l "I think I’d be doing you a favour if I disposed of him."
    "His grin grows more menacing. I feel my heart beating in my throat."
    "What do I do? What do I do?!"

    show lucifrid grin

    l "{i}Ehehehe!{/i} Your scared face is really cute, miss."

    show edelweiss angry

    e "Emrys is my property! Don’t lay your hands on him."
    "My voice quakes a little. I doubt I sound convincing, but it’s too late to drop my act."

    show edelweiss determined

    e "Your business is with me, isn’t it?"
    #sfx footsteps
    "He walks up to me. With every step forward he takes, I take one step backward, until my back is against the wall."

    show lucifrid evilsmile guardedopen at halfcloseup

    l "So, will you offer yourself in exchange for him?"
    l "I’d be happy to let him go if I receive something more... valuable."    
    "Ugh, this was his plan all along, wasn’t it? I walked right into his trap."
    e "What do you want from me?"

    show lucifrid neutral at halfcloseup
    l "I need a strong human’s power. Become my assistant. I promise I won’t treat you badly."
    show lucifrid grin at halfcloseup
    l "Well, you won’t die at least, hehe."
    e "And you promise you’ll let Emrys go? You’ll never bother him again?"
    show lucifrid innocent at halfcloseup
    l "I swear it! I’ll even make sure he doesn’t remember a thing."
    "I breathe a small sigh of relief. Apparitions lie and cheat with the best of them, but their formal promises are usually binding."
    "I'll figure my way out of this situation somehow, as long as I can keep Emrys safe."
    "Though I have no idea what he could want from me as his assistant..."
    "Humans have little influence on apparition affairs, and if apparitions have interest in humans at all, it's usually to consume their spiritual energy."
    "But surely if that's all he wanted then this would be an unnecessarily roundabout method..."
    "It's no use. I'll find out eventually."
    e "I’ll help you. But no life-threatening situations! And only during after-school hours!"
    show lucifrid pout at halfcloseup
    l "We’re going to have to work on the bond of trust between us. I already said I wouldn’t treat you badly..."
    "Ugh, you won’t manipulate me with that cute act!"
    "I can't tell at all what his intentions are, or whether anything he's saying is sincere, and it unsettles me."

    show lucifrid evilsmile at closeup
    l "Well, then, let’s make our contract."
    "His four hands press against the wall behind me, pinning me in place. Before I have time to process what’s happening he presses his lips against mine."
    show lucifrid neutral at closeup
    l "Let this be proof of the invisible ties that bind us, now and forever. Neither life nor death shall come between us."
    "He snaps his fingers again and Emrys falls from his web. A procession of spiders softens his fall and parades him out of the classroom."
    show lucifrid neutral at halfcloseup
    l "Don’t worry, they’ll deliver him safely back to where he came from."
    show lucifrid grin at halfcloseup
    l "Now, we have work to do, my dearest partner!"

    scene black
    with fade

    scene hideout placeholder
    with MVNStainedGlass10
    show edelweiss angry slightblush

    e "What on Earth was that all about?!"

    show lucifrid neutral thinkingrelaxed
    l "Hmm, what do you mean?"
    e "That was my first kiss! You don’t just get to take it!"
    
    show lucifrid innocent thinkingopen
    l "Oh, that? I mean, we could’ve intermingled our blood if you preferred. I thought this would be most agreeable to human sensibilities."
    l "Was I wrong?"

    show edelweiss pout

    e "..."

    show edelweiss deepblush

    e "..."
    e "Hmph! If that really was the only way then I guess there’s no helping it!"

    show lucifrid thinkingrelaxed
    l "But I just said it wasn’t the only way?"

    show edelweiss angry slightblush

    e "Argh!"

    scene hideout placeholder
    with MVNStainedGlass10
    
    "The setting sun coats the abandoned classroom in a pleasant, warm glow."
    "The air is dense with specks of dust that twirl and dance, illuminated by the sun’s rays."
    "Desks and chairs are stacked haphazardly against the south wall, holding forgotten belongings never to be retrieved again."
    "Only the astute eye would notice an unnatural amount of spiders hiding in various nooks and crannies, marking the territory of their prince."

    show lucifrid grin invitinghips

    l "Well, it’s about time for me to give you your first task!"

    show lucifrid neutral thinkinghips

    l "Before we can get to work, we’re going to need a suitable base of operations..."
    e "What do you even need a human for anyway?"

    show lucifrid evilsmile

    l "All in due time, my dearest partner."

    show lucifrid invitinghips grin

    l "First, this place needs to be set in order! My classroom should not be this decrepit."

    show edelweiss smug

    e "Is an abandoned classroom really the best you can do for a hideout?"

    show lucifrid evilsmile at halfcloseup

    "His face inches up to mine. A chill runs up my spine."
    "I let my guard down. I shouldn’t forget he’s dangerous."
    "The way his face can change from charming to terrifying at the drop of a hat... I can’t decide if I’m impressed or disturbed."
    l "Do you not trust my judgment?"

    show lucifrid neutral guardedrelaxed at normal

    "He turns on his heels and paces the room as he continues."
    l "The boundary is thinnest in this exact location. If an apparition wants to cross over into this world, they’re likely to pass through this classroom."
    l "Not to mention I can tap into my powers more easily without crossing over."
    "I listen to his explanation as I follow his instructions to tidy up the room, gathering up the belongings of students who have probably long graduated."

    show lucifrid invitingrelaxed innocent

    "Lucifrid smiles and pats my head. Well, tries to, as I push one of his four hands away."
    l "You’re surprisingly obedient, aren’t you?"

    show edelweiss pout slightblush

    e "Hmph, I just have a sense of responsibility."
    e "..."

    show edelweiss unamused none

    e "But you're right! Why am I doing this? You have more hands than I do!"

    show edelweiss angry

    e "And you’re a fiend who threatened my assistant, forced my hand into this arrangement and {i}stole my first kiss!{/i}"

    show lucifrid thinkingrelaxed

    l "Hmmm~ You’re cute even when you’re angry."
    l "Did the kiss bother you that much?"

    show lucifrid invitingrelaxed grin

    l "My~ soul~ mate~"
    "What kind of apparition is he..."
    "Why did I have to get caught up in this..."
    "Emrys better be real grateful."

    hide lucifrid

    "The sun sinks further and further as I thoroughly clean the dusty classroom."
    "In the meantime, Lucifrid merely lounges around while playing with his familiars."
    "They still give me the creeps..."

    show edelweiss determined

    e "Why don’t you help out a little?! Or at least ask your little followers to help me out!"
    "He turns around languidly and the very movement annoys me."
    "Here I am, toiling away my beautiful summer afternoon—time I could have been spending so many better ways—and he can’t even appreciate it!"
    "After a long pause he opens his mouth."

    show lucifrid thinkingrelaxed

    l "Hmm..."
    l "Let me think..."
    e "Answer me properly!"

    show lucifrid grin guardedopen

    l "Alright, I won’t help then, hehe!"

    hide lucifrid

    "He turns back around and continues his game with the spiders."
    "..."
    "A deep sigh escapes me."
    "By the time everything is sorted out and set up, the day has firmly turned into night and I'm pretty sure we’re the only ones left in the school building."

    show edelweiss unamused

    e "Well Your Majesty, please take to your throne."
    "I point to the paint-peeled chair behind the desks arranged meticulously according to Lucifrid’s vision, but the prideful smirk on his face doesn’t falter for a second."
    "Something tells me he isn’t taking my sarcasm the way I intended it."

    show lucifrid grin invitinghips

    l "Well done, my assistant. I think this deserves a little reward."
    "My suspicious expression remains undisturbed."
    "One of the little spiders runs up to me carrying a piece of candy on its back."
    "I try my hardest to keep frowning but fine, it’s kind of cute."
    "I seat myself atop one of the desks as I unwrap the spider’s treat and pop it into my mouth."
    "It’s sour and sweet, melting easily on my tongue." 
    "Not nearly equivalent to all my hard work, but I'll take it."

    show edelweiss neutral

    e "So, can you tell me your master plan yet?"

    show lucifrid evilsmile guardedhips

    l "Edelweiss of Hesgothia. I’ve been sensing your power since you entered this school."
    l "Your blood has a strong affinity with the spirit realm, but have you ever been across the boundary?"

    show edelweiss smug

    e "H-heh, what kind of top class diviner would I be if I hadn’t even set foot in the spirit realm myself?"

    show lucifrid innocent at halfcloseup

    l "Hmmmm, is that so?"
    "He gently twirls a strand of my hair around his finger as his eyes seem to pierce straight through to my core."

    show lucifrid evilsmile invitinghips at halfcloseup

    l "{i}Ehehehe!{/i}"

    show lucifrid ominous threateninghips at halfcloseup

    l "It’s no good to lie to your trusted partner."
    "Heat rises to my cheeks. How does he know I was bluffing...?"

    show lucifrid guardedopen grin

    l "If you don’t properly anchor yourself you won’t be able to return, you know!"

    show lucifrid evilsmile

    l "But you are bound to me, so I’m all you need."

    show lucifrid neutral guardedopen

    l "You’ll be seeing a lot of the beyond soon."

    show lucifrid guardedhips

    l "But fine, let me show you exactly where you fit into my plans..."
    "He claps his hands—all four of them—and sinks two of his arms into the desk arrangement, seemingly phasing them out of existence."
    "Is he... reaching into the beyond? Interesting."

    hide lucifrid

    "Bit by bit I’m becoming more aware of exactly how much I don’t know, and don’t understand about apparitions."
    "If my mother were here, would she have been able to handle this situation better? Would she have bested Lucifrid the moment they met?"
    "If my mother were here... I could have at least asked for her advice."
    "Her figure appears in my mind, but she’s faint and I can’t quite make out her face. It’s been a long time after all."
    "Would she scold me? If father knew I had somehow gotten myself into a contract with an apparition deity he would be furious..."
    "But I have a feeling she would’ve responded differently."
    "Mom" "Oh Edie, reckless as always."
    "The mother in my imagination laughs softly, her voice clear as day."
    "Mom" "You’ve made your own mess, so it’s your duty now to get yourself out of it. Rise to the challenge, it can only help you grow."
    "The encouragement somehow doesn’t ring as hollow as expected. Is she... really there?"
    "But that would be impossible."
    #book smack sfx
    "I snap out of my reverie with a start."

    show lucifrid guardedhips displeased

    l "Edelweiss... pay attention. This part is important."

    show lucifrid invitinghips neutral

    l "Here. This is my tome. Everything contained in it is mine to control."
    "He rifles through the pages, stopping upon a page filled with red ink that seems like it has barely dried."
    "I can’t make out any of the characters until he slowly drags his finger over the words."

    show edelweiss awkward slightblush

    e "Ah! It’s my name."

    show lucifrid evilsmile

    l "Yes, it is proof that we are bound together."

    show lucifrid neutral thinkingrelaxed

    l "Names hold a high authority in the spirit realm, but only humans can truly claim the names of apparitions."

    show lucifrid thinkingopen

    l "Apparitions are like smoke, their names can make them corporeal, but only if there is something corporeal to tie them down. Do you follow?"

    show edelweiss none neutral

    e "Somewhat... I think..."
    "My lessons covered something like this once, but I can’t quite recall the details."
    "A lot of my family’s knowledge is passed down for generations through nothing but scrawled notes and incomplete observations."
    "Father is from a minor branch family and mostly minds the affairs at home, so when mother passed away young, she took a lot of information with her to the grave."

    show lucifrid grin guardedrelaxed

    l "Well, it matters not. What matters is that you will claim the names of all my opponents for me, so that I may reign over the dark side of this school undisputedly."

    show lucifrid invitingrelaxed

    l "Don’t worry, I’ll let you reign alongside me, that’s only fair."
    "He laughs, unconcerned with whether I {i}want{/i} to reign alongside him."

    show edelweiss awkward

    e "Your... opponents? You have many of those?"

    show lucifrid smug guardedrelaxed

    l "Oh, apparitions rarely play nice if someone’s encroaching on their territory."

    show lucifrid neutral guardedopen

    l "There’s many who don’t even have capability for reason, though most are of the live and let live mentality."

    show lucifrid evilsmile

    l "Though I personally do not intend to let live, {i}ehe.{/i}"

    show edelweiss

    e "So you’re looking to stage a bloody revolution? I’ve become the assistant to an evil oppressor?!"
    "Well, I can hardly say I'm surprised. A noble creature would not have threatened to murder my friend in order to get me to help with his plans."
    "It's just another conflict between apparitions. I can't feel too guilty over whatever I do under coercion, and it's not like they'd care if it was humans in their path..."
    "Well, I just have to play along for now. There has to be some way out of this."

    show lucifrid neutral

    l "Oh, don’t be like that! They’re a disorganised mess right now! I’m doing them a favour by giving them a purpose."

    show lucifrid innocent

    l "A unified spirit realm will be for the benefit of everyone."

    show edelweiss unamused

    e "Everyone except humans..."
    "He responds with nothing but a wide, almost innocent smile. Guess that’s my answer."
    "Well, let's not stir the pot. If I can earn his trust, maybe I can catch him off guard."

    show edelweiss smile

    e "Well, I’ll take it as a learning experience for my future as a diviner!"
    "There’s nothing to do but look on the bright side and make the best of it. Or at the very least convince Lucifrid that that's what I'm doing."

    show lucifrid guardedhips grin

    l "Mm, mm!"
    "He nods emphatically."
    l "I’m glad we were able to see eye to eye!"

    show edelweiss unamused

    e "I wouldn’t quite put it that way..."

    show lucifrid evilsmile invitinghips

    l "I’ll see you here tomorrow after class! For now you’re dismissed!"

    scene classroom day
    with fade
    #school bell sfx
    show emrys casual small_smile

    em "Alright, I'll give you the keyword and you tell me what you know."

    show edelweiss smile

    e "Mm-hm."
    em "{i}Diviner.{/i}"

    show edelweiss awkward

    e "What? Is this really necessary? Of course I know that!"

    show emrys neutral

    em "The basics are the basics for a reason."

    show edelweiss neutral

    e "Individuals from a bloodline with a strong connection to the beyond. They can see apparitions and exercise some power over them."
    em "That's too broad."

    show edelweiss awkward

    e "I wasn't done yet! They keep balance between the human realm and the spirit realm and try to seek peaceful solutions, like sealing an apparition instead of banishing it."

    show emrys small_smile

    em "Alright, what about exorcists?"

    show edelweiss neutral

    e "Similar powers, different approach. They usually possess stronger tools and rituals to dispose of apparitions. They're uh, fight before flight."

    show emrys neutral

    "Emrys opens his mouth, probably to reprimand my casual speech, but closes it again and just nods."
    em "Next, the beyond."
    e "It's where apparitions live. It's like, another layer of this world."

    show emrys determined

    em "I don't think your father will be satisfied with that answer."

    show edelweiss determined

    e "Well, it's vague! We don't even know exactly what it is! Sometimes it's just the same as our world, and sometimes it's completely different."

    show emrys neutral

    em "It's connected to our world, and overlaps in places, but not everywhere. It's oversimplifying to call it another layer."

    show edelweiss pout

    e "Fiiiine."
    em "Next. The boundary."
    show edelweiss neutral
    e "The dividing line between our world and the beyond. Crossing over is possible, but requires rituals, and it's quite dangerous." 
    e "The work of a diviner usually starts when apparitions cross the boundary. Sometimes humans summon them, purposefully or inadvertently. But some of them can cross over on their own."
    
    show emrys small_smile
    em "That's more like it."

    show edelweiss awkward
    e "You really think my dad's gonna ask stuff like this?"
    show emrys neutral
    em "He's trying to be serious about your education. Conducting exams is part of that."
    show emrys small_smile
    em "You'll do fine. Maybe he'll finally let you carry one of your mom's talismans after this."
    show edelweiss pout
    e "As if. I wish he'd take me seriously... How am I supposed to learn without any hands-on experience?"
    "True to his word, Lucifrid has made sure Emrys remembers nothing of his spidery ordeal. He's back to quizzing me on theory like nothing happened."
    "I suppose I'll be getting plenty of hands-on experience soon enough..."
    em "I'll put in a good word for you if you do well on the exam, maybe he'll listen to me."
    show edelweiss smile
    e "Can't believe my own father trusts you more than me but yeah, that might actually help."

    show emrys alert
    em "So with that, wanna hang out at the arcade?"

    show edelweiss awkward
    e "Ah, um, I can’t, I’ve got... stuff."
    "It would be beyond foolish to give up the one advantage I’ve gained by teaming up with Lucifrid, but my mind is drawing a blank on a convincing excuse."
    show emrys casual
    em "What, don’t tell me you’ve started taking your schoolwork seriously! If it's more diviner business I'll help out."

    e "Schoolwork!{nw=1}"
    show edelweiss smile
    extend " Yes, that’s the stuff! You know, with test week coming up and all..."

    show emrys confused
    em "..."
    "A man couldn’t look more incredulous if he tried. Guess Emrys knows me better than that."

    show edelweiss laugh
    e "Ahaha, you got me!"
    show edelweiss smile
    e "Maybe it wouldn’t be a bad idea to blow off steam at the arcade."
    show emrys alert small_smile
    em "I thought losing made your mood worse, not better."
    "Emrys smirks."

    show edelweiss smug

    e "It does. I was more thinking of watching you lose, personally."
    "I mean, Lucifrid {i}did{/i} tell me to meet him after class today but it’s not like I explicitly agreed to it or anything..."
    "Besides, apparitions operate within their own domains. If I just make it out of the school there should be nothing he can do."
    "That settles it."

    show edelweiss smile

    e "Fine, you’re right, I don’t need to do the stuff today."
    show emrys determined
    em "Whatever your \"stuff\" is, it better not be dangerous."
    "I’d say he’s being overprotective, but I can't exactly argue that meddling in apparition domain wars {i}isn't{/i} dangerous."
    "Well, better make something up."
    e "Oh no, of course not! Just, you know, girl things."
    "Like hanging out with spider apparitions. As all girls do."

    scene black
    with fade

    scene hallway day
    with MVNStainedGlass10

    "We make our way down to the first floor and Emrys takes a last minute bathroom break. Tension builds up inside me."
    "This is so not the time! We have to get out of here!"
    "...Is what I’d like to say, but I have to play it cool. Instead I wait patiently by the front entrance."

    #Lucy appears, looking very displeased
    show lucifrid frown guardedclenched

    l "What exactly do you think you’re doing?" 
    l "Foolish human. We are quite literally bound to each other’s life essence and you thought you could sneak out unnoticed?"
    "Though Lucifrid is barely an inch taller than me, right now his presence is looming."
    "The atmosphere of the entire hallway darkens as my pulse speeds up."
    "I can’t do much but stare and stammer. I have no excuse."
    "I {i}did{/i} think I could sneak out unnoticed."

    #Lucifrid smile 
    show lucifrid guardedhips evilsmile

    l "But no matter! I’ll discipline you whatever way it takes. Though I was so looking forward to our burgeoning camaraderie, hehe."

    show edelweiss conflicted

    e "I-I’m sorry! I just didn’t know what to—"

    show lucifrid threateninghips

    "He places two of his hands across my mouth and uses the other two to spin me around. Emrys is walking over."
    l "Hush now, you wouldn’t want him to get suspicious."
    "I try to calm my breathing and pretend I’m not deeply terrified."

    show emrys confused casual
    show lucifrid guardedhips evilsmile

    em "Edelweiss, your face is pale, is everything alright?{nw=1} "
    extend  "{size=-8}...Apparitions again?{/size}"
    "He whispers the last part as he leans in, completely unaware of the third party that has joined in on our little gathering."
    "I didn’t know Lucifrid could willfully erase his presence like that, but I guess Emrys’ spiritual abilities are easily thrown off. He can't see him."

    show edelweiss awkward

    e "Oh yeah, a real scary-looking spider just crawled past. Probably harmless though!"

    show edelweiss neutral

    e "Listen, I got a call and it looks like my plans really can’t wait. I’m sorry for being all wishy-washy. I’ll make it up to you some other time, I promise."

    show lucifrid displeased

    "Lucifrid’s eyes narrow."

    show edelweiss awkward

    e "O-on the weekends, you know. When I have more time!"

    l "This won't do. Say something to throw him off."
    "Well, I know one thing I can say to stop Emrys from digging further. But that's no longer little white lie territory, that's big black lie, and I'm not sure I feel good about it."
    "I look over at Lucifrid nervously, but his menacing glower has lost none of its intensity."
    "I swallow hard."

    show emrys casual small_smile
    em "Just don’t forget I’m not {i}just{/i} your assistant. I want to spend time with you off-duty all the same."
    
    #e warm smile
    show edelweiss slightblush smile

    e "I know that. I’m happy about that."
    "Forgive me Emrys. This is all to protect you."
    e "I would never forget my best friend just because I got a boyfriend."

    show lucifrid smug guardedrelaxed
    show emrys confused blush

    "Emrys blushes while Lucifrid grins widely."
    em "A boyfriend...? When did you find the time to{cps=3}...{/cps} Is he taking good care of you at least?"

    show lucifrid innocent invitingrelaxed

    l "I didn't know you thought of me that way, Edie."
    "Lucifrid languidly slings two arms around me as I try my best to keep my composure."
    "I’m going to regret this, aren’t I?"

    show edelweiss awkward

    e "I’ll tell you the details sometime, once I know for sure it’s the real thing."

    show edelweiss neutral

    e "Just go on ahead, Emrys! I’ll see you in class tomorrow."
    "Emrys lowers his head just a bit bashfully. As I look at his face, the shame of deceit washes over me." 

    hide emrys
    show lucifrid guardedrelaxed

    "I watch his frame move into the distance and promise myself I’ll tell him the truth eventually. He’ll understand.{w} He'll understand, right?"
    "...He'll definitely tell father. I can scarcely imagine the scolding I’ll receive."
    "But what's done is done. Regret can wait."

    show lucifrid grin

    "Lucifrid pushes me forward towards the staircase and I stumble unceremoniously."
    l "Onward, underling. We’ve wasted enough time."

    scene black
    with fade

    scene hideout placeholder
    with MVNStainedGlass10
    show lucifrid guardedrelaxed

    l "Are we clear on the plan?"
    e "I follow your lead and stay behind you until you’ve subdued the enemy, at which point I’ll open the tome and say: ‘Speak thy name and thine allegiance be manifest.’"

    show lucifrid innocent

    "He hums contentedly."

    show lucifrid neutral

    l "Seems like we’re ready."

    show lucifrid evilsmile invitingrelaxed

    l "Now, take my hand. Don’t be afraid."
    "I try to steady my breathing as I link our hands, forming an anchor for safe passage across the boundary. I'm not afraid. I'm not afraid."
    "The hands-on experience father wouldn't allow me... is coming sooner than I expected."

    show edelweiss determined

    e "Wait!"

    show lucifrid neutral

    l "Hmm?"

    show edelweiss smile

    e "Can I whack them over the head with the tome while I chant?"

    show lucifrid grin

    "Lucifrid bursts out laughing."
    l "Well, I don't see why not."

    scene black
    with MVNTurbulence04
    "The air around us contorts and I squint my eyes shut, feeling briefly like I might lose consciousness."
    "All sense perception leaves me except a hazy weightlessness and the feeling of Lucifrid's hand in mine. For a brief moment I am nowhere and everywhere."
    
    scene classroom day
    #classroom beyond
    with MVNTurbulence04
    
    "My feet land on solid ground again and I open my eyes. There stands the prince of spiders with his battalion of familiars, cast in a dim, eerie light. The classroom around us appears... normal."
    "Upon closer inspection, there are eyes peering out from places they shouldn’t be, and everything sways and twists periodically, as though the edges between objects are not quite laws, and more like suggestions of physics."
    "A piercing wind shrieks and howls in a way it should not be able to inside a school building, chilling me to my core."
    "I’m suddenly glad for the faint warmth of Lucifrid’s hand in mine."
    "He looks over me and nods as he steps forward determinedly, defying the fierce headwind opposing us."
    "So we walk. Onward and onward. And onward.{w} And onward."
    "A distance that should have taken us minutes, if not seconds to cross seems to stretch endlessly onward as the blackboard at the front of the classroom remains ever distant."

    show lucifrid threateninghips grin

    l "Come out, come out, wherever you are!"
    "In the blink of an eye, Lucifrid shoots silky threads in four directions, coating the room in pathways for his familiars." 
    "The spider battalion spreads out in a trained formation, attempting to scope out the denizen of this mysterious place."
    e "Who... or what are we even looking for?"
    "I lean forward, trying to peer behind the desks ahead of us."

    show lucifrid neutral

    l "Stay back, Edelweiss. These threads are sharper than they look."
    "I shiver as I jolt back. The room is so cold that even the light glinting menacingly off Lucifrid’s web seems like it could freeze."
    "As he clenches a fist, the web spun around the teacher’s desk coils and cinches, slicing through solid wood with ease."

    #sfx ghost cry
    show lucifrid smug

    l "Heh, I think someone didn’t like that."
    "The howling breeze intensifies into a gale and as Lucifrid spins his web to span more and more of the room before us, frost crystallises on every thread."
    "A glacial maelstrom materialises into a ghastly cloaked figure. Its long hair billows, obscuring its features as it wheezes at us."
    "Ghost" "Leave this place."

    show lucifrid grin
    show lucifrid innocent

    l "Terribly afraid I can’t do that."
    "Lucifrid’s familiars have begun clambering up the creature’s robes."
    "Right as I start to feel a tinge of pity for it, it dashes forward, scattering the arachnid battalion on its vestments and shooting icicles in our direction."
    "Ghost" "Stay away..."
    "Lucifrid avoids the attack nimbly, stopping one of the projectiles just short of hitting me in the process."
    "No time to feel sorry now."

    show lucifrid neutral

    l "Take cover and bide your time."
    "I follow his instructions and hide behind a student’s desk, watching as he continues to taunt the snow spirit."
    "It seems to lose its temper the longer it fails to hit a single strike."

    show lucifrid threateninghips grin

    l "Hehehe, haha! Is that all you've got?"
    "Then it rushes forward just slightly too desperately and carelessly gets tangled in the spider prince’s web. It's trapped now."
    "Lucifrid responds by toyingly flexing his fingers, the web cutting and slicing with his every move."
    "Ghost" "Uuuh..."
    "Isn’t he being too cruel? Our opponent is defenseless!"

    show edelweiss determined

    e "Did no one ever teach you not to play with your food?"
    l "Ah, a classic human saying, isn't it? But where do you think we are?"
    show lucifrid evilsmile

    l "I can even express it in your terms. I believe it goes... \"when in Rome\"?"
    "That smug little..."

    hide lucifrid

    "Instead of waiting for a signal, I decide to cut his playtime short and run ahead with the tome in tow."
    e "State thy name and thine allegiance be manifest!"
    "I smash the creature with all the strength I can muster. I don't even hear the syllables it spits out over the sound of the blood rushing to my head."
    "Ink flows across the tome’s opened pages and the creature slinks away. Immediately the air calms and warmth returns to the room."
    "The breath I didn't know I was holding in slips out with a sigh."
    "Lucifrid dissolves his webs with a swift exhale, his expression displeased."

    show lucifrid neutral guardedopen

    l "You’re not too good at taking orders, are you? My cumbersome partner."

    show edelweiss smile

    e "Partner implies a relationship between equals. I can act on my own authority!"
    e "I got the job done, didn’t I? Who knows, maybe that thing would have broken free from your web in no time!"

    show lucifrid guardedhips smug

    l "Hah, not a chance."

    show lucifrid evilsmile

    l "I wanted to bully that one a little longer! Guess I’ll have to content myself with bullying you."
    "He pinches my cheek just hard enough that it hurts—but I refuse to give him the satisfaction of acknowledging the pain."

    show edelweiss unamused

    e "Hmph. Be careful or I'll teach you another saying. You reap what you sow."

    show lucifrid grin

    l "Hmm, not sure that one's relevant to me. {i}Hehe.{/i}"
    "I shake my head and move on."

    show edelweiss neutral

    e "...So, what happens to that apparition now?"

    show lucifrid invitinghips

    l "It's entirely mine! Powerless until I say the word, its territory incorporated into my domain effective immediately."
    e "So is this classroom free of outside influence on the other side of the boundary too?"
    l "Mhm-mhm! Light side or dark side, it's mine. Though alas, my power is still limited in the human realm."
    e "And that ice spirit is just... gone until you call upon it?"
    l "Familiars are free to wander around as they please! They can't do any harm anyway.{nw=1}"
    show lucifrid innocent
    extend " Endlessly benevolent, aren't I?"
    "It’s... less cruel than I expected, though I suppose pragmatism is the ruling principle here."
    "It leaves me to wonder what a cruel fate for an apparition would even look like."
    e "How do apparitions even die? Do apparitions die?"

    show lucifrid thinkingrelaxed neutral

    l "Hmm, it’s more like they wax and wane... they don’t truly disappear like humans do. Though an eternal waning is pretty much the same as death. As long as someone remembers us and calls upon us, we can return."

    show edelweiss awkward
    show edelweiss rueful

    e "I guess being forgotten is the final end for humans and spirits alike."

    show lucifrid thinkingopen innocent

    l "Well, that’s through natural means. You pesky humans have devised ways to exorcise us. You’re far more cruel than us!" 

    show edelweiss determined

    e "There’s apparitions that threaten to destroy entire communities! Sometimes harsh measures are justified."

    show lucifrid guardedhips grin

    l "Mm, mm. Glad you’re starting to warm to my point of view."
    "Purposefully twisting my words again, huh? Now it’s my turn to pinch his cheek."
    "...Squishy."

    show lucifrid pout

    l "Hey, ow! That hurts!"

    show edelweiss smug

    e "Merely returning the favour. After sowing comes reaping, I warned you."
    l "...These crops are growing unreasonably quickly."
    l "Now off you go, your duty is done. I've had quite enough of you."
    "He reacts like a sulking schoolboy and it betrays the terrifying image of our first meeting."
    "I wonder how old he really is... He looks to be my age, but there’s no way to tell with apparitions."

    show edelweiss neutral
    show lucifrid neutral

    e "I’ll be gone as soon as you escort me back to the light side of the barrier—it's not like I'm here for my own enjoyment." 

    show edelweiss pout

    e "It won’t even be light out anymore at this rate! You’re taking up all my free time..."

    show lucifrid smug
    show lucifrid neutral

    l "I {i}was{/i} considering cutting you some slack tomorrow until your... physical insubordination."
    "He links his hand to mine so we can once again cross the boundary."

    show edelweiss determined

    e "We’re partners! On equal footing! Something like this is nothing. In fact, it’s only the beginning of Edelweiss emancipation."

    show edelweiss smile

    e "For our next mission I’d say I deserve my own spider battalion, or squadron at the very least."

    show lucifrid evilsmile guardedrelaxed

    l "You can try to win their trust, hehe. But don't think they'll let you stage a mutiny."

    show lucifrid ominous

    l "Their eyes are my eyes."

    show lucifrid neutral
    l "Now hush, let's move."

    scene black
    with MVNTurbulence04
    scene hideout placeholder
    with MVNTurbulence04

    "The passage is less violent on my senses this time, but can’t quite be described as pleasant."
    "Perhaps with time I’ll get used to it."
    "My first foray into the beyond... I wouldn’t admit it out loud but without Lucifrid there I would have been terrified."
    "The fear he instilled in me in our first meeting... I'm on the other side of that blade, at least for now."
    "I'm learning and growing, perhaps more than a whole year of my father’s diviner tutoring could do for me."
    "Are you proud, mother? Are you watching over me?"
    "Perhaps soon I’ll finally be like you."

    scene black
    with fade
    scene hideout placeholder
    with MVNStainedGlass10
    #sfx door creak
    "Hmm?"
    "Now this is unusual. It seems like I’m the first one to arrive at our hideout."
    "Almost two weeks have passed since my first meeting with the prince of spiders, and I guess I’ve settled into the rhythm of our after school meetings."
    "I’ve learned that while I am on academy grounds there is no way to escape him. I’ve made my peace with that fact—so I might as well go willingly."

    "I draw a small sigil on the blackboard in chalk, meant to draw out any apparitions in hiding."
    "A number of spiders scurry out of their webs towards me, but Lucifrid is nowhere in sight."

    show edelweiss smile

    e "Hello, little ones. Care to inform me of the location of your master?"
    "Of course, the spiders don’t possess the gift of speech."
    "With their unsettling, abundant gazes settled on me, I can’t help but feel uncomfortable still."
    "I guess... While he’s out, I might as well take the opportunity for exposure therapy. We’re allies now, and it won’t do to be afraid of them."
    "I move closer to them and sit down on the floor, stretching out my arm. The spiders seem apprehensive about my intentions, perhaps they’re not used to acting outside their master’s orders."

    show edelweiss determined

    e "Go forth! Tread upon me!"
    "It worked! The spiders march in disciplined motion. Once they reach my shoulders I speak up once more."
    e "Halt!"
    "I nod in self-satisfaction. There’s nothing to be afraid of if they’ll listen to me."

    show edelweiss smile

    e "Gather on the desk and await further instruction."
    "The spiders seem happy to obey me. It must be some effect of the contract between me and Lucifrid."
    "Do we give off the same spiritual energy now? Is what's his also mine in equal measure? I wonder if I could summon other familiars too."
    "But for now, I ought to focus on what's in front of me."
    "Interested in the spiders' abilities, I spend the next half hour testing out different commands. They’ll happily spin webs to coat substances, or create bridges. It seems they can create sturdy threads or sharp threads, depending on the needed occasion."
    "I want to know what their bite does, but without a target, that will have to wait. They refuse to fight each other at any rate."
    "Tiring of the serious exercise, I remember the candy in my pocket and offer it as a prize in various spider contests."
    "Climbing, running, jumping, spinning the longest threads, or the fastest webs. They appear eager to win my approval."
    e "You did well, little Yang."
    "I pet the favoured child, fastest runner of the cohort, and give him his well-earned reward."
    
    #sfx footsteps
    "The sound of footsteps makes my hair stand on end. An apparition...?"
    "But there is nothing to be afraid of."

    show edelweiss determined

    e "Yang battalion, apprehend the intruder!"
    "The spiders rush behind me and shoot their strings."

    show lucifrid threateninghips worry

    l "I leave you alone for one afternoon and you’ve turned my followers against me already?!"

    show lucifrid guardedhips evilsmile

    l "A wily one, this assistant."
    l "I guess the mutiny isn't far off!"
    "His tone feigns annoyance but I can tell he’s more impressed than anything."

    show edelweiss neutral

    e "Lucifrid! You’re late!"

    show lucifrid evilsmile
    l "I’m happy you missed me! Now please, help me get this mess off."
    "He motions at the silky substance coating his clothes. Well, I guess that was my fault."

    scene black
    with fade

    scene hideout placeholder
    with MVNStainedGlass10

    show lucifrid neutral guardedrelaxed

    l "Today I’ve tidied up most of our task for us."

    show lucifrid neutral
    show lucifrid invitingrelaxed

    l "Here."
    "Lucifrid presents me with a tiny bird slumped in his palm, barely breathing."
    "He doesn’t need to explain much to me, this must be the weakened form of one of the apparitions in his domain."
    "Many apparitions have various forms, the more intricate forms becoming impossible to maintain as they lose power."
    "I wonder if Lucifrid manifests himself in different ways than this; this form doesn’t seem too strenuous in upkeep."
    "I've gotten used to helping him by now. I lend my assistance in various ways: sometimes it's a fight like against the ice spirit, sometimes it's nothing more than using his tome to administer the final rites. Like now."
    "Drawing upon a larger sigil inscribed in one of the desks, I manifest the spider prince’s tome. Its pages scramble open as I recite the incantation."
    e "State thy name and thine allegiance be manifest."
    "The bird croaks something indeterminable, though the tome does not discriminate."
    "Laid to rest on the page, the bird’s physical form fades and the abandoned classroom quiets down once again."

    show lucifrid guardedrelaxed grin

    l "Well done, my dear assistant. It seems a reward is in order!"
    "Lucifrid pats my head. Other than my unimpressed expression I offer no resistance. Choose your battles."

    show edelweiss smile

    e "Alright! Let’s go get ice cream!"

    show lucifrid neutral

    l "You’re aware I can’t leave school grounds?"

    show edelweiss neutral

    e "There’s a vending machine in the gardens, you’ve never used it?"

    show lucifrid pout guardedhips

    l "I have greater concerns than sweet treats."

    show edelweiss smug

    e "Hehe, seems there are some things the humble Edelweiss can teach our dark overlord."

    scene courtyard evening
    with MVNStainedGlass10
    
    "The two of us sit down on a bench in the courtyard, ice cream in hand, basking in the last rays of sun of a clement summer afternoon."
    "The breeze rustles through the trees, obscuring quiet snippets of conversation between students on their way home."
    "I don’t think anyone is paying attention, but I take care to speak quietly nonetheless. If I’m talking to the air, I should at least be subtle about it."

    show edelweiss smile

    e "My father has been quite impressed with me lately. Unsurprisingly, practical experience teaches more about diviner business than the classroom ever could."

    show edelweiss awkward

    e "Well, I didn't mention the cause for the sudden improvement. That would probably impress him less..."

    show lucifrid displeased guardedclenched

    l "Is that what concerns you? Your father’s opinion?"
    "Lucifrid sounds disdainful, as if the very idea of doing something for another person’s approval causes him offense."

    show edelweiss neutral

    e "Well, it’s not just that! I want to be a great diviner for my own sake!"

    show lucifrid guardedrelaxed neutral

    l "Does it afford you power and status in human society?"
    e "Hmm... Not exactly."
    e "Most people don’t even know about apparitions so it’s not like there’s anything to brag about. But it’s in my family’s blood, it’s our honorable duty."

    show edelweiss determined

    e "My mother was one of the most powerful diviners to ever live, I have to live up to her name!"
    "Lucifrid looks pensively into the distance—one of the first times he hasn’t had a quip at the ready."

    show lucifrid neutral guardedopen

    l "I think duty is something you have to give shape for yourself."
    l "No one can know what anyone else is thinking or feeling. Your mother and the whole lineage of your family, who knows what they were doing anything for? It’s just your projection, right?"
    show lucifrid displeased guardedhips
    l "The only thing you can trust is your own gut, and the only one who needs to be pleased with your actions is yourself." 
    l "It’s a fool’s errand to try and live up to the expectations of forces outside your understanding."
    l "If someone doesn’t like what you’re doing, you just have to become strong enough that they can’t begin to object."
    show lucifrid grin  
    "His tone is uncharacteristically serious, but before I can comment on it he switches back to his usual demeanour, making a big show out of grasping his ice cream wrapper and crushing it in his hand like an insect."
    
    menu:
        "How should I respond to this?"


        "Jokingly.# If I did follow his advice there’s no way I’d be his obedient little assistant anymore.":
            $ lucy_yan += 1
            e smile "Yes, I think I’ll do just that!"
            e smug "I’ll grow my powers in secret until the day I can overthrow you and be free of our contract once and for all."

            show lucifrid invitingrelaxed evilsmile
            l "You’re stuck in my web, my dear assistant. There’s no way out of it unless I wish it so."
            show lucifrid guardedrelaxed
            l "And the more you resist...   the more you get stuck."
            show lucifrid ominous
            l "Don’t even dream of challenging me at my own game."
            "He laughs, and I shiver. I keep getting too comfortable around him. No matter how affable he may act, he’s not my friend."
            jump postchoice_lucycourtyard


        "Decisively.# There’s no point in a life lived only for oneself.": 
            $ negative_arc += 1
            e "It’s easy to say all that when you’re an apparition with no concept of family or kin."
            e "If I do as you say, I’ll end up like you! Alone, with my only company someone who wouldn’t be there if I hadn’t twisted their arm into it."
            show lucifrid guardedhips evilsmile
            l "Ah yes, truly the worst of all fates. I’ll have you know I’m quite happy with my life."
            e conflicted "Well, I’m happy for you, but I wouldn’t be! I need other people."
            e rueful "And if I have to sacrifice some of my personal desires to keep them around, then that’s more than worth it to me."
            show lucifrid grin
            l "Alright! As long as you’re sacrificing your personal desires for {i}me{/i} I won’t complain, ehehe."
            jump postchoice_lucycourtyard 


        "Questioningly.# What if I don’t even know what I want?":
            $ positive_arc += 1
            e awkward "If I’m going to do what {i}I{/i} want, then I at least have to know what that is..."
            show lucifrid thinkinghips worry
            "Lucifrid looks at me incredulously. Like it’s the first time he’s even considered the possibility of someone without a strong desire of their own."
            "His confused face transforms into a grin, until he bursts into earnest laughter."
            show lucifrid guardedhips grin
            l "Ahahahaha!" 
            e angry "Wow, hey, I can take abuse, but no laughing at me! You’re horrible!"
            l "Haha...ha... it’s your fault for saying something so absurd."
            show lucifrid evilsmile
            l "Well, you were right, there are some things you can still teach me. Humans truly are mystifying."
            "I frown at him. He doesn’t have to be so rude... but maybe he has a point."
            e neutral "I’ll let you know once I’ve found it. That something I want."
            l "Who knows, if you’re a good little assistant, I might even help you achieve it."
            jump postchoice_lucycourtyard



label postchoice_lucycourtyard:

    hide lucifrid
    "Dusk begins to set in, and without my noticing, the school grounds have grown deserted."
    "Lucifrid gets up, stretches his arms and yawns. Eating ice cream is a tiring affair."

    show edelweiss smile

    e "My liege, might I have your permission to head home for the day?"

    show lucifrid

    "He gives a curt nod, befitting a noble of his station."

    show lucifrid invitinghips

    l "For today you are dismissed."
    "I salute him and give a bow."
    "We slip in and out of our little roles with aplomb. Everything is a game, but I am worried for the day when it will no longer be."


    scene black
    with MVNStainedGlass10


    "As I walk home, the topic of our discussion lingers in my mind."
    "The idea of what I want... has always been blurry to me. To begin with, the person I am is the addition of what everyone else thinks or hopes or expects of me."
    "Isn't that how everyone is?"
    "We start with something, but then we're reflected in the mirrors of other people's eyes, and we model ourselves on that reflection. Either by rebelling, or conforming, or whatever else."
    "It's an eternal recursion of interpretation and reinterpretation. Who can distinguish what the original was?"
    "The first people we look to are our family. For as long as I can remember, I've looked up to mother."
    "Everyone loved her, trusted her, believed in her. And so did I."
    "If I could be like her, then my father wouldn't need to worry anymore. I know he misses her."
    "I could protect my brother, if I were just a little more reliable."
    "All the same, I know I can't be her. But why won't anyone let me try? Why doesn't father trust me with any responsibility?"
    "All I want to do is prove myself; prove that I am worthy of that same love and trust and belief."
    "Maybe I can show them. If I can handle Lucifrid, they'll have to see that I'm competent. Something good will come of this situation, it simply has to."
    
    scene classroom day
    with MVNStainedGlass10
    "As much as I’m starting to get used to chasing apparitions and appeasing spider princes, the supernatural unfortunately doesn’t excuse me from exams."

    show edelweiss unamused

    e "Haaaa... finally. Today’s lecture felt like it would never end. Can you believe they’d cover the exact same stuff father keeps drilling me on?"

    show emrys casual small_smile

    em "Think of it this way, at least it’s less work studying for this semester’s history test."

    show edelweiss neutral

    e "You’re right, you’re right."

    show edelweiss smile

    e "Onto more important topics! What’s for lunch today?"

    show emrys big_smile

    em "Thought you’d never ask!"
    "Emrys leans down to rummage through his bag, digging out two lunchboxes and placing them on his desk."
    "I waste no time in unwrapping mine as he outlines today’s menu."

    show emrys small_smile

    em "Today we serve saffron fried rice with lamb skewers, spiced with cumin and accompanied by a yogurt and mint sauce."
    em "I perfected the recipe over the weekend. I believe it has potential to become a mainstay."
    e "That sounds delicious. Thank you, Emrys! What would I do without you?"

    show emrys neutral

    em "Yes, an appropriate concern. In order to survive my absence, you could start by observing me in the kitchen. You'll know what to do to avoid overcooking a dish, or overseasoning it."

    show emrys small_smile

    em "Maybe you could even learn the age old art known as following the recipe."

    show edelweiss pout

    e "Rhetorical question! Rhetorical question!"
    "I dig in and a delectable smell travels through the classroom, drawing some of our classmates over to our desks."
    "And regrettably... it seems they’re not the only ones."

    #show Lucifrid smirk
    show lucifrid smug threateningrelaxed

    l "What a luxurious lunch for a regular Tuesday! Can you spare me a bite?"
    "I glare at Lucifrid with daggers in my eyes. He knows I can’t respond to him with everyone here."
    "Noticing my expression, Emrys chimes in."

    show emrys confused

    em "Is the food okay? You know I’m always open to constructive criticism."

    show edelweiss awkward

    e "Oh, um, no, don’t worry, haha! It’s lovely."

    show lucifrid threateninghips smug at halfcloseupl 

    l "I’m sorry, am I distracting you?"
    "He inches his face close to mine, evidently trying to get a rise out of me."
    "I try my best to ignore him and enjoy my meal, but just at that moment a brigade of upperclassmen drops by the classroom."

    hide emrys
    hide lucifrid

    "President" "So sorry to interrupt your lunch! I think most of you have seen me around but just in case, I’m Rosiel, your student council president!"
    "President" "As you all know, the cultural festival is coming up again and we’d like to have representatives from each class to help with general affairs rather than their class’ own exhibit."

    show lucifrid thinkinghips evilsmile
    l "Don’t you volunteer now, Edie. I know how much of a good samaritan you are, but I can’t have you slacking off from your duties."
    e pout "{size=-8}I wouldn’t have volunteered anyway!{/size}" 
    "I hiss under my breath and kick his shin. With everyone’s eyes focussed on the announcement, it should slip under the radar."
    #ilya sprite eyes edelweiss 
    "Well, it should have..."
    show lucifrid pout
    l "Ow! You never know how to appreciate my well-meant advice.{nw=1}"
    show lucifrid threateninghips smug at halfcloseup
    extend " As compensation I shall take one lamb skewer."
    e determined "{size=-8}No. You. Won’t.{/size}" 
    "I grip onto my last skewer like it’s a piece of driftwood in a seastorm but Lucifrid doesn’t relent."
    "My lunchbox slides dangerously close to the edge of the desk and I make a sudden leap to prevent the impending disaster."
    #sfx slide/clatter/something
    #sfx footsteps
    "A tall upperclassman sidles up beside me and places a hand on my shoulder."
    show lucifrid:
        zoom 1.0
        yalign 1.0  
    show ilya calm
    i "Is everything alright?"
    show lucifrid grin
    l "Ehehe!"
    hide lucifrid with dissolve
    "That’s Lucifrid’s cue to slip away. From the corner of my eye I see him stuff the skewer in his mouth. Curses."
    "I eye the upperclassman properly for the first time and force a smile."
    e smile "All clear! Sorry for disturbing the speech."
    "His expression doesn’t change." 
    "Did he just... look where Lucifrid was? There's no way, right?"
    "No, I must have been imagining it."
    hide ilya
    "The student council president continues her recruitment speech and eventually finds two willing subjects."
    "Already that time of the year, huh? I guess we’ll be deciding our class exhibit soon."
    "I’m busy enough with my current {i}extracurriculars{/i} that I’m not exactly looking forward to adding cultural festival preparation into the mix, but perhaps we’ll do something fun."
    "Putting on a play, a concert with a band, a maid cafe..."
    "For some reason all that comes to mind is Lucifrid stepping in to cause trouble. Maybe if we did a haunted house he could cooperate..."
    "Yeah, as if."
    "The student council members walk out as Rosiel finishes her talk, our classroom erupting into excited discussion."
    "The same upperclassman from before pauses at my table on his way out."

    show ilya polite calm

    i "I’m Ilya. What’s your name?"
    e "I’m Edelweiss. It’s nice to meet you."
    
    show ilya gentle

    i "Could we speak after class? I’ll be waiting outside the student council room."
    "His tone is matter-of-fact but his expression is gentle as his eyes fix on me quite intently."
    "It’s making me blush."
    "What could he want from me? I guess there’s only one way to find out."

    e awkward slightblush "A-alright. I’ll be there."
    
    hide ilya
    pause 1.5
    show emrys neutral

    em "Hmm...  Any idea what he wants from you?"
    "I give Emrys a blank look and shrug."
    e neutral none "Your guess is as good as mine."

    hide emrys

    "Classmate" "I can't believe it! Ilya noticed you! What did you do to catch his eye?!"
    e awkward "Should I know who he is? I don’t think I did anything."
    "Other Classmate" "He’s the student council vice-president and top of his year in academics! 
    Other Classmate" "He’s always polite but it’s rumoured he’s not close to anyone. He’s so mysterious and dreamy..."
    "Classmate" "You have to tell us what you talked about after!"
    e smug "Hehe, I’ll see what I can do. If you want details on him you’ll have to find some way to repay me..."
    "Discouraged, the two classmates slink away to pack up their lunches. Emrys leans in closer to me."

    show emrys alert neutral

    em "Do you want me to go with you? You never know how it’ll end up. It’s easy to get pressured into things."
    e smile "Oh, don’t worry so much! He’s a student council member, they’re all about proper conduct."
    e smug "Unless you don’t like me being alone with another guy?"
    "I tease Emrys to get him to back off. It’s a failsafe strategy."
    
    show emrys casual

    em "It’s my duty to look after you, Edelweiss. It has nothing to do with my personal feelings."
    
    show emrys small_smile

    em "Besides, what happened to that boyfriend of yours?"
    "Oh, right. {i}That{/i}."
    "Emrys laughs softly."

    show emrys alert

    em "That’s what’s really going on here, isn’t it? Don’t worry, I’ll keep your secret."
    
    show emrys confused
    
    em "Wouldn’t want the whole school on your case."
    "{cps=3}...{/cps}That is not the conclusion I thought he would draw."
    "I look away. My mind races to come up with the right response. Should I accept the excuse Emrys so graciously invented?"
    "Well, there’s nothing more believable than a lie you let someone else come up with."
    e determined slightblush "Don’t say it out loud! It’ll cause all sorts of problems if people find out!"
    e rueful "I guess I can never keep a secret from you."
    e conflicted "Please don’t tell anyone..."
    "If my lie is exposed, I don’t know if Ilya or his admirers will sooner have my head. Let’s hope I never find out the answer."
    
    show emrys casual small_smile
    
    em "All safe with me. So long as he makes you happy."
    e rueful none "Thanks, Emrys. I’ll be off then."
    
    scene black
    with fade

    scene hallway day
    with MVNStainedGlass10

    #ilya intro CG 

    "As I approach, Ilya stands by the student council room still as a statue."
    "The setting sun fragments his silhouette into a myriad of glowing colours and I start to understand what had my classmates so enraptured."
    "He looks like a renaissance painting."
    "I guess I wouldn’t mind if he really was my boyfriend."
    "I start to imagine us walking home from school, hand in hand."
    "When he notices me, he nods his head politely."
    i "Edelweiss, I’m glad you came."
    "I nod at him in turn, blushing involuntarily. Alright, that’s enough. Stop daydreaming."
    i "Why don’t you come inside? We’re the only ones here this afternoon."
    
    scene student council placeholder
    with MVNStainedGlass10

    #sfx door locking
    "A steaming cup of tea warms my hands as I sit at the table across from Ilya."
    "It’s my first time in the student council room, and my eyes wander around to various decorations and accolades crowding the shelves."
    show ilya stiff calm
    i "Ahem."
    "Ilya clears his throat to draw my attention back to him."
    i "You must be wondering why I called you here. Allow me to get straight to the point."
    i "As a member of the student council I concern myself with the well-being of the whole student body."
    i "Have you noticed strange happenings around yourself lately? Has anything been bothering you?"
    "He’s being vague on purpose. Is he testing me?" 
    "Don’t panic, there’s no way he could know about the apparitions. He just saw you acting strange in class."
    e awkward "N-no! Nothing strange going on with me!"
    show ilya determined
    "Ilya narrows his eyes."
    "Wait, I know what this could be about. The 4th floor... We’re not supposed to go there."
    "If he discovers the hideout, I'll be in a world of trouble. I guess it’s time for confusion tactics."
    e "Have you? Noticed anything strange?" 
    show ilya sigh
    i "Yes... I’m afraid something might be afoot in this school. And I’m afraid it might have something to do with you."
    i "I know you may be in a precarious situation, but please don’t be alarmed. I am on your side."
    show ilya polite gentle
    i "You can trust me."
    "When he looks straight into my eyes with that gentle expression, I can’t help but grow flustered."
    e conflicted deepblush "I- um, I’m sorry but I don’t really know what you mean."
    "This is starting to sound less and less like someone who doesn’t want me rummaging around abandoned classrooms."
    "Can he... really sense apparitions somehow?"
    "But even if he could, how could he help me? This situation is my own responsibility to solve. There’s nothing to learn from letting others clean up my messes."
    show ilya stiff determined
    i "Alright. You leave me no choice but to change my approach."
    "Ilya places a bracelet made of bells on the table. Each bell is engraved with symbols and as I look closer I realise that I recognise most of them."
    "I suppose the look on my face reveals enough. Only someone who knows about the world beyond the boundary would have this on them."
    show ilya calm
    i "You must recognise these, no? After class today I looked into your family."
    show ilya polite
    i "Your family and mine were allies once, before our methods diverged too much to allow such cooperation."
    i "You are diviners, we are exorcists."
    i "But we both bear strong blood ties to the beyond."
    e neutral none "This bracelet is exquisite... I’ve seen similar relics in our family’s vault, but father would never let me walk around with those. Not while I’m still in training."
    e smile "Does that mean you’re a full-fledged exorcist?"
    i gentle "As the appointed heir to our estate I have been trained from a young age to carry out my duties as an exorcist, yes. Though I still have much to learn."
    e laugh "I can’t believe no one told me there were others like us! Surely we aren’t so different."
    i stiff sigh "Our parents have their reasons, I’m sure. There have been... disagreements in the past.{nw=1.5}"
    show ilya gentle
    extend " But there is no reason for us to carry on their feud."
    i "We share a duty to protect the human realm from the beyond, wouldn’t you agree?"
    show ilya calm
    i "But we can’t do that without first keeping ourselves safe."
    "He pauses and my initial excitement chills down to a freezing temperature."
    show ilya polite sigh
    i "You’ve been beset by one of {i}them{/i}, haven’t you?"
    "A sinking feeling settles in my stomach, and I don’t know how to respond."
    "If this is a game, then I have no cards in hand and the board is firmly under his control."
    "But if he is my ally, why do I feel so threatened?"
    "I need more time to think through my moves. Why is Emrys always right?! Though what good would it do if he were here..."
    "I haven’t even decided what to do about Lucifrid yet, so I can’t involve anyone else. Let alone a complete stranger." 
    "Ilya may be an exorcist, but who knows if he can best the prince of spiders? And if he can’t, I’m the one who will take the fall."
    e determined "I have done nothing outside my own volition. You don’t need to concern yourself with me."
    show ilya pity
    "His eyes turn to pity now. Oh, that look pisses me off."
    i "I cannot allow an apparition of his calibre to exert influence over the light side of the barrier. You understand that, don’t you?"
    i stiff cold "That thing needs to be eliminated. For your good as well."
    i cold_smile "In fact, perhaps I should have started off by thanking you. For bringing this existence to my attention. It has lowered its guard around you, it appears."
    
    menu:
        "How do I feel about all of this?"


        "This is my business, and I have the situation under control.#I’ll determine if Lucifrid poses a threat, and when he does I will be the one to deal with him.":
            $ positive_arc += 1
            $ ilya_respect += 1
            "Eliminate Lucifrid? If anyone’s doing that it’ll be me. And it would be a last resort."
            "I’m a diviner, we protect the balance across the boundary. It would be a gross overstepping of our duties to eliminate without searching for a more peaceful resolution."
            "We’re supposed to help breed understanding, not hatred!"
            "I have a feeling he’s not going to be convinced of my point anytime soon though. I’ll have a better chance convincing him to back off by using his own terms. Force against force."
            e smile "I should thank you too, for opening up to me and letting me know I’m not as alone as I assumed in this school!"
            show ilya calm
            e determined "However, I think you should know better than to meddle in diviner affairs. I may still be in training, but that doesn’t mean I can’t handle my own."
            e neutral "The spider boy is under my control, and I will deal with him as is necessary."
            e "He hasn’t posed a threat to the students, and as long as he’s willing to help keep other apparitions in check I’d say antagonising him would only be going against our own objectives."
            e smile "So thank you, but no thank you. If the situation changes, I’ll keep your offer in mind."
            "Checkmate, Ilya."
            "Did I embroider the truth a little to strengthen my point? Sure. Did I embroider it a lot? Okay, maybe. But there’s nothing you can say now that won’t make you seem reckless and hasty."
            show ilya annoyed_smile
            i "I see. Perhaps I have underestimated you indeed. But I assure you it was with the best of intentions that I approached you."
            show ilya polite gentle
            i "I would hate to see you in trouble. If anything concerns you, please don’t hesitate to confide in me."
            jump postchoice_ilyameeting


        "I appreciate Ilya’s concern.#Perhaps it wouldn’t be a bad idea to open up to him, but to exorcise Lucifrid? That’s going too far.":
            $ ilya_affection += 1
            "Ilya means me no harm, he’s acting out of concern for me even if we may not agree on our methods."
            "Diviners are meant to facilitate peaceful coexistence with the beyond, making sure that the two sides of the barrier stay in harmony, balanced like two sides of a scale."
            "Exorcists are guardians of the human realm, and will do what they must even at the detriment of apparitions."
            "Isn’t there some way for us to see eye to eye?"
            e conflicted "Ilya... Thank you for telling me all this. I never knew there were others I could confide in about the dark side of this school."
            show ilya calm
            e rueful "Truthfully, I’m still learning every day about the apparitions and their ways, but I want to respect the legacy of my mother and her belief in our peaceful coexistence."
            e neutral "I can’t condone exorcising Lucifrid, even if he may interfere with my life. {nw=1}"
            show edelweiss awkward
            extend "Being annoying isn’t a sin!"
            e smile "I have faith that I can convince him to leave the student body in peace, so won’t you give me some time?"
            show ilya cold
            i "So he calls himself Lucifrid..."
            show ilya polite determined
            i "You can’t let your guard down around these creatures, Edelweiss. They’re not like us, no matter how similar their forms may appear. You can’t expect them to act with reason or empathy."
            show ilya gentle
            i "But I am not your enemy. I will watch over you from a distance then, but know that I won’t hesitate to act if he proves to be a threat to you or any other student."
            jump postchoice_ilyameeting


        "Actually... working alongside Lucifrid has been great.#I’m not going to let Ilya interfere now that I've finally found purpose in something.":
            $ negative_arc += 1
            $ ilya_affection -= 1
            "I wouldn’t let Lucifrid know but... in a way, he’s finally made me feel useful. He's given me what my father refused me: a chance to prove myself."
            "There’s a task that only I can fulfill by his side, and if anyone is going to take that away, it’s going to be me."
            "Ilya doesn’t know anything about our contract, he doesn’t know anything about Lucifrid, and he doesn’t know anything about me."
            "How could he claim to be on my side? He’s only fulfilling his own goals and trying to manipulate me into doing his bidding."
            "Well, is Lucifrid any different? Maybe not."
            "But at least I know that devil."
            "Lucifrid’s never been ambiguous about his questionable goals, he’s easier to trust than someone who claims to be \"helping\" me with a chillingly cold smile on their face."
            #edelweiss frown
            e angry "Aren’t you misunderstanding something? The spider prince and I are allies. Why on earth would I agree to let you exorcise him?"
            e "Diviners and exorcists clearly operate differently, and you will not force your crude methods upon me."
            e determined "I don’t care to make an enemy of you, but if you lay a hand on my partner, I will be forced to act."
            show ilya stiff annoyed_smile
            "Ilya’s carefully controlled demeanour cracks as I veritably {i}hear{/i} him grit his teeth."
            i "You’ve clearly wasted no time in choosing the company you keep. Perhaps a measure of discernment would have served you better."
            i "I have your best interests at heart, please remember that. I have years of experience dealing with the beyond, perhaps my knowledge might serve you one day."
            show ilya gentle
            i "But rest assured, I have no interest in making enemies today either. This was merely my first warning."
            e smile "Consider your warning received. I hope mine was as well."
            jump postchoice_ilyameeting


label postchoice_ilyameeting:


    "Ilya and I shake hands. I can’t tell if we are allies or enemies, it seems we may be both."
    e neutral slightblush "I should probably let you know—I told Emrys we're dating."
    
    show ilya annoyed_smile
    with Dissolve(1.0)
    show ilya gentle

    "Did Ilya twitch a little just then?"
    i stiff calm "Emrys?"
    e neutral none "...My assistant. I can't let him find out about the spider apparition."
    i "Have you told anyone else about this?"
    e "No. Just him. He was more than happy to assume we don't want your admirers on my case."
    i sigh "I—"
    "He sighs, though he tries to make even this movement swift and dignified. His discomfort is palpable in the air."
    i calm "If we’ll be seeing more of each other soon, then I suppose this is a fine cover story."
    i "I’ll play along with your ruse. You’re free to tell who you like, though it may do more harm than good."
    i polite sigh "I’ll trust your judgment on the matter. I can’t claim to be an expert on... girl politics."
    "I think of the girls in class and the way they stared at my back as I left the classroom. Yeah, this might require a delicate approach."
    e smile "Alright then. I'll see you later... {i}boyfriend.{/i}"
    show ilya stiff calm
    "He raises an eyebrow at me, but doesn’t respond further. Hrm... he isn’t even fun to tease."
    "In any case, I need to keep an eye on him. And I should inform Lucifrid, he should be on his guard too."
    "Ilya doesn’t know of our contract. If he harms Lucifrid, he may inadvertently harm me as well."
    "I’ll keep that little fact up my sleeve, who knows when I will need a bargaining chip—or an element of surprise."

    scene black
    with fade

    "I push past other students on their way to after school activities in a rush to reach the fourth floor."

    scene hideout placeholder
    with MVNStainedGlass10
    #sliding door sfx
    #Lucifrid is lounging
    e determined "Lucifrid! I have... something to... report!"

    show lucifrid thinkingrelaxed neutral
    l "My, my! What’s got my darling assistant all out of breath?"
    l thinkingopen evilsmile "Calm down, take a seat."
    "I sit down on one of the desks, dangling my legs, and Yang patters over to me."
    e smile "Hey little friend."
    "I hold out my arm and he climbs up to my shoulder."
    show lucifrid threateninghips at halfcloseup
    l "Now don’t keep me waiting after you’ve piqued my interest."
    e smug "Getting jealous of your own familiars now?"
    show lucifrid threateningclenched displeased at halfcloseup
    l "Out with it!"
    e neutral "That guy from the student council this morning... He saw you."
    show lucifrid thinkinghips neutral at halfcloseup
    l "Ah, I did sense some manner of spiritual power coming from him. So that’s what it was."
    e determined "It’s not just that. He’s an exorcist. Said he wanted to eliminate you and tried to present it like he was doing me a favour."
    "I sense the air around Lucifrid growing still and dark as I continue, though I can’t yet tell if it is me or the situation that he’s vexed with."
    show lucifrid guardedhips ominous at halfcloseup
    l "Oh, he thinks he can toy with my property? Win over my assistant with sweet words?"
    "Something tells me the fake boyfriend thing is {i}not{/i} going to go over well. Best keep my story vague."
    e neutral "Don’t worry, I got him to back off for now. But he’s definitely keeping an eye out for you, we need to be careful."
    show lucifrid neutral at closeup
    "Lucifrid wordlessly clasps two arms around my neck and leans his forehead against mine."
    "He doesn’t look angry, but he’s got none of his usual joking energy either."
    l "Don’t forget, our souls are linked."
    show lucifrid evilsmile at closeup
    l "Whether you’d like to or not, you can’t leave my grasp. Even when I’m not holding on."
    e conflicted "Wow, hey, calm down. I just said I got him to back off. I defended your honour, spider prince."
    "He lets go of me swiftly."
    show lucifrid guardedhips grin
    l "Hehe, just making sure you know!"
    l "Let’s build an even stronger front against all those who oppose us!"
    "He turns around and strikes a menacing pose."
    show lucifrid threateninghips grin
    l "We will be the undisputed rulers of this land, either side of the barrier! And there will be no one to stop us, certainly no measly human exorcist."
    "I laugh along with him—it’s not so bad having big dreams to chase."
    hide lucifrid
    with Dissolve(0.7)
    "I wonder why the idea of becoming a great diviner never felt like this. It’s a noble dream in its own right. Perhaps not quite as catchy as ruling the school, but still."
    "Somehow it’s not fun or light, but heavy and solemn."
    "I want to chase a dream that’s waving in the wind. One that, if I don’t start running now, I won’t have a chance of catching up to. Who knows where it will lead?"
    "It’s nothing like a path set out by my ancestors, trodden by my forebears, in the shade of their looming figures."
    "If Mother were here, I would ask her how she felt about it all."
    "{i}Hey Mother, did it come as naturally as they all make it sound?{/i}"
    "{i}Hey Mother, did you ever doubt yourself?{/i}"
    "Maybe she would've said something to make my path more clear."
    "Or maybe just given me another reason for doubt."
    "But in her absence, I return to the present."
    show lucifrid threateninghips grin
    with Dissolve(0.7)
    e determined "Yes, my liege. Who is the next usurper we shall defeat?"
    l guardedhips evilsmile "I have located one of the greater threats to our rule, they dwell on the dark side of the gymnasium."
    e "Leave it to me, I shall speak the binding words."
    "And so we head off, made invincible in spirit by our continuous successes, the threat of the exorcist but a footnote in our minds."

    scene black
    with fade

    scene classroom day
    with MVNStainedGlass10

    "The next couple of days are peaceful. I continue my hunts with Lucifrid after school, and keep my head down in class."
    "I can't let my grades slip too much and risk getting put into supplementary lessons, or worse—roped into helping organise the festival."
    "I don't want a reputation for being a delinquent either, with all the sneaking around on school grounds after hours."
    "Classmate" "Edelweiss! How did the rice dumplings turn out?"
    e neutral "Oh... yeah."
    "I lift the lid of the small container, revealing the food I made in home economics—three skewers glazed in glossy sauce."
    "They didn't turn out half bad, if I do say so myself. Maybe there’s something to that whole ‘following the recipe’ idea Emrys suggested."
    "Classmate" "Ugh, lucky."
    "Classmate" "Mine completely fell apart. I think I stirred the sauce too much."
    "Other Classmate" "At least you didn't burn yours."
    "Other Classmate" "I wanted to give mine to my boyfriend, but now it looks like charcoal on a stick..."
    "Classmate" "Didn't you break up with your boyfriend?"
    "She lets out a dramatic sigh, resting her chin in her hands."
    "Other Classmate" "We're still together... sorta. It's complicated."
    "Oh, to have regular high school girl problems."
    "Other Classmate" "Don't judge me. It's not like you have someone to give your rice dumplings to."
    "Classmate" "Wow, uncalled for. I'm giving mine to Ilya."
    "Other Classmate" "Oho, bold choice. All the competition doesn’t scare you off?"
    "Classmate" "H-hey, it's not like that! He just helped me out once... I wanted to pay him back!"
    "A few amused laughs ripple through the group."
    "Classmate" "Anyway! Uh— Edelweiss! Who are you giving yours to?"
    "I blink. Me?"
    "Other Classmate" "Emrys, right? You're always together."
    "Other Classmate" "Wait, I know!"
    "Her eyes narrow."
    "Other Classmate" "Didn't you go see Ilya alone the other day?"
    "She lets out a sly giggle. News sure does travel fast in this school, huh?"
    e awkward slightblush "H-hey, it's not like—"
    "Classmate" "You saw Ilya alone?"
    "Is this the moment to publicise our ruse? Ilya did say it was up to my judgment."
    "I see her face fall, and falter. I don’t have the heart to crush her dreams."
    e awkward none "I... was just going to have them myself."
    "The two girls eye me, suspicious."
    "Other Classmate" "If you say so."
    "Here’s what they don't tell you about lying. You tell one lie, and it starts asking for friends.  And the more they pile up, the harder it is to keep your story straight."
    "The one with a boyfriend winks at me as they walk away."
    "But the question remains... who {i}should{/i} I give these to?"


    menu:
        "Who should I give the rice dumplings to?"

        "Ilya.#":
            "I suppose I best keep up with my own lies and reinforce the boyfriend narrative. Everyone in class suspects me of something anyway..."
            "And Lucifrid already stole my lunch the other day, I shouldn’t reward him for it."
            "Besides, I can’t help but feel I owe Ilya for accepting the boyfriend ploy so gracefully."
            scene hallway day
            with MVNStainedGlass10
            "I knock three times, then let myself in."

            scene student council placeholder
            with MVNStainedGlass10
            show ilya stiff calm

            i "Oh, Edelweiss."
            "Ilya looks up from a small stack of papers, pen paused mid-air."
            i "I wasn't expecting anyone."
            e smile "Hope I'm not interrupting."
            show ilya gentle
            "His stiff posture relaxes slightly. He smiles as though he recently remembered how to do it and his face isn’t used to the expression yet."
            i "Not at all. What can I help you with?"
            "I close the door behind me and walk over to his desk."
            e neutral "I brought this for you. From home economics."
            show ilya calm
            "I hold the container up a little awkwardly, and he cocks his head, slightly puzzled. Is he waiting for me to say something?"
            e smile "I can’t eat them all by myself!"
            show ilya polite
            "He gestures to the seat across from him without saying a word and I sit down, carefully placing the container between us."
            "He opens it, staying silent while examining the skewers. I feel like I’m being graded."
            "After what feels like ages, he takes a small, thoughtful bite."
            i "..."
            show ilya stiff gentle
            i "Adequate."
            "I stare at him. That's it?"
            e unamused "{i}Adequate?{/i} That’s all you’ve got after your in-depth analysis?"
            i calm "The consistency is passable. The sauce is slightly over-reduced."
            e pout "Alright, my bad, hand it over. I’ll give it to someone who can actually appreciate it."
            "But he doesn’t obey. Instead he takes another bite."
            i polite "Hm? I thought you wanted my feedback."
            i "I do appreciate it, I was just getting hungry." 
            i gentle "You’re saving me time and resources, that’s much more important than the fleeting enjoyment of flavour."
            "Is this... his way of complimenting me? I can’t say I feel especially flattered."
            "I wonder if this is what all those girls imagine their princely vice-president to be like in private."
            "Ilya sets the skewer down and folds his hands neatly in front of him."
            i stiff sigh "You’re taking this fake relationship quite seriously, aren’t you?"
            i calm "We’re not actually dating, lest you forget."
            "I frown at him."
            e determined "How could I forget? I’d hope my actual boyfriend would be a bit more affectionate."
            e smile "But still, I owe you. For going along with the whole thing. So here’s my thanks."
            i determined "That wasn’t... for you. It was simply the best way to resolve the situation. It doesn’t warrant thanks."
            e laugh "Oh, is that so? I usually choose the worst way to resolve situations, personally."
            "I wait for him to laugh, or at least crack a smile—a real one, not that rehearsed mask he puts on— but the moment never comes."
            "I just can’t figure him out." 
            "After a pause, I pipe up."
            e neutral "Do you even like anyone at this school?"
            i calm "I respect a few people."
            e unamused "That's not what I asked."
            "He picks up the second skewer, more slowly this time."
            i polite "People expect things of me. As the student council vice-president. As the heir to my family's estate. It leaves little room for closeness."
            e rueful "...You're really bleak."
            "He lets out the faintest ghost of a smile."
            i stiff cold_smile"Am I?"
            i calm "If I am, it’s only because I was taught by experience."
            "I don't respond."
            "Instead, I rest my chin in my hand and watch him finish the second skewer."
            "The student council room is full of awards and certificates—proof of excellence."
            "Just how long has Ilya been living as this careful, precise vice-president, always slightly at arm's length?"
            e smile "If I bring you more next time, are you going to insult my cooking again?"
            i gentle "Not if it improves."
            e smug "Heh, is that a challenge?"
            show ilya calm
            "He glances out the window, light casting across his profile."
            e smile "Well, the offer for friendship is on the table, if you want it."
            i polite "Are we not dating? The friendship is implied." 
            e smug "We’re not actually dating, lest you forget."
            show ilya calm_smile
            "Finally, the smile I was waiting for comes out, like sunshine after a long night."
            "I didn't even know Ilya's face could do that. He looks beautiful."
            show ilya stiff sigh
            "But as suddenly as it appeared, it fades again. He guards nothing as closely as his own emotions, it seems."
            i polite "I care about you, Edelweiss, but... I don’t know how to be your friend."
            i  "Still, you’re free to stay despite that."
            "And just as I thought I had cracked his armour. But it’s too early to give up."
            e rueful "I suppose we’ll start with {i}respects me slightly more than most.{/i}"
            i gentle "...That's within reach."


        "Lucifrid.#":
            "I think of how Lucifrid can't leave the school grounds."
            "Has he ever had rice dumplings before? There’s probably tons of food he’s never tried."
            "I guess I could wait until our usual after-school rendezvous, but rice dumplings are best eaten fresh."
            "Before I can overthink it, I head towards the hideout."

            scene hallway day
            with MVNStainedGlass10

            scene hideout placeholder
            with MVNStainedGlass10

            "Lucifrid is lounging atop his so-called throne."
            "He grins when I enter, folding two of his arms behind his head, while the other two cradle a particularly smug-looking spider."
            
            show lucifrid invitingrelaxed grin

            l "You're early. Skipping class?"
            e smile "It's lunchtime. I brought you something."
            "I pull out the container from my bag and hold it up."
            e "I made these skewers in home economics."
            l guardedrelaxed smug "Ah. A nuptial gift."
            e awkward "A {i}what?{/i}"
            l thinkingopen neutral "A male spider may court a female by offering prey wrapped in silk. While the female is distracted by the gift, the male inserts his-"
            e unamused slightblush "I know what that is! I've done biology class.{nw=1}"
            show edelweiss awkward
            extend "Why am I the male spider in this analogy?"
            show lucifrid innocent guardedopen
            "Lucifrid hums cheerfully as he leans forward to inspect the box of skewers, four hands braced on the desk."
            e pout "Try one before you say something else ridiculous."
            show lucifrid smug guardedrelaxed
            l "Such a demanding assistant."
            l innocent "You know, the last time I accepted a gift from a human, I nearly lost my head."
            e neutral none "Oh? I’m finally getting the spider prince’s tragic backstory?"
            show lucifrid evilsmile guardedopen
            l "Heh, and let you know all my weaknesses? Not a chance."
            show lucifrid guardedhips
            l "I’m just making sure you know this is a special exception."
            show lucifrid threateninghips neutral
            "Lucifrid plucks up a skewer, sniffing it a little."
            l "Shiny. Like lacquered beetle shells."
            e unamused "You do know how to compliment a lady’s cooking."
            "He bites."
            "For a moment, he goes still."
            show lucifrid guardedhips innocent
            l "Mm."
            show lucifrid thinkinghips
            l "Mm, mm."
            e smile "So... you like it?"
            l neutral "When did you find the time to make these?"
            e neutral "During class? That’s literally what home economics is for."
            l worry "But why not just—"
            show lucifrid guardedhips evilsmile
            "He stops himself. His usual grin sneaks back over his features."
            l "Never mind."
            l guardedopen "It’s sweeter than necessary. Sticky. Clings."
            e unamused "Well, yeah. It's a rice dumpling."
            e smile "You’re welcome by the way."
            l guardedhips neutral "I didn’t say thanks."
            e smug "I know. It was implicit."
            "He takes another bite, slower this time."
            l guardedrelaxed wrysmile "...Thank you."
            "He says it quietly, almost like he’s testing how the words feel in his mouth."
            "I don’t know what to say in response, but he soon resumes."
            l thinkingrelaxed grin "What’s your favourite food, Edelweiss?"
            e smile "Me? I was going to ask you."
            l guardedrelaxed smug "Too bad, hehe. I was first."
            "I pause to think about it for a moment."
            e "...Grilled mackerel."
            l invitingrelaxed grin "Pfft... hahaha!"
            l smug "Are you a grandfather?"
            e pout slightblush "What’s wrong with liking something traditional?!"
            show lucifrid threateningrelaxed evilsmile 
            l "I was going to have my familiars procure it for you, but stealing from grandfathers might cross a line even for me."
            e conflicted none "I don’t think stealing is good practice for gifts anyway..."
            show lucifrid guardedrelaxed 
            l "Well, it’s {i}my{/i} practice."
            e smile "Anyway! It’s your turn! What’s your favourite?"
            e "If it’s within my skills... I’ll bring it for you next time."
            "I don't know what I'm saying anymore. What would my father think if I told him I was cooking for an apparition deity?"
            "He doesn’t hesitate for a beat."
            l grin "Hamburg steak."
            e smug "...Hehe."
            "Of course the apparition making fun of my grandfatherly taste likes a staple children’s food."
            l guardedopen neutral "What’s so funny? It’s simple, warm, and unpretentious; things you humans undervalue far too often." 
            e neutral "The cafeteria has hamburg steak every now and then."
            l guardedclenched displeased "Ah yes. The overcooked, low quality loaf with a cold centre and fake cheese."
            e unamused "My bad. Forgot I was dealing with royalty."
            show lucifrid neutral
            "Lucifrid finishes the first skewer, and reaches over to take a second."
            e neutral "You have sauce on your—"
            "I lean forward without thinking."
            show lucifrid neutral at closeup
            e deepblush "—face."
            "For a second, our eyes are level with each other. The world seems to pause."
            "Lucifrid lifts one of his hands to wipe the glaze with his fingertip."
            "Then, before I can react, he swipes a smear of sauce across my cheek."
            e angry slightblush "Lucifrid!"
            l grin guardedopen "See? It suits you."
            l evilsmile guardedrelaxed "Now we both match your offering."
            "He laughs, and the spiders seem to skitter in time with the rhythm of his laughter."
            "I wipe my cheek, and after a moment’s hesitation rub my sauce-covered finger on his face in retaliation."
            "He laughs, unbothered, and something about the gleam in his eyes makes me nervous."
            e neutral none "Anyway. I need to get back before someone notices I’ve gone missing."
            l smug "Already tired of my company?"
            e pout "I'm just trying not to get detention."
            "I swing my bag over my shoulder. Lucifrid walks me to the door like a host seeing off a guest, but before I leave, he places a hand on my head."
            l invitingrelaxed innocent "Be good. And don’t go offering rice dumplings to anyone else, alright?"
            e rueful slightblush "Don't worry. There's none left."
            "I feel my face flush, but I don’t give him the satisfaction of seeing it."

    scene black
    with fade
    scene classroom day
    with MVNStainedGlass10

    em "Hey, did you hear? There’s been some worrying rumours."
    e "Thought you weren’t the gossiping type. What’s this about then?"
    em "This is different. It seems a kid from another class just stopped speaking from one day to the next, no one knows what caused it."
    e "Could it be selective mutism? Just trying to seem cool and mysterious?"
    em "Plausible explanations. If it weren’t for the fact that someone else had the exact same thing happen to her just yesterday."
    e "..."
    e "You’re thinking it could be something more otherworldly."
    "Emrys nods."
    em "Should we try to look into it after class today?"
    e "Sounds like a task for us, yes!"
    "With our after school objective in mind, the day crawls by at a snail’s pace."
    #sfx school bell
    "By the time the bell sounds I fear the clock may be burnt onto my retinas like a ghost-image on a paused VHS tape."
    "But no, the only ghosts here are the ones haunting the beyond; and perhaps now our student body."
    "I lock eyes with Emrys and we make a coordinated dash for the hallway. The two afflicted students are from different classes, so we have to split up to investigate."

    scene black
    with dissolve

    scene hallway

    "The female student is my target. She’s in class 2D, so my best bet would be asking her classmates."
    "I intercept a group of girls spilling out of classroom 2D while chatting merrily."
    e "Excuse me, you’re classmates of Marigold’s, right?"
    "Liese" "You’re wondering about the voice thing, right? I don’t know what everyone’s making such a big deal out of. She must have just done too much karaoke..."
    "Phila" "Not everyone’s like you, Liese! Have some empathy!"
    "Trish" "Have to admit it’s kind of nice and quiet like this though, hehe."
    e "I was wondering if you knew what she was up to the day before her voice went away. Did you go with her to karaoke?"
    "Trish" "She’s just joking. Mari’s usually pretty diligent—she wouldn’t be out late on a schoolday."
    "Liese" "Well, she wasn’t at volleyball practice at least!"
    "Phila" "Maybe she was studying? It was the day before that history test."
    "Liese" "Oh, please don’t remind me of that ordeal."
    "Phila" "I’m a little worried about her. Will you let us know if you find anything?"
    e "Of course, leave it to me! Thanks for telling me what you know."
    #girls leave, emrys appears
    em "So, any leads?"
    e "Well, we should see if there’s a pattern between our two victims here." 
    e "It seems Marigold skipped her extracurricular the day before her... affliction set in. Did you find out what club Oliver is in?"
    em "It appears he isn’t much of a social type; his classmates couldn’t tell me much about him and he isn’t in any clubs."
    e "Guess that’s that for the volleyball club lead."
    e "Hmm..."
    em "They did tell me he usually spends his breaks in the library on the computer."
    e "That’s it! One of her friends speculated Marigold was studying for a test instead of attending volleyball practice. Let’s check out the library!"
    #emrys proud smile
    "Emrys’ eyes glimmer and he looks like he wants to say something for a moment, but he merely nods."
    em "Let’s go."
    #bg library
    #sfx sliding door
    "The library air is heavy with dust, forcing a cough from my throat." 
    "A slight breeze blows from the window, but nothing else disturbs the stillness of the room. Two students sit deeply engrossed in schoolbooks, another at the computer with headphones so large as to be comical."
    "By all accounts, it’s an ordinary school library."
    "The silence commands us not to disturb it. With the gentlest of footfalls, Emrys and I make our way around to investigate."
    "..."
    "..."
    "..."
    e "{size=-8}I’ll be honest, I don’t think we’re getting anywhere.{/size}" 
    em "{size=-8}Should we ask one of the students here if they’ve seen anything?{/size}"
    "I tap one of the reading students on the shoulder."
    e "Sorry to disturb you. Were you here last Wednesday too? Do you happen to have seen Marigold?"
    "The underclassman knits his brows together."
    "Boy" "Yes, she was very hard to miss..."
    "Boy" "She was sighing and complaining, and that boy who’s always glued to the computer, well, I’ve never heard him say more than two words until that moment."
    "Boy" "They got into a big fight, which ended up louder than the noise he was complaining about to begin with."
    "Boy" "I left to find some actual peace and quiet so I don’t know what happened after that..."
    "Bingo! They were here together right before things went south. It has to be connected!"
    "At that moment, a cat jumps onto the table almost pontifically. The underclassman’s eyes soften as he moves to pet it."
    em "Since when does this library have a cat?"
    "Boy" "Shhh..."
    "Boy" "She hates noise."
    "He puts his finger to his mouth, while his other hand continues petting the cat now stretched out across his coursebook."
    "Wait... That’s no regular cat..."
    "While the boy is engrossed in his petting I pull on Emrys’ sleeve and he leans his ear close to me."
    e "{size=-8}...I think that’s an apparition. I sense something, and there’s no one else around.{/size}" 
    em "{size=-8}But it’s visible. {i}Touchable{/i}. Are you sure?{/size}"
    "I nod. We both know what that means: it has to be powerful."
    e "Well, thanks for helping us out! We’ll be on our way now!"
    #sfx cat hiss
    "I purposefully raise my voice and the cat bares its teeth at me."
    "Boy" "No, no, Patches, calm down!"
    "The boy shoots us a cutting glare."
    "Boy" "What did I tell you about noise?"
    "Boy" "If you’re not here to read, then be off."
    "Emrys gives me an annoyed glance as we scurry out of the library."

    scene hallway
    #sfx sliding door
    em "What exactly were you trying to do?"
    e "Upset it enough to prove it caused the incidents!"
    em "By becoming a victim yourself?!"
    e "No, of course not!"
    "Lucifrid would sense if I was in danger... he wouldn’t allow his assistant to become patently useless."
    em "So what do we do now? This seems like it’s more than the two of us can handle, but we can’t just leave things as they are."
    em "If it truly is an apparition’s doing then who else could take care of it?"
    "Well, I know someone... Two someones, if we’re being precise."
    "I sigh. I’m tired of having to deceive Emrys. We’re supposed to be allies. Best friends."
    "I’m treating him like he’s an outsider when I should be relying on him."
    "He cocks his head in a silent plea to hear my thoughts on the matter."
    e "...I have a plan. But you have to promise not to get mad at me for what I’m about to tell you."
    #fade to black
    "..."
    "I tell Emrys about Lucifrid and our contract."
    em "You did what?!" 
    e "Don’t get angry! You promised!"
    em "I’m not angry, angry does {i}not{/i} begin to describe what I’m feeling."
    "Oh no, now I’ve really done it."
    "Emrys is far scarier when he’s calmly scolding me."
    e "Look, you can at least be glad we have some way of tackling the case of the stolen voices!"
    em "Don’t think you can distract me by giving this investigation a cool name."
    "Drat, that usually works..."
    em "This is like getting out of gambling debt by borrowing money from the yakuza! Yes, he’ll take care of this problem, and then he’ll take care of {i}us{/i}."
    e "I know what it sounds like but Lucy’s not a bad guy, okay..."
    em "LUCY?! You’re giving the evil overlord of the beyond pet names now?" 
    "Oh, I guess I did..."
    #edelweiss blush
    e "I-it’s only one! One pet name!"
    "Emrys sighs deeply."
    e "Let’s just go meet with him, alright? If I keep him waiting much longer he’ll come find me anyway."
    "He grits his teeth, knowing there’s nothing he can do to change the situation."
    "His expression doesn’t soften, but he squeezes my hand briefly. It’s his way of telling me he’s still on my side."
    e "Sorry, Emrys... I should’ve told you earlier, but this whole thing was to protect you. I wanted to keep you safe."
    em "Yeah, I know."
    em "There's about a million better ways you could have gone about this, but I'm sure you've beaten yourself up over that without my help."
    em "...I appreciate the thought."

    scene classroom evening
    #sfx sliding door slam
    #bg hideout
    e "Lucifrid! Where are you?"
    em "It’s a wonder that door is still whole if you treat it this roughly all the time."
    "Spiders blink their manifold scarlet eyes in silence, patiently awaiting their master’s return."
    "Emrys isn't nearly as unsettled by them as I was at first."
    "We look around the hideout for a sign of Lucifrid, to no avail."
    "There’s no finding an apparition of his caliber if he doesn’t want to be found, so there's little to do but wait around."
    "..."
    "Growing tired of waiting, Emrys sits down on Lucifrid’s usual chair. The room darkens immediately."
    "Lucifrid spawns in an instant from a corner obscured by a crawling mass of his familiars."
    "Startled, Emrys jumps up from the chair with a flinch."
    l "Do not casually take my throne, human."
    "He says it dismissively, in a way I haven’t heard him speak to me. As if getting upset with Emrys would be impossibly far beneath him."
    em "You-"
    "Emrys starts but Lucifrid interrupts him heedlessly, fixing his eyes on me."
    l "What exactly is the meaning of this, my dear assistant?"
    "Seeing his eyes so void of emotion, I swallow nervously."
    l "I believe I agreed to keep this human out of our affairs in return for your services. You can’t extricate yourself by bringing him back here."
    "I take a deep breath and collect myself. Lucifrid’s intimidation tactics are nothing more than that: tactics."
    e "The two of us were investigating. Something is afoot in this school and it involves an apparition, so it seems our interests align."
    #Lucifrid sprite moves closer
    l "My dealings are with you. What could his presence possibly add to this equation?"
    e "You have nothing to lose from an extra ally! Especially not now you’ve drawn the eye of an exorcist!"
    "Emrys steps between the two of us."
    em "I am in the employ of the Hesgothia family, and more than that I am Edelweiss’ friend. Her diviner activities are my business all the same."
    "Lucifrid grins."
    l "I am oh-so-glad she has a friend, but your support in these matters is no longer necessary."
    #lucifrid grin
    l "Edelweiss agreed to our contract in order to protect you, so who would I be to get you into danger and invalidate the terms of that agreement?"
    l "You would do nothing but get in the way."
    "I let out a scoff."
    e "What a caring apparition you are, all of a sudden."
    em "You do not get to decide what risks I do or do not take. The only one who has any say in that is Edelweiss herself."
    "Lucifrid engages Emrys in a stare-off, and I look at the latter apologetically." 
    "I want to defend him but... Lucifrid isn’t exactly wrong." 
    "Emrys wants to keep an eye on us to protect me from Lucifrid, but what could he even {i}do{/i}? I'll just have one more thing to worry about."
    e "Why don’t you just listen in for now? You’ll see our means and methods are solid and you won’t have to worry!"
    "I motion to Yang, who has been inching closer to us for the span of our conversation."
    e "Look, this is my own spider familiar! His name is Yang and he’s very reliable."
    "Emrys cracks a smile, and Lucifrid at the very least isn’t protesting letting him stay. Small victories."
    "Lucifrid sighs, his threatening aura melting away."
    l "Well, you had business here. Tell me about this apparition then."
    e "Two students lost their voices. When we started investigating, it turned out they had an altercation in the library the day before this happened."
    e "Then we saw a cat in the library who gave off spiritual energy. I believe it must have been an apparition, taking the voices of students it considers loud and bothersome." 
    e "I have no proof it was the cat, but the fact alone that it can interfere with our realm, that the other students can see it and pet it is... worrisome."
    l "The librarian is operating on this side of the boundary now? Interesting."
    l "You want to break its spell then, I assume?"
    em "Wait, you knew about the cat and never mentioned anything?"
    #lucy angry
    l "I know of all the creatures that are active in my domain, human. Do not underestimate me."
    #lucy casual
    l "It’s no threat to me, but as magnanimous ruler of the beyond to be, I suppose this falls under my jurisdiction."
    e "See, I knew this would be a task for you! I’m helping you spread your influence!"
    l "...Under one condition."
    l "Your {i}friend{/i} ceases his meddling and concerns himself with your human activities only."
    em "I will not shirk my duties with regards to Lady Edelweiss’ protection."
    "Lady Edelweiss... He never calls me that anymore."
    "My eyes cloud with worry in the pregnant silence that follows. Lucifrid merely stares at Emrys, unfazed."
    em "...{w}but I concede that the best way to do that is sometimes to step back and hold the rear."
    em "I don’t trust you for a second. But I trust Edelweiss, and I don’t want to make her life more difficult by causing strife. Clearly she won’t be rid of you anytime soon."
    em "But I will be around. Don’t think you can do whatever you please to her just because I’m not a diviner."
    "Lucifrid snickers, making no attempt to hide his derision."
    l "Off you go then, little protector."
    e "Thanks, Emrys..."
    #emrys leaves
    "A weight I didn’t know I was carrying lifts from my shoulders now that everything is out in the open, but I don’t know if I did the right thing. The enmity between these two is palpable."
    "If only they could see they’re on the same side..."
    "Turning around, I flick my finger against Lucifrid’s forehead."
    l "Ow! What’s that for?! I’m helping you out of the goodness of my heart."
    e "You’re bullying Emrys for no reason! You know he means well!"
    l "There is a hierarchy to this world and no good comes of disobeying it."
    e "That’s {i}your{/i} world, that you’re {i}choosing{/i} to live in. Not everything is about who’s above or below who."
    l "The only reason you can say that so easily is because you’ve never been at the bottom."
    l "He’d only get hurt if he got involved, better to make it clear from the start. The beyond is no place for weakness or idealism."
    e "Even if that’s true, you don’t have to delight in knocking him down a peg!"
    l "Oh, but I always mix business with pleasure, {i}ehehe~{/i}"
    #edelweiss unamused
    e "Is that what this is then?"
    "I motion between the two of us."
    #Lucifrid cute
    l "Don’t debase yourself, my soulmate."
    "My face grows hot. I don’t know what I was hoping for with that question."
    "I can never tell what’s a game with him and what’s serious. Is everything a game? Is everything sincere? Perhaps both at the same time."
    e "Ahem."
    e "If you were aware of our library critter, shouldn’t you have subdued it already?"
    l "All in due time, all in due time. Neither threatening nor meddlesome, it wasn’t exactly at the top of my priorities."
    l "We share an unspoken alliance. Well, {i}shared{/i}, I suppose. It wouldn’t do to refuse my dutiful assistant’s earnest request."
    e "But how is it that the other students can interact with it? Has it always had this disguise?"
    l "That, I do not know. It must be a recent development." 
    l "It’s not usually a creature of antagonistic nature, so the fact it would attack humans means it’s probably not pleased with the development either." 
    e "Didn’t seem to mind the petting all that much."
    l "There’s pros and cons to everything."
    "He reaches out and pets my head in his usual fashion."
    l "See?"
    e "I’m not a pet."
    l "Alas, I’ve always wanted a pet human."
    e "Really? I thought I heard you describe humans as ‘annoying imbeciles’ before."
    #Lucifrid close up
    l "Alright, I stand corrected. I want a pet Edelweiss."
    "He grins as I stare pointedly at him. I’m not dignifying that with a response."
    "Then he takes my hands into his, and I pull back instinctively."
    e "Stop it already!"
    l "Hm? I thought we were going to defeat that cat. We’ll have to travel to the other side for that, do you forget already?"
    e "O-oh. Right."
    "I place my hands back into his gently and close my eyes."
    "The floor beneath me dissolves and my awareness slips. The only thing I can feel is the soft warmth of Lucifrid’s hands—my anchor."
    "I open my eyes a little too soon, and the disorienting sight of the world around me slotting together like puzzle pieces turns my stomach. Lucifrid steadies me when I almost fall over."
    "One day I will get used to crossing the barrier. One day."
    "We find ourselves in a hallway packed with mirrors that has become familiar to me by now. It is the nexus of Lucifrid’s domain, each mirror leading to different domains and sections of the dark side of our school."
    "Ever since we suppressed that first icy ghost, he rearranged things to make it connect directly to our hideout."
    "I pace the hallway, gazing into each mirror as I pass. They reflect potentialities; alternate futures and pasts of whoever looks into them."
    "I stop in front of a large and decorative mirror that shows me asleep in bed, hair grown so long it doesn’t fit the frame, surrounded by towers and towers of books."
    e "This must be it, right?"
    l "Excellent work, my dear assistant. This one indeed connects to the library."
    #transition
    #sfx creak
    #bg library beyond
    "The library..."
    "The layout is identical to its light side counterpart but the details are all different, like the same page in a colouring book filled in by different people."
    "Nightgown flowing, a petite girl with catlike features trots over to us, her expression stern. Her ears perk up when she spots Lucifrid."
    "Cat" "Your Dark Majesty, what brings you to my library today?"
    "She addresses him respectfully but curtly, giving both of us small nods of acknowledgement. Then her eyes linger on me in contemplation. She doesn’t get many humans in her domain, I’d wager."
    l "Librarian, I know you to be reasonable. That’s why I extend the courtesy of parley."
    "Oh, wait. This girl {i}is{/i} the library cat,  should’ve connected those dots."
    l "You’ve been meddling in the students’ affairs, haven’t you? Why get involved with the light side of the barrier?"
    "Cat" "I-"
    l "No, phrasing it as a question is unfair. I will have you return these students’ voices. The choice remaining to you is whether that will be of your own volition or by force."
    "So his idea of an alliance is when someone unequivocally submits to his will. I suppose it shouldn’t come as a surprise."
    "Cat" "With all due respect, Your Majesty, why do you take the humans’ side? Did this girl cast a spell on you?"
    "Cat" "I can only imagine you would have laughed with me over this a little while ago." 
    "Cat" "The library is mine to oversee, and ought to be a place of calm and quiet. The students knowingly broke that agreement; their punishment is deserved."
    "His casual grin falling from his face, Lucifrid backs the girl into a corner and spins a web round her feet."
    l "I don’t take lightly to your implications. Know your place, and know that your every freedom is because I allow it."
    l "Every day you draw more attention to me and my designs by playing around on the light side. Is my rule a game to you?"
    l "And that is assuming the best, who says you are not amassing forces to oppose me? Appearing in some beguiling, innocent form before the students to win them to your cause."
    "I bite my thumb, my eyes darting between the two of them."
    "This negotiation doesn’t seem to be going the way we hoped. Is there anything I can do to help?"
    #sfx cat hiss
    "The catgirl hisses in my direction."
    "Cat" "First I’ll remove this human distraction, then I can be sure you are in your right mind."
    "Her form flickers and shifts as she grows into a monstrous, many-headed feline hydra. Her beastly proportions rip her out of Lucifrid’s web with ease."
    "I think it’s safe to say the time for negotiations is over."
    "Both of us dash to the side, ducking behind a bookshelf just as the hydra's massive claw swipes where we were standing. The impact cleaves the table in two."
    "Lucifrid summons forth his spider legions and I manifest his tome to call upon the names of other familiars." 
    e "I can’t believe talking things out didn’t work! And you were so accommodating!"
    l "Are my ears deceiving me? Are you advocating violence?"
    e "Oh, I would never."
    "I focus my thoughts on a spirit we subdued recently and the tome flutters open to the page where its name is inlaid. I place my hand over the thick ink and chant the invocation."
    e "Heed the voice that calls, honour the ties that bind."
    "The librarian doesn’t wait for my summoning ritual and bites at me with one of her heads."
    l "Charge!"
    "Luckily Lucifrid has less need for preparation. His spiders rush in without hesitation at his command, creating a veritable wall between me and my feline assailant."
    "In the meantime, the fire spirit I called for rises up from the tome and an idea sprouts in my mind."
    "We’re on the defensive now, and we can’t compete with her brute strength. We’re going to need trickery of some kind."
    e "Go! Raze the shelves!"
    "The fire spirit flies off on burning wings at my command, setting aflame the defenseless books at the slightest touch."
    "I flash Lucifrid a cheeky grin. I can't believe it but... this is kind of fun."
    e "I hope you didn’t need those!"
    l "I was never much of a reader anyway."
    "The cat-hydra seems to grow even angrier, growling, hissing and charging after the fire spirit."
    "The distraction affords Lucifrid the time to spin a dense web around us as a protective barrier, his underlings working industriously to fortify its gaps."
    l "You’re clearly its target, so please take cover behind the web and act defenseless. And say some incensing words; I know you’re skilled at that."
    e "Will it be enough to stop her? She broke out of your other web pretty easily..."
    l "Probably, hehe!"
    #edelweiss unamused
    e "{i}Probably{/i} is not enough with my life on the line!"
    l "Oh, have some faith in me. When have I allowed harm to befall my dearest partner?"
    "With the librarian and fire spirit embroiled in combat, the library is well and truly ablaze now. I grow a little worried for our spidery friends."
    "I search for Yang and his battalion. They’re safely perched in the web, ready to attack; my courageous little fighters. I probably shouldn’t distract them."
    "It doesn’t take long for the librarian to get the upper hand over my summon and I trace its name on the page, bidding it to return to its slumber." 
    e "Well fought, you may rest now." 
    "Then the librarian focuses all her heads on us, looking no wearier for taking out her previous opponent." 
    #edelweiss uncomfortable
    e "..."
    "There’s nothing to do but stick to Lucifrid’s plan. I swallow hard and try to dispel my doubts."
    e "Here, kitty! If you’re quick you might make it before all your books are turned to ash."
    e "Ack!"
    "As smoke floods my respiratory system, I start coughing. This is more dangerous than I thought."
    l "Edelweiss! Are you alright?"
    "I can hardly stop coughing as I try to force out a sentence."
    e "S-smoke— we need to—" 
    "Another cough."
    e "G-get out—"
    "Without a moment’s pause, Lucifrid grabs my hands. From the corner of my eye I see the librarian moving in on us, ready to pounce."
    l "Quick, Edie, close your eyes!"
    "I forcefully squint my eyes shut; half in obedience and half in the unwitting, childlike belief that a threat disappears when you can’t see it."
    "I can still hear the cat-hydra’s gallop as the floor disappears beneath me and that familiar queasy feeling fills my stomach. He’s taking us back across the boundary!"
    "Is that even safe? What’s going to happen to the librarian?"
    "I don’t have time to ponder as we stumble and crash back into the human realm, accompanied by our entire army of spiders."
    e "Ow, ow, ow!"
    "The two students occupying the library turn to look at the source of the sudden racket. Guess I have to find some way to explain appearing out of thin air later."
    l "Don’t let your guard down!"
    "But it’s too late. When I look up I see the librarian has followed through the pathway we made; the threads we spun enough to cut and scrape, but not enough to stop her."
    "She bites, and with the unnatural speed only an apparition could muster, Lucifrid grabs me and pulls me out of her path."
    "Adrenaline rushing through my veins, I muster all my focus to summon the tome." 
    "That was way too close!"
    "Arachnids swarm our assailant, and she shrieks and shakes to drive them off."
    "Possessing none of his usual controlled nonchalance, Lucifrid jumps atop the feline monstrosity and bites down savagely on one of her necks."
    "The spiders follow his lead in one coordinated biting motion and she wails in agony."
    l "Now!"
    e "Speak thy name and thine allegiance be manifest!"
    "I bash one of her heads with the tome and to my utter relief, ink starts pulling from her form onto the page."
    "As her name is absorbed, she is transfigured back into a harmless house cat.Her paws land softly on the carpet, and she quickly scampers off."
    "Our army of familiars disbands and the spiders disappear to their usual hiding places."
    "I collapse to the floor, tome clutched to my chest, breathing heavy. Lucifrid rushes over to me but doesn’t say a word."
    "I follow his gaze and my stomach twists. The students..."
    "While Lucifrid saved me from the librarian’s bite, it seems her other heads reached their targets unhindered."
    "One of them wheezes with every breath, ribs hitching as if something inside won’t move the way it should." 
    "Another lies frighteningly still until a shudder runs through them, their jaw tightening around a sound of pain they don’t quite manage to suppress."
    "I listen for their breaths without meaning to."
    "This... is this my fault? Because I was here? Because Lucifrid had to protect me?"
    l "Don’t worry. They’ll be fine. I’m just glad you’re unharmed."
    "He smiles. Not a smirk, or a grin. A smile."
    e "But..."
    "The words don’t come to me. I’m not sure what better choices were available to me, but I can’t feel right about this."
    "Lucifrid walks over to the wounded students and makes unfamiliar motions with his four arms."
    #edelweiss confused
    e "...?"
    l "I can’t heal them, but they’ll forget what happened. No one will know we were here."
    #sfx footsteps
    "I freeze at the sound of someone approaching."
    l "Come, let’s get out of here. Our job is done."
    "I open my mouth to stammer a protest but I’m too tired to formulate my thoughts into words. I relent and let Lucifrid drag me back to our hideout, away from the chaos we caused."

    #bg hallway
    #bg hideout
    #fade to black

    #bg library
    #sfx footsteps
    #ilya cold
    i "..."
    i "...it’s one thing to make a mess of things, but to not even clean it up..."
    if ilya_respect >= 1:
        i "I expected better of you, Edelweiss."
    else:
        i "Just as I thought, you have no clue what you’ve gotten into, Edelweiss."
    #ilya indignant
    i "You leave me no choice. I can’t let this slide."
    #fade to black

    scene classroom day

    "Liese" "And after all that, I still missed the train!"
    "Phila" "I think that was entirely your own fault..."
    "Liese" "No way! The conductor should’ve understood my plight! Right, Mari?"
    "Marigold" "W-well, the timetable would get all messed up then. He did the best he could, I think."
    #sliding door sfx
    #edelweiss sprite appears
    "Liese" "Oh! Edelweiss!"
    "Phila" "Good morning!"
    #edelweiss smiles
    e "Morning! I thought I’d come check in!"
    e "But it seems a certain someone is entirely back to normal."
    "Marigold" "They told me you went investigating on my behalf. Thank you, Edelweiss... You’d do that for someone you barely know..."
    e "What can I say, I can’t resist a good mystery."
    "Phila" "So, did you figure out what happened?"
    "Marigold" "I still don’t know... My voice came back as suddenly as it disappeared."
    e "I’m sure it’s all because of my efforts, {i}hehe!{/i}"
    "Liese" "But... what did you do...?"
    #sliding door sfx
    #ilya neutral/calm appears
    #edelweiss uncomfortable
    e "..."
    "Phila" "Ilya! Good morning!"
    "Liese" "Vice-president Ilya, what a pleasant sight early in the morning. Can I help you with anything?"
    #ilya gentle
    i "Good morning Phila, Liese, Marigold."
    "He makes eye contact with them in turn as he says their names, to which they each grow a shade redder."
    i "Actually, my business today is with Edelweiss. You don’t mind if I borrow her for a moment, do you?"
    "Phila" "No, no! Go right ahead!"
    "Liese nods along emphatically as my blood runs cold. It might freeze in my veins if I keep looking at that icy smile."
    e "Ah, sorry, I forgot I actually have fish feeding duty! Gotta head over to my classroom!"
    #ilya cold smile
    i "No worries, I’ll assist you while we chat. I won’t take much of your time."
    e "...ahaha. Thank you."
    "Marigold" "Oh, he’s so kind..."
    "Don’t be fooled, Marigold. Why are you all so weak to his charms?!"

    scene hallway
    #sfx footsteps
    e "Uh, yeah, I don’t actually need to feed the fish."
    #ilya smile
    i "I know. Your classroom doesn’t have fish, Edelweiss. You have a rabbit."
    i "Why don’t you come to the student council room with me? We’ll have some privacy there."
    "Privacy? I guess president Rosiel must be busy with cultural festival preparations."
    "The way he phrases it doesn’t make it seem like a suggestion. Resigning myself to my fate, I follow him through the halls."
    #sfx sliding door
    #bg student council room
    #ilya neutral
    i "Tea?"
    "Ilya walks over to the kettle without waiting for my response."
    e "That’s alright." 
    #ilya smile
    i "Hm? It’s not poisoned or anything."
    #edelweiss laugh
    e "We all know people usually announce their poisoning attempts beforehand."
    i "I’ll take that as a yes then."
    "I’m slowly learning that talking to Ilya is like one of those video games where you’re presented with a choice but the question simply repeats until you choose the correct answer."
    #cup placed on table sfx
    #sitting down sfx
    #ilya solemn
    i "I visited the hospital yesterday. I thought you might want to know that Johan and Caitlin are doing alright considering the circumstances."
    i "They’ll return home soon but they probably won’t make a complete recovery in time for the cultural festival."
    "Johan and Caitlin. I only learned their names after the fact, but they’re the students that got hurt in the library."
    "I cast my eyes downward and fiddle with the hem of my skirt."
    #edelweiss uncomfortable
    e "I... wish them a speedy recovery."
    "There’s no use in pretending I don’t know what he’s talking about. I wanted to go visit them myself to apologise—but Lucifrid told me I couldn’t."
    "Something about how their memories are muddled, so it could mess with their mental state if I confused them further by apologising for something they don’t remember."
    "The whole situation makes my stomach turn, and not even being allowed to own up to my mistakes is just pouring salt in the wound."
    i "Let me start by saying this."
    "Ilya couldn’t possibly make me feel worse about this than I already do."
    "I know it’s all my fault."
    #ilya gentle
    i "I don’t blame you, Edelweiss."
    e "...!"
    i "That spider has been using you as a pawn in his battle for control of the school, and he doesn’t care who or what gets caught in the crossfire." 
    i "Can’t you see? He’s showing you his true colours now."


    menu:
        "No, no! He’s got everything all wrong. But what can I even say to him?"
        
        "He only went after the library cat because I asked him to!#":
            jump postchoice_ilyajustify
        "The only reason the battle escalated to our side of the school is because I started a fire and then couldn’t handle the smoke!#":
            jump postchoice_ilyajustify
        "The students got hurt when he lost focus because I’m weak and he needed to protect me!#":
            jump postchoice_ilyajustify


label postchoice_ilyajustify:


    #ilya pity
    i "Please listen to yourself. You’re making excuses for an apparition."
    "{i}I'm making excuses for Lucifrid?{/i} What does he know about Lucifrid and I?"
    "I should’ve known I wouldn’t convince him..."
    i "I didn’t know his influence had gotten this bad. I should’ve taken action sooner."
    i "Forgive me my carelessness, Edelweiss. You’re my junior and I should’ve protected you."
    #ilya cold
    i "Rest assured that the next time I see that vile creature, I will reduce him to dust. I swear it on my honour as an exorcist." 
    #ilya gentle
    i "And I have faith that you’ll thank me for it once you’re free from his grasp."
    "No... This isn’t what I wanted! I’ve messed everything up!"
    "I thought I could keep Lucifrid safe from him! He doesn’t deserve to be exorcised!"
    "And now I’m the one who doomed him with my selfish request, because I needed to be useful to my fellow students so badly."
    "No, perhaps it’s not that. If I’d just been a better diviner... If I’d paid more attention in my lessons, if I was more like Mother..."
    "Can I persuade Ilya by telling him my soul is bound to Lucifrid’s? I don’t even know what that means in practical terms. He did say ‘neither life nor death shall come between us’."
    "But what if he'll just use the information against me? I don't want to mess up anymore... I don't know what to do."


    menu:
        "Well, Edelweiss, don't just stare at him. Say something!"


        "You haven’t once tried talking with him!# You’d see Lucifrid’s not the one at fault here if you just gave him a chance! How will there ever be cooperation between diviners and exorcists if you simply force your way?!":
            
            $ ilya_affection -= 1
            $ ilya_respect -= 1
            $ negative_arc += 1
            
            #ilya calm
            i "I feared you would respond like this."
            i "I gave you a chance to do things your way. I can’t stand idly by while people get hurt due to your inexperience and grand ideals."
            #ilya sigh
            i "I wanted us to cooperate. I didn’t want to have to force anything."
            i "Why do you trust that monster more than you trust your fellow student? He cares nothing for human lives, no matter how much he has made you believe you’re special."
            "I bite my lip, holding in the urge to say: ‘But I {i}am{/i} special to him.’"
            "Is Ilya right? Is Lucifrid performing an elaborate act?"
            "Even if all his affection is a farce, he still needs me. But then the question remains: for how long?"
            "Have I just caused trouble for him in the end? Just been a burden on him and Ilya at the same time?"
            #edelweiss teary
            e "You... you don’t know any of that..."
            e "Why would you— *sniff*"
            "I can’t stop my tears from welling up."
            e "You’re mean... But you keep pretending like you’re nice... That’s why I can’t trust you!"
            #ilya baffled
            i "..."
            "The ever-charming, perpetually calm student council vice-president is clearly at a loss for words."
            i "I, um, well..."
            #edelweiss angry
            e "See! You’re not even denying it! Do whatever you want, I’ll never go along with your plans!"
            e "Accusing someone of manipulating me when you’re doing the same stupid thing!"
            "As hot tears involuntarily start rolling down my cheeks, I storm out of the room, leaving Ilya behind in his stupor. I can’t bear to hear more of what he has to say."
            "So he’s our enemy now, so what? We’ll show him."


            jump postchoice_ilyafallout




        "I’m truly sorry for what happened, Ilya.# I overestimated my abilities as a diviner, and I’ll work to make reparations. Please give me another chance to deal with Lucifrid by myself.":
            
            $ ilya_affection += 1
            $ negative_arc += 1
            
            #ilya gentle
            i "I’m sorry too, Edelweiss. It’s not that I don’t trust your intentions, but this is too dangerous for you alone."
            #ilya pity
            i "Please... don’t place the blame on yourself. We can work together to set this right, it’s not too late."
            "That pitying look again... He truly doesn’t trust me to accomplish anything by myself, does he?"
            "I suppose I can hardly blame him. I wouldn’t trust me either."
            #edelweiss neutral
            e "I would be happy to work together, but I won’t exorcise Lucifrid. He’s done nothing to warrant that. It would be akin to betraying my mother’s legacy."
            #ilya calm
            i "Then I’m afraid there is nothing left to discuss. When next we meet in the company of that apparition, you and I will be enemies."
            #ilya gentle
            i "I won’t hold back, but I’ll be here for you once it’s over."
            "A shiver creeps up my back. He means it."
            #edelweiss uncomfortable
            e "I haven’t given up on convincing you."
            #ilya gentle
            i "And I, you."
            "Just like last time, the two of us shake hands, as if to formalise the breaking of our tenuous peace."
            "May the righteous one win. Or something."


            jump postchoice_ilyafallout




        "Lucifrid did all this at my request.# It didn’t go perfectly, but we did get back the students’ voices that were stolen. You need us for when stronger apparitions inevitably threaten the school.":
            
            $ ilya_respect += 1
            $ positive_arc += 1


            "I try to get ahold of myself, gathering together what little composure I can find inside of me. No matter how I feel, I can’t let him get the better of me." 
            "Think. What would Lucifrid do? He’d posture and intimidate, overemphasising his own indispensability."
            "I breathe in deeply and continue in his tradition." 
            e "What would you have had me do, Ilya? Stand by and do nothing to win back our students’ voices?" 
            #ilya gentle
            i "You could have come to me for help."
            e "Yes, and then you would have killed the cat, and Lucifrid too while you were at it." 
            #ilya annoyed smile
            i "Exorcism is not {i}murder{/i}, Edelweiss."
            e "All the same as you can’t condone my methods, I can’t condone yours."
            e "If you eliminate Lucifrid now, you lose all the apparitions the two of us have under our control as familiars."
            e "Isn’t it strange that the students’ voices could get stolen to begin with? Haven’t you noticed that the apparitions’ influence is increasing?"
            #ilya calm
            i "It hasn’t escaped my notice. That is precisely why we need to act before things escalate any further." 
            e "You need us, Ilya. If Lucifrid has undisputed rule over the beyond, none of this will happen."
            #ilya cold
            i "Is that what you think?"
            "He laughs humourlessly."
            i "How do you know he isn’t the one behind all of this?"
            e "What does he stand to gain by any of that?!"
            "Calm down, Edelweiss. If you lose your composure, he wins."
            #ilya calm
            i "There’s no convincing you, I can see that now. But you will see that I’m right in time, that this is for your good as well."
            #edelweiss stern
            e "I doubt that."
            i "..."
            e "..."
            "We stare pointedly at each other for a moment, neither of us wanting to relent."
            "There’s a strange glint in his eyes, almost like he’s enjoying this rivalry."
            e "Well, there’s nothing more to talk about here."
            i "I’ll see you out."
            #sliding door sfx


label postchoice_ilyafallout:
    scene black
    with fade


    scene hallway
    #add inline variable [quiet, not-so-quiet] in line below
    "Since my confrontation with Ilya, the dissolution of our armistice, I haven’t quite known how to proceed."
    "Ilya is out for blood—do apparitions have blood?—that much is obvious, but I don’t think he can find Lucifrid on his own, or else he would’ve made a move much sooner." 
    "Of course, I wanted to warn Lucifrid... but I don’t know Ilya’s tactics. If he’s somehow following me then I’d be leading him right to his target."
    "As proven by our last battle, I’m little more than a liability. It’s not like I can smack Ilya in the head with a tome and make him our familiar..."
    "So these past few days I’ve been going straight home after classes, training with Emrys at home to learn more about the spirit realm."
    "It feels like a futile endeavour. Our enemy is human, not apparition. But it’s the only thing I can do to attempt to shake off the feeling of uselessness that keeps haunting me."
    "I tell myself the distance between us is a strategic choice, but deep inside I hear that voice over and over:"
    #bg blurs and line displays in middle of screen
    "{i}Lucifrid is better off without you.{/i}"
    #world comes into focus
    #lucifrid intimidating
    l "What on Earth do you think you’re doing?"
    #edelweiss downcast
    e "...Walking down the hall."
    l "Don’t you dare play dumb with me."
    #lucy close up
    l "What{w} are{w} you{w} doing?"
    "He backs me into a corner, his usual favourite tactic, and I can’t bring myself to look into his eyes."
    e "I have my reasons."
    e "{size=-8}Now please stop, you’re making me look weird in front of the other students.{/size}"
    l "Oh, I’m making you look weird, is that it?"
    l "Yes, that would be a grave matter. Truly a fate worse than death."
    l "Why are you avoiding me, Edelweiss?"
    l "You know that it’s pointless, yes? That you will not be rid of me in this lifetime? That our {i}souls{/i} are {i}bound{/i}?"
    #ilya appears in the distance
    e "...!"
    "Without time to think, I open the door Lucifrid has me cornered against."
    e "Quick!"
    #cg broom closet
    "The prince of spiders stumbles in after me and I turn the lock on the door."
    "Then I notice how very small this room is.{w} And how little space there is between us."
    #lucifrid angry
    l "Will you explain to me what exactly you’re trying to do?!"
    #edelweiss panic/teary
    e "Shh! Please, just be quiet! I’ll explain everything if you promise you’ll be quiet."
    #lucifrid neutral
    "Lucifrid’s angry expression fades when he notices the genuine panic in my voice."
    "I lower my voice to a whisper, afraid Ilya may find us."
    e "I— I messed up..."
    e "Of course, you know that I messed up... But you don’t know what it led to..."
    e "I thought I could protect you!"
    e "Ilya, that exorcist... He’s set on eliminating you. I-I couldn’t convince him otherwise."
    e "It’s all because of me! But— but I can still set it right!"
    e "If I can just stay away from you, then I can keep you safe."
    e "...It’s the only good I can do now."
    l "Edelweiss..."
    "Lucifrid takes hold of my chin and lifts my face to make me meet his gaze."
    "Blood rushes to my head and all I can think about is how unsightly I must seem to him in this moment."
    l "You’re an idiot."
    l "How does all of this have any bearing on me?"
    l "I am a deity of the otherworld. You are worried over nothing. You think I can’t handle something like this?"
    "Yes, he’s right. I’m an idiot. I know that. But... I didn’t know what to do."
    "I never know what to do. And yet I keep moving, and acting, and making things worse."
    e "It doesn’t matter if you can handle it! Be honest, I’m a burden on you! You’d be better off without me holding you down!"
    #lucifrid intimidating
    l "Are you questioning my judgment, Edie?"
    "He leans his forehead against mine as he continues. My heart feels like it’s beating in my throat."
    #lucifrid grin
    l "I won’t say this twice, so listen closely."
    l "You are not a burden on me. I have need of you. {i}You{/i}, and no one else."
    #edelweiss blushes
    l "You are my precious assistant, and I will not tolerate you running off elsewhere, no matter what silly justifications you come up with for yourself." 
    l "No matter your doubts, from now on you come to me instead of trying to take care of things alone."


    menu:
        "...Okay. Thank you, Lucifrid.#":
            $ positive_arc += 1
            #lucifrid pause
            "Something changes in Lucifrid then. He’s normally so quick to respond, so candid in his emotions, but now, he seems unsure."
            "I was expecting him to tease me for being an obedient little helper, but he lets the moment linger."
            "My eyes trace his form. The way his hair falls over his brow; the way it curls at the nape of his neck. The deep vermillion of his eyes."
            "Without thinking I cup his face in my hand."
            "He casually forces his touch upon me all the time, but when have I moved to touch him?"
            "He still doesn’t move. The slight smile he wears seems almost shy."
            "With my own heartbeat calmed and no longer filling up my ears, the quiet allows me to notice his for the first time."
            "He isn’t human, but he lives and breathes and feels."
            e "I mean it, thank you. When I get like this... it’s almost impossible for me to shake myself out of it."
            #cg changes to regular position
            l "It was never quite my intention to became an expert in the stirrings of the human heart, but it seems I hold at least a faint grasp over yours."
            l "Cheer up now, worrywart."
            jump postchoice_broomcloset


        "How am I supposed to trust anything you say with that smirk on your face?#":
            $ lucy_yan += 1
            #cg changes to regular position
            #lucifrid innocent
            l "Oh, you wound me."
            l "I was being entirely earnest!"
            l "I’m busy enough managing all the threats upon our domain without you suffering existential crises."
            #edelweiss pout
            e "See! Right back to the bullying! Your feigned concern is only self-serving in the end."
            #lucifrid serious
            l "Though it may serve me well, that doesn’t mean the concern is feigned."
            l "You are free to believe what you will, so long as you obey my command."
            #lucifrid grin
            l "I will show you just how serious I am through actions rather than words."
            e "First bullying, now threats of physical nature... I can hardly remember why I felt the need to protect you."
            l "Perfect! Then it seems this crisis is resolved."
            jump postchoice_broomcloset


label postchoice_broomcloset:
    "It’s hard to believe the prince of spiders is skilled at easing the pains and fears of teenage girls, but I can’t deny that I’m feeling better."
    "My mind cleared of its undue fog, a lingering question from before rises to the surface."
    e "Something’s been on my mind lately because of Ilya’s threats. What would happen if you got exorcised while we have our contract?"
    l "I can’t believe you would entertain the thought! A deity of the beyond is not so easily bested."
    e "That’s not answering the question."
    l "Because the question is completely divorced from reality!"
    e "...you don’t actually know what will happen, do you?"
    l "Ah, I still remember the day I forced you into this arrangement. You were shaking like a leaf, trying to seem brave."
    l "You hated my guts, didn’t you?"
    l "And look at you now, worrying about the evil overlord, you pure, innocent soul!"
    e "Who will have use of my abilities when you’re gone? You’re not the only one who can mix care with pragmatism, Lucy!"
    #lucifrid blushes
    l "L-Lucy?"
    #edelweiss blushes
    e "O-oh. Um."
    e "You always call me Edie too..."
    l "Hmph. I suppose I can allow it this one time."
    "Our eyes meet and the world seems to freeze in time. Everything we were arguing about vanishes into thin air."
    "Suddenly the close quarters we find ourselves in seem too close for comfort."
    "I become hyper-aware of exactly how many centimeters are between us, how many layers separate us, and my heart starts to race."
    "The thought he might be able to hear my heart beating from this distance becomes too much for me to bear."
    "Surely Ilya will be gone by now."
    "Right?"
    e "Ahem."
    e "I-it’s probably safe. Let’s get out of here."


    scene hallway 
    #sfx crash 
    #sfx panting
    #sfx running
    "I struggle to catch my breath while running down the third floor hallway."
    "Something is after me, but I’m not about to stick around to find out what it is." 
    "Where’s Lucifrid when you need him? Why is an apparition haunting the light side so aggressively?"
    "???" "Edelweiss... Accursed human..."
    "And why does it know my name?!"
    "This is bad."
    "The last thing I need is a repeat of the last time an apparition found its way to the light side."
    "I have to get it out of the way of the other students somehow!" 
    "Without time to weigh my options, I run towards the courtyard. Everyone should still be in class, and an open area will at least minimise damage to the building."
    
    scene courtyard day
    with MVNStainedGlass10

    e "Hah... hah..."
    "Pausing to catch my breath, I swivel around to face my adversary for the first time."
    "The horned humanoid creature dons a mask portraying a most eerie grin."
    "At first glance it doesn’t appear too powerful, but one can never judge an apparition by its physical form."
    "???" "Edelweiss... You shall pay for your crimes..."
    "Should I try to bargain with it? Well, it’s that or running. Without the Yang battalion or Lucifrid’s tome I’m not about to beat it into submission." 
    "Lucifrid will sense something amiss with me by virtue of our bond, I just need to bide my time until he gets here."
    e "Don’t come any closer!"
    #sfx bells
    "I hold out my belled staff, a minor family talisman I managed to persuade father to let me carry with me, and the horned apparition stops in its tracks."
    "It evidently looks the part of a spirit-repelling artifact, but the staff’s true power is dubious at best."
    "But this isn’t the first time I’m posturing in front of apparitions, and something tells me it won’t be the last."
    e "What is your quarrel with me, fiend?"
    "???" "Don’t play innocent!"
    "???" "You burned our library, and robbed us of decades of knowledge!"
    "???" "Even our librarian isn’t fit to rebuild anything, reduced to a mere pet."
    "???" "Your debt cannot be repaid, but spilling your blood will dull the ache, if but for a moment."
    "It’s not enough to bear the guilt on one side of this conflict, huh? Seems I’ve earned myself universal scorn."
    e "Ah yes, spilling blood for ink. The height of justice."
    e "Is that library worth putting your life on the line for?"
    #sfx bells
    "I shake my staff menacingly once more."
    "???" "Bwahahaha."
    "The creature laughs derisively."
    "???" "You don’t frighten me, human. We’ll see how strong you are when you can’t cower behind the spider prince."
    "Well, that’s about as far as dialogue will get me."
    "I jump backwards to put some extra distance between us, and still holding the staff towards it, begin chanting a rite I studied up on recently."
    #edelweiss determined
    e "Light unto light, dark unto dark. Stay thy hand, walk thy path."
    "The masked spirit is slowed, but keeps pushing towards me. As expected, the rite isn’t strong enough..."
    "A heavy feeling sinks into my stomach bit by bit."
    "Why isn’t Lucifrid here yet?"
    #edelweiss panic
    e "Light unto light, dark unto dark! Stay thy hand, walk thy path!"
    "As the apparition inches closer, sweat starts to form on my brow. I don’t know what else I’m supposed to do!"
    "My eyes wander around for any sort of escape, then spot Ilya through the window. He’s heading this way! I don’t believe I’ve ever been so glad to see him."
    "Ilya bursts through the doors and into the courtyard. Though his movements are hurried, his expression doesn’t betray the slightest agitation."
    "Stress-fueled adrenaline coursing through my veins, I dash off to the side to hopefully give Ilya an opening to attack."
    #ilya determined
    i "Edelweiss! Don’t stop chanting!"
    "Channelling my focus, I repeat the words once more."
    e "Light unto light, dark unto dark. Stay thy hand, walk thy path."
    "Ilya throws a number of paper talismans at the apparition then adds his bracelet’s jingling to my belled staff’s."
    "Our voices ring in unison, until his phrase changes."
    i "Light unto light, dark unto dark. From nothing thy comest, and to nothing thy shalt return."
    "The apparition is cast to the ground by an invisible force and wails."
    "???" "Foul exorcist! This was not your fight to meddle in!"
    "???" "Anathema on you and your house!"
    "The masked figure bursts into flame, disintegrating piece by piece."
    "I can’t help but avert my eyes."
    "???" "More of my kin will come for you, Edelweiss!"
    "Until its last breath it curses us, and the pained sound echoes horrifically."
    "As I try to focus on anything else, Ilya rushes over to me, face flushed with an unreadable expression."




    if ilya_affection >= 2:
        #ilya worry
        i "Are you alright, Edelweiss?"
        "Ilya’s composure seems actually shaken, the worry apparent in his voice."
        i "This is precisely what I didn’t want happening to you..."
        "I let out a deep breath."
        e "Y-yeah, I am. ...Thanks."
        "There’s no use clinging on to my pride here. I would’ve been toast without him, and seeing his genuine emotion is almost disarming."
        "I was useless again by myself..."
        #ilya neutral
        i "What happened? Did that demon leave you to fight his battles all by yourself?"
        #e distressed
        e "N-no! I don’t know how it happened... It just suddenly appeared and started chasing me and calling my name."
        e "Maybe I’m just a magnet for these things. It seems I’m only making everything worse..."
        e "Lucifrid should’ve been able to sense I was in trouble. I don’t know what took him so long."
        #ilya cold
        i "Sense? Why would he have sensed that?"
        "I swallow hard, unable to utter more than a small stammer. I said too much."
        i "Haven’t I told you over and over? An apparition doesn’t form bonds like a human does—everything is transactional to them. As soon as you have no value, you will be discarded."
        #edelweiss downcast
        e "Y-you’re wrong. I still have value. Lucifrid and I... our souls are bound."
        #ilya shock
        i "You... That’s what this was all along?!"




    else:
        #ilya annoyed
        i "You could’ve gotten yourself killed, Edelweiss. What were you thinking?!"
        #edelweiss annoyed
        e "The apparition didn’t exactly show up at my invitation."
        i "Then why was it calling your name?"
        #edelweiss upset
        e "Because it hates my guts, Ilya!"
        e "Because every time I try to {i}fix{/i} something around here, every time I try to be a good person and follow my moral compass, I end up disappointing absolutely everyone involved."
        e "Isn’t it nice to know you’re not the only one who thinks I’m an abject failure?"
        e "Heck, count me in while we’re at it. Even {i}I{/i} have started hating my own guts."


        if ilya_respect >= 1:
            #ilya strict
            i "Stop it. Stop abasing yourself."
            #ilya pity
            i "I don’t... think you’re an ‘abject failure’."
            #ilya gentle
            i "I don’t."
            i "I just wish you would let yourself in with better company. ...Company that actually shows up when you’re in mortal peril."
        else:
            #ilya cold
            i "I’m sure wallowing in self-pity has been an indispensable tactic in your life so far, but perhaps you should try something constructive for once."
            i "Go on, cry to that spider for help and see how it’ll serve you."
            i "Do you still believe he cares about you? Where is he now?"


        #edelweiss verge of tears
        e "..."
        e "...I’m sure he has his reasons."
        e "The point is- I- I didn’t know these things could even cross over here all on their own! This whole school is a mess!"
        #ilya frown
        i "That’s the thing, they never could do that! Something has upset the balance, but the mere involvement of a diviner shouldn’t be able to-"
        #ilya shock
        i "Unless..."
        "He looks at me almost in horror."
        i "You made a contract with him, didn’t you?"
        #edelweiss flinch
        e "...!"


    #ilya pity
    i "If that’s the case then... what can I even do?"
    i "This can’t go on like this, Edelweiss. This contract between the two of you is slowly melding the light and dark side of the barrier into one amalgamation."
    i "I’ve never seen anything this disordered occur, but it must be because of your respective affinities."
    "Can I trust what he says? Is this another tactic to get me on his side?"
    "...Is everything really my fault again?"
    #edelweiss downcast
    e "..."
    #ilya stern
    i "Do you think this is what it means to keep the balance between the realms? That {i}this{/i} is your duty as a diviner?"
    #edelweiss pensive
    e "It’s not what I set out to do... But I don’t think it’s all bad."
    e "I have real power now, I can do something to protect this school."
    i "You have no clue what you’ve gotten yourself into."
    i "This needs to be set right, one way or another."
    if ilya_affection >= 2:
        i "I will save you, Edelweiss. You can depend on me."
    else:
        i "I will do what I must, Edelweiss. That I promise."
    "When I avert my eyes to avoid Ilya’s piercing gaze, I notice Lucifrid glaring daggers at us from the roof, and I start to piece things together."
    "Lucifrid isn’t late, and he certainly hasn’t abandoned me. He simply couldn’t approach without risking exorcism at Ilya’s hands."
    "The roof is as close as he can get without being noticed."
    #edelweiss neutral
    e "I have to go."
    "Ilya blankly nods at me as I leave the courtyard."


    scene hallway
    with fade
    scene classroom evening
    #bg hideout
    #cut-in yang
    #edelweiss small smile
    e "...Hey little guy."
    "Yang patters over to me from under a desk as soon as I enter the room."
    "I have no idea if he has the emotional intelligence to tell that I could use company right now, but I’m grateful all the same."
    "There’s so much happening and I’ve barely had a moment to process it all."
    "When I was younger, when her passing still felt less like a scar and more like a wound, I used to imagine talking to Mother to get my thoughts in order."
    "It’s been a while but... maybe it would help. Mother would know what to do in this situation, I’m sure."


    #bg blurs
    #edelweiss’ Mom silhouette sprite appears
    "Mom" "What is it, Edie? Tell me what’s on your mind, I’m here to listen."


label mom_convo:
        
    menu:
        "Where do I even begin?"


        "Talk about being a diviner#" if momconvodiviner == 0:
            $ momconvodiviner += 1
            
            e "Well, one thing’s never changed. I’m still trying my hardest to be like you, Mother."
            e "I just... don’t know if I’m doing the right thing anymore."
            e "How far should I go to live up to your expectations?"


            menu:
                e "I'm almost scared to say this but..."
                "I’m not sure being a diviner is what {i}I{/i} really want.#":
                    $ positive_arc += 1
                    "Mom" "Don’t you worry about my expectations, dear."
                    "Mom" "All I’ve ever wanted is for you to be happy."
                    "Mom" "It’s no good to run away from your responsibilities, but that’s not what you’re doing, is it?"
                    "Mom" "Ever since you were little, you were so eager to please me and your father."
                    "Mom" "It’s alright to think of yourself too."


                "I don’t think I’m cut out to be a diviner.#":
                    $ negative_arc += 1
                    "Mom" "Aren’t you just afraid to face the possibility of failure?"
                    "Mom" "It’s always easier to give up and say you never intended to succeed, than to try and fall short."
                    "Mom" "You are the heir of our house, Edelweiss. Have some faith in yourself, and if not that, in your bloodline!"
                    "Mom" "I’ll always cheer you on."
            
            jump mom_convo


        "Talk about Lucifrid#" if momconvolucy == 0:


            $ momconvolucy += 1


            e "Well, you know about Lucifrid, don’t you? He’s the spider apparition who I bound my soul to."
            e "I didn’t really realise the gravity of the situation at the start, but I thought I was making the best of it."
            e "And now, our bond may be causing a whole lot of trouble..."
            e "Well, it’s not about that at all, is it?"
            "I make a sound somewhere between a sigh and a laugh."
            e "I just can’t get to the point, I can’t face my own feelings."


            menu:
                "He’s domineering and selfish and unreasonable and capricious, and it makes me afraid to trust him.#":
                    $ positive_arc -= 3
                    #locks you out of true ending
                "He’s domineering and selfish and unreasonable and capricious, and I think I love him.#":
                    $ ilya_affection -= 3
                    #locks you out of ilya ending
                "My feelings keep swaying between one extreme and the other.#":
                    $ lucy_yan += 1


            "Mom" "You’ve gotten entangled in his web now."
            "Mom" "And the more you struggle, the more you get stuck."
            "Mom" "I’ve always told you, haven’t I? That no good comes from getting so wrapped up in the affairs of apparitions."
            "Mom" "But you just wouldn’t listen."
            "She smiles and shakes her head. There’s no condemnation in her tone."
            "Mom" "Look out for yourself, alright?"


            jump mom_convo


        "Talk about Ilya#" if momconvoilya == 0:


            $ momconvoilya += 1


            e "So there’s more than one person who’s been meddling in my life... There’s an exorcist attending this school—his name is Ilya."
            e "At first I was excited to find someone else who knows about the spirit realm, but we uh, haven’t really been seeing eye to eye."
            e "He’s determined to get rid of Lucifrid... Thinks he’s doing it for my own good."


            menu:
                "Sometimes I find myself wondering if he’s right, wondering what would have happened if I met Ilya before getting caught up in Lucifrid’s plans.#":
                    $ ilya_affection += 1
                "I wish he’d stop acting so condescending, then maybe we could get along.#":
                    $ ilya_respect += 1
                "He’s an arrogant prick. I’ll prove him wrong soon enough.#":
                    $ ilya_affection -= 3


            "Mom" "An exorcist... I was hoping an encounter like that would help broaden your understanding."
            "Mom" "In an ideal world, exorcists and diviners would work together — kind where possible, unrelenting where necessary."
            "Mom" "But it seems like things are never quite that simple in reality."
            "Mom" "There’s nothing you can do but trust in your own judgment."


            jump mom_convo


        "I think I've addressed everything.#" if momconvoilya >= 1 and momconvolucy >= 1 and momconvodiviner >= 1:


            jump postchoice_momconvo


label postchoice_momconvo:
    "For a moment, the vision of my mother becomes almost tangible."
    "Mom" "Don’t make the same mistake I did, Edie. Choose your own happiness."
    "The same mistake she did? What does that mean?"
    "She laughs softly and fades from view. How- Was I... really talking to her?"
    "Giving no answer, the room grows still."
    "Yang and I sit together in silence for a moment, but it doesn’t take long for Lucifrid to show up."
    #lucifrid wrathful
    "I know that look on his face... This can’t be good."
    l "I saw you fraternising with that exorcist."
    l "Go ahead, I’ll give you one chance to explain that the two of you were not plotting against me."
    "He says it calmly, but his tone is laced with venom."
    e "Are you out of your mind?! I was attacked by an apparition! If Ilya didn’t show up, I could’ve well been dead!"
    "Yang crawls up to my shoulder, as if to bolster me. Lucifrid pays him no heed."
    l "Oh, is that how you see it? You’re relying on him now?"
    l "No, Edelweiss, you’ve got that very wrong. The only reason I didn’t step in—couldn’t step in—is because of that meddlesome human."
    l "He’s successfully convincing you to his side now, is he?!"
    "Suddenly his voice grows cutting and shrill, and I shrink back. What’s gotten into him?"
    e "What did you want me to do? Reject his help?! I was scared, Lucifrid!{w} ...I’m still scared."
    #lucifrid frown
    l "Well, don’t be! The danger has passed! I will never hurt you. When have I ever neglected to protect you?!"


    if lucy_yan <= 1 and positive_arc >= 3:
        $ true_ending += 1
        #edelweiss verge of tears
        e "P-please stop yelling... I know you’re not really like this. I trust you, Lucifrid, can’t you try to trust me too?"
        "I try to stay calm but my voice crumbles anyway. I choke out a sob, biting my lip hard to prevent myself from crying."
        "Crying won’t solve anything."
        l "..."
        "He falters."
        l "...I just can’t stand to see you with {i}him{/i}. Out of my reach."
        "Despite my best attempts, a single tear silently makes its way down my cheek."
        l "E-Edelweiss... I’m sorry... I’m sorry!"
        "He reaches out to catch my tear. I let him."
        "I won’t let anyone convince me he’s the villain. Not even Lucifrid himself."
        l "I don’t feel like myself lately. You’ve made me weak, and I hate it!"
        l "How can I be in control of anything if I’m not even in control of myself?!"
        l "Nothing is going like it was meant to go."
        e "But you don’t have to be in control all the time."
        e "In fact, well, these are just my thoughts but- {w}...Hmm, no, maybe it’s stupid."
        l "No, go on. I want to hear."
        e "It’s an impossible goal to begin with, right? What are we really in control of?"
        e "Certainly not the world around us, or the people in it. If you think everything is marching to your tune, it’s an illusion!"
        e "And the more you believe that it is, the more uneasy you become when things veer off course."
        e "Because if it’s all in the palm of your hand, then anything that goes wrong is your fault, right?"
        e "And- and- Some things are valuable {i}because{/i} they’re out of your control."
        e "Do you think I’m here because you willed it so? Because you’ve employed all your tactics and used all your talents?"
        e "If that’s so, then there’s no meaning in it."
        #edelweiss blush
        e "Sorry, I’m rambling..."
        l "You’re the only one who dares address me like this, Edelweiss."
        l "I don’t know if I agree with what you’re saying but..."
        l "Keep doing it."
        "He pauses pensively, then opens his mouth only to close it again."
        l "I’ll give you my trust. Don’t betray it."
        l "If it leads me to ruin, I’ll make sure you go down with me."


    else: 
        e "Stop acting like this! All you’re doing is proving Ilya’s point! If you don’t think of me as a tool, then try to treat me better than one."
        "Lucifrid suddenly bursts into laughter."
        l "A tool?"
        l "If you were a {i}tool{/i} to me, all of this would be much easier! Oh, if only."
        l "No, a tool could not unsettle me like this. If all I needed was your absolute obedience, I could rely on so many methods."
        #lucifrid wry smile
        l "Somewhere along the way, I started wanting something more of you. You’ve made all my methods impotent."


        menu:
            "I deflate like a balloon as all my pent-up anger floods out of me.#":


                $ negative_arc += 1


                "I suppose I got exactly what I wanted."
                "Yes, he needs me now, and he’s worse off for it. I’m worse than useless, I’m a liability."
                e "I never meant to do anything like that..."
                l "Well, it’s a good thing I’m so magnanimous and forgiving."
                "He pats my head."
                e "No, it’s not a good thing. I can see it already—you’re going to get yourself killed for my sake."
                e "The contract you thought would be a help is going to be nothing but a hindrance."
                l "Stop, stop, that’s nothing for you to concern yourself with. You only need to follow my lead and everything will be alright."
                l "The prince of spiders will ascend to kingship, one way or the other. And you will be my queen."


            "The pent-up anger inside of me threatens to explode.#":


                $ lucy_yan += 1
                $ lucy_distrust = True


                e "Oh, I see, you like me, so you’re going to treat me {i}worse{/i} than a tool!"
                e "This isn’t grade school! You don’t have to bully the girls you like! What if you tried being nice?"
                e "You ever consider that?"
                l "Being {i}nice{/i} hasn’t gotten me anywhere in life, Edie."
                l "Every single time I’ve tried to trust someone, it has been to my detriment. Apparitions are vile creatures, the exorcist isn’t wrong. But don’t think humans are any different."
                e "Well I’m not ‘humans’, I’m me. And the least you could do is trust me after I’ve stuck by your side despite everything."
                l "That doesn’t prove much when it was the only choice I left you."
                e "I have choices. Maybe I’ll make a different one soon."
                "His eyes grow cold. A miasma of oppressive darkness spills out from him."
                "Everything around me feels lifeless and still, like I am suddenly the only thing alive in this world."
                "Lucifrid doesn’t say another word. It feels like something inside him has cracked, but I don’t know what."


    if true_ending >= 1:
        jump post_Lucifridmeltdown
    elif ilya_affection >= 2:
        $ ilya_ending += 1
        $ lucy_distrust = True
        jump post_Lucifridmeltdown
    elif lucy_yan >= 2:
        $ lucy_ending += 1
        jump post_Lucifridmeltdown
    else:
        $ bad_ending += 1
        jump post_Lucifridmeltdown


label post_Lucifridmeltdown:


    "The wind from the open window rustles through the abandoned classroom, blowing a stray leaf inside."
    "I look outside at the waving treetops; they show hints of their autumn colours already."
    "It feels like ages have passed since I met him, but I suppose it hasn’t even been two months since that fateful encounter."
    "I can’t figure out how to broach the topic. That our contract is causing the boundary to fade. Our worlds to meld."
    "What will happen to us?"
    "..."
    "...No. I won’t bring it up. Not now."


    if lucy_distrust:


        "What good will it do to confide in him? He won’t believe what I have to say, especially once he figures out the knowledge comes from Ilya."
        "I’m tired. I’ll figure out some way to deal with this later. Maybe Emrys could help..."
        e "Can I go home for today?"
        l "Do as you please."
        
        scene hallway
        with fade
        scene classroom evening
        "And so I trudge off. I look for Emrys in our classroom, but it seems he’s headed home for the day already."
        "Well, that’s alright. I don’t know if I have the energy to go over the whole affair with him right now anyway."
        "I slump down at my desk, wanting to be neither here, nor home, nor anywhere."
        "It’s going to be alright.{w} It’s going to be alright.{w} It’s going to be alright."


    else:
        "I feel like something will irreversibly change once I mention it."
        "We’ll have to face the consequences eventually, but is it wrong for me to want these days to continue like this just a little longer?"
        "I glance over at Lucifrid, who has seated himself on his ‘throne’."
        "His eyes meet mine and he grins. I smile in return, glad to see him back to his usual demeanour after his outburst."
        l "Something on your mind?"
        l "I thought I’d let you rest after your little run-in today, but there’s always inferior creatures to subdue."
        e "Really? I thought we were getting pretty close to conquering the entire beyond!"
        l "Hehe, perhaps."
        "I move closer and sit down atop one of the desks facing Lucifrid."
        e "Maybe we can just relax here today."
        l "Oh? You have nothing better to do with your after-school hours than loiter with an apparition?"
        e "Not just any apparition! The prince of spiders, most powerful deity on the dark side of the boundary!"
        "He laughs heartily."
        l "Oh, now you’re just flattering me!"
        #edelweiss smirk
        e "What of it?"
        l "Well, don’t stop there!"
        e "Hmm, you want more titles? I think it’s already quite a mouthful, my arachnid overlord."
        e "Oh, right, what did the catgirl call you?"
        e "I am at your service, Your Dark Majesty."
        e "For loitering, or whatever else."
        "Who knew that he was this easy to amuse all along?"
        "But no, I get the sense his contented smile has nothing to do with the words I'm speaking."
        "He gets up from where he’s seated and looms over me."
        l "Whatever else?"
        "As he leans in closer, fangs gleaming, I can’t help but feel a hint of unease creep up on me still."
        "My gaze darts from his fangs up to his eyes. Then down again. Then up again."


        if true_ending >= 1:
            #edelweiss smile
            e "Whatever else."
        else:
            #edelweiss uncomfortable
            e "O-okay, maybe not {i}whatever{/i} else."


        l "Hehe, just kidding!"
        l "What sorts of twisted things were you hoping for, hmm?"
        "I pinch his cheek hard. He deserves it."
        l "Ow! I can’t believe I get assaulted for {i}not{/i} resorting to violence now!"
        "Our carefree days are bound to end someday soon, I can feel it. Can he feel it too?"
        "Regardless, that day is not today. Today we live. In feigned, blissful ignorance."


label endings:


    scene classroom day
    "It’s the dawn of the final day. The day before the cultural festival."
    "In the end, I barely helped out with our class exhibit. I think my classmates think I’m a slacker, which may well have been true any other year, but not this time."
    "I don’t think I have to tell you who’s to blame."
    "It’s almost thematic. Our class really did decide on a haunted house, though Lucifrid did not volunteer his help."
    
    #emrys focussed
    "Emrys did, though. He’s putting his peerless domestic skills to good use putting together various monster costumes from old bedsheets and other fabric scraps."
    "Right now he’s putting the final touches on a vampire’s cape."
    e "Ooh, this one’s looking fancy!"
    e "Who’s gonna play this character? It has to be a dashing fellow for it to work."
    e "Do the monsters have names? Can I give them names?"
    e "What about ‘Vergilius’? That sounds pretty vampirey to me."
    
    #emrys small smile
    em "I appreciate your enthusiasm, Edelweiss, but maybe you could channel it into helping out?"
    #edelweiss pout
    e "Thinking of names {i}is{/i} helping out!"
    "Classmate" "Hey Emrys, we can’t find the class decorations from the other day. Do you know where they were stored?"
    em "Sure, I’ll go get them. They should be in the storage room by the broom closet, but maybe someone moved them."
    em "Edelweiss, can you finish this? It’s very simple, you just need to glue this gem right here and make sure the bow isn’t crooked."
    e "Fine, fine... I’ll do it."
    "..."
    "It’s not as simple as Emrys made it look. I don’t have his talents."
    "The first time the gem falls clean off. The second time it’s not centered right. Don’t get me started on the bow."
    "When I finally get it to look passable, Emrys still isn’t back."
    e "Shouldn’t he be back by now?"
    "The other student merely shrugs."

    scene hallway
    "I don’t know what else there is for me to do, so I head out to look for Emrys. The storage room next to the broom closet, right."
    "The broom closet..."
    #broomcloset cg shows up in bw
    #edelweiss blushes
    e "..."
    "I force the memory back into my subconscious and make my way over."
    e "...Hmm?"
    "There’s a strange energy emanating from the door to the storage room. It’s like the sense an apparition’s presence gives off, but lighter, more suffused."
    "I open the door and my jaw clenches. This isn’t the storage room."
    "It’s dark, and warped, and {i}swaying{/i}. A mouse with three eyes slips out from behind a cabinet, past me into the hallway."
    "Oh, it’s bad. It’s very bad. The light side and the beyond, they’re really converging now."
    "I can’t step in there. Not without an anchor."
    e "Emrys?"
    "No response."
    e "Emrys?!"
    "I call out louder, but the sound seems to get swallowed in the darkness of a room that has no perceivable end."
    #sfx door slam
    "Did Emrys go in there? Is he lost in the beyond now?" 
    "No, calm down. Even if he did go in, it’s not too late."
    "I’ll go back to the classroom one more time, to see if he simply returned some other way."

    scene classroom day
    "But my fears aren’t quelled."
    "Classmate" "Where did Emrys get sidetracked? We need him to finish these too..."
    "He holds up several white sheets, presumably would-be ghosts."
    "Classmate" "Should I go check the storage room?"
    #edelweiss angry
    e "No!"
    "My classmate looks startled at my intense retort when he wasn’t even addressing me."
    #edelweiss uncomfortable
    e "Um, I already checked, he’s not there."
    "Classmate" "S-sure. Guess he’ll be back eventually."
    "I sit down in my chair, blankly staring out ahead of me."
    "Not only is Emrys missing in action, there’s also no guarantee others won’t suffer the same fate. Maybe they already have."
    "A wave of panic wells up inside me. Panic that normally I’d be relying on Emrys to dispel. But he’s not here now, and I have to find some way to solve all of this before it spirals out of my control."


    if true_ending >= 1:
        "I knew this moment would come eventually, all I can do is face it head-on."
    else:
        "How could I have let it get this far? My complacency knows no bounds. Was I just waiting for someone else to save the day for me again?"

    menu:
        "There’s only one person I can rely on..."


        "Lucifrid#" if true_ending >= 1:
            "I get up and walk towards the fourth floor."

            scene hallway
            "I don’t know what’s going to happen. I don’t know what we should do. But I know that as long as we’re together, we can handle anything."
            "I’m still nervous and scared, but I’m not unsure."
            "We’re going to save Emrys. What happens after that, we’ll figure out when we get there."

            scene classroom day
            #bg hideout
            "The hideout is crowded with spiders. They must be spilling over from the other side."
            "Past me would have been terrified, but their glittering eyes are strangely comforting now."
            "It means their master can’t be far."
            e "Lucifrid?"
            "I haven’t even finished calling his name and he appears."
            l "My dear assistant, to what do I owe the pleasure?"
            l "Ah, wait, don’t tell me. It’s begun, hasn’t it?"
            l "The boundary’s complete collapse is imminent."
            e "Heh, I guess it was silly to assume you didn’t know. Here I was, thinking I was one step ahead of you."
            l "Wait, how long have {i}you{/i} known?"
            e "A while. It seems we were both pretending to be ignorant and hoping the problem would go away."
            l "Who knew we had such similar methods!"
            e "Oh, I’ve been learning a lot from you."
            l "Hopefully some of it more useful than willful negligence."
            "We laugh, but our laughter soon fades into an uncomfortable silence."
            "Lucifrid has no quip at the ready. He just looks at me with a hint of wistfulness in his eyes, as if he’s waiting for me to say something to fix this mess."
            "Too bad Lucy, that’s what I was counting on you for..."
            e "Well, there {i}was{/i} a more manageable problem I was hoping we could address."
            l "More avenues for avoidance? Why didn’t you say so earlier? Go on."
            e "The storage room appears to have become a passage into the beyond, and Emrys wandered in unknowingly."
            e "That’s the only case I know of, but more students may have suffered the same fate."
            l "That boy does have a knack for getting you into trouble, doesn’t he?"
            "I shoot him an incredulous glance."
            e "Are you sure {i}you{/i} should be the one to say that?"
            l "Oh, but you like my kind of trouble, don’t you?"
            "He wraps an arm around my neck, clearly expecting no retort."
            "I lean my head onto his shoulder."
            "He’s right, I’ve officially given up resisting. I like nothing more than his kind of trouble."
            l "The magnanimous prince of spiders will take this burden upon himself. Underlings, march!"
            
            #bg hallway beyond
            "We cross over from the hideout, hands linked. I barely feel the world-warping, head-swirling pressure from before."
            "Still, I’m hesitant to let go of Lucifrid’s hand once we arrive."
            "He looks down at our hands, then up at me."
            l "Well, I suppose I’m in no shortage of hands, hehe."
            l "I sensed human life force around here, so with a bit of luck your friend is around."
            "We walk around the beyond in search of Emrys. As always, the hallway stretches endlessly onwards."
            "Still, the air doesn’t seem quite so oppressive. Our spiders scout ahead around corners and into classrooms, but the apparitions we encounter are docile and passive."
            "A question that seems almost forbidden reaches my lips."
            e "Is it really so bad if the worlds converge?"
            l "Oh, {i}now{/i} you’re coming around? This is what things are like for the upper echelons! I told you I’d have you rule by my side!"
            l "Nothing here dares raise a finger to harm us."
            #lucy serious
            l "It’s not too late, you know. You can still—"
            "I wait, but the second half to his sentence never comes."
            e "Still what?"
            l "...Nothing. It’s nothing."
            "I don’t bother prying, casting my eyes down to the floor instead."
            "I know. I know as well as he that there’s no magical solution to any of this."
            "But I can’t stop my brain from scrambling to come up with hopeless ideas."
            "A large spider runs up to us in a hurry. It must have found something."
            "It disappears around a corner and I let go of Lucifrid’s hand to run after it."
            "There he is!"
            "I spot Emrys seated on the floor, blood trailing from his leg. An apparition must have gotten to him."
            em "Edelweiss!"
            "His face flushes with relief when he sees me. He struggles to get up."
            "Lucifrid, having caught up to us in seconds with his superhuman speed, extends one of his arms to him."
            #lucy smug
            l "She couldn’t have found you without me, you know."
            "Emrys begrudgingly takes the arm extended to him."
            em "You have my thanks."
            e "To think I would see a day where you two get along!"
            l "Shush or I’ll let him fall."
            em "...At least one of us was raised with good manners."
            "I let out a sigh of relief. If he has enough energy to retort sarcastically, his wound can’t be that bad."
            e "Sorry about... all of this."
            "He frowns and shakes his head."
            em "I don’t know what kind of mess you’ve gotten into this time but... you’re going to set it right, aren’t you? I’m counting on you."
            "He sternly eyes Lucifrid."
            em "Both of you."
            "I nod at him with a smile, long used to his lectures. The spider prince merely rolls his eyes."
            l "Injured, caught in a hostile place, and still refusing to show respect to the only one capable of saving you..."
            l "Where’s your self-preservation instinct, human?"
            "He makes some hand signals towards a spider battalion, which gathers around Emrys."
            l "The boundary’s weak. These guys will get you across just fine."
            em "Stay safe, Edelweiss."
            l "Quickly now, before I change my mind."
            e "You too! Make sure to go to the nurse’s office!"
            #cut-in effect CG
            "And with that, Emrys is transported back to safety."
            "A heavy silence settles around us again. When I look over at Lucifrid I find him looking at me intently."
            "I breathe in deep. There’s no way around it now."
            e "What are we going to do about the boundary? You know something I don’t, don’t you?"
            #lucy innocent
            l "Hmm..?"
            e "Come on, you’ve been acting strange all day. Don’t think I can’t tell."
            #lucy ominous close up
            l "You want to know? Are you sure you’re prepared?"
            #edelweiss smile
            e "Even if I’m not, there’s no way around it."
            e "It’s the two of us, right? We’re causing the boundary to collapse."
            #lucifrid escalating mania
            l "Ahahaha, yes, isn’t it wonderful? It’s exactly as I predicted! There’s nothing stronger than the two of us together, not even the fabric of reality."
            #edelweiss resigned
            e "The closer we get... the weaker the boundary becomes."
            l "Our very souls are intertwined, aren’t they?"
            "He grips both my hands and entangles our fingers as if to demonstrate. Then he presses himself into me, his face up against mine."
            "His touch is reckless, almost aggressive. But I’m not scared anymore."
            e "You’ll keep your promise, right?"
            l "I don’t recall making any promises."
            e "Neither life nor death will come between us."
            l "Hehe... hehehe."
            l "Never thought you’d hold me to that one."
            "In my head it’s echoing: \"I love him,\" \"I love him,\" \"I love him.\""
            "It’s relentless."
            "It’s unfair."
            "I can’t say it."
            "I shouldn’t say it."
            l "My lovely, dutiful assistant, the only way this world can be restored to normal is by dissolving our contract."
            l "Will you forgive me for breaking my promise?"
            e "No! Not a chance! There has to be another way!"
            e "I thought it wasn’t even possible to dissolve!"
            l "Ah, always reading the fine print, my reliable soulmate."
            l "You’re right. The only way it can possibly be dissolved is by severing your connection to the beyond completely."
            l "I’ll pull it out at the root. Snap our invisible ties irrevocably."
            l "You’ll be a puny, powerless human like the rest of them."
            l "Ahahahaha."
            e "Stop it! Why are you being so cruel?! I don’t—"
            "I stop and look at him."
            "He’s not laughing, or gloating. His face is unbearably sad."
            e "Lucifrid..."
            l "Edelweiss, I’m—"

            #ilya appears
            i "I’ve finally found you. This can’t go on any longer."
            "What? Ilya? How did he get here?"
            "While I’m stuck in my emotional stupor, Lucifrid backs away from me and immediately snaps back into his usual persona."
            l "Come now, can’t you see we’re having a moment? You have terrible timing, exorcist."
            i "How much longer would you like me to wait? How much more havoc do you want to wreak before you’re satisfied?"
            "He places a hand on the hilt of his sword."
            "Wait... his sword?! Since when has he had that?"
            e "Ilya, please, wait!"
            "Ilya turns towards me. At least he’s willing to hear me out."
            e "We’re working out a plan. The boundary’s collapse doesn’t benefit us either!"
            #ilya regretful
            i "Don’t you think it’s a little late for that?"
            i "You know I didn’t want things to turn out this way, Edelweiss. But the two of you have left me no choice."
            i "Don’t be afraid, I won’t harm you."
            e "You don’t understand a thing."
            e "Why would I be afraid of that? There’s a billion things I’m afraid of, but if my pain can help in any way then I will walk up to the chopping block willingly!"
            "I step forward between Ilya and Lucifrid and call upon the tome."
            e "If you mean to attack Lucifrid, you’ll have to get through me first."
            "I don’t want to hurt Ilya... I don’t want anyone to get hurt. But what can I do?"
            "While Ilya stands bewildered for a moment, Lucifrid steps forward and leans in close to my ear."
            "His voice is barely above a whisper."
            l "You can’t do this, Edie. What if you kill him? And for what? It won’t solve our problems."
            e "But— I—"
            "But there’s no time to speak. Ilya rushes at us with his ancestral sword."
            "I try to blot out my emotions and put all my focus into defending us. The tome is here. I know what to do."
            e "Heed the voice that calls, honour the ties that bind."
            "My reliable fire spirit manifests in the blink of an eye."
            e "Use your fire to keep him from reaching us!"
            "While it flaps its wings to whip up a scorching wall of flame, Lucifrid has called his spiders to him and is webbing Ilya in place."
            "We’re only buying time, I know that."
            "I turn to catch my breath, and my eyes meet Lucifrid’s."
            e "There’s nothing we can do, is there?"
            "He shakes his head."
            e "Tell me. Tell me how to do it."
            e "If it has to end then I’ll do it myself."
            l "Come here, my soulmate."
            "I stand face to face with him. The wildly raging world seems to fall away."
            "If I can just look at his face a little longer."
            "If I can just hold him in my arms a little longer."
            "No, none of that would make this any easier to accept."
            "Again, he interlaces his fingers with mine and uses his other arms to press me against the wall."
            "But softly, this time. Gently."
            l "You remember how we made our contract, I’m sure?"
            e "Mm, I do."
            l "It comes undone in just the same way."
            e "It’ll be different this time."
            l "Oh, is that so?"
            l "Pray tell, how might that be?"
            "He grins. He’s asking for answers he already knows."
            e "Because I love you, Lucifrid."
            e "Even once this contract breaks. Even once there’s no way to reach you anymore. We’re still connected."
            e "You don’t have the power to snap those invisible ties."
            l "Edelweiss... How could I have known what meeting you would do to me?"
            l "Look at me! A deity of the beyond, all soft-hearted for love of one human girl."
            l "No one ever told me love would make me weak."
            "I can sense Lucifrid hesitate, the look in his eyes unsure. He’s so close I can feel his breath on my skin."
            "The most indescribable feeling comes over me. I want to kiss him more than anything, but I know that it will be the end."
            e "No one ever told me love would make me strong."
            "I press my body against his and close the distance between our lips."
            "My arms pull him in as if to touch as many inches of our forms together at once."
            "Who knew a boy of such thorny character would feel so soft?"
            "Our lips are careful at first, but the realisation that this is the last chance we have quickly makes us greedy."
            "I bite his bottom lip and he smiles against me, wasting no time in taking me up on the challenge."
            "We struggle against each other rapturously, afraid to squander a single second."
            "For humans and apparitions alike, time progresses in a straight line from past to future."
            "But I’ve been told that time is another dimension, and that perhaps, to someone on the outside, all moments exist in perpetuity."
            "Even if I never reach there, this moment too, is eternal."
            "We break from each other to catch our breaths, and I look at him. I try to memorise every little detail about him, even knowing that it’s futile."
            l "Edelweiss..."
            e "Lucifrid..."
            l "I hereby dissolve the invisible ties that bind us."
            l "Live well, my soulmate, and I will do the same."
            "As soon as he speaks the words, something snaps inside my chest."
            "All this time, I was being held together by something I didn’t know I had."
            "My insides are collapsing, scrambling, desperate and confused by the lack of something intangible yet indispensable."
            "Though my eyes are fixed on him, I can’t focus. I don’t want to blink, but I can’t resist any longer."
            "And when I look up, he is gone."
            "The spiders, the webs, the fire spirit—they’re all gone. Only Ilya remains."
            "My body feels weak. My mind blank."
            "I collapse to the ground, filled with sadness, yet no tears find their way out."
            
            scene classroom evening
            #school bell sfx
            em "Are you coming?"
            em "That essay isn’t going to write itself."
            e "Yeah, yeah, I didn’t forget."
            e "I promise I’ll meet you in the library, there’s just... something I need to do first."
            #emrys smile
            em "Alright, I’ll be waiting."
            "Emrys saunters off, and one by one, the other students filter out of the classroom as well."
            "I look out the window. The wind is still blowing through the bright orange trees. The courtyard is covered in their leaves."
            "Classes continue on. Essays need to be written."
            "Everything is the same."
            "I take a deep breath and heave myself up from my chair."

            scene hallway
            "Leaving the classroom, I make my way towards the staircase then stop in front of it. Something inside me hesitates."
            "I still look around for apparitions as if by habit. Only now, there’s no way to tell if they are there."
            "I thought losing my diviner abilities would feel like losing a limb, but it’s more like setting down a heavy bag."
            "I was carrying it for so long, I forgot how it felt to be without it."
            "As I walk on, the steps creak beneath my loafers. All the way up to the fourth floor."

            #sfx creak
            scene classroom evening
            "The door creaks terribly. I guess no one’s been up here."
            "My chest feels heavy as I look around the room. Everything is exactly as we left it. Why wouldn’t it be?"
            "..."
            "Is it naive to hope for some trace of him here?"
            "I pace around and eventually settle atop one of the desks, hugging my knees for some semblance of comfort."
            #black screen
            "I close my eyes and rest my head on my knees."
            e "Lucifrid... Are you there?"
            #sfx chair squeeking
            #cg with semi-transparent lucifrid
            e "W-what was that?"
            "I look over at the chair he always sat in, but he’s not there. Of course he’s not."
            "But when I look closer, I see something else."
            "A single spider sits in his place, shuffling around almost uncertainly."
            e "Yang?"
            "The spider perks up at my voice, and jumps over to the desk in front of him."
            "I get up and walk towards the desk."
            e "But... how?"
            "I stretch my arm out to him, and he walks up to my shoulder."
            "Spiders can’t give any answers."
            "Something finally gives way inside me, and tears spill down my cheeks."
            e "You’re there, aren’t you?"
            "My voice shakes."
            e "Only the prince of spiders could pull off something like that!"
            #lucifrid hugs edelweiss cg
            #screen pans over it for a moment
            "A faint warmth envelops me, and I find myself smiling through my tears."
            "I’m sure if he could speak to me now, he would be scolding me."
            l "{i}Unbelievable! I give you a gift, and you reward me with tears?{/i}"
            e "...I’ll take good care of him, I promise."
            "I cradle Yang in my hands and walk to the door." 
            "Before I leave, I turn back to the empty room." 
            e "Don’t forget, Lucifrid. Neither life nor death." 
            "The breeze stirs through the open window." 
            "And somewhere, I know, he's smiling."
            return

        "Lucifrid#" if lucy_ending >= 1: #Lucifrid's yandere ending
            "I swallow hard, but fail to stop the anxiety from rising like bile in my throat."
            "There's nowhere for me to run except into the arms of danger, but if that's what it takes to save Emrys, then I will."
            "It's only right for me to be the victim of my own incompetence, but I can't allow it to affect him."
            "There's no way of knowing what will happen if I place my fate in Lucifrid's hands, but this is the path I've chosen. The only path left to me."
            "It's not that moths don't know the flame will burn them, it's that they feel drawn to its warmth all the same. Perhaps not even despite the danger, but because of it."
            "With shaky steps, I make my way towards the abandoned fourth floor classroom."

            #transition hallway
            #sliding door sfx
            #transition abandoned classroom 

            e "Lucifrid?"
            "As soon as I call his name, he manifests atop the desk. He must have been expecting me."
            l "My dearest assistant. Shouldn't you be busying yourself with that school festival?"
            e "There's more important things right now. You... must have noticed something."
            "His casual grin widens, baring his fangs."
            l "I notice many things. Could you be a bit more specific?"
            e "The boundary is fading, Lucifrid! Don't pretend you don't know what's going on!"
            l "Oh, that? Hehehe, I can't believe you're only noticing it now. It's been slipping away bit by bit for a long time now."
            #edelweiss shock
            e "..."
            #edelweiss downcast
            e "A-are you serious? You knew all this time?"
            l "Mm-hmm."
            l "I had my suspicions since the library incident. But what did you want me to do?"
            "I don't know why I expected him to be anything but nonchalant about this, but still his attitude gets under my skin."
            "Time and again I expect him to change. To be different. To be better. And time and again I'm the one who ends up hurt in my disillusionment."
            "Why do I still hold on to that hope? Is it easier to abandon myself to a lost cause than to admit that I was wrong?"
            "Well, I'll admit it. I was wrong. But it's too late to choose differently now."
            e "I don't get you! There's no way this benefits you! There'll be nowhere for apparitions to hide from exorcists or any other threats."
            #lucy serious/ominous
            l "Edelweiss. What did you want me to do?"
            #lucy dark smile
            l "It's you and me. We're such a devastating combination that we're causing this whole world to crumble. Isn't that romantic?"
            l "I wasn't lying before, much as you continue to distrust me."
            l "Neither life nor death shall come between us."
            e "You even knew the cause?! Did you know this would be the outcome from the very day we met?"
            e "How can I trust you when you don't even tell me anything?"
            l "What good would have come of it?! If everything's going to collapse and you're powerless to stop it, wouldn't you rather live freely until the moment it does?"
            "I bite my thumb. Fuck. Isn't that the exact same logic I was using to justify not addressing this?"
            "What's wrong with me?"
            e "...You're right. You're right and I'm a hypocrite. I'm all talk of lofty ideals but I can't do a thing to back them up."
            e "Ilya told me all this would happen and I never said a word to you."
            "He gets up and moves towards me. I freeze, unable to read his expression."
            "Then he wraps his four arms around me and rests his head on my shoulder. His hushed breath tickles my ear."
            l "Don't you worry now, it's alright. I've accepted all your flaws. Because you are mine."
            "The arms around me don't change their weight or force, but they feel tighter. I can't go anywhere."
            l "You can curse me, distrust me, struggle all you want. It's alright. No matter how far you fall, how dark your soul gets, I'll take care of you."
            "Should I stop resisting? Should I fall into his embrace and forget about everything?"
            "Before I know it, tears are forming in my eyes."
            e "P-please help... I can't do anything without you, Lucifrid."
            e "Emrys disappeared in the convergence, if nothing else, please, let's save him."
            "As he speaks, he moves one arm to stroke my hair."
            l "Of course. We'll find him, and I won't stop there. I'll undo the convergence."
            e "B-but how?"
            l "Don't worry about it, I've got a plan. You just have to trust me."
            "He lifts his head to look at me and loosens his grip."
            l "Will you trust me?"
            "Do I trust him? How could I know? As much as I'd like to claim I know who he really is, there's precious little I understand about Lucifrid."
            "I'm going to drown in those vermillion eyes, there's no way around it. The only choice that rests me is whether to accept it, or fight until the bitter end."
            "And I'm tired of fighting."
            e "Alright, I'll trust you."

            #transition hallway beyond
            l "I sensed human life force in this area of my domain. It's no guarantee, who knows how many students have stumbled their way over here, but it's our first lead."
            "I nod at him nervously."
            "The journey from the light side to the dark side of the boundary has become less arduous than ever. Whether I've grown more experienced, or it's simply a result of the boundary fading, I don't know."
            "The world around us shakes and contorts as usual, but this time every little movement has me searching for a trace of my assistant."
            "Suddenly, I hear footsteps from somewhere up ahead."
            "Lucifrid motions me to be quiet and we hide around the corner of a darkened classroom."
            "Voices echo from nearby, but I can’t make out the words." 
            "Wait, I would recognise that voice anywhere! It’s Emrys!"
            "But who is he speaking to?"
            "I peek around the corner. Is that... Ilya?"
            l "It’s that exorcist vermin, isn’t it?"
            "He scoffs."
            l "No matter, he’s no match for my current form." 
            "I don’t think it’s overconfidence. The very air bends to his will now, the entire beyond singing praises at his feet."
            "The boundary’s weakness is Lucifrid’s strength."
            "He walks out into the hallway and I follow just a step behind."
            l "You, exorcist. Step away from the boy."
            "The two of them turn to us and for a moment we are suspended in silence. A deadlock."
            em "Edelweiss, Lucifrid! Don’t worry, Ilya was just helping me find my way back. We can resolve all of this peacefully."
            "I form a wry smile at Emrys’ attempt to defuse the tension."
            "It’s too late for that now. He knows it too, but he can’t stop himself from trying."
            i "No, we can’t. You don’t understand—these two are the cause of all of this."
            "Ilya fixes his eyes on us."
            i "And I doubt they’re about to give in willingly."
            "He reaches for his sword, no doubt one of his family’s relics."
            #sword unsheathing sfx
            e "...!"
            e "Stop this! We have the same goal! Lucifrid has a plan to undo the convergence, isn’t that what you want?"
            i "Hah. You want me to trust him? You’re blind, Edelweiss. You’ve been completely taken in by him."
            "For a split second, he looks almost forlorn."
            i "I didn’t want this for you."
            l "Hehe... hehehehe!"
            l "Amusing as the melodrama may be, can we get to the point? I’m losing my patience."
            i "..."
            "Not a single second spared, Ilya grips his blade and rushes forward."
            "There’s nothing I can do. This outcome was inevitable."
            l "Edelweiss, behind me. Call upon my tome."
            "He wants me to... fight Ilya?"
            e "I-I can’t do that! He’s still human!"
            l "Hehe, well, I thought you would say that."
            #slash animations and sfx
            "Lucifrid dodges Ilya’s attacks nimbly, while coating the room in his sharp threads." 
            "I look over at Emrys. Shouldn’t he get out of here?{w} ...I suppose if it were me, I wouldn’t leave him alone either."
            #slash animations and sfx
            "Ilya gets a hit in on Lucifrid. Red spills from a cut on his cheek."
            l "What are you trying to do, little human?"
            l "Let’s say you exorcise me, what do you think will become of Edelweiss?"
            "His voice is lilting and playful, absolutely unconcerned."
            l "She’ll face a fate worse than death, alone in the beyond! You’ll be dooming the one you’re trying to protect!"
            "Ilya grits his teeth. He doesn’t address the spider boy. That’s beneath him."
            "Lucifrid turns to me."
            l "Can you shield me for a moment?"
            "I nod and follow his command."
            e "Heed the voice that calls, honour the ties that bind."
            "A spider squadron scuttles forth from the tome. I command them to weave a web to block Ilya."
            "The exorcist responds by chanting an incantation. His sword lights up."
            "Then the blade is set ablaze. It tears through the webs with ease."
            "I didn’t know he could do that..."
            "The spiders rush in on him but he shakes them off and lunges at Lucifrid."
            i "Edelweiss, look at him! Is this the creature you want to protect?!"
            i "Open your eyes! It’s never too late to make the right choice!"
            "It is, Ilya. It is. I don’t have the will to fight this anymore."
            #spider hybrid lucy cg
            "When I look over at Lucifrid, he is no longer the boy that I knew."
            "His face is unchanged, but his top half is unclothed; skin hard and glossy, melded into chitinous armour."
            "Below the waist there is not even the semblance of humanity left. All hard shell and squelching joints. Arachnid anatomy where there used to be flesh and bone."
            "Somehow I find myself unable to look away. I’m mesmerised."
            "He’s a monster. A beautiful, horrifying monster."
            "The demon was never Lucifrid. It is the part of me that saw this conclusion coming, and still ran towards it."
            "The part of me that doesn’t distinguish between fear and love. The part that equates them."
            "And it won."
            #slash animations and sfx
            "I’m frozen in place as the battle continues before me."
            "Ilya is holding out, but he’s growing tired. I can tell."
            l "Edelweiss, close your eyes."
            "Before I can process his command, before I can even blink, Lucifrid closes the distance."
            "Wait— That’s not— Emrys?!"
            "He screams."
            "Ilya throws himself in front of my best friend and a horrible,{w} wet{w} crunch resounds."
            "I want to close my eyes, but I can’t."
            "My heart pounds intolerably."
            "My throat feels too strained to even breathe."
            i "...hrgh..."
            "He’s alive."
            "He’s alive!"
            "And Emrys— Emrys is safe."
            "Everything is okay. It’s okay. It’s all okay."
            em "Edelweiss, y-you can’t stay with that thing."
            em "Save yourself."
            em "Edelweiss!"
            l "Now, now, don’t get upset. I wasn’t {i}trying{/i} to hurt you!"
            l "This all went exactly according to plan."
            "Emrys is quivering. I wish I could take away his fear."
            e "Calm down, Emrys. You’re safe!"
            e "He wouldn’t hurt you. He promised me he’d save you!"
            "Lucifrid smiles at me so gently. It’s all okay."
            l "Now, Edie, time for the final step in our plan."
            l "Have you figured it out, the solution to the convergence?"
            l "A bond between a powerful spiritual life force belonging to the human realm, and a deity of the beyond."
            l "Something has to give. There is no happiness without sacrifice."
            "He reaches out his hand to me."
            "I think I know where this is going. But I don’t need to ask him, I only need to take his hand."
            "So I do."
            e "Thank you... for rescuing Emrys. For saving this school."
            "He pulls me closer, then lifts me up in his arms effortlessly. I cling onto him feverishly."
            l "Hold still now. This will hurt just a little bit, but then it’ll all be better."
            e "Lucifrid, I’m scared."
            l "Shh, you’ll be okay. I’m with you."
            l "Neither life nor death shall come between us."
            #screen black
            "I close my eyes."
            #sfx slash/crush idk
            #sfx gasp inhale
        

            #sfx school bells
            scene hallway
            #silhouette sprites displayed
            "As always, I watch the students filter out of class 2C at the end of the day."
            #emrys appears
            "My eyes look for him involuntarily. When I catch a glimpse of him, his face calm and composed, I smile."
            "He moves closer, walking towards me, but he doesn’t look at me."
            "He walks through me, then stops and lingers, looking back to where I stand." 
            "He does not see me."
            em "Edelweiss?"
            e "I’m here."
            "I know he can’t hear me. But maybe I can impress the slightest bit of comfort upon him all the same."
            "He shakes his head and keeps walking. I know his destination."
            "Still, I pause before entering."
            #bg student council room
            #emrys sprite
            "The interim student council vice president takes place behind his desk and works through a stack of papers."
            "He always was dutiful, and I suppose he feels responsible for what happened to... him."
            "..."
            #lucifrid appears
            l "I knew I’d find you here. Come, are you done reminiscing?"
            #edelweiss laugh
            e "Oh, are you jealous of a boy who can’t even see me now?"
            "He pulls me close."
            l "No, how could I be?"
            l "You chose me."
            #cg of edelweiss and lucifrid as apparition royals
            "I barely notice the world around us giving way, replaced by my new home."
            "Lucifrid seats himself on his throne, and I take my place beside him."
            "Here, every atom moves in blissful obedience to his will."
            "I can hardly remember what things were like before his rule. It feels like every day, I forget a little more."
            "Is there a greater joy than losing oneself in the person one loves?"
            "I give him all my fear, and he returns his love."
            e "Lucifrid?"
            "He turns to me with a tender look."
            l "Yes, my queen?"
            "I wanted to ask something, but the thought slips away."
            e "No, it’s nothing."
            "I rest my head on his shoulder and close my eyes."
            "It must not have been important."
            return

        "Ilya" if ilya_ending >= 1:

            "I’m so tired of being caught in Lucifrid’s web. No matter what I do, I’m nothing but a pawn in his game."
            "I’ve followed his plans over and over, and yet he refuses to see me as an equal."
            "More and more, I find myself wondering if Ilya was right from the start."
            "No good ever comes from getting involved with an apparition. All diviners know this."
            "Then why didn’t I heed it?"
            "Did I even have a choice?"
            "Well, it doesn’t matter. What matters is that I have a choice now, and I won’t let Lucifrid convince me otherwise."
            "I won’t be his pawn."
            "I won’t."
            
            scene hallway

            "I move with hurried steps towards the student council room."
            #sfx knock
            #sfx sliding door
            #bg student council room
            #ilya taken aback
            i "Edelweiss."
            i "Can I... help you with anything?"
            e "I..."
            "My voice wavers, barely audible. I clear my throat and try again."
            e "I was hoping you could."
            "His face falls into his practiced, gentle smile."
            i "Take a seat. I’ll make us tea."
            e "I- I don’t know if we have time for that."
            i "Quite the opposite, the tea is necessary."
            i "You’re in a panic. You won’t be able to get anything done in that state."
            "My anxiety conjures a sharp-tongued response, but it doesn’t make it past my lips. Perhaps he’s right."
            "I sit down on the couch. I can’t settle." 
            "I play with my shirt sleeve, unbuttoning then buttoning the cuff. Then unbuttoning it again."
            #sfx place cup
            "He places a cup of tea on the table and sits down on the opposite end of the couch."
            i "I hope this will calm you down."
            i "Can you tell me what’s going on?"
            "I take a deep breath. In, then out."
            "He’ll listen. He won’t get angry."
            e "I-it’s as you said. I think. I don’t know."
            e "The boundary is fading, probably. I opened the door to the storage room and it wasn’t the storage room. It was the beyond."
            e "A-and, Emrys, he got lost! He’s my best friend, you see, I need to save him."
            e "But not just that of course, I mean, who knows who else has gotten involved?"
            e "I’m just worried, and it’s all my fault, isn’t it? And Lucifrid too. Lucifrid too... I suppose."
            "I keep stumbling over my words. I feel so stupid I just want to cry."
            "But Ilya listens patiently until I’ve gotten everything out."
            i "It’s alright Edelweiss, it’s not too late. You couldn’t have known what you were getting into."
            i "I always said I would help you. I’m glad you could trust in the truth of my words."
            i "Don’t worry, I can take care of all of it. You can leave it in my hands."
            e "Is it really not my fault?"
            e "Ilya... Tell me the truth."
            "My eyes fix on him expectantly. My breath is erratic."
            "There’s not enough air in the room. Not in the entire world, it seems."
            i "It’s not your fault, Edelweiss."
            "Ilya knows everything, and yet, he’s not judging me? I don’t understand."
            "Tears blur the corners of my vision but I try to steady myself."
            "I want to lean into him. To leave myself in his hands.{w} He said it, right?"
            "He said it."
            "I move closer and bury my face in his chest."
            "I can’t see his expression. He doesn’t say anything, but he doesn’t push me away."
            "His heart betrays him, pounding frantically against my cheek."
            "Growing embarrassed, I pull away."
            e "S-sorry."
            #ilya blushing
            i "No, it’s... it’s okay."
            "He grips my hand and squeezes it. It hurts, but I do feel a bit lighter."
            e "...What should I do?"
            "Ilya lets out a deep breath and continues with regained composure."
            i "The contract has to be dissolved, that’s the only way to restore the boundary. Emrys will be returned to us as soon as it’s back."
            e "Can I do that? Lucifrid said something about—"
            i "You don’t have to do anything. I’ll take care of it. All I need is for you to trust me."
            i "I’ll confront that spider and end this once and for all."
            e "...Okay."
            "The word comes out before I can stop it. Before I can consider what I’ve agreed to."
            "All that washes over me is relief. I don’t have to think about any of it anymore."
            "Whether it’s right or wrong, the decision has been made."
            "And Ilya is here beside me."
            "I look up at him and finally see what they all see in him. He really does look like a fairytale prince."
            "And I have the privilege of causing the creases in his vest."
            "He isn’t like Lucifrid."
            "He doesn’t see me as his possession. He’s gentle. Kind."
            "But the look in his eyes... is strangely cold."
            
            scene hallway
            "Ilya needed time to prepare, and involuntarily, I find myself outside the fourth floor classroom."
            "I should tell him. I should warn him Ilya is coming."
            "But my hand won’t move."
            "I’m afraid.{w} Afraid he’ll make me doubt everything.{w} Afraid he’ll drag me back in."
            "I don’t hate him. I don’t hate him at all. I hate that I don’t hate him."
            "That’s why I can’t face him."
            "I can’t tell how long I’ve been hovering outside the hideout when Ilya approaches me and puts his hand on my shoulder."
            "Though I hear him coming, I’m startled. I try not to let it show." 
            "There’s an impossibly warm comfort in his touch. Deliberate, not casual. I want to savour it."
            i "He’s here, isn’t he?"
            e "Should be."
            "I smile at him, though it feels forced."
            e "Thank you for not giving up on me, Ilya."
            i "Save the thanks for when we’re done here."
            "I examine Ilya. He has a sheathed sword strapped to his back, and is holding a veritable mountain of paper talismans."
            e "Can I help with anything?"
            i "Help me affix these to the doorframe."
            "As we make our preparations, my mind wanders. I guess I won’t be seeing Yang and the others again."
            "It’s alright. It’ll be alright. I can leave it to Ilya."
            scene hideout
            "When we’re done, I enter first."
            "Classes ended less than half an hour ago. It’s around the time Lucifrid and I usually meet, and as expected, he appears when he senses me."
            l "Now what have we here, are the two of you ganging up on me?"
            "He grins, but there’s no amusement in his voice."
            "Ilya unsheathes his sword and I can’t bring myself to say anything."
            l "This is a joke, right? You led him here for me to defeat, Edelweiss? Would’ve appreciated the heads-up."
            i "You’re wrong. {i}I{/i} will be the one to defeat {i}you{/i} and restore order to this school."
            l "Shut up. I’m not talking to you."
            l "Edelweiss, look at me."
            "His voice sounds almost desperate. I was expecting anger, fury—not... this."
            "So I look at him with resigned eyes. It’s all I can do."
            "This is no longer my fight. I’ve already made my choice."
            l "You don’t need him. Whatever he told you, it’s all lies."
            l "We could have solved this together."
            "I feel a lump in my throat."
            i "Don’t listen to him. He’s trying to manipulate you now that he’s at a disadvantage. You made the right call."
            e "I’m sorry."
            l "Ahahahaha. Ha. Ha. Ha."
            l "Hilarious."
            l "Oh, I should’ve known from the start that this is how it would be."
            l "Come then, exorcist. Give it your all."
            "I can’t do anything but cower in the corner. I’ve never seen Lucifrid like this."
            #attack screen/sfx
            "He spins his webs and sends out his spider battalions. Yang isn’t among them."
            "Ilya readies his blade. Flames emanate from it as he chants an incantation."
            "Whenever Ilya moves in with his sword, Lucifrid bites at him."
            "But I can tell... he’s not fighting for his life."
            "Lucifrid tries to create a bit of distance to allow him the time to manifest his tome, but Ilya’s attacks are relentless. They won’t let him."
            "No, he’s trying to make it look convincing, but he already knows he won’t win."
            #attack screen/sfx
            "Then the blazing blade reaches its target and slices one of Lucifrid’s four arms clean off."
            "The smell of burning makes the bile rise in my throat."
            l "Ahahaha! Is that all you’ve got? Why don’t you come and finish the job?"
            "Ilya remains stoic in the face of his taunting."
            "Despite his arrogant tone, Lucifrid is noticeably weakened."
            "Why isn’t he cursing my name? I’m the one who did this to him."
            i "Your reign ends here."
            i "Light unto light, dark unto dark."
            i "From nothing thy comest, and to nothing thy shalt return."
            "Lucifrid is cast to the ground. His spiders scatter."
            "He looks right at me, wearing the hint of a smile."
            "I try to speak but my throat goes dry."
            "I’m sorry. I didn’t know. I didn’t know this would happen."
            "No, that’s naive. I’m so hopelessly naive. Did I really think any peaceful resolution would come of this?"
            "I did this to him. I condemned him."
            "So why isn’t he condemning me?"
            i "Light unto light, dark unto dark."
            l "Be well, Edelweiss."
            l "I hereby dissolve the invisible ties that bind us."
            "Something snaps behind my ribs—a thread I didn’t know was holding me together, severed clean."
            "Now that it’s gone, my chest collapses, leaving nothing but a sudden emptiness. Dark and heavy."
            i "From nothing thy comest, and to nothing thy shalt return."
            "He screams out and burns up, like the apparition in the courtyard before."
            "A real exorcism."
            "But it all goes faint and blurry. I can’t sense the presence of the beyond anymore."
            "My body collapses like it’s nothing but a bag of bones."
            "Ilya doesn’t look affected. Is he tormented by the weight of what he has done? Is he triumphant over the defeat of his nemesis?"
            "His face doesn’t reveal a thing."
            "He sheathes his sword when it’s all done, and walks towards me."
            i "I’m proud of you, Edelweiss. You didn’t falter."
            "Proud. What a disgusting word."
            "There’s nothing to be proud of here. Though I let someone else do all the dirty work, my soul is squalid all the same."
            "But it’s over now."
            "I can’t move or speak. I just want to rest."
            i "Here. Let me help you."
            "Ilya lifts me in his arms and holds my limp body against his."
            "There is warmth here."
            "All else may be gone, but this warmth alone remains."
            e "...Don’t let me go."
            i "I won’t."
            e "Promise."
            i "I promise. I’ll never let you go."
            "I rest my head against his chest and close my eyes."
            "His heart beats violently."
            
            scene classroom evening
            #sfx school bell
            #sfx voices
            "..."
            em "Earth to Edelweiss! Class is over."
            e "...Hm?"
            em "You’re free to enjoy your afternoon!"
            e "Oh. Right. Sorry."
            em "Don’t apologise..."
            "He pauses."
            em "You know, I’m a little worried about you lately. I know you say you’re happy about it but..."
            em "Don’t you miss being a diviner?"
            em "You never even had the chance to say goodbye to Lucifrid, did you?"
            "I don’t answer."
            em "...Sorry, I shouldn’t have brought it up."
            #ilya appears
            "Classmate" "Vice president Ilya! Is there anything I can do for you?"
            #ilya gentle
            i "No need, I’m here for Edelweiss."
            #edelweiss happy
            e "Ilya!"
            "I jump up from my seat and move past Emrys towards him."
            i "I’ve come to escort you home."
            "He takes my hand and raises it to his lips, pressing a chaste kiss upon it."
            e "I was waiting for you."
            i "Then let’s not tarry."
            "He doesn’t let go of my hand as we walk out of the classroom, intertwining our fingers instead."
            "Classmate" "Oh, I can’t believe it! I’m so jealous!"
            "Classmate 2" "She must be the luckiest girl in the whole school..."
            scene hallway
            "I don’t look back."
            "The only comfort I have is the warmth of his touch."
            "The only guidance I need is his hand pulling me onward."
            e "What are we doing this weekend?"
            i "They’ve just displayed the winter illuminations at the theme park a few stations over. I got us tickets."
            e "That sounds lovely."
            i "Don’t forget to wear the scarf I got you. They say the temperature will drop near zero this weekend."
            e "Of course. Thank you again for the thoughtful gift."
            i "Think nothing of it. It’s my duty to look after you."
            e "I love you, Ilya."
            i "..."
            "He hasn’t said it back yet. But I know he loves me."
            "I feel it in everything he does."
            "Right when we reach the school entrance, I see something crawling out of a corner."
            "A spider."
            "Before I realise it, I’m moving towards it, reaching out my hand."
            "My fingers are inches away when—"
            "Ilya must not have seen it. His boot comes down with a squelch."
            "He squeezes my hand, and I turn back towards him."
            i "I love you too, Edelweiss."
            return

        "Myself#" if bad_ending >= 1:
            "No! I refuse to let Lucifrid solve all my problems again."
            "Isn’t it about time I become a diviner Mother and Father can be proud of?"
            "{i}I{/i} will be the one to save Emrys, and we can come up with a plan to save the school together."
            "Lucifrid is better off without me anyway, even if he doesn’t agree. We spell nothing but bad news for one another."
            "I have to do this."
            "I have to prove myself."
            "If nothing else, I author my own disaster."
            "I get up from my chair and leave the classroom. A classmate’s voice echoes, but the words don’t even register."
            "My goal is singular. I will find Emrys and bring him back."

            scene hallway
            
            "Once again I stand before the storage room door, shaking. My hand trembles as it reaches out."
            "Stop it, Edelweiss. Stop it! Stop letting your irrational nerves have such power over you!"
            #sfx sliding door loud
            #sfx footsteps
            "It’s fine. I’m a diviner. I have my staff and my wits, the beyond is no match for me."
            "Mother, please, watch over me..."
            #bg hallway beyond
            "There is no stomach churning or vertigo to mark the crossing this time, but I can’t say I feel at ease. The boundary has been reduced from a reality to a word."
            #sfx bells
            "As I walk on, I hold my belled staff out in front of me; its chime both a balm to my nerves and a signal to Emrys— I am here."
            #bg hallway beyond
            "I hear laboured breathing coming from one of the classrooms up ahead. Could it be...?"
            "I walk over slowly and quietly, keeping my staff still, and peer inside."
            "Just an apparition. Best move on before it spots me."
            #sfx bells
            "So I keep walking, and walking. My heart sinks with each step."
            "I can’t recall the last time I felt so alone."
            #bg hallway beyond
            #sfx crash
            "...What’s that?!"
            "I turn around with a start."
            #emrys wounded cg?
            "Emrys!"
            "He’s on the floor, blood trickling down his forehead, and a shadowy figure looms over him."
            "I rush over and shake my staff in time with the syllables of my chant."
            e "Light unto light, dark unto dark!{w} Light unto light, dark unto dark!"
            "The shadow dissipates quickly. Thank goodness it wasn’t more powerful."
            em "My reliable hero."
            "He laughs weakly."
            "I crouch down beside him to assess the damage, taking a handkerchief from my pocket and wiping the blood from his forehead gently."
            e "I’m so glad I found you."
            "Emotion wells up in my throat, but I force it down."
            e "Are you hurt anywhere else? This wound doesn’t seem too deep at least."
            em "It’s nothing too concerning."
            e "What isn’t?"
            em "Moving my arm... hurts."
            e "...How much does it hurt?"
            em "Well, it’s probably more correct to say the pain prevents me from moving my arm entirely."
            e "Emrys! That’s {i}obviously{/i} concerning! We have to get you out of here!"
            "Emrys smiles at me apologetically. He’s always been like this, downplaying his own needs."
            "It’s almost like the more trouble he gets into, the more caring and self-effacing he becomes."
            e "But how did this even happen? That shadow spirit wasn’t that strong, surely it couldn’t have done that."
            em "No, you’re right... I was running away and it merely took advantage of my weakness."
            e "If some indiscriminately aggressive apparition is roaming around freely, we have to stop it! With the school as it is now, everyone will be at risk!"
            em "..."
            "He seems hesitant to speak of whatever did this to him. It must have been terrifying."
            em "So how do we get back? This is the beyond, right?"
            em "Heh... never thought I’d get to experience it like {i}this{/i}."
            e "Uh, yeah, about that..."
            em "You don’t know."
            e "I don’t know."
            "He laughs heartily, then grasps his arm in pain."
            "I can’t help but laugh a little too."
            em "Well, there’s no point staying here."
            #sfx footsteps
            #bg hallway beyond
            "Reunited, we turn back the way I came, hoping we can exit the way we came."
            "This is the part where my plan falters."
            "Honestly, somewhere inside, I didn’t believe I’d find Emrys at all. That it’d be pointless to think beyond that point."
            "Lucifrid will probably find me at some point. That nagging knowledge is more of a burden than a blessing."
            "I don’t want him to find me. I want to finally do something useful by myself."
            "But I hate that I’m still comforted by the fact."
            "I keep thinking I hear footsteps trailing behind us, but it must be my mind working in overdrive."
            "If Lucifrid had found me, he wouldn’t be hiding himself."
            "I try to distract myself by talking to Emrys."
            e "Can you tell me about the apparition that attacked you? In case we do encounter it, I mean."
            em "Hmm..."
            "He sighs softly."
            em "Yes, that might be for the best."
            em "It’s... dangerous because it doesn’t appear to be."
            em "It lures you in sweetly, tries to trick you."
            em "But you can’t grow soft. You have to attack it while it cries for mercy."
            "He looks at me solemnly."
            em "...Can you do that?"
            "How strange, there’s never been an apparition like that."
            "The tactic seems almost... human."
            e "Well, knowing about it beforehand should help."
            em "Just know that it’s fine to run away too. I don’t want to see you get hurt."
            #bg hallway beyond
            "The scenery repeats itself and we seem neither closer to nor further from our destination."
            "I don’t even know how much time has passed."
            "Then, light seems to glow from up ahead. I hear a human voice."
            e "Are we crossing back into the light side?"
            "I run forward."
            em "Edelweiss, wait! Be careful!"
            "I stop abruptly."
            "Light fills the hallway we stand in and overwhelms my senses."
            "I don’t know what I am seeing."
            e "M-Mom?"
            #mom sprite appears on screen
            "Mom" "Edie... It’s been so long..."
            "Mom" "I can’t believe you’re really here in front of me."
            "Mom" "Come here, let me hold you."
            em "Edelweiss, don’t trust her! I... I don’t think that’s your mother."
            "My mind races as I’m frozen in place. How is this possible?"
            "Mom" "I’m sorry, my sweet. I understand that this is hard to believe. Ask me anything, I’ll answer you."
            e "Mom... How did you end up here? Are you really alive?"
            em "Please, get away while you can!"
            e "Forgive me Emrys, I have to know."
            "Mom" "What did they tell you about my passing? Did they tell you anything at all?"
            e "I... I was told you got into an accident. I was too young for the details."
            "Mom" "I suppose they couldn’t have known. They never found my body, because there wasn’t one to be found."
            "Mom" "I passed from the realm of the living, and was confined to the realm beyond instead."
            e "...!"
            e "S-so all those times I felt like I was talking to you, it was really you?"
            "She smiles knowingly and nods."
            "Mom" "You formed a connection to the beyond when you contracted with the spider boy, and the stronger your bond got, the more I was able to reach out to you."
            "Mom" "I was so happy when you confided in me about your troubles. It has made all these long, wandering years worth it."
            e "E-Emrys, it has to be her. There’s no way any apparition could know these things."
            "He keeps silent. Perhaps he knows nothing he can say will influence me now."
            "But there’s one more thing I need to ask."
            e "Mom, are you... proud of me?"
            "Mom" "Oh my dear Edie... I will always be proud of you."
            "Tears well up in my eyes as I close the distance to my mother and let her hug me."
            "What does it matter if she’s an apparition or a human? She’s still my mom."
            e "I missed you. I missed you so much... I’ve been so alone!"
            "She wraps her arms around me. The warmth feels deeply familiar."
            "Mom" "Don’t you worry. You’ll never have to feel alone again."
            "Mom" "We can stay together..."
            #mom’s mask cracks
            "Mom" "Forever."
            "A terrible, dark energy spills out from her at that moment."
            e "H-huh?"
            "When I look up at my mother, her face is cracked, broken. {i}Something{/i} peeks out from behind."
            "Something black as dirt."
            "Something horrible."
            "I try to wrest free from her grasp as tendrils of black begin to burst out from her and slash at me."
            "But her grip is too strong."
            "I don’t know what to do."
            "They’re closing in!"
            #screen flash
            #shake
            "No tendrils reach me. I’m violently flung backwards instead."
            "Pain sears through my body, but I’m alive."
            l "I never took my assistant for such an idiot."
            l "But there’ll be time to lecture you later. Now summon my tome."
            "He doesn’t even sound angry, just tired."
            "It hits me like a jab to the stomach and I seize up, unable to move or even breathe properly."
            "Idiot. Idiot. Idiot. Idiot."
            "I can’t even form a coherent thought under the crushing weight of guilt."
            "Lucifrid is fighting that {i}thing{/i} that I can no longer tell is my mother or not."
            "And he is losing."
            "Bleeding."
            l "Edelweiss, don’t just lie there, do something!"
            "I try to clear my mind and focus."
            "But I can’t."
            "I can’t do it. I can’t do anything."
            "I don’t want to be here. I just want to fall off the face of the earth."
            "I can’t do it."
            "I can’t."
            #ilya appears
            e "...!"
            "For a split second I feel relief at the sight of the exorcist."
            "But that is soon replaced by a further deepening dread."
            i "Light unto light, dark unto dark. From nothing thy comest, and to nothing thy shalt return."
            "He repeats his chant."
            "His face is horribly calm."
            "There’s nothing there."
            "I scramble to summon the tome."
            "Come on, appear! Appear!"
            "A shape begins to manifest, but soon dissipates."
            "I try to throw my whole body into Ilya in a last hope of stopping him."
            "But even that fails when I trip and fall flat on the floor in front of him."
            "I prop my head up just in time to see black tendrils pierce Lucifrid through."
            "I wish I never asked myself if apparitions bleed."
            i "Light unto light, dark unto dark. From nothing thy comest, and to nothing thy shalt return."
            e "Mom... Lucifrid..."
            "The both of them are cast to the ground, wailing."
            #screen black
            "I squint my eyes shut but it just worsens the sounds."
            "I press my hands to my ears but it doesn’t end."
            "I can feel the crackling heat when they burn."
            "I can smell the smoke."
            "And then there’s nothing left of them."
            "Not even ashes."
            "..."
            "..."
            "My pain is gone."
            #bg hallway beyond
            "The hallway is still. My mind is still."
            "When I get up, my head doesn’t spin. My breath doesn’t falter."
            "No, I do not breathe."
            "Spiders spill from their hiding places towards me."
            "They await my command."
            return
