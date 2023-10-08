#include <stdio.h>
#include <stdlib.h>


int main(int argc, char* argv[]){
    double proba[11] = {1 / (double)36, 1 / (double)18, 1 / (double)12, 1 / (double)9, 5 / (double)36, 1 / (double)6, 5 / (double)36, 1 / (double)9, 1 / (double)12, 1 / (double)18, 1 / (double)36};

    char cases[40] = {'n', 'n', 'C', 'n', 'n', 'n', 'n', 'c', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'C', 'n', 'n', 'n', 'n', 'c', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'p', 'n', 'n', 'C', 'n', 'n', 'c', 'n', 'n', 'n'};

    double matrice[35][35];

    for(int i = 0; i<35; i++){
        for(int j = 0; j<35; j++){
            matrice[i][j] = 0;
        }
    }
    double proba_chance = 1/(double)7;
    double proba_chancellerie = 1/(double)3;
    int compteur_cC = 0;

    int indice_case = 0;

    for(int i = 0; i<35; i++){
        compteur_cC = 0;
        for(int j = 0; j<11; j++){
            if (cases[(indice_case + j + 2)%40] == 'c'){
                matrice[i][0] += proba_chance * proba[j];
                matrice[i][8] += proba_chance * proba[j];
                matrice[i][11] += proba_chance * proba[j];
                matrice[i][15] += proba_chance * proba[j];
                matrice[i][22] += proba_chance * proba[j];
                matrice[i][34] += proba_chance * proba[j];
                if(indice_case + j + 2 == 36){
                    matrice[i][0] += proba_chance * proba_chancellerie * proba[j];
                    matrice[i][1] += proba_chance * proba_chancellerie * proba[j];
                    matrice[i][8] += proba_chance * proba_chancellerie * proba[j];
                }
                else{
                    if ((indice_case + j + 2)%40 ==7)
                        matrice[i][3] += proba_chance * proba[j];
                    else if (indice_case + j + 2 == 22)
                        matrice[i][18] += proba_chance * proba[j];
                }
                compteur_cC++;
            }

            else if (cases[(indice_case + j + 2)%40] == 'C'){
                matrice[i][0] += proba_chancellerie * proba[j];
                matrice[i][1] += proba_chancellerie * proba[j];
                matrice[i][8] += proba_chancellerie * proba[j];
                compteur_cC++;
            }
            else if (cases[(indice_case + j + 2) % 40] == 'p' && i + j + 2 == 29)
            {
                matrice[i][8] += proba[j];
            }
            else if(i == 8){
                matrice[8][9] += 5./6;
                matrice[8][12] += 1. / 36;
                matrice[8][14] += 1. / 36;
                matrice[8][16] += 1. / 36;
                matrice[8][18] += 1. / 36;
                matrice[8][20] += 1. / 36;
                matrice[8][0] += proba_chance * 1. / 36;
                matrice[8][8] += proba_chance * 1. / 36;
                matrice[8][11] += proba_chance * 1. / 36;
                matrice[8][15] += proba_chance * 1. / 36;
                matrice[8][22] += proba_chance * 1. / 36;
                matrice[8][34] += proba_chance * 1. / 36;
                matrice[8][18] += proba_chance * 1. / 36;
                break;
            }
            else if(i == 9){
                matrice[9][10] += 5. / 6;
                matrice[9][12] += 1. / 36;
                matrice[9][14] += 1. / 36;
                matrice[9][16] += 1. / 36;
                matrice[9][18] += 1. / 36;
                matrice[9][20] += 1. / 36;
                matrice[9][0] += proba_chance * 1. / 36;
                matrice[9][8] += proba_chance * 1. / 36;
                matrice[9][11] += proba_chance * 1. / 36;
                matrice[9][15] += proba_chance * 1. / 36;
                matrice[9][22] += proba_chance * 1. / 36;
                matrice[9][34] += proba_chance * 1. / 36;
                matrice[9][18] += proba_chance * 1. / 36;
                break;
            }
            
            else if((indice_case + j + 2)%40 == 10){ 
                matrice[i][10] += proba[j];
            }
            else if((indice_case + j + 2)%40 == 11){ 
                matrice[i][11] += proba[j];
            }
            else if ((indice_case + j + 2)%40 == 12)
            {
                matrice[i][12] += proba[j];
            }

            else{
                matrice[i][(i+j+2-compteur_cC)%35] += proba[j];}
        }
        if(i==1 || i==5 || i==16 || i ==20 ||i == 27 || i == 29 || i == 31 ){
            indice_case++;
        }
        if(i==8 || i==9){
            indice_case--;
        }
        indice_case++;

    }
    double ok;
    for(int i = 0; i<35; i++){
        ok = 0;
        for(int j = 0; j<35; j++)
            ok+=matrice[i][j];
        printf("%lf\n", ok);
    }

    FILE *fscv;
    fscv = fopen("matriceQ2_1.csv", "w");
    for(int i = 0; i<35; i++){
        for(int j = 0; j<34; j++){
            fprintf(fscv,"%lf, ", matrice[i][j]);
        }
        fprintf(fscv, "%lf\n", matrice[i][34]);
    }
    fclose(fscv);



    return 0;
}