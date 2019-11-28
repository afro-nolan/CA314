from GameCard import GameCard
from Game import Game

def set_chance_cards(self):
	##Pseudocode for game card
	gamecards = {
	gc1 = GameCard("Chance Card", "Take a trip to King's Cross Station. If you pass Go collect 200." ) : "resources/chance1.jpg",
	gc2 = GameCard("Chance Card", "Advance to MayFair") : "resources/chance2.jpg",
	gc3 = GameCard("Chance Card", "You have been elected Chairman of the Board. Pay each player 50.") : "resources/chance3.jpg",
	gc4 = GameCard("Chance Card", "Advance to the nearest utility. If unowned you may buy it from the bank. If owned, throw dice and pay owner a total ten times thrown.") : "resources/chance4.jpg",
	gc5 = GameCard("Chance Card", "Go back three spaces." ) : "resources/chance5.jpg",
	gc6 = GameCard("Chance Card", "Your building loan matures. Collect 150." ) : "resources/chance6.jpg",
	gc7 = GameCard("Chance Card", "Advance to Pall Mall. If you pass go collect 200.") : "resources/chance7.jpg",
	gc8 = GameCard("Chance Card", "Make general repairs on all your property: For each house pay 25, for each hotel pay 100." ) :"resources/chance8.jpg",
	gc9 = GameCard("Chance Card","Go to Jail. Go directly to jail, Do not pass Go, Do not collect 200." ) : "resources/chance9.jpg",
	gc10 = GameCard("Chance Card", "Advance to go (collect 200)." ) : "resources/chance10.jpg",
	gc11 = GameCard("Chance Card", "Advance to Trafalgar Square. If you pass Go collect 200.") : "resources/chance11.jpg",
	gc12 = GameCard("Chance Card", "Get out of jail Free. This card may be kept until needed or traded") : "resources/chance12.jpg",
	gc13 = GameCard("Chance Card", "Speeding fine 15.") : "resources/chance13.jpg",
	gc14 = GameCard("Chance Card", "Bank pays you dividend of 50") : "resources/chance14.jpg",
	gc15 = GameCard("Chance Card", "Advance to nearest railway station. If unowned you may buy it from the bank. If owned, pay owner twice the rental to which they are otherwise entitled") : "resources/chance15.jpg",
	gc16 = GameCard("Community Chest Card", "Bank Error in your favour. Collect 200" ) : "resources/communitychest1.jpg",
	gc17 = GameCard("Community Chest Card", "Doctor's fees pay 50.") : "resources/communitychest2.jpg",
	gc18 = GameCard("Community Chest Card", "Holiday fund matures. Receive 100.") : "resources/communitychest3.jpg",
	gc19 = GameCard("Community Chest Card", "Get out of jail free. This card may be kept until needed or traded.") :"resources/communitychest4.jpg",
	gc20 = GameCard("Community Chest Card", "Pay school fees of 50.") : "resources/communitychest5.jpg",
	gc21 = GameCard("Community Chest Card", "Income tax refund. Collect 20.") : "resources/communitychest6.jpg",
	gc22 = GameCard("Community Chest Card", "Pay hospital fees of 100.") : "resources/communitychest7.jpg",
	gc23 = GameCard("Community Chest Card", "Receive 25 consultancy fee.") : "resources/communitychest8.jpg",
	gc24 = GameCard("Community Chest Card", "It is your birthday. Collect 10 from each player.") : "resources/communitychest9.jpg",
	gc25 = GameCard("Community Chest Card", "You inherit 100.") : "resources/communitychest10.jpg",
	gc26 = GameCard("Community Chest Card", "From sale of stock you get 50.") :"resources/communitychest11.jpg",
	gc27 = GameCard("Community Chest Card", "You have won second prize in a beauty contest. Collect 10.") : "resources/communitychest12.jpg",
	gc28 = GameCard("Community Chest Card", "You are assessed for street repairs: 40 per house, 115 per hotel.") : "resources/communitychest13.jpg",
	gc29 = GameCard("Community Chest Card", "Advance to go. (Collect 200).") : "resources/communitychest14.jpg",
	gc30 = GameCard("Community Chest Card", "Life insurance matures. Collect 100.") : "resources/communitychest15.jpg",
	gc31 = GameCard("Community Chest Card", )

	}


