def mergeCellPos(cellPos1 = [[]], cellPos2 = [[]]):
    cellPos = [[]]

    ix1 = 0
    ix2 = 0

    if cellPos1[ix1] < cellPos2[ix2]:
        cellPos.append(cellPos1[ix1])
    else:
        cellPos.append(cellPos2[ix2])

    while ix1 < len(cellPos1) and ix2 < len(cellPos2):
        cellPosEnd = len(cellPos) - 1
        
        if cellPos1[ix1] < cellPos2[ix2]:
            if cellPos[cellPosEnd] != cellPos1[ix1]:
                cellPos.append(cellPos1[ix1])
            else:
                ix1 += 1
        
        elif cellPos[cellPosEnd] != cellPos2[ix2]:
            if cellPos[cellPosEnd] != cellPos2[ix2]:
                cellPos.append(cellPos2[ix2])
            else:
                ix2 += 1

    while ix1 < len(cellPos1):
        cellPosEnd = len(cellPos) - 1

        if cellPos[cellPosEnd] != cellPos1[ix1]:
                cellPos.append(cellPos1[ix1])
        else:
            ix1 += 1

    while ix2 < len(cellPos2):
        cellPosEnd = len(cellPos) - 1

        if cellPos[cellPosEnd] != cellPos2[ix2]:
                cellPos.append(cellPos2[ix2])
        else:
            ix2 += 1