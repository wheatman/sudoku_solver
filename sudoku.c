#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>
#include <assert.h>
#include <string.h>

#define LEN 9
#define uint uint16_t

#define puzzleEasy  {	0,0,0,3,0,0,0,4,0,	0,0,2,1,0,4,6,5,9,	0,1,4,0,6,9,8,0,0,	0,0,0,8,0,7,3,0,0,	0,2,0,6,3,0,0,0,0,	0,3,0,0,2,0,0,0,5,	0,0,3,0,0,0,5,0,0,	1,0,0,2,9,0,0,3,8,	0,4,0,0,1,0,2,0,6}
#define puzzleMiddle {	9,0,5,2,0,0,8,4,3,	0,3,0,0,0,0,0,7,0,	4,0,0,6,0,8,0,0,0,	0,0,0,7,1,9,0,0,0,	0,0,0,8,5,0,0,0,0,	1,0,4,0,0,2,0,0,0,	0,0,6,9,4,3,2,8,0,	0,0,9,0,0,6,0,0,5,	0,1,0,0,8,0,0,0,0}
#define puzzleHard {	3,0,9,0,0,0,4,0,0,	4,8,0,0,0,0,0,0,0,	0,6,2,0,0,0,0,0,0,	2,3,0,0,5,4,7,0,0,	0,0,0,3,0,9,2,0,4,	0,0,0,8,0,0,3,5,1,	0,0,6,0,2,0,8,0,0,	0,0,0,0,9,0,0,0,0,	0,5,8,0,0,0,0,9,0}
#define puzzleExpert {	0,0,0,0,0,9,0,7,1,	0,0,4,0,3,0,0,0,0,	0,0,0,0,0,0,3,0,0,	3,0,0,0,0,0,0,8,0,	2,0,0,9,5,0,0,0,7,	0,0,0,7,0,1,0,0,3,	0,0,1,3,0,8,0,0,5,	9,0,0,1,0,0,0,0,0,	5,0,0,0,0,0,0,4,0}
#define puzzleExtreme {	8,0,0,0,0,0,0,0,0,	0,0,3,6,0,0,0,0,0,	0,7,0,0,9,0,2,0,0,	0,5,0,0,0,7,0,0,0,	0,0,0,0,4,5,7,0,0,	0,0,0,1,0,0,0,3,0,	0,0,1,0,0,0,0,6,8,	0,0,8,5,0,0,0,1,0,	0,9,0,0,0,0,4,0,0}
#define puzzleExtreme2 {0,6,1,0,0,7,0,0,3,	0,9,2,0,0,3,0,0,0,	0,0,0,0,0,0,0,0,0,	0,0,8,5,3,0,0,0,0,	0,0,0,0,0,0,5,0,4,	5,0,0,0,0,8,0,0,0,	0,4,0,0,0,0,0,0,1,	0,0,0,1,6,0,8,0,0,	6,0,0,0,0,0,0,0,0}

static uint puzzles[6][LEN*LEN] = {puzzleEasy, puzzleMiddle, puzzleHard, puzzleExpert, puzzleExtreme, puzzleExtreme2};

struct board_t {
	uint bd[LEN*LEN];
};

#define board struct board_t

void setSquare(board* b, uint i, uint j, uint val) {
	assert(i < LEN);
	assert(j < LEN);
	b->bd[i*LEN + j] = val;
}
void removeOption(board* b, uint i, uint j, uint val) {
	assert(i < LEN);
	assert(j < LEN);
	assert(val != 0);
	uint mask = ~val;
	b->bd[i*LEN + j] &= mask;
}
uint getSquare(board* b, uint i, uint j) {
	assert(i < LEN);
	assert(j < LEN);
	return b->bd[i*LEN + j];
}
		

void printPuzzle(board *b) {
	for (uint i = 0; i < LEN; i++){
	    for (uint j = 0; j < LEN; j++){
	    	printf("%d ",getSquare(b, i, j));
	    }
	    printf("\n");
	}
}
bool checkValid(board *b) {
	for (uint i = 0; i < LEN; i++){
	    for (uint j = 0; j < LEN; j++){
	    	if (getSquare(b, i, j) == 0) {
	    		return false;
	    	}
	    }
	}
	return true;
}
void convertInto(board *b) {
	for (uint i = 0; i < LEN; i++){
	    for (uint j = 0; j < LEN; j++){
	    	if (getSquare(b, i, j) == 0) {
	    		// in binary we wat it to be 1111111110
	    		// so it has bits filled in at all the possible shifts from 1 to 9
	    		setSquare(b, i, j, 0x3FE);
	    	} else {
	    		setSquare(b, i, j, 1 << getSquare(b, i, j));
	    	}
	    }
	}
}

 uint bitIndex (uint val) {
	assert(val !=0);
	uint count = 0;
	while (val != 1){
		count +=1;
		val = val >>1;
	}
	return count;
}

