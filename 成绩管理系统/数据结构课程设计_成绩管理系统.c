#include<stdio.h>
#include<stdlib.h> 
#include<string.h>


FILE *fp;
struct student	//定义学生这个结构体 
{
	char name[6];
	int num;
	long int chi;
	long int math;
	long int eng;
	long int sum;
	
};

struct student  stu1[100],stu2[100],stu3[100],stu4[100],t,tmp;


void get_info1()	//获取1.txt文件中学生的信息 
{
	int i;
	for(i=1; i<=5; i++)
	{
		fscanf(fp,"%s%d%d%d%d", stu1[i].name, &stu1[i].num, &stu1[i].chi, &stu1[i].math, &stu1[i].eng);
	}
	printf("\n1.txt中学生的成绩如下：\n");
	printf("姓名\t学号\t语文\t数学\t英语\n");
	for(i=1; i<=5; i++)
	{
		printf("%s\t%d\t%d\t%d\t%d\n", stu1[i].name, stu1[i].num, stu1[i].chi, stu1[i].math, stu1[i].eng);
	}
	
}


void get_info2()	//获取2.txt文件中学生的信息 
{
	int j;
	for(j=1; j<=5; j++)
	{
		fscanf(fp,"%s%d%d%d%d", stu2[j].name, &stu2[j].num, &stu2[j].chi, &stu2[j].math, &stu2[j].eng);
	}
	
	printf("\n2.txt中学生的成绩如下：\n");
	printf("姓名\t学号\t语文\t数学\t英语\n");
	
	for(j=1; j<=5; j++)
	{
		printf("%s\t%d\t%d\t%d\t%d\n", stu2[j].name, stu2[j].num, stu2[j].chi, stu2[j].math, stu2[j].eng);
	}
	
}

void merge_txt()	//合并1.txt和2.txt文件中的学生信息
{
	int i;
	for(i=1; i<=5; i++)
	{
		stu3[i] = stu1[i];
	}
	
	for(i=6; i<=10; i++)
	{
		stu3[i] = stu2[i-5];
	}
	printf("\n3.txt中的所有学生的成绩名单；\n");
	printf("姓名\t学号\t语文\t数学\t英语\t总分\n");
	for(i=1;i<=10;i++)
	{
		stu3[i].sum = stu3[i].math+stu3[i].eng+stu3[i].chi;
		printf("%s\t%d\t%d\t%d\t%d\t%d\n", stu3[i].name, stu3[i].num, stu3[i].chi, stu3[i].math, stu3[i].eng, stu3[i].sum);
		fscanf(fp,"%s%d%d%d%d\n", &stu3[i].name, &stu3[i].num, &stu3[i].chi, &stu3[i].math, &stu3[i].eng, &stu3[i].sum);
	}
	
	
}

int extract()	//获取3.txt中所有学生中要补考的学生信息，并存入4.txt文件中 
{
	int i,j;
	j = 1;
	for(i=1;i<=10;i++)
	{
		if(stu3[i].math<60||stu3[i].eng<60||stu3[i].chi<60)
		{
			stu4[j] = stu3[i];
			j++;
		}
	}
	printf("\n补考学生成绩名单如下：\n");
	printf("姓名\t学号\t语文\t数学\t英语\n");

	for(i=1;i<j;i++)
	{	printf("%s\t%d\t%d\t%d\t%d\t\n", stu4[i].name, stu4[i].num, stu4[i].chi, stu4[i].math, stu4[i].eng);
		fprintf(fp,"%s\t%d\t%d\t%d\t%d\n",stu4[i].name, stu4[i].num, stu4[i].chi, stu4[i].math, stu4[i].eng);
	}
	return 0;
}


