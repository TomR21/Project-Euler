# PROBLEM 84
import numpy as np
import random

class Monopoly:
    def __init__(self, places):
        self.double_rolls = 0
        self.current_place = 0
        self.places = places
        self.community_count = 0
        self.chance_count = 6

    def roll(self, d=6):
        r1 = random.randint(1, d)
        r2 = random.randint(1, d)
        if r1 == r2:
            self.double_rolls += 1
        else:
            self.double_rolls = 0

        return r1 + r2

    def update_place(self, roll):
        if self.double_rolls == 3:  # When throwing double 3 times, move to jail
            new_place = 10
            self.current_place = 10
            self.double_rolls = 0
            return new_place

        go_to = (self.current_place + roll) % 40  # Goes back to zero after moving over GO
        place = self.places[go_to]

        tile_class = place[:-1]
        if tile_class == "CC":
            new_place = self.community(go_to)
        elif tile_class == "CH":
            new_place = self.chance(int(place[-1]), go_to)
        elif tile_class == "G2":
            new_place = 10
            self.double_rolls = 0
        else:
            new_place = go_to

        self.current_place = new_place
        return new_place

    def community(self, place):
        if self.community_count == 0:
            new_place = 0
        elif self.community_count == 1:
            new_place = 10
            self.double_rolls = 0
        else:
            new_place = place

        self.community_count = (self.community_count + 1) % 16
        return new_place

    def chance(self, tile_number, place):
        if self.chance_count == 0:  # Go to GO
            new_place = 0
        elif self.chance_count == 1:  # Go to JAIL
            new_place = 10
            self.double_rolls = 0
        elif self.chance_count == 2:  # Go to C1
            new_place = 11
        elif self.chance_count == 3:  # Go to E3
            new_place = 24
        elif self.chance_count == 4:  # Go to H2
            new_place = 39
        elif self.chance_count == 5:  # Go to R1
            new_place = 5
        elif self.chance_count == 6 or self.chance_count == 7:  # Go to next R
            # Different R depending on which CH we landed on
            if tile_number == 1:
                new_place = 15
            elif tile_number == 2:
                new_place = 25
            elif tile_number == 3:
                new_place = 5
        elif self.chance_count == 8:  # Go to next U
            if tile_number == 1 or tile_number == 3:
                new_place = 12
            else:
                new_place = 28
        elif self.chance_count == 9:  # Go back 3 tiles
            new_place = place - 3
            if place == 33:  # If we land on CC3
                new_place = self.community(place)
        else:
            new_place = place

        self.chance_count = (self.chance_count + 1) % 16

        return new_place


places = {0: "GO", 1: "A1", 2: "CC1", 3: "A2", 4: "T1", 5: "R1", 6: "B1", 7: "CH1", 8: "B2", 9: "B3", 10: "JAIL",
          11: "C1", 12: "U1", 13: "C2", 14: "C3", 15: "R2", 16: "D1", 17: "CC2", 18: "D2", 19: "D3", 20: "FP",
          21: "E1", 22: "CH2", 23: "E2", 24: "E3", 25: "R3", 26: "F1", 27: "F2", 28: "U2", 29: "F3", 30: "G2J",
          31: "G1", 32: "G2", 33: "CC3", 34: "G3", 35: "R4", 36: "CH3", 37: "H1", 38: "T2", 39: "H2"}

# Initialize Monopoly class and load all tiles
monopoly = Monopoly(places)
arr = np.zeros(40)
for _ in range(10_000_000):
    roll = monopoly.roll(d=4)
    place = monopoly.update_place(roll)
    arr[place] += 1

idx = arr.argsort()[-3:][::-1]
s = sum(arr)
string = ""
for x in idx:
    print(places[x], (arr[x] / s) * 100)  # Prints out the tile with its corresponding percentage
    string += str(x)
