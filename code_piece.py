def randomTile_player1():
    free_tile_indexes_player1 = []

    for rowindex in range(len(tileMatrix_player1)):
        for colindex in range(len(tileMatrix_player1)):
            if tileMatrix_player1[rowindex][colindex] == 0:
                free_tile_indexes_player1.append([rowindex, colindex])
                
    if not free_tile_indexes_player1:
        pass
        
    else:
        free_coords_player1 = random.choice(free_tile_indexes_player1)
        tileMatrix_player1[free_coords_player1[0]][free_coords_player1[1]] = 2

def CheckIfMovable_player1():
    for i in range(0, Board_Size ** 2):
        if tileMatrix_player1[math.floor(i / Board_Size)][i % Board_Size] == 0:
            return True
    for i in range(0, Board_Size):
        for j in range(0, Board_Size - 1):
            if tileMatrix_player1[i][j] == tileMatrix_player1[i][j + 1]:
                return True
            elif tileMatrix_player1[j][i] == tileMatrix_player1[j + 1][i]:
                return True
    return False

def Movable_player1():
    for i in range(0, Board_Size):
        for j in range(1, Board_Size):
            if tileMatrix_player1[i][j - 1] == 0 and tileMatrix_player1[i][j] > 0:
                return True
            elif (tileMatrix_player1[i][j - 1] == tileMatrix_player1[i][j] and tileMatrix_player1[i][
                j - 1] != 0):
                return True
    return False

def ListToMatrixConvert_player1():
    if len(tempMatrix_player1) > 0:
        matrix_player1 = tempMatrix_player1.pop()

        for i in range(0, Board_Size ** 2):
            tileMatrix_player1[math.floor(i / Board_Size)][i % Board_Size] = matrix_player1[i]

        global Total_Points_player1
        Total_Points_player1 = matrix_player1[Board_Size ** 2]

        kiirMatrix()
		
def Tile_Mover_player1():
    for i in range(0, Board_Size):
        for j in range(0, Board_Size - 1):
            while tileMatrix_player1[i][j] == 0 and sum(tileMatrix_player1[i][
                                                        j:]) > 0:
                for k in range(j, Board_Size - 1):
                    tileMatrix_player1[i][k] = tileMatrix_player1[i][k + 1]
                tileMatrix_player1[i][Board_Size - 1] = 0
				
def Tile_Merger_player1():
    global Total_Points_player1

    for i in range(0, Board_Size):
        for j in range(0, Board_Size - 1):
            if tileMatrix_player1[i][j] == tileMatrix_player1[i][j + 1] and tileMatrix_player1[i][
                j] != 0:
                tileMatrix_player1[i][j] = tileMatrix_player1[i][j] * 2
                tileMatrix_player1[i][j + 1] = 0
                Total_Points_player1 += tileMatrix_player1[i][j]
                Tile_Mover_player1()

def do_Action_player1():

    global shoot_Actual_Counter_player1
    shootable_tile_indexes_player2 = []

    if shoot_Actual_Counter_player1 > 0:

        for rowindex1 in range(len(tileMatrix_player2)):
            for colindex1 in range(len(tileMatrix_player2)):
                if tileMatrix_player2[rowindex1][colindex1] > 0:
                    shootable_tile_indexes_player2.append([rowindex1, colindex1])
                    
        if len(shootable_tile_indexes_player2) <= 1 :
            pass
            
        else:
            shootable_coords_player2 = random.choice(shootable_tile_indexes_player2)
            
            tileMatrix_player2[shootable_coords_player2[0]][shootable_coords_player2[1]] = 0

            shoot_Actual_Counter_player1 -= 1
    else:
        pass