void bubble_sort()	//采用冒泡排序给学生总成绩排名 
{	
	int i,j;
	for(i=1;i<=10;i++)
	{
		for(j=i+1;j<=10;j++)
		{
			if(stu3[j].sum>stu3[i].sum)
			{
				tmp = stu3[j];
				stu3[j]= stu3[i];
				stu3[i]= tmp;
			}
		}
	}
	printf("\n按总分由高到低排序（冒泡）后的成绩如下：\n");
	printf("姓名\t学号\t语文\t数学\t英语\t总分\n");
	for(i=1;i<=10;i++)
	printf("%s\t%d\t%d\t%d\t%d\t%d\n",stu3[i].name, stu3[i].num, stu3[i].chi,stu3[i].math, stu3[i].eng, stu3[i].sum);
}



void insert_sort()	////采用插入排序给学生总成绩排名  
{
	int i,j;
	for(i=2;i<=10;i++)
	{
		if(stu3[i].sum>stu3[i-1].sum)
		{
			stu3[0]= stu3[i];
			stu3[i]= stu3[i-1];
			for(j= i-2; stu3[0].sum>stu3[j].sum;j--)
			stu3[j+1]= stu3[j];
			stu3[j+1]= stu3[0];
		}
	}
	printf("\n按总分由高到低排序（插入）后的成绩如下：\n");
	printf("姓名\t学号\t语文\t数学\t英语\t总分\n");
	for(i=1;i<=10;i++)
	printf("%s\t%d\t%d\t%d\t%d\t%d\n", stu3[i].name, stu3[i].num, stu3[i].chi, stu3[i].math, stu3[i].eng, stu3[i].sum);
}


void  _clear()	//清除输入缓冲区 
{
	char c_tmp;
	while((c_tmp = getchar()!='\n')&&c_tmp!=EOF);
}


void sequence_search()	//采用顺序查找查找学生信息 
{
	int i;
	char fname[6];
	printf("\n请输入要查找学生的姓名：");
	
	scanf("%s",&fname);
	_clear();
	for(i=1;i<=10;i++)
	{
		if(!strcmp(stu3[i].name,fname))
		{
			printf("\n你所查找（名字顺序）的学生成绩如下：\n");
			printf("姓名\t学号\t语文\t数学\t英语\t总分\n");
			printf("%s\t%d\t%d\t%d\t%d\t%d\n",stu3[i].name, stu3[i].num, stu3[i].chi, stu3[i].math, stu3[i].eng, stu3[i].sum);
			return ;
		}
		
	}
	
	printf("没有查询到%s的相关信息\n",fname); 
	
}

void  binary_search()	//采用折半查找查找学生信息
{
	char fname[6];
	int mid,low=1;
	int high =10;
	int i,j;
	for(i=1;i<=10;i++)
	{
		for(j=i+1;j<=10;j++)
		{
			if(strcmp(stu3[j].name,stu3[i].name)>0)
			{
				t = stu3[j];
				stu3[j]= stu3[i];
				stu3[i]= t;
			}
		}
	}
	printf("\n按名字由高到低排序（冒泡）后的成绩如下：\n");
	printf("姓名\t学号\t语文\t数学\t英语\t总分\n");
	for(i=1;i<=10;i++)
	printf("%s\t%d\t%d\t%d\t%d\t%d\n",stu3[i].name, stu3[i].num, stu3[i].chi,stu3[i].math, stu3[i].eng, stu3[i].sum);
	printf("\n请输入要查找的学生的姓名：");
	scanf("%s",&fname);
	_clear();
	while(low<=high)
	{
		mid = (low+high)/2;
		if(strcmp(stu3[mid].name,fname)==0) 
		break;
		else  if(strcmp(fname,stu3[mid].name)>0)
		high = mid-1;
		else
		low = mid+1;
	}
	if(strcmp(fname,stu3[mid].name) == 0)
	{
		printf("\n你所查找（名字折半）的学生成绩如下：\n");
		printf("姓名\t学号\t语文\t数学\t英语\t总分\n");
		printf("%s\t%d\t%d\t%d\t%d\t%d\n", stu3[mid].name, stu3[mid].num, stu3[mid].chi, stu3[mid].math, stu3[mid].eng, stu3[mid].sum);
	
	}
	else
		printf("没有查询到%s的相关信息\n",fname);
		
}


