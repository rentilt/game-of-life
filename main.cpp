#include <iostream>
#include <vector>
#include <math.h>       /* ceil and log */
#include <utility>    // pair
#include <stack>
#include <unistd.h>
#include <time.h>       /* time */

#include <algorithm>    // std::sort


using namespace std;
double probability;

vector<vector<bool>> board;
void print();
void init();

void convertToLife(int i, int j);

void convertToDeath(int i, int j);
void step();
int main(){
  int n,iterations;
  cin >> n;
  cin >> iterations;
  probability = 0.35;
  board.resize(n, vector<bool>(n,false));
  init();
  print();

  for (size_t i = 0; i < iterations; i++) {
    sleep(1);
    step();
    system("clear");
    print();
  }
  return 0;
}

void print(){
  cout << "\n";
  for (size_t i = 0; i < board.size(); i++) {
    cout << "\n";

    for (size_t j = 0; j < board.size(); j++) {
      cout << "|" << board[i][j];
    }
  }
  cout << "\n";
}

void init(){
  system("clear");
  srand (time(NULL));
  #include <time.h>       /* time */

  double r = 0;
  for (size_t i = 0; i < board.size(); i++) {
    for (size_t j = 0; j < board.size(); j++) {
      r = ((double) rand() / (RAND_MAX));
      if(r<probability){
        board[i][j] = true;
      }
    }
  }
}

void step(){
  for (size_t i = 0; i < board.size(); i++) {
    for (size_t j = 0; j < board.size(); j++) {
      if(board[i][j]){
        convertToDeath(i,j);
      }else{
        convertToLife(i,j);
      }
    }

  }
}

void convertToLife(int i, int j){
  int count = 0;
  int low_i = (i-1 > 0) ? i-1: 0;
  int low_j = (j-1 > 0) ? j-1 : 0;

  int hi_i = (i+1<board.size()) ? i+1: board.size()-1;
  int hi_j = (j+1<board.size()) ? j+1: board.size()-1;
  for (size_t x = low_i; x < hi_i  ; x++) {
    for (size_t y = low_j; y < hi_j; y++) {
      if(x==y){
        continue;
      }
      if(board[x][y]){
        count+=1;
      }
    }
  }
  if(count==3){
    //cout << "Mudei para vida: " << i << j << endl;
    board[i][j]=true;
  }
}

void convertToDeath(int i, int j){
  int count = 0;
  int low_i = (i-1 > 0) ? i-1: 0;
  int low_j = (j-1 > 0) ? j-1 : 0;
  int hi_i = (i+1<board.size()) ? i+1: board.size()-1;
  int hi_j = (j+1<board.size()) ? j+1: board.size()-1;

  for (int x = low_i; x <= hi_i  ; x++) {
    for (int y = low_j; y <= hi_j; y++) {
      if(board[x][y]){
      //  cout << "Contei: " << endl;
        count+=1;
      }
    }

  }
  if(count<2 || count>3){
    //cout << "Mudei para morte: " << i << " " << j << " "<< count  <<" " << low_i << " "<< hi_i <<" " << low_j << " "<< hi_j<<endl;
    board[i][j]=false;
  }
}
