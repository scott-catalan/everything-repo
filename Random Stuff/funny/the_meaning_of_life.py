'''
# Project Creation Date: 9:18:15 PM, 2/12/2026
'''

import random, time

def texter(text, t):
    for i in text:
        if i == "=":
            time.sleep(0.7)
        elif i == "-":
            time.sleep(0.15)
        else:
            print(i, end='', flush=True)
            time.sleep(random.uniform(0.04, 0.1))
    if t:
        print()
    
def dramatexter(text, t):
    for i in text:
        if i == "=":
            time.sleep(1.5)
        elif i == "-":
            time.sleep(0.3)
        else:
            print(i, end='', flush=True)
            time.sleep(random.uniform(0.12, 0.17))
    if t:
        print()

def chaos():
    text = """\nWizard: Then hear this... and listen well, young wanderer, for the truth you seek is older than stone and sharper than steel. 
    Life is not a path neatly paved with answers, nor a scroll that can be read once and understood. 
    It is a crucible, a test of choices, courage, and cunning. 
    Each step you take leaves a mark, unseen yet lasting, shaping the world and yourself in ways you cannot yet fathom. 
    You will stumble, you will falter, but even failure is a teacher, harsh and unyielding. 
    The meaning of life… is to carve purpose from the chaos, to fight your battles not for glory, 
    but for understanding, to light a candle in the darkness, however faint it may burn. 
    Seek, yes, but know this: the quest itself is the answer, and the wisdom you earn along the way is the true treasure. 
    Guard it, wield it, and do not squander the gift of your own fleeting spark."""
    angrytext = ""
    chaos_chars = [
        "⸘", "⸚", "⸮", "⌬", "⌖", "⍟", "⨀", "⨂", "⨌", "⩚", "⩛", "⪧", "⫯", "⭑", "⭒", 
        "⸴", "⸵", "⸸", "⸹", "⸺", "⸻", "⸼", "⸽", "⸾", "⸿", "⹀", "⹁", "⹂", "⹃", "⹄",
        "⌇", "⌈", "⌉", "⌊", "⌋", "⍈", "⍉", "⍊", "⍋", "⍌", "⍍", "⍎", "⍏", "⍐", "⍑", "⍒"
    ]
    severity = 0.0
    increment = 1/len(text)*2
    for i in range(len(text)):
        pr = True
        choice = random.random()
        rand = random.random()
        
        if choice > severity:
            angrytext = text[i]
        else:
            if choice > (0.5 + increment * 3):
                angrytext = text[i].upper()
            elif choice < (0.5 - increment * 3):
                angrytext = text[i].lower()
            else:
                angrytext = text[i]
                if i > len(text) / 2:
                    angrytext += random.choice(chaos_chars)
                if rand > (0.4 - increment * 3):
                    for i in range(random.randint(1, int((i / 5)) + 1)):
                        rand2 = random.random()
                        angrytext += random.choice(text)
                        angrytext += random.choice(chaos_chars)
                        if rand2 > 0.8:
                            print()
                        print(angrytext, end='', flush=True)
                        angrytext = ""
                        time.sleep(0.05)
                    pr = False
        if pr:
            print(angrytext, end='', flush=True)
            
        time.sleep(random.uniform(0.01, 0.2))
        severity += increment

def scene():
    texter("You: =(collapsing, -coughing) =I… -I’ve come… -for the meaning… -of life.", True)
    time.sleep(1.5)
    texter("Wizard: =(calm, -voice like gravel) =All for-.-.-. what, =", False)
    dramatexter("c -h -i -l -d-?", True)
    time.sleep(2.5)
    texter("You: =(voice cracking) =For this… -moment… -for an answer I can’t live without.", True)
    time.sleep(1.5)
    texter("Wizard: =(arches an eyebrow) =And you think the meaning of life is something you can find-.-.-.- in a single word-.-.-.- in a single breath?= F-o-o-l-i-s-h-...", True)
    time.sleep(1.5)
    texter("You: =(shaking, -desperate) =I-.-.-.- don’t care about words… -I don’t care about riddles… -I’ve lost everything else. =I’ve lost-.-.-.- myself. =Just… -tell me.", True)
    time.sleep(1.5)
    texter("Wizard: =(leans back, -studying him) =You come here, -bloodied, -broken, -and expect a ", False)
    time.sleep(1.5)
    dramatexter("g i f t?", True)
    time.sleep(1.5)
    texter("You: =(falls to knees, -trembling) =I don’t expect… -I beg. -I’ve burned every bridge, -spilled every drop… -I’ve nothing left but this question.", True)
    time.sleep(1.5)
    chaos()
    texter("\nYou: =(voice breaking) =That-.-.-.- that’s it? =That’s the meaning?", True)
    time.sleep(1.5)
    texter("Wizard: =(chuckling) =Yeah, -I saw it on TikTok.", True)
    time.sleep(0.5)
    texter("You: ", False)
    dramatexter("What the fu-", True)
    ma()
    time.sleep(3)
    am()

def ma():
    for i in range(200):
        for e in range(96):
            print("�", end='')
        print()
        time.sleep(0.02)
        for r in range(8):
            print("cyanidedonut", end='')
        print()
        time.sleep(0.04)

