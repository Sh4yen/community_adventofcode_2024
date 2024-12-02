#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>

void readinput(std::vector<std::string> &zeilen);

int main(){

    std::vector<std::string> zeilen;
    readinput(zeilen);


    std::vector<int> left;
    std::vector<int> right;
    for(auto zeile : zeilen){
        std::stringstream ss(zeile);
        std::string left_string;
        std::string right_string;
        std::getline(ss, left_string, ' ');
        std::getline(ss, right_string, '\n');
        
        left.push_back(std::stoi(left_string));
        right.push_back(std::stoi(right_string));
    }
    sort(left.begin(), left.end());
    sort(right.begin(), right.end());


    int sum = 0;
    int sum2 = 0;   
    for(int i = 0; i < left.size(); i++){
        std::cout << left[i] << " " << right[i] << std::endl;
        if(left[i]>=right[i]){
            sum = (left[i]-right[i]) + sum;
        }else{
            sum = (right[i]-left[i]) + sum;
        }
        int mult = 0;
        for(int j = 0; j < left.size(); j++){
            if(left[i]==right[j]){
                mult++;
            }
        }
        sum2 = sum2 + left[i]*mult;
    }

    std::cout << sum << std::endl;
    std::cout << sum2 << std::endl;
    return 0;
}



void readinput(std::vector<std::string> &zeilen){

    std::string zeile;
    std::ifstream in("input");

    if(in.is_open()){
        while(std::getline(in, zeile)){
            zeilen.push_back(zeile);
        }
        in.close();
        return;
    }
    
    else{
        std::cout << "Error opening file" << std::endl;
        return;
    }
}