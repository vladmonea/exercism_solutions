#include "scrabble_score.h"

int getValueOfChar(char i){
  if (i == 'a' || i == 'e' || i == 'i' || i == 'o' || i == 'u' || i == 'l' || i == 'n' || i == 'r' || i == 's' || i == 't'){
    return 1;
  } else if (i == 'd' || i == 'g') {
    return 2;
  } else if (i == 'b' || i == 'c' || i == 'm' || i == 'p') {
    return 3;
  } else if (i == 'f' || i == 'h' || i == 'v' || i == 'w' || i == 'y') {
    return 4;
  } else if (i == 'k') {
    return 5;
  } else if (i == 'j' || i == 'x') {
    return 8;
  } else {
    return 10;
  }
}

int score(char* word[]){
  int word_score = 0;
  for (int i = 0; i < strlen(word); i++) {
    word_score += word[i];
  }
}
