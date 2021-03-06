import operator
import time
from operator import attrgetter

from hashTable import *
from BST import *

def formatItem(item):
      return "name: {}\nenergy: {}\nfat: {}\ncarbohydrates: {}\nproteins: {}\ningredients: {}\n".format(
            item[0],
            item[1],
            item[2],
            item[3],
            item[4],
            item[5]
        )

def search(userInput, productNames):
    return (productNames[productNames.str.contains(userInput)].values)

def sort(array, metric):
    array.sort(key=lambda x: x[metric])
    for i in array:
        print (formatItem(i))


def main():
    foodData = pd.read_csv('food_data_no_duplicates.csv')
    b = foodData.values


    dataStructureChoice = 0
    while dataStructureChoice != 3:
        print ("Welcome to the nutrition look-up tool.")
        print ("Please select which data structure you would like to use:")
        print ("1. Map")
        print ("2. Tree")
        print ("Press 3 to quit.")

        dataStructureChoice = input()
        if dataStructureChoice == "3":
            break
        if dataStructureChoice == "1" or dataStructureChoice == "2":
            print ("Thank you! Please enter the item you are searching for:")

            item = input()

            # product names for searching
            productNames = foodData.loc[:, 'product_name']

            result = search(item, productNames)

            if dataStructureChoice == "1":

                t = hashTable()

                for i in b:
                    t.insert(i)
                start = time.time()
                resultSort = []
                #prints the products that match in the hashTable
                for i in result:
                    print(formatItem(t.getItem(i)))
                    resultSort.insert(0, t.getItem(i))
                end = time.time()
                print ("The time it took for this process is: ")
                print(end-start)

            elif dataStructureChoice == "2":

                df = pd.read_csv("food_data_no_duplicates.csv")

                tree = BST()
                for i in range(165817):
                    n = node.Node(
                        df["product_name"][i],
                        df["energy_100g"][i],
                        df["fat_100g"][i],
                        df["carbohydrates_100g"][i],
                        df["proteins_100g"][i],
                        df["ingredients_text"][i]
                    )
                    tree.insertNode(n, tree.getRoot())
                start1 = time.time()
                resultSort1 = []
                for i in result:
                    print(tree.searchNode(i, tree.getRoot()))
                    resultSort1.insert(0, tree.searchNode(i, tree.getRoot()))
                end1 = time.time()
                print("The time it took for this process is: ")
                print(end1 - start1)

            print("Which metric would you like to sort by?")
            print("1. Calories")
            print("2. Fat")
            print("3. Carbohydrates")
            print("4. Protein")

            sortingMetric = input()

            if sortingMetric == "1" and dataStructureChoice == "1":
                sort(resultSort, 1)

            elif sortingMetric == "2" and dataStructureChoice == "1":
                sort(resultSort, 2)

            elif sortingMetric == "3" and dataStructureChoice == "1":
                sort(resultSort, 3)

            elif sortingMetric == "4" and dataStructureChoice == "1":
                sort(resultSort, 4)

            elif sortingMetric == "1" and dataStructureChoice == "2":
                resultSort1.sort(key=lambda x: x.getEnergy())
                for i in resultSort1:
                    print(i)

            elif sortingMetric == "2" and dataStructureChoice == "2":
                resultSort1.sort(key=lambda x: x.getFat())
                for i in resultSort1:
                    print(i)

            elif sortingMetric == "3" and dataStructureChoice == "2":
                resultSort1.sort(key=lambda x: x.getCarbs())
                for i in resultSort1:
                    print(i)

            elif sortingMetric == "4" and dataStructureChoice == "2":
                resultSort1.sort(key=lambda x: x.getProteins())
                for i in resultSort1:
                    print(i)

            else:
                print("I'm sorry. That is not a valid option.")
        else:
            print("I'm sorry. That is not a valid choice.")



main()