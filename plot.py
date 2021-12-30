import matplotlib.pyplot as plt

max_fitnesses = []
max_generations = []

def collect_data(max_fitness: int, generation_number: int) -> None:
    global max_fitnesses
    global max_generations
    max_fitnesses.append(max_fitness)
    max_generations.append(generation_number)

def plot() -> None:
    global max_fitnesses
    global max_generations
    plt.figure("Plot")
    plt.title('Training result')
    plt.xlabel('Generations')
    plt.ylabel('Fitness score')
    plt.bar(max_generations, max_fitnesses, width=0.3)
    plt.xticks(range(1,len(max_generations)+1))
    plt.yticks(range(0, max(max_fitnesses)+1,500))
    plt.grid(color='grey', linestyle='dotted', linewidth=0.5)

    for index, value in enumerate(max_fitnesses):
        plt.text(index+1, value, str(value),ha='center', va='bottom')

    plt.show()