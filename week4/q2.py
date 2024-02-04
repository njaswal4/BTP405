import matplotlib.pyplot as plt

def graphSnowfall(file_path):
    # Read data from the file
    with open(file_path, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file]

    # Aggregate the data into 10 cm ranges
    ranges = [0, 10, 20, 30, 40, 50]
    counts = [0] * (len(ranges) - 1)

    for snowfall in snowfall_data:
        for i in range(len(ranges) - 1):
            if ranges[i] <= snowfall < ranges[i + 1]:
                counts[i] += 1
                break

    # Plotting the bar graph
    plt.bar([f"{ranges[i]}-{ranges[i+1]}cms" for i in range(len(ranges)-1)], counts)
    plt.xlabel('Snowfall Range (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Distribution')
    plt.show()


