// x o game
#include<iostream>
#include<iomanip>
#include<ctime>
#include<cmath>
void drawboard(char *s);
void playermove(char*s,char p);
void compmove(char*s,char c);
bool checkwinner(char*s,char p,char c);
bool checktie(char*s);
int main(){
    char spaces[9]={' ',' ',' ',' ',' ',' ',' ',' ',' '};
    char  player='x';
    char  comp='o';
    bool running =true;
    drawboard(spaces);
    while (running){
        playermove(spaces , player);
        drawboard(spaces);
        if(checkwinner(spaces , player, comp)){running=false;break;}
        else if(checktie(spaces)){running=false;break;}
        //
        compmove(spaces , comp);
        drawboard(spaces);
        if(checkwinner(spaces , player , comp)){running=false;break;}
        else if(checktie(spaces)){running=false;break;}}
    return 0;
    }
void drawboard(char *s){
    std::cout<<"     |     |     "<<'\n';
    std::cout<<"   "<<s[0]<<" | "<<s[1]<<"   | "<<s[2]<<'\n';
    std::cout<<"_____|_____|_____"<<'\n';
    std::cout<<"     |     |     "<<'\n';
    std::cout<<"   "<<s[3]<<" | "<<s[4]<<"   | "<<s[5]<<'\n';
    std::cout<<"_____|_____|_____"<<'\n';
    std::cout<<"     |     |     "<<'\n';
    std::cout<<"   "<<s[6]<<" | "<<s[7]<<"   | "<<s[8]<<'\n';
    std::cout<<"_____|_____|_____"<<'\n';
    std::cout<<"     |     |     "<<'\n';
    std::cout<<"*************************************************"<<'\n';
    // return 0;
}
void playermove(char*s,char p){
    int num;
    do{
        std::cout<<"wright number of grid from 1 to 9: ";
        std::cin>>num;
        num--;
        if(s[num]==' '){s[num]=p;break;}
    }while(!num>0 |!num<8 );
}
void compmove(char*s,char c){
    srand(time(0));
    while(true){
        int n=rand() % 9;
        if(s[n]==' '){s[n]=c;break;}
    }
}
bool checkwinner(char*s,char p,char c){
    bool test =false;
    for(int i=0;i<9;i++){
        if(s[i]!=' '&&s[i]==s[i+1]&&s[i]==s[i+2]&&i<=6){test=true;break;}
        else if(s[i]!=' '&&s[i]==s[i+3]&&s[i]==s[i+6]&&i<=2){test=true;break;}
        else if(s[i]!=' '&&s[i]==s[i+4]&&s[i]==s[i+8]&&i==0){test=true;break;}
        else if(s[i]!=' '&&s[i]==s[i+2]&&s[i]==s[i+4]&&i==2){test=true;break;}
        else{return false;}}
    if (test=true){std::cout<<"you win \n";}else{std::cout<<"you lose \n";}
}
bool checktie(char*s){
    for(int i=0;i<9;i++){
        if(s[i]==' '){return false;}}
    std::cout<<"it is tei \n";
    return true;}