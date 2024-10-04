// https://leetcode.com/problems/reshape-the-matrix

import (
	"fmt"
)
func matrixReshape(mat [][]int, r int, c int) [][]int {
	matDimensions, newDimensions := len(mat)*len(mat[0]), r*c
	if matDimensions != newDimensions {
		return mat
	}

	newMat := make([][]int, r)
	for i := range newMat {
		newMat[i] = make([]int, c)
	}

	colCount := 0
	rowCount := 0
	for _, row := range mat {
		for _, val := range row {
			newMat[rowCount][colCount] = val
			colCount++
            if colCount == c {
                colCount = 0
                rowCount++
            }
		}
	}

	return newMat
}