#addresses of chance cards
	image_addr1 = "resources/chance1.jpg"
	image_addr2 = "resources/chance2.jpg"
	image_addr3 = "resources/chance3.jpg"
	image_addr4 = "resources/chance4.jpg"
	image_addr5 = "resources/chance5.jpg"
	image_addr6 = "resources/chance6.jpg"
	image_addr7 = "resources/chance7.jpg"
	image_addr8 = "resources/chance8.jpg"
	image_addr9 = "resources/chance9.jpg"
	image_addr10 = "resources/chance10.jpg"
	image_addr11 = "resources/chance11.jpg"
	image_addr12 = "resources/chance12.jpg"
	image_addr13 = "resources/chance13.jpg"
	image_addr14 = "resources/chance14.jpg"
	image_addr15 = "resources/chance15.jpg"
	image_addr16= "resources/chance16.jpg"

#addresses of community chest cards

	image_addr17 = "resources/communitychest1.jpg"
	image_addr18 = "resources/communitychest2.jpg"
	image_addr19 = "resources/communitychest3.jpg"
	image_addr20 = "resources/communitychest4.jpg"
	image_addr21= "resources/communitychest5.jpg"
	image_addr22 = "resources/communitychest6.jpg"
	image_addr23 = "resources/communitychest7.jpg"
	image_addr24 = "resources/communitychest8.jpg"
	image_addr25 = "resources/communitychest9.jpg"
	image_addr26 = "resources/communitychest10.jpg"
	image_addr27= "resources/communitychest11.jpg"
	image_addr28= "resources/communitychest12.jpg"
	image_addr29= "resources/communitychest13.jpg"
	image_addr30= "resources/communitychest14.jpg"
	image_addr31= "resources/communitychest15.jpg"
	image_addr32= "resources/communitychest16.jpg"



	#chance cards descriptions
	gc1 = GameCard("Chance Card", "Take a trip to King's Cross Station. If you pass Go collect 200." )
	gc2 = GameCard("Chance Card", "Advance to MayFair")
	gc3 = GameCard("Chance Card", "You have been elected Chairman of the Board. Pay each player 50.")
	gc4 = GameCard("Chance Card", "Advance to the nearest utility. If unowned you may buy it from the bank. If owned, throw dice and pay owner a total ten times thrown.")
	gc5 = GameCard("Chance Card", "Go back three spaces." )
	gc6 = GameCard("Chance Card", "Your building loan matures. Collect 150." )
	gc7 = GameCard("Chance Card", "Advance to Pall Mall. If you pass go collect 200.")
	gc8 = GameCard("Chance Card", "Make general repairs on all your property: For each house pay 25, for each hotel pay 100." )
	gc9 = GameCard("Chance Card","Go to Jail. Go directly to jail, Do not pass Go, Do not collect 200." )
	gc10 = GameCard("Chance Card", "Advance to go (collect 200)." )
	gc11 = GameCard("Chance Card", "Advance to Trafalgar Square. If you pass Go collect 200.")
	gc12 = GameCard("Chance Card", "Get out of jail Free. This card may be kept until needed or traded")
	gc13 = GameCard("Chance Card", "Speeding fine 15.")
	gc14 = GameCard("Chance Card", "Bank pays you dividend of 50")
	gc15 = GameCard("Chance Card", "Advance to nearest railway station. If unowned you may buy it from the bank. If owned, pay owner twice the rental to which they are otherwise entitled")

	#community chest card descriptions
	gc16 = GameCard("Community Chest Card", "Bank Error in your favour. Collect 200" )
	gc17 = GameCard("Community Chest Card", "Doctor's fees pay 50.")
	gc18 = GameCard("Community Chest Card", "Holiday fund matures. Receive 100.")
	gc19 = GameCard("Community Chest Card", "Get out of jail free. This card may be kept until needed or traded.")
	gc20 = GameCard("Community Chest Card", "Pay school fees of 50.")
	gc21 = GameCard("Community Chest Card", "Income tax refund. Collect 20.")
	gc22 = GameCard("Community Chest Card", "Pay hospital fees of 100.")
	gc23 = GameCard("Community Chest Card", "Receive 25 consultancy fee.")
	gc24 = GameCard("Community Chest Card", "It is your birthday. Collect 10 from each player.")
	gc25 = GameCard("Community Chest Card", "You inherit 100.")
	gc26 = GameCard("Community Chest Card", "From sale of stock you get 50.")
	gc27 = GameCard("Community Chest Card", "You have won second prize in a beauty contest. Collect 10.")
	gc28 = GameCard("Community Chest Card", "You are assessed for street repairs: 40 per house, 115 per hotel.")
	gc29 = GameCard("Community Chest Card", "Advance to go. (Collect 200).")
	gc30 = GameCard("Community Chest Card", "Life insurance matures. Collect 100.")
	gc31 = GameCard("Community Chest Card", )


