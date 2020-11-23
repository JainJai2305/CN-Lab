import java.util.* ;
class Node
{
    int[] dist= new int[20] ;
    int[] from= new int[20] ;
} 
class Cnl
{
    public static void main(String args[])
    {
        Scanner sc =new Scanner(System.in);
        int[][] costmat = new int[20][20] ;
        Node[] rt = new Node[10] ;
        for (int i=0;i<10;i++)
        {
            rt[i]=new Node() ;
        }
        int nodes ;
        int count =0 ;
        System.out.println("Enter the number of nodes :") ;
        nodes =sc.nextInt() ;
        System.out.println("Enter the cost matrix :") ;
        for (int i=0 ;i<nodes;i++)
        {
            for(int j=0;j<nodes;j++)
            {
                costmat[i][j]=sc.nextInt() ;
                costmat[i][i]=0 ;
                rt[i].dist[j]=costmat[i][j] ;
                rt[i].from[j]=j ;

            }
        }
        do
        {
            count=0 ;
            for(int i=0;i<nodes;i++)
            {
                for(int j=0;j<nodes;j++)
                {
                    for(int k=0;k<nodes;k++)
                    {
                        if(rt[i].dist[j]>costmat[i][k]+rt[k].dist[j])
                        {
                            rt[i].dist[j]=rt[i].dist[k]+rt[k].dist[j];
                            rt[i].from[j]=k;
                            count++;
                        }
                    }
                }
            }
        }while(count!=0) ;
        System.out.println() ;
        for(int i=0;i<nodes;i++)
        {
            System.out.println("for router: "+(i+1)) ; 
            for(int j=0;j<nodes;j++)
            {
                System.out.println("Destination "+(j+1)+" "+"Outgoing Line "+(rt[i].from[j]+1)+" "+"Hop Count "+(rt[i].dist[j])) ;
            }
            System.out.println() ;
        }
    }
}



