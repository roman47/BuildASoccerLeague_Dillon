# Make sure the script doesn't execute when imported; put all of your logic and function calls inside of an if
if __name__ == "__main__":

    import csv
    # Create variables and programming logic to divide the 18 players into three teams: Sharks, Dragons and Raptors.
    TEAM_NAMES = ['Sharks', 'Dragons', 'Raptors']
    DATE_AND_TIME_FIRST_PRACTICE = 'the Ides of March, 2019 at 5 PM'

    def import_players():
        """Import players from a a csv file named soccer_players.csv and return a list of that data"""
        all_player_info = []
        with open("soccer_players.csv", mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                    all_player_info.append({"Name": row["Name"], "Soccer Experience": row["Soccer Experience"],
                                            "Guardian Name(s)": row["Guardian Name(s)"]})
            return all_player_info


    # Create a text file named teams.txt that includes the name of a team, followed by the players on that team.
    # List all three teams and their players.
    def process_players(player_data):
        """Take in a list of player information and process it into teams"""
        # sort the players based on experience
        sorted_player_data = sorted(player_data, key=lambda k: k["Soccer Experience"])
        #so we can go through the list and distribute them out evenly
        for idx, player in enumerate(sorted_player_data):
            # Make sure the teams have the same number of players on them, and that the experienced players are divided
            # equally across the three teams.
            player["Team Name"] = TEAM_NAMES[idx % len(TEAM_NAMES)]
            # print(player["Name"] + ", " + player["Soccer Experience"] + ", " + player["Guardian Name(s)"])
        #print(sorted_player_data)
        return sorted_player_data


        # Create a text file named teams.txt that includes the name of a team, followed by the players on that team.
        # List all three teams and their players.
    def print_teams(sorted_player_data):
        """Take in a sorted set of player information and export it into a text file named teams.txt"""
        teams_file = open("teams.txt", "w+")
        for team in TEAM_NAMES:
            # In the list of teams include the team name on one line
            teams_file.write(team+ "\n")
            # followed by a separate line for each player.
            # Include the player's name, whether the player has experience playing soccer, and the player's guardian names.
            # Separate each bit of player information by a comma. For example, the text file might start something like this:
            for player in sorted_player_data:
                if player["Team Name"] == team:
                    teams_file.write(player["Name"] + ", " + player["Soccer Experience"] + ", " + player["Guardian Name(s)"] + "\n")

    #Create 18 text files ("welcome" letters to the players' guardians)
    def print_welcome_letters(sorted_player_data):
        """Create 18 text files ("welcome" letters to the players' guardians). You'll create 1 text file for each
        player. Use the player’s name as the name of the file, in lowercase and with underscores and ending in .txt.
        For example, kenneth_love.txt. Make sure that each file begins with the text "Dear" followed by the guardian(s) name(s). Also include
        the additional required information: player's name, team name, and date & time of first practice."""
        for player in sorted_player_data:
            welcome_letter_file = open(player["Name"].lower().replace(" ", "_") + ".txt", "w+")
            welcome_letter_file.write("Dear {},\n"
                                      "You child, {}, is a new member of the team {}. The first practice will be on {}.\n"
                                      "We look forward to meeting you all.\n"
                                      "Sincerely,\n"
                                      "The Coaches".
                                      format(player["Guardian Name(s)"], player["Name"], player["Team Name"],DATE_AND_TIME_FIRST_PRACTICE))


    # Here we will go step by step through the data
    player_data_from_csv = import_players()
    processed_player_data = process_players(player_data_from_csv)
    print_teams(processed_player_data)
    print_welcome_letters(processed_player_data)
