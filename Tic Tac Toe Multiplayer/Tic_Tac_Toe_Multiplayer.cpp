#include<iostream>
#include<windows.h>
#include<string>
using namespace std;

int inputting_for_position_filling(char a[3][3],string player,char ch)
{
    int row_choice, column_choice, c=0, i, j;
    system("cls");                                        //CLEARING THE COMMAND WINDOW FOR BETTER CLARITY
    cout<<endl;
    cout<<" "<<a[0][0]<<" | "<<a[0][1]<<" | "<<a[0][2]<<endl;  //PRINTING THE RESULTANT GAME VIEW
    cout<<" ----------"<<endl;
    cout<<" "<<a[1][0]<<" | "<<a[1][1]<<" | "<<a[1][2]<<endl;
    cout<<" ----------"<<endl;
    cout<<" "<<a[2][0]<<" | "<<a[2][1]<<" | "<<a[2][2]<<endl<<endl;
    cout<<"Player of the current turn: "<<player<<endl;
    do
    {
        row_choice = -1;
        column_choice = -1;
        while(row_choice<0 || row_choice>2)               //ACCEPTING THE ROW NUMBER
        {
            cout<<"Choose a row number (0 to 2):"<<endl;
            cin>>row_choice;
            if(row_choice<0 || row_choice>2)
                cout<<row_choice<<" is not a valid row."<<endl;
        }
        while(column_choice<0 || column_choice>2)         //ACCEPTING THE COLUMN NUMBER
        {
            cout<<"Choose a column number (0 to 2):"<<endl;
            cin>>column_choice;
            if(column_choice<0 || column_choice>2)
                cout<<column_choice<<" is not a valid column."<<endl;
        }
    }while(a[row_choice][column_choice]!='.');            //CHECKING IF ROW AND COLUMN IS NOT OCCUPIED
    a[row_choice][column_choice] = ch;                    //ALLOCATING THE POSITION WITH THE PLAYER'S SYMBOL
    if(c!=1)                                              //CHECKING FOR STRAIGHT LINE PATTERN
    {
        for(i=0;i<3;i++)
        {
            if((a[i][0]==ch && a[i][1]==ch && a[i][2]==ch) || (a[0][i]==ch && a[1][i]==ch && a[2][i]==ch))
                c=1;
        }
        if(c!=1)
        {
            if(a[0][0]==ch && a[1][1]==ch && a[2][2]==ch)
                c=1;
            if(c!=1)
                if(a[2][0]==ch && a[1][1]==ch && a[0][2]==ch)
                    c=1;
        }
    }
    return c;                                             //RETURNING THE RESULT ABOUT STRAIGHT LINE PATTERN
}

int check_for_playing_again()
{
    char ans='M';
    while(ans!='Y' && ans!='N')
    {
        cout<<"Would you like to play again? (Y/N)"<<endl;
        cin>>ans;
        ans = toupper(ans);
        cin.ignore();
        if(ans=='Y' || ans=='N')
        {
            if(ans=='Y')
            {
                return 1;
            }
            else if(ans=='N')
            {
                cout<<"Bye!"<<endl;
                return 0;
            }
        }
        else if(ans!='Y' && ans!='N')
            cout<<ans<<" is not a valid answer."<<endl;
    }
}

void print(char a[3][3])
{
    system("cls");                                        //CLEARING THE SCREEN
    cout<<endl;
    cout<<" "<<a[0][0]<<" | "<<a[0][1]<<" | "<<a[0][2]<<endl;
    cout<<" ----------"<<endl;
    cout<<" "<<a[1][0]<<" | "<<a[1][1]<<" | "<<a[1][2]<<endl;
    cout<<" ----------"<<endl;
    cout<<" "<<a[2][0]<<" | "<<a[2][1]<<" | "<<a[2][2]<<endl<<endl;
}

int check_draw(char a[3][3])                              //TO CHECK IF THERE IS A DRAW
{
    int i,j,c=0;
    for(i=0;i<3;i++)
        for(j=0;j<3;j++)
            if(a[i][j]=='X' || a[i][j]=='O')
                c++;
    return c;
}



int main()
{
    bool play = 1;
    //NOW THE GAME STARTS
    while(play==1)   //WILL CONTINUE IF PLAY = 1, IF PLAY = 0 IT WILL TERMINATE
    {
        system("cls");                                    //CLEARING THE SCREEN
        int c=0, m=0, row_choice, column_choice;
        char a[3][3]={'.','.','.','.','.','.','.','.','.'};
        string x_player="", y_player="", first="";

        cout<<endl<<"Enter a name for the X-player:"<<endl;
        getline(cin,x_player);
        cout<<"Enter a name for the Y-player:"<<endl;
        getline(cin,y_player);

        while(first!=x_player && first!=y_player)
        {
            first="";
            cout<<"Who plays first, "<<x_player<<" or "<<y_player<<" ?"<<endl;
            getline(cin,first);
            if(first!=x_player || first!=y_player)
                cout<<first<<" is not a registered player."<<endl;
        }

        c = (first==x_player) ? -1 : 0;
        while(m!=1)                               //CHECKING CONTINUITY OF GAME
        {
            c++;
            if(c%2==0)                            //CHECKING IF THE TURN IS OF PLAYER X
                m = inputting_for_position_filling(a,x_player,'X');
            else if(c%2==1)                       //CHECKING IF THE TURN IS OF PLAYER Y
                m = inputting_for_position_filling(a,y_player,'O');
            if(m==1 && c%2==0)                   //CHECKING IF PLAYER X HAS WON THE GAME
            {
                print(a);
                cout<<"Game is over:"<<endl<<x_player<<" wins!"<<endl;
                play = check_for_playing_again();
            }
            else if(m==1 && c%2==1)              //CHECKING IF PLAYER Y HAS WON THE GAME
            {
                print(a);
                cout<<"Game is over:"<<endl<<y_player<<" wins!"<<endl;
                play = check_for_playing_again();
            }
            else if(check_draw(a)==9 && m!=1)    //CHECKING IF THE GAME IS DRAW
            {
                print(a);
                cout<<"Game is over:"<<endl<<"it is a tie!"<<endl;
                m=1;
                play = check_for_playing_again();
            }
        }
    }
    return 0;
}
