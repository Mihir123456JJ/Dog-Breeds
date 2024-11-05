class Dogs:
    def __init__(self,name,colur,behaviour,texture,features,weight):
        self.name=name
        self.colur=colur
        self.behaviour=behaviour
        self.texture=texture
        self.features=features
        self.weight=weight
dog1=Dogs("Poodle","Cream,Black,Blue,Brown,Red,Apricot,Silwer,Sable","Alert,Intelligent,Trainable,Faithfull","Rough and Wiry","Square-like body, with a straight back and a long, elegant neck","Between 20 and 32 kilograms")
dog2=Dogs("German Shepard","Red,Black,Sable,White,Gray,Tan","Stubborn,Loyal,Curious,Intelligent,Brave,Protective","abrasive,wiry,soft undercoat","loyalty, courage, confidence, the ability to learn commands for many tasks, and the willingness to put their life on the line in defense of loved ones"," 32 to 35 kilos")
dog3=Dogs("Mastiff","Brindle,Fawn,Apricot","Calm,Protective","Short, dense and hard in texture with a good sheen","Rectangular body is deep and thickly muscled","68 to 110 kg")
dog4=Dogs("Pomeranian","White,Black,Blue,Cream,Tan,Grey,Orange,","Playful,Active,Friendly,Lively","Short and dense undercoat and harsh overcoat","foxlike faces, triangle ears that point straight up, and feathered tails that arch over their backs","1.4 to 3.2 kg")
print("The Poodles weight is {} and it comes in these colors {} it is {} and also it feels {} ",Dogs(dog1.weight,dog1.colur,dog1.behaviour,dog1.texture))
print("The German Shepard comes in these colors {} and it weighs {} it is {} and it feels {} ",Dogs(dog2.colur,dog2.weight,dog2.behaviour,dog2.texture))
print("The Mastiff weighs around {} and it comes in these colurs {} it is {} and if feels {}",Dogs(dog3.weight,dog3.colur,dog3.behaviour,dog3.texture))
print("The {} weighs {} it is {} it has a {}",Dogs(dog4.name,dog4.weight,dog4.behaviour,dog4.texture))