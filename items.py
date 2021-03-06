class item():
    def __init__(self,item_id,name,weight,description,value,type,potency):
        self.id=item_id         #unique item ID
        self.name=name          #item name
        self.weight=weight      #appropriate weight
        self.description=description    #description of item
        self.value=value        #value of item in gold
        self.type=type          #type e.g. food, weapon, misc
        self.potency=potency    #effectiveness (how much food heals, how much damage a weapon does)

#eg reference "items.caviar" to call upon it in another file (after importing items)
#food
itemDict = {
    "caviar":item("caviar","caviar",0.1,"Salt-cured fish eggs, a rare delicacy",100,"food",30),
    "oyster":item("oyster","oyster",0.2,"Grown on racks in bags and can be characterized as being salty",100,"food",30),
    "insects":item("insects","insects",0.2,"Small creepy crawlies that can be eaten",20,"food",-10),
    "bread":item("bread","bread",0.3,"A dry, un-appetising loaf, with a crisp outside",5,"food",10),
    "apple":item("apple","apple",0.2,"A shiny, ripe, red fruit",15,"food",15),
    "banana":item("banana", "banana",0.2,"Curved, yellow fruit with a thick skin and soft sweet flesh",15,"food",15),
    "chicken":item("chicken","chicken",0.4,"All parts intact, including the giblets stuffed in the cavity",20,"food",20),
    "fish":item("fish","fish",0.3,"Small, bluish-golden plaice, with eyes inlcuded",25,"food",20),
    "honey":item("honey","honey",0.1,"A small jar of golden honey fluid",40,"food",5),
    "water":item("water","water",0.2,"A bladder full of refreshing cold water",5, "food",5),
    "wine":item("wine","wine",0.3,"A small glass bottle filled with delicious Pinot Noir",50,"food",10),
    "beer":item("beer","beer",0.2,"A hip flask full of cheap beer",5,"food",5),
#weapons
    "kitchenknife":item("knife", "kitchen knife", 3, "A standard 4 inch knife for food prep, could be used as a weapon in an emergency.",50,"weapon",25),
    "basesword":item("basesword","sword",8,"A single handed, double edged sword",90,"weapon",50),
    "claymore":item("claymore","claymore",11,"a two handed sword, basic in design, lethal in use",90,"weapon",75),
    "zweihander":item("zweihander","zweihander",17,"A large blade with a big handle",120,"weapon",100),
    "ultimatesword":item("ultimatesword","ultimatesword",10,"A skillfully crafted sword with perfect balance and speed",200,"weapon",150),
#armour    I added armour in but idk if there's an armour type 
    "helmet":item("helmet","helmet",9,"A garment for protecting the head",60,"armour",30),
    "chestplate":item("chestplate","chestplate",20,"A garment for protecting the chest",70,"armour",40),
    "leggings":item("leggings","leggings",8,"A garment for protecting the legs",50,"armour",25),
    "boots":item("boots","boots",5,"A garment for protecting the feet",40,"armour",25),
#potions
    "potionhp":item("pot.hp","health potion",0.3,"A potion used to restore 60 hp to the drinker",40,"food",60)
    }