void show_menu()	//显示选择菜单选项 
{ 
	char digit;
	printf("\n\n**************************欢迎使用邵阳学院成绩管理系统*********************\n");
	printf("--------------------------------*系统功能菜单*-----------------------------\n");
	printf("___________________________________________________________________________\n");
	printf("|                                     |                                   |\n");
	printf("|      *1.读取3.txt的成绩（合并）     |      **2.读取4.txt的成绩（补考）  |\n");
	printf("|_____________________________________|___________________________________|\n");
	printf("|                                     |                                   |\n");
	printf("|      *3.按总分排序（冒泡）          |      **4.按总分排序（插入）       |\n");
	printf("|_____________________________________|___________________________________|\n");
	printf("|                                     |                                   |\n");
	printf("|      *5.按名字查找（顺序）          |      **6.按名字查找（折半）       |\n");
	printf("|_____________________________________|___________________________________|\n");
	printf("|                                                                         |\n");
	printf("|                               *7.退出系统                               |\n");
	printf("|_________________________________________________________________________|\n");
	printf("|-------------------------------------------------------------------------|\n");
	printf("请选择菜单编号：");
	
 } 
 
 
 void swich_choice()	//菜单选项对应的操作函数 
 {
 	char choice; 
 	scanf("%c",&choice);
	_clear();
 	switch(choice)
	{
		case '1':
			fp = fopen("e:\\1.txt","r+");
			get_info1();
			fclose(fp);
			fp = fopen("e:\\2.txt","r+");
			get_info2();
			fclose(fp);
			fp = fopen("e:\\3.txt","w");
			merge_txt();
			fclose(fp);
			break;
		case '2':
			fp = fopen("e:\\1.txt","r+");
			get_info1();
			fclose(fp);
			fp = fopen("e:\\2.txt","r+");
			get_info2();
			fclose(fp);
			fp = fopen("e:\\3.txt","w");
			merge_txt();
			fclose(fp);
			fp = fopen("e:\\4.txt","w");
			extract();
			fclose(fp);
			break;
		case '3':
			fp = fopen("e:\\1.txt","r+");
			get_info1();
			fclose(fp);
			fp = fopen("e:\\2.txt","r+");
			get_info2();
			fclose(fp) ;
			fp = fopen("e:\\3.txt","w");
			merge_txt();
			fclose(fp);
			bubble_sort();
			break;
		case '4':
			fp = fopen("e:\\1.txt","r+");
			get_info1();
			fclose(fp);
			fp = fopen("e:\\2.txt","r+");
			get_info2();
			fclose(fp) ;
			fp = fopen("e:\\3.txt","w");
			merge_txt();
			fclose(fp);
			insert_sort();
			break;
		case '5':
			fp = fopen("e:\\1.txt","r+");
			get_info1();
			fclose(fp);
			fp = fopen("e:\\2.txt","r+");
			get_info2();
			fclose(fp) ;
			fp = fopen("e:\\3.txt","w");
			merge_txt();
			fclose(fp);
			sequence_search();
			break;
		case '6':
			fp = fopen("e:\\1.txt","r+");
			get_info1();
			fclose(fp);
			fp = fopen("e:\\2.txt","r+");
			get_info2();
			fclose(fp) ;
			fp = fopen("e:\\3.txt","w");
			merge_txt();
			fclose(fp);
			binary_search();
			break;
		case '7':
			exit(0);
		default:
			printf("\a输入选项有误请输入1-7的菜单选项！！！！\n");	//非法输入会产生提示音提示语 
			break;
 	}
}
 
 
int main()
{	
	while(1)
	{
		show_menu();
		swich_choice();	
		_clear();
	
	}
	
return 0;
	
}
