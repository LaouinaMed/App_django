#include<iostream>
using namespace std;

class pokemon{
	protected:
	int poids;
	string nom;
	public:
	pokemon(int poids,string nom){
	this->nom=nom;
	this->poids=poids;}
		
	
	
};


class poke1:public pokemon{
	protected:
	int nbrpattes;
	int taille;
	public:
	
	poke1(int nbrpattes,int taille,int poids,string nom):pokemon(poids,nom){
	this->nbrpattes=nbrpattes;
	this->taille=taille; }	
	
	};
	
	
class pokemonspo:public poke1{
   public:  
	float frequence;
	
	pokemonspo(float frequence,int taille,int poids,string nom,int nbrpattes):poke1(taille,poids,nom,nbrpattes){
	this->frequence=frequence;}	
	
	float calculvitess(){
		return nbrpattes*taille;
	}
	void tostring(){
		cout<<nom<<endl;
		cout<<poids<<endl;
		cout<<frequence<<endl;
		cout<<nbrpattes<<endl;
		cout<<taille<<endl;
	
	}
	
};

class pokemoncasa:public poke1{
    private:  
	float frequence;
	poke1(float  frequence,int nbrpattes,int taille,int poids;string nom,float frequence):poke1(poids,nom,nbrpattes,taille){
	this->frequence=frequence;
	this->taille=taille;	
         }
	float calculvitess(){
		return nbrpattes*taille;
	}
	
};	
	
	
	
	
};
class poke2:public pokemon{
	protected:
	int nbrdenag;
		poke1(int nbrdenag,string nom,int poids):pokemon(poids,nom){
	this->nbrdenag=nbrdenag;
	
	}
	
	
	
};
main(){
	pokemospo p("hhhhh",1,2,3,4);
	p.tostring;
	
}