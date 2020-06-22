import unittest
from main import app
from db import mysql
import random
from random import randint


class TestAgent(unittest.TestCase):

    mycon = mysql.connect()
    mycursor = mycon.cursor()

    def test_agent(self):

        # issue = ["sales", "support", "speaker"]

        start = str(input("Describe your issue and press enter key? "))
        print(start)

        agent_mode = str(
            input(
                "Choose the Agent selection mode?(choose them as they are)?? "
                + "\n"
                + " a. all_available"
                + "\n"
                + " b. least_busy"
                + "\n"
                + " c. random "
                + "\n"
            )
        )
        print("You Choose: " + agent_mode)

        if agent_mode == "all_available":
            print("Our All Agents Are Available For You.")
            self.mycursor.execute("select name from agents")
            select = self.mycursor.fetchall()
            for i in select:
                print(i)
            print("Your Issue has taken by: ", random.choice(select))

        elif agent_mode == "least_busy":
            print("Our Least busy agents are as follows: ")
            self.mycursor.execute("select name from agents where is_available='1' ")
            select = self.mycursor.fetchall()
            for i in select:
                print(i)
            print("Your Issue has taken by: ", random.choice(select))

        elif agent_mode == "random":

            issue = str(
                input(
                    "Select the Issue About "
                    + "\n"
                    + " a. sales"
                    + "\n"
                    + " b. support"
                    + "\n"
                    + " c. speaker"
                    + "\n"
                )
            )
            print(issue)
            issues = ["sales", "support", "speaker"]

            if issue == "sales":
                print("Our agents for Sales Issues are: ")
                self.mycursor.execute("select name from agents where role='sales'")
                select = self.mycursor.fetchall()
                for i in select:
                    print(i)
                print("Your Issue has taken by: ", random.choice(select))

            elif issue == "support":
                print("Our agents for Support Issues are: ")
                self.mycursor.execute("select name from agents where role='support'")
                select = self.mycursor.fetchall()
                for i in select:
                    print(i)
                print("Your Issue has taken by: ", random.choice(select))

            elif issue == "speaker":
                print("Our agents for Speaker Issues are: ")
                self.mycursor.execute("select name from agents where role='speaker'")
                select = self.mycursor.fetchall()
                for i in select:
                    print(i)
                print("Your Issue has taken by: ", random.choice(select))

            else:
                print("Choose Only From the above list")

        else:
            print("Choose Only From the above list")


if __name__ == "__main__":
    unittest.main()
