import random

words = ["meadow - A tract of grassland used for pasture or serving as a hayfield.", 
         "sherbet - a frozen dessert made with sweetened fruit juice or puree.", 
         "pomegranate - a chambered, many-seeded, fruit, having a tough, usually red rind", 
         "peony - a widely cultivated species of plants with large and showy flowers.",
         "voyage - a course of travel or passage.",
         "foraging - the acquisition of food by hunting, fishing, or the gathering of plant matter.",
         "hammock - a hanging bed or couch made of canvas, netted cord, or the like, with cords attached to suppoers at each end.",
         "goggle - large spectacles equipped with special lenses often used for skiing, swimming, or industrial work.",
         "snorkeling - moving face down at or just below the durface of the water with a hard rubber or plastic tube through which a swimmer can breathe.",
         "cowrie - the highly polished, usually brightly colored shell of a marine gastropod."
         "luau - a feast of Hawaiian food, usually held outdoors and accompanied by Hawaiian entertainment.",
         "lanai - a room that has a balcony or patio with an overlook of water or garden.", 
         "ecotourism - a responsible way of travelling to natural areas that conserve the environment and sustains the wellbeing of local people.", 
         "glamping - the activity of camping with some of the comforts and luxuries of home.", 
         "itinerary - a detailed plan for a journey, especially a list of places to visit", 
         "paragliding - a sport in which a wide canopy resembling a parachute is attached to a person's body by a harness in order to allow them to glide through the air after jumping from or being lifted to a height."]
print(len(words))
i = 1
while words != []:
    word = random.choice(words)
    print(str(i)+'.', word)
    
    i+=1
    words.remove(word)
    