bool checkPowerOf2(uint val) {
	assert(val != 0);
	return !(val & (val - 1));
}

void convertBack(board *b) {
	assert(checkValid(b));
	for (uint i = 0; i < LEN; i++){
	    for (uint j = 0; j < LEN; j++){
	    	assert(checkPowerOf2(getSquare(b, i, j)));
	    	setSquare(b, i, j, bitIndex(getSquare(b, i, j)));
	    }
	}
}
bool done(board *b) {
	assert(checkValid(b));
	for (uint i = 0; i < LEN; i++){
	    for (uint j = 0; j < LEN; j++){
	    	if (!checkPowerOf2(getSquare(b, i, j))) {
	    		return false;
	    	}
	    }
	}
	return true;
}
uint lowestBit(uint val) {
	uint index = 0;
	assert(val < (1 << (LEN+1)));
	while (val > 1) {
		index+=1;
		val = val >> 1;
	}
	assert(index <= LEN);
	return index;
}
board* makeGuess(board *b) {
	board* newPuzzle = (board*) malloc(sizeof(board));
	memcpy((void*) newPuzzle, (void*) b, sizeof(board));
	assert(checkValid(b));
	assert(checkValid(newPuzzle));
	for (uint i = 0; i < LEN; i++){
	    for (uint j = 0; j < LEN; j++){
	    	if (!checkPowerOf2(getSquare(b, i, j))) {
	    		uint index = lowestBit(getSquare(b, i, j));
	    		uint mask = 1 << index;
	    		setSquare(newPuzzle, i, j, mask);
	    		removeOption(b, i, j, mask);
	    		return newPuzzle;
	    	}
	    }
	}
	assert(false);
	return newPuzzle;
}

bool solver(board *puzzle, uint level) {
	assert(checkValid(puzzle));
	uint change = 1;
	while (change) {
		change = 0;
		for (uint row = 0; row < LEN; row++) {
			for (uint column = 0; column < LEN; column++) {
				assert(checkValid(puzzle));
				if (checkPowerOf2(getSquare(puzzle, row, column))) {
					for (uint k = 0; k < LEN; k++) {
						uint mask = ~getSquare(puzzle, row, column);
						if (column != k){
							change |= (getSquare(puzzle, row, k) & getSquare(puzzle, row, column));
							setSquare(puzzle, row, k, getSquare(puzzle, row, k) & mask);
							if (getSquare(puzzle, row, k) == 0) {
								return false;
							}
						}
						if (row != k) {
							change |= (getSquare(puzzle, k, column) & getSquare(puzzle, row, column));
							uint mask = ~getSquare(puzzle, row, column);
							setSquare(puzzle, k, column, getSquare(puzzle, k, column) & mask);
							if (getSquare(puzzle, k, column) == 0) {
								return false;
							}
						}
					}
					uint rowStart = (row/3)*3;
					uint colStart = (column/3)*3;
					for (uint k = rowStart; k < rowStart+3; k++) {
						for (uint l = colStart; l < colStart+3; l++) {
							if (row != k || column != l) {
								change |= (getSquare(puzzle, k, l) & getSquare(puzzle, row, column));
								uint mask = ~getSquare(puzzle, row, column);
								setSquare(puzzle, k, l, getSquare(puzzle, k, l) & mask);
								if (getSquare(puzzle, k, l) == 0) {
									return false;
								}
							}
						}
					}
				}
			}
		}
	}
	assert(checkValid(puzzle));
	if (done(puzzle)) {
		return true;
	} else {
		board *guessPuzzle = makeGuess(puzzle);
		assert(checkValid(puzzle));
		if (done(puzzle)) {
			return true;
		}
		else {
			bool next = solver(puzzle, level+1);
			if (next) {
				return true;
			}
		}
		memcpy((void*) puzzle, (void*) guessPuzzle, sizeof(board));
		assert(checkValid(puzzle));
		if (done(puzzle)) {
			return true;
		}
		else {
			return solver(puzzle, level+1);
		}
	}
	assert(false);
	return false;
}
int main(){
	for (uint i = 0; i < 6; i++){
	    board puzzle;
	    memcpy((void*) puzzle.bd, (void*) puzzles[i], sizeof(puzzle.bd));
	    printPuzzle(&puzzle);
	    convertInto(&puzzle);
	    solver(&puzzle, 0);
	    convertBack(&puzzle);
	    printPuzzle(&puzzle);
	    printf("\n");
	}
	return 1;
}