#example
	#players = Game.get_players() #Instances of the players in the game. You can get this from the Game class.
	#	if gc1 not in gamecards:
	#	gamecards[gc1] = image_addr

	#return gamecards



players = Game.get_players()
	if gc1 not in gamecards:
			gamecards[gc1] = image_addr1

	elif gc2 not in gamecards:
			gamecards[gc2] = image_addr2

	elif gc3 not in gamecards:	
			gamecards[gc3] = image_addr3

	elif gc4 not in gamecards:	
			gamecards[gc4] = image_addr4

	elif gc5 not in gamecards:
			gamecards[gc5] = image_addr5

	elif gc6 not in gamecards:
			gamecards[gc6] = image_addr6

	elif gc7 not in gamecards:
			gamecards[gc7] = image_addr7

	elif gc8 not in gamecards:
			gamecards[gc8] = image_addr8

	elif gc9 not in gamecards:
			gamecards[gc9] = image_addr9

	elif gc10 not in gamecards:
			gamecards[gc10] = image_addr10

	elif gc11 not in gamecards:
			gamecards[gc11] = image_addr11

	elif gc12 not in gamecards:
			gamecards[gc12] = image_addr12

	elif gc13 not in gamecards:
			gamecards[gc13] = image_addr13

	elif gc14 not in gamecards:
			gamecards[gc1] = image_addr14

	elif gc15 not in gamecards:
			gamecards[gc15] = image_addr15

	elif gc16 not in gamecards:
			gamecards[gc16] = image_addr16

	elif gc17 not in gamecards:
			gamecards[gc17] = image_addr17

	elif gc18 not in gamecards:
			gamecards[gc18] = image_addr18

	elif gc19 not in gamecards:
			gamecards[gc19] = image_addr19

	elif gc20 not in gamecards:
			gamecards[gc20] = image_addr20

	elif gc21 not in gamecards:
			gamecards[gc21] = image_addr21

	elif gc22 not in gamecards:
			gamecards[gc22] = image_addr22

	elif gc23 not in gamecards:
			gamecards[gc23] = image_addr23

	elif gc24 not in gamecards:
			gamecards[gc24] = image_addr24

	elif gc25 not in gamecards:
			gamecards[gc25] = image_addr25

	elif gc26 not in gamecards:
			gamecards[gc26] = image_addr26

	elif gc27 not in gamecards:
			gamecards[gc27] = image_addr27

	elif gc28 not in gamecards:
			gamecards[gc28] = image_addr28

	elif gc29 not in gamecards:
			gamecards[gc29] = image_addr29

	elif gc30 not in gamecards:
			gamecards[gc30] = image_addr30

	elif gc31 not in gamecards:
		gamecards[gc] = image_addr31

	elif gc32 not in gamecards:
		gamecards[gc] = image_addr32
return gamecards