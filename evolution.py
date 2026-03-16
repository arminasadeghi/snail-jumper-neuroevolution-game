import copy
import numpy as np
from player import Player
import csv
import matplotlib.pyplot as plt
import random


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """

        # TODO (Implement top-k algorithm here)
        newlist = sorted(players, key=lambda x: x.fitness, reverse=True)
        top_k_Res=newlist[: num_players]
        total=0
        for i in newlist:
            total+=i.fitness
        # TODO (Additional: Implement roulette wheel here)

        # TODO (Additional: Implement SUS here)


        # TODO (Additional: Implement Qtournament here)
        QRes=[]
        for i in range(0,num_players):
            temp=[]
            for j in range(0,6):
                selected=random.randint(0, len(players) - 1)
                temp.append(players[selected])
            QRes.append(max(temp, key=lambda x: x.fitness))

        # TODO (Additional: Learning curve)
        max_value = newlist[0].fitness
        min_value = newlist[len(newlist)-1].fitness
        avg_value = 0 if len(newlist) == 0 else total / len(newlist)
        self.writeToCSV(max_value,avg_value,min_value)

        return  newlist[: num_players]



    def writeToCSV(self,max_value,avg_value,min_value):
        file=open("result_file.csv","a")
        row=str(max_value) + ',' + str(avg_value) + ',' + str(min_value) +'\n'
        file.write(row)
        file.close()



    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            children=self.crossover_mutation(prev_players)
            # modify new players
            new_players = prev_players
            return children


    def crossover_mutation(self,prev_players):
        children=[]
        for i in range(0, len(prev_players) - 1, 2):
            #         ndArray[start_row_index : end_row_index , start_column_index : end_column_index]
            # ndArray[start_index: end_index ,  :]
            child1 = self.clone_player(prev_players[i])
            child2 = self.clone_player(prev_players[i + 1])

            child1.nn.weight_1_2 = np.concatenate(
                (prev_players[i].nn.weight_1_2[0:5, :], prev_players[i + 1].nn.weight_1_2[5:10, :]))
            child2.nn.weight_1_2 = np.concatenate(
                (prev_players[i + 1].nn.weight_1_2[0:5, :], prev_players[i].nn.weight_1_2[5:10, :]))
            child1.nn.weight_2_3 = np.concatenate(
                (prev_players[i].nn.weight_2_3[0:5], prev_players[i + 1].nn.weight_2_3[5:10]))
            child2.nn.weight_2_3 = np.concatenate(
                (prev_players[i + 1].nn.weight_2_3[0:5], prev_players[i].nn.weight_2_3[5:10]))

            child1.nn.bias_1_2 = np.concatenate(
                (prev_players[i].nn.bias_1_2[0:5], prev_players[i + 1].nn.bias_1_2[5:10]))
            child2.nn.bias_1_2 = np.concatenate(
                (prev_players[i + 1].nn.bias_1_2[0:5], prev_players[i].nn.bias_1_2[5:10]))
            child1.nn.bias_2_3 = prev_players[i].nn.bias_2_3
            child2.nn.bias_2_3 = prev_players[i + 1].nn.bias_2_3

            r = random.random()
            if r <= 0.5:
                child1.nn.weight_1_2 += np.random.normal(0, 0.2, child1.nn.weight_1_2.shape)
                # child2.nn.weight_1_2 += np.random.normal(0, 0.2, child2.nn.weight_1_2.shape)
                child1.nn.weight_2_3 += np.random.normal(0, 0.2, child1.nn.weight_2_3.shape)
                # child2.nn.weight_2_3 += np.random.normal(0, 0.2, child2.nn.weight_2_3.shape)
                child1.nn.bias_1_2 += np.random.normal(0, 0.2, child1.nn.bias_1_2.shape)
                # child2.nn.bias_1_2 += np.random.normal(0, 0.2, child2.nn.bias_1_2.shape)
                child1.nn.bias_2_3 += np.random.normal(0, 0.2, child1.nn.bias_2_3.shape)
                # child2.nn.bias_2_3 += np.random.normal(0, 0.2, child2.nn.bias_2_3.shape)
            children.append(child1)
            children.append(child2)
        return children

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player
