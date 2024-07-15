import sys
import argparse

# Function to get the data from the file
def load_file(f):
    file = open(f, 'r')
    data = file.readline()
    values = data.strip().split()
    for i in range(len(values)):
        values[i] = float(values[i])
    return values

# Main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    timestamps = load_file(args.file)
    print(timestamps)

if __name__ == "__main__":
    main()