def adjacency_matrix_to_list(adjacency_matrix):
    adjacency_list = {}
    for i in range(len(adjacency_matrix)):
        adjacency_list[i] = []
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                adjacency_list[i].append(j)
    return adjacency_list

def print_adjacency_list(adjacency_list):
    for key in adjacency_list:
        print(f"{key}: {adjacency_list[key]}")

# Test the implementation
if __name__ == "__main__":
    adjacency_matrix = [
        [0, 0, 0, 1, 1, 0],  # Agree Funding
        [0, 0, 0, 0, 0, 1],  # Install Software
        [1, 0, 0, 0, 0, 0],  # Planning Meeting
        [0, 1, 0, 0, 0, 0],  # Purchase Hardware
        [0, 1, 0, 0, 0, 0],  # Purchase Software
        [0, 0, 0, 0, 0, 0]   # Train Users
    ]

    adjacency_list = adjacency_matrix_to_list(adjacency_matrix)
    print("Adjacency List:")
    print_adjacency_list(adjacency_list)
