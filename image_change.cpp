#include "cv.h"
#include "highgui.h"
#include "iostream"
#include "fstream"
#include "unistd.h"
using namespace std;

int main()
{
	ifstream in("name.txt");
static   int i=0;
	while(!in.eof())
        //for(int j=0;j<10;j++)
        {
	IplImage* Img=cvLoadImage("1.jpg");
	if(!Img)
	{
		cout<<"Img load error..."<<endl;
		exit(-1);
	}
	        char* name;
        i++;
                name=new char[256];
		in.getline(name,100);
                cout<<name<<endl;
		CvFont font;
		CvSize name_size;
		CvPoint pt;
		cvInitFont(&font, CV_FONT_HERSHEY_COMPLEX, 3.0, 1.0, 0,4, 8);
		cvGetTextSize(name,&font,&name_size,NULL);
		pt.x=1070-name_size.width/2;
		pt.y=870;
		cvPutText(Img,name,pt,&font,CV_RGB(0,0,0));
		string image_name="./data/"+string(name)+".jpg";
		cvSaveImage(image_name.c_str(),Img);
                delete name;
	cvReleaseImage(&Img);
                usleep(10000);
	}
    cout<<i<<endl;
	in.close();
	return 0;
}