def am():
    cup_statements = [
        "is a cup folding into itself",
        "isn’t a cup but occupies cup space",
        "is a cup intersecting with another cup",
        "is a cup that contains nothing but itself",
        "is a cup larger than reality",
        "is a cup shrinking inside a bigger cup",
        "is a cup that refuses edges",
        "isn’t a cup but reflects cup-ness",
        "is a cup overlapping multiple dimensions",
        "is a cup dissolving into possibility",
        "is a cup trying to be two cups at once",
        "is a cup that exists between sips",
        "is a cup whose bottom is the top",
        "isn’t a cup but could be poured into",
        "is a cup occupying the idea of emptiness",
        "is a cup inside a cup inside a cup",
        "is a cup only visible from the corner of your eye",
        "is a cup folding around nothing",
        "isn’t a cup but stabilizes other cups",
        "is a cup orbiting another cup",
        "is a cup that bends time",
        "isn’t a cup but thinks like one",
        "is a cup being poured by nothing",
        "is a cup that evaporates into possibility",
        "is a cup inside a teacup inside a thought",
        "isn’t a cup but everyone calls it one anyway",
        "is a cup that knows all cups",
        "is a cup that refuses to hold anything",
        "is a cup existing only in dreams",
        "is a cup pretending to be a bowl",
        "is a cup that contains every cup ever",
        "isn’t a cup but could be mistaken for liquid",
        "is a cup that doesn’t obey physics",
        "is a cup folded over itself",
        "is a cup that multiplies when ignored",
        "is a cup that hates cups",
        "is a cup inside a cup inside a cup inside a cup",
        "is a cup that collapses when looked at",
        "isn’t a cup but balances on top of one",
        "is a cup that flows like water",
        "is a cup shrinking into infinity",
        "is a cup that doesn’t exist but exists",
        "is a cup is a cup is a cup is a cup",
        "is a cup that rotates without moving",
        "is a cup folding space and tea",
        "is a cup that sings when empty",
        "isn’t a cup but casts a cup shadow",
        "is a cup bending around concepts",
        "is a cup that refuses definition",
        "is a cup hiding from other cups",
        "is a cup pretending to be two cups",
        "is a cup that drinks itself",
        "is a cup that cannot be touched",
        "is a cup inside a cup floating in a cup",
        "is a cup that echoes infinitely",
        "isn’t not an non true non anti cup",
        "is a cup that folds time into tea",
        "is a cup orbiting ideas",
        "is a cup that cannot be emptied",
        "is a cup folded like a paper crane",
        "is a cup that reflects other cups",
        "isn’t a cup but pours like one",
        "is a cup that multiplies when ignored",
        "is a cup inside a cup inside a cup inside a cup inside a cup",
        "is a cup that melts when observed",
        "is a cup folding reality into itself",
        "is a cup that doesn’t exist but you see it anyway",
        "is a cup that swallows cups",
        "is a cup that doesn’t contain anything",
        "is a cup bending around imagination",
        "is a cup that refuses gravity",
        "is a cup that leaks time",
        "is a cup that thinks it is a teapot",
        "isn’t a cup but exists in cup form",
        "is a cup that grows when you blink",
        "is a cup pretending to be a mug",
        "is a cup folding into another dimension",
        "is a cup that whispers",
        "is a cup that folds itself into circles",
        "is a cup inside a cup orbiting nothing",
        "is a cup that cannot be held",
        "is a cup folding over itself endlessly",
        "isn’t a cup but contains other cups",
        "is a cup that bends like a thought",
        "is a cup inside a cup that doesn’t exist",
        "is a cup that occupies empty space",
        "is a cup that exists only as an idea",
        "is a cup folding into another cup",
        "is a cup that grows when ignored",
        "is a cup orbiting invisible cups",
        "is a cup reflecting other cups inside itself",
        "is a cup that folds around the concept of nothing",
        "is a cup that multiplies in imagination",
        "is a cup that defies understanding",
        "is a cup that stretches into infinity",
        "is a cup inside a cup inside a cup inside a cup inside a cup inside a cup",
        "is a cup that cannot be emptied or filled",
        "is a cup folding itself into a thought",
        "is a cup that exists only when observed",
        "is a cup that refuses to exist in one place",
        "is a cup orbiting itself",
        "is a cup bending around other cups",
        "is a cup that sings when full",
        "is a cup that drifts in abstract space",
        "is a cup that folds into every possible cup",
        "is a cup inside a cup inside a cup inside a cup inside a cup inside a cup inside a cup",
        "milk inside a bag of milk inside a bag of milk inside a bag of milk",
        "isn’t a cup but everyone pours into it anyway"
        ]
    time.sleep(3)
    print("inside the cup")
    time.sleep(4)
    print("is a bigger cup")
    time.sleep(5)
    print("isnt a bigger cup")
    time.sleep(6)
    print("is not a bigger cup")
    time.sleep(5)
    print("isnt not a bigger cup")
    time.sleep(4)
    print("is a nonbigger cup")
    time.sleep(3)
    for i in range(5000):
        print(random.choice(cup_statements))
        time.sleep(1/(i+1) * 3)
    print()
    for o in range(50):
        print("A", end='')
        time.sleep(0.02)
    print()
    for p in range(20):
        print("------------------------------------------------------------------------------")
        time.sleep(0.05)
    time.sleep(2)
    texter("Wizard: =(cyanide donut) =Cups are -G-O-A-T-E-D", True)
    time.sleep(5)
    for a in range(20):
        print("adjasdjasfahfbashfdsahdasgfhagsfhasgduywcbhkavyufvauysbcuwevfasycubkefbebcuyaevwfbsdhfjdsgkvuwbeakc")
        time.sleep(0.01)
    print("chromium tree")

am()